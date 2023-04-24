(Sec:QuadraticForm)=
# Quadratic Forms

(Subsec:Terminology)=
## Introduction and Terminology

The simplest functions from $\R^n$ to $\R$ are linear functions 

$$
   f(x_1,\ldots,x_n) = \sum_{i=1}^n a_ix_i +b \, =\, a_1x_2 + a_2x_2 + \ldots + a_nx_n + b.
$$

In short  $f(\mathbf{x}) = \mathbf{a}^T\mathbf{x} + b$,  for some vector $\mathbf{a}$ in $\R^n$ and some number $b$ in $\R$.

After that come the *quadratic functions*  

$$
   q(x_1,\ldots,x_n) = \sum_{i,j=1}^{n} a_{ij}x_ix_j + \sum_{i=1^n} b_ix_i + c,
$$

in short $q(\mathbf{x}) = \mathbf{x}^TA\mathbf{x} + \mathbf{b}^T\mathbf{x} + c$, for an $n\times n$ matrix $A$, a vector $\vect{b}$ in $\R^n$, and a number $c$ in $\R$.

The part  $\mathbf{x}^TA\mathbf{x}$ is called a **quadratic form**.

::::{prf:example}
:label: Ex:QuadForms:Diagonalize

For the matrix  $A = \begin{bmatrix} 1 & 2 \\ 4 & 3 \end{bmatrix}$  the corresponding quadratic form is 

$$
  \begin{array}{rcl}
  q(\vect{x}) =  \begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 4& 3 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} 
   &=& \begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} x_1 + 2x_2 \\ 4x_1+ 3x_2 \end{bmatrix} \\
   &=& x_1^2 + (2+4)x_1x_2 + 3x_2^2 \\
   &=& x_1^2 + 6x_1x_2 + 3x_2^2.
   \end{array}
$$
::::

The quadratic form does not uniquely determine the matrix. 
For example, the matrix  $A_2 = \begin{bmatrix} 1 & 1 \\ 5 & 3 \end{bmatrix}$ also gives

$$
 \mathbf{x}^TA_2\mathbf{x} = x_1^2+(1+5)x_1x_2 + 3 x_2^2 = x_1^2+ 6x_1x_2 + 3 x_2^2
$$

However,  if we require the matrix to be *symmetric*, then each quadratic form
leads to one matrix representing it



::::{prf:example}

We will find the symmetric matrix $A$ for the symmetric form

$$
    q(x_1,x_2,x_3) = x_1^2 + 2x_2^2 + 5 x_3^2  - 4 x_1x_2 + 6 x_2x_3.
$$

So we need a symmmetric matric  $A = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ 
                                                     a_{21} & a_{22} & a_{23} \\
                                                     a_{31} & a_{32} & a_{33}
                                     \end{bmatrix}$.

From  

$$
 \begin{array}{rl}
  \mathbf{x}^TA\mathbf{x} = & a_{11}x_1^2 + a_{22}x_2^2 + a_{33}x_3^3 \\
   & + (a_{12}+a_{21})x_1x_2 + (a_{13}+a_{31})x_1x_3 + (a_{23}+a_{32})x_2x_3
 \end{array}  
$$

we read off that $ a_{11} = 1$,  $a_{22} = 2$, $a_{33} = 5$, 

and $a_{12}=a_{21} = -2$,  $a_{13}= a_{31} = 0= 2$, $a_{23} = a_{32}= 3$.


So  $A = \begin{bmatrix} 1 & -2 & 0 \\ 
                        -2 &  2 & 3 \\
                         0 &  3 & 5 
         \end{bmatrix}$.

::::

When we speak of *the matrix of a quadratic equation*  we will always mean the symmetric matrix.

If we restrict ourselves to two variables we see that 
the graph of a linear function  $z = a_1x_1 + a_2x_2 + b$ is a plane.


:::{figure} Images/Fig-QuadForms-Plane1.svg
:name: Fig:QuadForms:Plane1

The plane  $z = \frac13x_1 - x_2 +2$
:::

:::{figure} Images/Fig-QuadForms-Plane2.svg
:name: Fig:QuadForms:Plane2

The plane  $z = -x_1 - \frac12x_2 +3$
:::

