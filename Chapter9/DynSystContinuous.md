(Sec:DynSystContinuous)=

# Continuous Dynamical Systems

In this section, we will deal with similar problems as in {numref}`Section %s <Sec:DynSystDiscrete>`. There, we were concerned with discrete time. That is, we assumed a certain initial state $\vect{x}_{0}$ at time $t=0$, then predicted the next state $\vect{x}_{1}$ on time $t=1$, $\vect{x}_{2}$ on time $t=2$ and so on. But just as often we want to deal with continuous time. That is, there is no *next* state but rather a state for every positive real number. 


## Preliminaries

In order to deal with this new context, we need some preliminaries from calculus. We will consider functions depending on  the variable $t$. The derivative of a function $f(t)$ will be denoted by $f'(t)$. To lighten notation, we will often write $f$ instead of $f(t)$.

::::{prf:proposition}
:label: Prop:DynSystContinuous:CalcStuff

Let $f$ and $g$ be differentiable functions on $\R$ and let $c$ be a real number. Then:

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

This last point means that the equation $x'=\lambda x$ has solution $x=e^{\lambda t}$. In fact, for every real number $c$, $y=ce^{\lambda t}$ is solution of $x'=\lambda x$. We want to generalise this idea. But first, we need some terminology.

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
\begin{pmatrix}
x_{1}\\
x_{2}\\
\vdots\\
x_{n}
\end{pmatrix},
\quad
\vect{x}'=
\begin{pmatrix}
x_{1}'\\
x_{2}'\\
\vdots\\
x_{n}'
\end{pmatrix}
\quad\text{and}\quad
A=
\begin{pmatrix}
a_{11}&a_{12}&\cdots&a_{1n}\\
a_{21}&a_{22}&\cdots&a_{2n}\\
\vdots&\vdots&\ddots&\vdots\\
a_{n1}&a_{n2}&\cdots&a_{nn}
\end{pmatrix}.
$$

:::{prf:definition}

In this context, we call $\vect{x}'=A\vect{x}$ a **system of (linear) differential equations** or a **dynamical system**, $\vect{x}$ a **vector-valued function**, $\vect{x}'$ the **derivative** of $\vect{x}$, and the $x_{i}$'s the **component functions** of $\vect{x}$. Any $\vect{x}$  for which $\vect{x}'=A\vect{x}$ holds is called a **solution** to the system of differential equations.

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

In view of this result, it makes sense to generalise some concepts which we have seen for vectors to the setting of vectors of functions.

:::{prf:definition}

We say that a vector function $\vect{x}$ is a **linear combination** of vector functions $\vect{x}_{1},...,\vect{x}_{n}$ if there are scalars $c_{1},...,c_{n}$ in $\mathbb{R}$ such that:

$$

\vect{x}=c_{1}\vect{x}_{1}+\cdots + c_{n}\vect{x}_{n}.

$$

In particular, the function $\vect{0}$ can be written as a linear combination of any set of vector functions $S=\left\{\vect{x}_{1},...,\vect{x}_{n}\right\}$ by putting $c_{1}=\cdots=c_{n}=0$. If this is the only way $\vect{0}$ can be written as a linear combination of vector functions in $S$, then $S$ is called **linearly independent**.

:::



## Solving a dynamical system

How do we find the solutions of a dynamical system? Let us see what happens in a simple example.

:::{prf:example}
:label: Ex:DynSystContinuous:DiagEx

Consider the system $\vect{x}'=A\vect{x}$

$$

\vect{x}=\begin{pmatrix}
x_{1}\\
x_{2}
\end{pmatrix}\quad\text{and}\quad A=\begin{pmatrix}
3&0\\
0&-1
\end{pmatrix}.

$$

which can be rewritten as 

$$

\begin{cases}
    x_{1}'&=3x_{1}+0x_{2}=3x_{1}\\
    x_{2}'&=0x_{1}-1x_{2}=-x_{2}
\end{cases}

$$

By {prf:ref}`Prop:DynSystContinuous:CalcStuff`, this system has solutions $x_{1}=c_{1} e^{3t}$, $x_{2}=c_{2}e^{-t}$. Therefore, the vector functions

$$

\vect{x}=c_{1}\begin{pmatrix}
    1\\
    0
\end{pmatrix}e^{3t}+c_{2}\begin{pmatrix}
    0\\
    1
\end{pmatrix}e^{-t}

$$

are solutions.

:::


