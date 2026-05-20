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
<Welche Tests, Checks, Diffs oder sichtbaren Verhaltensaenderungen beweisen Erfolg?>

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
