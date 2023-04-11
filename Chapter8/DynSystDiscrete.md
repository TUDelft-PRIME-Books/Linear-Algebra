(Sec:DynSystDiscrete)=
# Discrete Dynamical Systems

## Introduction

For a linear transformation $T: \R^n \to \R^n$, instead of looking at the image of subsets under $T$, we may also follow the 'path' of one vector $\vect{x}_0$ under repeated application of $T$.  In case $T$ is represented by the matrix $A$ this means we will study the sequence

$$
   \vect{x}_0,\,\, \vect{x}_1,\,\,\vect{x}_2,\,\,\ldots \,\,\, = \,\,\,\vect{x}_0,\,\,A\vect{x}_0,\,\,A^2\vect{x}_0,\,\ldots
$$

In  {prf:ref}`Ex:Diagonalize:DiagonalizeMigration` in {numref}`Section %s <Sec:Diagonalize>`  we considered a migration model.

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
   \end{array}.  
$$

The table has to be read column by column.  For instance, the meaning of the first column is that  of the age group  'young', 30\% reaches the adolescent state.  And from the third column it can be read off that 
individuals of the age group 'full grown'  reproduce 4 offspring and with probability 40% reach 'old age'.  The graph in {numref}`Figure %s <Fig:DynSystDiscrete:Leslie>` visualizes the table.


:::{figure} Images/Fig-DynSystDiscrete-LeslieGraph.svg
:name: Fig:DynSystDiscrete:Leslie

:::



One of the questions of interest here is whether with these numbers the propulation will survive or die out.

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

In the context of population dynamics, the matrix $M$  would be called a **Leslie matrix**.

::::


Both examples lead to a so-called discrete dynamical system.

::::{prf:definition}
:label: Def:DynSystDiscr:DiscreteDynSyst

Suppose $A$ is an $n \times n$ matrix, and $\vect{s}$ a vector in $\R^n$.

The **discrete dynamical system** with matrix $A$ and initial state $\vect{s}$ is the process described by 

$$
  \vect{x}_0 = \vect{s}, \quad \vect{x}_{k+1} = A\vect{x}_k, \,\,k = 0,1,2,\ldots
$$

::::

In this subsection we will address the questions whether we can give an 'explicit' expression for the general state $\mathbf{x}_k$, and what is the behaviour 'on the 'long run',  i.e., when $k \to \infty$.

## The case where $A$ is diagonalizable

If the matrix $A$ is diagonalizable, that is, if a basis of eigenvectors exists, the behaviour of the dynamical system can be made completely transparent.

::::{prf:proposition}
:label: Prop:DynSystDiscrete:DiagCase

Suppose  $A$ is an $n\times n$ diagonalizable matrix.
Let $(\vect{v}_1, \ldots, \vect{v}_n)$ be a basis of eigenvectors, and let 
$\lambda_1, \ldots, \lambda_n$ be the corresponding eigenvalues.

Then the behaviour of the dynamical system 

$$
  \vect{x}_{0} = \vect{s}, \quad  \vect{x}_{k+1} = A\vect{x}_k, \quad k = 0,1,2,\ldots
$$

is as follows.


If    

:::{math}
:label: Eq:DynSystDiscrete:InitCoords

 \vect{s} =  c_1\vect{v}_1 + c_2\vect{v}_2 +  \ldots + c_n\vect{v}_n,
:::

then

:::{math}
:label: Eq:DynSystDiscrete:GenSolDiagble

 \vect{x}_k =  c_1\lambda_1^k\vect{v}_1 + c_2\lambda_2^k\vect{v}_2 +  \ldots + c_n\lambda_n^k\vect{v}_n.

:::

The last expression for  $\vect{x}_k$ is often refered to as being the **general solution** of the dynamical system.

::::

Note that the coordinates  $c_1,c_2,\ldots,c_n$  in {eq}`Eq:DynSystDiscrete:InitCoords` are uniquely determined, since $(\vect{v}_1, \ldots, \vect{v}_n)$ is assumed to be a basis.


::::{prf:proof}

There is nothing much to prove.

