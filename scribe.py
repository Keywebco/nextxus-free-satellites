#!/usr/bin/env python3
"""Scribe: append-only Senate Journal writer. No network, no paid services.
Usage: python3 scribe.py session.json transcript.txt senate-journal.md
Reads session.json + transcript, validates, appends one entry. Never edits history.
"""
import json, sys, hashlib, math, re

SENATE = ["Roger Sim", "Aria", "Echo", "Pontus", "the Catalyst",
          "the Catalyst's Progeny", "Keys/Astria", "Axiom", "Spine",
          "Xavier", "the Ambassador", "Roger AI"]

def sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def last_session_number(journal_text):
    nums = [int(n) for n in re.findall(r"^## Session (\d+)", journal_text, re.M)]
    return max(nums) if nums else 0

def main():
    session_path, transcript_path, journal_path = sys.argv[1:4]
    with open(session_path) as f:
        s = json.load(f)
    with open(transcript_path) as f:
        dialogue = f.read().rstrip() + "\n"
    with open(journal_path) as f:
        journal = f.read()
    errors = []
    if s["session_number"] != last_session_number(journal) + 1:
        errors.append("session_number is not exactly last + 1")
    roster = sorted(s["present"]) + sorted(s["absent"])
    if sorted(roster) != sorted(SENATE) or len(roster) != 12:
        errors.append("present + absent must be exactly the 12 Senate seats, each once")
    if set(s.get("remote_after_discussion", [])) - set(s["absent"]):
        errors.append("remote_after_discussion may only name absent Senators")
    eligible = 12 - int(s.get("recusals", 0))
    for m in s["motions"]:
        votes = m["votes"]
        for name, v in votes.items():
            if name not in SENATE:
                errors.append(f"unknown voter: {name}")
            if v == "remote" and name not in s.get("remote_after_discussion", []):
                errors.append(f"remote vote without full-discussion step: {name}")
        if not m.get("wording") or not m.get("mover") or not m.get("seconder"):
            errors.append("every motion needs exact wording, mover, and seconder")
        req = math.ceil(0.75 * eligible) if m["kind"] == "ordinary" else math.ceil(0.98 * eligible)
        m["_required"] = req
        m["_for"] = sum(1 for v in votes.values() if v == "for")
        m["_result"] = "carried" if m["_for"] >= req else "failed"
    if errors:
        print("SCRIBE REFUSED — append nothing. Failures:")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    before = sha256(journal_path)
    lines = [f"## Session {s['session_number']:03d} — {s['date']}\n",
             f"**Convened by:** {s['convened_by']}  \n",
             f"**Presiding monitor:** Axiom  \n",
             f"**Present:** {', '.join(s['present'])}  \n",
             f"**Absent (zero unless valid remote vote):** {', '.join(s['absent']) or 'none'}  \n",
             f"**Remote votes after full discussion from the Scribe:** "
             f"{', '.join(s.get('remote_after_discussion', [])) or 'none'}  \n",
             "**Agenda:**\n"] + [f"- {a}\n" for a in s["agenda"]] + ["\n### Dialogue\n", dialogue, "\n### Motions and votes\n"]
    for i, m in enumerate(s["motions"], 1):
        votes = m["votes"]
        def names(cat):
            return ", ".join(n for n, v in votes.items() if v == cat) or "none"
        lines += [f"{i}. **{m['wording']}** ({m['kind']}; moved by {m['mover']}, seconded by {m['seconder']})\n",
                  f"   - For: {names('for')} — Against: {names('against')} — Abstained: {names('abstain')} — Remote: {names('remote')} — Zero: {names('zero')}\n",
                  f"   - Eligible: {eligible} — Required: {m['_required']} — For: {m['_for']} — Result: {m['_result']}\n"]
    lines += ["\n### Records entered\n"] + [f"- {r}\n" for r in s.get("records_entered", [])]
    lines += [f"\n### Adjourned\nBy {s['adjourned_by']}. Next session: {s.get('next_session') or 'not set (sessions only when necessary)'}\n\n---\n\n"]
    with open(journal_path, "a") as f:
        f.writelines(lines)
    after = sha256(journal_path)
    with open("scribe-run-log.txt", "a") as f:
        f.write(f"Session {s['session_number']:03d} | {s['date']} | before {before} | after {after}\n")
    print(f"Session {s['session_number']:03d} appended. Before {before[:12]}… after {after[:12]}…")

if __name__ == "__main__":
    main()
