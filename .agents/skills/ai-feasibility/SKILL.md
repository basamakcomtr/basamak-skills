---
name: ai-feasibility
description: >-
  Evaluate whether an AI capability is needed, technically plausible, economically justified and acceptably safe for a product or workflow. Use to compare deterministic rules, retrieval, model inference and human review before implementation.
---

# AI Feasibility

## Decision
Answer **Should this use AI at all?** A rule, search index, structured form or human workflow is often preferable. Avoid both AI hype and reflexive rejection when AI genuinely adds value.

## Steps
1. Define the job, user, input, expected output and consequences of an incorrect answer. Identify whether the task is classification, extraction, summarization, retrieval, recommendation or action-taking.
2. Establish a simple baseline: rules, SQL/search, templates, traditional automation or manual review. Explain why it succeeds or falls short before recommending a model.
3. If AI is justified, compare at most **two fitting approaches**: for example prompted structured extraction versus retrieval-grounded generation. Specify the actual data and tool access required; do not invent an available model feature.
4. Assess input rights and data exposure: personal information, confidential business records, consent/legal review as appropriate, provider boundary, retention, prompt injection and output leakage. Set human approval for consequential or irreversible actions.
5. Assess error tolerance, latency, throughput, token or usage cost assumptions, observability, drift, quality evaluation and fallback. Label every cost figure as sourced, calculated from provided inputs or a placeholder.
6. Recommend a small **offline evaluation** with representative, permissioned examples, a non-AI baseline, success thresholds, failure categories and an upper bound on usage/cost. Do not claim evaluation ran unless it did.
7. Decide: **use AI**, **use non-AI automation**, **hybrid**, or **insufficient evidence**. Explain the strongest reason and what would change the choice.

## Output
Decision statement; inputs and risks; option comparison; projected constraints with provenance; an evaluation protocol; explicit go/no-go criteria and owner review points.

## Guardrails
No production prompts containing real private customer data by default. Do not enable paid calls, agent actions or autonomous publishing without authorization and cost controls. Never promise accuracy percentages, deterministic reliability or compliance certifications without verification. Coordinate with `workflow-architect` for integrating an approved approach.
