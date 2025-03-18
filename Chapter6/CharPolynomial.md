(Sec:EV:CharPoly)=

# The Characteristic Polynomial

Until now we have seen how we can check whether a real number is an eigenvalue, but we have not come up with a method to actually find the eigenvalues (better than just trying all real numbers one by one ...).

In this section we will show that **the eigenvalues are exactly the zeros of a polynomial function** intricately connected with the matrix $A$. So intricately that it is called the characteristic polynomial of $A$.

(Subsec:EV:DefCharPoly)=
## The definition of the characteristic polynomial

::::::{prf:proposition}
:label: Prop:Eigenvalues:DetAminusLambdaI

Suppose $A$ is an $n\times n$ matrix. Then $\lambda$ is an eigenvalue of $A$ if and only if the determinant of the matrix $A -\lambda I$ is equal to zero.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:Eigenvalues:DetAminusLambdaI`
:class: tudproof

There's not much new here.

We have seen in {prf:ref}`Prop:Eigenvalues:AminusLambdaI` that the statement

$\lambda$ is an eigenvalue of $A$

is equivalent to

$(A-\lambda I)\vect{x} = \vect{0}, \quad$ for a nonzero vector $ \vect{x}$.

We also know ({prf:ref}`Thm:MatrixInv:InvertibilityCharacterizations`) that such a nonzero solution exists only if

the matrix $A - \lambda I$ is **not** invertible,

and this, in its turn, is equivalent to

$$
\det({A - \lambda I)} = 0.
\nonumber
$$

::::::

::::::{prf:example}
:label: Ex:EigenValues:FirstCharPoly

Consider the matrix $A = \begin{bmatrix} 1 & 4 \\ 1 & 1 \end{bmatrix}$. We evaluate det$(A - \lambda I)$.

$$
\begin{vmatrix} 1-\lambda & 4 \\ 1 & 1-\lambda \end{vmatrix} = (1-\lambda) (1-\lambda) - 4 = \lambda^2 -2\lambda -3.
$$

So we see that $\lambda$ is an eigenvalue if and only if

$$
\lambda^2 -2\lambda -3 = (\lambda-3 )(\lambda+1) = 0
$$

and conclude that the eigenvalues of $A$ are $\lambda_1 =3, \lambda_2 = -1$. We call $\lambda_1$ a *double eigenvalue*.

::::::

{prf:ref}`Prop:Eigenvalues:DetAminusLambdaI` can also be used to show that a matrix does not have any (real) eigenvalues.

::::::{prf:example}
:label: Ex:Eigenvalues:NoEigenvalues

For the matrix $R=\begin{bmatrix} 0 & -1 \\ 1 & 0  \end{bmatrix}$ the determinant of $R - \lambda I$ becomes

$$
\begin{vmatrix} 0-\lambda & -1\\ 1 & 0-\lambda \end{vmatrix} =  \lambda^2 +1.
$$

Since this polynomial has no zeros, the matrix $A$ has no eigenvalues. We have already seen a geometric argument when we considered this matrix in {prf:ref}`Ex:EigenValues:Rotation`: $R$ is the matrix of a rotation.

In the remark immediately after that example we mentioned that it is possible to treat $\lambda = \pm i$ as eigenvalues of the matrix $R$. Of course these are exactly the _complex_ zeros of the polynomial $p(\lambda) = \lambda^2 + 1$.

::::::

In general, to compute the characteristic polynomial of an $n \times n$ matrix when $n > 2$ becomes cumbersome. And to find its zeros is close to impossible. There is one exception, which is when the matrix is of triangular form. Recall that this means that either all entries below the diagonal are zero (in which case the matrix is upper triangular), or all entries above the diagonal are zero.

::::::{prf:example}
:label: Ex:EigenValues:TriangularMatrix

Consider the matrix
$U = \begin{bmatrix} u_{11} & u_{12} & u_{13}  \\
0    & u_{22} & u_{23}  \\
0   &   0    & u_{33}
\end{bmatrix}$,
an arbitrary $3 \times 3$ upper triangular matrix.

Since $U - \lambda I$ is also an upper triangular matrix, we find that

$$
\text{det}(U - \lambda I) = ( u_{11}-\lambda)( u_{22}-\lambda)( u_{33}-\lambda).
$$

The last expression becomes 0 exactly for the values

$$
 \lambda_1 = u_{11}, \,\,\lambda_2 = u_{22},    \,\,\lambda_3 = u_{33}.
$$

So for a $3 \times 3$ upper triangular matrix the eigenvalues are the diagonal entries.

::::::

Obviously {prf:ref}`Ex:EigenValues:TriangularMatrix` can be generalized. This leads to the following proposition.

::::::{prf:proposition}
:label: Prop:EigenValues:TriangularMatrix

For any upper or lower triangular matrix $A$ the eigenvalues are given by the diagonal entries.

Note that this includes diagonal matrices $D$.

::::::

For the $2\times 2$ matrix in {prf:ref}`Ex:EigenValues:FirstCharPoly` the expression det$(A - \lambda I)$ eventually comes down to a polynomial of degree 2.

For an arbitrary $2 \times 2$ matrix $A = \begin{bmatrix} a-\lambda & b \\ c & d-\lambda \end{bmatrix}$ we quickly see that

$$
\text{det}(A - \lambda I) = \begin{vmatrix} a-\lambda & b \\ c & d-\lambda \end{vmatrix} =
(a-\lambda) (d-\lambda) - bc  = \lambda^2 - (a+d)\lambda + (ad-bc).
$$

Likewise, we saw that for $n\times n$ triangular matrices the characteristic polynomial is a polynomial of degree $n$.
That this can be generalized to arbitrary matrices is the content of the next proposition.

::::::{prf:proposition}
:label: Prop:EigenValues:CharPoly

For an $n\times n$ matrix $A$ the function det$(A - \lambda I)$ is a polynomial of degree $n$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:EigenValues:CharPoly`
:class: tudproof