The vectors $\vect{v}_i$  being eigenvectors for the corresponding $\lambda_i$ means that

$$
  A\vect{v}_i = \lambda_i\vect{v}_i.
$$

Thus

$$
  A^2\vect{v}_i = A(A\vect{v}_i) = A(\lambda_i\vect{v}_i) = \lambda_iA\vect{v}_i 
  =  \lambda_i^2\vect{v}_i,
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

From Equation {eq}`Eq:DynSystDiscrete:GenSolDiagble` it follows that if **all** eigenvalues have an absolute value smaller than 1, **all** solutions will approach the origin $\vect{0}$ if  $k \to \infty$.  In this case the origin is called (asymptotically) stable.  

::::{prf:definition}
:label: Def:DynSystDiscrete:Stable

Let $A$ be the matrix of a dynamical system. 
The origin is called **asymptotically stable**  if all solutions $\vect{x}_k$  go to $\vect{0}$ if $k \to \infty$.  If for some starting values $\vect{x}_0 = \vect{s}$ the solution $\vect{x}_k$ becomes arbitrarily large, i.e., if $\norm{\vect{x}_k} \to \infty$ for $k \to \infty$, then the dynamical system is called **unstable**. In the borderline case where the highest absolute value of the eigenvalues is exactly 1, the origin is just called **stable**.


In the case of asymptotic stability we will call the origin an **attractor**, in the case of instability we say the origin is a **repeller**.  
::::

::::{prf:remark}

This definition of stable and unstable suffices for *linear* dynamical systems.  For nonlinear systems a more subtle definition is needed.

Furthermore,  in the literature there is  quite a bit of terminology to describe the behaviour of dynamical systems around the origin. Apart from dynamical systems in the plane, where we can nicely visualize what is going on, we will stick to the two qualifications attractor and repellor.

::::

The following proposition is an almost immediate consequence of Equation {eq}`Eq:DynSystDiscrete:GenSolDiagble`. 

::::{prf:proposition}

Suppose the matrix $A$ is diagonalizable, with eigenvalues $\lambda_i$ ordered by absolute value,

$$
   |\lambda_1| \geq |\lambda_2| \geq \ldots \geq |\lambda_n|.
$$

Then

<ol type ="i">

<li>

  If  $|\lambda_1| < 1$  the origin is asymptotically stable.

</li>

<li>

  If  $|\lambda_1| > 1$  the origin is unstable.
  
</li>

<li>

  If  $|\lambda_1| = 1$  the origin is stable but not asymptotically stable.
  
</li>

</ul>
::::


::::{prf:remark}

The same conclusions as in {prf:ref}`Prop:DynSystDiscrete:DiagCase` may be drawn in the case of multiple eigenvalues or complex eigenvalues.  For  complex eigenvalues $|\lambda_i|$ then denotes the modulus of the number $\lambda_i$. 

That is,  if the matrix has the (possibly complex) eigenvalues  $\lambda_1, \ldots, \lambda_n$, the origin is an asymptotically stable point if all $|\lambda_i|$ are smaller than 1, and the origin is an unstable point if at least one of the eigenvalues has a modulus greater than 1.

The argument for a matrix  with multiple eigenvalues becomes more involved, as we cannot use   Equation {eq}`Eq:DynSystDiscrete:GenSolDiagble` anymore.

::::

::::{prf:example} 
:label: Ex:DynSystDiscrete:PopulationModel-2

In the population model of example {prf:ref}`Ex:DynSystDiscrete:PopulationModel` we introduced the dynamical system with matrix 

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

It appears that $|\lambda_{2,3}| = 0.8668 < 1$  too, thus the origin is a stable point here.

So, pity for the population, but it is doomed to die out.

This may take quite a while, though.  For instance, if at time 0 the population
is described by

$$
  \vect{x}_0 = \left[\begin{array}{cc} 1000\\1000\\2000\\3000 \end{array}\right],
$$

then  (rounded to integers;  recall it is just a model)

