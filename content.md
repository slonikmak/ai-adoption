# Engineering the AI-Ready Organization

**Anton Mashkov · White paper v0.3 · 2026**

AI adoption starts where a team loses time or has to redo work. The people who own that part of the process decide what AI can help with, which decisions stay in their hands, and what evidence justifies wider use.

<!-- Generated from index.html. The HTML is canonical. -->

01 / Vision & philosophy

## AI-ready by design.

A question overlooked in design review can come back weeks later as a bug report. By then, two teams may already have built different answers into the product.

Illustrative case

### Feature request: Let users reschedule a meeting

A team is adding a rescheduling feature to its calendar app. The design shows how a user changes the meeting time. During design review, an AI assistant spots an open question: what happens to a reminder that’s already scheduled?

The product owner decides that the reminder moves with the meeting. QA now has a concrete test: move a 3:00 meeting to 4:00 and check that its ten-minute reminder arrives once, at 3:50. Nothing should arrive at 2:50.

> The same workflow should work for an engineer using an AI assistant and a colleague working by hand.

01

#### AI-ready processes

Explicit requirements, accessible knowledge, consistent artifacts and verifiable outcomes. Improvements that remain valuable with or without AI.

02

#### Human agency

People retain ownership of decisions, accountability for results and the choice of how to perform their work.

03

#### Shared intelligence

Project knowledge and engineering practices become organizational assets, rather than private context held by individuals or their agents.

04

#### Incremental adoption

Introduce concrete, independently valuable capabilities. Evaluate their results before expanding automation and autonomy.

### One process. Multiple execution methods.

**Human-centered operating model** FIG. 01

**Business goals & human decisions** Intent · ownership · accountability

**Shared SDLC & quality requirements** Specifications · acceptance criteria · evidence

**Human execution** Manual work

**AI-assisted execution** Human–agent collaboration

**Same quality expectations** Verification · review · testing

**Shared engineering foundation** Knowledge · standards · skills · tools

Engineers choose how to do the work within the same quality and security rules.

Teams keep manual development and human review available wherever people prefer them or policy requires them.

02 / Organizational challenges

## The hidden cost of fragmented processes.

Many obstacles to effective AI adoption are existing organizational problems made more visible by automation.

When a product decision lives only in a design conversation, the developer has to piece it together from the ticket and mockup. The reviewer and QA may have to ask the same people again.

#### Fragmented workflow

Incomplete task / design

Developer reconstructs intent

Implementation

Reviewer reconstructs context

QA reconstructs requirements

Knowledge remains fragmented

#### AI-ready workflow

Product intent & exploration

Shared product specification

Technical design & implementation

Verification against specification

QA using shared test plan

Updated project knowledge

### Four recurring sources of friction

#### Fragmented requirements

Jira tickets, visual designs, conversations and comments contain different parts of the intended behavior.

#### Knowledge concentration

Technical and business knowledge is tied to individual developers, limiting cross-project mobility and increasing dependency.

#### Late discovery

Ambiguities surface during coding, review or QA, when changes may already be expensive to correct.

#### Inconsistent AI workflows

Different agents receive different instructions, context and tools. Successful personal practices are difficult to reproduce.

An assistant can look up earlier decisions. When the team has yet to settle a question, the assistant needs a way to bring it to the product owner.

03 / AI-ready SDLC

## From product intent to verified behavior.

Product, engineering and QA share a record of what the feature should do and why. An assistant can draft the specification and test plan as the team makes those decisions.

**The feature lifecycle** FIG. 02

**Product intent** Business goal or feature idea

**Design-first** Design + user stories

**Requirements-first** Behavior + design as needed

**Product specification** Behavior · rules · acceptance criteria · manual test plan

**Technical specification** Architecture · APIs · data model · implementation strategy

Manual development

AI-assisted development

**Verification & review** CI · AI review · human review as appropriate

**Deployment & QA** Validation against the shared specification

**Knowledge update** Improved context for the next feature ↺