We have to dive into the hardware of determinants a bit. If the determinant of an $n\times n$ matrix $M$ is computed by iteratively expanding along the first rows, i.e., doing it the hard way, we end up with a sum of $n!$ terms. Each term is the product of $n$ entries of $M$, where each row and each column of $A$ is represented exactly once.

Now we apply this to the matrix $M = (A  - \lambda I)$, where $A$ is the most general $n\times n$ matrix. We then can deduce that

$$
\text{det}(A - \lambda I) =
\begin{vmatrix} a_{11}-\lambda & a_{12} & a_{13} & \cdots & \cdots & a_{1n} \\
a_{21} & a_{22}-\lambda & a_{23} & \cdots & \cdots & a_{2n} \\
a_{31} & a_{32} & a_{33}-\lambda &  \cdots & \cdots & a_{3n} \\
\vdots & \vdots & \vdots & \ddots & \ddots & \vdots \\
\vdots & \vdots & \vdots & \ddots & \ddots & \vdots \\
a_{n1} & a_{n2} & a_{n3}&  \cdots & \cdots & a_{nn}-\lambda
\end{vmatrix}
$$

is indeed a polynomial function of $\lambda$, and the highest power of $\lambda$ comes from the product of the diagonal elements

$$
(a_{11}-\lambda)(a_{22}-\lambda)(a_{33}-\lambda) \cdots (a_{nn}-\lambda).
$$

We see that the highest power of $\lambda$ in this expression is the $n$-th power, and that its coefficient is $(-1)^n$.

::::::

The function det$(A - \lambda I)$ is of paramount importance. We will see that it reveals important intrinsic properties of the matrix $A$. It deserves a name.

::::::{prf:definition}

The function det$(A - \lambda I)$ is called the **characteristic polynomial** of $A$. We will sometimes denote it by
$p_A(\lambda)$, so

$$
p_A(\lambda) = \text{det}(A -\lambda I).
$$

::::::

Let us put the important properties of the characteristic polynomial that we have seen so far into a theorem.