$$
  \vect{x}_1 = \left[\begin{array}{cc} 14000\\300\\600\\1100 \end{array}\right] , \quad \vect{x}_{10} = \left[\begin{array}{cc} 5910 \\ 684 \\ 965 \\ 573 \end{array}\right] , \quad \vect{x}_{50} = \left[\begin{array}{cc} 910 \\ 282 \\ 179\\ 82 \end{array}\right].
$$

The trajectories in $\R^4$ are hard to plot. Instead we can plot the progressions of the four age groups.  {numref}`Figure %s <Fig:DynSystDiscrete:Leslie>` shows these in time slots of five years.

:::{figure} Images/Fig-DynSystDiscrete-Leslie-2.svg
:name: Fig:DynSystDiscrete:Leslie

The evolvement in time of the population model
:::


What is not so clear in the picture is that for large $k$ the state vectors $\vect{x}_k$ are approximately eigenvectors for the matrix $M$. For instance,  

$$
  \vect{x}_{70} = \left[\begin{array}{cc}  612 \\190\\119\\55 \end{array}\right] \approx 612\cdot\left[\begin{array}{cc}  1.000 \\0.345 \\0.194\\ 0.090 \end{array}\right], \quad
  \vect{x}_{75} = \left[\begin{array}{cc}  499 \\156\\98\\45 \end{array}\right]
  \approx 499\cdot\left[\begin{array}{cc}  1.00 \\0.313 \\0.196\\ 0.090 \end{array}\right],
$$

where up to three decimals

$$
   \vect{v}_{1} = \left[\begin{array}{c} 1.000 \\ 0.312 \\ 0.195 \\0.090 \end{array}\right]
$$

is an eigenvector of $M$ for its largest eigenvalue $\lambda_1 = 0.9606$.
::::


## Graphical analysis of dynamical systems in $\R^2$.

In this subsection we analyze  dynamical systems  

$$ 
\mathbf{x}_0 = \mathbf{s}, \quad \mathbf{x}_{k+1} = A\mathbf{x}_k, \,\, k=0,1,2,\ldots\,,
$$

where $A$ is a $2\times 2$ matrix. 


::::{prf:definition}
:label: Defn:DynSystDiscrete:Path

The set of points  

$$
 \mathbf{x}_0 \,(\,= \vect{s}), \,\, \mathbf{x}_1, \, \mathbf{x}_2, \, \mathbf{x}_3, \ldots  
$$

is called the **trajectory** or **path**  starting from $\mathbf{s}$.

:::: 

Let us start by considering a few examples.  In the first two examples the matrices will
have two real eigenvalues, hence they are diagonalizable, in the third example the eigenvalues are complex.


::::{prf:example}
:label:  Ex:DynSystDiscrete:SimplestSystem

Consider the dynamical system with 
matrix  $A = \left[\begin{array}{cc} 1.2 & 0 \\ 0 & 0.8 \end{array}\right]$.

Starting from any vector  $\vect{x}_0 = \left[\begin{array}{cc} x_0 \\ y_0 \end{array}\right]$ we get the path

:::{math}
:label: Eq:DysSystDiscrete:SimplestSystem

  \left[\begin{array}{cc} x_0 \\ y_0 \end{array}\right]  \, \longrightarrow \,
  \left[\begin{array}{cc} 1.2x_0 \\ 0.8y_0 \end{array}\right]  \, \longrightarrow \,
  \left[\begin{array}{cc} (1.2)^2x_0 \\ (0.8)^2y_0 \end{array}\right]  \, \longrightarrow \,
  \left[\begin{array}{cc} (1.2)^3x_0 \\ (0.8)^3y_0 \end{array}\right]  \, \ldots 
:::

In  {numref}`Fig:DynSystDiscrete:SimplestSystem` the paths are shown for the starting points $(0, \pm 8)$, $(\pm 1,\pm 8)$,  $(\pm 2,\pm 8)$, and $(\pm 1,0)$.  The paths are in fact the asterisks. The  line segments are only drawn to make clear how the dynamical system moves from one point to the next.


:::{figure} Images/SimplestSystem.svg
:name: Fig:DynSystDiscrete:SimplestSystem

A very simple dynamical system

:::



It seems clear from the picture, and it is clear from the general solution
% {eq}`Eq:DysSystDiscrete:SimplestSystem` 

