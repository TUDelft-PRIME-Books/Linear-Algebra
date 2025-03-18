(Sec:Gram-Schmidt)=

# The Gram-Schmidt Process

## Introduction

In Section {numref}`Sec:OrthoBase` we have seen that orthogonal bases are nice to work with. Both for finding coordinates and also for finding orthogonal projections.

In this section an algorithm is presented to construct an orthogonal basis from an arbitrary basis of a subspace $W$ in $\R^n$.

As a starter have a look at the following example

::::{prf:example}

Let $W$ be the subspace in $\R^3$ spanned by the two vectors $\vect{a}_1 = \begin{bmatrix} 2 \\ 1   \\3    \end{bmatrix}$ and $\vect{a}_2 = \begin{bmatrix} 3 \\ -2   \\1    \end{bmatrix}$.
We want to construct an orthogonal basis $\{\vect{b}_1,\vect{b}_2 \}$ for $W$.

For the first vector of this 'new' basis we can simply take $\vect{b}_1 = \vect{a}_1$.

As a second basis vector we can take

:::{math}
:label: Eq:GramSchmidt:Step2

  \vect{b}_2 = \vect{a}_2 - \text{proj}_{\vect{a}_1}(\vect{a}_2) = 
               \vect{a}_2 - \dfrac{\vect{a}_2\ip\vect{a}_1}{\vect{a}_1\ip\vect{a}_1}    \vect{a}_1.

:::

It is then clear that $\vect{b}_2$ is in span$\{\vect{a}_1, \vect{a}_2\}$, and by the property of the orthogonal projection $\text{proj}_{\vect{a}_1}(\vect{a}_2)$ it follows that $\vect{b}_2 \perp \vect{b}_1$.

A fortiori $\{\vect{b}_1, \vect{b}_2\}$ is linearly independent, so $\{\vect{b}_1, \vect{b}_2\}$ is an orthogonal basis for $W = \text{span}{\{\vect{a}_1, \vect{a}_2\}}$.

The explicit vectors we find are

$$
   \vect{b}_1 = \begin{bmatrix} 2 \\ 1   \\3    \end{bmatrix}, \quad
   \vect{b}_2 =  \begin{bmatrix} 3 \\ -2   \\1    \end{bmatrix} - \dfrac{7}{14}\begin{bmatrix} 2 \\ 1   \\3    \end{bmatrix} = \begin{bmatrix} 2 \\ -5/2   \\ -1/2    \end{bmatrix} =
   \dfrac{1}{2}\begin{bmatrix} 4 \\ -5   \\ -1    \end{bmatrix}
$$

If we prefer vectors without fractions, we can rescale the second vector, and then find the orthogonal basis

$$
  \{\vect{b}_1, 2\vect{b}_2\} = \left\{\begin{bmatrix} 2 \\ 1   \\3    \end{bmatrix},  \begin{bmatrix} 4 \\ -5   \\ -1    \end{bmatrix}  \right\}.
$$

::::

## The Gram-Schmidt process

::::{prf:theorem}
:label: Thm:GramSchmidt:GramSchmidt

Suppose $W$ is a subspace in $\R^n$ with basis $\{\vect{a}_1,\ldots,\vect{a}_m\}$. Construct the set of vectors
$\vect{b}_1,\ldots,\vect{b}_m$ according to the following rules

$$

  \begin{array}{lcl}
     \vect{b}_1 &=& \vect{a}_1 \\
     \vect{b}_2 &=& \vect{a}_2 - \dfrac{\vect{a}_2\ip\vect{b}_1}{\vect{b}_1\ip\vect{b}_1}\vect{b}_1 \\
     \vect{b}_3 &=& \vect{a}_3 - \dfrac{\vect{a}_3\ip\vect{b}_1}{\vect{b}_1\ip\vect{b}_1}\vect{b}_1  - \dfrac{\vect{a}_3\ip\vect{b}_2}{\vect{b}_2\ip\vect{b}_2}\vect{b}_2 \\
  \end{array}
$$

and in general

$$

    \vect{b}_{j+1} = \vect{a}_{j+1} - \dfrac{\vect{a}_{j+1}\ip\vect{b}_1}{\vect{b}_1\ip\vect{b}_1}\vect{b}_1  - \ldots - \dfrac{\vect{a}_{j+1}\ip\vect{b}_j}{\vect{b}_j\ip\vect{b}_j}\vect{b}_j,
