(Sec:QuadraticForm)=

# Quadratic Forms

(Subsec:Terminology)=

## Introduction and Terminology

The simplest functions from $\R^n$ to $\R$ are linear functions

$$
   f(x_1,\ldots,x_n) = \sum_{i=1}^n a_ix_i +b \, =\, a_1x_2 + a_2x_2 + \ldots + a_nx_n + b.
$$

In short $f(\mathbf{x}) = \mathbf{a}^T\mathbf{x} + b$, for some vector $\mathbf{a}$ in $\R^n$ and some number $b$ in $\R$.

This is the common notion of linearity in calculus. To be linear in the linear algebra sense the constant term $b$ must be zero.

After that come the *quadratic functions*

::::{math}
:label: Eq:QuadForms:GeneralQuadForm

q(x_1,\ldots,x_n) = \sum_{i,j=1}^{n} a_{ij}x_ix_j + \sum_{i=1}^{n} b_ix_i + c,
::::

where all parameters $a_{ij}$, $b_i$ and $c$ are real numbers.

A quadratic function in the two variables $x_1$, $x_2$ thus becomes

$$
   q(x_1,x_2) = a_{11}x_1^2  + a_{12}x_1x_2 + a_{21}x_2x_1 + a_{22}x_2^2 + b_1x_1 + b_2x_2 + c,
$$

Note that this can be written as

$$
  q(x_1,x_2) = \begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + \begin{bmatrix} b_1 & b_2 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} + c.
$$

In general, a shorthand representation of Equation {eq}`Eq:QuadForms:GeneralQuadForm` becomes

$$
 q(\mathbf{x}) = \mathbf{x}^TA\mathbf{x} + \mathbf{b}^T\mathbf{x} + c,
$$

for an $n\times n$ matrix $A$, a vector $\vect{b}$ in $\R^n$, and a number $c$ in $\R$.

The part $\mathbf{x}^TA\mathbf{x}$ is called a **quadratic form**.

::::{prf:example}
:label: Ex:QuadForms:Diagonalize

For the matrix $A = \begin{bmatrix} 1 & 2 \\ 4 & 3 \end{bmatrix}$ the corresponding quadratic form is

$$
  \begin{array}{rcl}
  q(\vect{x}) =  \begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 4& 5 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
   &=& \begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} x_1 + 2x_2 \\ 4x_1+ 5x_2 \end{bmatrix} \\
   &=& x_1^2 + (2+4)x_1x_2 + 5x_2^2 \\
   &=& x_1^2 + 6x_1x_2 + 5x_2^2.
   \end{array}
$$

Note that the last expression does not uniquely determine the matrix. We can split the coefficient $6$ of the term $x_1x_2$ in a different way and will end up with a different matrix. If we distribute it evenly over $x_1x_2$ and $x_2x_1$ we get a _symmetric_ matrix.

$$
  \begin{array}{rcl}
  x_1^2 + 6x_1x_2 + 5x_2^2 &=& x_1^2 + (3+3)x_1x_2 + 5x_2^2 \\
   &=& x_1^2 + 3x_1x_2 + 3x_2x_1 + 5x_2^2 \\
   &=& x_1(x_1 + 3x_2) + x_2(3x_1 + 5x_2) \\
   &=& \begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} x_1 + 3x_2 \\ 3x_1+ 5x_2 \end{bmatrix}\\
  &=&\begin{bmatrix} x_1 & x_2 \end{bmatrix} \begin{bmatrix} 1 & 3 \\ 3 & 5 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}.
   \end{array}
$$

::::

The above example leads to the first proposition about quadratic forms.

::::{prf:proposition}
:label: Prop:QuadForms:SymmMatrixA
Every quadratic form $q(\mathbf{x})$ can be written uniquely as

$$
  q(\mathbf{x}) = \mathbf{x}^TA\mathbf{x}
$$

for a _symmetric_ matrix $A$.

This symmetric matrix $A$ is then called **the matrix of the quadratic form**.
::::

::::{prf:example}

We will find the symmetric matrix $A$ for the symmetric form

$$
    q(x_1,x_2,x_3) = x_1^2 + 2x_2^2 + 5 x_3^2  - 4 x_1x_2 + 6 x_2x_3.
$$

So we need a symmetric matrix $A = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ 
                                                     a_{12} & a_{22} & a_{23} \\
                                                     a_{13} & a_{23} & a_{33}
                                     \end{bmatrix}$.

From

$$

  \mathbf{x}^TA\mathbf{x} =  a_{11}x_1^2 + a_{22}x_2^2 + a_{33}x_3^2 + 2a_{12}x_1x_2 + 2a_{13}x_1x_3 + 2a_{23}x_2x_3
$$

we read off

$$
a_{11} = 1, \,  a_{22} = 2, \,  a_{33} = 5, \,\,\text{and}\,\,
 a_{12} = -2, \,  a_{13} = 0, \,  a_{23} = 3.
$$

So $A = \begin{bmatrix} 1 & -2 & 0 \\ 
                        -2 &  2 & 3 \\
                         0 &  3 & 5 
         \end{bmatrix}$.

::::

If we restrict ourselves to two variables,  we see that
the graph of a linear function $z = a_1x_1 + a_2x_2 + b$ is a plane.

:::{figure} Images/Fig-QuadForms-Plane1.svg
:name: Fig:QuadForms:Plane1
:class: dark-light

The plane $z = \frac13x_1 - x_2 +2$.
:::

The graph of a quadratic function is a curved surface.
{numref}`Figure %s <Fig:QuadForms:QuadSurface1>` and
{numref}`Figure %s <Fig:QuadForms:QuadSurface2>` show two of these quadratic surfaces.

