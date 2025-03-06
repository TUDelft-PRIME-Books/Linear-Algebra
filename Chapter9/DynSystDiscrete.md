(Sec:DynSystDiscrete)=

# Discrete Dynamical Systems

## Introduction

In this section we will consider linear transformations $T: \R^n \to \R^n$ from another perpective. We will follow the 'paths' of vectors under repeated application of $T$. In case $T$ is represented by the matrix $A$ this means we will study the sequence

$$
   \vect{x}_0,\,\, \vect{x}_1=A\vect{x}_0,\,\,\vect{x}_2= A\vect{x}_1,\,\,\vect{x}_3= A\vect{x}_2,\,\,\ldots
$$

In {prf:ref}`Ex:Diagonalize:DiagonalizeMigration` in {numref}`Section %s <Sec:Diagonalize>` we analysed the simple migration model

$$
\vect{x}_{k+1} = \left[\begin{array}{cc} 0.9 & 0.2 \\ 0.1 & 0.8 \end{array}\right]\vect{x}_k, \quad
\vect{x}_k = \left[\begin{array}{c} x_k \\ y_k \end{array}\right]
$$

where the 'state vector' $\vect{x}_k = \begin{bmatrix}x_k \\ y_k\end{bmatrix}$ represented the sizes of the populations in two cities.

The next example introduces a more general -- still much simplified -- population model.

::::{prf:example}
:label: Ex:DynSystDiscrete:PopulationModel

Consider a species in which four 'generations' can be distinguished:
young, adolescent, full grown and old.  
In a specified period of time individuals move to the next phase or die,
and possibly reproduce.
Assume the following (fictitious) survival/reproduction table describes the behaviour.

$$
   \begin{array}{ccccc}
        &  y   &  a   &  f  & o  \\ \hline\hline
     y  &  0   &  0   &  4   &  2 \\
     a  & 0.3  &  0   &  0   &  0 \\
     f  &  0   & 0.6  &  0   &  0  \\
     o  &  0   &  0   &  0.4 & 0.1 \\ \hline\hline
   \end{array}
$$

The table has to be read column by column. For instance, the meaning of the first column is that of the age group 'young', 30% reaches the adolescent state. And from the third column it can be read off that
individuals of the age group 'full grown' reproduce 4 offspring and with probability 40% reach 'old age'. The graph in {numref}`Figure %s <Fig:DynSystDiscrete:Leslie1>` visualizes the table.

:::{figure} Images/Fig-DynSystDiscrete-LeslieGraph.svg
:name: Fig:DynSystDiscrete:Leslie1
:class: dark-light

The graph of the population model.
:::

One of the questions of interest here is whether with these numbers the population will survive or go extinct.

Note that, if we define the state at time $k$ as the vector

$$
   \vect{x}_k = \left[\begin{array}{c} y_k \\ a_k \\ f_k \\ o_k \end{array}\right],
$$

we can describe the population dynamics by the process

$$
   \vect{x}_{k+1} = M \vect{x}_k =
   \left[\begin{array}{cccc}   0   &  0   &  4   &  2 \\
                              0.3  &  0   &  0   &  0 \\
                               0   & 0.6  &  0   &  0  \\
                               0   &  0   &  0.4 & 0.1
                      \end{array}\right] \vect{x}_k.
$$

In the context of population dynamics, the matrix $M$ would be called a **Leslie matrix**.

We will study this model more closely in {prf:ref}`Ex:DynSystDiscrete:PopulationModel-2` later in this section.
::::

::::{prf:example}
:label: ExDynSystDiscrete:PageRank

A 'real' example is given by the PageRank algorithm to rank pages on the internet (and which made Google great). The whole internet is modeled as a graph, a set of 'nodes' (= sites) connected by 'edges' (= links). The basic idea is to start from an arbitrary initial situation with a large amount of 'visitors' on the sites and simulate random walks for each visitor where at each step each visitor chooses an arbitrary site that is connected to his present site. Next many cycles are run/simulated, modeled by products

$$
   \vect{x}_{k+1} = M\vect{x}_k
$$

where $M$ is a huge matrix representing the internet graph. Eventually the system reaches a state where 'important' sites, can be recognized by having many visitors.

::::

All three examples lead to so-called _discrete dynamical systems_. The definition of which is as follows.

::::{prf:definition}
:label: Def:DynSystDiscr:DiscreteDynSyst

Suppose $A$ is an $n \times n$ matrix, and $\vect{s}$ a vector in $\R^n$.

The **discrete dynamical system** with matrix $A$ and _initial state_ $\vect{s}$ is the process described by

$$
  \vect{x}_0 = \vect{s}, \quad \vect{x}_{k+1} = A\vect{x}_k, \,\,k = 0,1,2,\ldots
$$

::::

## Stability of Dynamical Systems

In this subsection we will address the questions whether we can give an 'explicit' expression for the general state $\mathbf{x}_k$, and what is the behaviour 'on the long run', i.e., when $k \to \infty$.

Let us start with a definition straight away.

::::{prf:definition}
:label: Def:DynSystDiscrete:Stable

Consider a discrete dynamical system with matrix $A$, so

$$
  \vect{x}_0 = \vect{s}, \quad \vect{x}_{k+1} = A\vect{x}_k, \,\,k = 0,1,2,\ldots