$$

for $j = 1,2,\ldots, m-1$.

Then all along the way

$$

\{\vect{b}_1, \ldots, \vect{b}_j\}
$$

is an orthogonal basis for

$$

\text{span}\{\vect{a}_1, \ldots, \vect{a}_j\}.
$$

In particular, in the end $\{\vect{b}_1,\ldots,\vect{b}_m\}$
will be an orthogonal basis for $\text{span}\{\vect{a}_1, \ldots, \vect{a}_m\} = W$.

::::

The above construction/algorithm is called the **Gram-Schmidt process**.

::::{prf:example}
:label: Ex:GramSchmidt:Orthogonalize

Let $W$ be the defined as the span of the set $\left\{\begin{bmatrix} 1 \\ 1   \\ -1 \\ 1    \end{bmatrix}, \begin{bmatrix} 3 \\ 3   \\ -2 \\ 0    \end{bmatrix}, \begin{bmatrix} 3 \\ 1   \\ 4 \\ -4    \end{bmatrix}  \right\}$. It can be shown that these vectors are linearly independent.

We use the Gram-Schmidt algorithm to create an orthogonal basis for $W$.

%$$
%   (\vect{a}_1,\vect{a}_2,\vect{a}_3 ) = 
%   \left( 
%    \begin{bmatrix} 1 \\ 1   \\-1  \\1  \end{bmatrix},
%   \begin{bmatrix} 3 \\ 3   \\-2  \\0  \end{bmatrix}
%    \begin{bmatrix} 3 \\ 1   \\4  \\-4  \end{bmatrix}
%    \right).
%$$

Step by step we find

$$

  \vect{b}_1 = \vect{a}_1 = \begin{bmatrix} 1 \\ 1   \\-1  \\1  \end{bmatrix}, \quad
  \vect{b}_2 = \vect{a}_2 - \dfrac{\vect{a}_2\ip\vect{b}_1}{\vect{b}_1\ip\vect{b}_1}\vect{b}_1 =
  \begin{bmatrix} 3 \\ 3   \\-2  \\0  \end{bmatrix} -
  \dfrac{8}{4}\begin{bmatrix} 1 \\ 1   \\-1  \\1  \end{bmatrix}=
  \begin{bmatrix} 1 \\ 1   \\0  \\-2  \end{bmatrix}
$$

and

$$

\begin{array}{lcl}
  \vect{b}_3 &=& \vect{a}_3 - \dfrac{\vect{a}_3\ip\vect{b}_1}{\vect{b}_1\ip\vect{b}_1}\vect{b}_1  - \dfrac{\vect{a}_3\ip\vect{b}_2}{\vect{b}_2\ip\vect{b}_2}\vect{b}_2 \\
  &=&
  \begin{bmatrix} 3 \\ 1   \\4  \\-4  \end{bmatrix} -
  \dfrac{-4}{4}\begin{bmatrix} 1 \\ 1   \\-1  \\1  \end{bmatrix} -
  \dfrac{12}{6}\begin{bmatrix} 1 \\ 1   \\0  \\-2  \end{bmatrix} = \begin{bmatrix} 2 \\ 0   \\3  \\1  \end{bmatrix}
  \end{array}
$$

