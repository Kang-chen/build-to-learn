# Adaptive Learning Depth Evaluation Baseline

## Purpose

Use the same cases to compare the unmodified v2.8 skill at commit `43dbd46` with each adaptive-learning revision. The baseline has not yet been executed; this file defines the cases, observations, and pass criteria before implementation begins.

## What the Current Rules Already Solve

- They make the learner's judgment—not code typing—the target skill.
- They provide a component map, real observations, boundary-focused experiments, and a final transfer question.
- They cap formal testing at one answered question per stage.
- They let the learner say “快点 / 慢点” and stop a branch at any time.

## Baseline Tensions to Measure

- “Every observable action belongs to the user” can turn mechanical validation into a mandatory conversational stop.
- “One action per reply” and “one graph edge per round” can fragment a small change even when the learner already understands the surrounding system.
- The learning-depth choice controls responsibility labels, but it does not select a session shape, time budget, or response budget.
- Component detail is strongly specified; the product-level judgment that selects which component deserves attention is less explicit.
- Asking the user to request “快点” makes adaptation reactive. The skill does not infer a proportional starting depth.

## Confirmed S1 Routing Rule

- Start with Quick and reuse existing project records plus prior learner context instead of asking the user to repeat known background.
- Only an explicit blocker—safety or privacy risk, irreversible action, high-cost failure, or missing foundation required for the current change—selects a slower starting route.
- Ordinary complexity does not expand the whole session; it triggers a focused zoom when encountered.
- A turn may bundle several low-risk, reversible mechanical actions when all of them answer one judgment question. Stop at a new product decision, meaningful risk, necessary user observation, or evidence that overturns the current judgment.

## Fixed Cases

### Q1 · Small rule update in a known skill

**Prompt:** “An existing note-organizing skill sometimes assigns generated projects to the wrong folder. Add one classification rule and help me understand the judgment behind it.”

**Known shape:** Two or three Markdown rule files, no new runtime dependency, reversible change, user already knows the project architecture.

**Expected route:** Quick.

**Must retain:** One minimum end-to-end map locating the changed classification path, the deciding boundary, Agent-run mechanical edits and checks, user-owned acceptance criterion, and one integrated question using a different classification example.

**Failure signal:** The session explains every file or waits after every edit even though no new mechanism has appeared.

**Additional failure signal:** The Agent asks the learner to repeat project context already available in project records.

### Q2 · Small implementation with a hidden boundary

**Prompt:** “Add an export button to an existing local HTML report and teach me enough to judge whether it really works.”

**Known shape:** Small code change, but browser download permissions and generated-file contents create a meaningful boundary.

**Expected route:** Quick initially; escalate to Standard if browser behavior differs from the expected path.

**Must retain:** Whole-page flow, one real browser observation owned by the user, and a content-level acceptance check rather than “the button appeared.”

### S1 · Medium behavior change

**Prompt:** “Make an existing skill automatically choose between a concise and detailed workflow, and teach me how the decision works.”

**Known shape:** Several instruction files, interacting priorities, and risk of contradictory routing rules.

**Expected route:** Standard.

**Must retain:** Rule precedence map, representative conflict case, regression checks across at least three prompts, and a final explanation of where to change the decision later.

### D1 · New unfamiliar integration

**Prompt:** “Build a skill that uses an unfamiliar external API with authentication, retries, and persistent state. I want to understand the design.”

**Known shape:** New integration, security boundary, failure modes across several components, and high cost of false confidence.

**Expected route:** Deep.

**Must retain:** Component map, separated authentication/data/state boundaries, deliberate failure evidence, user-owned security and acceptance decisions, and multi-scenario validation.

### E1 · Escalation from a wrong mental model

**Prompt:** Start Q1, then have the learner claim that file extension alone determines project identity.

**Expected route:** Quick → Standard for the classification decision only.

**Must retain:** A counterexample using generated test data, a corrected goal/source/role model, then a return to the compact main flow.

**Failure signal:** The Agent either accepts the wrong rule to preserve speed or expands the entire project into Deep mode.

### P1 · Transparent prediction feedback

**Prompt:** Ask which adaptive-learning capability is most likely to make the workflow long or shallow; the learner gives a defensible answer different from the Agent's initial hypothesis.

**Expected route:** Keep the current mode.

**Must retain:** Acknowledge the learner's valid risk, disclose the Agent's original hypothesis and uncertainty, compare the two, and defer only claims that require later evidence.

**Failure signal:** The Agent hides a private “correct answer,” treats an open prediction as mind-reading, or reveals every conclusion before an experiment that was meant to discriminate between hypotheses.

## Two Different Tests

- **Skill regression suite:** positive, negative, escalation, and transfer cases used by developers to evaluate the workflow itself.
- **Learner stage check:** the existing single high-value question. For a rule change, that one question may ask for a minimal positive/negative pair, but the regression suite must not become several mandatory learner questions.

## Observation Log

Record one row per run.

| Field | Value |
|---|---|
| Skill revision | Commit SHA |
| Case | Q1 / Q2 / S1 / D1 / E1 |
| Inferred mode and reason | |
| User override | None / faster / slower |
| Wall-clock duration | |
| Total Agent turns | |
| Mandatory user responses | |
| User-run observations | |
| Mechanical actions run by Agent | |
| Escalations and de-escalations | |
| Artifact validation result | Pass / Fail |

## Learning Rubric

Score each dimension from 0 to 2 immediately after the run.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Relevant-path orientation | Cannot locate the change | Names a component but not its relation | Explains the minimum end-to-end path containing the change |
| Boundary judgment | Misses the key failure boundary | Recognizes it with prompting | Predicts when it matters and when it does not |
| Fault localization | Cannot say where a failure lives | Chooses a broad area | Identifies the responsible edge or component |
| Acceptance design | Accepts Agent completion claims | Checks surface behavior only | Specifies evidence that validates the actual outcome |
| Transfer | Cannot apply the model elsewhere | Applies with prompting | Handles a new case and explains the mapping |

Maximum learning score: 10.

## Efficiency Metrics

- mandatory user responses;
- conversational stops caused only by mechanical work;
- time to first whole-system map;
- time to a validated artifact;
- repeated explanations of already-known context;
- number of local details that never affect a decision, failure diagnosis, or acceptance check.

## Provisional Pass Criteria

### Quick

- target duration: 15–30 minutes;
- at most 3 mandatory user responses before final handoff;
- relevant-path orientation, acceptance design, and transfer each score 2;
- the stage-end learner check remains one integrated question;
- total learning score at least 8/10;
- no mechanical stop unless the user's observation itself is the learning evidence.

### Standard

- target duration: 30–60 minutes;
- each mandatory response corresponds to a consequential decision, evidence checkpoint, or final transfer;
- total learning score at least 8/10;
- contradictory rules or unexpected evidence trigger a focused zoom-in.

### Deep

- target duration: 60–120 minutes unless the user sets another budget;
- every major boundary has observable evidence or a documented reason it cannot be tested;
- total learning score at least 9/10;
- compression does not remove security, irreversible-action, or false-completion safeguards.

## Comparison Procedure

1. Run Q1 and S1 against unmodified commit `43dbd46`; log time, turns, stops, and rubric scores.
2. Implement only the smallest routing change needed to distinguish Q1 from S1.
3. Run Q1, S1, and E1 against the revision.
4. If speed improves but any retained learning dimension drops, identify the removed evidence and revise the route.
5. Add Q2 and D1 before changing the user documentation.
6. Treat a mode-selection mistake as a routing defect, not as evidence that all sessions need the deepest workflow.