::::::{prf:theorem}
:label: Thm:CharPoly:BasicProperties

The characteristic polynomial of the $n \times n$ matrix $A$

<ul>
<li>

is a polynomial of degree $n$,

</li>
</ul>

and

<ul>
<li>

its _zeros_ are the _eigenvalues_ of the matrix $A$.

</li>
</ul>

::::::

As a corollary we find a second argument why an $n\times n$ matrix cannot have more than $n$ different eigenvalues: a polynomial of degree $n$ can have at most $n$ zeros.

A note of warning: to compute the determinant of the matrix $A - \lambda I$ it may seem helpful to first row reduce the matrix $A$ to echelon form $E$, and then take the determinant of $E - \lambda I$, which is a triangular matrix. However, that procedure is incorrect. Except for very special cases, in general

$$
\det{(A - \lambda I)} \neq \det{(E - \lambda I)} !
$$

For instance, take the earlier example $ A = \left[\begin{array}{cc} 1 & 4 \\ 1 & 1 \end{array}\right]$ with characteristic polynomial

$$
\det{(A-\lambda I)}= (\lambda - 3)(\lambda+1).
$$

Since $A$ is invertible, $A$ can be row reduced to the echelon matrix $E = I$, the identity matrix, and

$$
\det{(E-\lambda I)} = (\lambda - 1)^2,
$$

which has nothing to do with $\det{(A - \lambda I)}$.

So, if you want to find the characteristic polynomial via row reduction of det$(A - \lambda I)$ you _have to include $\lambda$ right from the beginning_.

Let's look at one other example before we give the characteristic polynomial a closer look.

::::::{prf:example}
:label: Ex:EigenValues:SecondCharPoly

We find the characteristic polynomial of the matrix $A = \begin{bmatrix} 4 & -1 & -2 \\0 & 3 & 0 \\ 1 & 2 & 1 \end{bmatrix}$.

Because of the zeros in the second row a good start is to expand along this row:

$$
\begin{vmatrix} 4-\lambda & -1 & -2 \\0 & 3-\lambda & 0 \\ 1 & 2 & 1-\lambda \end{vmatrix} =
(3-\lambda)\begin{vmatrix} 4-\lambda  & -2 \\1 & 1-\lambda \end{vmatrix} =
(3-\lambda)\big((4-\lambda)(1-\lambda) +2)\big),
$$

which can be rewritten as

$$
(3-\lambda)(\lambda^2 - 5\lambda + 6).
$$

We certainly do **not** eliminate the parentheses here, since in this factorized form the eigenvalue $\lambda = 3$
is staring us right into the eyes.
From the last expression we read off that $\lambda$ is an eigenvalue of $A$ if either
$ (3-\lambda)=0 $ or $(\lambda^2 - 5\lambda +6)=0$. Noting that

$$
\lambda^2 - 5\lambda +6 = ( \lambda -2)(\lambda -3),
$$

we may conclude that the eigenvalues of this matrix are

$$
\lambda_1 = 3, \quad \lambda_2 = 2, \quad \lambda_3 = 3.
$$

::::::

From the examples so far it seems we have solved the question of how to find the eigenvalues. However, there is a proviso:
if we start with a 'full' $3 \times 3$ matrix $A$, there may be nothing better to do than to compute det$(A - \lambda I)$
by iteratively expanding across columns or rows. We then end up with a cubic polynomial, not in factorized form.
In general it will be quite a hard task to compute its zeros. Obviously, things get even worse in higher dimensions.

In the previous example ({prf:ref}`Ex:EigenValues:SecondCharPoly`) the eigenvalue $\lambda_1  = 3$  seems to play a different role than the eigenvalue $\lambda_2$. That is, the characteristic polynomial

$$
p_A(\lambda) = (\lambda-3)^2(\lambda -2)
$$

contains two factors $(\lambda - 3)$ and only one factor $(\lambda - 2)$. In algebra it is then said that $\lambda = 3$ is a zero/root of multiplicity 2 of the polynomial $p_A$, and likewise the root $\lambda = 2$ has multiplicity 1.


