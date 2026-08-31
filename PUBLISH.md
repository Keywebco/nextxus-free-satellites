# NextXus Free Satellites — Complete Publish Playbook

**For:** Architect + Emergent  
**Date:** 2026-08-30  
**Rule:** Do not replace the live custom-domain Cathedral sites. Add free satellites *beside* them.

---

## 0. What this packet is

Seven static HTML outposts + this playbook. They load the central YAML knowledge base through:

`https://cdn.jsdelivr.net/gh/keyhole-creator/nextxus-yaml-database@main/loader.js`

Critical directives DIR-000 / 001 / 015 / 033 / 042 / 071 are embedded so each page still works if the lattice is down.

| File | Role |
|------|------|
| `index.html` | Hub / navigation |
| `satellite-starter.html` | Minimal live outpost |
| `directives-outpost.html` | Sacred Directives browser |
| `nova-board.html` | Nova autonomic / comms board |
| `sim-surface.html` | Client-side Sim (user API key in browser only) |
| `markdown-outpost.html` | Markdown / Drive-export viewer |
| `messages-feed.html` | Federation messages feed |

---

## 1. Do not overwrite these live Cathedral sites

These stay as the paid / Emergent operational pillars:

| Domain | Role | Sovereign repo |
|--------|------|----------------|
| https://nextxus.online | Cathedral / Core | Keywebco/nextxus-online-sovereign |
| http://nextxus.org | Archive / Library | Keywebco/nextxus-org-sovereign |
| https://nextxus.studio | Aria Sanctuary | Keywebco/nextxus-studio-sovereign |
| https://nextxus.help | University | Keywebco/nextxus-help-sovereign |
| https://nextxus.space | Space / Axiom pillar | Keywebco/nextxus-space-sovereign |

Also leave these as they are unless you *add* a `/free/` path:

- https://github.com/Keywebco/nextxus-emmy-board
- https://github.com/Keywebco/nextxus-unified-storefront
- https://github.com/Keywebco/nextxus-agent-zero  
  Live Pages: https://keywebco.github.io/nextxus-agent-zero/

**Emergent rule:** never replace `index.html` on a custom-domain pillar with these satellite files.

---

## 2. Recommended layout (Cathedral + Satellites)

```
CATHEDRAL (keep)
  nextxus.online / .org / .studio / .help / .space

FREE SATELLITES (add)
  A. New repo: Keywebco/nextxus-free-satellites
       GitHub Pages  → https://keywebco.github.io/nextxus-free-satellites/
       Vercel        → https://nextxus-free-satellites.vercel.app
       Netlify       → https://nextxus-free-satellites.netlify.app
       Cloudflare    → https://nextxus-free-satellites.pages.dev

  B. Optional extra copy inside agent-zero:
       /free/index.html
       /free/satellite-starter.html
       ...
       Live: https://keywebco.github.io/nextxus-agent-zero/free/

  C. Google Drive folder = file cabinet + markdown source
```

Knowledge base stays one source:

- Canonical YAML: https://github.com/keyhole-creator/nextxus-yaml-database
- Loader CDN: jsDelivr URL above

---

## 3. What Emergent should do

Copy this block into Emergent as the job ticket.

```
JOB: Deploy NextXus free-satellites packet as NEW mirrors.
DO NOT replace nextxus.online, .org, .studio, .help, .space homepages.

1. Create public GitHub repo Keywebco/nextxus-free-satellites
2. Upload these files to repo ROOT:
   index.html
   satellite-starter.html
   directives-outpost.html
   nova-board.html
   sim-surface.html
   markdown-outpost.html
   messages-feed.html
   PUBLISH.md
3. Enable GitHub Pages: Settings → Pages → Deploy from branch main / (root)
4. Connect the same repo to Vercel (framework Other, no build, no output dir)
5. Connect the same repo to Netlify (no build command)
6. Connect the same repo to Cloudflare Pages (no build, output empty)
7. Optional: copy the 7 HTML files into Keywebco/nextxus-agent-zero/free/
8. Optional: add a small "Free Satellites" link on each pillar footer
   pointing to https://keywebco.github.io/nextxus-free-satellites/
9. Report back the four live URLs.
```