The graph of a quadratic function is a curved surface.
{numref}`Figure %s <Fig:QuadForms:QuadSurface1>`  and {numref}`Fig:QuadForms:QuadSurface2` show two of these quadratic surfaces.

:::{figure} Images/Fig-QuadForms-QuadSurface1.svg
:name: Fig:QuadForms:QuadSurface1

The surface  $z = -\frac13x_1^2 + \frac13x_2^2 + 2 $
:::

:::{figure} Images/Fig-QuadForms-QuadSurface2.svg
:name: Fig:QuadForms:QuadSurface2

The surface  $z = -\frac12x_1^2 - \frac14x_2^2 + x_1 - y_2 + 2$
:::

The shape of the surfaces is determined by the quadratic part  $\vect{x}^TA\vect{x}$.  The linear part is only relevant for the position.

::::{prf:example}

The surfaces  defined by

$$
   \mathcal{S}_1: z = 2x_1^2 - 2x_1x_2 + x_2^2  \quad \text{and} \quad
   \mathcal{S}_2: z = 2x_1^2 - 2x_1x_2 + x_2^2 + 8x - 6y + 4
$$

are shifted versions of the same surface.  Namely,

$$
   2x_1^2 - 2x_1x_2 + x_2^2 + 8x - 6y + 4 = 2(x_1+1)^2 - 2(x_1+1)(x_2-2) + (x_2-2)^2 - 6.
$$

Thus  $\mathcal{S}_2$  is also described by

$$
  z + 6 = 2(x_1+1)^2 - 2(x_1+1)(x_2-2) + (x_2-2)^2 
$$

This means that if $\mathcal{S}_1$ is translated over the vector 
$\left[\begin{array}{c} -1 \\ 2 \\ -6 \end{array}\right]$ it becomes the  surface $\mathcal{S}_2$.
::::

For the rest of the section we will therefore only look at the quadratic part $\vect{x}^TA\vect{x}$.  

One of the  simplest quadratic forms results when we take $A = I = I_n$, the identity matrix.
Then we have

$$
  q(\vect{x}) = \vect{x}^TI_n\vect{x} = \vect{x}^T_n\vect{x} =x_1^2 + x_2^2 + \ldots + x_n^2 = \vect{x}\ip\vect{x}.
$$

For this quadratic form, it is clear that it will only take on nonnegative values. And that 

$$
   q(\vect{x}) = 0   \quad \iff \quad  \vect{x}=\vect{0}.
$$

Such a quadratic form is called *positive definite*.
In the next subsection we will learn how to find out whether an arbitrary quadratic form has this property.


(Subsec:SignOfQuadForm)=
## Diagonalization of quadratic forms

Let's consider an example, to get some feeling for what is going on.

::::{prf:example}
:label: Ex:QuadForms:CompleteSquares

Consider the quadratic form

$$
   q(x_1,x_2) = x_1^2 + 4x_1x_2 + 3x_2^2 = 
   \begin{bmatrix}x_1 & x_2 \end{bmatrix} \begin{bmatrix}1 & 2 \\ 2 & 3 \end{bmatrix}\begin{bmatrix}x_1 \\ x_2 \end{bmatrix} = \vect{x}^TA\vect{x} .
$$

At first sight you might think that this quadratic form only takes on nonnegative values.
One way to show that this is not actually true is by *completing squares*.

$$
  x_1^2 + 4x_1x_2 + 3x_2^2 = (x_1 + 2x_2)^2 - 4x_2^2 + 3x_2^2 = (x_1 + 2x_2)^2 - x_2^2.
$$

For the last expression, that does not contain a *cross term*, we can see how we can get a negative outcome. For instance, if we take  $x_2 = 1$ and $x_1 = -2$,  we find that

$$
  q(x_1,x_2) = q(-2,1) = (-2+2\cdot1)^2 - 1^2 = -1.
$$

::::

One way to describe in a more abstract/general way what we did in {prf:ref}`Ex:QuadForms:CompleteSquares` is the following.
We can introduce new variables  $y_1, y_2$ via the *substitution*