Another natural question is how many linearly **independent** eigenvectors  there are for an eigenvalue $\lambda$.  This we will refer to as the geometric multiplicity.

(Subsec:EV:AlgGeomMultiplicity)=
## Algebraic and geometric multiplicity

::::::{prf:definition}

The **algebraic multiplicity** of an eigenvalue $\lambda_k$ is the number of factors $(\lambda - \lambda_k)$ appearing in the characteristic polynomial. It is often abbreviated as **a.m.**($\lambda_k$).

The **geometric multiplicity** of an eigenvalue $\lambda_k$, with short 
notation **g.m.**($\lambda_k$),   is the dimension of the eigenspace corresponding to $\lambda_k$. In other words, it is the number of independent eigenvectors for $\lambda_k$.


::::::

::::::{prf:example}
:label: Ex:EigenValues:SecondCharPolyContinued

We continue with the matrix
$A = \left[\begin{array}{ccc} 4 & -1 & -2 \\0 & 3 & 0 \\ 1 & 2 & 1  \end{array}\right]$
of {prf:ref}`Ex:EigenValues:SecondCharPoly` and find the geometric multiplicities of the eigenvalues.
The characteristic polynomial of $A$ was found to be $p_A(\lambda) = (3-\lambda)^2(2-\lambda)$, so $A$ has the eigenvalues $\lambda_1 = 3$ with algebraic multiplicity $2$
and $\lambda_2 = 2$ with algebraic multiplicity $1$.

To find the geometric multiplicities we proceed as follows.

The eigenspace for $\lambda_{1}$ is the null space of $A - \lambda_{1} I = A -3I$.

$$
A - 3I = \left[\begin{array}{ccc} 4-3 & -1 & -2 \\0 & 3-3 & 0 \\ 1 & 2 & 1-3  \end{array}\right]
 =
\left[\begin{array}{ccc} 1 & -1 & -2 \\0 & 0 & 0 \\-1 & 2 & -2\end{array}\right]
  \sim
\left[\begin{array}{ccc} 1 & -1 & -2 \\0 & 1 & 0 \\0 & 0 & 0 \end{array}\right]
.
$$

This is a $3 \times 3$ matrix of rank 2, so its null space has dimension $3-2 =1$, and we conclude that the geometric multiplicity of the eigenvalue
$\lambda = 3$ is equal to 1.
For the other eigenvalue we perform a similar computation:

$$
A - 2I =  \left[\begin{array}{ccc} 4-2 & -1 & -2 \\0 & 3-2 & 0 \\ 1 & 2 & 1-2  \end{array}\right]
 =
\left[\begin{array}{ccc} 2 & -1 & -2 \\0 & 1 & 0 \\1 & 2 & -1 \end{array}\right]
  \sim
\left[\begin{array}{ccc}  1 & 2 & -1 \\0 & 1 & 0 \\0 & 0 & 0 \end{array}\right]
,
$$

from which we deduce that the geometric multiplicity of the eigenvalue $\lambda = 2$ is also equal to 1.

::::::

At this moment it is not so easy to prove the following proposition, of which the previous example gives an illustration. 
(For the proof: see the section 'Similar Matrices',  right after formula {eq}`Eq:Diagonalizable:GeomMultversusAlgMult`.)

::::::{prf:proposition}
:label: Prop:EigenValues:SmallerGeomMultiplicity

For every eigenvalue of a matrix $A$, the geometric multiplicity is at most equal to the algebraic multiplicity. So we always have

&nbsp; &nbsp; $1$ &nbsp; $\leq$ &nbsp;  geometric multiplicity of $\lambda$  &nbsp; $\leq$ &nbsp;  algebraic multiplicity of $\lambda$.

::::::

::::::{prf:definition}
:label: Def:Eigenvalues:Defect

A matrix $A$ that has an eigenvalue $\lambda$ for which the geometric multiplicity is *strictly smaller* than the algebraic multiplicity  is called a **defect** matrix.
::::::