$$

The origin is called **asymptotically stable** if for all initial states $\vect{s}$, the sequence $\vect{x}_0,\vect{x}_1,\vect{x}_2,\ldots $  converges to  $\vect{0}$ if $k \to \infty$.

If for some starting values $\vect{x}_0 = \vect{s}$ the vectors $\vect{x}_k$ become arbitrarily large, i.e., $\norm{\vect{x}_k} \to \infty$ for $k \to \infty$, the dynamical system is called **unstable**.

If $\norm{\vect{x}_k}$ remains bounded, but does not necessarily approach zero for all starting values, the origin is called **stable**.

In the case of asymptotic stability we will call the origin an **attractor**, in the case of instability we say the origin is a **repeller**.  
::::

::::{prf:remark}

This definition of stable and unstable suffices for the dynamical systems we will consider here,
which are in fact _linear_ dynamical systems. Note that according to this definition asymtotic stability implies stability.

If the initial state is $\vect{s} = \vect{0}$, all vectors $\vect{x}_k$ will be $\vect{0}$, so the system is at rest/in equilibrium. For this reason the origin is sometimes called a _stationary point_ or _equilibrium point_. Asymptotic stability means that when due to some 'distortion' the system gets away from this equilibrium point, it will eventually return to it.

::::

::::{prf:remark}

For more general (read: non-linear) dynamical systems a more subtle definition is needed. For one thing, a non-linear dynamical system may have multiple equilibrium points, each with their own behaviour.

In the literature there is quite a bit of terminology to describe the behaviour of dynamical systems at equilibrium points. Apart from linear dynamical systems in the plane, where we can nicely visualize what is going on
(cf. {numref}`Subsec:GraphicalDiscDynSyst`), we will stick to the two qualifications attractor and repellor.

::::

The next proposition describes the behaviour of a dynamical system when its matrix $A$ is diagonalizable. Recall that diagonalizable means that there exists a basis of eigenvectors. For the moment we assume that the eigenvectors are _real_, though this actually plays a minor role.

::::{prf:proposition}
:label: Prop:DynSystDiscrete:DiagCase

Suppose $A$ is an $n\times n$ (real) diagonalizable matrix.
Let $(\vect{v}_1, \ldots, \vect{v}_n)$ be a basis of eigenvectors, and let
$\lambda_1, \ldots, \lambda_n$ be the corresponding eigenvalues.

Each initial state $\vect{s}$ can be  written (in a unique way) as

$$
  \vect{s} =  c_1\vect{v}_1 + c_2\vect{v}_2 +  \ldots + c_n\vect{v}_n,
$$

for some constants (coefficients) $c_1, \ldots, c_n$ in $\R$.

The general vector $\vect{x}_k$ of the dynamical system

$$
  \vect{x}_{0} = \vect{s}, \quad  \vect{x}_{k+1} = A\vect{x}_k, \quad k = 0,1,2,\ldots
$$

is then given by

:::{math}
:label: Eq:DynSystDiscrete:GenSolDiagble

\vect{x}_k =  c_1\lambda_1^k\vect{v}_1 + c_2\lambda_2^k\vect{v}_2 +  \ldots + c_n\lambda_n^k\vect{v}_n.

:::


The expression for $\vect{x}_k$ with unspecified parameters $c_1,\ldots,c_n$ is often referred to as the **general solution** of the dynamical system.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:DynSystDiscrete:DiagCase`
:class: tudproof

There is nothing much to prove.

Since $(\vect{v}_1, \ldots, \vect{v}_n)$ is assumed to be a basis, each vector $\vect{s}$ can be written (uniquely) as

:::{math}
:label: Eq:DynSystDiscrete:InitCoords

\vect{s} =  c_1\vect{v}_1 + c_2\vect{v}_2 +  \ldots + c_n\vect{v}_n,
:::

for some constants  $c_1, \ldots, c_n$ in $\R$.

The vectors $\vect{v}_i$ being eigenvectors for the corresponding $\lambda_i$ means that

$$
  A\vect{v}_i = \lambda_i\vect{v}_i,   \,\, i = 1, \ldots, n.
$$

Thus

$$
  A^2\vect{v}_i = A(A\vect{v}_i) = A(\lambda_i\vect{v}_i) = \lambda_iA\vect{v}_i
  = \lambda_i \lambda_i\vect{v}_i =  \lambda_i^2\vect{v}_i,
$$

and in general

$$
    A^k\vect{v}_i  =  \lambda_i^k\vect{v}_i, \quad  k = 1,2,\ldots
$$

By properties of the matrix product it readily follows that

$$
   \begin{array}{rcl}
     \vect{x}_k = A^k\vect{s} &=& A^{k}(c_1\vect{v}_1 + \ldots + c_n\vect{v}_n)  \\
     & = & c_1A^{k}\vect{v}_1 + \ldots + c_nA^{k}\vect{v}_n \\
     & = & c_1\lambda_1^{k}\vect{v}_1 + \ldots + c_n\lambda_n^{k}\vect{v}_n.
     \end{array}
$$

::::

From Equation {eq}`Eq:DynSystDiscrete:GenSolDiagble` it follows that if **all** eigenvalues have an absolute value smaller than 1, **all** solutions will approach the origin $\vect{0}$ if $k \to \infty$. So then the origin is asymptotically stable.

The following proposition is an almost immediate consequence of Equation {eq}`Eq:DynSystDiscrete:GenSolDiagble`.

::::{prf:proposition}
:label: Prop:DynSystDiscrete:DiagCase2

Suppose the matrix $A$ is diagonalizable, with eigenvalues $\lambda_i$ ordered by absolute value,

$$
   |\lambda_1| \geq |\lambda_2| \geq \ldots \geq |\lambda_n|.
$$

Then

<ol type ="i">

<li>

If $|\lambda_1| < 1$ the origin is asymptotically stable.

</li>

<li>

If $|\lambda_1| > 1$ the origin is unstable.

</li>

<li>

If $|\lambda_1| = 1$ the origin is stable but not asymptotically stable.

</li>

</ul>
::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:DynSystDiscrete:DiagCase2`
:class: tudproof

