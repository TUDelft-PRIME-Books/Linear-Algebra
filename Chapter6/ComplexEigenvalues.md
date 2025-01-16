(Section:ComplexEV)=

# Complex Eigenvalues (and Eigenvectors)

In the previous sections we hinted at the possibility to allow eigenvalues to be complex numbers. For an $n\times n$ matrix $A$ the eigenvalues are the zeros of the characteristic polynomial $p_A(\lambda)$ of $A$. Even if the matrix is real, these zeros may be complex. We start with an example to explore this until now unknown territory.

::::{prf:example}
:label: Ex:ComplexEV:FirstExample

Consider the matrix $A = \left[\begin{array}{cc} 1 & -2 \\ 1 & 3  \end{array}\right]$.

We first compute the characteristic polynomial

$$
p_A(\lambda) = \left|\begin{array}{cc} 1-\lambda & -2 \\ 1 & 3-\lambda  \end{array}\right|= (1-\lambda)(3-\lambda) +2 = \lambda^2 - 4\lambda +5.
$$

Completing the square we see that

$$
p_A(\lambda) = 0 \,\, \iff \,\, \lambda^2 - 4\lambda +5 = (\lambda -2)^2 + 1 = 0
\,\, \iff \,\,  \lambda = 2 \pm i.
$$

So the eigenvalues are complex numbers. Can we still find eigenvectors? We sure can, but they will not be real vectors. To find an eigenvector for $\lambda_1 = 2+i$, as before we have

$$
A\vect{v} = \lambda_1\vect{v}    \quad\iff\quad  (A -  \lambda_1I)\vect{v} = \vect{0}.
$$

So we have to solve a homogeneous system of linear equations, where now the coefficient matrix contains complex numbers. This slightly complicates the computation, but for this $2 \times 2$ matrix things don't get too bad.

$$
\left[\begin{array}{cc|c} 1 - (2+i) & -2& 0 \\ 1 & 3- (2+i) & 0 \end{array}\right]
=
\left[\begin{array}{cc|c} -1 - i & -2& 0 \\ 1 & 1-i & 0 \end{array}\right]
\sim
\left[\begin{array}{cc|c} 0 & \class{blue}0 & 0 \\ 1 & 1-i & 0 \end{array}\right]
,
$$

where the row operation we invoke is: add the second row $(1+i)$ times to the first row.
The blue \class{blue}{0} is the result of the evaluation of

$$
-2 + (1+i)(1-i).
$$

We can read off a solution (i.e., complex eigenvector): &nbsp; 
$\vect{v} = \left[\begin{array}{c}  -1+i \\1 \end{array}\right]$.

To check that we have indeed an eigenvector is also slightly more involved than in the real case.

$$
\left[\begin{array}{cc} 1 & -2 \\ 1 & 3  \end{array}\right]
\left[\begin{array}{c}  -1+i \\1 \end{array}\right]
= \left[\begin{array}{c}  -1+i-2 \\-1+i +3 \end{array}\right]
= \left[\begin{array}{c}  -3+i \\ 2+i \end{array}\right]
$$

and that agrees with

$$
(2+i)\left[\begin{array}{c}  -1+i \\1 \end{array}\right]
 = \left[\begin{array}{c}  -3+i \\2+i \end{array}\right].
$$

Alternatively, to simplify the augmented matrix

$$
\left[\begin{array}{cc|c} -1 - i & -2& 0 \\ 1 & 1-i & 0 \end{array}\right]
,
$$

we could have used the entry $-2$ in the first row of the augmented matrix to create a zero in the second row. More specifically, if we add the first row $\dfrac{1-i}{2}$ times to the second row, we get

$$
\left[\begin{array}{cc|c} -1 - i & -2& 0 \\ 1 & 1-i & 0 \end{array}\right]
\sim
\left[\begin{array}{cc|c} -1-i & -2& 0 \\ 0 & 0 & 0 \end{array}\right]
 \sim
\left[\begin{array}{cc|c} 1+i & 2& 0 \\ 0 & 0 & 0 \end{array}\right]
.
$$

Then the vector $\vect{u} = \left[\begin{array}{c} -2 \\ 1+i \end{array}\right] $ is a natural candidate for
an eigenvector.

At first sight it seems that we have found two linearly independent eigenvectors for the eigenvalue $\lambda_1 = 2+i$.
However, closer inspection shows that