$$
   \left\{ \begin{array}{l}
              y_1 = x_1 + 2x_2 \\
              y_2 = \quad x_2.
            \end{array}  
      \right.
      \quad \quad\text{For short:} \quad
      \vect{y} = \left[\begin{array}{c} y_1  \\ y_2 \end{array}\right] =  \left[\begin{array}{cc} 1 & 2  \\ 0 & 1 \end{array}\right]\left[\begin{array}{c} x_1  \\ x_2 \end{array}\right] = B\vect{x}.
$$

Then  in terms of the new variables the quadratic form becomes

$$
  q(\vect{x}) = (x_1 + 2x_2)^2 - x_2^2 = y_1^2 - y_2^2 = 
  \begin{bmatrix}y_1 & y_2 \end{bmatrix} \begin{bmatrix}1  & 0 \\ 0 &-1 \end{bmatrix}\begin{bmatrix}y_1 \\ y_2 \end{bmatrix} = \vect{y}^TD\vect{y}.
$$

<BR>

Actually, it proves slightly advantageous to express the substitution as
$\vect{x} = P\vect{y}$.  We then have the following proposition.

::::{prf:proposition}  Quadratic form under a substitution
:label: Prop:QuadForms:Substitution

The substitution  $\vect{x} = P\vect{y}$  brings the quadratic form  

$$
  q(\vect{x}) = \vect{x}^TA\vect{x}
$$

over to

$$
  \tilde{q}(\vect{y}) = \vect{y}^TP^TAP\vect{y}.
$$

::::


::::{prf:proof}

This is a one line proof.

$$
    q(\vect{x}) = \vect{x}^TA\vect{x} \,\,\stackrel{\scriptsize \vect{x} = P\vect{y}}{\longrightarrow}\,\, 
    \tilde{q}(\vect{y}) =     (P\vect{y})^TA(P\vect{y}) = \vect{y}^TP^T A P \vect{y}.
$$

::::


::::{prf:example}

In {prf:ref}`Ex:QuadForms:CompleteSquares` we considered the substitution

$$
  \vect{y} = \left[\begin{array}{cc} 1 & 2  \\ 0 & 1 \end{array}\right]\vect{x}
$$

or, equivalently

$$
  \vect{x} = \left[\begin{array}{cc} 1 & 2  \\ 0 & 1 \end{array}\right]^{-1}\vect{y} =
             \left[\begin{array}{cc} 1 & -2  \\ 0 & 1 \end{array}\right]\vect{y} = P \vect{y} 
$$

to the quadratic form

$$
  q(\vect{x}) = \vect{x}^T\left[\begin{array}{cc} 1 & 2  \\ 2 & 3 \end{array}\right]\vect{x}.
$$


We then have

$$
\begin{array}{rcl}
  P^TAP &=&  \begin{bmatrix} 1 & -2  \\ 0 & 1 \end{bmatrix}^T\begin{bmatrix} 1 & 2  \\ 2 & 3 \end{bmatrix}\begin{bmatrix} 1 & 2  \\ 2 & 3 \end{bmatrix}\begin{bmatrix} 1 & -2  \\ 0 & 1 \end{bmatrix} \\
        &=&
   \begin{bmatrix} 1 & 0  \\ -2 & 1 \end{bmatrix}\begin{bmatrix} 1 & 0  \\ 2 & -1 \end{bmatrix} = \begin{bmatrix} 1 & 0  \\ 0 & -1 \end{bmatrix}.
   \end{array}
$$

According to {prf:ref}`Prop:QuadForms:Substitution` we then get the quadratic form

$$
   \tilde{q}(y) = \vect{y}^TP^TAP\vect{y} = \vect{y}^T\left[\begin{array}{cc} 1 & 0  \\ 0 & -1 \end{array}\right]\vect{y} = y_1^2 - y_2^2.
$$

This agrees with what we derived in {prf:ref}`Ex:QuadForms:CompleteSquares`.

::::

The technique of completing the squares to 'diagonalize' a quadratic form also works for quadratic forms in $n$ variables. 

Using the properties of symmetric matrices provides another route. This route we explore in the next proposition.

::::{prf:proposition} 
:label: Prop:QuadForms:Diagonalize

Suppose  $A$ is a symmetric matrix.  Then $A = QDQ^{-1}$, for an orthogonal matrix $Q$
(cf. {prf:ref}`Thm:SymmetricMat:OrthogDiag`).

Applying the substitution  $\vect{x} = Q\vect{y}$ to the quadratic form

$$
    q(\vect{x}) = \vect{x}^TA\vect{x}
$$

yields the quadratic form

$$
  \vect{y}^TD\vect{y} = \lambda_1y_1^2 + \lambda_2y_2^2 + \ldots + \lambda_ny_n^2,
$$

where $\lambda_1, \ldots, \lambda_n$ are the eigenvalues of the matrix $A$.
::::

::::{prf:proof}

Recall that an orthogonal matrix is a square matrix for which  $Q^TQ = I$.
Equivalently,  $Q^T = Q^{-1}$.

Second, recall that if $A = PDP^{-1}$, then the diagonal elements of $D$ are the eigenvalues of $A$.


The conclusion then follows immediately from {prf:ref}`Prop:QuadForms:Substitution`.
Namely, if we make the substitution  $\vect{x} = Q\vect{y}$  we find that

$$
  \vect{x}^TA\vect{x} = (Q\vect{y})^TQDQ^{-1}(Q\vect{y}) = \vect{y}^TQ^TQD
  Q^{-1}Q\vect{y} = \vect{y}^TD\vect{y}.
$$

Recall that  both $Q^TQ = I$  and   $Q^{-1}Q = I$.
::::

Let us see how the construction of {prf:ref}`Prop:QuadForms:Diagonalize` works out in an earlier example.


::::{prf:example}

Consider again the matrix  $A = \left[\begin{array}{cc} 1 & 2  \\ 2 & 3 \end{array}\right]$  of {prf:ref}`Ex:QuadForms:CompleteSquares`.

Its characteristic polynomial is given by

$$
  p_A(\lambda) = (1-\lambda)(3-\lambda)-4 = \lambda^2 - 4\lambda - 1.
$$

The eigenvalues (not very nice) are

$$
   \lambda_1 = 2 + \sqrt{5}, \quad \lambda_2 = 2 + \sqrt{5}.
$$

So  if we take $Q = \begin{bmatrix} \vect{q}_1 & \vect{q}_2 \end{bmatrix}$, where
$\vect{q}_1$ and $\vect{q}_2$ are corresponding eigenvectors of unit length (even less nice),  we find that the substitution  $\vect{x} = Q\vect{y}$ leads to 


$$
  \vect{x}^TA\vect{x}  \,\stackrel{\scriptsize \vect{x} = Q\vect{y}}{\longrightarrow}\,
  \vect{y}^TD\vect{y} = (2 + \sqrt{5})y_1^2 - (2 - \sqrt{5})y_2^2.
$$

Since $(2 + \sqrt{5})> 0$ and $(2 - \sqrt{5})<2-2=0$ we may again conclude that the quadratic form takes on both positive and negative values.

::::


::::{prf:remark}
 In {prf:ref}`Ex:QuadForms:CompleteSquares` and {prf:ref}`Ex:QuadForms:Diagonalize` we applied  two different substitutions to the same quadratic form with the matrix  $A = \left[\begin{array}{cc} 1 & 2  \\ 2 & 3 \end{array}\right]$.

 They led to the two different quadratic forms 

 $$
   \vect{y}^TD_1\vect{y} = \vect{y}^T\begin{bmatrix}1 & 0\\ 0 & -1 \end{bmatrix}\vect{y} \quad \text{and} \quad
   \vect{y}^TD_2\vect{y} = \vect{y}^T\begin{bmatrix}2 + \sqrt{5} & 0\\ 0 & 2 - \sqrt{5}\end{bmatrix}\vect{y}.
 $$  

The diagonal matrices do not seem to have much in common.  However, they do.

It can be shown that if for a symmetric $n\times n$ matrix  $A$ it holds that

$$
  P_1^TAP_1 = D_1 \quad \text{and} \quad P_2^TAP_2 = D_2,
$$

for two invertible matrices $P_1$, $P_2$, 
then the signs of the values on the diagonals of $D_1$ and $D_2$ match in the following sense: <BR> if  $p_1$, $p_2$ denote the numbers of positive diagonal elements of $D_1$ and $D_2$,
$n_i$ the numbers of negative diagonal elements, then

$$
  p_1 = p_2 \quad \text{and} \quad n_1 = n_2.
$$

It follows that also the numbers of zeros on the diagonal, $n - p_i - n_i$, $i = 1,2$,  must be equal for the two matrices.

This property is known as *Sylvester's Law of Inertia*.

::::

(Subsec:PosDefMatrices)=
## Positive definite matrices

Let's start with a list of definitions.

::::{prf:definition}  Classification of Quadratic Forms
:label: Dfn:QuadForms:DefiniteMatrix

Let $A$ be a symmetric matrix and  $q_A(\vect{x}) = \vect{x}^TA\vect{x}$ the corresponding quadratic form.

<ul>

<li>  

$q_A$ is called  **positive definite**    if $q_A(\vect{x}) > 0$ for all $\vect{x} \neq \vect{0}$.

</li>

<li>  

$q_A$ is called  **positive semi-definite**    if $q_A(\vect{x}) \geq 0$ for all $\vect{x} \neq \vect{0}$, and $q_A(\vect{x}) = 0$ for some $\vect{x} \neq \vect{0}$.

</li>

<li>  

$q_A$ is called  **negative definite**    if $q_A(\vect{x}) < 0$ for all $\vect{x} \neq \vect{0}$.

</li>

<li>  

$q_A$ is called  **negative semi-definite**    if $q_A(\vect{x}) \leq 0$ for all $\vect{x} \neq \vect{0}$, and $q_A(\vect{x}) = 0$ for some $\vect{x} \neq \vect{0}$.

</li>

</ul>

If none of the above applies, then $q_A$ is called an **indefinite**  quadratic form.

The same classification is used for symmetric matrices.  E.g.,  $A$ is a **positive definite matrix**  if the corresponding quadratic form is positive definite.

::::

The classification of a quadratic form follows immediately from the eigenvalues of its matrix.

::::{prf:theorem}
:label: Thm:QuadForms:Classification

Suppose    $q_A(\vect{x}) = \vect{x}^TA\vect{x}$  for the symmetric $n \times n$ matrix $A$. 
Let  $\lambda_1, \ldots, \lambda_n$ be the complete set of (real) eigenvalues of $A$

Then 

<ul>

<li>  

$q_A$ is   **positive definite**    if  and only if all eigenvalues are positive.

</li>

<li>  

$q_A$ is   **positive semi-definite**    if   and only if  all eigenvalues are nonnegative, and $0$ is an eigenvalue.

</li>

</ul>

Likewise for negative (semi-)definite, and lastly 

<ul>

<li>  

$q_A$ is   **indefinite**    if   at least one  eigenvalues is positive, and at least one eigenvalue is negative.


</li>
</ul>

::::

::::{prf:proof}

This immediately follows from  {prf:ref}`Prop:QuadForms:Diagonalize`.

If we make the substitution $\vect{x} = Q\vect{y}$, with the matrix $Q$ of the orthogonal diagonalization  

$$
  A = QDQ^{-1} = QDQ^T, \quad 
  D = \left[\begin{array}{cccc} 
  \lambda_1 & 0 & \ldots & 0  \\ 
  0 & \lambda_2 & \ldots & 0 \\
  \vdots & \vdots & \ddots &\vdots\\
  0 & 0 & \ldots & \lambda_n
  \end{array}\right]
  $$

the quadratic form transforms to

$$
  \tilde{q}(\vect{y}) = \vect{y}^TD\vect{y} = \lambda_1y_1^2 + \ldots + \lambda_ny_n^2.
$$

If all eigenvalues $\lambda_i$ are positive, the last expression is positive for all $\vect{y} \neq \vect{0}$,  and hence for all nonzero  vectors $\vect{x} = Q\vect{y}$ too. Here we use that $Q$ is invertible,  so  $Q\vect{y} = \vect{0} \iff \vect{y} = \vect{0}$.

Likewise the other possibilities of the signs of the eigenvalues may be checked.

::::

::::{exercise}
:label: Exc:QuadForms:CheckTheorem

Verify the validity the other statements made in {prf:ref}`Thm:QuadForms:Classification`.

::::

::::{prf:example}
:label: Ex:QuadForms:CompleteSquares2


Consider the quadratic form

$$
  q(x_1,x_2,x_3) = 2x_1^2 + x_2^2 +x_3^2  - 2x_1x_2 - 2x_1x_3.
$$

The matrix of this quadratic form is

$$
  A = \left[\begin{array}{cc} 2 & -1 & -1  \\ -1 & 1 & 0 \\ -1 & 0 & 1 \end{array}\right].
$$

The eigenvalues of $A$ are computed as

$$
   \lambda_1 = 3, \quad \lambda_2 = 1, \quad \lambda_3 = 0.
$$

With {prf:ref}`Thm:QuadForms:Classification` in mind, we can conclude that the quadratic form is positive semi-definite.

::::

::::{exercise}  Completing  squares  once more
:label: Exc:QuadForms:CompleteSquares2

Show that the quadratic from in {prf:ref}`Ex:QuadForms:CompleteSquares2` can be rewritten
as follows

:::{math}
:label: Eq:QuadForms:CompleteSquares2

  q(x_1,x_2,x_3) = 2(x_1 - \tfrac12x_2 - \tfrac12x_3)^2 + \tfrac12(x_2 + x_3)^2.   

:::

<ol type = "i">

<li>

What is the corresponding transformation $\vect{y} = P\vect{x}$ that brings the quadratic form in diagonal form  $\vect{y}^TD_2\vect{y}$, and what is the diagonal matrix $D_2$?

</li>


<li>

 By inspection of $D_2$ find the classification of $q$.

</li>

<li>

 By inspection of Equation {eq}`Eq:QuadForms:CompleteSquares2`,  find a nonzero vector
 $\vect{x}$  for which   $q(\vect{x}) = 0$.

</li>

<li>

 Check that the vector you found in  iii. is an eigenvector of the matrix of the quadratic form,  i.e.,  $A = \left[\begin{array}{cc} 2 & -1 & -1  \\ -1 & 1 & 0 \\ -1 & 0 & 1 \end{array}\right]$.

</li>

</ol>

::::

(Subsec:ConicSections)=
## Conic Sections

A *conic section*  or *conic* is a curve that results when a circular cone is intersected with a plane. Figure ... shows the different shapes when the plane is not going through the apex.  The resulting curve is either  a *hyperbola*, a *parabola* or an *ellipse*, with as special ellipse the *circle*.  If the plane does  go through the apex of the cone the conic section is called **degenerate**. 


::::{exercise}

Describe the (three)  possible degenerate forms of conic intersections.

::::


In the plane these curves are all described by a quadratic equation

::::{math}
:label: Eq:ConicSec:MostGeneralFormula

   Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0

::::

where the parameters $A,B,C$ are not all three equal to zero.

::::{prf:example}

The curve given by the equation  $x^2 + y^2 - 25 = 0$  is a circle with radius 5.

The equation  $x^2 - y - 2x + 5 = 0$  is a parabola with vertex ('top')  at  $(1, 4)$ and the line $x = 1$ as axis of symmetry.

::::

If the parameters  $D$ and $E$ in Equation {eq}`Eq:ConicSec:MostGeneralFormula` are zero, the equation

::::{math}
:label: Eq:ConicSec:CentralConic

   Ax^2 + Bxy + Cy^2 + F = 0

::::

is said to represent a **central conic**.  And when  $B = 0$ as well,

::::{math}
:label: Eq:ConicSec:StandardConic

   Ax^2 + Cy^2 + F = 0

::::

defines a central conic in **standard position**.  Such a conic is symmetric with respect to both coordinate axes.

If  all parameters $A,C,F$ in {eq}`Eq:ConicSec:StandardConic` are nonzero  the equation can be rewritten in one of the **standard forms**

$$
   (I) \, \dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1, \quad 
   (II) \, \dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = \pm 1, \quad a,b > 0
$$

In case $(I)$  the equation describes an ellipse if  $a \neq b$ and a circle if $a = b$.
<BR>
In case $(II)$  the resulting curve is a hyperbola, with the lines $y = \pm\dfrac{a}{b}x$
as asymptotes.  See {numref}`Figure %s <Fig:QuadForms:EllipseHyperbola>`.
<BR>
Both curves have the coordinates axes as axes of symmetry. In this context they are also called the **principal axes**.


:::{figure} Images/Fig-QuadForms-EllipseHyperbola.svg
:name: Fig:QuadForms:EllipseHyperbola

(Standard) Hyperbola and Ellipse
:::


To make the notation consistent with the quadratic forms in the previous subsection,  from now on we will use  $x_1, x_2, x_3$ instead of $x,y,z$.

If in {eq}`Eq:ConicSec:CentralConic` the parameter $B$ is not equal to zero, the principal axes can be found by diagionalization of the quadratic form

$$
  Ax_1^2 + Bx_1x_2 + Cx_2^2 = 
  \begin{bmatrix} x_1 & x_2 \end{bmatrix}\begin{bmatrix} A & \tfrac12B \\ \tfrac12B & C\end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}.
