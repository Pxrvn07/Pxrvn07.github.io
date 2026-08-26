#!/usr/bin/env python3
"""Scrape the public Codolio card page and write assets/codolio.json.

Codolio has no public CORS-enabled API, so the browser can't read it directly.
This runs in CI on a schedule instead, committing fresh numbers to the repo.
"""

import datetime
import json
import os
import re
import sys
import urllib.request

SLUG = os.environ.get("CODOLIO_SLUG", "pxrvn")
URL = f"https://codolio.com/profile/{SLUG}/card"
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "codolio.json")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"


def fetch(url):
    # CODOLIO_FIXTURE lets you exercise the parser against a saved page offline.
    fixture = os.environ.get("CODOLIO_FIXTURE")
    if fixture:
        with open(fixture, encoding="utf-8", errors="replace") as f:
            return f.read()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def grab_object(text, key):
    """Return the JSON object that follows "key": in text."""
    i = text.find(f'"{key}":')
    if i == -1:
        return None
    i = text.index("{", i)
    depth, in_str, esc = 0, False, False
    for j in range(i, len(text)):
        c = text[j]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
            continue
        if c == '"':
            in_str = True
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(text[i:j + 1])
                except json.JSONDecodeError:
                    return None
    return None


def scalar(text, key, cast=str):
    m = re.search(r'"%s":\s*("(?:[^"\\]|\\.)*"|true|false|null|-?\d+(?:\.\d+)?)' % re.escape(key), text)
    if not m:
        return None
    val = json.loads(m.group(1))
    if val is None:
        return None
    return cast(val) if cast is not str or isinstance(val, str) else val


def main():
    raw = fetch(URL)
    # The Next.js RSC payload embeds JSON with escaped quotes; normalise it.
    text = raw.replace('\\"', '"')

    card = grab_object(text, "codolioCardDetails") or {}
    gh = grab_object(text, "githubProfileDetails") or {}
    profile_map = grab_object(text, "profileMap") or {}

    if not card.get("totalQuestionsSolved"):
        sys.exit("could not find codolioCardDetails on the page — layout may have changed")

    first = scalar(text, "firstName") or ""
    second = scalar(text, "secondName") or ""

    data = {
        "slug": SLUG,
        "name": " ".join(p for p in (first, second) if p).strip(),
        "verified": bool(scalar(text, "isVerified")),
        "avatar": scalar(text, "imageUrl") or "",
        "questionsSolved": int(card.get("totalQuestionsSolved") or 0),
        "activeDays": int(card.get("totalActiveDays") or 0),
        "tags": card.get("problemSolvingTags") or [],
        "platforms": sorted(k for k, v in profile_map.items() if v),
        "github": {
            "handle": gh.get("githubProfile") or "",
            "stars": int(gh.get("stars") or 0),
            "contributions": int(gh.get("totalContributions") or 0),
            "commits": int(gh.get("commitCounts") or 0),
        },
        "profileUrl": f"https://codolio.com/profile/{SLUG}",
    }

    path = os.path.abspath(OUT)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Reuse the previous timestamp when nothing substantive moved, so the
    # scheduled job doesn't commit a no-op diff every six hours.
    previous = {}
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as f:
                previous = json.load(f)
        except (json.JSONDecodeError, OSError):
            previous = {}

    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    unchanged = {k: v for k, v in previous.items() if k != "updatedAt"} == data
    data["updatedAt"] = previous.get("updatedAt") or now if unchanged else now
    if unchanged:
        print("unchanged")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