Check for yourself that the vectors $\vect{b}_1,\vect{b}_2, \vect{b}_3$ are indeed orthogonal.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Thm:GramSchmidt:GramSchmidt`
:class: tudproof

Let $W_j$ be the subspace spanned by the first $j$ vectors $\vect{a}_1, \ldots, \vect{a}_j$, for $j = 1,2\ldots,m$.

First of all

$$

 \text{span}\{\vect{b}_1\} = W_1 = \text{span}\{\vect{a}_1\}.
$$

In the other steps, assume that we have so far created the orthogonal basis
$\{\vect{b}_1, \ldots,\vect{b}_j \}$ for $W_j$.

Then in fact

$$

 \vect{b}_{j+1} = \vect{a}_{j+1} - \text{proj}_{W_j}(\vect{a}_{j+1}).
$$

Namely, the projection $\text{proj}_{W_j}(\vect{a}_{j+1})$ can be computed using the already created _orthogonal_ basis
$(\vect{b}_1, \ldots, \vect{b}_j)$ of $W_j$. See {numref}`Figure %s <Fig:GramSchmidt:GS-step123>`

:::{figure} Images/Fig-GramSchmidt-GS-step123.svg
:name: Fig:GramSchmidt:GS-step123
:class: dark-light

First steps in the Gram-Schmidt process.
:::

That is,

$$

  \text{proj}_{W_j}(\vect{a}_{j+1}) =
  \dfrac{\vect{a}_{j+1}\ip\vect{b}_1}{\vect{b}_1\ip\vect{b}_1}\vect{b}_1  + \ldots + \dfrac{\vect{a}_{j+1}\ip\vect{b}_j}{\vect{b}_j\ip\vect{b}_j}\vect{b}_j.
$$

This makes $\text{proj}_{W_j}(\vect{a}_{j+1})$    an element of $W_{j}$  and 
$\vect{b}_{j+1} = \vect{a}_{j+1} - \text{proj}_{W_j}(\vect{a}_{j+1})$  an element of
$W_{j+1}$.    

$\vect{b}_{j+1} \neq \vect{0}$ since we assumed that the vectors $\vect{a}_1, \ldots, \vect{a}_m$ are independent, so $\vect{a}_{j+1}$ is not in $W_j$.

Moreover, $\vect{b}_{j+1} = \vect{a}_{j+1} - \text{proj}_{W_j}(\vect{a}_{j+1})$ is perpendicular to $W_j$ by the properties of orthogonal projection.
Since all $\vect{b}_i$ with $i \leq j$ lie in $W_j$, this makes $\vect{b}_{j+1}$ orthogonal to all its predecessors $\vect{b}_1, \ldots, \vect{b}_j$.  
Hence if the vectors $\vect{b}_1, \ldots, \vect{b}_j$ are orthogonal,
so are the vectors $\vect{b}_1, \ldots, \vect{b}_j, \vect{b}_{j+1}$.

(By using mathematical induction the proof can be made absolutely rigorous.)

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bb336bca-f300-48ba-8744-e38ad3a7bcd0?id=87814
:label: grasple_exercise_7_3_A
:dropdown:
:description: Gram-Schmidt D.I.Y.

::::

The following example shows what happens if the Gram-Schmidt construction is applied to
a subspace $W = \text{span}\{\vect{a}_1, \ldots, \vect{a}_m\}$ where the vectors $\vect{a}_i$ are not linearly independent.

::::{prf:example}
:label: Ex:GramSchmidt:NonOrthog

Let $W$ be the defined as the span of the set $\left\{\begin{bmatrix} 1 \\ -1   \\ 2 \\ 3    \end{bmatrix}, \begin{bmatrix} 2 \\ -2   \\ 4 \\ 6    \end{bmatrix}, \begin{bmatrix} 2 \\ 0   \\ 1 \\  2    \end{bmatrix}, \begin{bmatrix} 0 \\ 2  \\ -3 \\  -4    \end{bmatrix} \right\}$.

Let us denote the vectors by $\vect{a}_1, \ldots, \vect{a}_4$. As in the proof of the Gram-Schmidt process
we use the notation $W_j$ for the span of the vectors $ \vect{a}_1, \ldots, \vect{a}_j$.

Just following the protocol we find

$\vect{b}_1 = \vect{a}_1 = \begin{bmatrix} 1 \\ -1   \\ 2 \\ 3    \end{bmatrix},  \quad
      \vect{b}_2 =   \vect{a}_{2} - \dfrac{\vect{a}_{2}\ip\vect{b}_1}{\vect{b}_1\ip\vect{b}_1}\vect{b}_1        = \begin{bmatrix} 0 \\ 0   \\ 0 \\ 0    \end{bmatrix}$.

The explanation is that $\vect{b}_2 = \vect{a}_{2} - \text{proj}_{\vect{a}_1}(\vect{a}_2) =
\vect{a}_{2} - \vect{a}_{2} = \vect{0}$, since $\vect{a}_2$ lies in span$\{\vect{a}_1\}$.
In other words, since $W_2 = W_1$.

We discard the zero vector, and continu to compute the next new basis vector.

$$
 \vect{b}_3 = \vect{a}_3 - \text{proj}_{W_2}(\vect{a}_3) = \vect{a}_3 - \text{proj}_{W_1}(\vect{a}_3)
 =  \begin{bmatrix} 2 \\ 0   \\ 1 \\  2    \end{bmatrix} - \dfrac{10}{15}\begin{bmatrix} 1 \\ -1   \\ 2 \\ 3    \end{bmatrix} = \dfrac13 \begin{bmatrix} 4 \\ 2   \\ -1 \\  0    \end{bmatrix}.
$$

To get rid of fractions we rather continue with $\vect{b}_3 = \begin{bmatrix} 4 \\ 2   \\ -1 \\  0    \end{bmatrix}$.

The last step:

$$
  \vect{b}_4 = \vect{b}_4 - \text{proj}_{\text{span}\{\vect{b}_1, \vect{b}_3\}}
             = \vect{b}_4 - \dfrac{-10}{15}\vect{b}_1 -\dfrac{7}{21}\vect{b}_3 = \vect{0}.
$$

Here again we may conclude that $\vect{a}_4$ lies in span$\{\vect{b}_1,\vect{b}_3\}$, and we
discard $\vect{b}_4$ from our basis.

The conclusion is that

$$
 \left\{\vect{b}_1,\vect{b}_3\right\} = \left\{\begin{bmatrix} 1 \\ -1   \\ 2 \\ 3    \end{bmatrix},
          \begin{bmatrix} 4 \\ 2   \\ -1 \\ 0    \end{bmatrix}\right\}
$$

is an orthogonal basis for span$\{\vect{a}_1,\ldots, \vect{a}_4\}$.

::::

%::::{prf:remark}
%:label: Exc:GramSchmidt:NonBasis

The idea of {prf:ref}`Ex:GramSchmidt:NonOrthog` can be generalized as follows.
Suppose $W = \text{span}\{\vect{a}_1,\ldots,\vect{a}_m\}$, where the vectors $\vect{a}_i$ are not
necessarily linearly independent.
If we apply the Gram-Schmidt construction and discard the zero vector if it comes up, then we end up with an orthogonal basis $\{\vect{b}_1,\ldots,\vect{b}_k\}$ for $W$. Note that $k < m$ occurs precisely when the original generating set of vectors $\{\vect{a}_1,\ldots,\vect{a}_m\}$ is linearly dependent.

%::::

::::{prf:remark}
:label: Rem:GramSchmidt:OrthonormalBasis

By applying the Gram-Schmidt process to a linearly independent set of vectors $\{\vect{a}_1,\ldots,\vect{a}_m\}$ we get a orthogonal basis $\{\vect{b}_1,\ldots,\vect{b}_m\}$ for the subspace $W =  \text{span}\{\vect{a}_1,\ldots,\vect{a}_m\}$.

By rescaling the vectors $\vect{b}_i$ as follows

$$

   \vect{q}_i = \dfrac{\vect{b}_i }{\norm{\vect{b}_i}}, \quad  i = 1, \ldots , m
$$

we can turn this new basis into an **orthonormal** basis.

::::

::::{prf:example}
:label: Ex:GramSchmidt:Orthonormalize
For the subspace

$$

W = \text{span}
\left(
    \begin{bmatrix} 1 \\ 1   \\-1  \\1  \end{bmatrix},
    \begin{bmatrix} 3 \\ 3   \\-2  \\0  \end{bmatrix}
    \begin{bmatrix} 3 \\ 1   \\4  \\-4  \end{bmatrix}
    \right).
$$

we found, in {prf:ref}`Ex:GramSchmidt:Orthogonalize`, the orthogonal basis

$$
   \left\{\begin{bmatrix} 1 \\ 1   \\-1  \\1   \end{bmatrix}, \begin{bmatrix} 1 \\ 1 \\0 \\-2  \end{bmatrix},   \begin{bmatrix} 2 \\ 0   \\3  \\1  \end{bmatrix}\right\}.
$$

Rescaling (or normalizing) gives the orthonormal basis

$$

   \left\{ \dfrac{1}{2}\begin{bmatrix} 1 \\ 1   \\-1  \\1   \end{bmatrix}, \quad \dfrac{1}{\sqrt{6}}\begin{bmatrix} 1 \\ 1 \\0 \\-2  \end{bmatrix},   \quad  \dfrac{1}{\sqrt{14}}\begin{bmatrix} 2 \\ 0   \\3  \\1  \end{bmatrix}\right\}.
$$

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/40c42331-9c9f-45ca-b498-83a8ba884a57?id=87816
:label: grasple_exercise_7_3_B
:dropdown:
:description: Finding an orthonormal basis.

::::

(Sec:Gram-Schmidt:QRdecomp)=

## The QR decomposition

The Gram-Schmidt process leads to the following interesting decomposition of an $n \times m$ matrix $A$ with linearly independent columns.

::::{prf:theorem} QR decomposition
:label: Thm:GramSchmidt:QR-decomp

Suppose $A$ is an $n \times m$ matrix of rank $m$.
Then $A$ can be written as

$$

   A = QR,
$$

where $Q$ is an $n \times m$ matrix with _orthonormal columns_, and $R$ is an _upper triangular_ $m \times m$ matrix, with *positive* diagonal entries.

The matrix $Q$ is found by applying the Gram-Schmidt process to the (linearly independent) columns $\vect{a}_1,\ldots,\vect{a}_m$ of the matrix $A$ and then renormalizing.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Thm:GramSchmidt:QR-decomp`
:class: tudproof