$$

The next proposition explains how.

::::{prf:proposition} 
:label: Prop:QuadForms:PrincipleAxesR2

Suppose the conic $\mathcal{C}$ is defined by the equation

$$
  ax_1^2 + 2bx_1x_2 + cx_2^2 = k, \,\,a,b,c\,\,\text{not all equal to zero}
  $$

Then the principal axis are the lines generated by the eigenvectors of the matrix

$$
  A = \begin{bmatrix} a & b \\ b & c \end{bmatrix}
$$


::::

The following examples illustrate proposition {prf:ref}`Prop:QuadForms:PrincipleAxesR2`.


::::{prf:example}
:label: Ex:QuadForms:PrinciplesAxes1

We consider the quadratic form

:::{math}
:label: Eq:QuadForms:ConicExample1

  x_1^2 - 4x_1x_2 + x_2^2 = 4.
:::

Since  $x_1^2 - 4x_1x_2 + x_2^2 = \begin{bmatrix} x_1 & x_2 \end{bmatrix}\begin{bmatrix} 1 & -2 \\ -2 & 1\end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$, 
<BR>
{prf:ref}`Prop:QuadForms:PrincipleAxesR2`  tells us we have to look for eigenvectors of the matrix

$$
  A = \begin{bmatrix} 1 & -2 \\ -2 & 1\end{bmatrix}.