$$
\vect{u} = \left[\begin{array}{c} -2 \\ 1+i  \end{array}\right]
=  (1+i)  \left[\begin{array}{c}  -1+i \\1 \end{array}\right]
 = (1+i)\vect{v},
$$

so the two vectors are *complex* multiples of each other, and hence are not linearly independent.

For the other eigenvalue we can proceed in the same manner and find (for instance) the eigenvector
&nbsp; $\vect{v}_2 =\left[\begin{array}{c} -2 \\ 1-i \end{array}\right] $.

:::::

Note that the two eigenvalues are each others complex conjugate, and that the same holds for the corresponding eigenvectors,
that is, if we define the complex conjugate of a vector component wise.

## Vectors and matrices with complex entries

We need a few definitions to settle matters a bit more formally. In the remainder of this section matrices (so in particular vectors) are allowed to have complex numbers as entries. If the entries are supposed to be real numbers we explicitly state this by speaking of a real matrix (or a real vector).

::::::{prf:definition}
:label: Dfn:ComplexEV:Conjugate

The **complex conjugate** $\overline{A}$ of a matrix $A$ is defined component wise:

if $\quad A = \left[\begin{array}{ccc} a_{11} & \ldots & a_{1n} \\ \vdots & &\vdots \\ a_{m1} & \ldots & a_{mn}  \end{array}\right] \quad$
then
$\quad\overline{A} = \left[\begin{array}{ccc} \overline{a_{11}} & \ldots & \overline{a_{1n}} \\ \vdots & &\vdots \\ \overline{a_{m1}} & \ldots & \overline{a_{mn}} \end{array}\right] $.

::::::

::::::{prf:proposition}
:label: Prop:ComplexEV:PropConjugate

<ol type = "i">
<li>

If $A$ and $B$ are two $m\times n$ matrices, then $\overline{A+B} = \overline{A}+\overline{B}$.

</li>
<li>

If $A$ and $C$ are two matrices for which the product $AC$ exists,
<BR>
then $\overline{AC} = \overline{A}$ $\overline{C}$.

</li>
</ol>

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:ComplexEV:PropConjugate`
:class: tudproof

The statements follow immediately from the definitions of the sum and product of two matrices, and of the corresponding rules of complex arithmetic that say

$$
\overline{z+w} = \overline{z} + \overline{w} \quad\text{and} \quad
\overline{z\cdot w} = \overline{z}\cdot\overline{w},  \quad \text{for all }  z,w \in \C.
$$

::::::

With this we can put the outcomes in {prf:ref}`Ex:ComplexEV:FirstExample` in a broader perspective.

::::::{prf:proposition}
:label: Prop:ComplexEV:Conjugation

Suppose $A$ is a _real_ matrix, and $\lambda = \alpha + \beta i$, with $\beta \neq 0$, is an eigenvalue of $A$.
Then the following properties hold:

<ol type = "i">
<li>

$\overline{\lambda} = \alpha - \beta i$ is an eigenvalue too.

</li>
<li>

If $\vect{v} = \vect{u}+i\vect{w}$, where $\vect{u}$ and $\vect{w}$ are real vectors, is an eigenvector
for $\lambda$, then
$\overline{\vect{v}} = \vect{u}-i\vect{w}$ is an eigenvector for $\overline{\lambda}$.

</li>
</ol>

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:ComplexEV:Conjugation`
:class: tudproof

Suppose $A(\vect{u}+i\vect{w}) = (\alpha + \beta i)(\vect{u}+i\vect{w})$.

Complex conjugation yields that

$$
\overline{A(\vect{u}+i\vect{w})} = \overline{A}\,\overline{(\vect{u}+i\vect{w})} =
A(\vect{u}-i\vect{w}),
$$

since $A$ is a real matrix, and $\vect{u}$ and $\vect{v}$ are supposed to be real.
At the same time

$$
\overline{A(\vect{u}+i\vect{w})} =
\overline{(\alpha + \beta i)(\vect{u}+i\vect{w})} = (\alpha - \beta i)(\vect{u}-i\vect{w}).
$$

Equating the last expressions of both derivations yields the desired result.

$$
A(\vect{u}-i\vect{w}) = (\alpha - \beta i)(\vect{u}-i\vect{w}).
$$

This states exactly that $A$ has the eigenvalue $\overline{\lambda} = \alpha - \beta i$ with the corresponding eigenvector $\vect{u}-i\vect{w}$.