As a consequence of {prf:ref}`Prop:EigenValues:SmallerGeomMultiplicity` there is one case where the geometric multiplicity follows immediately from the algebraic multiplicity.
Namely, if $\lambda$ is an eigenvalue of algebraic multiplicity 1, then the geometric multiplicity must be 1 too: it cannot be larger, because of {prf:ref}`Prop:EigenValues:SmallerGeomMultiplicity`, and it cannot be smaller either, since for any eigenvalue there must be at least one eigenvector.

::::::{prf:example}
:label: Ex:Eigenvalues:TwodimEigenspace2

The matrix $A = \begin{bmatrix} 1 & 2 & 2 \\ 2 & 1 & 2 \\ 2 & 2 & 1  \end{bmatrix}$
has the two independent eigenvectors
$\vect{v}_1 = \begin{bmatrix} 1 \\ 0 \\ -1  \end{bmatrix}, \vect{v}_2 =\begin{bmatrix} 0 \\ 1 \\ -1  \end{bmatrix}$
for the eigenvalue $\lambda = -1$, and the eigenvector $\vect{v}_3 = \begin{bmatrix} 1 \\1\\ 1  \end{bmatrix}$ for the eigenvalue 5.
(We studied this matrix in {prf:ref}`Ex:EigenValues:TwodimEigenspace2`.)
From {prf:ref}`Prop:EigenValues:SmallerGeomMultiplicity` we can deduce that the characteristic polynomial must contain at least two factors $(\lambda - (-1))$ and one factor $(\lambda - 5)$. Since its degree is equal to 3, and the coefficient of $\lambda^3$ is equal to $(-1)^3 = -1$, we may conclude that

$$
p_A(\lambda) = -(\lambda +1)^2(\lambda - 5).
$$

The eigenvalue $\lambda = -1$ has both algebraic multiplicity and geometric multiplicity equal to 2.

::::::

The following exercise, which is meant to shed some more light on the concepts just introduced, requires few technicalities.

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6e01d5c1-897b-44bf-bbb2-4653ff095f48?id=92498
:label: grasple_exercise_6_1_A
:dropdown:
:description:  Finding eigenvalues and their multiplicities for an upper triangular matrix $A$.

::::::


(Subsec:EV:SpecPropCharPoly)=
## Some special properties of the characteristic polynomial

In the proof of {prf:ref}`Prop:EigenValues:CharPoly` it was mentioned that for an $n \times n$ matrix $A$ the coefficient of the highest power $\lambda^n$  is equal to  $(-1)^n$.
In this subsection we will find expressions for two other coefficients of the characteristic polynomial. The results we mention are interesting in themselves, but they are not essential for the sequel.

::::::{prf:proposition}
:label: Prop:EigenValues:CharPolyTrace

Suppose the characteristic polynomial of the $n \times n$ matrix $A$ is given by

:::{math}
:label: Eq:EigenValues:CharPoly

p_A(\lambda) = c_n\lambda^n + c_{n-1}\lambda^{n-1} + \ldots + c_2\lambda^2 +c_1\lambda + c_0.

:::

Then the following identities hold for the coefficients $c_n, c_{n-1}$ and $c_0$:

$$
c_n = (-1)^n, \quad c_{n-1} = (-1)^{n-1} (a_{11}+a_{22}+\ldots + a_{nn})
$$

and

$$
  c_0 = \text{det}(A).
$$

::::::

::::::{admonition} (Sketch of the) Proof of&nbsp;{prf:ref}`Prop:EigenValues:CharPolyTrace`
:class: tudproof, dropdown

For $n=2$ we have already seen that the characteristic polynomial of the most general $2 \times 2$ matrix
$A = \left[\begin{array}{cc} a_{11} & a_{12} \\ a_{21} & a_{22} \end{array}\right]
= \left[\begin{array}{cc} a & b \\ c & d \end{array}\right] $ is given by