$$
   \vect{x}_k = A^k \vect{x}_0 = \left[\begin{array}{cc} 1.2^kx_0 \\ 0.8^k y_0 \end{array}\right]
$$

that all solutions starting on the $y$-axis will converge to the origin and all other solutions will go to $\pm \infty$ while getting closer and closer to the $x$-axis.

::::


::::{exercise}

Check how  in {prf:ref}`Ex:DynSystDiscrete:SimplestSystem` we can use
{prf:ref}`Prop:DynSystDiscrete:DiagCase` to arrive at the same conclusion.
::::

::::{prf:example}
:label: Ex:DynSystDiscrete:NiceNode

Consider the dynamical system with 
matrix  $A = \left[\begin{array}{cc} 0.5 & 0.2 \\ -0.2 & 1.0 \end{array}\right]$.

{numref}`Fig:DynSystDiscrete:NiceNode` shows a few trajectories. On each of them the direction of the points $\vect{x}_k$  is towards the origin.

:::{figure} Images/Fig-DynSystDiscrete-NiceNode.svg
:name: Fig:DynSystDiscrete:NiceNode

A dynamical system with a stable node

:::

The behaviour is most easily explained by looking at the eigenvalues and eigenvectors
(as in  {prf:ref}`Prop:DynSystDiscrete:DiagCase`).  They are

$$
  \lambda_1 = 0.9, \,\text{with} \,\,\vect{v}_1 = \left[\begin{array}{cc} 1 \\ 2 \end{array}\right], \quad 
   \lambda_1 = 0.6, \,\text{with} \,\,\vect{v}_2 = \left[\begin{array}{cc} 2 \\ 1 \end{array}\right]
$$

So if  

$$
 \vect{x}_0 = c_1\vect{v}_1 +  c_2\vect{v}_2,
$$

then  

$$
 \vect{x}_k = 0.9^kc_1 \vect{v}_1 +  (0.6)^kc_2\vect{v}_2.
$$ 

If $c_1 = 0$,  then  $\vect{x}_k \to \vect{0}$  along the line generated by $\vect{v}_2$.

If $c_1 \neq 0$, then

$$
  \vect{x}_k = 0.9^k\left(c_1 \vect{v}_1 +  \left(\dfrac{0.6}{0.9}\right)^kc_2\vect{v}_2\right).
$$

For large values of $k$ the second term becomes negligible compared to the first, so the points  $\mathbf{x}_k$  will move towards the origin in the direction of the eigenvector $\vect{v}_1$, the eigenvector corresponding to the largest eigenvalue.

::::

In the third example the matrix  $A$ has complex eigenvalues.



::::{prf:example}
:label: Ex:DynSystDiscrete:SpiralPoint

Consider the dynamical system with 
matrix  $A = \left[\begin{array}{cc} 1.6860 &  -0.9167 \\ 0.9167  &  0.2193 \end{array}\right]$.


{numref}`Fig:DynSystDiscrete:Spiral1B` shows the trajectories starting from the points
$(1,1)$ and $(-1,-1)$. On each of them the direction of the points $\vect{x}_k$  is away from the origin.

:::{figure} Images/Fig-DynSystDiscrete-Spiral1B.svg
:name: Fig:DynSystDiscrete:Spiral1B

A dynamical system with a spiral point

:::

Again the eigenvalues and eigenvectors, in this case complex, explain what is going on.
The matrix $A$ has the eigenvalues $\lambda_{1,2} = 0.9526 \pm 0.5500i$, with modulus
$|\lambda_i| = 1.1$.
An eigenvector corresponding to $\lambda = 0.9526 - 0.5500i$  is given 
by  $\vect{v} = \left[\begin{array}{cc} 0.8 - 0.6i \\ i \end{array}\right]$.

According to  {prf:ref}`Prop:ComplexEV:HiddenRotation` $A$ can be written as $PCP^{-1}$
where  

$$
  P = \left[\begin{array}{cc} 0.8 & - 0.6 \\ 0 & 1 \end{array}\right], \quad
  C = r \left[\begin{array}{cc} \cos{\vartheta} & -\sin{\vartheta} \\ 
                                \sin{\vartheta} & \cos{\vartheta} \end{array}\right].