From Equation {eq}`Eq:DynSystDiscrete:GenSolDiagble` in {prf:ref}`Prop:DynSystDiscrete:DiagCase` it follows immediately that if all

$$
  |\lambda_i|  < 0,
$$

the sequence $\vect{x}_0, \vect{x}_1, \vect{x}_2, \ldots $ will approach the zero vector whatever the values of  the parameters  $c_1,c_2,\ldots,c_n$.

If we have

$$
|\lambda_j| > 1
$$

for one of the eigenvalues, then if we let the process start from

$$
   \vect{s} = \vect{v}_j,
$$

an eigenvector for this eigenvalue, then

$$
  \norm{\vect{x}_{k}} = \norm{\lambda_j^k\vect{v}_j} =
  |\lambda_j|^k \norm{\vect{v}_j}  \longrightarrow \infty,
$$

if $k \to \infty$. This means that the system is _unstable_.

If the largest eigenvalue has absolute value 1, then we can again resort to
Equation {eq}`Eq:DynSystDiscrete:GenSolDiagble` to conclude that all sequences will remain bounded. Furthermore, starting from an eigenvector $\mathbf{v}$ for an eigenvalue of absolute value 1 it is seen that the process will not converge to the zero vector.

::::

::::{prf:remark}

Statement i. and ii. in {prf:ref}`Prop:DynSystDiscrete:DiagCase2` still hold in the case of repeated eigenvalues or complex eigenvalues. For complex eigenvalues $|\lambda_i|$ denotes the modulus of the number $\lambda_i$.

Thus, if the matrix has the (possibly complex) eigenvalues $\lambda_1, \ldots, \lambda_n$, the origin is an asymptotically stable point if all $|\lambda_i|$ are smaller than 1, and the origin is an unstable point if at least one of the eigenvalues has a modulus greater than 1.

The argument for a matrix with a repeated eigenvalue that does not provide a complete set of eigenvectors becomes more involved, as we cannot use Equation {eq}`Eq:DynSystDiscrete:GenSolDiagble` anymore. <BR>
Property iii. may fail if $\lambda_1$ is a double eigenvalue of modulus or absolute value 1. An example where this happens is given by the matrix

$$
   A = \left[\begin{array}{cc}
                          1 & 1 \\
                          0 & 1
      \end{array}\right].
$$

This matrix has the double eigenvalue $\lambda = 1$, with only one independent eigenvector.

It can be shown that

$$
   A^k = \left[\begin{array}{cc}
                          1 & k \\
                          0 & 1
      \end{array}\right],
$$

so

$$
  A^k \vect{x}_0 = \left[\begin{array}{cc}
                          1 & k \\
                          0 & 1
      \end{array}\right]\left[\begin{array}{c}
                          s_1 \\
                          s_2
      \end{array}\right] = \left[\begin{array}{c}
                          s_1+ks_2 \\
                          s_2
      \end{array}\right].
$$

For starting vectors $\vect{s} = \begin{bmatrix} s_1 \\ s_2\end{bmatrix}$ with $s_2 \neq 0$,  this will not be bounded.

::::

::::{prf:example}
:label: Ex:DynSystDiscrete:PopulationModel-2

In the population model of {prf:ref}`Ex:DynSystDiscrete:PopulationModel` we introduced the dynamical system with matrix

$$
   M =   \left[\begin{array}{cccc}   0   &  0   &  4   &  2 \\
                                    0.3  &  0   &  0   &  0 \\
                                     0   & 0.6  &  0   &  0  \\
                                     0   &  0   &  0.4 & 0.1
         \end{array}\right].
$$

Numerical computations show that the eigenvalues are given by

$$
  \lambda_1 = 0.9606, \quad \lambda_{2,3} = -0.3806\pm0.7788i, \quad \lambda_4 = -0.0997.
$$

Since $|\lambda_{2,3}| = 0.8668$ is smaller than 1 too,  the origin is a stable point.

So, pity for the population, but it is doomed to die out.

This may take quite a while, though. For instance, if at time 0 the population
is described by

$$
  \vect{x}_0 = \left[\begin{array}{cc} 1000\\1000\\2000\\3000 \end{array}\right],
$$

then (rounded to integers; recall it is just a model)

