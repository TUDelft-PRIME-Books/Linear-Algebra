(Section:SolutionSets)=

# The Solution Set of a System of Linear Equations

As we have seen in {numref}`Sec:LinesAndPlanes`, the solutions of a single linear equation with $2$ variables form a line in the plane. Similarly, the solutions of a single linear equation in $3$ variables form a plane in three-dimensional space. If we want to know which points lie in the intersection of two planes, we therefore have to find those points that solve two equations simultaneously. This raises some very natural questions: what is the set of vectors that satisfy a number of given equations? What does this set look like geometrically?

Also in {numref}`Sec:LinesAndPlanes` we have already studied the easiest case, that of two equations in $\mathbb{R}^{2}$. We have seen there that there are three possibilities. The first one is that the equations describe parallel lines. In that case, there is no point of intersection and therefore no common solution of the two equations. The solution set is therefore empty. In the second case, the lines described by the equations cross in a single point $(v_{1},v_{2})$. The solution set therefore consists of the single vector
$\mathbf{v}=\begin{bmatrix}v_{1}\\v_{2}\end{bmatrix}$. In the final case, the two equations describe the same line. The solution set of the system of equations is then the infinite set of vectors which lie on the line.

In this section, we will study solution sets of linear systems in higher dimensions. But first, let us get a clear idea of how we find and write down a solution set.

(Subsec:SolSet:WritingSolSets)=

## Writing Down Solution Sets

In {numref}`Section %s <Section:LinSystems>`, we saw how to solve a system of linear equations: we reduced the augmented matrix to echelon form and expressed the basic variables in terms of the free variables. This means that any choice of numbers for the free variables determines a solution. We can conveniently write down the set of all such solutions by using a parametrized vector. What we mean by that is best illustrated with a couple of examples.

::::{prf:example}
:label: Example:SolSet:TwoLinesinR3

Consider the following system of equations:

:::{math}
:label: Eq:SolSet:HomSys2D

