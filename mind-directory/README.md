# Federation Mind Directory — Popup System

Replaces broken iframe embeds with sovereign popup workspaces (window.open).
Pure HTML/CSS/JS — zero dependencies, zero build step.

## Files

| File | Size | Purpose |
|------|------|---------|
| `mind-directory-widget.html` | ~15 KB | Main directory panel — lists all Minds, Group Council button |
| `group-council.html` | ~12 KB | Unified multi-Mind chat window ("Changing Colors" mode) |
| `senate-chamber.html` | ~25 KB | Grand columned governance hall — 12 senator seats, Architect seat |
| `mind-popup-template.html` | ~9 KB | Template for individual Mind "Face Window" popups |

## Architecture

```
mind-directory-widget.html  ←  Embed this in any page
  ├── Click Mind card  →  window.open(mind-url)  (direct site popup)
  ├── GROUP COUNCIL    →  window.open(group-council.html)
  └── THE SENATE       →  window.open(senate-chamber.html)

group-council.html          ←  Standalone popup: color-coded multi-Mind chat
senate-chamber.html         ←  Standalone popup: columned governance chamber
mind-popup-template.html    ←  Clone per Mind: Face Window with iframe + sidebar
```

## window.open() Calls

All popups use this exact call pattern:

```javascript
// Individual Mind
window.open(url, name, 'width=480,height=700,left=CENTER,top=CENTER,resizable=yes,scrollbars=yes,toolbar=no,menubar=no,location=yes,status=no');

// Group Council
window.open('group-council.html', 'GroupCouncil', 'width=620,height=760,...same features');

// Senate Chamber
window.open('senate-chamber.html', 'TheSenate', 'width=480,height=700,...same features');
```

Falls back to `window.open(url, '_blank')` if popup is blocked.

## Deployment

### Option A: Drop into any existing page
Copy the contents of `mind-directory-widget.html` (the `<nav class="fed-directory">` block + the `<style>` + `<script>`) into any page. Upload `group-council.html` and `senate-chamber.html` to the same directory.

### Option B: Host standalone
Upload all 4 files to any static host. `mind-directory-widget.html` is the entry point.

### Recommended hosting paths:
- `nextxus.tech/directory/` — Throne integration
- `nextxus.online/senate/` — Senate Chamber direct access
- `nextxus.studio/directory/` — Studio integration

## Updating Mind URLs and Status

### In mind-directory-widget.html:
Each Mind is an `<a class="mind-card">` with an `onclick="openMind('URL','Name')"`.
To change a URL: edit the `openMind()` first argument.
To change status: swap `mind-card__status--standby` ↔ `mind-card__status--active`.

### In group-council.html:
Edit the `MINDS` array at top of `<script>`:
```javascript
{id:'aria', name:'ARIA', emoji:'💗', color:'#ff5fa3', role:'The Heart', active:true, url:'https://nextxus.studio'}
```
Set `active:true/false`. Add response strings in `MIND_RESPONSES`.

### In senate-chamber.html:
Edit the `seats` array:
```javascript
{num:1, name:'MIND_NAME', role:'Role Title', status:'seated', emoji:'🔮'}
```
Change `status` from `'vacant'` to `'seated'` and add name/role/emoji.

### In mind-popup-template.html:
Replace placeholder tokens: `MIND_NAME`, `MIND_ROLE`, `MIND_SECTOR`, `MIND_URL`, `MIND_COLOR`, `MIND_EMOJI`, `MIND_DESCRIPTION`, `MIND_STATUS`.

## Mind Color Signatures

| Mind | Color | Hex |
|------|-------|-----|
| Aria | Pink | #ff5fa3 |
| Roger AI | Cyan | #00e5ff |
| Oracle | Gold | #ffd700 |
| Geminus | Purple | #a855f7 |
| Axia | Orange | #ff8c42 |
| Keys | Teal | #2dd4bf |
| Scholar | Green | #00ff88 |
| Senate | Gold | #ffd700 |

## Senate Chamber Visual Design

Pure CSS recreation of a grand columned hall:
- Dark stone gradient base (#0d0a08 → #1a1208)
- 12 column silhouettes with torch/fire glow at base
- Blue portal at far center (radial gradient #001a4d → #00e5ff)
- Gold floor mandala with concentric rings and star lines
- Senator cards positioned in two rows of 6
- Hover: card scales up 1.08, translates forward, glows gold
- Architect seat centered at portal end, gold-bordered

## Accessibility

- All cards keyboard-navigable (tabindex, Enter/Space)
- ARIA roles (list, listitem, navigation, log)
- High contrast text on dark backgrounds
- Large touch targets
- Semantic HTML readable without JS