One way to see this, is to look at the creation of the orthonormal set $\{\vect{q}_1,\ldots,\vect{q}_m\}$
from the linearly independent set $\{\vect{a}_1,\ldots,\vect{a}_m\}$.

The general step in the Gram-Schmidt process is of the form

$$

 \vect{b}_{j+1} = \vect{a}_{j+1} - \dfrac{\vect{a}_{j+1}\ip\vect{b}_1}{\vect{b}_1\ip\vect{b}_1}\vect{b}_1  - \ldots - \dfrac{\vect{a}_{j+1}\ip\vect{b}_j}{\vect{b}_j\ip\vect{b}_j}\vect{b}_j.
$$

Realizing that each $\vect{b}_i$ is in the span
of $\{\vect{a}_1, \vect{a}_2, \ldots , \vect{a}_{i} \}$,

it follows that

$$

  \begin{array}{ccl}
   \vect{b}_1 &=& \rule{1em}{0ex}\vect{a}_1 \\
   \vect{b}_2 &=&   c_{12}\vect{a}_1 + \vect{a}_2 \\
   \vect{b}_3 &=&   c_{13}\vect{a}_1 + c_{23}\vect{a}_2 + \vect{a}_3\\
    \vdots &=& \quad \vdots
  \end{array}
$$

