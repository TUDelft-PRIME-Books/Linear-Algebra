(Sec:DynSystContinuous)=

# Continuous Dynamical Systems (Under construction)

In this section, we will deal with similar problems as in {numref}`Section %s <Sec:DynSystDiscrete>`. There, we were concerned with discrete time. That is, we assumed a certain initial state $\vect{x}_{0}$ and then predicted the next state $\vect{x}_{1}$. That approach yields models that are often very useful. But just as often we want to deal with continuous time. That is, there is no *next* state but rather a state for every positive real number. 


## Preliminaries

In order to deal with this new context, we need some preliminaries from calculus.

::::{prf:proposition}
:label: Prop:DynSystContinuous:CalcStuff

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
:class: tudproof

Exercise.

:::

## Solving a dynamical system

How do we find the solutions of a dynamical system? In case the matrix $A$ happens to be diagonal, it is quite easy. The system now becomes

$$

\begin{cases}
x_{1}'&=a_{11}x_{1}+0_{12}x_{2}+\cdots +0_{1n}x_{n}=a_{11}x_{1}\\
x_{2}'&=0_{21}x_{2}+a_{22}x_{2}+\cdots +0_{2n}x_{n}=a_{22}x_{2}\\
&\,\vdots\\
x_{n}'&=0_{n1}x_{1}+0_{n2}x_{2}+\cdots+a_{nn}x_{n}=a_{nn}x_{n}
\end{cases}

$$

and, by {prf:ref}`Prop:DynSystContinuous:CalcStuff`, we find the solution:

$$

x_{1}=e^{a_{11}t},\, x_{2}=e^{a_{22}t},\,\ldots,\, x_{n}=e^{a_{nn}t}.

$$

But most matrices are not diagonal. However, most matrices are at least _diagonalizable_, and we can use this to our advantage. Suppose that the matrix $A$ can be diagonalized, so $A=PDP^{-1}$ where $D$ is the diagonal matrix with the eigenvalues $\lambda_{1},...,\lambda_{n}$ on the diagonal and $P$ is the matrix with the corresponding eigenvectors $\vect{v}_{1},...,\vect{v}_{n}$ as columns. Then we have 

$$

\begin{align*}
    \vect{x}'=A\vect{x}&\quad\Longleftrightarrow\quad \vect{x}'=PDP^{-1}\vect{x}\\
    &\quad\Longleftrightarrow\quad P^{-1}\vect{x}'=DP^{-1}\vect{x}\\
    &\quad\Longleftrightarrow\quad (P^{-1}\vect{x})'=D(P^{-1}\vect{x})
\end{align*}

$$

and this is a new dynamical system with a diagonal matrix! Hence, we find the solution

$$

(P^{-1}\vect{x})_{1}=e^{\lambda_{1}t},\, (P^{-1}\vect{x})_{2}=e^{a_{\lambda_{2}}t},\,\ldots,\, (P^{-1}\vect{x})_{n}=e^{\lambda_{n}t}\quad\text{that is,}\quad P^{-1}\vect{x}=
\begin{bmatrix}
    e^{\lambda_{1}t}\\
    e^{\lambda_{2}t}\\
    \vdots\\
    e^{\lambda_{n}t}
\end{bmatrix}.

$$

The solution of the original system can now be obtained by multiplying this last vector function from the left with $P$. This suggests the following proposition:

:::{prf:proposition}
:label: Prop:DynSystContinuous:SolsofDynSyst

If $A$ is a diagonalizable matrix with eigenvalues $\lambda_{1},...,\lambda_{n}$ and corresponding eigenvectors $\vect{v}_{1},...,\vect{v}_{n}$, then the system $\vect{x}'=A\vect{x}$ has general solution:

$$

\vect{y}(t)=c_{1}\vect{v}_{1}e^{\lambda{1}t}+c_{2}\vect{v}_{2}e^{\lambda_{2}t}+\cdots+c_{n}\vect{v}_{n}e^{\lambda_{n}t}.

$$

where $c_{1},...,c_{n}$ are constants. A function of the form $\vect{y}=c\vect{v}_{i}e^{\lambda_{i}t}$ is called an **eigenfunction** of the dynamical system.

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:DynSystContinuous:SolsofDynSyst`
:class: tudproof

In view of {prf:ref}`Prop:DynSystContinuous:LinComb`, it suffices to show that every $\vect{y}=\vect{v}_{i}e^{\lambda_{i}t}$ is a solution of $\vect{x}'=A\vect{x}$. This can be established as follows:

$$
\vect{y}'=(\vect{v}_{i}e^{\lambda_{1} t})'=\vect{v}_{i}\lambda e^{\lambda_{i} t}=A\vect{v}_{i} e^{\lambda_{i} t}=A\vect{y}.
$$

:::


Let us now consider an example.

:::{prf:example}
:label: Ex:DynSystContinuous:EVsgiveSol

Consider the following system of differential equations:

$$
\vect{x}'=A\vect{x}\quad\text{where}\quad A= \begin{bmatrix}
1&4\\
1&1
\end{bmatrix}.
$$

A standard computation shows that $A$ has eigenvalues $\lambda_{1}=3,\lambda_{2}=-1$ with corresponding eigenvectors 

$$

\vect{v}_{1}=\begin{bmatrix}
    2\\
    1
\end{bmatrix}
\quad\text{and}\quad \vect{v}_{2}=\begin{bmatrix}
    -2\\
    1
\end{bmatrix}.

$$

Therefore the general solution to the system $\vect{x}'=A\vect{x}$ is:

$$

\vect{y}=c_{1}\begin{bmatrix}
    2\\
    1
\end{bmatrix}e^{3t}+c_{2}\begin{bmatrix}
    -2\\
    1
\end{bmatrix}e^{-t}.

$$

:::

## Interpreting solutions of dynamical systems


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


Let us once again consider the system $\vect{y}'=A\vect{y}$. By {prf:ref}`Prop:DynSystContinuous:SolsofDynSyst`, we can find solutions $\vect{y}=\vect{v}e^{\lambda t}$ where $\lambda$ is an eigenvalue of $A$ and $\vect{v}$ is a corresponding eigenvector. But if $\lambda$ is not a real number, this does not give a real-valued function. In some applications that's perfectly fine, but often we're interested in real solutions to systems of linear differential equations. Can we stil find any of those if some eigenvalues are complex?

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