::::::

Things look especially simple in the next example.

::::::{prf:example}
:label: Ex:ComplexEV:abba

Let $A$ be the matrix $A=  \left[\begin{array}{cc} a & -b \\ b & a \end{array}\right]$, with $b \neq 0$.

The characteristic polynomial of $A$ is then given by $p_A(\lambda) = (a-\lambda)^2 + b^2$.

So $A$ has the complex eigenvalues

$$
\lambda_{1,2} = a \pm bi.
$$

From row reduction of the augmented matrix

\begin{eqnarray*}
[A - (a+bi)I | \vect{0}] &=&
\left[\begin{array}{cc|c} a-(a+bi) & -b &0\\ b & a-(a+bi)&0 \end{array}\right]\\
&=&
\left[\begin{array}{cc|c} -bi & -b&0 \\ b & -bi&0 \end{array}\right] \\
&\sim&
\left[\begin{array}{cc|c} bi & b &0\\ 0 & 0&0 \end{array}\right],
\end{eqnarray*}

we see that $\vect{v} = \left[\begin{array}{c} 1 \\ -i \end{array}\right]$
is an eigenvector for $\lambda_1 = a+bi$. By taking conjugates
(according to {prf:ref}`Prop:ComplexEV:Conjugation`) we can conclude that
$\vect{w} = \left[\begin{array}{c} 1 \\ i \end{array}\right]$,
i.e. the conjugate of $\vect{v}$, will be an eigenvector for $\lambda_2= a-bi$.

::::::

There is a nice geometric interpretation for matrices of the form $\left[\begin{array}{cc} a & -b \\ b & a \end{array}\right]$.

Or rather, for the corresponding linear transformation.

::::::{prf:proposition}
:label: Prop:ComplexEV:Rotation

The linear transformation $T:\R^2\to\R^2$ given by

$$
T(\vect{x}) = \left[\begin{array}{cc} a & -b \\ b & a \end{array}\right]
\vect{x}, \quad  a,b \in \R, \quad b \neq 0,
$$

can be described as a rotation followed by a "scaling".

In fact, it holds that

$A = \left[\begin{array}{cc} a & -b \\ b & a \end{array}\right] = r  \left[\begin{array}{cc} \cos({\varphi}) & -\sin({\varphi}) \\ \sin({\varphi}) & \cos({\varphi}) \end{array}\right]
$, for some $r > 0$ and angle $\varphi$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:ComplexEV:Rotation`
:class: tudproof

Both columns of $A$ have length $r = \sqrt{a^2 + (\pm b)^2} = \sqrt{a^2 + b^2}$.

If we take out this factor, we get

$$
\left[\begin{array}{cc} a & -b \\ b & a \end{array}\right]
 =
r \left[\begin{array}{cc} a/r & -b/r \\
b/r & a/r \end{array}\right]
.
$$

The first column $\left[\begin{array}{c} a/r  \\     b/r \end{array}\right]$
has length one, so it lies on the unit circle, and hence must be of the form

$$
\left[\begin{array}{c} a/r  \\     b/r \end{array}\right]
 = \left[\begin{array}{c} \cos(\varphi)  \\    \sin(\varphi) \end{array}\right]
, \quad \text{for some angle  }  \varphi,
$$

and this makes that

$$
\left[\begin{array}{cc} a & -b \\ b & a \end{array}\right]
 =
r \left[\begin{array}{cc} a/r & -b/r \\
b/r & a/r \end{array}\right]
 = r \left[\begin{array}{cc} \cos(\varphi)  & - \sin(\varphi)\\
\sin(\varphi) & \cos(\varphi) \end{array}\right]
.
$$

So the 'action' of the matrix $A = \left[\begin{array}{cc} a & -b \\ b & a \end{array}\right]$
on a vector $\vect{x}$ is a (counterclockwise) rotation over the angle $\varphi$ followed by
a scaling (stretching/dilatation) with a factor $r$.

::::::

The scaling factor $r$ and the angle $\varphi$ are exactly the polar coordinates of the eigenvalue $\lambda = a + bi$.
That is,

$$
a + bi = r(a/r + b/r i) = r (\cos(\varphi) + i \sin(\varphi)),
$$

where

$$
  r = |\lambda|, \quad \varphi = \text{arg}\,\lambda.
$$

{prf:ref}`Prop:ComplexEV:Rotation` can be generalized as follows. If a real $n \times n$ matrix $A$ has a non-real eigenvalue, there is always a rotation 'hidden' in the transformation $T: \vect{x} \mapsto A\vect{x}$.

::::::{prf:proposition}
:label: Prop:ComplexEV:Invariant
Suppose the real $n \times n$ matrix $A$ has a complex eigenvalue $\lambda = \alpha - \beta i$, with $\beta \neq 0$. Then there exist two linearly independent _real_ vectors $\vect{u}$ and $\vect{w}$ for which

$$
\begin{cases}
A\vect{u} = \alpha\vect{u} + \beta\vect{w} \\
A\vect{w} = -\beta\vect{u} + \alpha\vect{w}.
\end{cases}
$$

That means that the two-dimensional subspace $S = \Span{\vect{u},\vect{w}}$ is invariant under the linear transformation $T$ that has $A$ as a standard matrix.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:ComplexEV:Invariant`
:class: tudproof