:::{figure} Images/Fig-QuadForms-QuadSurface1.png
:name: Fig:QuadForms:QuadSurface1
:class: dark-light

The surface $z = -\frac13x_1^2 + \frac13x_2^2 + 2 $.
:::

:::{figure} Images/Fig-QuadForms-QuadSurface2.png
:name: Fig:QuadForms:QuadSurface2
:class: dark-light

The surface $z = -\frac12x_1^2 - \frac14x_2^2 + x_1 - x_2 + 2$.
:::

The shape of the surfaces is in most cases determined by the quadratic part $\vect{x}^TA\vect{x}$. The linear part is then only relevant for the position.

::::{prf:example}
:label: Es:QuadForms:Shift

Consider the quadratic surface described by

$$
   z = x_1^2 + 2x_1x_2 + 3 x_2^2.
$$

We will apply the shift

$$
\tilde{x}_1 = x_1-3,  \,\, \tilde{x}_2 = x_2 + 2,
$$

so

$$
 x_1 =  \tilde{x}_1+3, \,\,x_2 = \tilde{x}_2- 2.
$$

In the new variables $(\tilde{x}_1,\tilde{x}_2)$ we get

$$
   \begin{array}[t]{rcl} z &=&(\tilde{x}_1+3)^2 + 2(\tilde{x}_1+3)(\tilde{x}_2- 2) + 3 (\tilde{x}_2- 2)^2  \\
   &=& \tilde{x}_1^2 + 2\tilde{x}_1\tilde{x}_2 + 3 \tilde{x}_2^2 +2\tilde{x}_1-6\tilde{x}_2 + 9.
   \end{array}
$$

Note that the quadratic parts are the same,

$$
x_1^2 + 2x_1x_2 - 3 x_2^2 \quad \text{versus} \quad \tilde{x}_1^2 + 2\tilde{x}_1\tilde{x}_2 - 3 \tilde{x}_2^2.
$$

::::

::::{prf:example}

The surfaces defined by

$$
   \mathcal{S}_1: z = 2x_1^2 - 2x_1x_2 + x_2^2  \quad \text{and} \quad
   \mathcal{S}_2: z = 2x_1^2 - 2x_1x_2 + x_2^2 + 8x - 6y + 4
$$

are shifted versions of the same surface. Namely,

$$
   2x_1^2 - 2x_1x_2 + x_2^2 + 8x - 6y + 4 = 2(x_1+1)^2 - 2(x_1+1)(x_2-2) + (x_2-2)^2 - 6.
$$

Thus $\mathcal{S}_2$ is also described by

$$
  z + 6 = 2(x_1+1)^2 - 2(x_1+1)(x_2-2) + (x_2-2)^2.
$$

This means that if $\mathcal{S}_1$ is translated over the vector
$\left[\begin{array}{c} -1 \\ 2 \\ -6 \end{array}\right]$ it becomes the surface $\mathcal{S}_2$.
::::

For the rest of the section we will therefore only look at the quadratic part $\vect{x}^TA\vect{x}$.

One of the simplest quadratic forms results when we take $A = I = I_n$, the identity matrix.
Then we have

$$
  q(\vect{x}) = \vect{x}^TI_n\vect{x} = \vect{x}^T\vect{x} =x_1^2 + x_2^2 + \ldots + x_n^2 = \vect{x}\ip\vect{x}.
$$

For this quadratic form, it is clear that it will only take on nonnegative values. And that

$$
   q(\vect{x}) = 0   \quad \iff \quad  \vect{x}=\vect{0}.
$$

Such a quadratic form is called _positive definite_.
In the next subsection we will learn how to find out whether an arbitrary quadratic form has this property.

(Subsec:SignOfQuadForm)=

## Diagonalization of quadratic forms

Let us first consider an example, to get some feeling for what is going on.

::::{prf:example}
:label: Ex:QuadForms:CompleteSquares

Consider the quadratic form

$$
   q(x_1,x_2) = x_1^2 + 4x_1x_2 + 3x_2^2 =
   \begin{bmatrix}x_1 & x_2 \end{bmatrix} \begin{bmatrix}1 & 2 \\ 2 & 3 \end{bmatrix}\begin{bmatrix}x_1 \\ x_2 \end{bmatrix} = \vect{x}^TA\vect{x} .
$$

At first sight you might think that this quadratic form only takes on nonnegative values.
One way to show that this is not actually true is by _completing squares_.

$$
  x_1^2 + 4x_1x_2 + 3x_2^2 = (x_1 + 2x_2)^2 - 4x_2^2 + 3x_2^2 = (x_1 + 2x_2)^2 - x_2^2.
$$

For the last expression, that does not contain a _cross term_, we can see how we can get a negative outcome. We can make the first term equal to $0$ by taking $x_2 = 1$ and $x_1 = -2$, and then have

$$
  q(x_1,x_2) = q(-2,1) = (-2+2\cdot1)^2 - 1^2 = -1 < 0.
$$

::::

One way to describe in a more abstract/general way what we did in {prf:ref}`Ex:QuadForms:CompleteSquares` is the following.
We can introduce new variables $y_1, y_2$ via the _substitution_

