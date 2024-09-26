(Sec:DynSystContinuous)=

# Continuous Dynamical Systems (Under construction)

In this section, we will deal with similar problems as in {numref}`Section %s <Sec:DynSystDiscrete>`. There, we were concerned with discrete time. That is, we assumed a certain initial state $\vect{x}_{0}$ and then predicted the next state $\vect{x}_{1}$. That approach yields models that are often very useful. But just as often we want to deal with continuous time. That is, there is no *next* state but rather a state for every positive real number. 


## Continuous dynamical system

In order to deal with this new context, we need some preliminaries from calculus.

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

In this context, we call $\vect{x}'=A\vect{x}$ a **system of (linear) differential equations** or a **dynamical system**, $\vect{x}$ a **vector-valued function**, $\vect{x}'$ the **derivative** of $\vect{x}$, and the $x_{i}$'s the **component functions** of $\vect{x}$. Any $\vect{y}$  for which $\vect{y}'=A\vect{y}$ holds is called a **solution** to the system of differential equations.

:::

The following proposition will be quite useful to us. It tells us that, in order to find the full (infinite) solution set, it suffices to find a (finite) basis of solutions.

:::{prf:proposition}
:label: Prop:DynSystContinuous:LinComb

If $\vect{y}$ and $\vect{z}$ are solutions of $\vect{x}'=A\vect{x}$ and $c$ and $d$ are arbitrary real numbers, then $c\vect{y}+d\vect{z}$ is also a solution of $\vect{x}=A\vect{x}'$.

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:DynSystContinuous:LinComb`
:class: myproof

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
:label: Prop:DynSystContinuous:EVsgiveSols

If $\lambda$ is an eigenvalue of $A$ with associated eigenvector $\vect{v}$, then $\vect{y}=\vect{v}e^{\lambda t}$ is a solution of the system of linear differential equations $\vect{x}'=A\vect{x}$. Such a $\vect{y}$ is sometimes called an **eigenfunctions** of the dynamical system.

:::

We now know how to solve systems of linear differential equations. But we know more. We also know how a solution $f(t)$ to such a system will behave as $t$ goes to infinity. In practical applications, $t$ usually is time, so this gives us predictions for what happens after a long time.

:::{prf:Example}

Suppose some airborn disease is affecting a population. To keep matters simple, we will assume that the population is constant and that recovery grants full immunity. Let $S(t)$ be the number of susceptible members and $I(t)$ the number of infected members of the population at time $t$. If $\alpha>0$ is the recovery rate and $\beta>0$ is the infection rate, then we find:

$$
\begin{array}{cccc}
S'(t)&=&-\beta S(t)&\\
I'(t)&=&\beta S(t)&-\alpha I(t) 
\end{array}
$$

Define

$$
\vect{y}=\begin{bmatrix}
S(t)\\
I(t)
\end{bmatrix}
\quad\text{and}\quad
A=\begin{bmatrix}
-\beta&0\\
\beta &-\alpha
\end{bmatrix}.
$$

Since $A$ is an upper diagonal matrix, we can conclude that its eigenvalues are $-\beta$ and $-\alpha$, which, for simplicity's sake, we will assume to be different. Therefore, a solution to the system of linear differential equations $\vect{y}'=A\vect{y}$ is given by 

$$
\vect{y}=c_{1}\vect{v}_{-\beta}e^{-\beta t}+c_{2}\vect{v}_{-\alpha}e^{-\alpha t}
$$

where $c_{1}$ and $c_{2}$ are some constants while $\vect{v}_{-\beta}$ and $\vect{v}_{-\alpha}$ are the eigenvectors of $A$ corresponding to $-\beta $ and $-\alpha$, respectively. In particular, if $t$ gets very large, we find very large but negative exponents on the right hand side. That is, both $\lim_{t\to\infty}S(t)$ and $\lim_{t\to\infty} I(t)$ are $0$. This makes perfect sense intuitively, as we expect all members of the population to get infected and recover. After that, they are neither susceptible nor infected anymore.

Note that, in the long run, we will end up arbitrarily close to $\vect{0}$ regardless of the starting values of $S$ and $I$. That is, if we start in any $\vect{v}$ and follow the solution $\vect{y}(t)$ of the system of linear differential equations satisfying the initial condition $\vect{y}(0)=\vect{v}$, then we will always end up in $\vect{0}$. In other words, $\vect{v}$ *attracts* all points. 

:::

:::{prf:definition}

If $A$ is a $2\times 2$-matrix with real eigenvalues $\lambda_{1}$ and $\lambda_{2}$, then the origin is called:

<ul>

<li>

an **attractor** or a **sink** if $\lambda_{1},\lambda_{2}<0$

</li>

<li>

a **repeller** or a **source** if $\lambda_{1},\lambda_{2}>0$

</li>

<li>

a **saddle point** if $\lambda_{1}\lambda_{2}<0$, i.e. if $\lambda_{1}$ and $\lambda_{2}$ have opposite signs.

</li>

</ul>

The three different behaviours are illustrated in {numref}`Figure %s <Fig:DynSystContinuous:Trajectories>`.

:::


Let us once again consider the system $\vect{y}'=A\vect{y}$. By {prf:ref}`Prop:DynSystContinuous:EVsgiveSols`, we can find solutions $\vect{y}=\vect{v}e^{\lambda t}$ where $\lambda$ is an eigenvalue of $A$ and $\vect{v}$ is a corresponding eigenvector. But if $\lambda$ is not a real number, this does not give a real-valued function. In some applications that's perfectly fine, but often we're interested in real solutions to systems of linear differential equations. Can we stil find any of those if some eigenvalues are complex?

Yes, we can! First, we can use the following well-known fact from calculus:

$$

e^{(a+bi)t}=e^{a}e^{bi}=e^{a}(\cos(bt)+i\sin(bt))

$$

that holds for any real numbers $a$ and $b$. In particular, if $\lambda$ is any complex number, then $\overline{e^{\lambda}}=e^{\overline{\lambda}}$. Let us write $\Re{\vect{v}}$ for the vector which entries are the real parts of the entries of $\vect{v}$ and $\Im{\vect{v}}$ for the vector which entries are the imaginary parts of the entries of $\vect{v}$, then we find

$$

\begin{align*}
\vect{v}e^{(a+bi)t}&=(\Re{\vect{v}}+i\Im{\vect{v})}e^{at}(\cos(bt)+i\sin(bt))\\
&=\left[(\Re{\vect{v}}\cos(bt)-\Im{\vect{v}}\sin(bt))+i(\Re{\vect{v}}\sin(bt)+\Im{\vect{v}}\cos(bt))\right]e^{at}
\end{align*}

$$

Secondly, we can use the fact that complex eigenvalues come in conjugate pairs $\lambda=a+bi,\overline{\lambda}=a-bi$ and that the conjugate $\overline{\vect{v}}$ of an eigenvector $\vect{v}$ corresponding to $\lambda$ is an eigenvector corresponding to $\overline{\lambda}$. Since any linear combination of $\vect{v}e^{\lambda t}$ and $\overline{\vect{v}}e^{\overline{\lambda} t}$ is a solution, we have that

$$

\begin{align*}
\frac{1}{2}\vect{v}e^{\lambda t}+\frac{1}{2}\overline{\vect{v}}e^{\overline{\lambda}t}&=\Re{\vect{v}e^{\lambda t}}\\
&=(\Re{\vect{v}}\cos(bt)-\Im{\vect{v}}\sin(bt))e^{at}\quad\text{and}\\
\frac{1}{2i}\vect{v}e^{\lambda t}-\frac{1}{2i}\overline{\vect{v}}e^{\overline{\lambda}t}&=\Im{\vect{v}e^{\lambda t}}\\
&=(\Re{\vect{v}}\sin(bt)+\Im{\vect{v}}\cos(bt))e^{at}
\end{align*}

$$

are solutions of $\vect{y}'=A\vect{y}$. If $A$ is a $2\times 2$-matrix, we can summarize this as follows. 

:::{prf:Proposition}

Let $A$ be a $2\times 2$-matrix with non-real eigenvalue $\lambda=a+bi$. Let $\vect{v}$ be an eigenvector associated to $\lambda.$ Then 

$$

\begin{align*}
\vect{y}_{1}(t)&=(\Re{\vect{v}}\cos(bt)-\Im{\vect{v}}\sin(bt))e^{at}\quad\text{and}\\
\vect{y}_{2}(t)&=(\Re{\vect{v}}\sin(bt)+\Im{\vect{v}}\cos(bt))e^{at}
\end{align*}

$$

are linearly independent solutions to the linear system of differential equations $\vect{y}'=A\vect{y}$. In this case, the origin is called a **spiral point**. An example of a spiral point can be seen in {numref}`Figure %s <Fig:DynSystContinuous:Trajectories>`.

:::

If $a<0$ in this proposition, then $e^{at}$ will become arbitrarily small, so as $t$ increases, $\vect{y}(t)$ will approach $0$. In this case, the trajectory will spiral towards the origin. If $a>0$, then $e^{at}$ becomes arbitrarily large and the trajectory will spiral away from the origin.


::::{figure} Images/Fig-DynSystContinuous-Trajectories.svg
:name: Fig:DynSystContinuous:Trajectories
:class: dark-light

The possible behaviours of the origin illustrated. On the top left, it's an attractor, on the top right a repeller, on the bottom left a saddle point, and on the bottom right a spiral point. For the spiral point, do you expect the real part of the eigenvalues to be positive or negative, given the figure?
::::

## Decoupling a dynamical system

In the previous section, we saw that the eigenvalues and eigenvectors determine the long-term behaviour of a dynamical system. This leads naturally to the suspicion that, perhaps, diagonalizing a matrix can help us solve a system of linear differential equations. This is indeed the case.

Let us assume $A$ is an $n\times n$-matrix with eigenfunctions $\vect{y}_{1},...,\vect{y}_{n}$, that is $\vect{y}_{i}=\vect{v}_{i}e^{\lambda_{i}t}$ where $\lambda_{i}$ is an eigenvalue of $A$ with associated eigenvector $\vect{v}_{i}$.