Let $\vect{v}$ be an eigenvector for $\lambda=\alpha - \beta i$.
So, $\vect{v} = \vect{u}+i\vect{w}$, for real vectors $\vect{u}$ and $\vect{w}$.
Note that $\vect{v}$ cannot be a real vector.

$\vect{u}$ and $\vect{w}$ must be linearly independent, because if $\vect{w}= \vect{0}$, then $\vect{v}$ would be a real eigenvector, and if $\vect{u}= k\vect{w}$ for some $k$ in $\R$, then $\vect{v} = (k+i)\vect{w}$, and then
$\vect{w}$ would be a real eigenvector for the complex eigenvalue $\lambda$ of the real matrix $A$. And that is unheard of.

So we conclude that $\vect{u}$ and $\vect{w}$ must be linearly independent.

We now have

$$
A(\vect{u}+i\vect{w}) = (\alpha - \beta i)(\vect{u}+i\vect{w}) =
\alpha\vect{u}+\beta \vect{w} -i\beta\vect{u} + i\alpha\vect{w}.
$$

Comparing real and imaginary parts we conclude that indeed

:::{math}
:label: Eq:ComplexEV:Eq1

\begin{cases}
A\vect{u} = \alpha\vect{u} + \beta\vect{w} \\
A\vect{w} = -\beta\vect{u} + \alpha\vect{w}.
\end{cases}

:::

::::::

If we apply the above to the case $n = 2$, we can rewrite Equation {eq}`Eq:ComplexEV:Eq1`
as

$$
A [\,\vect{u}\,\, \vect{w}\,] = [\,\vect{u}\,\, \vect{w}\,] \left[\begin{array}{cc} \alpha & -\beta \\ \beta & \alpha \end{array}\right].
$$

So if we define $P$ to be the matrix $[\,\vect{u}\,\, \vect{w}\,]$ then we have $AP = PC$, where

$$
  C =  \left[\begin{array}{cc} \alpha & -\beta \\ \beta & \alpha \end{array}\right].
$$

This more or less settles the following proposition.

::::::{prf:proposition}
:label: Prop:ComplexEV:HiddenRotation

Suppose $A$ is a $2 \times 2$ matrix with eigenvalues $\alpha \pm \beta i$, with $\beta \neq 0$. <BR>
Then $A$ can be written as

$$
A = PCP^{-1} = P\left[\begin{array}{cc} \alpha & -\beta \\ \beta & \alpha \end{array}\right]
P^{-1}
$$

for some invertible matrix $P$.

{prf:ref}`Prop:ComplexEV:Rotation` states that $C$ can be written as

$$
C = r\left[\begin{array}{cc} \cos(\varphi) & -\sin(\varphi) \\ \sin(\varphi) & \cos(\varphi) \end{array}\right]
.
$$

We can formulate this as there being a **hidden rotation** in $A$.

::::::

To be specific,

$$
P =   [ \,\vect{u}\,\, \vect{w}\, ] =\left[\begin{array}{cc}u_1 & w_1 \\ u_2&w_2 \end{array}\right],
$$

where $\vect{u} + i \vect{w}$ is an eigenvector for $\lambda = \alpha - \beta i$.
<BR>
Let us illustrate matters with the following example.

::::::{prf:example}

The matrix $A = \left[\begin{array}{cc} 1 & -2 \\ 1 & 3  \end{array}\right]$
of {prf:ref}`Ex:ComplexEV:FirstExample`
has the eigenvalues $\lambda_{1,2} = \alpha \pm \beta i = 2 \pm i$.
An eigenvector for $2-i$ is given by