$$

The usual computations yield the following eigenvalues and eigenvectors:

$$
  \lambda_1 = 3,\,\vect{v}_1 = \begin{bmatrix} 1 \\ -1\end{bmatrix},\quad
  \lambda_2 = -1,\,\vect{v}_2 = \begin{bmatrix} 1 \\ 1\end{bmatrix}.
$$

The eigenvectors are orthogonal, as they should, for a symmetric matrix, and we see
that $A$ can be orthogonally diagonalized as

$$
  A = QDQ^{-1} = QDQ^T, \quad Q = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ -1 & 1\end{bmatrix}, \,\,
  D = \begin{bmatrix} 3 & 0 \\ 0 & -1\end{bmatrix}.
$$

The substitution  $\vect{x} = Q\vect{y}$  yields

$$ 
  \vect{x}^T A \vect{x} = \vect{x}^T QDQ^T \vect{x} = \vect{y}^T D \vect{y} 
  = 3y_1^2 - y_2^2.
$$

So in the coordiantes $y_1$ and $y_2$ the equation becomes

$$
  3y_1^2 - y_2^2 = 4.
$$

From this we can already conclude that the curve defined by Equation {eq}`Eq:QuadForms:ConicExample1`  is a hyperbola. The principal axes are the lines given by

$$
   \mathcal{L}_1: \begin{bmatrix} x_1 \\ x_2\end{bmatrix} = c \begin{bmatrix} 1 \\ -1\end{bmatrix} \quad \text{and} \quad 
    \mathcal{L}_2: \begin{bmatrix} x_1 \\ x_2\end{bmatrix} = c \begin{bmatrix} 1 \\ 1\end{bmatrix}
