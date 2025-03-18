(Sec:SymmetricMat)=

# Symmetric Matrices

## Introduction

::::{prf:definition}
:label: Dfn:SymmetricMat:SymmetricMatrix

A matrix $A$ is called a **symmetric matrix** if

$$
  A^T = A.
$$

Note that this definition implies that a symmetric matrix must be a square matrix.

::::

::::{prf:example}
:label: Ex:SymmetricMat:SymmMat

The matrices

$$
  A_1 = \begin{bmatrix} 2&\class{blue}3&\class{red}4\\\class{blue}3&1&\class{green}5 \\\class{red}4&\class{green}5&7  \end{bmatrix} \quad \text{and} \quad
  A_2 = \begin{bmatrix} 0&2&3&4\\
    2&0&1&5 \\
    3&1&0&6 \\
    4&5&6&7\end{bmatrix}
$$

are symmetric. The matrices

$$
  A_3 = \begin{bmatrix} 2&3&4\\2&3&4 \\ 2&3&4 \end{bmatrix} \quad \text{and} \quad
  A_4 = \begin{bmatrix} 0&2&3&0\\
            2&0&1&0 \\
            3&1&0&0 \\
        \end{bmatrix}
$$

are not symmetric.

::::

Symmetric matrices appear in many different contexts. In statistics the _covariance matrix_ is an example of a symmetric matrix.
In engineering the so-called _elastic strain matrix_ and the _moment of inertia tensor_ provide examples.

The crucial thing about symmetric matrices is stated in the main theorem of this section.

::::{prf:theorem}
:label: Thm:SymmetricMat:OrthogDiag

Every symmetric matrix $A$ is orthogonally diagonalizable.

By this we mean: there exist an _orthogonal_ matrix $Q$ and a diagonal matrix $D$ for which

$$
   A = QDQ^{-1} = QDQ^T.
$$

Conversely, every orthogonally diagonalizable matrix is symmetric.

This theorem is known as the _Spectral Theorem for Symmetric Matrices_.
In other contexts the word _spectrum_ of a transformation is used for the set of eigenvalues.
::::

So, for a symmetric matrix an orthonormal basis of eigenvectors always exists. For the inertia tensor of a 3D body such a basis corresponds to the (perpendicular) principal axes.

::::{admonition} Proof of the converse of {prf:ref}`Thm:SymmetricMat:OrthogDiag`
:class: tudproof

Recall that an orthogonal matrix is a matrix $Q$ for which $Q^{-1} = Q^T$.

With this reminder it is just a one line proof. 

If $A = QDQ^{-1} = QDQ^T$,

then $A^T = (QDQ^{-1} )^T = (Q^{-1} )^TD^TQ^T = (Q^T)^TD^TQ^T = QDQ^T = A$.

::::

The proof of the other implication we postpone
till {numref}`Subsection %s <SubSec:SymmetricMat:OrthogDiag>`.

We end this introductory section with one representative example.

::::{prf:example}
:label: Ex:SymmetricMat:OrthDiag2x2

Let $A$ be given by $A = \begin{bmatrix} 1&2\\2&-2 \end{bmatrix}$.

The eigenvalues are found via

$$
 \det{(A - \lambda I)} = \begin{vmatrix} 1-\lambda&2\\2&-2-\lambda \end{vmatrix}
   = (1-\lambda)(-2-\lambda) -4 =   \lambda^2 +\lambda -6 =  (\lambda-2)(\lambda+3) .
$$

They are $\lambda_1 = 2$ and $\lambda_2 = -3$.

Corresponding eigenvectors are $\mathbf{v}_1 = \begin{bmatrix} 2\\1 \end{bmatrix}$ for $\lambda_1$, and
$\mathbf{v}_2 = \begin{bmatrix} -1\\2 \end{bmatrix}$.

The eigenvectors are orthogonal,

$$
  \mathbf{v}_1 \ip \mathbf{v}_2 = \begin{bmatrix} 2\\1 \end{bmatrix}\ip \begin{bmatrix} -1\\2 \end{bmatrix} = -2  +2  = 0,
$$

and $A$ can be diagonalized as

$$
   A = PDP^{-1} = \begin{bmatrix}2&-1\\1&2 \end{bmatrix}\begin{bmatrix}2 & 0\\0& -3 \end{bmatrix}
   \begin{bmatrix}2&-1\\1&2 \end{bmatrix}^{-1}.
$$

In {numref}`Figure %s <Fig:SymmetricMat:Evectors>`
the image of the unit circle under the transformation $\vect{x} \mapsto A\vect{x}$ is shown.
In the picture on the right,

$$
\vect{q}_1 = \frac{1}{\norm{\vect{v}_1}}\vect{v}_1 = \frac{1}{\sqrt{5}}\begin{bmatrix} 2\\1 \end{bmatrix}  \quad \text{and} \quad \vect{q}_2= \frac{1}{\norm{\vect{v}_2}}\vect{v}_2 = \frac{1}{\sqrt{5}}\begin{bmatrix} -1\\2 \end{bmatrix}
$$

 are two orthonormal unit eigenvectors.

:::{figure} Images/Fig-SymmetricMat-Evectors.svg
:name: Fig:SymmetricMat:Evectors
:class: dark-light

The transformation $T(\vect{x}) =  \begin{bmatrix} 1&2\\2&-2 \end{bmatrix}\vect{x}$. The vectors  $\vect{q}_1$ and $\vect{q}_2$ are two orthogonal vectors on the unit circle that are mapped onto multiples of themselves.
:::


Furthermore, if we normalize the eigenvectors, i.e., the columns of $P$, we find the following diagonalization of $A$ with an orthogonal matrix $Q$:

$$
 A = QDQ^{-1} = \begin{bmatrix}2/\sqrt{5}&1/\sqrt{5}\\1/\sqrt{5}&-2/\sqrt{5} \end{bmatrix}\begin{bmatrix}2 & 0\\0& -3 \end{bmatrix}
   \begin{bmatrix}2/\sqrt{5}&1/\sqrt{5}\\1/\sqrt{5}&-2/\sqrt{5} \end{bmatrix}^{-1}.
$$

::::

(SubSec:SymmetricMat:EssentialProp)=

## The essential properties of symmetric matrices

::::{prf:proposition}
:label: Prop:SymmetricMat:OrthogonalEigenvectors

Suppose $A$ is a symmetric matrix.

