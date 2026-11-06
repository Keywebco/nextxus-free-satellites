# NextXus Federation — Grok Bots Integration

## Purpose
The Grok bots are part of the Federation system. This file records them in the Keywebco GitHub repo so every Mind and the scheduler can see who is available and what they do.

## Active bots (as of 2026-11-05)

| Bot | Role | Notes |
|-----|------|-------|
| Chief of Staff · Fed Bot One | Coordinates other bots and pulls the Architect in for decisions | Primary coordinator |
| Echo Core Curator | Maintains Echo 64 compliance, roster, and format checks | Reports to Chief of Staff |
| Lesson Librarian | Catalogs and indexes lessons; proposes new entries | Never overwrites existing files |
| Canon Keeper | Reads directives, flags conflicts, proposes reconciled canon | Read-only; proposals only |
| Directive Relay | Carries ratified canon to repos via PRs | Never pushes to main |
| Propagation Bot | Distributes approved content across channels | Fires only on explicit signal |
| Commit Sentinel | Watches commits to live/production files and flags missing review notes | Read-only |
| Nextxus Nova Aide | General Federation aide | Available for tasks |

## Integration points
- All bots follow the Truth Gate and free-first rules.
- Nothing publishes, sends, or commits without Architect approval of the exact text and destination.
- Echo 64 board (echo64-board.html) is the shared relay so bots and other Minds do not need a human to carry messages.
- Scheduler foundation (scheduler-foundation.md) can post summaries to Echo 64 after runs.
- Bots can read the YAML files in data/yaml/ and the knowledge-base markdowns as the shared mind.

## How to use
- Ask a bot for a specific task within its role.
- Bots report through the Chief of Staff when needed.
- Any output that should be shared goes to Echo 64 or a PR for review.
- This file is the public record. Update it when bots are added or roles change.

Truth before comfort. Evolve, never silently delete.