The shared project context supports every stage. Requirements and design can iterate, and new decisions update the relevant artifacts.

### Responsibilities and artifacts

01

**Product & design exploration**

Explore the future feature through requirements, designs or both. Design-first and requirements-first approaches converge on one description of behavior.

**Human** Define product intent and choose desired behavior.

**AI** Retrieve related knowledge, draft user stories and identify missing scenarios.

**Output:**  user stories, design references, open questions.

02

**Product specification**

Translate the intent into expected behavior, business rules, constraints, edge cases and acceptance criteria. Resolve substantive uncertainties with the product owner.

**Human** Make product decisions and confirm requirements.

**AI** Interview stakeholders, detect gaps, draft specification and manual test plan.

**Output:**  agreed product specification and manual test plan.

03

**Technical specification**

Define how the feature fits into the existing system, including API contracts, data models, compatibility, interfaces and implementation risks.

**Human** Own architectural and implementation decisions.

**AI** Explore repositories, trace dependencies, propose solutions and implementation plans.

**Output:**  technical specification proportional to task complexity.

04

**Implementation**

Develop using the agreed product and technical context. Changes to the expected behavior are reflected in the specification, not only in code.

**Human** Choose execution method and take responsibility for the result.

**AI** Optionally implement, test, debug and investigate the system.

**Output:**  code, tests and relevant verification evidence.

05

**Verification & code review**

Evaluate implementation quality and conformance to agreed requirements. Use centralized AI review, automated checks and human review according to risk and team policy.

**Human** Resolve findings, provide judgment and review where appropriate.

**AI** Identify defects, missing requirements, test gaps and architecture violations.

**Output:**  review findings and verification results for the current revision.

06

**QA & delivery**

Validate the integrated feature using the manual test plan created during product specification. Record deviations and update requirements when necessary.

**Human** Perform exploratory and manual testing; assess the result.

**AI** Maintain test scenarios, investigate failures and suggest regression coverage.

**Output:**  test results, defects and accepted behavior.

07

**Knowledge feedback**

Record the rules and decisions that colleagues will need the next time they change this feature.

**Human** Confirm important product and architectural changes.

**AI** Extract decisions, propose documentation updates and generate digests.

**Output:**  updated, traceable project knowledge.

### Specification as a shared contract

A product specification provides one shared description of behavior for product owners, designers, frontend and backend engineers, reviewers and QA. Technical specifications explain how that behavior will be implemented in the existing system.

For a cross-component feature, frontend and backend subtasks should refer to the same product specification. Small changes require lightweight descriptions; complex changes justify deeper analysis.

#### Example: standardized feature template

```text
FEATURE / ISSUE ID

01  Intent & business objective
02  User stories and expected behavior
03  Business rules & constraints
04  Design references and UI states
05  Acceptance criteria
06  Dependencies and unresolved questions
07  Manual test plan
08  Related decisions & technical specification
```

A Jira template is one possible implementation. The objective is a common description of the feature, not mandatory long-form documentation.

From decision to acceptance criteria

#### Reminder behavior after rescheduling

The specification keeps the user’s chosen reminder interval. When a meeting moves, the user receives one reminder at that interval before the new start time. The old reminder is canceled.

04 / Shared knowledge & context

## Make organizational knowledge accessible.

People and agents should be able to understand a product without depending on the availability of a specific developer.

A useful answer points back to an approved specification, a recorded decision or evidence in the repository. The same access rules apply when an assistant retrieves those sources.

**Shared project context** FIG. 03

**Knowledge** Business rules, invariants, architecture, data model, user and technical documentation.

**Work context** Jira, specifications, design artifacts, decisions, relevant discussions.

**Evidence** Repositories, tests, API contracts, merge requests, build results and release history.

**Context access layer** Search · retrieval · source references · version awareness · permissions

Product & design

Development & review

QA & support

One knowledge foundation; different views and permissions for each role.

### Start with the sources that already exist