What made this example easy is the fact that $A$ was diagonal. Indeeed, for any diagonal matrix $A$, the system $\vect{x}'=A\vect{x}$ becomes:

$$

\begin{cases}
x_{1}'&=a_{11}x_{1}+0_{12}x_{2}+\cdots +0_{1n}x_{n}=a_{11}x_{1}\\
x_{2}'&=0_{21}x_{2}+a_{22}x_{2}+\cdots +0_{2n}x_{n}=a_{22}x_{2}\\
&\,\vdots\\
x_{n}'&=0_{n1}x_{1}+0_{n2}x_{2}+\cdots+a_{nn}x_{n}=a_{nn}x_{n}
\end{cases}

$$

By {prf:ref}`Prop:DynSystContinuous:CalcStuff`, we find the solutions:

$$

x_{1}=e^{a_{11}t},\, x_{2}=e^{a_{22}t},\,\ldots,\, x_{n}=e^{a_{nn}t}

$$

for the single equations, which allows us to write the solutions as vector functions: 

$$

\vect{x}=c_{1}\begin{pmatrix}
a_{11}\\
0\\
\vdots\\
0
\end{pmatrix}e^{\lambda_{1}t}+
c_{2}\begin{pmatrix}
0\\
a_{22}\\
\vdots\\
0
\end{pmatrix}e^{\lambda_{2}t}+
\cdots+c_{n}\begin{pmatrix}
0\\
0\\
\vdots\\
a_{nn}
\end{pmatrix}e^{\lambda_{n}t}.

$$

Of course, most matrices are not diagonal. However, most matrices are at least _diagonalisable_, and we can use this to our advantage. Suppose that the matrix $A$ can be diagonalised, so $A=PDP^{-1}$ where $D$ is the diagonal matrix with the eigenvalues $\lambda_{1},...,\lambda_{n}$ on the diagonal and $P$ is the matrix with the corresponding eigenvectors $\vect{v}_{1},...,\vect{v}_{n}$ as columns. Then we have 

$$

\begin{align*}
    \vect{x}'=A\vect{x}&\quad\Longleftrightarrow\quad \vect{x}'=PDP^{-1}\vect{x}\\
    &\quad\Longleftrightarrow\quad P^{-1}\vect{x}'=DP^{-1}\vect{x}\\
    &\quad\Longleftrightarrow\quad (P^{-1}\vect{x})'=D(P^{-1}\vect{x})
\end{align*}

$$

and this is a new dynamical system with a diagonal matrix! Hence, we find the solution

$$

P^{-1}\vect{x}=
c_{1}\begin{pmatrix}
a_{11}\\
0\\
\vdots\\
0
\end{pmatrix}e^{\lambda_{1}t}+
c_{2}\begin{pmatrix}
0\\
a_{22}\\
\vdots\\
0
\end{pmatrix}e^{\lambda_{2}t}+
\cdots+c_{n}\begin{pmatrix}
0\\
0\\
\vdots\\
a_{nn}
\end{pmatrix}e^{\lambda_{n}t}.

$$

The solution of the original system can now be obtained by multiplying from the left with $P$. This suggests the following proposition:

:::{prf:proposition}
:label: Prop:DynSystContinuous:SolsofDynSyst

If $A$ is a diagonalisable matrix with eigenvalues $\lambda_{1},...,\lambda_{n}$ and a corresponding basis of eigenvectors $\vect{v}_{1},...,\vect{v}_{n}$, then the system $\vect{x}'=A\vect{x}$ has general solution:

$$

\vect{y}(t)=c_{1}\vect{v}_{1}e^{\lambda{1}t}+c_{2}\vect{v}_{2}e^{\lambda_{2}t}+\cdots+c_{n}\vect{v}_{n}e^{\lambda_{n}t}.

$$

where $c_{1},...,c_{n}$ are constants.

:::

<!-- :::{admonition} Proof of&nbsp;{prf:ref}`Prop:DynSystContinuous:SolsofDynSyst`
:class: tudproof


::: -->


:::{prf:remark}


 A function $\vect{y}=c\vect{v}e^{\lambda t}$ is called an **eigenfunction** of the dynamical system if $\lambda$ is an eigevnalue with corresponding eigenvector $\vect{v}$.It is easy to check that such an eigenfunction is indeed a solution:

$$
\vect{y}'=(\vect{v}e^{\lambda t})'=\vect{v}\lambda e^{\lambda t}=A\vect{v} e^{\lambda t}=A\vect{y}.
$$