$$

In the $y_1$-$y_2$-plane, the asymptotes are the lines

$$
  y_2 = \pm\sqrt{3} y_1, \,\, \text{or} \,\,\,
  \begin{bmatrix} y_1 \\ y_2\end{bmatrix} = c \begin{bmatrix} 1 \\ \pm 3\end{bmatrix}.
$$

Since

$$
    \begin{bmatrix} x_1 \\ x_2\end{bmatrix} = \dfrac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ -1 & 1\end{bmatrix}\begin{bmatrix} y_1 \\ y_2\end{bmatrix} =
     \begin{bmatrix} \cos\left(-\frac14\pi\right) & \sin\left(-\frac14\pi\right) \\ -\sin\left(-\frac14\pi\right) & \cos\left(-\frac14\pi\right)\end{bmatrix}\begin{bmatrix} y_1 \\ y_2\end{bmatrix}
$$

we find the asymptotes in the $x_1$-$x_2$-plane by rotating these lines over an angle $-\frac14\pi$.  We find the direction vectors of the asymptotes in the $x_1$-$x_2$-plane
as

$$
  \dfrac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ -1 & 1\end{bmatrix}\begin{bmatrix} 1 \\ 3\end{bmatrix} = \dfrac{1}{\sqrt{2}} \begin{bmatrix} 4 \\ 2\end{bmatrix},\,\,
  \,\,
  \dfrac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ -1 & 1\end{bmatrix}\begin{bmatrix} 1 \\ -3\end{bmatrix} = \dfrac{1}{\sqrt{2}} \begin{bmatrix} -2 \\ -4\end{bmatrix}.