Connect issue trackers, repositories, user documentation and existing technical notes. Establish basic project maps and an interface for contextual questions. There is no need to document every line of legacy code before providing value.

Repository analysis is particularly useful when technical documentation is incomplete. However, observed code behavior must remain distinct from approved product requirements and deployed behavior. The system should indicate the relevant branch, version or release.

Practical use case

#### Product owner asks: “How does this feature actually work?”

The assistant retrieves existing documentation, related specifications and decisions. If these are insufficient, it examines implementation and tests within its authorized scope.

It cites the sources, flags any disagreement between the specification and the code, and tells the product owner which questions are still open.

### A continuous knowledge feedback loop

Existing project knowledge

New feature → specification → implementation → QA

Extract durable rules, decisions and technical changes

Validate, update or supersede knowledge

Improved knowledge for the next feature

After completing a feature, an assistant proposes documentation changes and links them to the relevant sources. Important business rules and architecture decisions require appropriate confirmation. Contradictions and outdated entries are surfaced rather than silently overwritten.

Weekly digests summarize meaningful changes, affected components, new contracts and decisions. The team can remain informed without studying every merge request.

### Knowledge governance

Preserve source links, ownership, revision history, status and applicability. Apply authorization consistently to search, indexes, answers, caches and published summaries. A chat or meeting may contain a new decision, but the accepted decision must be returned to the relevant specification or authoritative documentation.

05 / Agent enablement

## The engineering environment an agent needs

To make a change an engineer can verify, an agent needs access to the relevant code, a place to run it and feedback from the tests.

WHAT

#### Specification

Clear intent, expected behavior, requirements and acceptance criteria.

KNOW

#### Context

Relevant project knowledge, decisions, code and evidence.

HOW

#### Harness

Skills, tools, constraints, verification and feedback.

An agent harness is the combination of contextual access, instructions, tooling, execution environments, permissions and feedback mechanisms around a model. The organization should invest in the harness as an engineering asset, while keeping models and clients replaceable.

**Agent enablement stack** FIG. 04

**Product · Design · Engineering · QA · Support**

Personal agent clients

Centralized automated agents

**Reusable skills & project instructions** Workflows · domain rules · engineering practices

**Context interfaces** Search · APIs · MCP adapters

**Execution tools** Code · CI · tests · documentation

**Governance & evaluation** Access control · logs · budgets · quality benchmarks

