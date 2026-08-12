# Build-to-Learn Adaptive Learning Depth

## Product

Upgrade `build-to-learn` so that it adapts the learning cadence to the cognitive change introduced by the current modification, while preserving its central promise: learning is the goal and building is the test.

This repository is the active source for the upgrade. `origin` points to the user's fork and `upstream` points to the original project.

## Problem to Reproduce

The current v2.8 design already limits formal questions, but two global rules still force nearly every task into a fine-grained cadence:

- every observable action must be performed by the user;
- every reply advances only one action or one graph edge.

That cadence protects hands-on learning in unfamiliar or risky work. For a small change, however, it can turn a 15–30 minute learning goal into a session projected to take roughly two hours. It also emphasizes local components before giving the learner enough product-level orientation.

## Confirmed Scope

- Build-to-Learn is an instructional overlay on the Agent's normal autonomy, not a less capable execution mode. It spends user attention only where participation adds learning evidence.
- The Agent selects a provisional cadence, explains the reason in one sentence, and starts without an extra confirmation stop. The user can override it at any time.
- Learning covers the current change and the minimum existing context needed to locate it. Systematic study of an entire existing project belongs to a separate future skill.
- When observable evidence exposes a local gap, save a return anchor, zoom into only the smallest broken assumption or edge, and return only after the conflict is an executable rule, evidence explains the result, and no blocker still affects the current judgment.
- After the learner predicts, the Agent discloses its own initial hypothesis and uncertainty. Only evidence-dependent conclusions remain open until the experiment.
- The learner's stage-end check remains one high-value question. Positive, negative, and transfer cases belong primarily to the skill's regression suite and must not silently become several learner exams.
- A concrete learner check supplies every domain fact needed to derive the judgment and tests only the stage model already taught. After the answer, the Agent reveals its reference judgment and basis; missing prompt context is a teaching defect, not a reason to rephrase the exam repeatedly.
- A learner check also preserves experiential continuity: it defaults to the actual change, decision, failure, or evidence the learner just participated in. A self-contained but unfamiliar domain is still extraneous load; cross-context questions are reserved for an explicit transfer goal with prerequisites already established.
- Automatic handoff to a future project-exploration skill is explicitly out of scope.

## Invariants

The upgrade must keep these properties:

1. Learning remains the goal; a working artifact remains evidence rather than the sole outcome.
2. The learner sees the minimum end-to-end context needed to locate the change before zooming into its most informative detail.
3. The learner owns product boundaries, consequential tradeoffs, acceptance criteria, and the final transfer judgment.
4. New or risky mechanisms are tested against real evidence, including a meaningful failure boundary when useful.
5. The Agent does not claim completion without observable validation.
6. Deep mode remains available for unfamiliar, high-risk, or conceptually dense work.

## Working Hypothesis

Use route B: add one pacing decision source to `SKILL.md`, and make the four stage references consume that decision instead of independently reinventing it.

Replace a fixed interaction cadence with adaptive instructional routing:

- default to Quick by reusing project history and prior learner context; only explicit safety, irreversibility, high-cost, or missing-foundation blockers select a slower starting route;
- organize each turn around **one judgment question**, while allowing multiple reversible mechanical actions that serve that same question;
- follow **whole → key local detail → whole**;
- let the Agent bundle reversible mechanical work while preserving user ownership of high-information judgments and observations;
- zoom in when evidence shows confusion, a broken mental model, or an unexpected result;
- after a learner prediction, disclose the Agent's hypothesis and compare the two before deferring only what requires evidence;
- allow the user to override the inferred mode at any time.

Provisional modes:

| Mode | Typical task | Target duration | Interaction target |
|---|---|---:|---|
| Quick | Small update in a known system | 15–30 min | At most 3 mandatory user responses before handoff |
| Standard | A behavior change with one or two unfamiliar boundaries | 30–60 min | One response per consequential decision or evidence checkpoint |
| Deep | New system, high risk, or several interacting mechanisms | 60–120 min | Existing component-and-experiment depth where it adds learning value |

These are testable defaults, not three replacement workflows.

## Architecture Under Test

1. `SKILL.md`: the single source for cadence inference, the one-sentence rationale, user override, and escalation/de-escalation.
2. `references/1-立项.md`: proportional discovery and transparent prediction feedback.
3. `references/2-施工.md`: minimum context maps, one-judgment-question cadence, focused zoom-and-return, and selective user observation.
4. `references/3-通关.md`: retain one high-value learner question while keeping regression suites outside the teaching interaction.
5. `references/4-笔记.md`: proportional note depth and a compact continuation record.
6. `evals/`: fixed cases used before and after each revision.
7. `README.md` and `README.zh-CN.md`: user-visible behavior, updated only after the rules stabilize.

## Stage Ladder

| Stage | Runnable result | Learning focus | Status |
|---|---|---|---|
| S1 · Quick-flow MVP | A small modification receives an explained Quick route and completes through the existing stage skeleton | Why fixed action-sized turns create delay; how one routing source changes the contract | Complete |
| S2 · Focused-depth safeguards | Minimum context, local zoom-and-return, transparent prediction feedback, and grounded learner checks work on misconception cases | How to add depth without expanding the whole session | Complete |
| S3 · Compatibility and release | Standard/Deep behavior, four references, regression cases, and user docs agree | How to preserve validated mechanisms while evolving the instruction hierarchy | Complete |

## Acceptance Gate

The revision is ready only when:

- all fixed evaluation cases select a defensible mode;
- the small-update case can finish in 15–30 minutes with no more than 3 mandatory learner responses;
- the learner can explain where the change sits, why it belongs there, and how correct and incorrect outputs test the rule;
- a wrong assumption or failed test automatically increases depth instead of being rushed through;
- prediction feedback exposes the Agent's initial hypothesis rather than asking the learner to guess a hidden answer;
- Deep mode retains the existing ability to expose mechanisms and boundaries;
- `SKILL.md`, stage references, and user documentation do not contradict one another;
- the same evaluator can compare baseline and revised sessions using the rubric in `evals/adaptive-learning-depth.md`.

## Git Workflow

- `main`: fork baseline, kept comparable with `upstream/main`.
- `codex/adaptive-learning-depth`: active learning and implementation branch.
- Make atomic Conventional Commits for evaluation cases, routing rules, stage changes, and documentation.
- Do not open an upstream pull request until S3 passes and the user reviews the behavior.

## Open Learning Questions

1. Which signals predict task scale robustly without adding another questionnaire?
2. What evidence must remain user-observed, and which reversible mechanics can the Agent bundle?
3. Can “one judgment question per turn” be specified precisely enough that different Agents bundle mechanics consistently?
4. Which behavior-level evaluator best detects an Agent that writes the return anchor but still expands the explanation unnecessarily?