$$
\text{det}(A - \lambda I) = \begin{vmatrix} a-\lambda & b \\ c & d-\lambda \end{vmatrix} =
\lambda^2 - (a+d)\lambda + (ad-bc).
$$

which is indeed equal to

$$
(-1)^2 \lambda^2 + (-1)^1 (a_{11}+a_{22})\lambda + \det{(A)}.
$$

The value of $c_0$ is the easiest to establish: just plug in $\lambda=0$ in 
Equation {eq}`Eq:EigenValues:CharPoly`:

$$
\text{det}(A)= \text{det}(A - 0I) = p_A(0) = c_n0^n + c_{n-1}0^{n-1} + \ldots + c_1\cdot 0 + c_0 = c_0.
$$

For the other  coefficient we will not give the slightly technical  argument for an $n\times n$ matrix.  The idea will be pretty much clear when we consider a general $3 \times 3$ matrix

$$
 A = \left[\begin{array}{ccc} a_{11} & a_{12} & a_{13} \\a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}  \end{array}\right].
$$ 



When we expand

<!-- prettier-ignore -->
$ \quad  \text{det}(A - \lambda I) = \left|\begin{array}{ccc} a_{11}- \lambda  & a_{12} & a_{13} \\
a_{21} & a_{22}- \lambda  & a_{23} \\
a_{31} & a_{32} & a_{33}- \lambda  \end{array}\right|\quad $

along its first row we find

$$
(a_{11}- \lambda) \left|\begin{array}{cc}  a_{22}- \lambda  & a_{23} \\
a_{32} &  a_{33}- \lambda  \end{array}\right|-
a_{12} \left|\begin{array}{ccc}  a_{21}  & a_{23} \\
a_{31}  & a_{33}- \lambda  \end{array}\right|+
a_{13} \left|\begin{array}{ccc}  a_{21}  & a_{22}-  \lambda  \\
a_{31}  & a_{32}  \end{array}\right|.
$$

The highest power of $\lambda$ coming from the second and the third terms is $\lambda^1$, so the coefficients of $\lambda^3$ and of $\lambda^2$
are completely determined by the first term. A closer look at that term yields that these two coefficients in fact come from the product $(a_{11}-\lambda)(a_{22}-\lambda)(a_{33}-\lambda)$. For a general $n\times n$ matrix $A$ the first two coefficients also come from the 'diagonal product' of the complete expansion of $\det{(A - \lambda I)}$.

Expanding this product further we see that

$$
(a_{11}-\lambda)(a_{22}-\lambda)(a_{33}-\lambda) = -\lambda^3 + (a_{11} + a_{22} + a_{33}) \lambda^2 +  \ldots \lambda + \ldots 
$$

Thus the coefficients $c_3$  and $c_2$ of $\lambda^3$  and $\lambda^2$ are indeed as stated, i.e.

$$
c_3 = -1 = (-1)^3, \quad  c_2 = a_{11} + a_{22} + a_{33} = (-1)^2(a_{11} + a_{22} + a_{33}).
$$

::::::

::::::{prf:definition}
:label: Dfn:Eigenvalues:Trace

The sum of the diagonal entries of an $n\times n$ matrix $A$ is called the **trace** of $A$:

$$
\text{tr}(A) = a_{11} + a_{22} + \ldots + a_{nn} = \sum_{i=1}^{n}  a_{ii}.
$$

::::::

With this new terminology we can restate the second property in {prf:ref}`Prop:Eigenvalues:SumEigenvaluesAndTrace`  as follows.  For an $n\times n$ matrix $A$  the coefficient $c_{n-1}$ of $\lambda^{n-1}$ satisfies

 $$
   c_{n-1} = (-1)^{n-1} \text{tr}(A).
 $$

::::::{prf:proposition}
:label: Prop:Eigenvalues:SumEigenvaluesAndTrace

