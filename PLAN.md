# Build-to-Learn Adaptive Learning Depth

## Product

Upgrade `build-to-learn` so that it preserves its central promise—learning is the goal and building is the test—while matching the teaching depth and interaction cost to the scale, risk, novelty, and time budget of the task.

This repository is the active source for the upgrade. `origin` points to the user's fork and `upstream` points to the original project.

## Problem to Reproduce

The current v2.8 design already limits formal questions, but two global rules still force nearly every task into a fine-grained cadence:

- every observable action must be performed by the user;
- every reply advances only one action or one graph edge.

That cadence protects hands-on learning in unfamiliar or risky work. For a small change, however, it can turn a 15–30 minute learning goal into a session projected to take roughly two hours. It also emphasizes local components before giving the learner enough product-level orientation.

## Invariants

The upgrade must keep these properties:

1. Learning remains the goal; a working artifact remains evidence rather than the sole outcome.
2. The learner sees the whole system before zooming into the most informative local detail.
3. The learner owns product boundaries, consequential tradeoffs, acceptance criteria, and the final transfer judgment.
4. New or risky mechanisms are tested against real evidence, including a meaningful failure boundary when useful.
5. The Agent does not claim completion without observable validation.
6. Deep mode remains available for unfamiliar, high-risk, or conceptually dense work.

## Working Hypothesis

Replace a fixed interaction cadence with adaptive instructional routing:

- infer a provisional mode from task size, novelty, risk, prior knowledge, and available time;
- use **one cognitive unit per turn**, not necessarily one mechanical action per turn;
- follow **whole → key local detail → whole**;
- let the Agent bundle reversible mechanical work while preserving user ownership of high-information judgments and observations;
- zoom in when evidence shows confusion, a broken mental model, or an unexpected result;
- allow the user to override the inferred mode at any time.

Provisional modes:

| Mode | Typical task | Target duration | Interaction target |
|---|---|---:|---|
| Quick | Small update in a known system | 15–30 min | At most 3 mandatory user responses before handoff |
| Standard | A behavior change with one or two unfamiliar boundaries | 30–60 min | One response per consequential decision or evidence checkpoint |
| Deep | New system, high risk, or several interacting mechanisms | 60–120 min | Existing component-and-experiment depth where it adds learning value |

These are testable defaults, not final policy.

## Architecture Under Test

1. `SKILL.md`: mode inference, pacing invariants, user override, and routing.
2. `references/1-立项.md`: compact or full discovery based on uncertainty, not a fixed eight-step conversation.
3. `references/2-施工.md`: cognitive-unit cadence and selective user observation.
4. `references/3-通关.md`: mode-proportional validation with one integrated transfer check.
5. `references/4-笔记.md`: proportional note depth and a compact continuation record.
6. `evals/`: fixed cases used before and after each revision.
7. `README.md` and `README.zh-CN.md`: user-visible behavior, updated only after the rules stabilize.

## Stage Ladder

| Stage | Runnable result | Learning focus | Status |
|---|---|---|---|
| S1 · Baseline | Current rules are mapped to fixed evaluation cases and measurable costs | Distinguish essential learning safeguards from accidental ceremony | In progress |
| S2 · Routing design | The same cases receive an explainable Quick, Standard, or Deep route | Task-scale inference and escalation signals | Planned |
| S3 · Skill implementation | The adaptive route is encoded without contradictory instructions | Instruction hierarchy and single-source rules | Planned |
| S4 · Forward test | Old and revised versions are compared on the same cases | Time, turn count, global orientation, and transfer | Planned |
| S5 · Release decision | A reviewed revision is ready for installation and an optional upstream PR | Compatibility and contribution boundary | Planned |

## Acceptance Gate

The revision is ready only when:

- all fixed evaluation cases select a defensible mode;
- the small-update case can finish in the Quick target without losing system orientation or the final transfer check;
- a wrong assumption or failed test automatically increases depth instead of being rushed through;
- Deep mode retains the existing ability to expose mechanisms and boundaries;
- `SKILL.md`, stage references, and user documentation do not contradict one another;
- the same evaluator can compare baseline and revised sessions using the rubric in `evals/adaptive-learning-depth.md`.

## Git Workflow

- `main`: fork baseline, kept comparable with `upstream/main`.
- `codex/adaptive-learning-depth`: active learning and implementation branch.
- Make atomic Conventional Commits for evaluation cases, routing rules, stage changes, and documentation.
- Do not open an upstream pull request until S4 passes and the user reviews the behavior.

## Open Learning Questions

1. Which signals predict task scale robustly without adding another long questionnaire?
2. What is the smallest user-owned action that still trains judgment rather than passive approval?
3. Which observable metrics distinguish “faster” from “shallower”?
4. When should a Quick session escalate, and can it later de-escalate?
5. Can “one cognitive unit per turn” be specified precisely enough that different Agents behave consistently?