:::


Let us now consider an example.

:::{prf:example}
:label: Ex:DynSystContinuous:EVsgiveSol

Consider the following system of differential equations:

$$
\vect{x}'=A\vect{x}\quad\text{where}\quad A= \begin{pmatrix}
1&4\\
1&1
\end{pmatrix}.
$$

A standard computation shows that $A$ has eigenvalues $\lambda_{1}=3,\lambda_{2}=-1$ with corresponding eigenvectors 

$$

\vect{v}_{1}=\begin{pmatrix}
    2\\
    1
\end{pmatrix}
\quad\text{and}\quad \vect{v}_{2}=\begin{pmatrix}
    -2\\
    1
\end{pmatrix}.

$$

Therefore the general solution to the system $\vect{x}'=A\vect{x}$ is:

$$

\vect{y}=c_{1}\begin{pmatrix}
    2\\
    1
\end{pmatrix}e^{3t}+c_{2}\begin{pmatrix}
    -2\\
    1
\end{pmatrix}e^{-t}.

$$

:::


As long as the matrix $A$ is diagonalisable, we now know how to solve the system of linear differential equations. But we know more. We also know how a solution $f(t)$ to such a system will behave as $t$ goes to infinity. In practical applications, $t$ usually is time, so this gives us predictions for what happens after a long time.

:::{prf:Example}

Suppose some airborn disease is affecting a population. That means that people get sick from the environment, not from other sick people. To keep matters simple, we will assume that the population is constant and that recovery grants full immunity. Let $S(t)$ be the number of susceptible members and $I(t)$ the number of infected members of the population at time $t$. If $\alpha>0$ is the recovery rate and $\beta>0$ is the infection rate, then we find:

$$
\begin{array}{cccc}
S'(t)&=&-\beta S(t)&\\
I'(t)&=&\beta S(t)&-\alpha I(t) 
\end{array}
$$

Define

$$
\vect{y}=\begin{pmatrix}
S(t)\\
I(t)
\end{pmatrix}
\quad\text{and}\quad
A=\begin{pmatrix}
-\beta&0\\
\beta &-\alpha
\end{pmatrix}.
$$

Since $A$ is an upper diagonal matrix, we can conclude that its eigenvalues are $-\beta$ and $-\alpha$, which, for simplicity's sake, we will assume to be different. Therefore, a solution to the system of linear differential equations $\vect{y}'=A\vect{y}$ is given by 

$$
\vect{y}=c_{1}\vect{v}_{-\beta}e^{-\beta t}+c_{2}\vect{v}_{-\alpha}e^{-\alpha t}
$$

where $c_{1}$ and $c_{2}$ are some constants while $\vect{v}_{-\beta}$ and $\vect{v}_{-\alpha}$ are the eigenvectors of $A$ corresponding to $-\beta $ and $-\alpha$, respectively. In particular, if $t$ gets very large, we find very large but negative exponents on the right hand side. That is, both $\lim_{t\to\infty}S(t)$ and $\lim_{t\to\infty} I(t)$ are $0$. This makes perfect sense intuitively, as we expect all members of the population to get infected and recover. After that, they are neither susceptible nor infected anymore.

Note that, in the long run, we will end up arbitrarily close to $\vect{0}$ regardless of the starting values of $S$ and $I$. That is, if we start in any $\vect{v}$ and follow the solution $\vect{y}(t)$ of the system of linear differential equations satisfying the initial condition $\vect{y}(0)=\vect{v}$, then we will always end up in $\vect{0}$. In other words, $\vect{0}$ *attracts* all points. 

:::

For a graphic interpretation of these solutions, we refer to {numref}`Subsection %s <Subsec:DynSystContinuous:Trajectories>`.

## Dealing with complex eigenvalues


Let us once again consider the system $\vect{y}'=A\vect{y}$. By {prf:ref}`Prop:DynSystContinuous:SolsofDynSyst`, we can find solutions $\vect{y}=\vect{v}e^{\lambda t}$ where $\lambda$ is an eigenvalue of $A$ and $\vect{v}$ is a corresponding eigenvector. But if $\lambda$ is not a real number, this does not give a real-valued function. In some applications that's perfectly fine, but often we're interested in real solutions to systems of linear differential equations. Can we stil find any of those if some eigenvalues are complex?