$$
   \left\{ \begin{array}{rr}
              y_1 =& x_1 + 2x_2 \\
              y_2 =& x_2.
            \end{array}
      \right.
$$

For short,

$$
      \vect{y} = \left[\begin{array}{c} y_1  \\ y_2 \end{array}\right] =  \left[\begin{array}{cc} 1 & 2  \\ 0 & 1 \end{array}\right]\left[\begin{array}{c} x_1  \\ x_2 \end{array}\right] = M\vect{x}.
$$

Then in terms of the new variables the quadratic form becomes

$$
  q(\vect{x}) = (x_1 + 2x_2)^2 - x_2^2 = y_1^2 - y_2^2 =
  \begin{bmatrix}y_1 & y_2 \end{bmatrix} \begin{bmatrix}1  & 0 \\ 0 &-1 \end{bmatrix}\begin{bmatrix}y_1 \\ y_2 \end{bmatrix} = \vect{y}^TD\vect{y}.
$$

<BR>

Actually, it proves slightly advantageous to express the substitution as
$\vect{x} = P\vect{y}$ for an invertible matrix $P$. We then have the following proposition.

::::{prf:proposition} Quadratic form under a substitution
:label: Prop:QuadForms:Substitution

The substitution $\vect{x} = P\vect{y}$ brings the quadratic form

$$
  q(\vect{x}) = \vect{x}^TA\vect{x}
$$

over to

$$
  \tilde{q}(\vect{y}) = \vect{y}^TP^TAP\vect{y}.
$$

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:QuadForms:Substitution`
:class: tudproof

If we put $\vect{x} = P\vect{y}$ we get

$$
    q(\vect{x}) = \vect{x}^TA\vect{x} =
      (P\vect{y})^TA(P\vect{y}) = \vect{y}^TP^T A P \vect{y}.
$$

So in terms of $\vect{y}$ we have the quadratic form

$$
   \tilde{q}(\vect{y}) = \vect{y}^T \tilde{A} \vect{y}
$$

where

$$
   \tilde{A} = P^T A P.
$$

::::

::::{prf:example}
:label: Ex:QuadForms:CompleteSquaresCtd

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
  P^TAP &=&  \begin{bmatrix} 1 & -2  \\ 0 & 1 \end{bmatrix}^T\begin{bmatrix} 1 & 2  \\ 2 & 3 \end{bmatrix}\begin{bmatrix} 1 & -2  \\ 0 & 1 \end{bmatrix} \\
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

The technique of completing the squares is one way to 'diagonalize' a quadratic form. It may be turned into an algorithm that also works for quadratic forms in $n$ variables, but
we will not pursue that track. There is a route that is more in line with the properties of symmetric matrices.

Suppose $A$ is a symmetric matrix. We have seen (cf. {prf:ref}`Thm:SymmetricMat:OrthogDiag`) that it can be written as

$$
A = QDQ^{-1}
$$

for an orthogonal matrix $Q$. The diagonal matrix $D$ has the eigenvalues of $A$ on its diagonal.

Since $Q$ is an orthogonal matrix, we have

$$
   A = QDQ^{-1} = QDQ^T.
$$

If we compare this to {prf:ref}`Prop:QuadForms:Substitution` the following proposition results.

::::{prf:proposition}
:label: Prop:QuadForms:Diagonalize

Suppose $q(\vect{x})$ is a quadratic form with matrix $A$, i.e.,

$$
    q(\vect{x}) = \vect{x}^TA\vect{x}.
$$

Let $Q$ be an orthogonal matrix diagonalizing $A$. That is,  $A = QDQ^{-1}$. <BR>
Applying the substitution $\vect{x} = Q\vect{y}$ then yields the quadratic form

$$
  \vect{y}^TD\vect{y} = \lambda_1y_1^2 + \lambda_2y_2^2 + \ldots + \lambda_ny_n^2,
$$

where $\lambda_1, \ldots, \lambda_n$ are the _eigenvalues_ of the matrix $A$.
::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:QuadForms:Diagonalize`
:class: tudproof

If we make the substitution $\vect{x} = Q\vect{y}$ we find that

$$
  \vect{x}^TA\vect{x} = (Q\vect{y})^TQDQ^{-1}(Q\vect{y}) = \vect{y}^TQ^TQD
  Q^{-1}Q\vect{y} = \vect{y}^TD\vect{y}.
$$

The last expression is indeed of the form

$$
  \vect{y}^T\begin{bmatrix}
                 \lambda_1 & 0 & \ldots & 0 \\
                 0 & \lambda_2 & \ldots & 0 \\
                 \vdots & \vdots & \ddots & \vdots \\
                 0 & 0 & \ldots & 0
            \end{bmatrix}\vect{y} =
            \lambda_1y_1^2 + \lambda_2y_2^2 + \ldots + \lambda_ny_n^2,
$$

where $\lambda_1,\lambda_2, \ldots, \lambda_n$ are the eigenvalues of $A$.

::::

Let us see how the construction of {prf:ref}`Prop:QuadForms:Diagonalize` works out in an earlier example.

::::{prf:example}

Consider again the matrix $A = \left[\begin{array}{cc} 1 & 2  \\ 2 & 3 \end{array}\right]$ of {prf:ref}`Ex:QuadForms:CompleteSquaresCtd`.

Its characteristic polynomial is given by

$$
  p_A(\lambda) = (1-\lambda)(3-\lambda)-4 = \lambda^2 - 4\lambda - 1.
$$

The eigenvalues are

$$
   \lambda_1 = 2 + \sqrt{5}, \quad \lambda_2 = 2 + \sqrt{5}.
$$

So if we take $Q = \begin{bmatrix} \vect{q}_1 & \vect{q}_2 \end{bmatrix}$, where
$\vect{q}_1$ and $\vect{q}_2$ are corresponding eigenvectors of unit length, we find that the substitution $\vect{x} = Q\vect{y}$ leads to

$$
  \vect{x}^TA\vect{x}  \,\stackrel{\scriptsize \vect{x} = Q\vect{y}}{\longrightarrow}\,
  \vect{y}^TD\vect{y} = (2 + \sqrt{5})y_1^2 - (2 - \sqrt{5})y_2^2.
$$

Since $(2 + \sqrt{5})> 0$ and $(2 - \sqrt{5})<2-2=0$ we may again conclude that the quadratic form takes on both positive and negative values.

::::

::::{prf:remark}
In {prf:ref}`Ex:QuadForms:CompleteSquaresCtd` and {prf:ref}`Ex:QuadForms:Diagonalize` we applied two different substitutions to the same quadratic form with the matrix $A = \left[\begin{array}{cc} 1 & 2  \\ 2 & 3 \end{array}\right]$.

They led to the two different quadratic forms

$$
  \vect{y}^TD_1\vect{y} = \vect{y}^T\begin{bmatrix}1 & 0\\ 0 & -1 \end{bmatrix}\vect{y} \quad \text{and} \quad
  \vect{y}^TD_2\vect{y} = \vect{y}^T\begin{bmatrix}2 + \sqrt{5} & 0\\ 0 & 2 - \sqrt{5}\end{bmatrix}\vect{y}.
$$

The diagonal matrices do not seem to have much in common. However, they do.

It can be shown that if for a symmetric $n\times n$ matrix $A$ it holds that

$$
  P_1^TAP_1 = D_1 \quad \text{and} \quad P_2^TAP_2 = D_2,
$$

for two invertible matrices $P_1$, $P_2$,
then the _signs_ of the values on the diagonals of $D_1$ and $D_2$ match in the following sense: <BR> if $p_1$, $p_2$ denote the numbers of positive diagonal elements of $D_1, D_2$, and $n_i$ are the numbers of negative diagonal elements, then

$$
  p_1 = p_2 \quad \text{and} \quad n_1 = n_2.
$$

It follows that also the numbers of zeros on the diagonal, $n - p_i - n_i$, $i = 1,2$, must be equal for the two matrices.

In the two examples we see that $p_1 = p_2 = 1$ and also $n_1 = n_2 = 1$, in accordance with the statement.

The property is known as _Sylvester's Law of Inertia_.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5a3d937b-6ecb-4fe8-b805-424af7e7ac55?id=90077
:label: grasple_exercise_8_2_T1
:dropdown:
:description: To garner some evidence for Sylvester's Law of Inertia.

::::


The following proposition is  a direct consequence of the diagonalization  ({prf:ref}`Prop:QuadForms:Diagonalize`).  

::::{prf:proposition}
:label:  Prop:QuadForms:MaximumxTAx

Let  $q(x) = \vect{x}^TA\vect{x}$ be the quadratic form with matrix $A$ and suppose that $A$ has the (ordered) eigenvalues
$\lambda_1 \geq \lambda_2 \geq \ldots \geq \lambda_n$.  Then the maximum and the minimum value attained by   $q(\vect{x})$  under the constraint  $\norm{\vect{x}} = 1$  are $\lambda_1$ and $\lambda_n$.

::::

The proof contains the same type of reasoning as the proof of {prf:ref}`Prop:SymmetricMat:Max||Ax||`.

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:QuadForms:MaximumxTAx`
:class: tudproof, dropdown

Suppose that   $\vect{u}_1, \vect{u}_2,\ldots,\vect{u}_n$  is an orthonormal basis of eigenvectors for $A$ for the eigenvalues  $\lambda_1 \geq \ldots \geq \lambda_n$.


First of all

$$
  q(\vect{u}_1) = \vect{u}_1^TA\vect{u}_1 = \vect{u}_1^T(A\vect{u}_1) =  
  \vect{u}_1^T(\lambda_1\vect{u}_1)  = \lambda_1\vect{u}_1^T\vect{u}_1 = \lambda_1. 
$$

Likewise $q(\vect{u}_n) =  \lambda_n$, so $q(\vect{x})$  does take on the values  $\lambda_1$ and  $\lambda_n$.

Next, for an arbitrary unit vector $\vect{x}$, which can always be written as 

$$
  c_1\vect{u}_1 +    c_2\vect{u}_2 + \ldots +  c_n\vect{u}_n, \quad \text{with} \quad 
  c_1^2 + c_2^2 + \ldots + c_n^2 = 1 
$$

(cf. proof of {prf:ref}`Prop:SymmetricMat:Max||Ax||`), we deduce that

$$
\begin{array}{rcl}
  \vect{x}^TA\vect{x} &=& 
  (c_1\vect{u}_1 +  \ldots +  c_n\vect{u}_n)^T(c_1\lambda_1\vect{u}_1 +  \ldots +  c_n\lambda_n\vect{u}_n) \\
  &=& 
   c_1^2\lambda_1\vect{u}_1^T\vect{u}_1 + \cdots + c_n^2\lambda_n\vect{u}_n^T\vect{u}_n \\
   &=&
   c_1^2\lambda_1 + \cdots + c_n^2\lambda_n.
   \end{array}
$$

All cross terms $\vect{u}_i^T\vect{u}_j$  with $i\neq j$ drop out since $\vect{u}_i\ip\vect{u}_j=0$, for $i\neq j$,  and $\vect{u}_i^T\vect{u}_i = 1$ by the assumption that the vectors $\mathbf{u}_i$ are unit vectors.

Now, invoking  $\lambda_1 \geq \lambda_2 \geq \ldots  \geq \lambda_n$ and $c_1^2 + c_2^2 + \ldots +c_n^2 = 1$,  we see that

$$ 
  \begin{array}{rcl}    
     \lambda_n = \left(c_1^2 +c_2^2 +\cdots + c_n^2\right)\lambda_n 
     &=&
     c_1^2\lambda_n +c_2^2\lambda_n +\cdots + c_n^2\lambda_n \\
     &\leq&  c_1^2\lambda_1 +c_2^2\lambda_2 +\cdots + c_n^2\lambda_n,
     \end{array}
$$

and also  

$$ 
  \lambda_1 \geq c_1^2\lambda_1 +c_2^2\lambda_2 +\cdots + c_n^2\lambda_n,
$$

so we may conclude that indeed

$$
  \lambda_n \,\leq\, c_1^2\lambda_1 +c_2^2\lambda_2 +\cdots + c_n^2\lambda_n \,\leq\, \lambda_1,
$$

where the expression in the middle is equal to our  $\vect{x}^T A \vect{x} = q(\vect{x})$. 

::::



(Subsec:PosDefMatrices)=

## Positive definite matrices

Let's start with a list of definitions.

::::{prf:definition} Classification of Quadratic Forms
:label: Dfn:QuadForms:DefiniteMatrix

Let $A$ be a symmetric matrix and $q_A(\vect{x}) = \vect{x}^TA\vect{x}$ the corresponding quadratic form.

<ul>

<li>

$q_A$ is called **positive definite** if $q_A(\vect{x}) > 0$ for all $\vect{x} \neq \vect{0}$.

</li>

<li>

$q_A$ is called **positive semi-definite** if $q_A(\vect{x}) \geq 0$ for all $\vect{x} $.

</li>

<li>

$q_A$ is called **negative definite** if $q_A(\vect{x}) < 0$ for all $\vect{x} \neq \vect{0}$.

</li>

<li>

$q_A$ is called **negative semi-definite** if $q_A(\vect{x}) \leq 0$ for all $\vect{x} $.

</li>

</ul>

If none of the above applies, then $q_A$ is called an **indefinite** quadratic form.

The same classification is used for symmetric matrices. E.g., $A$ is a **positive definite matrix** if the corresponding quadratic form is positive definite.

::::

Note that every quadratic form $\vect{x}^TA\vect{x}$ gets the value $0$ when $\vect{x}$ is the zero vector. That is the reason we exclude the zero vector in the definition of positive/negative definite.

The classification of a quadratic form follows immediately from the eigenvalues of its matrix.

::::{prf:theorem}
:label: Thm:QuadForms:Classification

Suppose $q_A(\vect{x}) = \vect{x}^TA\vect{x}$ for the symmetric $n \times n$ matrix $A$.
Let $\lambda_1, \ldots, \lambda_n$ be the complete set of (real) eigenvalues of $A$

Then

<ul>

<li>

$q_A$ is **positive definite** if and only if all eigenvalues are positive.

</li>

<li>

$q_A$ is **positive semi-definite** if and only if all eigenvalues are nonnegative.

</li>

<li>

$q_A$ is **negative definite** if and only if all eigenvalues are negative.

</li>

<li>

$q_A$ is **negative semi-definite** if and only if all eigenvalues are nonpositive.

</li>

</ul>

And lastly

<ul>

<li>

$q_A$ is **indefinite** if at least one eigenvalue is positive and at least one eigenvalue is negative.

</li>
</ul>

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Thm:QuadForms:Classification`
:class: tudproof

This immediately follows from {prf:ref}`Prop:QuadForms:Diagonalize`. If we make the substitution $\vect{x} = Q\vect{y}$ with the matrix $Q$ of the orthogonal diagonalization, i.e.,

$$
  A = QDQ^{-1} = QDQ^T, \quad
  D = \left[\begin{array}{cccc}
  \lambda_1 & 0 & \ldots & 0  \\
  0 & \lambda_2 & \ldots & 0 \\
  \vdots & \vdots & \ddots &\vdots\\
  0 & 0 & \ldots & \lambda_n
  \end{array}\right],
$$

the quadratic form transforms to

$$
  \tilde{q}(\vect{y}) = \vect{y}^TD\vect{y} = \lambda_1y_1^2 + \ldots + \lambda_ny_n^2.
$$

Let us consider the case where all eigenvalues $\lambda_i$ are _positive_.
Then the expression for $\tilde{q}(\vect{y})$ is positive for all $\vect{y} \neq \vect{0}$. It remains to show that then also $q(\vect{x}) > 0$ for all vectors $\vect{x}\neq \vect{0}$.

Since $Q$ is an orthogonal matrix it is also an invertible matrix. So any _nonzero_ vector $\vect{x}$ can be written as

$$
  \vect{x} = Q\vect{y}
$$

for a (unique) _nonzero_ vector $\vect{y}$.

As a consequence, for any nonzero vector $\vect{x}$ we have

$$
   \vect{x}^TA\vect{x} = (Q\vect{y})^TA(Q\vect{y}) =
   \vect{y}^TQ^TAQ\vect{y} = \vect{y}^TD\vect{y} > 0.
$$

Likewise the other possibilities of the signs of the eigenvalues may be checked.

::::

::::{exercise}
:label: Exc:QuadForms:CheckTheorem

Verify the validity of the second statement made in {prf:ref}`Thm:QuadForms:Classification`.

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

With {prf:ref}`Thm:QuadForms:Classification` in mind, we can conclude that the quadratic form is positive semi-definite but not positive definite.

::::

::::{exercise}  
:label: Exc:QuadForms:CompleteSquares2

This exercise nicely recapitulates the ideas of the section. There is a cameo of the concept of completing the square, but that is of minor importance.

Show that the quadratic from in {prf:ref}`Ex:QuadForms:CompleteSquares2` can be rewritten
as follows

:::{math}
:label: Eq:QuadForms:CompleteSquares2

q(x_1,x_2,x_3) = 2(x_1 - \tfrac12x_2 - \tfrac12x_3)^2 + \tfrac12(x_2 - x_3)^2.

:::

<ol type = "i">

<li>

What is the corresponding transformation $\vect{y} = P\vect{x}$ that brings the quadratic form in diagonal form $\vect{y}^TD_2\vect{y}$, and what is the diagonal matrix $D_2$?

</li>

<li>

By inspection of $D_2$ find the classification of $q$.

</li>

<li>

By inspection of Equation {eq}`Eq:QuadForms:CompleteSquares2`, find a nonzero vector
$\vect{x}$ for which $q(\vect{x}) = 0$.

</li>

<li>

Check that the vector you found in iii. is an eigenvector of the matrix of the quadratic form, i.e., $A = \left[\begin{array}{cc} 2 & -1 & -1  \\ -1 & 1 & 0 \\ -1 & 0 & 1 \end{array}\right]$.

</li>

</ol>

::::

(Subsec:ConicSections)=

## Conic Sections

A _conic section_ or _conic_ is a curve that results when a circular cone is intersected with a plane.  
{numref}`Figure %s <Fig:QuadForms:ConeWithPlanes>` shows the different shapes when the plane is *not* going through the apex.

:::{figure} Images/Fig-QuadForms-ConicSections.png
:name: Fig:QuadForms:ConeWithPlanes
:class: dark-light

Intersections of a cone with several planes (not going through the apex).

:::

 The resulting curve is then either a _hyperbola_, a _parabola_ or an _ellipse_, with as special ellipse the _circle_. If the plane does go through the apex of the cone the conic section is called **degenerate**.

::::{exercise}

Describe the (three) possible degenerate forms of conic sections. That is, what are the three different forms that result when a cone is intersected with a plane that goes through the apex?

::::

In the plane all _non-degenerate_ conic sections may be described by a quadratic equation

::::{math}
:label: Eq:ConicSec:MostGeneralFormula

ax_1^2 + b x_1x_2 + cx_2^2 + dx_1 + ex_2 + f = 0,

::::

where both the parameter $f$ and at least one of the parameters $a,b,c$ are not equal to zero.  
% When $f$ is equal to zero the conic section is sometimes called _degenerate_.

::::{prf:example}

The curve given by the equation $x_1^2 + x_2^2 - 25 = 0$ is a circle with radius 5.

The equation $x_1^2 - x_2 - 2x_1 + 5 = 0$ gives a parabola with vertex ('top') at $(1, 4)$ and the line $x_1 = 1$ as axis of symmetry.

::::

If the parameters $d$ and $e$ in Equation {eq}`Eq:ConicSec:MostGeneralFormula` are zero, the equation

::::{math}
:label: Eq:ConicSec:CentralConic

ax_1^2 + bx_1x_2 + cx_2^2 + f = 0

::::

is said to represent a **central conic**. &nbsp; When $b = 0$ as well,

::::{math}
:label: Eq:ConicSec:StandardConic

ax_1^2 + cx_2^2 + f = 0

::::

defines a central conic in **standard position**. Such a conic is symmetric with respect to both coordinate axes.

If all parameters $a,c,f$ in {eq}`Eq:ConicSec:StandardConic` are nonzero the equation can be rewritten in one of the two **standard forms**

::::{math}
:label: Eq:QuadForms:StandardForms

(I) \,\, \dfrac{x_1^2}{r_1^2} + \dfrac{x_2^2}{r_2^2} = 1, \quad\quad
(II) \,\, \dfrac{x_1^2}{r_1^2} - \dfrac{x_2^2}{r_2^2} = \pm 1,
::::

where we may assume that $ r_1,r_2 > 0$.

In case $(I)$ the equation describes an ellipse if $r_1 \neq r_2$ and a circle if $r_1 = r_2$.
<BR>
In case $(II)$ the resulting curve is a hyperbola, with the lines $x_2 = \pm\dfrac{r_2}{r_1}x_1$
as asymptotes.
<BR>
Both curves have the coordinates axes as axes of symmetry. In this context they are also called the **principal axes**. See {numref}`Figure %s <Fig:QuadForms:EllipseHyperbola>`.

:::{figure} Images/Fig-QuadForms-EllipseHyperbola.svg
:name: Fig:QuadForms:EllipseHyperbola
:class: dark-light

(Standard) Hyperbola and Ellipse.
:::

::::{exercise}
:label: Exc:QuadForms:DegenerateStandardForm

What happens if in Equation {eq}`Eq:ConicSec:CentralConic` the coefficient $f$ is equal to zero? <BR>
(There are actually three cases to consider!)

::::

::::{prf:example}
:label: Ex:QuadForms:StandardForm

The equation

$$
   4x_1^2 + 9x_2^2 - 25 = 0
$$

can be rewritten as

$$
   \dfrac{4x_1^2}{25} + \dfrac{9x_2^2}{25} = 1,
$$

and a bit further to the standard form

$$
   \dfrac{x_1^2}{(5/2)^2} + \dfrac{x_2^2}{(5/3)^2} = 1.
$$

The corresponding curve is an ellipse with the coordinate axes as principal axes and
with $-5/2 \leq x_1 \leq 5/2$ and $-5/3 \leq x_2 \leq 5/3$.

Likewise

$$
   4x_1^2 - x_2^2 + 9 = 0  \quad \iff \quad    \dfrac{x_1^2}{(3/2)^2} -  \dfrac{x_2^2}{3^2}  = -1.
$$

When rewritten in the form

$$
   x_2 = \pm \sqrt{9 + 4x_1^2} = \pm2x_1\sqrt{\dfrac{9}{4x_1^2} + 1}
$$

it is seen that the lines $x_2 = \pm 2x_1$ are asymptotes.
Namely, if $x_1 \to \pm \infty$, then

$$
   \sqrt{\dfrac{9}{4x_1^2} + 1} \,\to\, \sqrt{0+1} = 1.
$$

::::

If in {eq}`Eq:ConicSec:CentralConic` the parameter $b$ is not equal to zero, the principal axes can be found by diagonalization of the quadratic form

$$
  ax_1^2 + bx_1x_2 + cx_2^2 =
  \begin{bmatrix} x_1 & x_2 \end{bmatrix}\begin{bmatrix} a & \tfrac12b \\ \tfrac12b & c\end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}.