$$
  \vect{x}_1 = \left[\begin{array}{cc} 14000\\300\\600\\1100 \end{array}\right] , \quad \vect{x}_{10} = \left[\begin{array}{cc} 5910 \\ 684 \\ 965 \\ 573 \end{array}\right] , \quad \vect{x}_{50} = \left[\begin{array}{cc} 910 \\ 282 \\ 179\\ 82 \end{array}\right].
$$

The trajectories in $\R^4$ are hard to plot. Instead we can plot the progressions of the four age groups. {numref}`Figure %s <Fig:DynSystDiscrete:Leslie2>` shows these for the first 70 time periods.

:::{figure} Images/Fig-DynSystDiscrete-Leslie-2.svg
:name: Fig:DynSystDiscrete:Leslie2
:class: dark-light

The evolvement in time of the population model.
:::

What is not so clear in the picture is that for large $k$ the state vectors $\vect{x}_k$ are approximately eigenvectors for the matrix $M$. However, numerical values shed light on this phenomenon. For instance, the last two 'states' are given by

$$
  \vect{x}_{69}  \approx 681 \left[\begin{array}{c}  0.627 \\0.195\\0.122\\0.057 \end{array}\right], \quad
  \vect{x}_{70} \approx 655\left[\begin{array}{c}  0.626 \\0.195\\0.122\\0.057 \end{array}\right].
$$

The numbers in the vectors are the _fractions_ of the total population per age group.

It holds that the last vector

$$
    \left[\begin{array}{c}  0.626 \\0.195\\0.122\\0.057 \end{array}\right] \approx
    \vect{v}_{1} = \left[\begin{array}{c} 0.6259 \\ 0.1954 \\ 0.1220 \\0.0567 \end{array}\right],
$$

where up to four decimals $\vect{v}_1$
is an eigenvector of $M$ for its largest eigenvalue $\lambda_1 = 0.9606$.

Moreover, we observe that the decrease in the total population from $k = 69$ to $k = 70$ is given by

$$
   655/681 = 0.9618 \approx \lambda_1.
$$

::::

(Subsec:GraphicalDiscDynSyst)=

## Graphical analysis of discrete dynamical systems in $\R^2$.

In this subsection we will analyze dynamical systems

$$
\mathbf{x}_0 = \mathbf{s}, \quad \mathbf{x}_{k+1} = A\mathbf{x}_k, \,\, k=0,1,2,\ldots\,,
$$

where $A$ is a $2\times 2$ matrix.

::::{prf:definition}
:label: Defn:DynSystDiscrete:Path

The set of points

$$
 \mathbf{x}_0 \,(\,= \vect{s}), \,\, \mathbf{x}_1, \, \mathbf{x}_2, \, \mathbf{x}_3, \, \ldots
$$

in $\R^2$ is called the **trajectory** or **path** starting from $\mathbf{s}$.

::::

Note that the definition also makes sense in larger dimensions.

Let us start by considering a few examples. In the first two examples the matrices will
have two distinct real eigenvalues, hence they are (real) diagonalizable, in the third example the eigenvalues are complex (thus the matrix is complex diagonalizable).

::::{prf:example}
:label: Ex:DynSystDiscrete:SimplestSystem

Consider the dynamical system with
matrix $A = \left[\begin{array}{cc} 1.2 & 0 \\ 0 & 0.8 \end{array}\right]$.

Starting from any vector $\vect{x}_0 = \left[\begin{array}{cc} x_0 \\ y_0 \end{array}\right]$ we get the path

:::{math}
:label: Eq:DysSystDiscrete:SimplestSystem

\left[\begin{array}{cc} x_0 \\ y_0 \end{array}\right] \, \longrightarrow \,
\left[\begin{array}{cc} 1.2x_0 \\ 0.8y_0 \end{array}\right] \, \longrightarrow \,
\left[\begin{array}{cc} (1.2)^2x_0 \\ (0.8)^2y_0 \end{array}\right] \, \longrightarrow \,
\left[\begin{array}{cc} (1.2)^3x_0 \\ (0.8)^3y_0 \end{array}\right] \,\,\, \ldots
:::

In each step the $x$-coordinate gets a factor $1.2$ and the $y$-coordinate is reduced by a factor $0.8$. <BR>
In {numref}`Fig:DynSystDiscrete:SimplestSystem` the paths are shown for the starting points $(0, \pm 8)$, $(\pm 1,\pm 8)$, $(\pm 2,\pm 8)$, and $(\pm 1,0)$. The paths, consisting of isolated points, are denoted by dots. The line segments are only drawn to make clear how the dynamical system moves from one point to the next.

:::{figure} Images/Fig-DynSystDiscrete-SimplestSystem.svg
:name: Fig:DynSystDiscrete:SimplestSystem
:class: dark-light

A very simple dynamical system.

:::

It seems clear from the picture, and it is clear from the general solution

$$
   \vect{x}_k = A^k \vect{x}_0 = \left[\begin{array}{cc} 1.2^kx_0 \\ 0.8^k y_0 \end{array}\right]
$$

that all solutions starting on the $y$-axis will converge to the origin and all other solutions will go to $\pm \infty$ while getting closer and closer to the $x$-axis. <BR>
To be more precise, if $x_0 > 0$ then $\vect{x}_k \to \left[\begin{array}{c} \infty \\ 0 \end{array}\right]$, and if $x_0 < 0$ then $\vect{x}_k \to \left[\begin{array}{c} -\infty \\ 0 \end{array}\right]$.

