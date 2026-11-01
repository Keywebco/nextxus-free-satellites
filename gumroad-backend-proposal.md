# Gumroad Backend Proposal — Working Model — 2026-11-01
Doctrine, standing: Gumroad is the EXCLUSIVE sales venue (2026-09-28, reaffirmed 2026-10-31). The Federation only places the Gumroad link — it never processes or honors sales itself. Anything offered must be downloadable as PDF + instructions. Custom work needs a chat interface, stable, well-documented.
Current working shell: redeem-portal-working.html, format-check only, real verification labeled as backend piece to add, NOT claimed working.
Proposal, NOT implemented yet in this file:
1. Verification endpoint, small, server-side only: receives license key + product ID, calls Gumroad license verification, returns valid/invalid only, no card, no charge, no new sale.
2. No secrets in repo, no token in chat, no token in page code. Gumroad API access, if Roger chooses it, goes through secure entry / Render environment only, never in WhatsApp.
3. On valid: show the Gumroad PDF + instructions download link for that purchase. On invalid: show a plain error, no download, no activation.
4. No stored value, no token-as-cash: Redeem verifies a Gumroad purchase already made, it does not create a stored-value token. This avoids the earlier next-xus.com token blocker.
5. Open check, not claimed resolved: Gumroad subdomain on GitHub copy was rogerkey.gumroad.com vs keywebster.gumroad.com on Emergent copy — reconcile to keywebster on a branch, for Roger's merge word, before any live link is promoted.
6. Costs: no new paid service proposed here. If a new Render service is needed, that is a separate spend question, Roger's explicit yes required, not assumed by this proposal.
Next step, on Roger's Proceed word: implement endpoint on a branch with a test key only, never a live customer key, then check, then merge word.
