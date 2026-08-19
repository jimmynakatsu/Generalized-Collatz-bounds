[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jimmynakatsu/generalized-collatz-bounds/blob/main/notebooks/collatz_animations.ipynb)
# Generalized Collatz Mappings: Bounds, Streak Invariants, and Global Drift

A formal investigation into generalized $(m+k, m, m-r)$ Collatz-type dynamical systems. This repository contains the mathematical framework, formal proofs, a complete LaTeX preprint, and visualization scripts exploring finite streak ceilings and critical stopping-time thresholds.

---

## 📌 Overview

The classical Collatz ($3n+1$) problem is an affine piecewise mapping over $\mathbb{Z}^+$. This project generalizes the system across arbitrary bases $m \ge 2$, multiplier parameters $k \ge 1$, and exact residue-patch offsets $(m - r)$:

$$T(x) = \begin{cases}  \dfrac{x}{m}, & x \equiv 0 \pmod m \\ \dfrac{(m + k)x + (m - (x \bmod m))}{m}, & x \not\equiv 0 \pmod m  \end{cases}$$

---

## 🔑 Formal Lemmas & Proofs

### Lemma 1: Single-Step Growth Envelope
For any $x \in \mathbb{Z}^+$ with $x \not\equiv 0 \pmod m$ and remainder $r = x \bmod m \in \{1, 2, \dots, m-1\}$:
$$T(x) \le \left(\frac{m+k}{m}\right)x + \frac{m-1}{m}$$
Equality holds strictly if and only if $x \equiv 1 \pmod m$.

> **Proof:**  
> Expanding the non-zero branch of $T(x)$:
> $$T(x) = \frac{(m+k)x + (m-r)}{m} = \left(\frac{m+k}{m}\right)x + 1 - \frac{r}{m}$$
> Since $r \in \{1, \dots, m-1\}$, the minimum remainder is $r = 1$, which minimizes the subtraction term:
> $$-\frac{r}{m} \le -\frac{1}{m} \implies 1 - \frac{r}{m} \le 1 - \frac{1}{m} = \frac{m-1}{m}$$
> Thus, $T(x) \le \left(\frac{m+k}{m}\right)x + \frac{m-1}{m}$, attaining its maximum uniquely at $r = 1$. $\blacksquare$

---

### Lemma 2: Base- $m$ Positional Representation Bound
Any positive integer $x_0$ with $L$ digits in base $m$ satisfies:
$$m^{L-1} \le x_0 < m^L \implies x_0 \le m^L - 1$$

---

### Lemma 3: Modular Streak Termination
Let $M$ denote the number of consecutive non-zero steps ($x_i \not\equiv 0 \pmod m$) starting from $x_0$. An unbroken streak of length $M$ requires:
$$x_0 \equiv m^M - 1 \pmod{m^M}$$
Consequently, for any seed $x_0 < m^L$, the maximum unbroken streak length is strictly bounded by:
$$M \le L$$

> **Proof:**  
> Each application of the non-zero branch consumes exactly one trailing maximal base-$m$ digit $(m-1)$ through carry propagation. For an integer to sustain $M$ consecutive non-zero operations without generating a multiple of $m$, its base-$m$ representation must end in at least $M$ consecutive $(m-1)$ digits:
> $$x_0 = \sum_{j=0}^{M-1} (m-1)m^j + q \cdot m^M = (m^M - 1) + q \cdot m^M \equiv m^M - 1 \pmod{m^M}$$
> Since $x_0 < m^L$, $x_0$ has at most $L$ total digits in base $m$. Therefore, the trailing streak of $(m-1)$ digits cannot exceed the total digit capacity, establishing $M \le L$. $\blacksquare$

---

## 🏆 Theorems & Complete Derivations

### Theorem 1: Maximum Peak Height for $L$-Digit Trajectories
Let $x_0 \in \mathbb{Z}^+$ have $L$ digits in base $m$, and let $k = 1$. The maximum value attainable after an unbroken streak of $M$ non-zero steps satisfies:
$$\max_{x_0 < m^L} x_M \le (m+1)^L - 1$$