$$
\vect{v} =  \left[\begin{array}{c} -2 \\ 1-i  \end{array}\right]
 = \left[\begin{array}{c} -2 \\ 1 \end{array}\right]
 + i\left[\begin{array}{c} 0 \\ -1  \end{array}\right].
$$

Let us establish the identity

$$
P^{-1}AP = \left[\begin{array}{cc} \alpha & -\beta \\ \beta & \alpha \end{array}\right] = \left[\begin{array}{cc} 2 & -1 \\ 1 & 2 \end{array}\right].
$$

According to {prf:ref}`Prop:ComplexEV:HiddenRotation` we can take

$$
P = \left[\begin{array}{cc} -2 & 0 \\ 1 & -1 \end{array}\right],
$$

with

$$
P^{-1} = \dfrac12\left[\begin{array}{cc} -1 & 0 \\ -1 & -2 \end{array}\right].
$$

We then get

$$
\begin{array}{rcl}
P^{-1}AP &=& \dfrac12\left[\begin{array}{cc} -1 & 0 \\ -1 & -2 \end{array}\right]
\left[\begin{array}{cc} 1 & -2 \\ 1 & 3  \end{array}\right]
\left[\begin{array}{cc} -2 & 0 \\ 1 & -1 \end{array}\right] \\
&=& \dfrac12\left[\begin{array}{cc}  -1 & 2 \\ -3 & -4 \end{array}\right]
\left[\begin{array}{cc} -2 & 0 \\ 1 & -1 \end{array}\right] \\
&=& \dfrac12 \left[\begin{array}{cc} 4 & -2 \\ 2 & 4 \end{array}\right]
 =
\left[\begin{array}{cc} 2 & -1 \\ 1 & 2 \end{array}\right]
 =
\left[\begin{array}{cc} \alpha & -\beta \\ \beta & \alpha \end{array}\right]
.
\end{array}
$$

::::::

We conclude this section by reconsidering diagonalizability of real matrices if we allow complex eigenvalues.

## Complex diagonalizability

Let us first generalize the definition:

::::::{prf:definition}
:label: Dfn:Eigenvalues:ComplexDiagonalizability

A matrix is $A$ is called **complex diagonalizable** if it can be written in the form

$$
A = PDP^{-1}.
$$

where $D$ is a diagonal matrix, and $P$ and $D$ may contain complex entries.
We then say that $PDP^{-1}$ is a **diagonalization** of $A$.

::::::



Just like in the real case diagonalizability has all to do with the existence of enough (possibly complex) eigenvectors. The derivation is the same as in {numref}`Section %s <Sec:Diagonalize>`, we only repeat the conclusion.

::::::{prf:proposition}

An $n\times n$ matrix is (complex) diagonalizable if and only if there exists a basis of eigenvectors for $\mathbb{C}^n$.

In that case, if $\vect{v}_1, \ldots, \vect{v}_n$ are $n$ linearly independent eigenvectors for the eigenvalues $\lambda_1, \ldots, \lambda_n$,
then

$$
A = PDP^{-1} \quad \text{for} \quad  D = \left[\begin{array}{cccc} \lambda_1 & 0 & \ldots & 0 \\
0 & \lambda_2 & \ldots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \ldots & \lambda_n\end{array}\right],
 \quad
P = [  \,\vect{v}_1\,\,  \vect{v}_2 \,  \ldots \,  \vect{v}_n\,].
$$

::::::

::::::{prf:example}
:label: Ex:ComplexEV:FirstExampleCtd

The matrix $A = \left[\begin{array}{cc} 1 & -2 \\ 1 & 3  \end{array}\right]$
of {prf:ref}`Ex:ComplexEV:FirstExample` has the eigenvalues $\lambda_1 = 2 + i$,
$\lambda_2 = 2 - i$,  with corresponding eigenvectors $\vect{v}_1 = \left[\begin{array}{c}  -1+i \\1 \end{array}\right]$,
$\vect{v}_2 = \left[\begin{array}{c}  -1-i \\1 \end{array}\right]$.

It follows that

