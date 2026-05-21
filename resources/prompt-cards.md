# Prompt Cards

Diese Karten sind zum Kopieren gedacht.

## 1. Solider Coding-Agent-Auftrag

```text
Goal:
<Was soll am Ende anders sein?>

Context:
<Welche Dateien, Fehlermeldungen, Docs, Beispiele sind relevant?>

Constraints:
<Was darf nicht passieren? Welche Patterns, Technologien, Limits gelten?>

Done when:
<Welche Tests, Checks, Diffs oder sichtbaren Verhaltensänderungen beweisen Erfolg?>

Work style:
Read first. Make a short plan. Keep changes small. Report exact verification.
```

## 2. Read-Only Codebase Scout

```text
Do not edit files.
Map the relevant code path for <problem>.
Return:
1. likely entry points
2. files to inspect
3. risky assumptions
4. the smallest next action
Use file references and line numbers where possible.
```

## 3. Spec-First Feature Prompt

```text
Before implementation, write a concise spec:
- user story
- current behavior
- desired behavior
- non-goals
- acceptance criteria
- edge cases

After the spec, propose an implementation plan.
Do not edit code until the spec and plan are coherent.
```

## 4. Ralph Loop Prompt

```text
Use this loop:
Read: inspect only the necessary files and command output.
Ask: ask at most one blocking question if needed.
Lock: restate scope, non-goals, and done criteria.
Produce: make the smallest useful change.
Halt: stop after verification and show exact evidence.
```

## 5. Verification Prompt

```text
Review your own work before declaring done.
Check:
- Does the diff match the request?
- Did any unrelated file change?
- Which test or command proves the behavior?
- What remains unverified?
Lead with risks, not reassurance.
```

## 6. Skill Extraction Prompt

```text
We repeated this workflow twice. Turn it into an Agent Skill.
Create:
- name and description with clear trigger words
- step-by-step workflow
- inputs and outputs
- edge cases
- references or scripts only if they improve reliability
Keep it focused on one job.
```

## 7. Flock Bug Branch Prompt

```text
Goal:
Fix the failing timer precision regression on the current Flock branch.

Context:
Read AGENTS.md, README.md,
src/flock/components/orchestrator/scheduling/timer.py,
and tests/test_timer_component.py first.

Constraints:
Do not read PR #412 before diagnosing.
Do not change the regression test unless it is demonstrably wrong.
Keep the fix scoped to timer scheduling.
Do not add dependencies.

Done when:
uv run pytest tests/test_timer_component.py::TestTimerStateTracking::test_calculate_next_fire_time_same_second_with_microseconds -q passes.

Work style:
Read first. Explain likely root cause. Propose a short plan. Then edit.
Report exact verification and changed files.
```

## 8. Greenfield Puzzle PRD Prompt

```text
We want to build a highly polished professional minimalistic puzzle game as a web app.
The puzzle game idea should be novel and addictive: easy to understand and play, hard to master.

Requirements:
- procedural/generative levels, no handcrafted levels
- infinite replayability
- fair losing condition
- mobile and desktop web
- playable without sound
- professional minimalistic look and feel
- extensive unit tests
- extensive browser automation tests
- production-ready enough to deploy and publish

Do not implement yet.
Search the web for puzzle game design best practices and browser-game testing guidance.
Return three concepts, recommend one, then write a PRD for the recommended concept.
```

## 9. Greenfield Slice Lock Prompt

```text
From the approved PRD, mechanics spec, and test plan, define the first implementation slice.

Rules:
- playable in browser
- one core mechanic only
- deterministic seed mode
- unit-testable game logic separated from UI
- one losing condition
- one restart flow
- no sound dependency
- no online services

Return:
- files likely to create
- acceptance criteria
- tests to write first
- explicit non-goals
Do not implement yet.
```

## 10. Browser Verification Prompt

```text
Use browser automation or Playwright MCP to verify the app manually.

Check:
- page loads without console errors
- core move works
- losing condition can be reached
- restart works
- mobile viewport is usable
- no sound is required

Report exact evidence and screenshots or observations.
Do not call it production-ready unless these checks pass.
```

## 11. Superpowers Tiny Fix Prompt

```text
Use Superpowers for this change.

Goal:
Fix the failing tiny issue tracker search test.

Context:
Read playground/tiny-issue-tracker/README.md,
playground/tiny-issue-tracker/issue_tracker.py,
and playground/tiny-issue-tracker/tests/test_issue_tracker.py.

Constraints:
Keep the public Issue and IssueTracker API stable.
Do not add dependencies.
Do not broaden search semantics beyond case-insensitive substring matching.

Done when:
python -m unittest discover -s playground/tiny-issue-tracker/tests passes.

Work style:
Follow the relevant Superpowers skills for debugging, TDD, verification, and review.
Show the gates you used, not just the final patch.
```

## 12. OpenSpec Tiny Change Prompt

```text
/opsx:propose "Fix tiny issue tracker search so title and body matching are case-insensitive without changing the public API"
```

Review the generated OpenSpec artifacts before implementation:

```text
Check proposal.md, specs, design.md, and tasks.md.
Non-goals must exclude fuzzy search, ranking, persistence, UI changes, and API changes.
Only then run /opsx:apply.
```