If $\mathbf{v}_1$ and $\mathbf{v}_2$ are eigenvectors of $A$ for _different_ eigenvalues, then $\mathbf{v}_1\perp \mathbf{v}_2$.
::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors`
:class: tudproof

Suppose $\mathbf{v}_1$ and $\mathbf{v}_2$ are eigenvectors of the symmetric matrix $A$ for the different eigenvalues $\lambda_1,\lambda_2$.
We want to show that $\mathbf{v}_1 \ip \mathbf{v}_2 = 0$.

The trick is to consider the expression

:::{math}
:label: Eq:SymmetricMat:Av1v2

(A\mathbf{v}_1) \ip \mathbf{v}_2.

:::

On the one hand

$$
   (A\mathbf{v}_1) \ip \mathbf{v}_2 = (\lambda_1\mathbf{v}_1) \ip \mathbf{v}_2 =  \lambda_1(\mathbf{v}_1 \ip \mathbf{v}_2).
\nonumber
$$

On the other hand

$$
   (A\mathbf{v}_1) \ip \mathbf{v}_2 = (A\mathbf{v}_1)^T \mathbf{v}_2 =\mathbf{v}_1^TA^T \mathbf{v}_2.
\nonumber
$$

Since we assumed that $A^T = A$ we can extend the chain of identities:

$$
  \mathbf{v}_1^TA^T \mathbf{v}_2 =   \mathbf{v}_1^T A \mathbf{v}_2 =\mathbf{v}_1^T (A \mathbf{v}_2) =
  \mathbf{v}_1^T (\lambda_2 \mathbf{v}_2) =  \lambda_2(\mathbf{v}_1^T  \mathbf{v}_2) =  \lambda_2(\mathbf{v}_1 \ip \mathbf{v}_2).
\nonumber
$$

So we have shown that

$$
    (A\mathbf{v}_1) \ip \mathbf{v}_2  = \lambda_1(\mathbf{v}_1 \ip \mathbf{v}_2) = \lambda_2(\mathbf{v}_1 \ip \mathbf{v}_2).
\nonumber
$$

Since

$$
\lambda_1 \neq \lambda_2,
\nonumber
$$

it follows that indeed

$$
\mathbf{v}_1\ip \mathbf{v}_2 = 0,

$$

as was to be shown.

::::

::::{exercise}
:label: Exc:SymmetricMat:uTAv

Prove the following slight generalization of {prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors`.

If $\vect{u}$ is an eigenvector of $A$ for the eigenvalue $\lambda$, and $\vect{v}$ is an eigenvector of $A^T$ for a different eigenvalue $\mu$, then $\vect{u} \perp \vect{v}$.

::::

::::{admonition} Solution to&nbsp;{numref}`Exc:SymmetricMat:uTAv`
:class: solution, dropdown