$$
\left[\begin{array}{cc} 1 & -2 \\ 1 & 3  \end{array}\right]
 =  \left[\begin{array}{cc}  -1+i & -1-i \\1 &1  \end{array}\right]
{\left[\begin{array}{cc}  2+i & 0 \\0 &2-i  \end{array}\right]
\left[\begin{array}{cc}  -1+i & -1-i \\1 &1  \end{array}\right]
}^{-1}.
$$

Which you are challenged to check by a careful calculation.

::::::

::::::{prf:remark}
:label:  Rem:Diagonalizable:RealVersusComplexDiagonalizable

<ul>
<li>

When the context requires it, we will specify whether we mean **real diagonalizable** or **complex diagonalizable**.

</li>
<li>

Since the real numbers are contained in the complex numbers, a matrix that is real diagonalizable is automatically complex diagonalizable.

</li>
<li>

The definition also makes sense for matrices with complex numbers as entries. However, we will not pursue that track.

</li>
</ul>

::::::


For a matrix to be real diagonalizable {prf:ref}`Thm:Diagonalizable:ThirdCharacterization` states that two conditions must be satisfied. One is that the characteristic polynomial of $A$ must have $n$ real roots, counting multiplicities. The second is that for each eigenvalue the geometric multiplicity must be equal to the algebraic multiplicity.
The Fundamental Theorem of Algebra guarantees that each polynomial of degree $n$ has $n$ roots. So if we allow complex eigenvalues, the first condition is automatically satisfied. We thus find the following criterion for complex diagonalizability of a (possibly complex) matrix $A$.

::::::{prf:proposition}
:label: Prop:ComplexEV:ComplexDiagonalizable

A matrix $A$ is complex diagonalizable if and only if for each eigenvalue the geometric multiplicity is equal to the algebraic multiplicity.

::::::



## Grasple Exercises 

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bf1aef1c-7948-4b32-951e-d79940282bfb?id=91545
:label: grasple_exercise_6_4_1
:dropdown:
:description:   Given a complex eigenvector of  a $2\times 2$ matrix, find the corresponding eigenvalue.  

::::::


::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4e7c813d-ce37-42a2-be36-9dffb42d5f0b?id=91546
:label: grasple_exercise_6_4_2
:dropdown:
:description: Given a complex eigenvector of  a $2\times 2$ matrix, find the corresponding eigenvalue.  

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/66dcb059-1c37-477c-9f23-8bd1bb26fb44?id=92368
:label: grasple_exercise_6_4_3
:dropdown:
:description:   To find the (complex) eigenvalues of a $2 \times 2$ matrix $A$.

::::::


::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/507921c2-d568-44d9-a254-536440ca613e?id=91553
:label: grasple_exercise_6_4_4
:dropdown:
:description:   To find the (complex) eigenvalues of a $2 \times 2$ matrix $A$.

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/593e9ddd-a7b8-4617-958e-95f328e28e80?id=91547
:label: grasple_exercise_6_4_5
:dropdown:
:description:   To find the (complex) eigenvalues and bases of their eigenspaces of a $2 \times 2$ matrix  $A$.

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f60a57c2-b0b3-45de-b18c-e0da1bbef601?id=91555
:label: grasple_exercise_6_4_6
:dropdown:
:description:  Given a complex  eigenvector of a real 2x2 matrix, point out other eigenvectors.
::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/440c03f9-9a5a-40a6-aa1a-77660a588b20?id=91556
:label: grasple_exercise_6_4_7
:dropdown:
:description: To find an invertible matrix $P$ and a scaling-rotation matrix $C$ for which $A = PCP^{-1}$.
   

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f3a6972e-f17b-4984-b0ee-38012ec542b3?id=91563
:label: grasple_exercise_6_4_8
:dropdown:
:description:  To find the complex eigenvalues of a $2 \times 2$ matrix (of a special form). 

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/79c7c433-fbcc-41b8-85d2-b1938a26d40e?id=91566
:label: grasple_exercise_6_4_9
:dropdown:
:description: T/F? Every real $5 \times 5$ matrix has at least one real eigenvalue.
  

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1720d806-7602-41b3-9beb-569967e74c84?id=92543
:label: grasple_exercise_6_4_10
:dropdown:
:description: To find a complex diagonalization of a real  $2\times 2$ matrix (eigenvalues given).  

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/510f78e6-717e-4550-8564-7bbf2c2cf673?id=55388
:label: grasple_exercise_6_4_11
:dropdown:
:description: To find a complex diagonalization of a real  $3\times 3$ matrix (one eigenvalue given).  

::::::