::::

::::{exercise}

Check how in {prf:ref}`Ex:DynSystDiscrete:SimplestSystem` we can use
{prf:ref}`Prop:DynSystDiscrete:DiagCase` to arrive at the same conclusion.
::::

::::{prf:example}
:label: Ex:DynSystDiscrete:NiceNode

Consider the dynamical system with
matrix $A = \left[\begin{array}{cc} 0.5 & 0.2 \\ -0.2 & 1.0 \end{array}\right]$.

{numref}`Fig:DynSystDiscrete:NiceNode` shows a few trajectories. On each of them the direction of the points $\vect{x}_k$ is towards the origin.

:::{figure} Images/Fig-DynSystDiscrete-NiceNode.svg
:name: Fig:DynSystDiscrete:NiceNode
:class: dark-light

A dynamical system with a stable node.

:::

The behaviour is most easily explained by looking at the eigenvalues and eigenvectors
(as in {prf:ref}`Prop:DynSystDiscrete:DiagCase`). They are

<!--

<center>

    $\lambda_1 = 0.9$, with $\vect{v}_1 = \left[\begin{array}{cc} 1 \\ 2 \end{array}\right]$ \nbsp;
    and \nbsp; $\lambda_2 = 0.6$, with $\vect{v}_2 = \left[\begin{array}{cc} 2 \\ 1 \end{array}\right]$

</center>

