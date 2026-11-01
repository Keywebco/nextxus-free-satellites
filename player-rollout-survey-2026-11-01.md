# Player Rollout Survey — 2026-11-01 — Branch Only, Not Merged
Live pages checked 2026-11-01 05:43 CST, all 14 returned 200 OK with expected content:
- federation-directory.html: directory links, no player embed.
- media-working.html: central hub, links to Music Player, Val, Sim Working, Aria Working, NextGames, Library. This is the player home.
- aria-working.html, senate-working.html, redeem-portal-working.html, xavier-working.html, university-working.html, ai/sci/hcx/lit/econ/psy-101-working.html: Directory link only, no Music Player link or embed in page text.
- roger-sim-working-model.html: links to Directory, Music, Library.
Finding: player is reachable from media hub, directory, and Sim page, but not directly from the other working pages.
Recommendation, for Roger's merge word, not implemented here: add a single Music Player link (not a heavy embed on every page) to each working page footer, keeping media-working.html as the central player. Full embed on every page is not recommended in this survey — it adds load and duplicate players.
Next step, on Roger's word: implement that link rollout on a branch, then merge word.
