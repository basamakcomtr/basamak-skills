---
name: web-audit
description: >-
  Evaluate websites and landing pages using evidence from accessible content,
  visuals and visitor journeys. Review usability, copy, trust, accessibility
  and conversion opportunities when a user requests a site audit or prioritized
  improvements. Do not claim tests or measurements that were not performed.
---

# Web Audit

## Purpose and boundaries

Assess how a website works for visitors and identify the most valuable improvements. This is a design and user-experience review, not a penetration test, security scan, performance benchmark, or authorization to change a live website.

## Process

1. **Identify the goal.** Determine the website URL, target audience, and desired visitor action from the conversation. If information is missing, choose a reasonable scope rather than asking a lengthy questionnaire.
2. **Verify access.** Use available tools to review the homepage and up to three additional pages most relevant to the visitor journey. Record the source URLs and review date. Explicitly disclose pages that could not be accessed.
3. **Separate observations from assumptions.** Reading text/HTML, inspecting a screenshot, testing a mobile browser emulation, viewing a physical mobile device, and observing real user behavior are different kinds of evidence. For visual inspection, record the viewing method and, where available, the screen or viewport width and height. Do not describe emulation as physical-device testing. Without screenshots or equivalent visuals, do not make definite claims about colors, spacing, or mobile layout.
4. **Evaluate the journey.** Consider the first-screen value proposition, navigation, audience fit, calls to action, forms and contact steps, trust signals, content clarity, and possible accessibility barriers.
5. **Select findings.** Report at most five substantial findings. For each, provide the page, observed evidence, possible visitor impact, actionable recommendation, and priority.
6. **Respect verification limits.** Do not invent speed scores, search rankings, conversion lifts, or user behavior when they were not measured. Do not claim visual testing without visual evidence. A sample interface, illustrated error, marketing figure, or mock message on a page is not automatically a real production failure or a measured performance result; identify it as on-page illustrative content unless independently verified.
7. **Stay safe.** Do not submit forms, make payments, sign into accounts, modify site files, or generate aggressive scanning traffic without explicit authorization.

## Output

- **Review scope:** URLs, date, and evidence type (text/HTML, desktop visual, mobile emulation, or physical device). If visual review occurred, include available viewport or screen dimensions; state explicitly if screenshots were unavailable.
- **Main conclusion:** The single most valuable improvement area, in one or two sentences.
- **Prioritized findings:** Up to five items containing evidence type, page/section, likely impact, recommendation, priority, and approximate effort. Where screenshots exist, attach a real reference for each visual finding; never invent a screenshot URL or number.
- **Implementation order:** The first two or three small next steps.
- **Not verified:** Areas such as mobile layout, forms, analytics, or performance that could not be checked.

Respond in the user's language unless requested otherwise. Do not write the report to a file unless asked. If a file is requested, place the report under `work/web-audit/` and do not commit private reports to Git.