> **Proof:**  
> Applying Lemma 1 inductively with $k=1$ across $M$ consecutive steps:
> $$x_{i+1} \le \left(\frac{m+1}{m}\right)x_i + \frac{m-1}{m}$$
> This produces the geometric recurrence:
> $$x_M \le \left(\frac{m+1}{m}\right)^M x_0 + \frac{m-1}{m} \sum_{j=0}^{M-1} \left(\frac{m+1}{m}\right)^j$$
> Using the finite geometric series identity $\sum_{j=0}^{M-1} \alpha^j = \frac{\alpha^M - 1}{\alpha - 1}$ with $\alpha = \frac{m+1}{m}$:
> $$\sum_{j=0}^{M-1} \left(\frac{m+1}{m}\right)^j = \frac{\left(\frac{m+1}{m}\right)^M - 1}{\frac{1}{m}} = m \left[ \left(\frac{m+1}{m}\right)^M - 1 \right]$$
> Multiplying by $\frac{m-1}{m}$:
> $$x_M \le \left(\frac{m+1}{m}\right)^M x_0 + (m-1)\left[\left(\frac{m+1}{m}\right)^M - 1\right] = \left(\frac{m+1}{m}\right)^M (x_0 + m - 1) - (m - 1)$$
> By Lemma 2, the maximum seed is $x_0 = m^L - 1$, and by Lemma 3, the maximum streak is $M = L$:
> $$x_L \le \left(\frac{m+1}{m}\right)^L (m^L - 1 + m - 1) - (m - 1) = \left(\frac{m+1}{m}\right)^L (m^L) - (m - 1) = (m+1)^L - m + 1$$
> Since $m \ge 2$, $(m+1)^L - m + 1 \le (m+1)^L - 1$. $\blacksquare$

---

### Theorem 2: Global Stopping Time Threshold
Let $\widetilde{T}(x) = \dfrac{(m+k)x + (m - r)}{m^{1 + d(x)}}$ denote the accelerated mapping, where $d(x) = \nu_m((m+k)x + (m-r))$ is the number of additional divisions by $m$. 

Under uniform residue distribution, the expected logarithmic drift $\mathbb{E}[\Delta \ln x]$ is strictly contractive ($\mathbb{E}[\Delta \ln x] < 0$) if and only if:
$$m + k < m^{\frac{m}{m-1}}$$

> **Proof:**  
> 1. **Distribution of $d$:** For random residues, the probability that the numerator has $j$ additional factors of $m$ is given by $\mathbb{P}(d = j) = \frac{m-1}{m^{j+1}}$ for $j \ge 0$.
> 2. **Expected Total Divisions:**
>    $$\mathbb{E}[\text{Divisions}] = 1 + \sum_{j=1}^{\infty} j \cdot \mathbb{P}(d=j) = 1 + \sum_{j=1}^{\infty} \frac{1}{m^j} = 1 + \frac{1}{m-1} = \frac{m}{m-1}$$
> 3. **Logarithmic Drift:**
>    $$\mathbb{E}[\Delta \ln x] \approx \ln(m+k) - \mathbb{E}[\text{Divisions}] \cdot \ln(m) = \ln(m+k) - \left(\frac{m}{m-1}\right)\ln(m)$$
> 4. **Enforcing Contraction ($\mathbb{E}[\Delta \ln x] < 0$):**
>    $$\ln(m+k) < \left(\frac{m}{m-1}\right)\ln(m) \implies m + k < m^{\frac{m}{m-1}}$$
> Subtracting $m$ gives the explicit parameter limit: $k < m\left(m^{\frac{1}{m-1}} - 1\right)$. $\blacksquare$

---

## 📊 Parameter Drift Regimes

| Base ($m$) | Threshold $m^{\frac{m}{m-1}}$ | Multiplier Ceiling ($m+k < \dots$) | Valid Integer Values of $k$ | Dynamics |
| :--- | :--- | :--- | :--- | :--- |
| **$m = 2$** | $2^2 = \mathbf{4.000}$ | $2 + k < 4 \implies k < 2$ | **$k = 1$ ($3x+1$)** | Strictly Contractive (Unique!) |
| **$m = 3$** | $3^{1.5} \approx \mathbf{5.196}$ | $3 + k < 5.196 \implies k < 2.196$ | **$k \in \{1, 2\}$** | Contractive for $4x+(3-r)$ & $5x+(3-r)$ |
| **$m = 4$** | $4^{4/3} \approx \mathbf{6.350}$ | $4 + k < 6.350 \implies k < 2.350$ | **$k \in \{1, 2\}$** | Contractive |
| **$m \to \infty$** | Asymptotic: $m + \ln(m)$ | $k < \ln(m)$ | Sub-logarithmic | Window tapers relative to base |

---

## 📂 Repository Structure

```text
├── paper/
│   └── paper.tex          # Complete LaTeX source file
├── scripts/
│   ├── collatz_anim.py    # Manim animation script (1080p 60fps)
│   └── plot_drift.py      # Python Matplotlib trajectory simulation
├── README.md
└── LICENSE
