# MoE Functional Demo

Minimal experimental demonstration of expert collapse in Mixture-of-Experts (MoE) systems and structural resistance via functional routing.

---

## Problem

Mixture-of-Experts architectures suffer from expert collapse when routing probabilities are amplified by positive feedback.

Standard routing with reinforcement:

Pᵢ ∝ (activationᵢ + 1)^α

As α increases, a nonlinear phase transition occurs:
- A small subset of experts dominates.
- Effective expert count drops.
- Load distribution becomes highly unequal.

---

## Experiment

64 experts  
30,000 routing steps  

Two routing strategies compared:

1. Standard popularity-based routing
2. Functional load-balanced routing

Metrics:
- Entropy
- Effective expert count (2^entropy)
- Gini coefficient
- Top-4 load share

---

## Representative Result

### Standard Routing

- Effective experts ≈ 16.7
- Gini ≈ 0.78
- Top-4 share ≈ 0.51

More than 50% of load is concentrated in 4 experts.

### Functional Routing

- Effective experts ≈ 64
- Gini ≈ 0.001
- Top-4 share ≈ 0.0625

Uniform distributed activation preserved.

---

## Conclusion

Popularity-amplified routing structurally collapses under sufficient feedback strength.

Functional routing with structural differentiation maintains distributed activation without external regularization.

---

## Reproducibility

Run:


python simulation.py


The script performs an alpha sweep and prints all metrics.
