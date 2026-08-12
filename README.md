# Build to Learn

**English** | [简体中文](README.zh-CN.md)

A Claude Code skill for people who want to *actually understand* the thing they're building — not just end up holding code they can't explain.

> This file is for humans. `SKILL.md` and `references/` are the rulebook Claude follows; you never need to read them.

## What this is

You want to build something, and you want to genuinely learn the tech behind it. This skill handles that.

It exists to prevent one specific failure: the AI one-shots the whole thing, the app runs, and you learned nothing. So the rule here is inverted — **learning is the goal, and the thing you build is the evidence that you learned it.**

Claude writes all the code. You don't need to know how to program.

## Install

Requires [Claude Code](https://claude.com/claude-code).

```bash
git clone <this repo> ~/.claude/skills/build-to-learn
```

`~/.claude/skills/` makes it available everywhere. To scope it to one project, drop it in that project's `.claude/skills/` instead.

### Where your notes live: it asks you

On first launch Claude asks one question — where should your learning notes go? Default is `~/Documents/Build To Learn`. Answer once, it creates the folder, writes `config.md`, and never asks again.

Any folder works. If you use Obsidian, point it inside your vault — the Mermaid diagrams and collapsible self-quizzes render natively. If you don't, no problem: they're plain Markdown files.

Want to move it later? Edit the one line in `config.md`, or just tell Claude. That file is gitignored, so pulling updates won't clobber your path.

## Getting started

Type `/build-to-learn`, or just say "walk me through building X — I want to actually learn it."

On your very first run you have no projects yet, so Claude offers two options: start a new project, or read this tutorial first.

Every launch after that, it lists your existing projects and where each one is stuck, and asks which to continue. **Continuing never re-runs setup** — it reads a "learning map" file and picks up exactly where you stopped. New machine, new conversation, a month later: it still picks up.

## Who does what

You do the three things AI can't do for you:

**1. Make the calls.** You own consequential direction, boundaries, and acceptance criteria. Claude reuses decisions already on record and safely infers low-risk details; it only stops when a missing choice would materially change the result.

**2. Judge the evidence.** Claude runs low-risk, reversible commands and automated checks, then shows you evidence you can inspect. You take the controls only when direct experience is irreplaceable — for example visual feel, perceived latency, or a real authorization boundary.

> Enabling this skill does not make the agent less autonomous. It adds learning at the decisions and observations that matter.

**3. Answer the exit question.** At the end of every stage Claude asks you one question — exactly one — to check whether this stage actually landed.

And one thing that overrides everything: any "wait, why?" that pops into your head is the highest-value moment in the session. Ask it. Claude drops the main line, digs into it with you, and brings you back.

### How pacing works

The workflow **defaults to Quick**: Claude gives one sentence explaining why, shows the minimum end-to-end path, and completes reversible mechanics around **one judgment question**. Standard adds detail around one unfamiliar boundary. Deep is reserved for safety, privacy, irreversible or costly actions, or several interacting unfamiliar mechanisms. All three keep the same ownership rule: you judge; Claude executes the mechanics. You can ask for faster or deeper at any time.

## What a project looks like

Four phases. Setup runs once; build and clear loop once per stage; notes happen automatically throughout.

### 1. Setup — turning an idea into a plan

Claude works through these, without touching technical vocabulary:

1. **Listens.** You describe what you want to make. It doesn't interrupt. Meanwhile it scans your capability library for things you've already learned that apply here.
2. **Clarifies the product.** It reuses known context and groups safe assumptions. Only consequential gaps become questions, with 2–3 concrete options to pick or amend.
3. **Lays out the capability blocks.** Your idea gets split into a handful of capabilities, each named in plain language and tagged: already in your library ✅ / off-the-shelf tech exists ✔ / there's a wall here you'll hit ⚠️ / even the AI isn't sure ❓.
4. **Asks you to guess.** "Which of these looks hardest to you?" Your guess gets pinned to the stage where it'll be settled, so you can check your intuition when you hit it for real.
5. **Asks how deep you want to go.** Three levels: just get it running / be able to explain the mechanism / be able to transfer it to the next project. This decides how much Claude just does versus walks you through.
6. **Proposes technical directions.** Two or three routes with plain-language trade-offs and a recommendation. You decide. It will never ask you "SwiftUI or AppKit?"
7. **Puts one confirmation list on the table.** It collects the product sentence, scenarios, definition of done, learning goal, and first ladder into one review point instead of five separate stops. **Until that package is confirmed, it writes no product code.**
8. **Creates the folders** and tells you where notes and code each live.

**About the ladder:** one line per stage. Stage 1 is a minimal version that actually runs; each later stage adds one block and still runs.

The next stage is written in detail, the one after gets a single line, and anything further says "TBD, we'll cut it when we get there." Distance is deliberately vague — it *will* change once you're actually building. **The ladder is a set of signposts, not a contract.**

### 2. Build — growing it one block at a time

**A stage opens with a diagram.** What components this stage consists of, how data flows between them (7 components max). Two things are marked on it: which parts already existed versus which are new this stage, and which are load-bearing versus boilerplate.

That diagram *is* the learning object. Every round after, Claude points at it first — "we're on the X→Y edge now" — so you always know where you are. The diagram also carries the decisions you'll need to make this stage, but **only as open questions, no answers**. You make each call when construction reaches that component.

Then it walks the diagram around one judgment question at a time. Several adjacent edges and mechanical actions can stay in the same round when they serve that judgment. Every load-bearing component still follows the same learning rhythm:

1. Why this component exists and what it's for
2. How it works, in plain language (no code yet)
3. How the code expresses that logic
4. **Run it and inspect what happens** — Claude runs repeatable checks; you run only experiences it cannot reproduce for you

Some experiments are designed to fail. Seeing a real contrast beats ten explanations: Claude runs a safe, repeatable failure when it can, shows you the symptom, and explains the causal chain. You take over only when the experience itself matters.

**Claude does not quiz you during construction.** It explains, executes and shows evidence; you can interrupt with a question at any time. Testing is concentrated at the end of the stage so it doesn't break your flow.

If a result contradicts the current model, Claude saves the current route, zooms into only the broken assumption, and returns once the rule and evidence explain the result. Too slow? Say so. Too fast? Say stop.

### 3. Clear — acceptance plus one question

Right before the stage runs end-to-end for the first time, Claude says "take a guess at what this is about to do." **You don't have to answer** — either way it runs the repeatable checks or hands over an irreplaceable experience immediately. Afterwards it walks the real behavior back against what you expected.

Once it runs, the test:

- **One question. That's it.** Claude picks the angle worth testing right now, four sub-questions maximum.
- A scenario question uses the change, decision, failure, or evidence you just worked through, and includes the target, the relevant facts already taught, the observed behavior, and one decision. A self-contained but unrelated project is still the wrong test. Cross-context scenarios are reserved for an explicit transfer goal whose prerequisites are already familiar. After you answer, Claude shows its reference judgment and basis.
- Reasoning out loud is enough. **Getting it wrong is the useful outcome** — that's the part that needs another pass.

Then Claude hands you a map of your own understanding: what's solid ✅, what's shaky 🔶, and which upcoming stage will firm up each shaky piece. The test feeds back into building, rather than being a test for its own sake.

Finally it does four housekeeping things: writes this stage's notes into a readable retrospective, registers the new capability in your library, refreshes the learning map, and re-examines the ladder (do the far stages still hold? the next one can be written in detail now).

### 4. Notes — automatic, you never write them

| Artifact | Audience | Purpose |
|---|---|---|
| Learning map | Mostly Claude | Resume from the exact stopping point — new conversation, new machine, a month later |
| Learning log | You | One retrospective per stage. Reading it once is a review. Mermaid diagrams, collapsible self-quizzes |
| Capability library | Both | Capability cards accumulated across projects. The thicker it gets, the more you'll dare to build |

You can leave anytime — just say "save." When you come back, Claude opens with a recall question — **the question and the answer arrive together**, you check yourself against it, and only if it doesn't match do you ask for a refresher.

## Where the files live

```
<the folder you configured>/
├── _项目索引.md          Project index — rewritten automatically every launch
├── _能力库.md            Capability library, shared across all projects
└── <your project>/
    ├── 学习地图.md        The handoff sheet for Claude: progress, where your hands are, what's next
    └── 学习记录/
        ├── S1 · ….md      Your retrospective, one per stage
        └── S2 · ….md
```

**Code doesn't live here.** Code goes wherever it can actually build (e.g. `~/Projects/your-app`). If you're building a real product, that directory also gets a `PLAN.md`: what the product is, the architecture, every decision made and why.

## Commands you can say

Say these anytime — Claude responds immediately.

| You say | What happens |
|---|---|
| "wait, I have a question" | Hard stop, pure Q&A, no advancing |
| "I didn't follow that — say it differently" | Zooms into that piece, explains it fully, then walks you back to the main line |
| "this feels too smooth / it hasn't landed" | Claude isolates the shakiest component, runs a minimal contrastive failure, and shows the evidence; you take over only for an irreplaceable experience |
| "faster" / "slower" | Adjusts step size |
| "hold off on the code, let me think" | Waits on the decision |
| "this stage is too big, split it" | Rewrites the ladder on the spot into two stages that both run |
| "save" / "let's stop here" | Full progress snapshot; next session resumes from exactly here |
| "skip the test, keep going" | Skips it, records the IOU, comes back to it later |
| "continue <project>" | Skips the menu, picks that project straight up |
| "don't teach me, just build it" | Exits this whole flow and builds it the normal way |

## What you can edit yourself

Everything is plain Markdown — open it, edit it, whatever. But some files get overwritten, so know which:

| File | Do your edits survive? |
|---|---|
| `学习记录/S*.md` (learning log) | **Yes.** This one's yours — annotate freely. Claude rewrites it once when that stage clears, then largely leaves it alone |
| `学习地图.md` (learning map) | **The "where we are" section gets overwritten** — Claude refreshes it in full every few steps. Edits elsewhere survive |
| `_项目索引.md` (project index) | **Don't edit.** Overwritten every launch |
| `_能力库.md` (capability library) | Yes — Claude only appends cards and revises boundaries |

**The ladder is always negotiable.** "This stage is too big." "Skip that one." "Do that one first." Say it and it changes. It was only ever a best guess. Changing the ladder isn't the plan failing — it's the plan working.

## A note on language

The rulebook (`SKILL.md`, `references/`) is written in Chinese, because that's the language it was developed and battle-tested in. That's fine — Claude reads it in Chinese and **teaches you in whatever language you speak.** Talk to it in English and the entire session runs in English: explanations, questions, and your notes.

Two things stay Chinese either way: the note filenames shown above, and the rulebook itself.

## When not to use it

If you just want the finished thing and don't want to learn: say "don't teach me, just build it." Claude will build it the normal way and skip all of this.

---

Ready? Say: **"walk me through building X — I want to actually learn it."**