so

$$

  B = [\vect{b}_1\,\,\vect{b}_2\,\,\ldots\,\,\vect{b}_m]  =
    [\vect{a}_1\,\,\vect{a}_2\,\,\ldots\,\,\vect{a}_m]
  \begin{bmatrix} 1 & c_{12} & c_{13} & \ldots & c_{1m} \\
  0 & 1 & c_{23} & \ldots & c_{2m} \\
  0 & 0 & 1 & \ldots & c_{3m} \\
  \vdots & \vdots &  & \ddots &  \\
  0 & 0 & 0 & \ldots & 1
   \end{bmatrix} = AC.
$$

Normalizing the vectors $\vect{b}_i$ can be seen as multiplying the matrix $B$ with a diagonal matrix $D$:

$$

   Q = [\vect{q}_1\,\,\vect{q}_2\,\,\ldots\,\,\vect{q}_m]  =  BD,
$$

where the diagonal entries $d_{ii}$ of $D$ are given by

$$

    d_{ii} = \dfrac{1}{\norm{\vect{b}_i}}.
$$

So

$$

  Q = BD = ACD = A(CD),
$$

where $CD$ is an upper triangular matrix with positive diagonal entries.

Multiplying both sides with the inverse of $CD$ gives

$$

  Q = A(CD) \iff A = Q(CD)^{-1} = QR,
$$

where $R = (CD)^{-1}$ is still an upper triangular matrix with positive diagonal entries.

::::

There is an quicker way to find the matrix $R$ than by inverting the matrix $CD$ as in the proof of {prf:ref}`Thm:GramSchmidt:QR-decomp`, which is the context of the next proposition.

::::{prf:proposition}
:label: Prop:GramSchmidt:QR-quick

Let $Q = [\vect{q}_1,\ldots,\vect{q}_m]$ be the matrix constructed by exactly applying the Gram-Schmidt process followed by rescaling. Define $R = Q^TA$.

Then $R$ is an upper triangular matrix with a positive entries on its diagonal, and