$$

The next proposition explains how. <BR  >
For notational convenience we denote the coefficient in the cross term as $2b$.

::::{prf:proposition}
:label: Prop:QuadForms:PrincipleAxesR2

Suppose the conic $\mathcal{C}$ is defined by the equation

$$
  ax_1^2 + 2bx_1x_2 + cx_2^2 = k,
$$

where $a,b,c$ are not all equal to zero, and $k \neq 0$.

Then the principal axes are the lines generated by the eigenvectors of the matrix

$$
  A = \begin{bmatrix} a & b \\ b & c \end{bmatrix}.
$$

::::

We will not give a proof of {prf:ref}`Prop:QuadForms:PrincipleAxesR2`, but instead we will give two 
illustrative examples.

::::{prf:example}
:label: Ex:QuadForms:PrinciplesAxes1

We consider the quadratic form

:::{math}
:label: Eq:QuadForms:ConicExample1

x_1^2 - 4x_1x_2 + x_2^2 = 4.
:::

Since

$$
 x_1^2 - 4x_1x_2 + x_2^2 = \begin{bmatrix} x_1 & x_2 \end{bmatrix}\begin{bmatrix} 1 & -2 \\ -2 & 1\end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix},
$$

{prf:ref}`Prop:QuadForms:PrincipleAxesR2` tells us we have to look for eigenvectors of the matrix

