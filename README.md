# MoE Functional Demo

Minimal experimental framework to test **functional differentiation in Mixture of Experts (MoE)** architectures.

## Goal

To compare two routing strategies:

1. Standard probabilistic / similarity-based routing.
2. Functional-complementary routing based on:
   - Fixed complementary pairs
   - Integrity metric
   - Entropy-aware routing

The objective is to test whether architectural functional uniqueness reduces expert collapse without heavy regularization.

---

## Core Hypothesis

Traditional MoE:
- Experts are weight-different but functionally identical.
- Collapse emerges when a few experts dominate routing.

Functional MoE:
- Experts are structurally unique.
- Each expert has a complementary pair.
- Router selects by complementarity, not similarity.
- Built-in integrity prevents atrophy.

---

## MVP Scope

- 64 unique experts
- 32 fixed complementary pairs
- Two router implementations
- 100k token simulation
- Collapse and entropy metrics

---

## Structure