\left\{\begin{array}{ccccccc}
2x_{1}&+&3x_{2}&-&x_{3}&=&0\\
x_{1}&+&x_{2}&+&x_{3}&=&0
\end{array}\right.

:::

If we apply {prf:ref}`Alg:LinSystems:ElimMethod`, we find that we can take $x_{3}$ as a free variable. So for every $t$ in $\mathbb{R}$ we can put $x_{3}=t$ and find a solution: $x_{1}=-4t$, $x_{2}=3t$, $x_{3}=t$. The solution set $\mathcal{L}_{1}$ of our linear system can therefore be written in the following way:

$$
     \mathcal{L}_{1}=\left\{\begin{bmatrix}-4t\\3t\\t\end{bmatrix}\mid t\in\mathbb{R}\right\}=
     \left\{t
\begin{bmatrix}-4\\3\\1\end{bmatrix}\mid t\in\mathbb{R}\right\}.
$$

We can see that the solution set consists of all multiples of a fixed vector $\mathbf{v}$, i.e. it is a line through the origin. This line can be seen in blue in {numref}`Figure %s <Fig:SolSet:TwoLinesinR3>`.

::::

We now look at what happens in a slightly different case where one of our constant terms is not necessarily $0$.

::::{prf:example}
:label: Example:SolSet:TwoLinesinR3b

Consider the system

:::{math}
:label: Eq:SolSet:NonHomSys2D

    \left\{      \begin{array}{ccccccc}
        2x_{1}&+&3x_{2}&-&x_{3}&=&a\\
        x_{1}&+&x_{2}&+&x_{3}&=&0
    \end{array}\right.

:::

for some $a\in\mathbb{R}$. Compared to {prf:ref}`Example:SolSet:TwoLinesinR3`, the only difference is that the right-hand side of the first equation is now $a$
instead of $0$. Applying the same algorithm as there, we find again that $x_{3}$ is free. So for every $t$ in $\mathbb{R}$ we can put $x_{3}=t$ and find a solution: $x_{1}=-4t-a$, $x_{2}=3t+a$, $x_{3}=t$. The solution set $\mathcal{L}_{2}$ can therefore be written as follows:

$$
    \mathcal{L}_{2}=\left\{\begin{bmatrix}-4t-a\\3t+a\\t\end{bmatrix}\mid t\in\mathbb{R}\right\}=
    \left\{\begin{bmatrix}
        -a\\a\\0
    \end{bmatrix}
    +t
\begin{bmatrix}-4\\3\\1\end{bmatrix}\mid t\in\mathbb{R}\right\}.
$$

We now get a line which is parallel to the one we found in {prf:ref}`Example:SolSet:TwoLinesinR3`, but which has been shifted away from the origin. In fact, any vector in this new solution set is obtained by adding the vector

$$
    \mathbf{r}_{0}=
\begin{bmatrix}
        -a\\a\\0
    \end{bmatrix}
$$

to an element of the solution set from {prf:ref}`Example:SolSet:TwoLinesinR3`. The green line in {numref}`Figure %s <Fig:SolSet:TwoLinesinR3>` corresponds to the $a=4$ case.

```{applet}
:url: solution_sets/two_lines_in_r3
:fig: Images/Fig-SolSet-TwoLinesinR3.svg
:name: Fig:SolSet:TwoLinesinR3
:class: dark-light

The solution sets for the two systems of equations from {prf:ref}`Example:SolSet:TwoLinesinR3` and {prf:ref}`Example:SolSet:TwoLinesinR3b`. In blue we see the solution set of the original system {eq}`Eq:SolSet:HomSys2D`, in green that of the system with the non-zero right hand side {eq}`Eq:SolSet:NonHomSys2D`.
```

::::

::::{prf:remark}

In general, the solution set of a linear system in $n$ variables, $k$ of which are free, can be written as

$$

    \left\{\mathbf{w}+t_{1}\mathbf{v}_{1}+\cdots+t_{k}\mathbf{v}_{k}\mid t_{1},...,t_{k} \text{ are in }\mathbb{R}\right\}
$$

for some vectors $\mathbf{v}_{1},...\mathbf{v}_{k},\mathbf{w}$ in $\mathbb{R}^{n}$. The expression $\mathbf{w}+t_{1}\mathbf{v}_{1}+\cdots+t_{k}\mathbf{v}_{k}$ is a parametrised vector with parameters $t_{1},...,t_{k}$. In {prf:ref}`Example:SolSet:TwoLinesinR3b`, we have

$$
    n=3,\quad k=1,\quad \mathbf{v}_{1}=
\begin{bmatrix}-4\\3\\1\end{bmatrix},\quad\text{and}\quad\mathbf{w}=
\begin{bmatrix}
        -a\\a\\0
    \end{bmatrix}.
$$

In {prf:ref}`Example:SolSet:TwoLinesinR3`, $n$, $k$, and $\mathbf{v}_{1}$ are the same, but $\mathbf{w}=0$.

::::

{prf:ref}`Example:SolSet:TwoLinesinR3` shows what typically happens when we consider the solutions set of two equations in $\mathbb{R}^{3}$: we get a line. Of course, this is not the only possibility. The system may be inconsistent, for example. This means that the two equations describe parallel planes. The solution set, which corresponds to the intersection of these planes, is therefore empty. The final possibility is that the second equation is a multiple of the first one. In this case, both equations describe the same plane. The solution set of the system is then that same plane, as in {prf:ref}`Ex:Solset:TwoPlanesinR3`.

::::{prf:example}
:label: Ex:Solset:TwoPlanesinR3

Consider the following linear system:

:::{math}
:label: Eq:SolSet:HomSys3D

    \left\{\begin{array}{ccccccc}
    x_{1}&+&3x_{2}&-&x_{3}&=&0\\
    2x_{1}&+&6x_{2}&-&2x_{3}&=&0
    \end{array}\right.

:::

We find two free variables and the following solution set:

$$
    \mathcal{P}_{1}=\left\{\begin{bmatrix}-3s+t\\s\\t\end{bmatrix}\mid s,t\in\mathbb{R}\right\}=
    \left\{s
\begin{bmatrix}-3\\1\\0\end{bmatrix}
    +t
\begin{bmatrix} 1\\0\\1\end{bmatrix} \mid s,t\in\mathbb{R}\right\}.
$$

What happens if we make the constant terms non-zero? Let us change the right hand side of the first equation from $0$ to $a$ and that of the second equation from $0$ to $2a$:

:::{math}

    \left\{\begin{array}{ccccccc}
    x_{1}&+&3x_{2}&-&x_{3}&=&a\\
    2x_{1}&+&6x_{2}&-&2x_{3}&=&2a
    \end{array}\right.

:::

The solution set now becomes

$$
\mathcal{P}_{2}=\left\{\begin{bmatrix}-3s+t+a\\s\\t\end{bmatrix}\mid s,t\in\mathbb{R}\right\}=\left\{
\begin{bmatrix}a\\0\\0\end{bmatrix}
+s
\begin{bmatrix}-3\\1\\0\end{bmatrix}+
t
\begin{bmatrix}1\\0\\1\end{bmatrix}\mid s,t\in\mathbb{R}\right\}.
$$

Note the similarity to {prf:ref}`Example:SolSet:TwoLinesinR3`. Making the right hand side non-zero translates the plane away from the origin by adding the vector

$$
\mathbf{r}_{0}=
\begin{bmatrix}a\\0\\0\end{bmatrix}
$$

to elements of the solution set of the linear system {eq}`Eq:SolSet:HomSys3D`. This translated plane is parallel to the original one. You can see both these planes in {numref}`Figure %s <Fig:SolSet:TwoPlanesinR3>` for the particular case $a=7$. The yellow vector there is

$$
\mathbf{v}_{1}=
\begin{bmatrix}-3\\1\\0\end{bmatrix}\quad\text{ and the orange one is}\quad
\mathbf{v}_{2}=
\begin{bmatrix}1\\0\\1\end{bmatrix}.
$$

```{applet}
:url: solution_sets/two_planes_in_r3
:fig: Images/Fig-SolSet-TwoPlanesinR3.svg
:name: Fig:SolSet:TwoPlanesinR3
:class: dark-light

The solution set for the two systems of equations from {prf:ref}`Ex:Solset:TwoPlanesinR3`.

```

Note that, if we had changed the right hand side of our first equation to $a$, $a\neq0$, and the second one to anything but $2a$, the system would have had no solutions at all. The two equations would in that case describe two parallel planes.

::::

From these examples, it seems like linear systems in which the constant terms are zero have solution sets containing the origin. Making some of the constant terms non-zero shifts the solution set away from the origin.

## Homogeneous Linear Systems

Our first aim in this section is to show that the intuition from {numref}`Subsec:SolSet:WritingSolSets` holds in general. We first introduce some terminology to avoid the long and clumsy phrase **linear system with all constant terms equal to $0$**.

::::{prf:definition}

We will call a linear system **homogeneous** if all constant terms are $0$. If

$$
\left\{\begin{array}{ccccccc}
a_{11}x_{1}&+&\cdots &+&a_{1n}x_{n}&=&b_{1}\\
a_{21}x_{1}&+&\cdots &+&a_{2n}x_{n}&=&b_{2}\\
&&&\vdots&&&\\
a_{m1}x_{1}&+&\cdots &+&a_{mn}x_{n}&=&b_{m}
\end{array}\right.
$$

is a system of equations, then the **associated homogeneous system** is given by

$$
\left\{\begin{array}{ccccccc}
a_{11}x_{1}&+&\cdots &+&a_{1n}x_{n}&=&0\\
a_{21}x_{1}&+&\cdots &+&a_{2n}x_{n}&=&0\\
&&&\vdots&&&\\
a_{m1}x_{1}&+&\cdots &+&a_{mn}x_{n}&=&0
\end{array}\right.
$$

::::

{prf:ref}`Prop:SolSet:SolplusHom` shows that the solution set of a non-homogeneous linear system can be obtained by adding the solutions of the associated homogeneous system to one particular solution of the original system. Which particular solution you take does not matter. Compare this to what we found in Section {numref}`Subsec:SolSet:WritingSolSets`, in particular to {numref}`Figures %s <Fig:SolSet:TwoLinesinR3>` and {numref}`Figure %s <Fig:SolSet:TwoPlanesinR3>`.

::::{prf:proposition}
:label: Prop:SolSet:SolplusHom

Suppose $(c_{1},...,c_{n})$ is a solution of a linear system. Then $(c_{1}',...,c_{n}')$ is also a solution of the linear system if and only if there exists a solution of the associated homogeneous system $(d_{1},...,d_{n})$ such that $c'_{i}=c_{i}+d_{i}$ for all $i$.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:SolSet:SolplusHom`
:class: tudproof

Consider the linear system

$$
\left\{\begin{array}{ccccccc}
a_{11}x_{1}&+&\cdots &+&a_{1n}x_{n}&=&b_{1}\\
a_{21}x_{1}&+&\cdots &+&a_{2n}x_{n}&=&b_{2}\\
&&&\vdots&&&\\
a_{m1}x_{1}&+&\cdots &+&a_{mn}x_{n}&=&b_{m}
\end{array}\right.
$$

Suppose first that $(c_{1},...,c_{n})$ and $(c_{1}',...,c_{n}')$ are solutions and put $d_{i}=c_{i}'-c_{i}$. Then

$$
\left\{\begin{array}{ccccccccccccccc}
a_{11}d_{1}&+&\cdots &+&a_{1n}d_{n}&=&a_{11}c_{1}-a_{11}c'_{1}&+&\cdots &+&a_{1n}c_{n}-a_{1n}c'_{n}&=&b_{1}-b_{1}&=&0\\
a_{21}d_{1}&+&\cdots &+&a_{2n}d_{n}&=&a_{21}c_{1}-a_{21}c'_{1}&+&\cdots &+&a_{2n}c_{n}-a_{2n}c'_{n}&=&b_{1}-b_{1}&=&0\\
&&&&&&&\vdots&&&&&&&\\
a_{m1}d_{1}&+&\cdots &+&a_{mn}d_{n}&=&a_{m1}c_{1}-a_{m1}c'_{1}&+&\cdots &+&a_{mn}c_{n}-a_{mn}c'_{n}&=&b_{1}-b_{1}&=&0
\end{array}\right.
$$

so $(d_{1},...,d_{n})$ is a solution of the associated homogeneous system such that $c_{i}'=c_{i}+d_{i}$ for all $i$.

Assume on the other hand that $(c_{1},...,c_{n})$ is a solution of the system and that $(d_{1},...,d_{n})$ is a solution of the associated homogeneous system such that $c'_{i}=c_{i}+d_{i}$. Then

$$
\left\{\begin{array}{ccccccccccccc}
a_{11}c'_{1}&+&\cdots &+&a_{1n}c'_{n}&=&a_{11}(c_{1}+d_{1})&+&\cdots &+&a_{1n}(c_{n}+d_{n})&=&b_{1}+0\\
a_{21}c'_{1}&+&\cdots &+&a_{2n}c'_{n}&=&a_{21}(c_{1}+d_{1})&+&\cdots &+&a_{2n}(c_{n}+d_{n})&=&b_{2}+0\\
&&&&&&\vdots&&&&&&\\
a_{m1}c'_{1}&+&\cdots &+&a_{mn}c'_{n}&=&a_{m1}(c_{1}+d_{1})&+&\cdots &+&a_{mn}(c_{n}+d_{n})&=&b_{m}+0\\
\end{array}\right.
$$

so $(c_{1}',...,c_{n}')$ is indeed a solution of the original system.

::::

In view of {prf:ref}`Prop:SolSet:SolplusHom`, it seems that a further study of solution sets of homogeneous systems could be very helpful. After all, the solution set to a general system is just a translation of the solution set of the associated homogeneous system. And homogeneous systems are easier!

::::{prf:proposition}
:label: Prop:SolSet:SolSetisVecSpa

Let $V$ be the solution set to a homogeneous linear system. The following statements hold:

<ol type="i">
<li id="Item:SolSet:ZeroinSolSet">

$\vect{0}$ is in $V$;

</li>
<li id="Item:SolSet:LinCombinSolSet">

Suppose $c_{1}$ and $c_{2}$ are arbitrary scalars. If $\vect{v}_{1}$ and $\vect{v}_{2}$ are in $V$, then so is $c_{1}\vect{v}_{1}+c_{2}\vect{v}_{2}$.

</li>
</ol>

%i. $\vect{0}$ is in $V$;\label{Item:SolSet:ZeroinSolSet}
%ii. Suppose $c_{1}$ and $c_{2}$ are arbitrary scalars. If $\vect{v}_{1}$ and $\vect{v}_{2}$ are in $V$, then so is $c_{1}\vect{v}_{1}+c_{2}\vect{v}_{2}$.\label{Item:SolSet:LinCombinSolSet}

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:SolSet:SolSetisVecSpa`
:class: tudproof

This is a left as an exercise.

::::

::::{prf:remark}
:label: Rem:SolSet:SolSetisClosed

Note that the converse of {prf:ref}`Prop:SolSet:SolSetisVecSpa` is also true: if [i.](#Item:SolSet:ZeroinSolSet) and [ii.](#Item:SolSet:LinCombinSolSet) hold for the solution set of some linear system, then the system is homogeneous. (In fact, just [i.](#Item:SolSet:ZeroinSolSet) suffices.) This, too, is left as an exercise.

The following consequences of {prf:ref}`Prop:SolSet:SolSetisVecSpa` will often be useful:

<ol>
<li>

By putting $c_{2}=0$ in statement [ii.](#Item:SolSet:LinCombinSolSet), we find that any multiple of a vector in the solution set is again in the solution set;

</li>
<li>

By putting $c_{1}=1=c_{2}$, we find that any sum of two solutions is again a solution.

</li>
</ol>

You should keep in mind, however, that this **only** holds for solutions of **homogeneous** systems!

::::

::::{prf:example} Application

Remember from {prf:ref}`App:Vectors:ChemReac` that adding carbon ($\ce{C}$) to sodium sulfate ($\ce{Na2SO4}$) gives sodium sulfide ($\ce{NaS}$) and carbon dioxide ($\ce{CO2}$). How much carbon do we need to add to a quantity of sodium sulfide in order to turn it all into sodium sulfate?

As we have seen in that application, we can interpret the different molecules as vectors in the following way:

$$
\ce{Na2SO4}:
\begin{bmatrix}
    2\\1\\4\\0
\end{bmatrix} \quad \ce{C}:
\begin{bmatrix}
    0\\0\\0\\1
\end{bmatrix} \quad \ce{Na2S}:
\begin{bmatrix}
    2\\1\\0\\0
\end{bmatrix} \quad \ce{CO2}:
\begin{bmatrix}
0\\0\\2\\1
\end{bmatrix}.
$$

Let $x_{1},x_{2},x_{3}$ and $x_{4}$ denote the quantities of $\ce{Na2SO4}$, $\ce{C}$, $\ce{Na2S}$, and $\ce{CO2}$, respectively. In order to turn all the $\ce{Na2SO4}$ into $\ce{Na2S}$, we must have

$$
    x_{1}
\begin{bmatrix}
2\\1\\4\\0
\end{bmatrix}+
x_{2}
\begin{bmatrix}
0\\0\\0\\1
\end{bmatrix}=
x_{3}
\begin{bmatrix}
2\\1\\0\\0
\end{bmatrix}+
x_{4}
\begin{bmatrix}
0\\0\\2\\1
\end{bmatrix}.
$$

If we subtract the right hand side, we can rewrite this as the homogeneous system

$$
\left\{\begin{array}{ccccccccc}
2x_{1}&+&0x_{2}&-&2x_{3}&-&0x_{4}&=&0\\
1x_{1}&+&0x_{2}&-&1x_{3}&-&0x_{4}&=&0\\
4x_{1}&+&0x_{2}&-&0x_{3}&-&2x_{4}&=&0\\
0x_{1}&+&1x_{2}&-&0x_{3}&-&1x_{4}&=&0
\end{array}\right..
$$

This system can be solved as follows, using the row reduction algorithm of {numref}`Section %s <Section:LinSystems>`:

$$
\left[\begin{array}{rrrr|r}2&0&-2&0&0\\1&0&-1&0&0\\4&0&0&-2&0\\0&1&0&-1&0\\\end{array}\right]\begin{array}{l}
[R_1] \\
{[R_2-\frac{1}{2}R_1]} \\
{[R_3-2R_1]} \\
{[R_4]}
\end{array} \sim
\left[\begin{array}{rrrr|r}2&0&-2&0&0\\0&0&0&0&0\\0&0&4&-2&0\\0&1&0&-1&0\\\end{array}\right]\begin{array}{l}
[R_1] \\
{[R_2\leftrightarrow R_4]} \\
{[R_3]} \\
{[R_4\leftrightarrow R_2]}
\end{array} \sim
\left[\begin{array}{rrrr|r}2&0&-2&0&0\\0&1&0&-1&0\\0&0&4&-2&0\\0&0&0&0&0\\\end{array}\right]
$$

Now we can conclude that the solution set looks as follows:

$$
    \left\{\begin{bmatrix}
        \frac{1}{2}t\\t\\\frac{1}{2}t\\t
    \end{bmatrix}\mid t\in \mathbb{R}\right\},\quad\text{which is the same as}\quad
    \left\{\begin{bmatrix}
        t\\2t\\t\\2t
    \end{bmatrix}\mid t\in \mathbb{R}\right\}.
$$

Hence, in order to turn one molecule of sodium sulfate into sodium sulfide, we must add two molecules of carbon. As a by-product, this will give two molecules of carbon dioxide. Compare this result to {prf:ref}`App:Vectors:ChemReac`, where we indeed found the reaction to be balanced when two molecules of carbon were added to one molecule of sodium sulfate.

::::

%\todo[inline]{Suggested exercises: prove Proposition \ref{Prop:SolSet:SolSetisVecSpa} and Remark\ref{Rem:SolSet:SolSetisClosed} [it]; write solutions in parametrised vector form [it, end of section 2]; solve non-homogeneous systems by using a particular solution and the solution of the associated homogeneous system [es].}

## Grasple Exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/03d9c585-c51a-41e0-b3ac-33ad9f42cb55?id=83384
:label: grasple_exercise_2_3_1
:dropdown:
:description: Solution set of a system of 2 equations in 3 unknowns.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1e3c93cb-4fa7-4bf5-b46f-0c631e074d7e?id=83594
:label: grasple_exercise_2_3_2
:dropdown:
:description: Solution set of a system of 3 equations in 2 unknowns.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/44dcb893-3beb-46a2-bddd-75f830cba5de?id=83499
:label: grasple_exercise_2_3_3
:dropdown:
:description: Solution set of a system of 2 equations in 2 unknowns.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ce8a45dc-f26f-45ca-a754-35512f882411?id=80874
:label: grasple_exercise_2_3_4
:dropdown:
:description: Solution set of a system of 3 equations in 4 unknowns.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/633cfb15-272d-40c0-adc6-36f091446d7d?id=83279
:label: grasple_exercise_2_3_5
:dropdown:
:description: Solution set of a system of 2 equations in 4 unknowns.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/611e08ab-df69-4a14-96d3-b6a9bbda316b?id=83238
:label: grasple_exercise_2_3_6
:dropdown:
:description: Solution set of a system of 3 equations in 3 unknowns.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9536051d-baba-4b22-94ed-94190e9e6b47?id=83246
:label: grasple_exercise_2_3_7
:dropdown:
:description: Solution set of a system of 3 equations in 5 unknowns.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/196ac202-23e4-4c94-842b-e50410fedea0?id=83505
:label: grasple_exercise_2_3_8
:dropdown:
:description: Solution set of a system of 2 equations in 4 unknowns.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6cbb0bd4-863c-4705-908b-bb01602abf05?id=87438
:label: grasple_exercise_2_3_9
:dropdown:
:description: Different parametrised vector solutions.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/021bb82e-7af3-4c84-86b8-0dcd22bf555b?id=84556
:label: grasple_exercise_2_3_10
:dropdown:
:description: Combining solutions of a linear system (1).

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5d723e95-a4e5-4594-970e-6332e4953e73?id=84559
:label: grasple_exercise_2_3_11
:dropdown:
:description: Combining solutions of a linear system (2).

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/297528c4-7ea0-426b-aaa0-85dbcbfa97af?id=83227
:label: grasple_exercise_2_3_12
:dropdown:
:description: Combining solutions of a linear system (3).

::::