Yes, we can! First, we can use the fact that complex eigenvalues come in conjugate pairs $\lambda=a+bi$, $\overline{\lambda}=a-bi$ and that the conjugate $\overline{\vect{v}}$ of an eigenvector $\vect{v}$ corresponding to $\lambda$ is an eigenvector corresponding to $\overline{\lambda}$. Let us write $\Re{\vect{v}}$ for the vector whose entries are the real parts of the entries of $\vect{v}$ and $\Im{\vect{v}}$ for the vector whose entries are the imaginary parts of the entries of $\vect{v}$. Then, since any linear combination of $\vect{v}e^{\lambda t}$ and $\overline{\vect{v}}e^{\overline{\lambda} t}$ is a solution, we have: 

$$

\begin{align*}
\frac{1}{2}\vect{v}e^{\lambda t}+\frac{1}{2}\overline{\vect{v}}e^{\overline{\lambda}t}&=\Re{\vect{v}e^{\lambda t}}\\
\frac{1}{2i}\vect{v}e^{\lambda t}-\frac{1}{2i}\overline{\vect{v}}e^{\overline{\lambda}t}&=\Im{\vect{v}e^{\lambda t}}
\end{align*}

$$

hence $\Re{\vect{v}}$ and $\Im{\vect{v}}$ are solutions, too.

Secondly, we can use the following well-known fact (cf. {prf:ref}`Dfn:ComplexNumbers:EulersFormule`):

$$

e^{(a+bi)t}=e^{at}e^{bit}=e^{at}(\cos(bt)+i\sin(bt))

$$

that holds for any real numbers $a$ and $b$. In particular, if $\lambda$ is any complex number, then $\overline{e^{\lambda}}=e^{\overline{\lambda}}$. So

$$

\begin{align*}
\vect{v}e^{(a+bi)t}&=(\Re{\vect{v}}+i\Im{\vect{v}})e^{at}(\cos(bt)+i\sin(bt))\\
&=\left[(\Re{\vect{v}}\cos(bt)-\Im{\vect{v}}\sin(bt))+i(\Re{\vect{v}}\sin(bt)+\Im{\vect{v}}\cos(bt))\right]e^{at}
\end{align*}

$$

From which we conclude that

$$

\begin{align*}
\Re{\vect{v}e^{\lambda t}}&=(\Re{\vect{v}}\cos(bt)-\Im{\vect{v}}\sin(bt))e^{a t}\quad\text{and}\\
\Im{\vect{v}e^{\lambda t}}&=(\Re{\vect{v}}\sin(bt)+\Im{\vect{v}}\cos(bt))e^{a t}
\end{align*}

$$

If $A$ is $2\times 2$, we can summarise this as follows. 

:::{prf:proposition}
:label: Prop:DynSystContinuous:ComplexEVs

Let $A$ be a $2\times 2$-matrix with non-real eigenvalue $\lambda=a+bi$. Let $\vect{v}$ be an eigenvector associated to $\lambda.$ Then 

$$

\begin{align*}
\vect{y}_{1}(t)&=\Re{\vect{v}e^{\lambda t}}=(\Re{\vect{v}}\cos(bt)-\Im{\vect{v}}\sin(bt))e^{at}\quad\text{and}\\
\vect{y}_{2}(t)&=\Im{\vect{v}e^{\lambda t}}=(\Re{\vect{v}}\sin(bt)+\Im{\vect{v}}\cos(bt))e^{at}
\end{align*}

$$

are linearly independent solutions to the linear system of differential equations $\vect{y}'=A\vect{y}$.

:::


For a graphic interpretation of these solutions, we refer to {numref}`Subsection %s <Subsec:DynSystContinuous:Trajectories>`.


(Subsec:DynSystContinuous:Trajectories)=
## Trajectories


In this section, we will see the geometric interpretation of the several cases we have dealt with. Note that the solution of a dynamical system $\vect{x}'=A\vect{x}$ contains as many constants as there are rows in $A$. Therefore, if $A$ is an $n\times n$-matrix and $\vect{x}_{0}$ is a vector in $\R^{n}$, there will be one solution of $\vect{x}'=A\vect{x}$ that satisfies $\vect{x}(0)=\vect{x}_{0}$.

:::{prf:definition}

Let $\vect{x}'=A\vect{x}$ be a dynamical system where $A$ is an $n\times n$-matrix. By a **trajectory** we mean a solution of an initial value problem

$$