$$
  A = \begin{bmatrix} 1 & -2 \\ -2 & 1\end{bmatrix}.
$$

The usual computations yield the following eigenvalues and eigenvectors:

$$
  \lambda_1 = 3,\,\vect{v}_1 = \begin{bmatrix} 1 \\ -1\end{bmatrix},\quad
  \lambda_2 = -1,\,\vect{v}_2 = \begin{bmatrix} 1 \\ 1\end{bmatrix}.
$$

The eigenvectors are orthogonal, as they should, for a symmetric matrix. We see
that $A$ can be orthogonally diagonalized as

$$
  A = QDQ^{-1} = QDQ^T, \quad Q = \frac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ -1 & 1\end{bmatrix}, \,\,
  D = \begin{bmatrix} 3 & 0 \\ 0 & -1\end{bmatrix}.
$$

The substitution $\vect{x} = Q\vect{y}$ yields

$$
  \vect{x}^T A \vect{x} = \vect{y}^T Q^TAQ \vect{y} = \vect{y}^T D \vect{y}
  = 3y_1^2 - y_2^2.
$$

So in the coordinates $y_1$ and $y_2$ the equation becomes

$$
  3y_1^2 - y_2^2 = 4.
$$

From this we can already conclude that the curve defined by Equation {eq}`Eq:QuadForms:ConicExample1` is a hyperbola. The principal axes in the $x_1$-$x_2$-plane are the lines given by