The proof is completely analogous to the proof of {prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors`.
Suppose  

$$
  A\mathbf{u} = \lambda\mathbf{u},\quad A\mathbf{v} = \mu\mathbf{v},\quad\text{  where} \,\,\,\lambda \neq \mu.
$$

We consider the expression  $\mathbf{u}^T\ip A \mathbf{v} = \mathbf{u}T A \mathbf{v}$.

On the one hand  

:::{math}
:label: eq:SymmetricMat:uTAv3

  \mathbf{u}\ip A \mathbf{v} = \mathbf{u}^T (A\mathbf{v}) = \mathbf{u}^T  \mu \mathbf{v} = \mu \mathbf{u}T\mathbf{v}  = \mu (\mathbf{u}\mathbf{v})

:::

On the other hand
:::{math}
:label: eq:SymmetricMat:uTAv4

  \mathbf{u}\ip A \mathbf{v} = \mathbf{u}^T\ A^T \mathbf{v} = (A\mathbf{u})^T\mathbf{v} = 
  \lambda \mathbf{u}^T\mathbf{v} = \lambda (\mathbf{u}\mathbf{v})

:::

Comparing {eq}`eq:SymmetricMat:uTAv3`  and  {eq}`eq:SymmetricMat:uTAv4`  we can conclude that $\mathbf{u}\ip\mathbf{v} = 0$,  i.e.,  $\mathbf{u}$ and $\mathbf{v}$
are indeed orthogonal.

::::

::::{prf:proposition}
:label: Prop:SymmetricMat:RealEigenvalues

All eigenvalues of symmetric matrices are real.

::::

The easiest proof is via complex numbers. Feel free to skip it, in particular when you don't feel comfortable with complex numbers.

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:SymmetricMat:RealEigenvalues`
:class: tudproof, dropdown

For two vectors $\mathbf{u},\mathbf{v}$ in $\C^n$ we consider the expression

$$
  \overline{\mathbf{u}}^{T}\mathbf{v} = \overline{u_1}v_1 + \ldots + \overline{u_n}v_n.
$$

If we take $\mathbf{v}$ equal to $\mathbf{u}$ we get

$$
  \overline{\mathbf{u}}^{T}\mathbf{u} = \overline{u_1}u_1 + \overline{u_2}u_2 + \ldots +  \overline{u_n}u_n =
                          |u_1|^2 + |u_2|^2 + \ldots + |u_n|^2,
$$

where $|u_i|$ denotes the modulus of the complex number $u_i$. This sum of squares (of real numbers) is a non-negative real number. We also see that
$\overline{\mathbf{u}}^{T}\mathbf{u} = 0$ only holds if $\mathbf{u} = \mathbf{0}$.

It can also be verified that

$$
  \overline{\overline{\mathbf{u}}^{T}\mathbf{v}} = \overline{\mathbf{v}}^T  \mathbf{u}.
$$

Now suppose that $\lambda$ is an eigenvalue of the symmetric matrix $A$, and $\mathbf{v}$ is a nonzero (possibly complex) eigenvector of $A$ for the eigenvalue $\lambda$. Note that, since $A$ is real and symmetric, $\overline{{A}^T} = \overline{A} = A$.
To prove that $\lambda$ is real, we will show that $\overline{\lambda} = \lambda$.

We use kind of the same 'trick' as in {prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors` Equation {eq}`Eq:SymmetricMat:Av1v2`.
<BR>
On the one hand

$$
  \overline{(A \mathbf{v})^T} \mathbf{v} = \overline{\lambda\mathbf{v}^T} \mathbf{v} =
 \overline{\lambda}  \overline{\mathbf{v}}^T \mathbf{v}.
$$

On the other hand,

$$
 \overline{(A \mathbf{v})^T} \mathbf{v} = \overline{\mathbf{v}^T A^T}\mathbf{v} = \overline{\mathbf{v}^T}\,\overline{{A}^T} \mathbf{v}  = \overline{\mathbf{v}}^T\,\overline{A} \mathbf{v}  =
 \overline{\mathbf{v}}^T A\mathbf{v}  =  \overline{\mathbf{v}}^T  \lambda\mathbf{v}  = \lambda\overline{\mathbf{v}}^T \mathbf{v}.
$$

So we have that

$$
   \overline{\lambda}  \overline{\mathbf{v}}^T \mathbf{v} = \lambda\overline{\mathbf{v}}^T \mathbf{v}.
$$

Since we assumed that $\mathbf{v}$ is not the zero vector, we have that $\overline{\mathbf{v}}^T \mathbf{v} \neq 0$ , and so it follows that $ \overline{\lambda} =\lambda$. Which is equivalent to $\lambda$ being real.

::::


::::{prf:example}

Let $A = \begin{bmatrix} a&b\\b&d \end{bmatrix} $.

Then the characteristic polynomial is computed as

$$
  \begin{vmatrix} a-\lambda&b\\b&d-\lambda \end{vmatrix} =
  (a-\lambda)(d-\lambda) - b^2 = \lambda^2 - (a+d)\lambda + ad - b^2.
\nonumber
$$

The discriminant of this second order polynomial is given by

$$
  D =  (a+d)^2 -4(ad -b^2) = a^2+d^2 - 2ad + 4b^2 = (a-d)^2 + 4b^2 \geq 0.
\nonumber
$$

The discriminant is non-negative, so the characteristic polynomial has only real roots, and consequently the eigenvalues of the matrix are real.

Obviously, an elementary approach like this will soon get very complicated for larger $n \times n$ matrices.

::::

Lastly we come to the third of three essential properties of symmetric matrices.

::::{prf:proposition}
:label: Prop:SymmetricMat:AlgGeomMultiplicity

For each eigenvalue of a symmetric matrix the geometric multiplicity is equal to the algebraic multiplicity.

::::

We will incorporate the proof of this proposition into the proof of the main theorem in
{numref}`Subsection %s <SubSec:SymmetricMat:OrthogDiag>`. For now, we will look at a few examples.

::::{prf:example}

We will verify that the symmetric matrix $A = \begin{bmatrix} 1 & 0 & 1\\0 & 1  & 2 \\ 1 & 2 & 5 \end{bmatrix}$
is diagonalizable and has mutually orthogonal eigenvectors.

We first compute the characteristic polynomial.

Expansion along the first column gives

$$
      \begin{array}{rcl}
        \begin{vmatrix}    1-\lambda & 0 & 1\\0 & 1-\lambda  & 2 \\ 1 & 2 & 5-\lambda \end{vmatrix}
        &=&
        (1-\lambda)\begin{vmatrix}    1-\lambda  & 2 \\ 2 & 5-\lambda\end{vmatrix} +
        1\cdot\begin{vmatrix}     0 & 1 \\ 1-\lambda  & 2\end{vmatrix} \\
        &=&
         (1-\lambda)\big((1-\lambda)(5-\lambda) -4 \big)- (1-\lambda)  \\
        &=&
         (1-\lambda) (\lambda^2-6\lambda) =  (1-\lambda) (\lambda-6)\lambda.
        \end{array}
    \nonumber
$$

So $A$ has the real eigenvalues $\lambda_{1} = 1$, $\lambda_2 = 6$ and $\lambda_3 = 0$. Since all eigenvalues have algebraic multiplicity 1, the corresponding eigenvectors will give a basis of eigenvectors, and we can immediately conclude that $A$ is diagonalizable.

The eigenvectors are found to be

$$
   \mathbf{v}_1 = \begin{bmatrix} 2 \\-1 \\ 0 \end{bmatrix} \text{ for } \lambda_1 = 1, \quad
   \mathbf{v}_2 = \begin{bmatrix} 1 \\ 2 \\ 5 \end{bmatrix} \text{ for } \lambda_2, \quad
   \mathbf{v}_3 = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix} \text{ for } \lambda_3.
\nonumber
$$

We see: the three eigenvectors form an orthogonal threesome, in accordance
with {prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors`.

::::

::::{prf:example}
:label: Ex:SymmetricMat:DoubleEV

Consider the matrix $A = \begin{bmatrix} 2&2&4\\2 & -1 & 2 \\ 4&2&2 \end{bmatrix}$.

A (rather involved) computation yields the eigenvalues $\lambda_{1,2} = -2$ and $\lambda_3 = 7$.
Indeed all eigenvalues are real, conforming to {prf:ref}`Prop:SymmetricMat:RealEigenvalues`.

Next we find the eigenvectors and the geometric multiplicities of the eigenvalues.

For $\lambda = -2$ we find via row reduction

$$
    [A - (-2)I\,|\,\mathbf{0}] =
    \left[\begin{array}{ccc|c} 4&2&4&0\\2 & 1 & 2 &0\\ 4&2&4&0\end{array}\right]       \sim
    \left[\begin{array}{ccc|c} 2&1&2&0\\0&0&0&0 \\0&0&0&0\end{array}\right]    \nonumber
$$

the two linearly independent eigenvectors $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \\ -1\end{bmatrix}$ and
$\mathbf{v}_2 = \begin{bmatrix} 1 \\ -2 \\ 0\end{bmatrix}$. The geometric multiplicity of $\lambda_{1,2}$ is equal to 2.
The other eigenvalue has algebraic multiplicity 1, so its geometric multiplicity has to be 1 as well. With this {prf:ref}`Prop:SymmetricMat:AlgGeomMultiplicity` is verified.

Lastly we leave it to you to check that an eigenvector for $\lambda_3 = 7$ is given by $\mathbf{v}_3 = \begin{bmatrix} 2 \\ 1 \\ 2\end{bmatrix}$. And that both $\mathbf{v}_3 \perp \mathbf{v}_1$ and $\mathbf{v}_3 \perp \mathbf{v}_2$, so that {prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors` is satisfied as well.
::::

(SubSec:SymmetricMat:OrthogDiag)=

## Orthogonal Diagonalizability of Symmetric Matrices

Let us restate the main theorem ({prf:ref}`Thm:SymmetricMat:OrthogDiag`) about symmetric matrices:

A matrix $A$ is symmetric if and only if it is orthogonally diagonalizable.

Note that this also establishes the property that for each eigenvalue of a symmetric matrix the geometric multiplicity equals the algebraic multiplicity
({prf:ref}`Prop:SymmetricMat:AlgGeomMultiplicity`).

We will put the intricate proof at the end of the subsection, and first consider two examples.

The first example is a continuation of the earlier {prf:ref}`Ex:SymmetricMat:DoubleEV`.

::::{prf:example}
:label: Ex:SymmetricMat:OrthogDiag3x3

The matrix $A = \begin{bmatrix} 2&2&4\\2 & -1 & 2 \\ 4&2&2 \end{bmatrix}$ was shown to have the eigenvalues/eigenvectors

$$
  \lambda_{1,2} = -2, \quad \mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \\ -1\end{bmatrix}, \,
  \mathbf{v}_2 = \begin{bmatrix} 1 \\ -2 \\ 0\end{bmatrix},
  \quad \lambda_3 = 7, \quad \mathbf{v}_3 = \begin{bmatrix} 2 \\ 1 \\ 2\end{bmatrix}.
$$

The pairs $\mathbf{v}_1, \mathbf{v}_3$ and $\mathbf{v}_2, \mathbf{v}_3$ are 'automatically' orthogonal.

For the eigenspace $E_{-2} = \Span{\mathbf{v}_1, \mathbf{v}_2}$ we can use Gram-Schmidt to get an orthogonal basis:

$$
  \mathbf{u}_1 = \mathbf{v}_1, \quad \mathbf{u}_2 =
         \mathbf{v}_2 - \dfrac{\mathbf{v}_2 \ip \mathbf{u}_1}{\mathbf{u}_1 \ip \mathbf{u}_1} \mathbf{u}_1
         = \dfrac12\begin{bmatrix} 1 \\ -4 \\ 1\end{bmatrix}.
$$

Normalizing the orthogonal basis $\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{v}_3\}$ and putting them side by side in a matrix yields the orthogonal matrix

$$
  Q = \begin{bmatrix} \dfrac{1}{\sqrt{2}} & \dfrac{1}{\sqrt{18}} & \dfrac{2}{3} \\
  0 & \dfrac{-4}{\sqrt{18}} & \dfrac{1}{3}\\ \dfrac{-1}{\sqrt{2}} &  \dfrac{1}{\sqrt{18}} & \dfrac{2}{3}
  \end{bmatrix}.
$$

The conclusion becomes that

$$
 A = QDQ^{-1} = QDQ^T, \quad \text{where still}  \,\,\, D = \begin{bmatrix} -2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 7\end{bmatrix}.
$$

::::

The procedure followed in  {prf:ref}`Ex:SymmetricMat:OrthogDiag3x3` leads way to an algorithm for constructing an orthogonal diagonalization.

::::{prf:algorithm}
:label: Alg:SymmetricMat:OrthogDiagonalization

1. Compute the eigenvalues of the matrix.

2. Find a basis for each eigenspace.

3. Use the Gram-Schmidt procedure to turn these bases into orthonormal bases for the eigenspace

4. Put everything together in the matrices $D$  and $Q$. 

::::

One more example to illustrate matters, before we get to the proof (or you jump over to
{numref}`SubSec:SymmetricMat:SpectralDecomp`).

::::{prf:example}
:label: Ex:SymmetricMat:OrthogDiag3x3bis

Let the symmetric matrix $A$ be given by $ A = \begin{bmatrix}
1 & 2 & 2 & 0 \\ 2 & -1 & 0 & 2 \\ 2 & 0 & -1 & -2 \\ 0 & 2 & -2 & 1
\end{bmatrix}$.

The hard part is to find the eigenvalues. (I.e., how to solve an equation of the order four?!)
Once we know what the eigenvalues are, the other steps are 'routine'.

It appears that $A$ has the double eigenvalues $\lambda_{1,2} = 3$ and $\lambda_{3,4} = -3$.

To find the eigenvectors for the eigenvalue 3 we row reduce the matrix $(A - 3I)$.

$$
\left[\begin{array}{cccc}1-3 & 2 & 2 & 0\\ 2 & -1-3 & 0 & 2 \\ 2 & 0 & -1-3 & -2 \\ 0 & 2 & -2 & 1-3  \end{array} \right]  \,\,  \sim \,\,\ldots\,\, \sim  \,\,
\left[\begin{array}{cccc}1 & 0 & -2 & -1\\ 0 & 1 & -1 & -1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0  \end{array} \right].
$$

We can read off two linearly independent eigenvectors

$$
\vect{v}_1 = \left[\begin{array}{c} 1 \\ 1 \\ 0 \\ 1   \end{array} \right], \quad
\vect{v}_2 = \left[\begin{array}{c} 2 \\ 1 \\ 1 \\ 0 \end{array} \right].
$$

As in {prf:ref}`Ex:SymmetricMat:OrthogDiag3x3` we can construct an orthogonal basis for the eigenspace $E_{3}$:

$$
  \mathbf{u}_1 = \mathbf{v}_1, \quad \mathbf{u}_2 =
         \mathbf{v}_2 - \dfrac{\mathbf{v}_2 \ip \mathbf{u}_1}{\mathbf{u}_1 \ip \mathbf{u}_1} \mathbf{u}_1
         = \begin{bmatrix} 1 \\ 0 \\ 1\\ -1\end{bmatrix}
$$

Likewise we can first find a 'natural' basis for the eigenspace $E_{-3}$ by row reducing $(A - (-3I))$:

$$
(A - (-3I)) = \left[\begin{array}{cccc}4 & 2 & 2 & 0\\ 2 & 2 & 0 & 2 \\ 2 & 0 & 2 & -2 \\ 0 & 2 & -2 & 4  \end{array} \right] \quad  \sim \ldots \sim  \quad
\left[\begin{array}{cccc}1 & 0 & 1 & -1\\ 0 & 1 & -1 & 2 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0  \end{array} \right].
$$

Two independent eigenvectors: $\vect{v}_3 = \left[\begin{array}{c} -1 \\ 1 \\ 1 \\ 0  \end{array} \right]$ and $\vect{v}_4 = \left[\begin{array}{c} 1 \\ -2 \\ 0 \\ 1  \end{array} \right]$.

Again these can be orthogonalized, and then we find the following complete set of eigenvectors, i.e., a basis for $\R^4$:

$$
  \vect{u}_1 = \begin{bmatrix} 1 \\ 1 \\ 0\\ 1\end{bmatrix}, \quad
  \vect{u}_2 = \begin{bmatrix} 1 \\ 0 \\ 1\\ -1\end{bmatrix}, \quad
  \vect{u}_3 = \begin{bmatrix} -1 \\ 1 \\ 1\\ 0\end{bmatrix}, \quad
  \vect{u}_4 = \begin{bmatrix} 0 \\ -1 \\ 1 \\ 1\end{bmatrix}.
$$

We conclude that $A = QDQ^{-1}$, where

$$
    D = \left[\begin{array}{cccc}3 & 0 & 0 & 0\\ 0 & 3 & 0 & 0 \\ 0 & 0 & -3 & 0 \\ 0 & 0 & 0 & -3  \end{array} \right], \quad
   Q = \dfrac{1}{\sqrt{3}} \left[\begin{array}{cccc}1 & 1 & -1 & 0\\
                                                    1 & 0 & 1 & -1 \\
                                                    0 & 1 & 1 & 1 \\
                                                    1 & -1 & 0 & 1  \end{array} \right].
$$

::::

And now it's time for the proof of the main theorem. The proof is of the type technical and intricate. Skip it if you like. 

::::{admonition} Proof of&nbsp;{prf:ref}`Thm:SymmetricMat:OrthogDiag`
:class: tudproof, dropdown

Suppose that $A$ is a symmetric $n \times n$ matrix. We know there are $n$ real, possibly multiple, eigenvalues
$\lambda_1, \lambda_2, \ldots, \lambda_n$.
Suppose $\vect{q}_1$ is an eigenvector for $\lambda_1$ with unit length.
We can extend $\{\vect{q}_1\}$ to an orthonormal basis $\{\vect{q}_1,\vect{q}_2,\ldots,\vect{q}_n\}$.
Let $Q_1$ be the matrix with the columns $\vect{q}_1,\vect{q}_2,\ldots,\vect{q}_n$.

It can be shown that $A_1 = Q_1^{-1}AQ_1 = Q_1^TAQ_1$ is of the form

$$
   \left[\begin{array}{ccc} \lambda_1 & 0   & \ldots & 0  \\
    0 &   \\
     \vdots   & & B_1 &  \\
    0 &
   \end{array}\right]
$$

where $B_1$ is an $(n-1)\times(n-1)$ matrix that is also symmetric.

Namely, the first column of $A_1$ can be computed as

$$
  A_1\vect{e}_1 = Q_1^{-1}AQ_1\vect{e}_1 = Q_1^{-1}A\vect{q}_1 = Q_1^{-1}\lambda_1\vect{q}_1 =
     \lambda_1Q_1^{-1}\vect{q}_1
$$

and $Q_1^{-1}\vect{q}_1$ is the first column of $Q_1^{-1}Q_1$, which is $\vect{e}_1$.

This shows that the first column of $A_1$ must indeed be $\lambda_1\vect{e}_1 = \left[\begin{array}{c}
\lambda_1 \\ 0 \\ \vdots \\ 0 \end{array}\right]$.

Since $A$ is symmetric and $Q_1$ is by construction an orthogonal matrix,

$$
   A_1^T = (Q_1^{T}AQ_1)^T = Q_1^T A^T (Q_1^T)^T = Q_1^{T}AQ_1 = A_1.
$$

So $A_1$ is also symmetric. Thus if the first column of $A_1$ contains $n-1$ zeros, so does its first row.

Since $A$ and $A_1$ are similar, they have the same eigenvalues.
It follows that $B_1$ has the eigenvalues $\lambda_2, \ldots, \lambda_n$.

We can apply the same construction to $B_1$, yielding

$$
   B_2 = (\tilde{Q}_2)^{-1}B_1\tilde{Q}_2
   =    \left[\begin{array}{cccc} \lambda_2 & 0   & \ldots & 0  \\
    0 &   \\
     \vdots   & & \tilde{B}_2 &  \\
    0 &
   \end{array}\right].
$$

Note that in this formula the matrices have size $(n-1)$ by $(n-1)$.

If we then define

$$
   Q_2 =
    \left[\begin{array}{cccc} 1 & 0   & \ldots & 0  \\
    0 &   \\
     \vdots   & & \tilde{Q}_2 &  \\
    0 &
   \end{array}\right],

$$

it follows that

$$
  A_2 = Q_2^{-1}A_1Q_2 =
  \left[\begin{array}{cccccc}
    \lambda_1 &      0    & 0  & \ldots & 0  \\
       0      & \lambda_2 & 0  & \ldots & 0  \\
       0      &  0  \\
    \vdots & \vdots & & \tilde{B_2}  \\
    0 & 0 &
   \end{array}\right].
$$

Continuing in this fashion we find

$$
  A_{n-1} = Q_{n-1}^{-1} \cdots Q_2^{-1}Q_1^{-1}A Q_1  Q_2 \cdots Q_{n-1} =
  \left[\begin{array}{ccccc}
    \lambda_1 &      0    & 0  & \ldots &0 \\
       0      & \lambda_2 & 0  &\ldots &0 \\
     \vdots & & \ddots &  & \vdots\\
     \vdots & &  & \ddots & \vdots\\
     0 & 0 &  \ldots & 0 &\lambda_n
   \end{array}\right].


$$

This proves that $A$ is diagonalizable, with $Q = Q_1Q_2 \cdots Q_{n-1}$ as a diagonalizing matrix.

Moreover, since the product of orthogonal matrices is orthogonal, $A$ is in fact orthogonally diagonalizable.

%::::

:::{prf:example}
:label: Ex:SymmetricMat:ConstructDiag

We will illustrate the proof for the matrix

$$
    A = \begin{bmatrix}
     1 & 2 & 2 & 0 \\ 2 & -1 & 0 & 2 \\ 2 & 0 & -1 & -2 \\ 0 & 2 & -2 & 1
    \end{bmatrix}.
$$

Since

$$
    \begin{bmatrix}
     1 & 2 & 2 & 0 \\ 2 & -1 & 0 & 2 \\ 2 & 0 & -1 & -2 \\ 0 & 2 & -2 & 1
    \end{bmatrix}
    \begin{bmatrix}
     1 \\-1\\-1\\0
    \end{bmatrix} =
    \begin{bmatrix}
     -3 \\3\\3\\0
    \end{bmatrix}
$$

we have as a starter the eigenvalue and corresponding eigenvector

$$
  \lambda_1 = -3, \quad \vect{v}_1 = \begin{bmatrix}  1 \\-1\\-1\\0   \end{bmatrix}.
$$

An orthogonal basis for $\mathbb{R}^4$, starting with this first eigenvector is, for instance

$$
   \vect{v}_1 = \begin{bmatrix}  1 \\-1\\-1\\0   \end{bmatrix}, \quad
   \vect{v}_2 = \begin{bmatrix}  1 \\1\\0\\0   \end{bmatrix}, \quad
   \vect{v}_3 = \begin{bmatrix}  1 \\-1\\2\\0   \end{bmatrix}, \quad
   \vect{v}_4 = \begin{bmatrix}  0\\0\\0\\1   \end{bmatrix}. \quad
$$

Rescaling and putting them into a matrix yields

$$
    Q_1 = \begin{bmatrix}
             1/\sqrt{3} & 1/\sqrt{2} & 1/\sqrt{6} & 0 \\
             -1/\sqrt{3} & 1/\sqrt{2} & -1/\sqrt{6} & 0 \\
             -1/\sqrt{3} & 0 & 2/\sqrt{6} & 0 \\
             0 & 0 & 0 & 1
        \end{bmatrix}.
$$

Next we compute

$$
   A_1 = Q_1^{-1}AQ_1 = Q_1^TAQ_1 = \begin{bmatrix}
             -3 &  0 & 0 & 0 \\
             0 & 2 & \sqrt{3} & \sqrt{2} \\
             0 & \sqrt{3} & 0  & -\sqrt{6} \\
             0 & \sqrt{2} & -\sqrt{6} & 1
        \end{bmatrix}.
$$

This is indeed of the form stated in the proof.

We continue with the matrix $B_1 = \left[\begin{array}{ccc}
                  2 & \sqrt{3} & \sqrt{2} \\ 
                  \sqrt{3} & 0  & -\sqrt{6} \\
                  \sqrt{2} & -\sqrt{6} & 1
                  \end{array}   \right]$.

$B_1$ has eigenvalue $-3$ with eigenvector $\vect{u}_1 = \left[\begin{array}{c}
                                            1 \\   -\sqrt{3} \\ -\sqrt{2}  
                                            \end{array}   \right]$.

Again we extend to an orthogonal basis for $\mathbb{R}^3$. For instance,

$$
    \vect{u}_1, \quad \vect{u}_2 = \left[\begin{array}{c}
                                            \sqrt{2} \\   0\\ 1
                                    \end{array}   \right], \quad
                      \vect{u}_3 = \left[\begin{array}{c}
                                            1 \\ \sqrt{3} \\  -\sqrt{2}
                                    \end{array}   \right].
$$

If we normalize and use them as the columns of $\tilde{Q}_2$ as in the proof of {prf:ref}`Thm:SymmetricMat:OrthogDiag`, we find as second matrix in that construction

$$

   Q_2 = \left[\begin{array}{cccc} 1 & 0 & 0 & 0 \\
                  0 & \dfrac{1}{\sqrt{6}} &  \dfrac{\sqrt{2}}{\sqrt{3}} & \dfrac{1}{\sqrt{6}} \\
                  0 & \dfrac{-1}{\sqrt{2}} &  0 & \dfrac{1}{\sqrt{2}} \\
                  0 & \dfrac{-1}{\sqrt{3}} &  \dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{3}}
                                    \end{array}   \right].


$$

And then

$$
A_2 = Q_2^TQ_1^T A Q_1Q_2 =
\left[\begin{array}{cccc}
-3 & 0 & 0 & 0 \\
0 &-3 & 0 & 0 \\
0 & 0 & 3 & 0 \\
0 & 0 & 0 & 3
\end{array} \right] = D,
$$

indeed a _diagonal_ matrix. <BR>
For this example the matrix has the second double eigenvalue $\lambda_{3,4} = 3$. Because of that, the construction takes one step less than in the general case.  
Defining $Q = Q_1Q_2$, we can rewrite the last identity as

$$
  Q^{-1}AQ = D, \,\,\text{ so }\,\,
  A = QDQ^{-1} = QDQ^T
$$

for the matrix $Q = Q_1Q_2$. This is the matrix

$$
  Q =  \left[\begin{array}{cccc} \dfrac{1}{\sqrt{3}} & 0 & \dfrac{1}{\sqrt{3}} & \dfrac{1}{\sqrt{3}} \\
                 -\dfrac{1}{\sqrt{3}} & \dfrac{1}{\sqrt{3}} & \dfrac{1}{\sqrt{3}} & 0 \\
                 -\dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{3}} & 0 & \dfrac{1}{\sqrt{3}} \\
                 0 & -\dfrac{1}{\sqrt{3}} & \dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{3}}
                                    \end{array}   \right] =
        \dfrac{1}{\sqrt{3}}\left[\begin{array}{cccc} 1 & 0 & 1 & 1 \\
                 -1 & 1 & 1 & 0 \\ -1 & -1 & 0 & 1 \\ 0 & -1 & 1 & -1
                                    \end{array}   \right].
$$

So we see that $A$ has the 'simpler' eigenvectors

$$
  \vect{v}_1 = \left[\begin{array}{c} 1 \\ -1 \\ -1 \\ 0
                                    \end{array}   \right], \quad
  \vect{v}_2 = \left[\begin{array}{c} 0 \\ 1 \\ -1 \\ -1
                                    \end{array}   \right], \quad
  \vect{v}_3 = \left[\begin{array}{c} 1 \\ 1 \\ 0 \\ 1
                                    \end{array}   \right], \quad
  \vect{v}_4 = \left[\begin{array}{c} 1 \\ 0 \\ 1 \\ -1
                                    \end{array}   \right].
$$

Note: given the eigenvalues, these eigenvectors could have been found more efficiently by solving the systems
$(A - \lambda_iI)\vect{x} = \vect{0}$, and then orthogonalize by the Gram-Schmidt procedure. As is done in
{prf:ref}`Ex:SymmetricMat:OrthogDiag3x3`. <BR>
The importance of the step-by-step reduction is that it shows that from the 'minimal' assumptions of symmetry and the existence of real eigenvalues it is possible to create an orthogonal diagonalization.

:::

::::


There are situations where it is important to know how large  $\norm{A\vect{x}}$ can become for unit vectors $\vect{x}$.  The general case, for non-square matrices,  will be handled in {numref}`Subsection %s <Subsec:SVDGeometrically>`.  For symmetric matrices the question is answered by the next proposition.

::::{prf:proposition}
:label: Prop:SymmetricMat:Max||Ax||

Suppose $A$ is a symmetric matrix.  Then the maximum value  $\norm{A\mathbf{x}}$  will attain on the set of unit vectors is equal to  $|\lambda|$, where $\lambda$ is the eigenvalue of the highest absolute value.
In formula form

$$
 \text{max}\norm{A\mathbf{x}} = |\lambda_{\text{max}}| \,\, \text{on the set} \,\, \{\vect{x}: \norm{\vect{x}} = 1\}.
$$

::::

We will give a proof that makes good use of the existence of an orthogonal basis of eigenvectors.
But first we will give an example that catches the main idea. 


::::{prf:example}
:label: Ex:SymmetricMat:Max||Ax|| 

The (symmetric)  matrix $A = \begin{bmatrix}  -1 & 4  \\ 4 & -1 \end{bmatrix}$ has the 
eigenvalues $\lambda_1 = -5$ and  $\lambda_2 = 3$ with corresponding unit 
eigenvectors  $\mathbf{u}_1 = \dfrac{1}{\sqrt{2}}\begin{bmatrix}  1   \\  -1 \end{bmatrix}$   and  $\mathbf{u}_2 = \dfrac{1}{\sqrt{2}}\begin{bmatrix}  1   \\  1 \end{bmatrix}$ respectively. 
So according to {prf:ref}`Prop:SymmetricMat:Max||Ax||`  the maximum value of $\norm{A\vect{x}}$ on 
the set of vectors with norm 1 must be 5.

First of all, for  $\vect{x} = \vect{u}_1$ it holds that $\norm{A\vect{u}_1} = ||5\vect{u}_1|| = 5$.

Second,  suppose $\vect{x} $ is an arbitrary unit vector. 
We will in fact show that  $\norm{A\vect{x}}^2 \leq 5^2$. Since $\{\vect{u}_1,\vect{u}_2\}$ is a basis,  $\vect{x} = c_1\vect{u}_1 + c_2\vect{u}_2 $, for some parameters $c_1, c_2$. 
Then,  since $\vect{u}_1$ and $\vect{u}_2$ are orthogonal unit vectors,

$$
  \begin{array}{rcl}
  \norm{\vect{x}}^2 = \norm{c_1\vect{u}_1 + c_2\vect{u}_2}^2 &=& \norm{c_1\vect{u}_1}^2  + \norm{c_2\vect{u}_2}^2 \\
  & = &   c_1^2\norm{\vect{u}_1}^2  + c_2^2 \norm{\vect{u}_2}^2 = c_1^2 + c_2^2,
  \end{array}
$$


so &nbsp; $c_1^2 + c_2^2 = \norm{\vect{x}}^2 = 1$.

Likewise,

$$
  \begin{array}{rcl}
  \norm{A\vect{x}}^2 &=& \norm{c_1A\vect{u}_1 + c_2A\vect{u}_2}^2\\
  &=&  \norm{c_1\cdot(-5)\vect{u}_1 + c_2\cdot3\vect{u}_2}^2 \\
  &=&   \norm{c_1\cdot(-5)\vect{u}_1}^2 + \norm{c_2\cdot3\vect{u}_2}^2 \\
  &=& (-5)^2c_1^2\norm{\vect{u}_1}^2  +  3^2c_2^2\norm{\vect{u}_2}^2 \\
  &=& 25c_1^2 + 9c_2^2.
  \end{array}
$$

So we have

$$
  \norm{A\vect{x}}^2 = 25c_1^2 + 9c_2^2 \leq 25c_1^2 + 25c_2^2 = 25(c_1^2 + c_2^2) = 25,
$$

which implies that  indeed  &nbsp;  $\norm{A\vect{x}} \leq 5$  for all vectors $\vect{x}$ with 
$\norm{\vect{x}} = 1$.

::::

The second example shows that symmetry of the matrix is necessary for the property to hold.

::::{prf:example}
:label: Ex:SymmetricMat:NonMax||Ax|| 

The  matrix $B = \begin{bmatrix}  3 & 4  \\ 0 &  3\end{bmatrix}$ has the double eigenvalue $\lambda_1 = \lambda_2 = 3$ and for the unit vector $\mathbf{x} = \begin{bmatrix}  0   \\  1 \end{bmatrix}$  it holds that &nbsp; $   \norm{A\vect{x}} = \norm{\begin{bmatrix} 4\\3 \end{bmatrix}} = 5 > 3 = |\lambda_1|$.

::::

As mentioned,  {prf:ref}`Ex:SymmetricMat:Max||Ax||`  contains the main idea, but for  a proof of the general situation you can open the following exposition.

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:SymmetricMat:Max||Ax||`
:class: tudproof, dropdown

Suppose  $A$ is a symmetric $n \times n$ matrix.
Then $A$ has an orthonormal basis $\vect{u}_1, \vect{u}_2,\ldots,\vect{u}_n$ of eigenvectors for the eigenvalues  $\lambda_1, \ldots, \lambda_n$, where we may suppose that these are ordered according to their absolute values in decreasing order

$$
   |\lambda_1| \geq |\lambda_2| \geq \ldots \geq   |\lambda_n|. 
$$

First of all

$$
   \norm{A\mathbf{u}_1} = \norm{\lambda_1\mathbf{u}_1} = |\lambda_1|,
$$

so  there is at least a unit vector of which the norm gets a factor $|\lambda_1|$.

It remains to show that for an arbitrary unit vector $\vect{x}$ always 

$$ 
 \norm{A\mathbf{x}} \leq 
|\lambda_1| \norm{\vect{x}} = |\lambda_1|.
$$

We will in fact show that  $\norm{A\mathbf{x}}^2 \leq 
|\lambda_1|^2$.

Since $\{\vect{u}_1, \ldots, \vect{u}_n \}$  is a basis  of $\R^n$  it follows that

$$
  \vect{x} = c_1\mathbf{u}_1 +  c_2\mathbf{u}_2 + \ldots +  c_n\mathbf{u}_n, \quad
  \text{for some } \enspace c_1,\ldots,c_n. 
$$

From the orthonormality of the $\vect{u}_i$ it follows that

$$
 1 = \norm{\vect{x}}^2  = \norm{c_1\mathbf{u}_1 +   \ldots + c_n\mathbf{u}_n}^2
 = c_1^2\norm{\mathbf{u}_1}^2 +   \ldots +  c_n^2\norm{\mathbf{u}_n}^2 = c_1^2 + \ldots + c_n^2,
$$

thus &nbsp; $c_1^2 + \ldots + c_n^2=1$.

Next, invoking that each $\vect{u}_i$ is an eigenvector for $\lambda_i$ and again that the $\vect{u}_i$ form an orthonormal set, we get

$$
\begin{array}{rcl}
\norm{A\vect{x}}^2 &=& \norm{c_1\lambda_1\vect{u}_1+ c_n\lambda_n\vect{u}_n}^2 \\
                   &=& c_1^2\lambda_1^2 \norm{\vect{u}_1}^2  + \ldots + c_n^2\lambda_n^2 \norm{\vect{u}_n}^2 \\
                   &=&
                   c_1^2\lambda_1^2   + \ldots + c_n^2\lambda_n^2 \\
                   &\leq & 
                   c_1^2\lambda_1^2   + \ldots + c_n^2\lambda_1^2  \\
                   &=& 
                   (c_1^2  + \ldots + c_n^2)\lambda_1^2 \\
                   &=& \lambda_1^2.
\end{array}
$$

At the $\leq$ step we used  that $\lambda_i^2 \leq \lambda_1^2$,  for  $i = 2, \ldots, n$.


::::




In the last subsection we will show how the orthogonal diagonalization can be rewritten in an interesting and meaningful way.

(SubSec:SymmetricMat:SpectralDecomp)=

## The Spectral Decomposition of a Symmetric Matrix.

Let's take up an earlier example ({prf:ref}`Ex:SymmetricMat:OrthDiag2x2`) to illustrate what the spectral decomposition is about.

::::{prf:example}
:label: Ex:SymmetricMat:SpectralDecomp

For the matrix $A = \begin{bmatrix} 1&2\\2&-2 \end{bmatrix}$ we found the orthogonal diagonalization

$$
 A = QDQ^T = \begin{bmatrix} 2/\sqrt{5}& 1/\sqrt{5}\\1/\sqrt{5}& -2/\sqrt{5} \end{bmatrix}
             \begin{bmatrix} 2 & 0 \\ 0 & -3 \end{bmatrix}
             \begin{bmatrix} 2/\sqrt{5}& 1/\sqrt{5}\\1/\sqrt{5}& -2/\sqrt{5} \end{bmatrix}^T.
$$

This is of the form

$$
  \begin{array}{rcl}
  A &=& [\,\mathbf{q}_1\,\,\mathbf{q}_2\,]\begin{bmatrix} 2 & 0 \\ 0 & -3 \end{bmatrix}
             \big[\,\mathbf{q}_1\,\,\mathbf{q}_2\,\big]^T =
     \big[\,2\mathbf{q}_1\,\,(-3)\mathbf{q}_2\big]\begin{bmatrix}\mathbf{q}_1^T \\ \mathbf{q}_2^T  \end{bmatrix}.
     \end{array}
$$

We bring in mind the column-row expansion of the matrix product. For two $2\times 2$ matrices this reads

$$
 \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}
 \begin{bmatrix} b_{11} &b_{12} \\ b_{21} & b_{22} \end{bmatrix} =
 \begin{bmatrix} a_{11} \\ a_{21} \end{bmatrix}
 \begin{bmatrix} b_{11} &b_{12}  \end{bmatrix}  +
 \begin{bmatrix} a_{12} \\ a_{22} \end{bmatrix}
 \begin{bmatrix} b_{21} &b_{22}  \end{bmatrix}.
$$

Applying this to the last expression for $A = QDQ^T$ we find

$$
  A = 2 \mathbf{q}_1\mathbf{q}_1^T + (-3)\mathbf{q}_2\mathbf{q}_2^T .
$$

The matrices

$$
   \mathbf{q}_1\mathbf{q}_1^T = \frac15 \begin{bmatrix} 4 & 2  \\ 2 & 1 \end{bmatrix}
   \quad \text{and} \quad
   \mathbf{q}_2\mathbf{q}_2^T = \frac15 \begin{bmatrix} 1 & -2  \\ -2 & 4 \end{bmatrix}
$$

represent the orthogonal projections onto the one-dimensional subspaces $\Span{\mathbf{q}_1}$ and $\Span{\mathbf{q}_2}$.

Furthermore these one-dimensional subspaces are orthogonal to each other.

So we have that this symmetric matrix can be written as a linear combination of matrices that represent orthogonal projections.
::::

The construction we performed in the last example can be generalized. Which is the content of the last theorem in this section.

::::{prf:theorem} Spectral Decomposition of Symmetric Matrices
:label: Thm:SymmetricMat:SpectralDecomp

Every $n \times n$ symmetric matrix $A$ is the linear combination

:::{math}
:label: Eq:SymmetricMat:SpectralDecomp

    A = \lambda_1P_1 +  \lambda_2P_2 + \ldots +  \lambda_nP_n

:::

of $n$ matrices $P_i$ that represent orthogonal projections onto one-dimensional subspaces that are mutually orthogonal.

Formula {eq}`Eq:SymmetricMat:SpectralDecomp` is referred to as being a **spectral decomposition** of the matrix $A$.
::::

::::{admonition} Proof of&nbsp;{prf:ref}`Thm:SymmetricMat:SpectralDecomp`
:class: tudproof

For a general $n\times n$ symmetric matrix $A$, there exists an orthogonal diagonalization

$$
   A = QDQ^{-1} = QDQ^{T}.
$$

Exactly as in {prf:ref}`Ex:SymmetricMat:SpectralDecomp` we can use the column-row expansion of the matrix product to derive

:::{math}
:label: Eq:SymmetricMat:SpectralDecomp2
  
A =  \lambda_1 \mathbf{q}_1\mathbf{q}_1^T + \lambda_2\mathbf{q}_2\mathbf{q}_2^T + \ldots + \lambda_n\mathbf{q}_n\mathbf{q}_n^T,

:::

where the vectors $\mathbf{q}_i$ of course are the (orthonormal) columns of the diagonalizing matrix $Q$. This is indeed a linear combination of orthogonal projections, as was to be shown.
::::

::::{exercise}

The eigenvalues of the matrix $A=\begin{bmatrix} 2 & 1 & 0 \\ 1 & 3 &  1\\ 0 & 1& 2 \end{bmatrix}$ are 1, 2 and 4.

Find the spectral decomposition of $A$.

::::

If in {prf:ref}`Thm:SymmetricMat:SpectralDecomp` the projections onto eigenvectors for the same eigenvalue are grouped together, then the following alternative form of the spectral decomposition results.

::::{prf:corollary} Spectral Theorem, alternative version
:label: Cor:SymmetricMat:SpectralThm-2

Every symmetric $n \times n$ matrix $A$ can be written as a linear combination of the orthogonal projections onto its (orthogonal) eigenspaces.

$$
   A = \lambda_1 P_1 + \, \ldots \, + \lambda_k P_k,
$$

where $P_i$ denotes the orthogonal projection onto the eigenspace $E_{\lambda_i}$.
::::

::::{admonition} Proof of&nbsp;{prf:ref}`Cor:SymmetricMat:SpectralThm-2`
:class: tudproof

We know that

$$
    A = \lambda_1P_1 +   \ldots +  \lambda_nP_n =
        \lambda_1\vect{q}_1\vect{q}_1^T +   \ldots +  \lambda_n\vect{q}_n\vect{q}_n^T.
$$

If all eigenvalues $\lambda_1, \ldots, \lambda_n$ are different that's just it.

If $\lambda_i$ is an eigenvalue of multiplicity $m$ with $m$ orthonormal eigenvectors
$\vect{q}_1, \ldots, \vect{q}_m$, then

$$
  \lambda_i\vect{q}_1\vect{q}_1^T + \,\ldots\,+ \lambda_i\vect{q}_m\vect{q}_m^T =
  \lambda_i [\,\vect{q}_1\,\,\cdots\,\,\vect{q}_m]  [\,\vect{q}_1\,\,\cdots\,\,\vect{q}_m]^T = \lambda_i Q_iQ_i^T.
$$

$P_i = Q_iQ_i^T$ is precisely the orthogonal projection onto the
eigenspace $E_{\lambda_i}$.
::::

The following example provides an illustration.

::::{prf:example}
For the matrix $A = \begin{bmatrix} 
     1 & 2 & 2 & 0 \\ 2 & -1 & 0 & 2 \\ 2 & 0 & -1 & -2 \\ 0 & 2 & -2 & 1
    \end{bmatrix}$ we had already found the orthogonal decomposition $A = QDQ^{-1}= QDQ^T$ with

$$
  Q = \left[\,\vect{q}_1\,\,\vect{q}_2\,\rule[-2ex]{0ex}{5ex}\,\vect{q}_3\,\,\vect{q}_4\,\right]
  =   \dfrac{1}{\sqrt{3}}\left[\begin{array}{cccc} 1 & 0 & 1 & 1 \\
                 -1 & 1 & 1 & 0 \\ -1 & -1 & 0 & 1 \\ 0 & -1 & 1 & -1
      \end{array} \right]
$$

and

$$
      D = \left[\begin{array}{cccc} -3 & 0 & 0 & 0 \\
       0 & -3 & 0 & 0 \\ 0 & 0 & 3 & 0\\ 0 & 0 & 0 & 3
                \end{array}\right].
$$

The spectral decomposition according to {prf:ref}`Cor:SymmetricMat:SpectralThm-2` then becomes

$$
   A = (-3) \left[\vect{q}_1\,\rule[-2ex]{0ex}{5ex}\,\vect{q}_2\,\right]\left[\vect{q}_1\,\rule[-2ex]{0ex}{5ex}\,\vect{q}_2\,\right]^T +
   3 \left[\vect{q}_3\,\rule[-2ex]{0ex}{5ex}\,\vect{q}_4\,\right]\left[\vect{q}_3\,\rule[-2ex]{0ex}{5ex}\,\vect{q}_4\,\right]^T = \,\,\ldots\,\,  =
$$

$$
  = (-3)\begin{bmatrix} 1/3 & -1/3 & -1/3 &   0 \\
                       -1/3 &  2/3 &   0  & -1/3 \\
                       -1/3 &   0  &  2/3 &  1/3 \\
                          0 & -1/3 &  1/3 &  1/3
  \end{bmatrix} +
      3 \begin{bmatrix} 2/3 &  1/3 &  1/3 &   0  \\
                        1/3 &  1/3 &   0  &  1/3 \\
                        1/3 &   0  &  1/3 & -1/3 \\
                          0 &  1/3 & -1/3 &  2/3
  \end{bmatrix}.
$$

::::


## Grasple Exercises


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f76823e6-8936-4edf-bd0b-fa3a2aa7246f?id=88040
:label: grasple_exercise_8_1_1
:dropdown:
:description: To check whether a matrix $A$ is symmetric.
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9828a4b4-98f7-46c3-8dab-74ac04fc1955?id=88032
:label: grasple_exercise_8_1_2
:dropdown:
:description: To check whether a matrix $A$ is orthogonal. And, if it is, to give its inverse.
::::
      

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8af926a0-80d8-459f-af55-c37a492a18c6?id=88045 
:label: grasple_exercise_8_1_3
:dropdown:
:description: To check whether a matrix $A$ is orthogonal. And, if it is, to give its inverse.
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/03d75a31-7e1b-4dd2-be0a-5e9a93a0ef09?id=94940  
:label: grasple_exercise_8_1_4
:dropdown:
:description: To give an orthogonal diagonalization of a (2x2) matrix.
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/926933aa-a33e-40f5-8e70-84bb9ed63fc8?id=87465
:label: grasple_exercise_8_1_5
:dropdown:
:description: To give an orthogonal diagonalization of a (2x2) matrix.
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9aac9c37-aa3b-4d5a-bb92-f00c09e5f052?id=94943
:label: grasple_exercise_8_1_6
:dropdown:
:description: To give an orthogonal diagonalization of a (3x3) matrix.
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a6a95823-15e4-4354-b89d-559306a5a7fa?id=94941
:label: grasple_exercise_8_1_7
:dropdown:
:description: To give an orthogonal diagonalization of a (3x3) matrix.
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/0403af25-edba-4bc6-b077-3de227253419?id=56931
:label: grasple_exercise_8_1_8
:dropdown:
:description: To give an orthogonal diagonalization of a (3x3) matrix.
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3a45e358-4898-4d1d-b6f4-ba9679dd13e0?id=87765
:label: grasple_exercise_8_1_9
:dropdown:
:description: To give an orthogonal diagonalization of a (3x3) matrix.
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/eb8b0e2f-d909-47ce-8ef1-50ad67e2b0f6?id=87905
:label: grasple_exercise_8_1_10
:dropdown:
:description: To give an orthogonal diagonalization of a (4x4) matrix.
::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5ce15529-61a7-43d0-9fd3-5ad5469618e8?id=89131 
:label: grasple_exercise_8_1_11
:dropdown:
:description: One step in an orthogonal diagonalization (as in the proof of the existence of an orthogonal diagonalization)  
::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5511e064-f22d-4601-9156-f00545d59f80?id=88649
:label: grasple_exercise_8_1_12
:dropdown: 
:description: Sequel to previous question, now for a 4x4 matrix.
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c994fa76-f723-4700-922b-2f05ff0ef822?id=87760
:label: grasple_exercise_8_1_13
:dropdown:
:description: To give an example of an symmetric 2x2 matrix with 1 eigenvalue and 1 eigenvector given.
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4fd8d027-0e63-46ec-aaf5-f2d10d8707c9?id=87038  
:label: grasple_exercise_8_1_14
:dropdown:
:description: To give an example of a 3x3 symm matrix with given eigenvalues and eigenspace.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/77b08679-8974-453a-8f68-7e08e8ecfaf5?id=94944 
:label: grasple_exercise_8_1_15
:dropdown:
:description: Deciding about the spectral decomposition of a 3x3 matrix (with  lot of prerequisites laid out).
::::

The following exercise have a more theoretical flavour.

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6e0ebf73-fba2-46d0-aaa8-44e53ea07e53?id=88034
:label: grasple_exercise_8_1_16 
:dropdown:
:description:  To think about  symmetric versus orthogonally diagonalizable. (true/false questions).
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/73c272d7-dbb0-47c9-8bee-074b1f8cc154?id=82845
:label: grasple_exercise_8_1_17
:dropdown:
:description: About the (non-)symmetry of  $A + A^T$  and  $A - A^T$.
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7959665f-09d0-4362-a0e8-c0a3e613399f?id=82848
:label: grasple_exercise_8_1_18
:dropdown:
:description: About the (non-)symmetry of  products.
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/33f5be5a-1cfa-4056-ac91-c2282de234b1?id=87864
:label: grasple_exercise_8_1_19
:dropdown:
:description: If $A$ and $B$ are symmetric, what about  $A^2$, $A^{-1}$  and $AB$?
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/59c4c327-1603-4cc1-8b92-7415c691098b?id=87873
:label: grasple_exercise_8_1_20
:dropdown:
:description:  True or false.  If $A$ is symmetric, then $A^2$ has nonnegative eigenvalues.  (and what if $A$ is not symmetric?).
::::