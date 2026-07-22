# Praveen Kumar — Portfolio Website

A futuristic, fully responsive personal portfolio website built with pure HTML, CSS, and JavaScript.

🔗 **Live:** [Deploy to GitHub Pages / Netlify / Vercel]

---

## ✨ Features

- **Futuristic cyber design** — dark theme with cyan, purple, and green neon accents
- **Custom SVG cursor** — animated arrow cursor with glow effect
- **Typing animation** — hero section cycles through roles
- **Live GitHub repos** — "View All Repositories" modal fetches your repos live via GitHub API
- **Animated stats counter** — numbers count up on scroll
- **Skill proficiency bars** — animated on scroll
- **Scroll reveal animations** — staggered fade-in on all sections
- **Hamburger nav** — full-screen drawer for mobile
- **Bottom sheet modal** — mobile-native feel for repo viewer
- **Resume link** — opens directly in Google Drive
- **Fully responsive** — desktop, tablet, and mobile optimized

---

## 📁 Project Structure

```
portfolio/
├── index.html          # Main portfolio file (everything is here)
├── Praveen-resume.pdf  # Resume PDF (kept as backup)
└── README.md           # This file
```

---

## 🚀 Deployment

### GitHub Pages (Recommended — Free)

1. Create a new GitHub repository named `username.github.io` (e.g. `Pxrvn07.github.io`)
2. Upload `index.html` and `Praveen-resume.pdf` to the repo
3. Go to **Settings → Pages → Source → main branch**
4. Your site will be live at `https://Pxrvn07.github.io`


### Vercel

1. Go to [vercel.com](https://vercel.com) and sign up
2. Import your GitHub repo or drag & drop
3. Done — live instantly

---

## ✏️ Customization Guide

### Update your name / bio
Edit the hero section in `index.html`:
```html
<h1 class="hero-name">Praveen<br>Kumar</h1>
<p class="hero-desc">Your bio here...</p>
```

### Update resume link
Find the View Resume button and replace the `href`:
```html
<a href="YOUR_GOOGLE_DRIVE_LINK" ...>↗ View Resume</a>
```

### Update social links
Search for these in `index.html` and replace with your URLs:
- `https://github.com/Pxrvn07`
- `https://www.linkedin.com/in/pxrvn`
- `https://x.com/Praveen__06`
- `https://www.instagram.com/pxrvn._06/`

### Add a new project card
Copy an existing `.project-card` block and update the content:
```html
<div class="project-card reveal">
  <span class="project-icon">🚀</span>
  <div class="project-num">05</div>
  <h3 class="project-name">Your Project Name</h3>
  <p class="project-desc">Your project description...</p>
  <div class="project-tags">
    <span class="tag lang">React</span>
    <span class="tag">Your Tag</span>
  </div>
  <div class="project-links">
    <a href="https://github.com/Pxrvn07/your-repo" target="_blank" class="project-link">↗ View Project</a>
  </div>
</div>
```

### Update skill bars
Find `.skill-bar-fill` elements and change `data-width`:
```html
<div class="skill-bar-fill fill-cyan" style="width:0%" data-width="90%"></div>
```

### Change accent colors
Edit CSS variables at the top of `index.html`:
```css
:root {
  --accent: #00c8ff;   /* cyan */
  --accent2: #7b2fff;  /* purple */
  --accent3: #00ff9d;  /* green */
}
```

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| HTML5 | Structure |
| CSS3 | Styling, animations, responsive design |
| Vanilla JavaScript | Interactivity, GitHub API, animations |
| GitHub REST API | Live repo fetching in modal |
| Google Fonts | Syne + JetBrains Mono |
| Google Drive | Resume hosting |

---

## 📱 Responsive Breakpoints

| Breakpoint | Target |
|---|---|
| > 960px | Desktop |
| ≤ 960px | Tablet |
| ≤ 600px | Mobile |
| ≤ 380px | Small phones |

---

## 📄 Sections

| Section | Description |
|---|---|
| **Hero** | Name, typing animation, resume + GitHub CTA |
| **Stats** | Animated counters — repos, projects, domains |
| **Projects** | 4 pinned projects with tags and links |
| **All Repos** | Modal with live GitHub API fetch |
| **Skills** | Tech stack chips + animated proficiency bars |
| **About** | Bio, profile card, social links |
| **Contact** | Social links + terminal widget |

---

## 🔗 Links

- GitHub: [github.com/Pxrvn07](https://github.com/Pxrvn07)
- LinkedIn: [linkedin.com/in/pxrvn](https://www.linkedin.com/in/pxrvn)
- Twitter/X: [@Praveen__06](https://x.com/Praveen__06)
- Instagram: [@pxrvn._06](https://www.instagram.com/pxrvn._06/)

---

© 2025 Praveen Kumar