$$
   \mathcal{L}_1: \begin{bmatrix} x_1 \\ x_2\end{bmatrix} = c \begin{bmatrix} 1 \\ -1\end{bmatrix} \quad \text{and} \quad
    \mathcal{L}_2: \begin{bmatrix} x_1 \\ x_2\end{bmatrix} = c \begin{bmatrix} 1 \\ 1\end{bmatrix}
$$

The asymptotes in the coordinates $y_1, y_2$ are the lines

$$
  y_2 = \pm\sqrt{3} y_1, \,\, \text{or} \,\,\,
  \begin{bmatrix} y_1 \\ y_2\end{bmatrix} = c \begin{bmatrix} 1 \\ \pm \sqrt{3}\end{bmatrix}.
$$

Since

$$
    \begin{bmatrix} x_1 \\ x_2\end{bmatrix} = \dfrac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ -1 & 1\end{bmatrix}\begin{bmatrix} y_1 \\ y_2\end{bmatrix} =
     \begin{bmatrix} \cos\left(-\frac14\pi\right) & -\sin\left(-\frac14\pi\right) \\ \sin\left(-\frac14\pi\right) & \cos\left(-\frac14\pi\right)\end{bmatrix}\begin{bmatrix} y_1 \\ y_2\end{bmatrix}
