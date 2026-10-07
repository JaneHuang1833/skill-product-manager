---
name: validation-plan
description: Design low-cost tests for critical Skill, Plugin, Workflow, MCP, or Agent assumptions, with behavior metrics, thresholds, inconclusive outcomes and stopping rules. Use for validation plans; does not launch experiments.
---

# Validation Plan

## Scope and inputs
Use to test decision-bearing assumptions, find the cheapest test, or support VALIDATE FIRST/MVP release preparation. Accept assumptions, decision, user segment, evidence, budget and prototype constraints. If only an idea exists, define the falsifiable assumption without rerunning the entire review.

## Tools
Read research/user material. Local documents and prototypes are optional. Targeted research may improve test design. Publishing, recruitment, messages, payment collection and real-user data collection are not default actions.

## Method
1. Read the [experiment guide](../../references/validation-experiments.md). Prioritize consequential unknowns and low-cost tests that could change the decision.
2. Prefer actual behavior, then costly commitment, then opinion. Recent-event interviews may reveal behavior; explain each method's limits.
3. Define hypothesis, method, participants/channel, observable metric and denominator, sample/window, success/failure thresholds, inconclusive zone, kill criteria, cost ceiling, permissions, owner and next action.
4. Label thresholds as proposed decision standards with reasons. No baseline means no invented benchmark. Include failed and inconclusive paths; an absent result is not success.
5. Provide dependencies and execution materials. Interpret real results only when supplied; record uncertainty and send evidence back to opportunity evaluation.

## Deliverable
A **Validation Plan** containing prioritized assumptions, full experiment contracts, resource/permission boundaries, sequence and outcome-specific actions. Follow `validation_plan` and `Experiment` in the [contracts](../../references/io-contracts.md).

End with knowns, critical unknowns and next action. A plan does not establish effectiveness or silently upgrade the decision to BUILD.