$$

They can be simplified to the direction vectors  $ \begin{bmatrix} 2 \\ 1\end{bmatrix}$
and $\begin{bmatrix} 1 \\ 2\end{bmatrix}$. 

::::


::::{prf:example}
:label: Ex:QuadForms:PrinciplesAxes2

We consider the quadratic form

:::{math}
:label: Eq:QuadForms:ConicExample2

  3x_1^2 + 4x_1x_2 + 6x_2^2 = 36.
:::

Here we have

$$
  3x_1^2 + 4x_1x_2 + 6x_2^2 = \begin{bmatrix} x_1 & x_2 \end{bmatrix}\begin{bmatrix} 3 & 2 \\ 2 & 6\end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix},
$$

 so now we have to look for eigenvectors of the matrix

$$
  A = \begin{bmatrix} 3 & 2 \\ 2 & 6\end{bmatrix}.
$$

They are found to be  

$$
  \lambda_1 = 2,\,\vect{v}_1 = \begin{bmatrix} 1 \\ 2\end{bmatrix},\quad
  \lambda_2 = 7,\,\vect{v}_2 = \begin{bmatrix} -2 \\ 1\end{bmatrix}.
$$

We  orthogonally diagonalize $A$  as 

$$
  A = QDQ^{-1} = QDQ^T, \quad Q = \frac{1}{\sqrt{5}}\begin{bmatrix} 1 & -2 \\ 2 & 1\end{bmatrix}, \,\,
  D = \begin{bmatrix} 2 & 0 \\ 0 & 7\end{bmatrix}.
$$

The substitution  $\vect{x} = Q\vect{y}$  yields the quadratic form

$$ 
   2y_1^2 + 7y_2^2 = 36,
$$

or

$$ 
   \dfrac{y_1^2}{3^2} + \dfrac{y_2^2}{(6/\sqrt{7})^2} = 1,
$$


This is an ellipse with long axis $6$, the length of the line segment from  $(-3,0)$ to $(3,0)$, and  short axis  $\dfrac{12}{\sqrt{7}}$.

For the ellipse in the $x_1$-$x_2$-plane we find the principle axes

$$ 
  \begin{bmatrix} x_1 \\ x_2\end{bmatrix} = c\begin{bmatrix} 1 \\ 2\end{bmatrix} \quad \text{and}\quad \begin{bmatrix} x_1 \\ x_2\end{bmatrix} = c\begin{bmatrix} -2 \\ 1\end{bmatrix}.
$$

See Figure  {numref}`Fig:QuadForms:Ellipses`




:::{figure} Images/Fig-QuadForms-Ellipses(2).svg
:name: Fig:QuadForms:Ellipses

The two ellipses
:::


::::