On one OpenAI team, a short AGENTS.md points engineers and agents to the relevant design documents. When a change breaks an architectural rule, a linter explains how to fix it. [OpenAI · Harness engineering](https://openai.com/index/harness-engineering/)

### Concrete capabilities

#### Requirements assistant

Interviews product stakeholders, identifies ambiguities, creates specifications and derives manual test plans.

#### Technical analysis assistant

Investigates existing code and dependencies; proposes a technical specification or an implementation plan.

#### Shared engineering skills

Reusable, versioned instructions for context retrieval, development practices, review, testing and documentation maintenance.

#### Centralized verification agent

Automatically reviews changes using relevant specifications, engineering standards and repository context.

#### Knowledge maintenance assistant

Extracts useful project knowledge, proposes updates, detects contradictions and produces summaries.

### Choosing practices for a team

In specification-driven development (SDD), the team writes a specification that guides the agent during implementation. Teams can use this approach where the change warrants it.

Agent skills, retrieval systems, MCP integrations, coding assistants and automated reviewers are implementation choices. Select and adapt them to the organization's infrastructure, policies and needs.

#### What a reusable skill should contain

- Purpose, applicability and expected output.
- Required sources and tools.
- Steps, quality checks and handling of uncertainty.
- Examples and known failure cases.
- Version, owner and evaluation scenarios.

Keep enforceable policies in deterministic tooling when possible. A written instruction is not a substitute for an actual security, test or access-control check.

06 / Quality & verification

## Where review starts

Some of the most consequential review happens before anyone writes code, while the team is deciding how the feature should behave.

Product and engineering review the specification while they can still change the design. Later, the reviewer reads the diff against those decisions.

**Verification across the lifecycle** FIG. 05

1

**Product specification review**

Are the behavior, business rules, acceptance criteria and user scenarios sufficiently clear?

2

**Manual test-plan generation**

Can meaningful test scenarios be derived from the requirements? Missing expected outcomes reveal specification gaps.

3

**Technical specification review**

Does the proposed solution fit the existing architecture and preserve important contracts?

4

**Implementation verification**

Automated checks and code review examine defects, risks and conformance to the specification.

5

**Integrated QA**

Validate the expected behavior in the target environment, including exploratory testing.

### Centralized AI code review

Integrate an AI reviewer with the Git platform, for example GitLab. It receives the current diff, relevant product and technical specifications, repository context, tests and engineering standards. It publishes concrete findings linked to affected code and explains the scenario, impact and evidence.

The reviewer identifies the exact revision it checked. If a tool fails, context is missing or the analysis stops early, it marks the review incomplete and explains what it could not verify.

#### A review finding the team can act on

The test checks that a reminder arrives at 3:50. It still passes if the calendar also sends the old reminder at 2:50. The AI reviewer flags the gap and asks for a test that records every notification for the meeting and checks that only the 3:50 reminder was delivered.

Anthropic’s guide to evaluating agents describes how to check what actually happened in the system. [Anthropic · Demystifying evals for AI agents](https://www.anthropic.com/research/demystifying-evals-for-ai-agents)

Uber evaluates its automated reviewer using developer feedback and a separate set of changes with known defects. [Uber Engineering · uReview](https://www.uber.com/us/en/blog/ureview/)

### Human review remains available

AI review should not be treated as proof of correctness. Keep manual review available and require appropriate expert involvement for high-risk changes, according to organization policy. Begin in advisory mode, measure findings and omissions, and reduce redundant manual review only where the evidence supports it.

> The same acceptance criteria apply whether a developer writes the code by hand or uses an agent.

07 / Adoption roadmap

## How teams phase adoption

The starting point depends on where a team encounters friction in its existing workflow.

For a team that regularly discovers missing requirements in QA, the first pilot can focus on using an assistant to surface open questions during design review.

Wave 01

#### Establish the foundation

Agree on core artifacts and test useful capabilities early.

**EVAL** Baseline and pilot success criteria

**SPEC** Common feature template

**CTX** Repository & documentation access

**SKILL** Requirements and analysis skills

**REV** Advisory reviewer pilot

Wave 02

#### Connect the workflows

Integrate capabilities around shared specifications and context.

**SPEC** Context-aware product assistant

**DEV** Technical specification workflow

**QA** Early manual test plans

**REV** Specification-aware review

Wave 03

#### Scale what works

Improve coverage and reduce repeated human work.

**KNOW** Knowledge feedback loop

**KNOW** Team digests

**EVAL** Regression benchmarks

**SCALE** Additional products & roles

Each team sets its own pace. Work can start in parallel wherever one pilot can run independently of another.

### Implementation backlog

#### SPEC — Requirements & specification process

#### SPEC-01 · Define a common feature template

Include intent, behavior, acceptance criteria, design references, questions and manual test plan.

**Done when:**  product, engineering and QA can use the template for real features without duplicating information.

#### SPEC-02 · Create a product specification assistant

Implement a question-and-answer workflow that detects missing and contradictory requirements.

**Done when:**  it produces reviewable specifications on representative tasks, while escalating decisions to humans.

#### SPEC-03 · Establish specification readiness and change handling

Agree how decisions are confirmed, updated and communicated during development.

**Done when:**  all participants can identify the current agreed behavior.

#### CTX — Shared project context

#### CTX-01 · Inventory project knowledge sources

Identify issue trackers, documentation, repositories, design and decision records; agree on access and ownership.

#### CTX-02 · Build a context retrieval MVP

Provide source-linked answers and repository fallback. Respect existing permissions.

**Done when:**  representative product and technical questions can be answered without the original developer.

#### CTX-03 · Connect personal and centralized agents

Expose a common context interface and adapt it to selected agent clients.

#### DEV — Engineering practices & skills

#### DEV-01 · Standardize shared engineering instructions

Capture existing practices and project-specific constraints in versioned skills and deterministic checks.

#### DEV-02 · Introduce technical specification support

Connect approved product requirements, repository research and implementation design. Offer SDD as one workflow.

#### DEV-03 · Pilot the development harness

Enable approved tools, builds, tests, context access and isolated execution.

**Done when:**  both manual and AI-assisted implementations fit the same quality process.

#### REV — Verification & code review

#### REV-01 · Pilot an automated GitLab reviewer

Start with diff, repository context and engineering rules. Publish actionable comments and track failures.

#### REV-02 · Connect product and technical specifications

Extend review to acceptance criteria, business behavior and implementation contracts.

#### REV-03 · Calibrate review policies

Evaluate true findings, false positives, omissions, cost and risk. Preserve manual escalation and audit paths.

#### QA — AI-assisted testing

#### QA-01 · Generate manual test plans during specification

Create expected results, alternative scenarios, permissions, errors and regression areas. Surface undefined behavior before development.

#### QA-02 · Connect QA to current feature artifacts

Make the test plan and agreed product specification available at testing time. Keep them synchronized when requirements change.

#### KNOW — Knowledge feedback & communication

#### KNOW-01 · Extract durable knowledge from completed work

Generate source-linked proposals to update business rules, architecture and technical documentation.

#### KNOW-02 · Maintain knowledge quality

Handle conflicting information, obsolete statements, version applicability and approvals.

#### KNOW-03 · Publish project digests

Summarize relevant changes for the team, highlighting cross-component implications and required actions.

#### EVAL — Adoption & evaluation

#### EVAL-01 · Establish baseline and evaluation cases

Collect representative feature, context retrieval, review and testing examples before changing the process.

#### EVAL-02 · Run bounded pilots and collect feedback

Measure practical outcomes and address weak results. Maintain separate evaluation cases to detect overfitting.

#### EVAL-03 · Extend adoption safely

Share successful workflows, support team onboarding and adapt them to other products.

08 / Evaluation & improvement

## How teams judge a pilot

Generated lines of code and agent interactions tell a team how much it used a tool. To judge its value, the team tracks what changed in delivery, quality and cost.

**Requirements quality** Completeness of feature descriptions, unresolved questions at development start, requirement changes discovered after implementation.

**Delivery effectiveness** Lead time, rework, time spent coordinating decisions and total engineering effort per completed feature.

**Knowledge accessibility** Time to answer project questions, source accuracy, freshness and success of cross-project onboarding.

**Review effectiveness** Validated findings, false positives, missed defects by severity and human effort needed to resolve findings.

**QA effectiveness** Coverage of acceptance criteria, requirement-related clarification requests and escaped defects.

**Operational sustainability** AI costs, failure rates, access violations, maintenance burden and ability to switch execution methods.

### Continuous improvement

Every recurring failure should lead to a system-level improvement: a missing business rule becomes a knowledge update; a repeated defect becomes a regression test; a weak agent workflow becomes a skill or harness improvement.

#### When does the requirements pilot justify wider use?

Before the pilot, the team samples comparable features and records how often an unresolved product question first surfaces after coding starts. It also records time spent preparing specifications and on rework. The team tracks the same measures during the pilot.

If late questions become less frequent and the time saved on rework outweighs the extra preparation, the team expands the pilot. If preparation takes longer and the same questions still reach QA, the team pauses the pilot and examines the missed cases with product and QA.

The target state

## Who owns the result?

The team owns the result. Its engineers can trace a product decision, check the shipped behavior and choose where an assistant helps with the next change.

The calendar feature and the pilot are illustrative examples.