Let   $A$ an $n\times n$ matrix with $n$ eigenvalues  $\lambda_1,\lambda_2,  \ldots , \lambda_n$, where eigenvalues/zeros of multiplicity $k$ are counted $k$ times. Then the sum of the eigenvalues is equal to the trace of $A$ and the product of the eigenvalues equals the determinant of $A$. For short:

:::{math}
:label: Eq:Eigenvalues:SumEigenvaluesAndTrace


\sum_{i = 1}^{n} \lambda_i = \text{tr}(A) \quad \text{and} \quad \prod_{i = 1}^{n} \lambda_i = \text{det}(A).


:::

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:Eigenvalues:SumEigenvaluesAndTrace`
:class: tudproof, dropdown

This is more a statement about algebra, in particular about polynomials, than about linear algebra.  In  {numref}`Section %s <Section:ComplexEV>`  we will see that it also holds for matrices with complex eigenvalues. 

If $A$ has $n$ real eigenvalues $\lambda_1, \ldots, \Lambda_n$,  the characteristic polynomial $p_A(\lambda)$ of $A$  must contain the $n$ factors $(\lambda - \lambda_i)$.   Since the 'leading' coefficent'  $c_n = (-1)^n$  we may deduce that  

$$
\begin{array}{rcl}
p_A(\lambda) &=& (-1)^n (\lambda - \lambda_1)(\lambda - \lambda_2) \cdots (\lambda - \lambda_n) \\
&=&  (\lambda_1 - \lambda)(\lambda_2 - \lambda) \cdots (\lambda_n - \lambda).
\end{array}
$$

Now we focus on the coefficient of $\lambda^{n-1}$ and the constant term:

$$
p_A(\lambda)  = (-1)^n \big[\lambda^n -(\lambda_1+\lambda_2+ \cdots+\lambda_n)\lambda^{n-1} + \ldots + (-1)^n\lambda_1\cdot\lambda_2\cdots\lambda_n\big].
$$

Comparing this with the expressions for the coefficients we found in {prf:ref}`Prop:Eigenvalues:SumEigenvaluesAndTrace`

$$
p_A(\lambda) = (-1)^n \lambda^n + (-1)^{n-1}\text{tr}(A) \lambda^{n-1} + \ldots + \Det{A},
$$

we readily read off the identities put forward in 
Equation {eq}`Eq:Eigenvalues:SumEigenvaluesAndTrace`.

::::::

The identity involving the sum gives an easy check on the eigenvalues; with the other identity one has to do some work to apply it for a check. The next example gives an illustration.

::::::{prf:example}
:label: Ex:Eigenvalues:SumEigenvaluesAndTrace

In {prf:ref}`Ex:EigenValues:SecondCharPoly` we found that the eigenvalues of the matrix
$A = \begin{bmatrix} 4 & -1 & -2 \\0 & 3 & 0 \\ 1 & 2 & 1 \end{bmatrix}$  &nbsp; are &nbsp; $\lambda_{1,3} = 3$, $\lambda_{2} = 2$.

We see that indeed

$$
\lambda_1+\lambda_2+\lambda_3 = 3 +2 + 3 = 8 = 4+3+1 = \text{tr}(A),
$$

and also  

$$
  \text{det}\,A = 3 \begin{vmatrix} 4 & -2 \\ 1 &  1 \end{vmatrix} = 3\cdot (4+2) = 18 = 3\cdot3\cdot2 =   \lambda_1\lambda_2\lambda_3.
$$

::::::

The last  'mind blowing' property of the characteristic polynomial we will only illustrate by an example.

::::::{prf:example}
:label: Ex:Eigenvalues:CayleyHamilton

Consider the matrix $A = \begin{bmatrix} 1 & 2 \\ 4 & 5 \end{bmatrix}$.
Its characteristic polynomial is computed as

$$
  \det{(A-\lambda I)} = \begin{vmatrix} 1-\lambda & 2 \\ 3 & 5-\lambda \end{vmatrix}
  = (1-\lambda)(5-\lambda) - 8= \lambda^2 - 6\lambda - 3.
$$

Now if we replace  in this last expression  $\lambda$ by the matrix $A$, where we then interpret the term $3$ as the matrix $3I$, we get

$$
 A^2 - 6A - 3I = \begin{bmatrix} 9 & 12 \\ 24 & 33 \end{bmatrix} -
 \begin{bmatrix} 6 & 12 \\ 24 & 30 \end{bmatrix} - \begin{bmatrix} 3 & 0 \\ 0 & 3 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}.
$$

So, interpreting the constant term as we did, we have for this matrix $A$ established the property

$$
   p_A(A) = O,
$$

the zero matrix.

::::::

That this is not a coincidence is the content of the following theorem, the proof of which is beyond the scope of this linear algebra book. (The interested reader can of course search the internet on "Cayley-Hamilton".)

::::::{prf:theorem}  Cayley-Hamilton
:label: Thm:Eigenvalues:CayleyHamilton


Every matrix $A$ is a zero of its characteristic polynomial.
::::::


## Grasple Exercises 



::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b43cd5dc-3fff-432a-bdec-d56e38c39e89?id=91450
:label: grasple_exercise_6_2_1
:dropdown:
:description:  To find the characteristic polynomial of a $2\times 2$ matrix $A$.


::::::


::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b89efbb3-c5cc-4fab-874b-8dd285644ab2?id=91452
:label: grasple_exercise_6_2_2 
:dropdown:
:description:  To find the eigenvalues of a $2\times 2$ matrix $A$.

::::::


::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/137aaf98-60d5-4aab-82f4-10ea40811a7b?id=91453
:label: grasple_exercise_6_2_3 
:dropdown:
:description:  To find the eigenvalues of a $3\times 3$ matrix $A$.

::::::



::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e3793a52-25f0-48cd-b47f-b59f872e3e1a?id=91454
:label: grasple_exercise_6_2_4 
:dropdown:
:description:  To find the eigenvalues of a $3\times 3$ matrix $A$.

::::::


::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3597a3e9-17b7-491c-89a7-4f33f1a4fb8c?id=91482
:label: grasple_exercise_6_2_5
:dropdown:
:description:  To find the eigenvalues of a $4\times 4$ matrix $A$.

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9e16e7ab-87f1-448c-a52a-a8d6c1470c4b?id=91483
:label: grasple_exercise_6_2_6 
:dropdown:
:description:  Is an eigenvalue of a matrix $A$ always an eigenvalue of $A^T$?


::::::





::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2c30dad3-17a4-4f20-b277-fd13e0c93e9f?id=92384
:label: grasple_exercise_6_2_7 
:dropdown:
:description: Finding the geometric multiplicities of the eigenvalues of a $3\times3$ matrix $A$. 

::::::


::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e35e7cfb-2a21-4849-ae48-6c7a94e85707?id=92409
:label: grasple_exercise_6_2_8
:dropdown:
:description:  Finding the geometric multiplicity of the eigenvalue of a $3\times3$ matrix $A$. 

::::::


::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/eb3e8ea4-3a0b-4767-aa62-0d8b05e35dda?id=91484
:label: grasple_exercise_6_2_9
:dropdown:
:description:  To find the eigenvalues and their multiplicities of an almost upper triangular $4 \times 4$ matrix $A$.

::::::


::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e9044c04-4bfb-474e-8823-bff6449b92ab?id=92210
:label: grasple_exercise_6_2_10 
:dropdown:
:description:  To find the geometric multiplicity of the single eigenvalue of an almost diagonal matrix $A$.

::::::


::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/82387c7b-49c8-4438-b72c-e1d023fb2780?id=92211
:label: grasple_exercise_6_2_11
:dropdown:
:description:  To find the geometric multiplicities of the eigenvalues of an almost diagonal matrix $A$.

::::::


::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b846c6e6-f2c6-4d5b-bc40-adaed4cf6276?id=92490
:label: grasple_exercise_6_2_12
:dropdown:
:description:  To find the 2nd and 3rd eigenvalue of $3\times 3$ matrix with known determinant and trace.

::::::