$$

we find the asymptotes in the $x_1$-$x_2$-plane by rotating the lines
$y_2 = \pm\sqrt{3}y_1$ over an angle $-\frac14\pi$. This leads to the direction vectors of the asymptotes in the $x_1$-$x_2$-plane
as

$$
  \dfrac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ -1 & 1\end{bmatrix}\begin{bmatrix} 1 \\ 3\end{bmatrix} = \dfrac{1}{\sqrt{2}} \begin{bmatrix} 4 \\ 2\end{bmatrix},\,\,
  \,\,
  \dfrac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ -1 & 1\end{bmatrix}\begin{bmatrix} 1 \\ -3\end{bmatrix} = \dfrac{1}{\sqrt{2}} \begin{bmatrix} -2 \\ -4\end{bmatrix}.
$$

They can be simplified to the direction vectors $ \begin{bmatrix} 2 \\ 1\end{bmatrix}$
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

so now we have to look for eigenvalues and eigenvectors of the matrix

$$
  A = \begin{bmatrix} 3 & 2 \\ 2 & 6\end{bmatrix}.
$$

They are found to be

$$
  \lambda_1 = 2,\,\vect{v}_1 = \begin{bmatrix} 2 \\ -1\end{bmatrix},\quad
  \lambda_2 = 7,\,\vect{v}_2 = \begin{bmatrix} 1 \\ 2\end{bmatrix}.