$$

For the given matrix $A$ we have  $r = |\lambda_i| = 1.1$, $\vartheta = \frac16\pi$.

If we define the dynamical system 

$$
  \vect{y}_{k+1} = C\vect{y}_k, \quad \vect{y}_0 = \vect{s},
$$

then $\vect{y}_{k+1}$ is found by rotating  $\vect{y}_k$  over an angle $\frac16\pi$,
and next scaling the resulting vector with a factor  1.1.
Figure {numref}`Fig:DynSystDiscrete:Spiral1A` shows a trajectory of this process.

:::{figure} Images/Fig-DynSystDiscrete-Spiral1A.svg
:name: Fig:DynSystDiscrete:Spiral1A

One trajectory  $\vect{y}_0$, $\vect{y}_1$, $\vect{y}_2$, ..... 

:::

The trajectory in terms of the $\vect{x}$ vectors is the image of the trajectory in terms of the $\vect{y}$ vectors under the transformation $\vect{y} \mapsto P\vect{y} = \vect{x}$.

To see why this is the case:

if  &nbsp; $\vect{y}_{k+1} = C\vect{y}_k$, &nbsp; and &nbsp; $\vect{x} = P\vect{y}$,  so &nbsp; $\vect{y} = P^{-1}\vect{x}$, &nbsp; then

$$
   \vect{x}_{k+1} = P\vect{y}_{k+1} = PC\vect{y}_k = PCP^{-1}\vect{x}_k = A\vect{x}_k.
$$

::::

Let us introduce some terminology to describe the behaviour of the dynamical systems in the previous three examples.

::::{prf:definition}
:label: Dfn:DynSystDiscrete:Types

Let  $A$ be a $2 \times 2$ matrix with eigenvalues  $\lambda_1$ and $\lambda_2$.  

If $0 < \lambda_1 < 1 < \lambda_2$ then the origin is called a **saddle point**.

If $0 < \lambda_1 < \lambda_2 < 1$ the origin is called a **stable node**.

If $1 < \lambda_1 < \lambda_2$ the origin is called an **unstable node**.

If $\lambda_{1,2} = \alpha \pm i\beta$, with $\beta \neq 0$, then if  $|\lambda_i| < 1$, the origin is called a **stable spiral point**, and if $|\lambda_i| > 1$ it is an 
**unstable spiral point**.

::::


::::{exercise}
:label: Exc:DynSystDiscrete:Classification

Classify the behaviour of the origin in  {prf:ref}`Ex:DynSystDiscrete:SimplestSystem` ,
{prf:ref}`Ex:DynSystDiscrete:NiceNode`  and
{prf:ref}`Ex:DynSystDiscrete:SpiralPoint` according to {prf:ref}`Dfn:DynSystDiscrete:Types`.
::::

::::{prf:remark}

If one of the eigenvalues of the matrix $A$ is negative, the paths of the process are 
rather erratic. For the borderline cases where either one of the eigenvalues is equal to 1
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
  \lambda_2 = 2,\,\,\vect{v}_2 =  \left[\begin{array}{c} 2 \\ 3 \end{array}\right]
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
has the eigenvalues $0.6 \pm 0.8i$. Show that all paths that start from a starting point that is not the origin will stay away from the origin and stay within a fixed distance from the origin.

Are the paths periodic?  That is, will $\vect{x}_k$  return to the starting value $\vect{s}$ for a certain $k$?  From there the process will then start anew. 
::::



## Application: linear difference equations

::::{prf:definition}
:label: Dfn:DynSystDiscrete

A  **linear $n$th order difference equation** is an equation of the form

$$
  y(k) = a_1y(k-1) + a_2y(k-2) + \ldots + a_ny(k-n), \quad k = n,n+1,n+2, \ldots
$$

where   the  **coefficients**  $a_i$ are real numbers.

Usually the equation comes with **initial values**  

$$
   y(0) = s_0,\,\,y(1) = s_1,\,\, \ldots \,\, , \,\, y(n-1) = s_{n-1}.