$$

  A = QR.
$$

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:GramSchmidt:QR-quick`
:class: tudproof

We know that for the matrix $Q$ as specified the decomposition

$$

  A = QR
$$

exists, with an upper triangular matrix $R$.

The matrix $Q$ has orthonormal columns, so

$$

 Q^TQ = I.
$$

Thus we can retrieve $R$ if we multiply both sides of the equation $\,A = QR\,$ by $\,Q^T$:

$$

  A = QR  \quad \Longrightarrow \quad  Q^TA = Q^TQR = R.
$$

::::

The following example provides an illustration of this last proposition.

::::{prf:example}

Consider the matrix

$$
A= \begin{bmatrix}
  1 & 3 & 3\\
  1 & 3 & 1\\
  -1 &-2 & 4  \\
  1 & 0 &-4
\end{bmatrix}.
$$

From {prf:ref}`Ex:GramSchmidt:Orthogonalize` and
{prf:ref}`Ex:GramSchmidt:Orthonormalize`
we know that applying the Gram-Schmidt process to the columns of $A$
leads to the matrix

$$
 Q = \begin{bmatrix}
        \dfrac{1}{2} & \dfrac{1}{\sqrt{6}} & \dfrac{2}{\sqrt{14}}\\
        \dfrac{1}{2} & \dfrac{1}{\sqrt{6}} & 0\\
        -\dfrac{1}{2} & 0 & \dfrac{3}{\sqrt{14}}\\
        \dfrac{1}{2} &-\dfrac{2}{\sqrt{6}} & \dfrac{1}{\sqrt{14}}
      \end{bmatrix}.
$$

We compute $R = Q^TA$

$$
 \begin{bmatrix}
        \dfrac{1}{2} & \dfrac{1}{2} & -\dfrac{1}{2} & \dfrac{1}{2} \\
        \dfrac{1}{\sqrt{6}} &\dfrac{1}{\sqrt{6}} &  0 & -\dfrac{2}{\sqrt{6}} \\
        \dfrac{2}{\sqrt{14}} & 0  & \dfrac{3}{\sqrt{14}} & \dfrac{1}{\sqrt{14}}
      \end{bmatrix}
      \begin{bmatrix}  1 & 3 & 3\\
                       1 & 3 & 1\\
                      -1 &-2 & 4  \\
                       1 & 0 &-4 \end{bmatrix}
       =
      \begin{bmatrix}  2 & 4 & -2\\
                       0 & \sqrt{6} & 2\sqrt{6}\\
                       0 & 0 & \sqrt{14}  \end{bmatrix},
$$

and see that this is indeed an upper triangular matrix (with positive diagonal entries).

You may check for yourself that $QR = A$.

::::

::::{exercise}
:label: Exc:GramSchmidt:AlternativeProofQR

Fill in the details of the following more direct proof of the quick way to find $QR$-decomposition.

Let $Q$ be the matrix coming from the Gram-Schmidt process, followed by rescaling.

Since by construction

$$
  \vect{q}_i \perp \text{span}\{\vect{q}_1,\ldots,\vect{q}_{i-1}\} = \text{span}\{\vect{a}_1,\ldots,\vect{a}_{i-1}\}
$$

it follows that the entries below the diagonal of the product $Q^TA$ are all equal to zero.
So: $Q^TA = R$ is an upper triangular matrix.

Recalling the construction of $\vect{b}_i$ and $\vect{q}_i$ from $\vect{a}_1,\ldots,\vect{a}_i$, it can be shown that the diagonal entries $r_{ii}$ are equal to $\vect{q}_i^T\vect{a}_i = \norm{\vect{a}_i} > 0$.

Furthermore, since the columns of $Q$ form an orthonormal basis of $\text{Col}\,{A}$, the matrix
$QQ^T$ represents the orthogonal projection onto $\text{Col}\,A$. Use this to show that
$QQ^TA = A$.

Warning: the columns of $Q$ being orthonormal is equivalent to $Q^TQ = I$. However, in the case where $Q$ is not a square matrix, this does not imply that $QQ^T = I$.

::::

## Grasple Exercises

The first exercises are about applying the Gram-Schmidt (GS) algorithm

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b07d879b-8d64-401d-9175-c346d4cbab9e?id=87823
:label: grasple_exercise_7_3_1
:dropdown:
:description: Performing one step in the Gram-Schmidt process.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6fd2eb99-c2be-4bc2-887b-1c0bfccbdcf9?id=87837
:label: grasple_exercise_7_3_2
:dropdown:
:description: Applying the Gram-Schmidt process for two vectors in $\R^3$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/15070d4c-f241-423d-a0af-3f1b4b57a397?id=87828
:label: grasple_exercise_7_3_3
:dropdown:
:description: Applying Gram-Schmidt for two vectors in $\R^4$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/eb46b234-d281-4d02-a92c-d0c4575ffe9c?id=87825
:label: grasple_exercise_7_3_4
:dropdown:
:description: Applying the Gram-Schmidt process for three vectors in $\R^4$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/63090a52-ba10-4881-b9c2-35ae64e79ffd?id=87827
:label: grasple_exercise_7_3_5
:dropdown:
:description: Orthogonal basis for span$\{\mathbf{a}_1, \mathbf{a}_2,\mathbf{a}_3\}$ in $\R^3$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/81e5b0f8-9d1a-4ff7-973f-e8b8cb84d42f?id=87838
:label: grasple_exercise_7_3_6
:dropdown:
:description: Finding an orthonormal basis for span$\{\mathbf{a}_1, \mathbf{a}_2\}$ in $\R^3$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6d39de25-aeaa-4ed0-8abd-7e98f4a0ef15?id=87705
:label: grasple_exercise_7_3_7
:dropdown:
:description: Applying Gram-Schmidt for three vectors in $\R^4$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/11b3cc56-0c2d-4ea8-b5ef-e5f26d58f362?id=87741
:label: grasple_exercise_7_3_8
:dropdown:
:description: Applying Gram-Schmidt for three vectors in $\R^5$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/319f882b-8498-492b-a97c-c1ce346a66f8?id=57189
:label: grasple_exercise_7_3_9
:dropdown:
:description: Finding the QR-decomposition of a $2\times2$ matrix.

::::


The following exercises are about the QR decomposition

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/98d48efb-0be6-4dee-a905-55dff061ce17?id=90209
:label: grasple_exercise_7_3_10
:dropdown:
:description: Finding the QR-decomposition of a $3\times2$ matrix.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d4466fcf-11be-4578-ac9e-3a570710a154?id=87629
:label: grasple_exercise_7_3_11
:dropdown:
:description: Finding the QR-decomposition of a $3\times3$ matrix.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b7be453d-4fd1-4c41-a3be-72e909ed0220?id=87646
:label: grasple_exercise_7_3_12
:dropdown:
:description: Finding the QR-decomposition of a $3\times3$ matrix.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2f957bf7-b1f1-424f-ad39-57af14cd1d86?id=87820
:label: grasple_exercise_7_3_13
:dropdown:
:description: Finding the QR-decomposition of a $4\times3$ matrix.

::::

The last exercises are more conceptual than computational.

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fb9adc06-f068-4c5b-96ac-575415620c82?id=87821
:label: grasple_exercise_7_3_14
:dropdown:
:description: T/F question about properties of Gram Schmidt process.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8a85a120-ef0c-41ec-9f60-ca492a35865a?id=87822
:label: grasple_exercise_7_3_15
:dropdown:
:description: From orthogonal to orthonormal.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c02e84cd-aa51-4d2a-8585-0cd56fa08ec6?id=87824  
:label: grasple_exercise_7_3_16
:dropdown:
:description: What about GS for a linearly dependent set?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/581f5f1d-cf12-4358-932f-70f65e4341b4?id=87829
:label: grasple_exercise_7_3_17
:dropdown:
:description: GS for set of linearly dependent set of vectors.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/12bda5c2-8ec2-44b2-b5c6-ec2cc4bb71d0?id=87841
:label: grasple_exercise_7_3_18
:dropdown:
:description: To build an orthogonal basis for the column space of a matrix.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a8741f26-64c7-4245-839a-8c5131bea496?id=87742
:label: grasple_exercise_7_3_19
:dropdown:
:description: Ponderings about the QR-decomposition (of a $4 \times 2$ matrix $A$).

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/24a2c96f-0618-4a90-8229-ce04b1dd4640?id=87747
:label: grasple_exercise_7_3_20
:dropdown:
:description: How many QR-decompositions are there for an $m \times n$ matrix?

::::