$$

We orthogonally diagonalize $A$ as

$$
  A = QDQ^{-1} = QDQ^T, \quad Q = \frac{1}{\sqrt{5}}\begin{bmatrix} 2 & 1 \\ -1 & 2\end{bmatrix}, \,\,
  D = \begin{bmatrix} 2 & 0 \\ 0 & 7\end{bmatrix}.
$$

The substitution $\vect{x} = Q\vect{y}$ yields the quadratic form

$$
   2y_1^2 + 7y_2^2 = 36,
$$

or

$$
   \dfrac{y_1^2}{(3\sqrt{2})^2} + \dfrac{y_2^2}{(6/\sqrt{7})^2} = 1.
$$

This is an ellipse in the $y_1$-$y_2$-plane with long axis $6\sqrt{2}$, the length of the line segment from $(-3\sqrt{2},0)$ to $(3\sqrt{2},0)$, and short axis $\dfrac{12}{\sqrt{7}}$.

For the ellipse in the $x_1$-$x_2$-plane we find the principal axes

$$
  \begin{bmatrix} x_1 \\ x_2\end{bmatrix} = c\vect{v}_1 = c\begin{bmatrix} 2 \\ -1\end{bmatrix} \quad \text{and}\quad \begin{bmatrix} x_1 \\ x_2\end{bmatrix} = c\vect{v}_2 = c\begin{bmatrix} 1 \\ 2\end{bmatrix}.
$$

See Figure {numref}`Fig:QuadForms:Ellipses`

:::{figure} Images/Fig-QuadForms-Ellipses(2).svg
:name: Fig:QuadForms:Ellipses
:class: dark-light

The  ellipse with its principal axes.
:::

::::


## Grasple Exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b0668dff-a174-447b-8008-09b242a804fb?id=87448
:label: grasple_exercise_8_2_1
:dropdown:
:description: To write down the matrix of a quadratic form in three variables.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/eaec14bd-fe7a-4c7a-a269-68e1d369bc2b?id=90207
:label: grasple_exercise_8_2_2
:dropdown:
:description: To write down the matrix of a quadratic form in three variables.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7044809f-28ca-4caf-b3fc-139010112ca1?id=90052
:label: grasple_exercise_8_2_3
:dropdown:
:description:  To perform a change of variables for a quadratic form $\vect{x}^TA\vect{x}$ in two variables.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b71d8b9f-a3e8-48f6-b236-58f85a4818a6?id=90997
:label: grasple_exercise_8_2_4
:dropdown:
:description: To classify a 3x3 matrix of which the characteristic polynomial is given.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f0f9e677-eb21-4f84-9850-039b24ee0999?id=93112  
:label: grasple_exercise_8_2_5
:dropdown:
:description: To classify a quadratic form in two variables.


::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f4657e73-219d-4ac9-bf17-81b240ddac96?id=93113
:label: grasple_exercise_8_2_6
:dropdown:
:description: To classify a quadratic form in two variables.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/21ad829b-77f5-4e14-9808-4fbbb901c9b4?id=93119
:label: grasple_exercise_8_2_7
:dropdown:
:description: To classify two quadratic forms in two variables. 

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/03704333-e9db-46f0-b292-eb235aee6b22?id=91025
:label: grasple_exercise_8_2_8
:dropdown:
:description: For which value of a parameter $\beta$ is a quadratic form in two variables indefinite?

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8b851997-932f-4ee6-8dfd-785bd7908e1c?id=91091
:label: grasple_exercise_8_2_9
:dropdown:
:description: To describe three central conic sections geometrically. 
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7c47dc31-b7d8-409e-9334-8a5de188c928?id=91912
:label: grasple_exercise_8_2_10
:dropdown:
:description: Natural sequel to previous exercise.

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ee9c377f-5150-4264-8d3e-1150c482fd7f?id=93116
:label: grasple_exercise_8_2_11
:dropdown:
:description: For which parameter $a$ is a conic section $\vect{x}^TA\vect{x} =1$  an ellipse/hyperbola/something else?

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/51f56e96-3761-44c5-8d20-4cf0047a1ea4?id=93115
:label: grasple_exercise_8_2_12
:dropdown:
:description: Maximizing  $\vect{x}^TA\vect{x}$ under the restriction $\norm{\vect{x}}=1$, for a 2x2 matrix $A$. 

::::

The following exercises are a more theoretical.

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/01a3d009-b2e0-4f2b-9d49-fcca955d6c5d?id=91048
:label: grasple_exercise_8_2_13
:dropdown:
:description: (True/False?)  if $A$ is a positive definite matrix, then the diagonal of $A$ is positive (v.v.).

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7fea2ed7-c54f-4665-8ac8-611a8b0f6c5e?id=93114
:label: grasple_exercise_8_2_14
:dropdown:
:description: If $A$ and $B$ are symmetric matrices with positive eigenvalues, what about $A+B$?

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/78b55ab4-4f27-4d32-90ec-9bb28bb8f7b8?id=91021
:label: grasple_exercise_8_2_15
:dropdown:
:description: Two True/False questions about vectors $\vect{x}$ for which $\vect{x}^TA\vect{x} = 0$. 

::::