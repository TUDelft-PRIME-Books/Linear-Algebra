(Sec:DynSystContinuous)=

# Continuous Dynamical Systems

In this section, we will deal with similar problems as in {numref}`Section %s <Sec:DynSystDiscrete>`. There, we were concerned with discrete time. That is, we assumed a certain initial state $\vect{x}_{0}$ and then predicted the next state $\vect{x}_{1}$. That approach yields models that are often very useful. But just as often we want to deal with continuous time. That is, there is no *next* state but rather a state for every positive real number. In order to deal with this new context, we need some preliminaries from calculus.

::::{prf:proposition}

We will denote the derivative of a function $f$ by $f'$. Let $f$ and $g$ be differentiable functions on $\R$ and let $c$ be a real number. Then:

<ol type="i">

<li> 

$(f+g)'=f'+g'$, 

</li>

<li> 

$(cf)'=cf'$, 

</li>

<li> 

if $f(t)=e^{\lambda t}$, then $f'(t)=\lambda e^{\lambda t}$. 

</li>

</ol>

::::

This last point means that the equation $x'=\lambda x$ apparently has solution $y(t)=e^{\lambda t}$. We can then conclude that in fact $y(t)=ce^{\lambda t}$ is a solution for every real number $c$. We want to generalise this idea. But first, we need some terminology.

Suppose we have differentiable functions $x_{1},...,x_{n}$ and real numbers $a_{ij}$ for $1\leq i,j\leq n$. A system of equations

$$

\begin{cases}
x_{1}'&=a_{11}x_{1}+a_{12}x_{2}+\cdots +a_{1n}x_{n}\\
x_{2}'&=a_{21}x_{2}+a_{22}x_{2}+\cdots +a_{2n}x_{n}\\
&\,\vdots\\
x_{n}'&=a_{n1}x_{1}+a_{n2}x_{2}+\cdots+a_{nn}x_{n}
\end{cases}

$$

can be conveniently rewritten as $\vect{x}'=A\vect{x}$ where 

$$ \vect{x}=
\begin{bmatrix}
x_{1}\\
x_{2}\\
\vdots\\
x_{n}
\end{bmatrix},
\quad
\vect{x}'=
\begin{bmatrix}
x_{1}'\\
x_{2}'\\
\vdots\\
x_{n}'
\end{bmatrix}
\quad\text{and}\quad
A=
\begin{bmatrix}
a_{11}&a_{12}&\cdots&a_{1n}\\
a_{21}&a_{22}&\cdots&a_{2n}\\
\vdots&\vdots&\ddots&\vdots\\
a_{n1}&a_{n2}&\cdots&a_{nn}
\end{bmatrix}.
$$

:::{prf:definition}

In this context, we call $\vect{x}'=A\vect{x}$ a **system of (linear) differential equations**, $\vect{x}$ a **vector-valued function**, $\vect{x}'$ the **derivative** of $\vect{x}$, and the $x_{i}$'s the **component functions** of $\vect{x}$. Any $\vect{y}$  for which $\vect{y}'=A\vect{y}$ holds is called a **solution** to the system of differential equations.

:::

The following proposition will be quite useful to us. It tells us that, in order to find the full (infinite) solution set, it suffices to find a (finite) basis of solutions.

:::{prf:proposition}

If $\vect{y}$ and $\vect{z}$ are solutions of $\vect{x}'=A\vect{x}$ and $c$ and $d$ are arbitrary real numbers, then $c\vect{y}+d\vect{z}$ is also a solution of $\vect{x}=A\vect{x}'$.

:::

:::{prf:proof}

Exercise.

:::

But how do we find solutions? Let us first consider an example.

:::{prf:example}
:label: Ex:DynSystContinuous:EVsgiveSol

Consider the following system of differential equations:

$$
\vect{x}'=A\vect{x}\quad\text{where}\quad A= \begin{bmatrix}
1&4\\
1&1
\end{bmatrix}.
$$

Consider the vector-valued function

$$
\vect{y}(t)=\begin{bmatrix}
2e^{3t}\\
1e^{3t}
\end{bmatrix}=\vect{v}e^{3t},$$ 

then

$$\quad \vect{y}'(t)=
\begin{bmatrix}
6e^{3t}\\
3e^{3t}
\end{bmatrix}=
\begin{bmatrix}
1&4\\
1&1
\end{bmatrix}\begin{bmatrix}
2e^{3t}\\
1e^{3t}
\end{bmatrix}
=A\vect{y}(t),
$$

so $\vect{y}$ is a solution. 

:::

Why does the particular choice of $\vect{v}$ and $e^{3t}$ in example {prf:ref}`Ex:DynSystContinuous:EVsgiveSol` yield a solution? Well, because $3$ is an eigenvalue of $A$ with associated eigenvector $\vect{v}$. For let us assume that $\lambda$ is an eigenvalue of $A$ with associated eigenvector $\vect{v}$ and put $\vect{y}=\vect{v}e^{\lambda t}$. Then 

$$
\vect{y}'=(\vect{v}e^{\lambda t})'=\vect{v}\lambda e^{\lambda t}=A\vect{v} e^{\lambda t}=A\vect{y},
$$

showing that $\vect{y}$ is indeed a solution. This observation leads us to the following statement.

:::{prf:proposition}

If $\lambda$ is an eigenvalue of $A$ with associated eigenvector $\vect{v}$, then $\vect{y}=\vect{v}e^{\lambda t}$ is a solution of the system of linear differential equations $\vect{x}'=A\vect{x}$.

:::

We now know how to solve systems of linear differential equations. But we know more. We also know how a solution $f(t)$ to such a system will behave as $t$ goes to infinity. In practical applications, $t$ usually is time, so this gives us predictions for what happens after a long time.

:::{prf:Example}

Suppose some airborn disease is affecting a population. To keep matters simple, we will assume that the population is constant and that recovery grants full immunity. Let $S(t)$ be the number of susceptible members and $I(t)$ the number of infected members of the population at time $t$. If $\alpha>0$ is the recovery rate and $\beta>0$ is the infection rate, then we find:

$$
\begin{align*}
S'(T)&=-\beta S(t)\\
I'(t)&=\beta S-\alpha I(t) 
\end{align*}
\quad\text{so we need the matrix}\quad
A=\begin{bmatrix}
-\beta&0\\
\beta &-\alpha
\end{bmatrix}.
$$

Since $A$ is an upper diagonal matrix, we can conclude that its eigenvalues are $-\beta$ and $-\alpha$. Therefore, a solution to the system of linear differential equations $\vect{y}'=A\vect{y}$ is given by 

$$
\vect{y}=c_{1}\vect{v}_{-\beta}e^{-\beta t}+c_{2}\vect{v}_{-\alpha}e^{-\alpha t}
$$

where $c_{1}$ and $c_{2}$ are some constants while $\vect{v}_{-\beta}$ and $\vect{v}_{-\alpha}$ are the eigenvectors of $A$ corresponding $-\beta $ and $-\alpha$, respectively.

:::