werkt niet ;-(  -->


$$
  \lambda_1 = 0.9, \,\text{with} \,\,\vect{v}_1 = \left[\begin{array}{cc} 1 \\ 2 \end{array}\right], \quad
   \lambda_2 = 0.6, \,\text{with} \,\,\vect{v}_2 = \left[\begin{array}{cc} 2 \\ 1 \end{array}\right]
$$

So if

$$
 \vect{x}_0 = c_1\vect{v}_1 +  c_2\vect{v}_2,
$$

then

$$
 \vect{x}_k = 0.9^kc_1 \vect{v}_1 +  0.6^kc_2\vect{v}_2.
$$

If $c_1 = 0$, then $\vect{x}_k \to \vect{0}$ along the line generated by $\vect{v}_2$.

If $c_1 \neq 0$, then

$$
  \vect{x}_k = 0.9^k\left(c_1 \vect{v}_1 +  \left(\dfrac{0.6}{0.9}\right)^kc_2\vect{v}_2\right).
$$

For large values of $k$ the second term within the parentheses becomes negligible compared to the first, so ultimately the points $\mathbf{x}_k$ will move towards the origin in the direction of the eigenvector $\vect{v}_1$, the eigenvector corresponding to the largest eigenvalue. Which can be clearly observed in {numref}`Fig:DynSystDiscrete:NiceNode`.

::::

In the third example the matrix $A$ has complex eigenvalues.

::::{prf:example}
:label: Ex:DynSystDiscrete:SpiralPoint

Consider the dynamical system with
matrix $A = \left[\begin{array}{cc} 1.3 &  -0.7 \\ 0.7  &  0.5 \end{array}\right]$.

{numref}`Fig:DynSystDiscrete:Spiral1A` shows the trajectories starting from the points
$(1,-1)$ and $(-1,1)$. On each of them the direction of the points $\vect{x}_k$ is along a spiral, away from the origin.

:::{figure} Images/Fig-DynSystDiscrete-Spiral1A.svg
:name: Fig:DynSystDiscrete:Spiral1A
:class: dark-light

A dynamical system with a spiral point.

:::

Again the eigenvalues and eigenvectors, in this case complex, explain what is going on.
The matrix $A$ has the eigenvalues $\lambda_{1,2} = 0.9 \pm 0.5745i$, with modulus
$|\lambda_i| = 1.0677$. <BR>
An eigenvector corresponding to $\lambda = 0.9 - 0.5745i$ is given
by

$$
  \vect{v} = \left[\begin{array}{c} 0.5714-0.8207i \\ 1 \end{array}\right] =
  \left[\begin{array}{c} 0.5714 \\ 1 \end{array}\right] +
  \left[\begin{array}{c} -0.8207 \\ 0 \end{array}\right]i .
$$

According to {prf:ref}`Prop:ComplexEV:HiddenRotation` $A$ can be written as $PCP^{-1}$
where

$$
  P = \left[\begin{array}{cc} 0.5714 &  -0.8207  \\ 1 & 0\end{array}\right],
$$

and

$$
  C =  \left[\begin{array}{cc} 0.9 & -0.5745  \\ 0.5745 & 0.9\end{array}\right] = r \left[\begin{array}{cc} \cos{\vartheta} & -\sin{\vartheta} \\
                                \sin{\vartheta} & \cos{\vartheta} \end{array}\right].
$$

For the given matrix $A$ we have $r = |\lambda_i| = 1.0677$, $\vartheta \approx 0.5681 \approx 0.1808  \pi$.

If we define the dynamical system

$$
  \vect{y}_{k+1} = C\vect{y}_k, \quad \vect{y}_0 = \vect{s},
$$

then $\vect{y}_{k+1}$ is found by rotating $\vect{y}_k$ over an angle $0.1808\pi$,
and next scaling the resulting vector with a factor $|\lambda_i| \approx 1.07$.
Figure {numref}`Fig:DynSystDiscrete:Spiral1A` shows a trajectory of this process.
The indicated radii make equal angles with each other and show that the points make a complete loop in about 11 steps. Indeed,

$$
  11\cdot0.1808\pi = 1.9888\pi \approx 2\pi.
$$

:::{figure} Images/Fig-DynSystDiscrete-Spiral1B.svg
:name: Fig:DynSystDiscrete:Spiral1B
:class: dark-light

One trajectory $\vect{y}_0$, $\vect{y}_1$, $\vect{y}_2$, $\ldots$.

:::

The trajectory in terms of the $\vect{x}$ vectors is the image of the trajectory in terms of the $\vect{y}$ vectors under the transformation $\vect{y} \mapsto P\vect{y} = \vect{x}$.

To see why this is the case:

if &nbsp; $\vect{y}_{k+1} = C\vect{y}_k$, &nbsp; and &nbsp; $\vect{x} = P\vect{y}$, &nbsp; so &nbsp; $\vect{y} = P^{-1}\vect{x}$, &nbsp; then

$$
   \vect{x}_{k+1} = P\vect{y}_{k+1} = PC\vect{y}_k = PCP^{-1}\vect{x}_k = A\vect{x}_k.
$$

::::

Let us introduce some terminology to describe the behaviour of the dynamical systems in the previous three examples.

::::{prf:definition}
:label: Dfn:DynSystDiscrete:Types

Let $A$ be a $2 \times 2$ matrix with eigenvalues $\lambda_1$ and $\lambda_2$.

If $0 < \lambda_1 < 1 < \lambda_2$ then the origin is called a **saddle point**.

If $0 < \lambda_1 < \lambda_2 < 1$ the origin is called a **stable node**.

If $1 < \lambda_1 < \lambda_2$ the origin is called an **unstable node**.

If $\lambda_{1,2} = \alpha \pm i\beta$, with $\beta \neq 0$, then if $|\lambda_i| < 1$, the origin is called a **stable spiral point**, and if $|\lambda_i| > 1$ it is an
**unstable spiral point**.

Lastly, if $\lambda_{1,2} = \alpha \pm i\beta$, with $\beta \neq 0$ and $|\lambda_i| = 1$, the origin is called a **center point**

::::

::::{exercise}
:label: Exc:DynSystDiscrete:Classification

Classify the behaviour of the origin in {prf:ref}`Ex:DynSystDiscrete:SimplestSystem` ,
{prf:ref}`Ex:DynSystDiscrete:NiceNode` and
{prf:ref}`Ex:DynSystDiscrete:SpiralPoint` according to {prf:ref}`Dfn:DynSystDiscrete:Types`.
::::

::::{prf:remark}

If one of the eigenvalues of the matrix $A$ is negative, the paths of the process can be
rather erratic, in particular if there is an eigenvalue smaller than $-1$. <BR>
For the borderline cases where either one of the eigenvalues is equal to 1
or where $\lambda_{1,2}$ are complex with modulus 1, see {numref}`Exc:DynSystDiscrete:Eigenvalue=1` and {numref}`Exc:DynSystDiscrete:Modulus=1`.

Note that we just ignore the case where the matrix $A$ has a double eigenvalue.

::::

::::{exercise}
:label: Exc:DynSystDiscrete:Eigenvalue=1

The matrix $A = \left[\begin{array}{cc} -1 & 2 \\ -3 & 4 \end{array}\right]$
has the following eigenvalues and eigenvectors

$$
  \lambda_1 = 1,\,\,\vect{v}_1 =  \left[\begin{array}{c} 1 \\ 1 \end{array}\right],
  \quad
  \lambda_2 = 2,\,\,\vect{v}_2 =  \left[\begin{array}{c} 2 \\ 3 \end{array}\right].
$$

Describe and sketch the trajectories starting from the 'states'

$$
  \vect{s}_1 = \left[\begin{array}{c} 1 \\ 0 \end{array}\right] \quad \text{and} \quad
  \vect{s}_2 = \left[\begin{array}{c} 0 \\ 1 \end{array}\right].
$$

::::

::::{exercise}
:label: Exc:DynSystDiscrete:Modulus=1

The matrix $A = \left[\begin{array}{cc} 1.2 & 1 \\ -1 & 0 \end{array}\right]$
has the eigenvalues $0.6 \pm 0.8i$. <BR>
Show that all paths that start from an initial point that is not the origin will stay away from the origin but will stay within a fixed distance from the origin.

In fact, one can show that the trajectories lie on _ellipses_. Can you give equations for these ellipses?

Are the paths periodic? That is, will $\vect{x}_k$ return to the starting value $\vect{s}$ for a certain $k$? From there the process will then start anew.
::::

## Application: linear difference equations

::::{prf:definition}
:label: Dfn:DynSystDiscrete

A **linear $n$th order difference equation** is an equation of the form

$$
  y(k) = a_1y(k-1) + a_2y(k-2) + \ldots + a_ny(k-n),
$$

for $k = n, n+1, \ldots$. <BR>
The _coefficients_ $a_i, i = 1,\ldots, n$ are real numbers.

Usually the equation comes with **initial values**

$$
   y(0) = s_0,\quad y(1) = s_1,\,\,\, \ldots \,\, , \,\,\, y(n-1) = s_{n-1}.
$$

::::

Note that all $y(k)$ are numbers here. Furthermore, verify that the initial values are exactly enough to determine $y(n),y(n+1), \ldots$ by repeatedly applying the difference equation.

::::{prf:example}

Consider the linear difference equation

$$
  y(k) = y(k-1) - 2y(k-2) + 3y(k-3), \quad k = 3,4, \ldots
$$

with the initial values

$$
   y(0) = 4,\,\,\,y(1) = 5,\,\,\,  y(2) = 6.
$$

Then

$$
   \begin{array}{ccccl}
          y(3) &=& y(2) - 2y(1) + 3y(0) &=& 6 - 10 + 12 = 8, \\
          y(4) &=& y(3) - 2y(2) + 3y(1) &=& 8 - 12 + 15 = 11, \\
          y(5) &=& y(4) - 2y(3) + 3y(2) &=& 11 - 16 + 18 = 13,
   \end{array}
$$

etc.

::::

The following example shows how the problem can be turned into a discrete dynamical system by a simple twist.

::::{prf:example}
:label: Ex:DynSystDiscrete:ToDynSystem

Consider the difference equation

$$
  \left\{ \begin{array}{l}
     y(k) = 2y(k-1) - 3y(k-2) + 5y(k-3),\\
     y(0)=1, \quad y(1)=3, \quad y(2)=0
     \end{array} \right.
$$

Define $\vect{x}_k = \left[\begin{array}{c} y(k) \\ y(k+1) \\ y(k+2) \end{array}\right]$,
for $k = 0,1,2,3,\ldots$

Then

$$
  \vect{x}_{k+1} = \left[\begin{array}{c} y(k+1) \\ y(k+2) \\ y(k+3) \end{array}\right] =
  \left[\begin{array}{c} y(k+1) \\ y(k+2) \\ 2y(k+2)  - 3y(k+1) + 5y(k)  \end{array}\right],
$$

so

$$
  \vect{x}_{k+1} =
  \left[\begin{array}{ccc}    0 & 1  & 0 \\ 0 & 0 & 1\\ 5 & -3 & 2     \end{array}\right]
  \left[\begin{array}{c} y(k) \\ y(k+1) \\ y(k+2) \end{array}\right] = A \vect{x}_k.
$$

Furthermore,

$$
  \vect{x}_0 = \left[\begin{array}{c} y(0) \\ y(1) \\ y(2) \end{array}\right] =
               \left[\begin{array}{c} 1 \\ 3 \\ 0 \end{array}\right].
$$

::::

This example hopefully suffices to convince you that every linear $n$th order difference equation can be put into the form of a discrete dynamical system.

Let us consider the probably most famous linear difference equation, by the way also a population model (something to do with rabbits; the search term "Fibonacci rabbits" will generate a long list of explanations).

::::{prf:example}
:label: Ex:DynSystDiscrete:Fibonacci

The **Fibonacci sequence** $f_0,f_1,f_2, \ldots$ is defined via

:::{math}
:label: Eq:DynSystDiscrete:DfnFibo

f_0 = 0, \, f_1 = 1, \,\, f_{n+1} = f_n + f_{n-1},\,\,\,n = 1,2,\ldots
:::

So the first thirteen terms of the sequence are

$$
  0,\,1,\,1,\,2,\,3,\,5,\,8,\,13,\,21,\,34,\,55,\,89,\,144.
$$

Using a diagonalization we will show the surprising formula

:::{math}
:label: Eq:DynSystDiscrete:Fibonacci

f_k = \frac1{\sqrt{5}} \left(\dfrac{1+\sqrt{5}}{2}\right)^{k} -
\frac1{\sqrt{5}} \left(\dfrac{1-\sqrt{5}}{2}\right)^{k}.

:::

We call the formula surprising, since at first sight the expression on the right in Equation {eq}`Eq:DynSystDiscrete:Fibonacci` is not an integer, where from the definition {eq}`Eq:DynSystDiscrete:DfnFibo` it immediately follows that the Fibonacci numbers are _integers_.

However, the computation of the complicated expression for $k = 3$

$$
\begin{array}{cl}
    & \dfrac1{\sqrt{5}} \left(\dfrac{1+\sqrt{5}}{2}\right)^{3} -
      \dfrac1{\sqrt{5}} \left(\dfrac{1-\sqrt{5}}{2}\right)^{3} \\
  = & \dfrac{(1+\sqrt{5})^3}{8\sqrt{5}} - \dfrac{(1-\sqrt{5})^3}{8\sqrt{5}} \\
  = & \dfrac{1 + 3\sqrt{5} + 15 + 5\sqrt{5}}{8\sqrt{5}} -
  \dfrac{1 - 3\sqrt{5} + 15 - 5\sqrt{5}}{8\sqrt{5}} \\
  = & \dfrac{16 + 8\sqrt{5} }{8\sqrt{5}} -
  \dfrac{16 - 8\sqrt{5}}{8\sqrt{5}} = 2  = f_3
  \end{array}
$$

gives us some confidence.

Let us now derive Equation {eq}`Eq:DynSystDiscrete:Fibonacci`.

Introducing $\vect{x}_{k} = \left[\begin{array}{c} f_{k} \\  f_{k+1} \end{array}\right]$
and using the identity

$$
  \left[\begin{array}{c} f_{k+1} \\  f_{k+2} \end{array}\right] = \left[\begin{array}{c} f_{k+1} \\  f_{k}+ f_{k+1} \end{array}\right] = \left[\begin{array}{cc} 0 & 1\\ 1 & 1 \end{array}\right] \left[\begin{array}{c} f_{k}\\  f_{k+1} \end{array}\right],
$$

we find as dynamical system corresponding to {eq}`Eq:DynSystDiscrete:DfnFibo` the system

$$
  \vect{x}_{k+1} = A\vect{x}_{k} =  \left[\begin{array}{cc} 0 & 1\\ 1 & 1 \end{array}\right]\vect{x}_{k}, \quad \vect{x}_{0} =  \left[\begin{array}{c} 0 \\  1 \end{array}\right].
$$

The matrix $A$ has the characteristic polynomial

$$
   p_A(\lambda) = (0-\lambda)\cdot(1-\lambda) - 1 = \lambda^2 - \lambda - 1.
$$

This gives the zeros/eigenvalues $\lambda_{1} = \dfrac{1+\sqrt{5}}{2}$, $\lambda_{2} = \dfrac{1-\sqrt{5}}{2}$, with corresponding eigenvectors

$$
  \vect{v}_1 = \left[\begin{array}{cc} 1 \\ \frac12(1+\sqrt{5})  \end{array}\right], \quad
  \vect{v}_2 = \left[\begin{array}{cc} 1 \\ \frac12(1-\sqrt{5})  \end{array}\right]
$$

respectively. So $A$ is diagonalizable, and we can use {prf:ref}`Prop:DynSystDiscrete:DiagCase` to find the general state vector $\vect{x}_k$.

For this we have to find the coordinates $(c_1, c_2)$ of $\vect{s}$ with respect to the basis $(\vect{v}_1,\vect{v}_2)$. A short computation shows that

$$
  \left[\begin{array}{c} 0\\ 1  \end{array}\right] = c_1\left[\begin{array}{c} 1 \\ \frac12(1+\sqrt{5})  \end{array}\right] + c_2\left[\begin{array}{c} 1 \\ \frac12(1-\sqrt{5})  \end{array}\right] \iff
  \left[\begin{array}{c} c_1\\ c_2  \end{array}\right] = \dfrac{1}{\sqrt{5}}\left[\begin{array}{c} 1\\ -1  \end{array}\right].
$$

This gives us

$$
  \vect{x}_k = \left[\begin{array}{c} f_{k} \\  f_{k+1} \end{array}\right] = c_1\lambda_1^k \vect{v}_1 + c_2\lambda_2^k \vect{v}_2  = \tfrac{1}{\sqrt{5}}\lambda_1^k \vect{v}_1 - \tfrac{1}{\sqrt{5}}\lambda_2^k \vect{v}_2.
$$

For the $k$th Fibonacci number we only need the first entry, which yields that

$$
  f_k = \frac{1}{\sqrt{5}} \left(\dfrac{1+\sqrt{5}}{2}\right)^k -
        \frac{1}{\sqrt{5}} \left(\dfrac{1-\sqrt{5}}{2}\right)^k,
$$

which is indeed the expression presented in Equation {eq}`Eq:DynSystDiscrete:Fibonacci`.

Noting that $0 < \frac12(\sqrt{5}-1) < 1 < \frac12(\sqrt{5}+1)$ we can see that eventually
$f_k$ more or less grows with a factor $r = \frac12(\sqrt{5}+1)$, the so-called _golden ratio_. More precisely, for large values of $k$ we find that

$$
   f_{k+1} \approx  r\,f_k \quad \text{and also} \quad f_k \approx c r^k,\,\,
   c = \tfrac1{\sqrt{5}}.
$$

Using the fact that $f_k$ is always an integer, we can go a bit further. If we define

$$
   a_k = \frac{1}{\sqrt{5}} \left(\dfrac{1+\sqrt{5}}{2}\right)^k, \quad  b_k = \frac{1}{\sqrt{5}} \left(\dfrac{1-\sqrt{5}}{2}\right)^k,
$$

we see that

:::{math}
:label: Eq:DynSystDiscrete:FiboInteger

a_k = f_k + b_k,
:::

where as said, $f_k$ is an integer and moreover $-\frac12 < b_k < \frac12$. So if we round both sides of Equation {eq}`Eq:DynSystDiscrete:FiboInteger` to the nearest integer, the term $f_k + b_k$ rounds to the integer $f_k$. This means that

<center>

_$f_k$ is equal to $\dfrac{1}{\sqrt{5}} \left(\dfrac{1+\sqrt{5}}{2}\right)^k$ rounded to the nearest integer_.

</center>

For example, for $k=6$ we find &nbsp; $\left[\dfrac{1}{\sqrt{5}}\left(\dfrac{1+\sqrt{5}}{2}\right)\right]^6 = 8.0249....$ , <BR>

which rounds correctly to the sixth Fibonacci number $f_6 = 8$.
::::