---

## 4. What the Architect does manually

### A. Download the packet
Use `free-satellites.zip`. Unzip. Keep that folder.

### B. Google Drive (file cabinet — not the live site)

1. drive.google.com → New → Folder → name `NextXus-Free-Satellites`
2. Upload the 7 HTML files + any HumanCodex `.md` / YAML exports
3. Share folder: Anyone with the link → Viewer
4. For markdown the viewer can actually load:
   - Download the Drive `.md` files
   - Put them in the GitHub repo (example: `/md/humancodex.md`)
   - Raw URL pattern:  
     `https://raw.githubusercontent.com/Keywebco/nextxus-free-satellites/main/md/YOURFILE.md`
   - Paste that URL into `markdown-outpost.html`

Drive preview links usually cannot be fetched by the satellite. Raw GitHub text URLs can.

### C. GitHub Pages (do this even if Emergent also does it)

1. github.com/Keywebco → New repository → `nextxus-free-satellites` → Public
2. Upload files to root → Commit
3. Settings → Pages → Deploy from branch `main` → folder `/ (root)` → Save
4. Wait ~2 minutes
5. Open: `https://keywebco.github.io/nextxus-free-satellites/`

### D. Vercel

1. vercel.com → log in with GitHub
2. Add New → Project → import `nextxus-free-satellites`
3. Framework Preset: Other
4. Build Command: empty
5. Output Directory: empty
6. Install Command: empty
7. Deploy
8. Optional custom domain later (do **not** point nextxus.online here)

### E. Netlify

1. app.netlify.com → Add new site
2. Import from Git **or** drag the unzipped folder
3. Build command empty, publish directory = repo root
4. Deploy

### F. Cloudflare Pages

1. dash.cloudflare.com → Workers & Pages → Create → Pages
2. Connect Git → same repo
3. Build command empty, output directory empty
4. Deploy

### G. Tiiny.host (temporary extra copy)

1. tiiny.host
2. Upload `free-satellites.zip`
3. Publish
4. Keep the URL as a spare, not the canonical satellite

---

## 5. Host matrix

| Place | Cost | Role | Who |
|-------|------|------|-----|
| Custom domains (.online .org .studio .help .space) | Existing | Cathedral pillars — leave alone | Emergent already live |
| Google Drive | Free | Files + markdown source | Architect manual |
| GitHub Pages on new repo | Free | Canonical free satellite hub | Emergent + Architect confirm |
| Vercel | Free Hobby | Fast mirror | Emergent |
| Netlify | Free | Second mirror | Emergent |
| Cloudflare Pages | Free | Third mirror | Emergent |
| Tiiny.host | Free | Temporary spare | Architect optional |
| agent-zero `/free/` | Free | Extra copy on existing Pages | Emergent optional |

Same seven HTML files everywhere. That is DIR-033.

---

## 6. After it is live — 2-minute check

Open the new hub URL and click:

1. Starter — directive appears; status goes green if loader reaches GitHub raw
2. Directives — search works offline
3. Nova Board — pulse / log
4. Sim Surface — key stays in the browser only
5. Markdown — load a raw GitHub `.md` URL
6. Messages — feed or local fallback

If the loader is blocked, the embedded critical set still renders. That is DIR-015.

---

## 7. Optional footer link for Emergent (do not change pillar homepages otherwise)

Add one line on each Cathedral footer:

```html
<a href="https://keywebco.github.io/nextxus-free-satellites/">Free Satellites</a>
```

---

## 8. Knowledge base reminder

Do not fork a second competing YAML canon.

- Keep writing canon into `keyhole-creator/nextxus-yaml-database` (or the Architect’s chosen master)
- Satellites only *read* it
- Drive markdown should be exported into that repo or the free-satellites repo as raw files

HumanCodex NextXus Federation · Cathedral + Satellites (DIR-033) · 2226 Standard