$$

::::


The following example shows how by a simple twist the problem can be turned into a discrete dynamical system.

::::{prf:example}
:label: Ex:DynSystDiscrete:ToDynSystem

Consider the difference equation 

$$
  \left\{ \begin{array}{l}
     y(k) = 2y(k-1) - 3y(k-2) + 5y(k-3),\\
     y(0)=1, \quad y(1)=3, \quad y(2)=0
     \end{array} \right.
$$

Define  $\vect{x}_k = \left[\begin{array}{c} y(k+2) \\ y(k+1) \\ y(k) \end{array}\right]$.

Then

$$
  \vect{x}_{k+1} = \left[\begin{array}{c} y(k+3) \\ y(k+2) \\ y(k+1) \end{array}\right] =
  \left[\begin{array}{c} 2y(k+2) - 3y(k+1) + 5y(k) \\ y(k+2) \\ y(k+1) \end{array}\right],
$$

so

$$
  \vect{x}_{k+1} = 
  \left[\begin{array}{ccc} 2 & -3 & 5 \\  1 & 0 & 0\\  0 & 1  & 0    \end{array}\right]
  \left[\begin{array}{c} y(k+2) \\ y(k+1) \\ y(k) \end{array}\right] = A \vect{x}_k.
$$

Furthermore,

$$
  \vect{x}_0 = \left[\begin{array}{c} y(2) \\ y(1) \\ y(0) \end{array}\right] = 
               \left[\begin{array}{c} 0 \\ 3 \\ 1 \end{array}\right].
$$

::::

This example hopefully suffices to convince you that every linear $n$th order difference equation can be put into the form of a discrete dynamical system.

Let us consider the probably most famous linear difference equation, by the way also a population model  (something to do with rabbits; the search term "Fibonacci rabbits" will generate a long list of explanations).

::::{prf:example}
:label: Ex:DynSystDiscrete:Fibonacci

The **Fibonacci sequence** $f_0,f_1,f_2, \ldots$  is defined via

:::{math}
:label: Eq:DynSystDiscrete:DfnFibo

   f_0 = f_1 = 1, \,\, f_{n+1} = f_n + f_{n-1},\,\,\,n = 1,2,\ldots
:::

So the first  twelve terms of the sequence are

$$
  1,\,1,\,2,\,3,\,5,\,8,\,13,\,21,\,34,\,55,\,89,\,144.
$$

Using a diagonalization we will show the surprising formula

:::{math}
:label: Eq:DynSystDiscrete:Fibonacci
   
   f_k = \frac1{\sqrt{5}} \left(\dfrac{1+\sqrt{5}}{2}\right)^{k+1} - 
      \frac1{\sqrt{5}} \left(\dfrac{1-\sqrt{5}}{2}\right)^{k+1}. 

:::

Noting that  $0 < \frac12(\sqrt{5}-1) < 1 < \frac12(\sqrt{5}+1)$ we can see that eventually
 $f_k$ more or less grows with a factor $r = \frac12(\sqrt{5}+1)$.  More precisely, for large values of $k$ we find that

$$
   f_{k+1} \approx  r\,f_k \quad \text{and also} \quad f_k \approx c r^k,\,\, 
   c = \tfrac1{\sqrt{5}}.
$$ 

We call the formula  surprising, since at first sight the expression on the right in equation {eq}`Eq:DynSystDiscrete:Fibonacci` is not an integer, where the Fibonacci numbers clearly  are integers.

However, the computation of the complicated expression for $k = 2$

$$ \begin{array}{cl}
    & \dfrac1{\sqrt{5}} \left(\dfrac{1+\sqrt{5}}{2}\right)^{3} - 
      \dfrac1{\sqrt{5}} \left(\dfrac{1-\sqrt{5}}{2}\right)^{3} \\
  = & \dfrac{(1+\sqrt{5})^3}{8\sqrt{5}} - \dfrac{(1-\sqrt{5})^3}{8\sqrt{5}} \\
  = & \dfrac{1 + 3\sqrt{5} + 15 + 5\sqrt{5}}{8\sqrt{5}} - 
  \dfrac{1 - 3\sqrt{5} + 15 - 5\sqrt{5}}{8\sqrt{5}} \\
  = & \dfrac{16 + 8\sqrt{5} }{8\sqrt{5}} - 
  \dfrac{16 - 8\sqrt{5}}{8\sqrt{5}} = 2  = f_2
  \end{array}
$$

gives us some confidence.

Let us now derive equation {eq}`Eq:DynSystDiscrete:Fibonacci`.

Introducing  $\vect{x}_{k} = \left[\begin{array}{c} f_{k+1} \\  f_k \end{array}\right]$ 
and using the identity

$$
  \left[\begin{array}{c} f_{k+2} \\  f_{k+1} \end{array}\right] = \left[\begin{array}{c} f_{k+1}+f_{k} \\  f_{k+1} \end{array}\right] = \left[\begin{array}{cc} 1 & 1\\ 1 & 0 \end{array}\right] \left[\begin{array}{c} f_{k+1}\\  f_{k} \end{array}\right],
$$

we find  as  dynamical system corresponding to {eq}`Eq:DynSystDiscrete:DfnFibo` the system

$$
  \vect{x}_{k+1} = A\vect{x}_{k} =  \left[\begin{array}{cc} 1 & 1\\ 1 & 0 \end{array}\right]\vect{x}_{k}, \quad \vect{x}_{0} =  \left[\begin{array}{c} 1 \\  1 \end{array}\right].
$$

The matrix $A$ has the characteristic polynomial

$$
   p_A(\lambda) = (1-\lambda)\cdot(0-\lambda) - 1 = \lambda^2 - \lambda - 1.
$$

This gives the zeros/eigenvalues $\lambda_{1} = \dfrac{1+\sqrt{5}}{2}$, $\lambda_{2} = \dfrac{1-\sqrt{5}}{2}$,  with corresponding eigenvectors

$$
  \vect{v}_1 = \left[\begin{array}{cc} \frac12(1+\sqrt{5})\\ 1  \end{array}\right], \quad
  \vect{v}_2 = \left[\begin{array}{cc} \frac12(1-\sqrt{5})\\ 1  \end{array}\right] 
$$

respectively.  So $A$ is diagonalizable, and we can use {prf:ref}`Prop:DynSystDiscrete:DiagCase` to find the general state vector $\vect{x}_k$.

For this we have to find the coordinates $(c_1, c_2)$ of $\vect{s}$ with respect to the basis $(\vect{v}_1,\vect{v}_2)$.  

$$
  \left[\begin{array}{c} 1\\ 1  \end{array}\right] = c_1\left[\begin{array}{c} \frac12(1+\sqrt{5})\\ 1  \end{array}\right] + c_2\left[\begin{array}{c} \frac12(1-\sqrt{5})\\ 1  \end{array}\right] \iff
$$

$$
  \left[\begin{array}{c} c_1\\ c_2  \end{array}\right] =
  \left[\begin{array}{cc} \frac12(1+\sqrt{5}) & \frac12(1-\sqrt{5})\\ 1 &1 \end{array}\right]^{-1}
  \left[\begin{array}{c} 1\\ 1  \end{array}\right] \,\,=\,\,
  \frac{1}{2\sqrt{5}} \left[\begin{array}{c} 1+\sqrt{5}\\ -1+\sqrt{5}  \end{array}\right].
$$

This gives us

$$
  \vect{x}_k = \left[\begin{array}{c} f_{k+1} \\  f_k \end{array}\right] = c_1\lambda_1^k \vect{v}_1 + c_2\lambda_2^k \vect{v}_2
$$

For the $k$th Fibonacci number we only need the second entry, which yields that

$$  
  f_k = \frac{1+\sqrt{5}}{2\sqrt{5}} \left(\dfrac{1+\sqrt{5}}{2}\right)^k  +
        \frac{-1+\sqrt{5}}{2\sqrt{5}} \left(\dfrac{1-\sqrt{5}}{2}\right)^k,      
$$

which is equivalent to the expression in Equation {eq}`Eq:DynSystDiscrete:Fibonacci`.

::::


