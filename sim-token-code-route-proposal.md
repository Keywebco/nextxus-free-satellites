# Roger Sim Token — Safe Code Route Proposal — Working Model — 2026-11-01
Problem, proven 2026-10-31: Render roger-sim-api, live commit c071e73, tries to load private Keywebco/roger-sim-brain files, GitHub returns 401, token present but not accepted, server stays empty, chat 503, corpus_loaded false.
Parked rule, still standing: No GitHub browser sign-in, no token creation by Roger, no 2FA scan, no payment, no sign-out step for Roger.
Safe code route, proposal only, NOT implemented yet in this file:
1. Modify roger-sim-api server.js loadPrompt() to try private files first, as now.
2. On 401, fall back to public files only: CORE public file (nextxus-free-satellites/main/knowledge-base/FEDERATION-CORE-KNOWLEDGE.md, public, 32,850 bytes, verified) plus Roger Sim working packet, already public in nextxus-sim.
3. No private prompt, no private corpus, no GITHUB_TOKEN needed for fallback, no token value exposed, no sign-in needed.
4. Health should flip to online with fallback content, chat should answer as working model, labeled working model, not as private Sim mind.
5. If Render auto-deploys on main push, fallback goes live on merge. If Render needs Manual Deploy, that is a Render step, not a GitHub sign-in step, to be done when Roger chooses, not forced now.
Rejected routes, with reasons:
- Make private Sim files public: REJECTED, exposes private prompt, Pontus blocking opinion stands.
- New token by Roger in Render: PARKED, needs GitHub sign-in, Roger will not do it, do not nag.
- Scratch rebuild of Sim: REJECTED, loses packet, history, and working model.
- Pay $10 Copilot: REJECTED, does not fix 401, does not verify token.
Next step, on Roger's Proceed word: Implement fallback in roger-sim-api on a branch, test locally with public files only, merge, then check Render deploy status, report, do not claim live until POST + browser chat verified.
