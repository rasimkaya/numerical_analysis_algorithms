<div align="center">
  <h1>🧮 Numerical Solutions of Nonlinear Equations</h1>
  <p><i>Python Implementations of Numerical Analysis Algorithms, Iteration Visualizations, and Root-Finding Methods</i></p>

  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="Numpy" />
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Sympy-3B5526?style=for-the-badge&logo=python&logoColor=white" alt="Sympy" />
</div>

<br>

> **Institution:** Gazi University | Faculty of Science | Department of Mathematics <br>
> **Author:** Rasim Kaya <br>
> **Advisor:** Prof. Dr. Mediha Örkcü <br>

---

## 📖 About the Project
This repository contains Python implementations of fundamental numerical analysis methods used to find the roots of nonlinear equations. The algorithms are applied programmatically, strictly adhering to mathematical principles, and visualized step-by-step using **Matplotlib**. The project focuses on clean code architecture and modular design, following the `DRY` (Don't Repeat Yourself) principle for shared utilities.

---

## 🔬 Fundamental Theorems (Existence of a Root)

To construct a numerical method, we first need to guarantee the existence of a root within a specific interval. The algorithms in this project are built upon the following fundamental theorems:

### 1. Rolle's Theorem
Let $f$ be a continuous function on the closed interval $[a,b]$ and differentiable on the open interval $(a,b)$. If $f(a) = f(b)$, then there exists at least one $c \in (a,b)$ such that:
$$f'(c) = 0$$

### 2. Mean Value Theorem
Let $f$ be continuous on $[a,b]$ and differentiable on $(a,b)$. Then there exists a $c \in (a,b)$ such that:
$$f'(c) = \frac{f(b) - f(a)}{b - a}$$

### 3. Intermediate Value Theorem
Let $f$ be a continuous function on $[a,b]$. If $K$ is any number between $f(a)$ and $f(b)$, then there exists at least one $c \in (a,b)$ such that:
$$f(c) = K$$

### 4. Bolzano's Theorem
Let $f$ be continuous on $[a,b]$. If the signs of the function values at the endpoints are opposite, meaning:
$$f(a) \cdot f(b) < 0$$
then there exists at least one $c \in (a,b)$ such that $f(c) = 0$. *(This condition guarantees the existence of a root in the interval and forms the core basis of the Bisection Method).*

---
