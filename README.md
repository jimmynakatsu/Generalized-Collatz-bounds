# Gener# Generalized Collatz Mappings: Bounds, Streak Invariants, and Global Drift

A formal investigation into generalized $(m+k, m, m-r)$ Collatz-type dynamical systems. This repository contains the mathematical derivations, a complete LaTeX preprint, and visualization scripts exploring finite streak ceilings and critical stopping-time thresholds.

---

## 📌 Overview

The classical Collatz ($3n+1$) problem is an affine piecewise mapping over $\mathbb{Z}^+$. This project generalizes the system across arbitrary bases $m \ge 2$, multiplier parameters $k \ge 1$, and exact residue-patch offsets $(m - r)$:

$$T(x) = \begin{cases}  \dfrac{x}{m}, & x \equiv 0 \pmod m \\ \dfrac{(m + k)x + (m - (x \bmod m))}{m}, & x \not\equiv 0 \pmod m  \end{cases}$$

---

## 🔑 Key Mathematical Results

### 1. Three Lemmas on Finite Streaks
* **Lemma 1 (Single-Step Growth Envelope):**
  $$T(x) \le \left(\frac{m+k}{m}\right)x + \frac{m-1}{m}$$
  with sharp equality if and only if $x \equiv 1 \pmod m$.
* **Lemma 2 (Positional Digit Bound):**
  Any $L$-digit seed in base $m$ satisfies $x_0 < m^L$.
* **Lemma 3 (Modular Carry Termination):**
  A continuous streak of $M$ non-zero steps requires $x_0 \equiv m^M - 1 \pmod{m^M}$. Since $x_0 < m^L$, unbroken expansion length is strictly bounded by $M \le L$.

### 2. Peak Height Theorem
For any $L$-digit seed ($k=1$), the maximum reachable peak in a single continuous expansion run satisfies:
$$\max_{x_0 < m^L} x_M \le (m+1)^L - 1$$

### 3. Global Stopping Time Threshold
Under uniform modular residue distribution, the expected logarithmic drift $\mathbb{E}[\Delta \ln x]$ is strictly contractive ($\mathbb{E}[\Delta \ln x] < 0$) if and only if:
$$m + k < m^{\frac{m}{m-1}}$$

* **Binary Case ($m=2$):** Multiplier bound is $2 + k < 2^2 = 4 \implies k < 2$. Thus, **$k = 1$ ($3x+1$) is the unique integer system** permitting contraction.
* **Large Base Asymptotics ($m \to \infty$):** The maximum permissible parameter satisfies $k < \ln(m)$.

---

## 📂 Repository Structure

```text
├── paper/
│   └── paper.tex          # Complete LaTeX source file
├── scripts/
│   ├── collatz_anim.py    # Manim animation script (1080p 60fps)
│   └── plot_drift.py      # Python Matplotlib trajectory simulation
├── README.md
└── LICENSEalized-Collatz-bounds