\vect{x}'=A\vect{x},\quad \vect{x}(0)=\vect{x}_{0}

$$

for some $\vect{x}_{0}$ in $\R^{n}$. If $A$ happens to be a $2\times 2$-matrix, such a trajectory describes a curve in the plane. By a **flow map** of a dynamical system, we mean a map in which several such curves have been plotted.

:::

::::{figure} Images/Fig-DynSystContinuous-Trajectory.svg
:name: Fig:DynSystContinuous:Trajectory
:class: dark-light

On the left a trajectory for the dynamical system associated to a $2x2$-matrix. This trajectory is fully determined by a single initial value, which is indicated by the blue dot. Note that any other initial value which on this trajectory determines the same trajectory. On the right, a flow map for the same dynamical system is plotted. For each trajectory, an initial value is indicated.
::::

It turns out that the eigenvalues and in particular their magnitudes determine what such a flow map will look like. The following definition describes all possible cases.

:::{prf:definition}

If $A$ is a $2\times 2$-matrix with real eigenvalues $\lambda_{1}$ and $\lambda_{2}$, then the origin is called:

<ul>

<li>

an **attractor** or a **sink** if $\lambda_{1},\lambda_{2}<0$,

</li>

<li>

a **repeller** or a **source** if $\lambda_{1},\lambda_{2}>0$,

</li>

<li>

a **saddle point** if $\lambda_{1}\lambda_{2}<0$, i.e. if $\lambda_{1}$ and $\lambda_{2}$ have opposite signs.

</li>

</ul>

The three different behaviours are illustrated in {numref}`Figure %s <Fig:DynSystContinuous:Trajectories>`.

Suppose now that $A$ is a $2\times 2$-matrix with complex eigenvalues $a\pm bi$. Then the origin is called

<ul>

<li>

a **centre** if $a=0$,

</li>

<li>

a **stable spiral point** if $a<0$,

</li>

<li>

an **unstable spiral point** if $a>0$.

</li>

</ul>

An example of a spiral point can be seen in {numref}`Figure %s <Fig:DynSystContinuous:Trajectories>`.

:::


To see where the names come from, consider the solutions given in {prf:ref}`Prop:DynSystContinuous:ComplexEVs`. If $a<0$ in this proposition, then $e^{at}$ will become arbitrarily small, so as $t$ increases, $\vect{y}(t)$ will approach $0$. In this case, the trajectory will spiral towards the origin. If $a>0$, then $e^{at}$ becomes arbitrarily large and the trajectory will spiral away from the origin. Finally, if $a=0$ -- that is, if we have a purely imaginary eigenvalue -- $\vect{y}(t)$ will move along an elliptic trajectory around the origin.


::::{figure} Images/Fig-DynSystContinuous-Trajectories.svg
:name: Fig:DynSystContinuous:Trajectories
:class: dark-light

The possible behaviours of the origin illustrated. On the top left, it's an attractor, on the top right a repeller, on the bottom left a saddle point, and on the bottom right a spiral point. For the spiral point, do you expect the real part of the eigenvalues to be positive or negative, given the figure? That is, do you expect the centre to be a stable spiral point, an unstable spiral point, or a centre?
::::


## Systems with higher derivatives

In this section, we will see a trick for dealing with higher derivatives. It works as long as the system under consideration is still linear. Suppose we have a system like this:

$$
\begin{cases}
x_{1}'''&=ax_{1}+bx_{2}\\
x_{2}'&=cx_{1}+dx_{2}
\end{cases}
$$

How do we solve this? Our usual method fails because of the higher-order derivative of $x_{1}$ appearing in the first equation. However, we can remedy this problem by introducing the new dummy variables $y_{1}=x'_{1}$ and $y_{2}=x''_{1}$. Now our system becomes:

$$
\begin{cases}
y_{2}'&=ax_{1}+bx_{2}\\
y_{1}'&=y_{2}\\
x_{1}'&=y_{1}\\
x_{2}'&=cx_{1}+dx_{2}
\end{cases}
$$

and this is of the form we have discussed! It translates to the equation $\vect{x}'=A\vect{x}$ where

$$
A=\begin{pmatrix}
0&0&a&b\\
1&0&0&0\\
0&1&0&0\\
0&0&c&d
\end{pmatrix}\quad\text{and}\quad\vect{x}=\begin{pmatrix}
y_{2}\\
y_{1}\\
x_{1}\\
x_{2}
\end{pmatrix}.
$$

As an basic application, we can solve second-order linear differential equations:

:::{prf:proposition}
:label: Prop:DynSystContinuous:2ndODE

If $\lambda$ is a root of the quadratic equation $ax^{2}+bx+c=0$, then the differential equation $ax''+bx'+cx=0$ has solution $e^{\lambda t}$.

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:DynSystContinuous:2ndODE`
:class: tudproof

By putting $y=x'$, we can rewrite the differential equation $ax''+bx'+cx=0$ as

$$
\begin{cases}
y'&=-\frac{b}{a}y-\frac{c}{a}x\\
x'&=y
\end{cases}
$$

or as $\vect{x}'=A\vect{x}$ where

$$
A=\begin{pmatrix}
-\frac{b}{a}&-\frac{c}{a}\\
1&0
\end{pmatrix}
\quad\text{and}\quad
\vect{x}=\begin{pmatrix}
y\\
x
\end{pmatrix}.
$$

To find solutions, we need the eigenvalues of $A$. So:

$$
\begin{align*}
0&=\begin{vmatrix}
-\frac{b}{a}-\lambda&-\frac{c}{a}\\
1&-\lambda
\end{vmatrix}=\lambda^{2}+\frac{b}{a}\lambda+\frac{c}{a}\\
&\Updownarrow\\
0&=a\lambda^{2}+b\lambda+c
\end{align*}
$$

whence the eigenvalues are precisely the solutions of $ax^{2}+bx+c=0$. Suppose $\lambda$ is one of these roots and assume $\vect{v}$ is a corresponding eigenvector. By {prf:ref}`Prop:DynSystContinuous:SolsofDynSyst`, $d \vect{v}e^{\lambda x}$ is a solution for any scalar $d$. As $x$ is the second component of this solution vector, $d v_{2}e^{\lambda x}$ is a solution to the original second-order differential equation and so is any scalar multiple of it. Note that $v_{2}$ is not $0$, because for any 

$$

\vect{0}\neq\vect{v}=\begin{pmatrix}
    v_{1}\\
    0
\end{pmatrix}\quad\text{we have}\quad
A\vect{v}=\begin{pmatrix}
-\frac{b}{a}v_{1}\\
v_{1}
\end{pmatrix}

$$

which is not a multiple of $\vect{v}$, so such a $\vect{v}$ cannot be an eigenvector.

:::


## Grasple exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7627c42a-1586-4a35-a812-d83711f03f9f?id=122172
:label: grasple_exercise_9_4_01
:dropdown:
:description: Solving an initial value problem step-by-step.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/cd9c5ac9-9188-4570-b986-8170957e1ab1?id=122176
:label: grasple_exercise_9_4_02
:dropdown:
:description: A particle moving in a planar force field.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b581d5c5-0592-4e9c-8187-72133c4581f6?id=122179
:label: grasple_exercise_9_4_03
:dropdown:
:description: Another initial value problem.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c3329d85-d622-4994-9e90-20d5495fd258?id=122181
:label: grasple_exercise_9_4_04
:dropdown:
:description: General solution of system of first-order differential equations.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/278f8099-f6af-4f8b-858a-8c5222866d19?id=122182
:label: grasple_exercise_9_4_05
:dropdown:
:description: Classify the nature of the origin as an attractor, repeller, saddle point, spiral point or center point.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a729894b-82f3-45f5-bfb7-c3ebdfd92773?id=122184
:label: grasple_exercise_9_4_06
:dropdown:
:description: Another classification question.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/22a26c36-8bba-4fa6-aa73-75d44f24c9b9?id=122186
:label: grasple_exercise_9_4_07
:dropdown:
:description: One more classification question.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/44d69ff4-2d01-43be-91f8-f55702d39500?id=122189
:label: grasple_exercise_9_4_08
:dropdown:
:description: For which value of a parameter will the origin be a repeller?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/85284014-7b76-4268-ba0f-a2ae61337a51?id=122190
:label: grasple_exercise_9_4_09
:dropdown:
:description: Classify and visualise.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9d71b746-2435-4c06-b9a2-635a4d0f9aaf?id=122192
:label: grasple_exercise_9_4_10
:dropdown:
:description: Classify and visualise once more.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c47751bd-d2d1-44e3-9dc8-4d5c500b5ef2?id=122194
:label: grasple_exercise_9_4_11
:dropdown:
:description: From a visualisation to eigenvalues and eigenvectors.

::::