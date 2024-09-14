### A simple example of FracGM with global optimal guarantees

Here we give a simple example that one can verify the differentiability and Lipschitz continuity of $\psi(\boldsymbol{\alpha},x_{\boldsymbol{\alpha}})$. Suppose we have an optimization problem:

$$
    \min_x\ \frac{f(x)}{h(x)}=\frac{x^2}{x^2+1},
$$

where the residual $r(x)=x$ and $c=1$ in sense of Geman-McClure. The dual problem $(6)$ is as follows:

$$
    \min_x\ \mu\big(f(x)-\beta h(x)\big)=\mu\big(x^2-\beta(x^2+1)\big)=\mu x^2-\mu\beta x^2-\mu\beta,
$$

where $\beta\in\mathbb{R}$ and $\mu\in\mathbb{R}$. Let $\boldsymbol{\alpha}=(\beta,\mu)^\top\in\mathbb{R}^2$ and $x_{\boldsymbol{\alpha}}$ be the optimal solution of Problem (6) given $\boldsymbol{\alpha}$, we obtain $x_{\boldsymbol{\alpha}}=0$ by setting the derivative to zero as follows:

$$
    \frac{\partial}{\partial x}(\mu x^2-\mu\beta x^2-\mu\beta)=2\mu(1-\beta)x=0\implies x^*=x_{\boldsymbol{\alpha}}=0.
$$

Thereby we can write 

$$
    \psi(\boldsymbol{\alpha},x_{\boldsymbol{\alpha}})=
    \begin{pmatrix}
    -f(x_{\boldsymbol{\alpha}})+\beta h(x_{\boldsymbol{\alpha}})\\
    -1+\mu h(x_{\boldsymbol{\alpha}})
    \end{pmatrix}=
    \begin{pmatrix}
    -x_{\boldsymbol{\alpha}}^2+\beta x_{\boldsymbol{\alpha}}^2+\beta\\
    -1+\mu x_{\boldsymbol{\alpha}}^2+\mu
    \end{pmatrix}=
    \begin{pmatrix}
    \beta\\
    \mu-1
    \end{pmatrix}.
$$

It is trivial that both component functions $\psi_1(\boldsymbol{\alpha},x_{\boldsymbol{\alpha}})=\beta$ and $\psi_2(\boldsymbol{\alpha},x_{\boldsymbol{\alpha}})=\mu-1$ are differentiable, thus $\psi(\boldsymbol{\alpha},x_{\boldsymbol{\alpha}})$ is differentiable. Given $\boldsymbol{\alpha}_1=(\beta_1,\mu_1)^\top$ and $\boldsymbol{\alpha}_2=(\beta_2,\mu_2)^\top$,

$$
    \\|\psi(\boldsymbol{\alpha}\_1,x_{\boldsymbol{\alpha}\_1})-\psi(\boldsymbol{\alpha}\_2,x_{\boldsymbol{\alpha}_2})\\|=
    \begin{Vmatrix}
    \beta_1-\beta_2\\\mu_1-1-(\mu_2-1)
    \end{Vmatrix}\leq\begin{Vmatrix}
    \beta_1-\beta_2\\\mu_1-\mu_2
    \end{Vmatrix},
$$

then $\psi(\boldsymbol{\alpha},x_{\boldsymbol{\alpha}})$ is Lipschitz continuous. Solving such (simple) case by FracGM guarantees that the solution is global optimal.


### Usage
We test variaous initial guess from `initial_list = [-10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000]`, and all solutions are approximately 0.

```
==================================================
initial guess: -10000
solution: 1.127029877646477e-05
==================================================
initial guess: -1000
solution: -1.9152677706308051e-10
==================================================
initial guess: -100
solution: -6.785652744569969e-07
==================================================
initial guess: -10
solution: -5.101460067959065e-08
==================================================
initial guess: -1
solution: -2.732847282600752e-09
==================================================
initial guess: 0
solution: 0.0
==================================================
initial guess: 1
solution: -2.732847282600752e-09
==================================================
initial guess: 10
solution: -5.101460067959065e-08
==================================================
initial guess: 100
solution: -6.785652744569969e-07
==================================================
initial guess: 1000
solution: -1.9152677706308051e-10
==================================================
initial guess: 10000
solution: 1.127029877646477e-05
```