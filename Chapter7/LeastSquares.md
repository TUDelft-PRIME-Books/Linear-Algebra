(Sec:LeastSquares)=

# Least Squares Solutions

(SubSec:LeastSquares:Introduction)=

## Introduction

In Chapter 2, especially {numref}`Section %s <Section:LinSystems>`, we studied linear systems. One way to write them down was as a matrix-vector equation $A\vect{x} = \vect{b}$. We saw that a linear system could be either consistent or inconsistent. And if a system was inconsistent, that would then be the end of the story.

In this section we will reconsider the inconsistent situation and ask ourselves the question whether there is a vector $\vect{x}$ that is in a sense the 'best possible' alternative to a solution.

One common situation where an inconsistent linear system arises quite naturally is fitting a line through a set of points.
Suppose $n \geq 3$ points $(x_1,y_1), \ldots, (x_n,y_n)$ in the plane are given.
Which line $\ell: y = ax + b$ best fits this set of points?

There are different ways to define what is the _best_ line. For instance, we may mean the line that minimizes the sum of the (perpendicular) distances of the points to the line. From a purely geometric point of view that seems the most natural way.
Or, we can take the line for which the sum of vertical distances from the points to the line, i.e.,

$$
  S = \sum_{i=1}^{n} |y_i - (a + bx_i)|
$$

is minimal. This approach makes sense in a physicial context where typically the $x$-variable may be an input variable over which a researcher has control, and $y$ is some output variable which may be liable to fluctuations and/or uncertainties.
See {numref}`Figure %s <Fig:LeastSquares:BestLines>` for both interpretations of 'best' line.

```{applet}
:url: leastsquares/bestlines_split_canvas
:fig: Images/Fig-LeastSquares-BestLines.svg
:name: Fig:LeastSquares:BestLines
:class: dark-light

What is the best best line? Can you get the total distance in the left picture below 6.5? Can you get the total distance in the right picture below 9.0 ?
```

Both are sensible ideas. However, to turn any of these two ideas into an algorithm to find the best line is not as straightforward as the computations that come up if we put the question into the realm of linear algebra.
And there it will turn out to be the problem of an inconsistent linear system.

Ideally there are parameters $a$ and $b$ such that the line with the equation

$$
    y = ax + b
$$

contains all points $(x_i,y_i)$.

That means that all equations

$$
   \left\{\begin{array}{ccc}
                     y_1 &=& ax_1 + b \\
                     y_2 &=& ax_2+ b \\
                      \vdots & & \vdots \\
                      y_n &=& ax_n + b \\
                     \end{array}\right.
$$

will be satisfied simultaneously. This only happens if the matrix-vector equation

:::{math}
:label: Eq:LeastSquares:Linefit

\left[\begin{array}{cc}
1 & x_1 \\ 1 & x_2 \\ \vdots & \vdots \\ 1 & x_n
\end{array}\right]
\left[\begin{array}{c}
a \\ b
\end{array}\right] =
\left[\begin{array}{c}
y_1 \\ y_2 \\ \vdots \\ y_n
\end{array}\right]
:::

is consistent. Which generally is not the case.

We will come back to this question in {numref}`Subsection %s <SubSec:LeastSquares:LinearModels>`.

(SubSec:LeastSquares:LS-solutions)=

## Least Squares Solutions

Let $A$ be an $m \times n$ matrix with columns $\vect{a}_1, \ldots, \vect{a}_n$.
<BR>
We have seen ({numref}`Section %s <Sec:MatVecProduct>`, {prf:ref}`Rem:MatVecProd:EquivalentEquations`) that the linear system

$$
  A\vect{x} = \vect{b}
$$

is equivalent to the vector equation

$$
  x_1\vect{a}_1 + \ldots + x_1\vect{a}_n = \vect{b}.
$$

What we can do if the linear system is inconsistent, thus if

$$
  \vect{b} \notin \Span{\vect{a}_1, ... , \vect{a}_n},
$$

is try to find the _best approximation_ of the vector $\vect{b}$ with a vector in
$\Span{\vect{a}_1, ... , \vect{a}_n}$. This is the idea behind the following definition.

::::{prf:definition}

Let $A$ be an $m\times n$ matrix and $\vect{b}$ a vector in $\R^{m}$.
A vector $\hat{\vect{x}}$ is called a **least squares solution** of the linear system $A\vect{x} = \vect{b}$ if for every $\vect{x}$ in $\R^n$ the inequality

$$
   \norm{A\hat{\vect{x}} - \vect{b}} \leq \norm{A\vect{x} - \vect{b}}
$$

holds.

The vector $ A\hat{\vect{x}} - \vect{b} $ is called the vector of the **errors**, and the norm of this vector, i.e.,

$$
    \norm{A\hat{\vect{x}} - \vect{b}}
$$

is called the **least squares error**.

::::

::::{prf:example}
:label: Ex:LeastSquares:4x3Example

Consider the linear system $A\vect{x} = \vect{b}$, with

$$
A = \left[\begin{array}{ccc}
         1 & 2 & 1  \\ 2 & 1 & 1  \\ 3 & 2 & 4 \\ 2 & 1 & 3
       \end{array}\right], \quad \vect{b} =
       \left[\begin{array}{c}  20 \\ 20 \\ 40 \\ 30 \end{array}\right].
$$

For the trial solution $x_1 = 5, x_2 = 4, x_3 = 5$, the error vector and its norm are computed as

$$
  \vect{v} = \left[\begin{array}{ccc}
         1 & 2 & 1  \\ 2 & 1 & 1  \\ 3 & 2 & 4 \\ 2 & 1 & 3
       \end{array}\right] \left[\begin{array}{c}  5 \\ 4 \\ 5 \end{array}\right] - \left[\begin{array}{c}  20 \\ 20 \\ 40 \\ 30 \end{array}\right]
       =  \left[\begin{array}{c}  18 \\ 19 \\ 43 \\  29 \end{array}\right] - \left[\begin{array}{c}  20 \\ 20 \\ 40 \\ 30 \end{array}\right] =
       \left[\begin{array}{c}  -2  \\ -1 \\ 3 \\ -1 \end{array}\right]
$$

and

$$
    \norm{\vect{v}} = \sqrt{15}.
$$

::::

::::{prf:remark}
:label: Rem:LeastSquares:BestLinComb

By definition $A\hat{\vect{x}} = \hat{x}_1\vect{a}_1  + \ldots + \hat{x}_n\vect{a}_n$ is the best approximation of $\vect{b}$ with vectors in $\Span{\vect{a}_1, ... , \vect{a}_n}$.

By minimizing $\norm{A\vect{x} - \vect{b}}$ we are in fact minimizing the sum of the squares of the errors. This explains the name _least squares error_.

From

$$
   \norm{A\hat{\vect{x}} - \vect{b}} = \norm{\hat{x}_1\vect{a}_1 + \ldots +  \hat{x}_n\vect{a}_n - \vect{b}}
$$

we read off that a least squares solution yields a linear combination of the columns of $A$ that has a minimal distance to $\vect{b}$.

For a _consistent_ linear system a least squares solution will be an actual solution,
i.e. $A\hat{\vect{x}} - \vect{b} = \vect{0}$. In this case the least squares error

$$
  \norm{A\hat{\vect{x}} - \vect{b}} =\norm{\vect{b} - \vect{b}} =\norm{\vect{0}}
$$

will be zero.
::::

::::{prf:remark}
:label: Rem:LeastSquares:Linefit

In the situation where we want to fit a line $y = ax + b$, we can take as 'best' parameters the _least squares_ solution of the linear system as in Equation
{eq}`Eq:LeastSquares:Linefit`,

$$
  \left[\begin{array}{cc}
        1 & x_1 \\ 1 & x_2 \\ \vdots & \vdots \\ 1 & x_n
       \end{array}\right]
       \left[\begin{array}{c}
        a \\ b
       \end{array}\right] =
        \left[\begin{array}{c}
        y_1 \\ y_2 \\  \vdots \\ y_n
       \end{array}\right].
$$

The interpretation of the 'error vector' $A\vect{x} - \vect{b}$ then becomes

$$
   \left[\begin{array}{c}
        a+bx_1 - y_1 \\ a+bx_2 - y_2 \\ \vdots  \\ a+bx_n - y_n
       \end{array}\right]
$$

and the error $\norm{A\vect{x} - \vect{b}}$ comes down to

$$
  \sqrt{ \big(y_1 - (ax_1+b)\big)^2 + \ldots + \big(y_n - (ax_n+b)\big)^2}.
$$

The least squares solution $(\hat{a},\hat{b})$ minimizes this error, so in fact it minimizes the sum of the squares

$$
   \sum_{i=1}^{n}  \big(y_i - (ax_i+b)\big)^2.
$$

::::

The questions we will address are

<ol type ="i">
<li>

Does a least squares solution always _exist_?

</li>

<li>

How to _compute_ the least squares solution(s)?

</li>

<li>

If a least squares solution exists, is it _unique_?

</li>

</ol>

The next proposition provides the answers to question i. and question iii.

::::{prf:proposition}
:label: Prop:LeastSquares:Existence

For each linear system $A\vect{x} = \vect{b}$, where $A$ is an $m \times n$ matrix and $\vect{b}$ a vector in $\R^m$, a least squares solution always exists. Moreover the least squares solution is unique if and only if the columns of $A$ are linearly independent.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:LeastSquares:Existence`
:class: tudproof

In {prf:ref}`Rem:LeastSquares:BestLinComb` it was noted that a least squares solution corresponds to the vector in Col $A$ that is closest to $\vect{b}$.

The vector in Col $A$ that is closest to $\vect{b}$ is precisely the orthogonal projection of $\vect{x}$ onto Col $A$. (See {prf:ref}`Prop:Orthogonality:BestApprox`.)

This projection, a linear combination of the colums of $A$, always exists.

The coefficients of this linear combination then give a least squares solution.

Lastly, these coefficients are unique if and only if the columns of $A$ are linearly independent.

::::

::::{margin}

:::{admonition} {prf:ref}`Thm:OrthoBase:OrthoDecomp`.
:class: theorem

Let $V$ be a subspace of $\R^{n}$ and let $\vect{v}_{1},...,\vect{v}_{k}$ be an orthogonal basis for $V$. For any $\vect{w}$ in $\R^{n}$, the _orthogonal projection_ of $\vect{w}$ on $V$ is given by

$$\proj_{V}(\vect{w})=\frac{\vect{w}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\cdots +\frac{\vect{w}\ip\vect{v}_{k}}{\vect{v}_{k}\ip\vect{v}_{k}}\vect{v}_{k}.$$

::::

::::{prf:example}
:label: Ex:LeastSquares:OrthogExample

Find the least squares solution of the linear system

$$
  \left\{       \begin{array}{ccccccc}
        x_1 &+&  x_2  &=& 9 \\
        2x_1 &-& 2x_2 &=& 7 \\
        3x_1 &+& x_2 &=& 11
       \end{array}
  \right.
$$

According to {prf:ref}`Prop:LeastSquares:Existence` the least squares solution consists of the coefficients of the orthogonal projection of the vector
$
  \vect{b} = \left[ \begin{array}{c} 9 \\ 7 \\ 11 \end{array}   \right]
$
onto $\Span{\vect{a}_1, \vect{a}_2} = \Span{\left[ \begin{array}{c} 1 \\ 2 \\ 3 \end{array}   \right], \left[ \begin{array}{c} 1 \\ -2 \\ 1 \end{array} \right]}$.

In this first example we have chosen $\vect{a}_1$ and $\vect{a}_2$ that are _orthogonal_.

So by the projection formula for an orthogonal basis (see {prf:ref}`Thm:OrthoBase:OrthoDecomp`, see side note), the projection is given by

$$
   \dfrac{\vect{b}\ip\vect{a}_1}{\vect{a}_1\ip\vect{a}_1}\vect{a}_1 +
   \dfrac{\vect{b}\ip\vect{a}_2}{\vect{a}_2\ip\vect{a}_2}\vect{a}_2 =
   \dfrac{56}{14}\vect{a}_1 + \dfrac{6}{6}\vect{a}_2 = 4\vect{a}_1 + 1\vect{a}_2.
$$

And then the least squares solution is found to be $\hat{\vect{x}} = \left[ \begin{array}{c} 4 \\ 1 \end{array}   \right]$.

For this vector we find

$$
  A\hat{\vect{x}} = \left[ \begin{array}{c} 5  \\ 6 \\ 13 \end{array}   \right], \quad
  \text{with} \,\,\norm{A\hat{\vect{x}} - \vect{b}} = \sqrt{(-4)^2 + (-1)^2 + 2^2 } = \sqrt{21}.
$$

{prf:ref}`Prop:LeastSquares:Existence` tells us this is the closest we can get.
::::

In {prf:ref}`Ex:LeastSquares:OrthogExample` the coefficients of the orthogonal projection were quickly found due to the fact that the vectors $\vect{a}_1$ and $\vect{a}_2$ were orthogonal.
In {numref}`Section %s <Sec:Gram-Schmidt>` we saw how we can construct an orthogonal basis from an arbitrary basis. And then we can use the projection formula {eq}`Eq:OrthoBase:OrthoProj` to find the orthogonal projection. However, we will see that this is an unnecessary detour.

(SubSec:LeastSquares:NormalEquations)=

## Normal Equations

There is a direct way to find the coefficients of the orthogonal projection onto Col$ A$ if the columns are not orthogonal.

::::{prf:theorem} Normal Equations
:label: Thm:LeastSquares:NormalEquations

Suppose $A$ is an $m \times n$ matrix and $\vect{b}$ is a vector in $\R^m$.

Then the system of linear equations

:::{math}
:label: Eq:LeastSquares:NormalEquations

A^TA\vect{x} = A^T\vect{b}
:::

is always consistent. The equations in this system are called the **normal equations**.

Any solution $\hat{\vect{x}}$ of the normal equations is a least squares solution.

::::

Before having a look at the proof consider the following example.

::::{prf:example}
:label: Ex:LeastSquares:NormalEqs-1

We compute the least squares solution of the linear system

$$
  \left\{       \begin{array}{ccccccc}
        x_1  &+&  2x_2  & +& x_3& =& 20 \\
        2x_1 &+&  x_2 &+& x_3&=& 20 \\
        3x_1 &+&2 x_2 & +& 4x_3&=& 40\\
        2x_1 &+& x_2 & +& 3x_3&=& 30.
       \end{array}
  \right.
$$

The normal equations lead to the augmented matrix

$$
  \left[\,A^TA \,| \,A^T \vect{b}\,\right] =
    \left[       \begin{array}{ccc|c}
        18 &   12 &   21 &   240 \\
        12 &   10 &   14 &   170 \\
        21 &   14 &   27 &   290
       \end{array}
  \right].
$$

This can be row reduced to the echelon form

$$
    \left[       \begin{array}{ccc|c}
        1 &   0 &   0 &   16/3 \\
        0 &   1 &   0 &   5 \\
        0 &   0 &   1 &   4
       \end{array}
  \right].
$$

The least squares solution can be read off from the last column in this matrix.

$$
  \hat{\vect{x}} =  \left[\begin{array}{c}
         16/3 \\   5 \\   4
       \end{array}
  \right].
$$

The error vector and the least squares error are found to be

$$
 \vect{v} = A\hat{\vect{x}} - \vect{b} = \left[ \begin{array}{c}
         -2/3 \\   -1/3  \\   2 \\ -7/3
       \end{array}
  \right], \quad \norm{\vect{v}} = \sqrt{10}.
$$

This is slightly better than the 'trial solution' in {prf:ref}`Ex:LeastSquares:4x3Example`,
where the norm of the error vector was found to be $\sqrt{15}$.

::::

In the proof properties of the orthogonal projection are combined in a clever way.
As usual, feel free to skip it.

::::{admonition} Proof of&nbsp;{prf:ref}`Thm:LeastSquares:NormalEquations`
:class: tudproof, dropdown

As usual we denote the columns of the $m \times n$ matrix $A$ by $\vect{a}_1, \ldots, \vect{a}_n$.

From the section about orthogonal projections, we know that the orthogonal projection of $\vect{b}$
onto the column space of $A$ exists and is unique. (cf. {prf:ref}`Thm:OrthoBase:OrthoDecomp`.) This projection will be a vector of the form

$$
   c_1\vect{a}_1 + \ldots + c_n\vect{a}_n
$$

for certain constants $c_1, \ldots c_n$.  
% If $A$ has independent columns, these constants are unique.

By the definition of the orthogonal projection we have that $(\vect{b} - (c_1\vect{a}_1 + \ldots + c_n\vect{a}_n))$ lies in the orthogonal complement of Col$ A$, i.e.,

$$
  \vect{a}_i \ip (\vect{b} - (c_1\vect{a}_1 + \ldots + c_n\vect{a}_n))   = 0, \quad  i = 1, \ldots, n.
$$

This leads to $n$ linear equations

$$
   \vect{a}_i^T (\vect{b} - c_1\vect{a}_1 + \ldots + c_n\vect{a}_n) = 0
$$

for the unknowns $c_1, \ldots, c_n$.

These equations can be rewritten as

$$
    \vect{a}_i^T\vect{b} - \vect{a}_i^T\vect{a}_1\, c_1 - \vect{a}_i^T\vect{a}_2\, c_2 -\ldots - \vect{a}_i^T\vect{a}_n\, c_n = 0,
$$

and further to

$$
    \vect{a}_i^T\vect{a}_1\, c_1 + \ldots + \vect{a}_i^T\vect{a}_n\, c_n = \vect{a}_i^T\vect{b}, \quad i = 1, \ldots, n.
$$

In matrix-vector form this becomes

$$
 \left[  \begin{array}{cccc}
     \vect{a}_1^T\vect{a}_1 &  \vect{a}_1^T\vect{a}_2 & \ldots & \vect{a}_1^T\vect{a}_n \\
     \vect{a}_2^T\vect{a}_1 &  \vect{a}_2^T\vect{a}_2 & \ldots & \vect{a}_2^T\vect{a}_n \\
        \vdots        &  \vdots        & & \vdots      \\
     \vect{a}_n^T\vect{a}_1 &  \vect{a}_n^T\vect{a}_2 & \ldots & \vect{a}_n^T\vect{a}_n \\
  \end{array} \right]
  \left[  \begin{array}{c}   c_1 \\ c_2 \\ \ldots \\ c_n   \end{array} \right] =
  \left[  \begin{array}{c}  \vect{a}_1^T\vect{b} \\ \vect{a}_2^T\vect{b} \\ \ldots \\ \vect{a}_n^T\vect{b}   \end{array} \right].
$$

Which leads to the following very concise form.

$$
   A^TA \vect{c} = A^T\vect{b}.
$$

So, to find the least squares solution(s) of the linear system $A\vect{x} = \vect{b}$, we have to solve the normal equations

:::{math}
:name: Eq:LeastSquares:NormalEquations2

A^TA \vect{x} = A^T\vect{b}.
:::

::::

If $\vect{c} =  \left[  \begin{array}{c}   c_1 \\ c_2 \\ \vdots \\ c_n   \end{array} \right]$ is the least squares solution of the linear system $A\vect{c} = \vect{b}$,
then the orthogonal projection of
$\vect{b}$ of Col$ A$ is given by

$$
  \text{proj}_{\text{Col} A}(\vect{b}) = c_1\vect{a}_1 + \ldots + c_n\vect{a}_n = A \vect{c}.
$$

If the columns $\vect{a}_1, \ldots, \vect{a}_n$ of $A$ are linearly independent, the coefficients $c_i$ are the coordinates with respect to the basis $\{\vect{a}_1, \ldots, \vect{a}_n\}$, hence they are unique. Thus in that case the normal equations

$$
  A^TA \vect{x} = A^T\vect{b}
$$

must have a unique solution.

There is another way to see this, which follows from the next proposition.

::::{prf:proposition}  
:label: Prop:LeastSquares:InvertibleATA

Suppose $A$ is an $m \times n$ matrix. If the columns of $A$ are linearly independent then
the matrix $A^TA$ is invertible.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:LeastSquares:InvertibleATA`
:class: tudproof

In fact, something stronger holds:

:::{math}
:label: Eq:LeastSquares:InvertibilityATA

A\vect{x}= \vect{0} \quad \iff \quad A^TA\vect{x} = \vect{0}.
:::

First if $A\vect{x}= \vect{0}$, then clearly $A^TA\vect{x} = A^T\vect{0} = \vect{0}$.

To prove the converse, suppose $A^TA\vect{x} = \vect{0}$.

Then &nbsp; $\vect{x}^TA^TA\vect{x} = \vect{x}^T\vect{0} = \vect{0}$ &nbsp; too.

Now realize that $\vect{x}^TA^TA\vect{x} = (A\vect{x})^TA\vect{x} = \norm{A\vect{x}}^2$.

So $A^TA\vect{x} = \vect{0}$ implies $\norm{A\vect{x}}^2 = 0$, and that means that $A\vect{x}$ must be the zero vector.

The equivalence {eq}`Eq:LeastSquares:InvertibilityATA` implies: if $A$ has linearly independent columns,
then $A\vect{x} = \vect{0}$ has $\vect{x}= \vect{0}$ as only solution, so $A^TA\vect{x} = \vect{0}$ has
$\vect{x}= \vect{0}$ as only solution. This means that $A^TA$ is invertible.
::::

::::{exercise}
:label: Exc:LeastSquares:InvertibleATA

Prove the converse of {prf:ref}`Prop:LeastSquares:InvertibleATA`.

For any $m \times n$ matrix $A$, if $A^TA$ is invertible, then the columns of $A$ must be linearly independent. (Note that the matrix $A$ is not supposed to be a square matrix.)

::::

::::{admonition} Solution to&nbsp;{numref}`Exc:LeastSquares:InvertibleATA`
:class: solution, dropdown

Suppose that $A$ is an $m \times n$ matrix $A$ for which $A^TA$ is invertible.
To prove that $A$ has linearly independent columns we have to show that the equation

$$
  A\vect{x} = \vect{0}
$$

has only the trivial solution $\vect{x} = \vect{0}$.

So suppose that $ A\vect{c} = \vect{0}$ for some vector $\vect{c} \in \R^{n}$.
Then a fortiori

$$
  A^TA\vect{c} = A^T\vect{0} = \vect{0}.
$$

The assumption that $A^TA$ is invertible implies that indeed $\vect{c} = \vect{0}$.

::::

::::{prf:remark}

As stated, the least squares solution of a system $A\vect{x} = \vect{b}$ consists of the coefficients $c_i$
of the orthogonal projection

$$
   \text{proj}_{\text{Col}\,A}(\vect{b}) = c_1\vect{a}_1 + c_2\vect{a}_2 + \ldots + c_n\vect{a}_n = A \vect{c}, \quad \vect{c} = \begin{bmatrix} c_1 \\ \vdots \\ c_n\end{bmatrix},
$$

of $\vect{b}$ onto the column space of $A$.

For a matrix $A$ with linearly independent columns, $\vect{c}$ is unique, and given by

$$
  \vect{c} = (A^TA)^{-1}A^T\vect{b}.
$$

So for a matrix $A$ with linearly independent columns the projection of a vector $\vect{b}$ onto Col $A$ is given by

:::{math}
:label: Eq:LeastSquares:ProjbColA

\hat{\vect{b}} = \text{proj}_{\text{Col }A}(\vect{b}) = A(A^TA)^{-1}A^T \vect{b}.

:::

::::

We already knew how to find this projection if the columns are orthogonal. Using the normal equations we don't need orthogonality.

Applying {prf:ref}`Thm:LeastSquares:NormalEquations` to the earlier example
({prf:ref}`Ex:LeastSquares:OrthogExample`),
shows that in the case of _orthogonal_ vectors there is actually nothing new. This is illustrated in the next example.

::::{prf:example}
:label: Ex:LeastSquares:OrthogExample2

Let us again find, but now using {prf:ref}`Thm:LeastSquares:NormalEquations`, the least squares solution of the linear system

$$
  \left\{\begin{array}{ccccccc}
        x_1 &+&  x_2  &=& 9 \\
        2x_1 &-& 2x_2 &=& 7 \\
        3x_1 &+& x_2 &=& 11.
       \end{array}
  \right.
$$

The normal equations give the augmented matrix

$$
  [\,A^TA \,| \,A^T \vect{b}\,] =
    \left[       \begin{array}{cc|c}
        \vect{a}_1^T\vect{a}_1 & \vect{a}_1^T\vect{a}_2 & \vect{a}_1^T\vect{b} \\
        \vect{a}_2^T\vect{a}_1 & \vect{a}_2^T\vect{a}_2 & \vect{a}_2^T\vect{b} \\
       \end{array}
  \right] = \left[       \begin{array}{cc|c}
        14 & 0 & 56 \\
        0 & 6 & 6 \\
       \end{array}
  \right].
$$

Note that the orthogonality of the columns leads to a coefficient matrix $A^TA$ that is a diagonal matrix.
The normal equations can be solved in one stroke.

This (again) yields the least squares
solution $\hat{\vect{x}} =\left[\begin{array}{c} 4 \\ 1  \end{array}   \right]$.

::::

The previous example can be generalized as follows.

If the columns $\{\vect{a}_1, \ldots, \vect{a}_n\}$ of an $m \times n$ matrix $A$ form a set of non-zero, _orthogonal_ vectors in $\R^m$, then the orthogonal projection

$$
   c_1\vect{a}_1 + c_2\vect{a}_2 + \cdots + c_n\vect{a}_n
$$

of a vector $\vect{b}$ in $\R^m$ onto Col $A$ is found by solving the normal equations

$$
 \left[  \begin{array}{cccc}
     \vect{a}_1^T\vect{a}_1 &  \vect{a}_1^T\vect{a}_2 & \ldots & \vect{a}_1^T\vect{a}_n \\
     \vect{a}_2^T\vect{a}_1 &  \vect{a}_2^T\vect{a}_2 & \ldots & \vect{a}_2^T\vect{a}_n \\
        \vdots        &  \vdots        & & \vdots      \\
     \vect{a}_n^T\vect{a}_1 &  \vect{a}_n^T\vect{a}_2 & \ldots & \vect{a}_n^T\vect{a}_n \\
  \end{array} \right]
  \left[  \begin{array}{c}   x_1 \\ x_2 \\ \ldots \\ x_n   \end{array} \right] =
  \left[  \begin{array}{c}  \vect{a}_1^T\vect{b} \\ \vect{a}_2^T\vect{b} \\ \ldots \\ \vect{a}_n^T\vect{b}   \end{array} \right].
$$

Since the columns are orthogonal, all products $\vect{a}_i^{T}\vect{a}_j = \vect{a}_i\ip\vect{a}_j$ with $i \neq j$ are zero.

Expressing the equation using inner products we find

$$
  \left[  \begin{array}{cccc}
     \vect{a}_1\ip\vect{a}_1 &  0 & \ldots & 0 \\
     0 &  \vect{a}_2\ip\vect{a}_2 & \ldots & 0 \\
        \vdots        &  \vdots        &\ddots  & \vdots      \\
     0 &  0 & \ldots & \vect{a}_n\ip\vect{a}_n \\
  \end{array} \right]
  \left[  \begin{array}{c}   x_1 \\ x_2 \\ \vdots \\ x_n   \end{array} \right] =
  \left[  \begin{array}{c}  \vect{a}_1\ip\vect{b} \\ \vect{a}_2\ip\vect{b} \\ \vdots \\ \vect{a}_n\ip\vect{b}   \end{array} \right].
$$

Which leads to the good old expressions &nbsp; $c_i = \dfrac{\vect{a}_i\ip\vect{b}}{\vect{a}_i\ip\vect{a}_i} =  \dfrac{\vect{b}\ip\vect{a}_i}{\vect{a}_i\ip\vect{a}_i}$.

As before ({prf:ref}`Thm:OrthoBase:OrthoDecomp`) the orthogonal projection becomes

$$
   \text{proj}(\vect{b}) =  \dfrac{\vect{b}\ip\vect{a}_1}{\vect{a}_1\ip\vect{a}_1}\vect{a}_1 +
    \dfrac{\vect{b}\ip\vect{a}_2}{\vect{a}_2\ip\vect{a}_2}\vect{a}_2 + \ldots +
     \dfrac{\vect{b}\ip\vect{a}_n}{\vect{a}_n\ip\vect{a}_n}\vect{a}_n.
$$

::::{exercise}
:label: Exc:LeastSquares:QR

Show that Formula {eq}`Eq:LeastSquares:ProjbColA` for a matrix $A$ with linearly independent columns and QR decomposition $A = QR$ (see {prf:ref}`Thm:GramSchmidt:QR-decomp`) simplifies to

$$
  \hat{\vect{b}} = \text{proj}_{\text{Col} A}(\vect{b}) =  QQ^T \vect{b}.
$$

Also explain this simpler formula by interpreting the $QR$ decomposition in a suitable way.
::::

::::{admonition} Solution to&nbsp;{numref}`Exc:LeastSquares:QR`
:class: solution, dropdown

This involves some elementary matrix operations. <BR>
Suppose $A = QR$, where $Q^TQ = I$, and $R$ is an upper triangular matrix with a positive diagonal. So $R$ is invertible. <BR>

Substitution of $A=QR$ into {eq}`Eq:LeastSquares:ProjbColA`

$$
 \hat{\vect{b}} = \text{proj}_{\text{Col }A}(\vect{b}) = A(A^TA)^{-1}A^T \vect{b}
$$

gives

$$
  \hat{\vect{b}} =  QR \left[(QR)^T(QR)\right]^{-1}\vect{b}
  = QR\left[R^TQ^TQR\right]^{-1} (R^TQ^T)\vect{b}.
$$

Using $Q^TQ = I$ and $\left[R^TR\right]^{-1} = R^{-1}(R^T)^{-1}$ this can be simplified further to

$$
  \hat{\vect{b}} = QR \left[R^TR\right]^{-1}R^TQ^T\vect{b} =QRR^{-1}(R^T)^{-1}R^TQ^T\vect{b} = QQ^T\vect{b}
$$

The interpretation is as follows. The columns $\vect{q}_i$ of $Q$ form an orthonormal basis for the column space of $A$. So the orthogonal projection onto Col$(A$) is the same as the orthogonal projection onto Col$(Q)$. For a matrix with _orthonormal_ columns the projection formula

$$
 \begin{array}{lcl}
  \hat{\vect{b}} = \proj_{\Col{(Q)}}(\vect{b}) &=& (\vect{b}\cdot\vect{q}_1)\vect{q}_1 + \cdots +   (\vect{b}\cdot\vect{q}_n)\vect{q}_n\\&=& \vect{q}_1(\vect{b}\cdot\vect{q}_1) + \cdots +  \vect{q}_n (\vect{b}\cdot\vect{q}_n)\\
  &= &  \vect{q}_1(\vect{q}_1^T\vect{b}) + \cdots + \vect{q}_n(\vect{q}_n^T\vect{b})\\
  &= &  \left[\vect{q}_1\vect{q}_1^T + \cdots + \vect{q}_n\vect{q}_n^T\right]\,\vect{b}
  \end{array}
$$

can be written in a very concise way as

$$
   \hat{\vect{b}} =  QQ^T\vect{b}.
$$

::::

To conclude this section we will consider the situation where the matrix $A$ has linearly _dependent_ columns.
Then the least squares solution is not unique.

Let us look at an example first.

::::{prf:example}
:label: Ex:LeastSquares:NonUnique

We find the least squares solutions of the linear system $A\vect{x} = \vect{b}$, where

$$
   A = \left[\begin{array}{cc}
                     1 & -2 \\ 2 & -4
                     \end{array}\right], \quad
   \vect{b} =    \left[\begin{array}{c}  2\\-4 \end{array}\right]
$$

Note that the columns of $A$ are indeed linearly dependent.

For the least squares solution we have to solve the system with the augmented matrix

$$
   \left[\,A^TA \,| \,A^T \vect{b}\,\right] =
    \left[  \begin{array}{cc|c}
        5 & -10 &  10 \\
        -10 & -20 & 20
       \end{array}
  \right].
$$

The augmented matrix can be row reduced to

$$
   \left[  \begin{array}{cc|c}
        1 & -2  & 2 \\
        0 &  0  & 0
       \end{array}
  \right].
$$

From this we can read off all least squares solutions. They are given by

$$
   \hat{\vect{x}} = \hat{\vect{x}}_0 + \vect{x}_H = \left[\begin{array}{c}  2 \\ 0 \end{array}\right] +
   c\left[\begin{array}{c}  2 \\ 1 \end{array}\right], \,\, c\in \R.
$$

%We can ask the question: what is the least squares solution _of minimal length_?

For this low-dimensional problem we can draw a picture.

:::{figure} Images/Fig-LeastSquares-SmallestLS.svg
:name: Fig:LeastSquares:SmallestLS
:class: dark-light

Multiple least squares solutions.
:::

The least squares solutions are depicted as the line $\ell:  \vect{x} = \hat{\vect{x}}_0 + c\left[\begin{array}{c}  2 \\  1 \end{array}\right]$.

::::

We can analyse {prf:ref}`Ex:LeastSquares:NonUnique` from a higher perspective.
In the general solution of the normal equations

$$
   \vect{x} = \hat{\vect{x}}_0 + c\left[\begin{array}{c}  2 \\  1 \end{array}\right],
$$

the 'homogeneous' part $\vect{x}_H = c\left[\begin{array}{c}  2 \\  1 \end{array}\right]$ is the nulspace of $A^TA$. Because of the equivalence {eq}`Eq:LeastSquares:InvertibilityATA` this is equal to the nulspace of $A$.
Now from {numref}`Section %s <Sec:OrthoComp>`, {prf:ref}`Prop:OrthoComp:OrthoComplementNulA`, we know that

$$
   (\text{Nul}\,A)^{\perp} = \text{Row}\,A = \Span{\begin{bmatrix} 1 \\ -2\end{bmatrix}}
$$

which is visualized in {numref}`Figure %s <Fig:LeastSquares:SmallestLS>`.

Let us give one more example to illustrate matters.

::::{prf:example}
:label: Ex:LeastSquares:NonUnique2

We find the least squares solutions of the linear system $A\vect{x} = \vect{b}$, where

$$
   A = \left[\begin{array}{ccc}
                     1 & 1 & 0 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \\ 1 & 0 & 1
                     \end{array}\right], \quad
   \vect{b} =    \left[\begin{array}{c}  1 \\3\\2\\4 \end{array}\right]
$$

The first column of $A$ is the sum of the other two columns, so the columns of $A$ are linearly dependent.

For the least squares solution we have to solve the system with augmented matrix

$$
   \left[\,A^TA \,| \,A^T \vect{b}\,\right] =
    \left[  \begin{array}{ccc|c}
        4 & 2 & 2 & 10 \\
        2 & 2 & 0 & 4 \\
        2 & 0 & 2 & 6
       \end{array}
  \right].
$$

The augmented matrix can be row reduced to

$$
   \left[  \begin{array}{ccc|c}
        1 & 0 &  1  & 3 \\
        0 & 1 & -1  & -1 \\
        0 & 0 &  0  & 0
       \end{array}
  \right].
$$

From this we can read off all least squares solutions. They are given by

$$
   \hat{\vect{x}} = \hat{\vect{x}}_0 + \vect{x}_H = \left[\begin{array}{c}  3 \\ -1 \\ 0 \end{array}\right] + c\left[\begin{array}{c}  1 \\ -1 \\ -1 \end{array}\right], \,\, c \in \R.
$$

As in {prf:ref}`Ex:LeastSquares:NonUnique` the 'homogeneous' part $\vect{x}_H = c\left[\begin{array}{c}  1 \\ -1 \\ -1 \end{array}\right]$ is the nulspace of $A^TA$, which is equal to the nulspace of $A$.

For instance, by taking $c=0$ and $c = -1$ we find the two least squares solutions

$$
   \hat{\vect{x}}_1 = \left[\begin{array}{c}  3 \\ -1 \\ 0 \end{array}\right], \quad \hat{\vect{x}}_2 = \left[\begin{array}{c}  2 \\ 0 \\ 1 \end{array}\right].
$$

For both we find the least squares error

$$
  \norm{A\hat{\vect{x}}_i - \vect{b}} =
  \norm{\left[\begin{array}{c}  2\\2\\3\\3 \end{array}\right] - \left[\begin{array}{c}   1 \\ 3 \\ 2 \\ 4\end{array}\right]} = \sqrt{4} = 2.
$$

::::

## Grasple Exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9666528f-1e81-4273-b571-8dae64a7972c?id=91139
:label: grasple_exercise_7_4_1
:dropdown:
:description: About the interpretation of a least squares solution.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c96c0359-9599-4fd4-b5b2-bd7f9d2da463?id=91141
:label: grasple_exercise_7_4_2
:dropdown:
:description: About the uniqueness of a least squares solution.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6068f5ac-3eb3-40a1-8686-ddbf05f172b2?id=91165
:label: grasple_exercise_7_4_3
:dropdown:
:description: About least squares solutions and normal equations.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/45e14081-07dd-4297-96ac-e1403c841511?id=110654
:label: grasple_exercise_7_4_4
:dropdown:
:description: About the interpretation of the LS   solution.
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/316a02be-a293-4340-ac81-47a6b25b115d?id=110658
:label: grasple_exercise_7_4_5
:dropdown:
:description: Finding the LS solution for 3x2 system in a geometric way.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a0878702-dcc0-4216-b2d6-0b1d7d1b046e?id=91142
:label: grasple_exercise_7_4_6
:dropdown:
:description: Finding the LS solution for 3x2 systems in three steps.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6a0628e8-065d-4390-b0c4-8ff131761de4?id=91161
:label: grasple_exercise_7_4_7
:dropdown:
:description: LS solution + LS error for a 3x2 system.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1d9a943a-b51f-48c9-99a9-691b80b8df60?id=91159
:label: grasple_exercise_7_4_8
:dropdown:
:description: LS solution + LS error for a 4x4 system.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d7480f19-afdb-474d-8542-299fc21a1952?id=91908
:label: grasple_exercise_7_4_9
:dropdown:
:description: LS solution + LS error for a 4x3 system.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c6a52270-1c43-46a2-9dda-f1ab8b366066?id=91146
:label: grasple_exercise_7_4_10
:dropdown:
:description: On the connection between orthogonal projections and least squares problems.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/743d744c-1bcb-460a-973e-3e693e86e20d?id=91157  
:label: grasple_exercise_7_4_11
:dropdown:
:description: LS solution + LS error for a 3x2 system.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b081f76a-0e03-48cc-b27b-afab51ac2c91?id=91155
:label: grasple_exercise_7_4_12
:dropdown:
:description: LS solutions + LS error for a 4x3 system.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/679d1581-08bc-416b-89bf-766faad9f118?id=91394
:label: grasple_exercise_7_4_13
:dropdown:
:description: Finding the LS solution for a 4x3 system (involving quite some reduction work).

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3d0a7884-09ee-4f89-a2e5-1c1476d7e2a3?id=91448
:label: grasple_exercise_7_4_14
:dropdown:
:description: Finding the LS solution for a 4x3 system (with some tricky reduction work).

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/396fd7a0-10cf-4b49-bb9e-fbc4acc2a06a?id=91148
:label: grasple_exercise_7_4_15
:dropdown:
:description: What is the quickest way to find the least squares solution?

::::

(SubSec:LeastSquares:LinearModels)=

## Linear Models

In {numref}`SubSec:LeastSquares:Introduction` we looked at ways to fit a line
$y = a + bx$ to a set of points $(x_i, y_i), i = 1, \ldots, n$ in the plane. In statistics this plays an important role in so-called _regression models_.

One way to define the best fitting line $y = \hat{a}+\hat{b}x$ is to let $(\hat{a},\hat{b})$ be the least squares solution to the set of $n$ linear equations

$$
  y_i = a+bx_i, \quad  i = 1, \ldots , n.
$$

Note that in these equations the parameters $a$ and $b$ are the unknowns.

This line is sometimes refered to as the _least squares line_.

::::{prf:example}
:label: Ex:LeastSquares:LineFit1

Suppose we want to find the least squares line for the set of four points

$$
  (1,2), (2,2),  (4,3),  (5,3).
$$

At first sight the line through the first and the last point, i.e.,

$$
   y = \tfrac14(x-1) + 2 = 0.25x + 1.75
$$

seems a good candidate.
The points and the 'first guess' are depicted in {numref}`Figure %s <Fig:LeastSquares:FirstGuess>`

:::{figure} Images/Fig-LeastSquares-FirstGuess.svg
:name: Fig:LeastSquares:FirstGuess
:class: dark-light

First guess for best line.
:::

For this line the sum of the squares of the errors

$$
  y_i - (0.25x + 1.75),
$$

which in this context are called **residues**, becomes

$$
  \sum_{i=1}^4 (y_i - (0.25x + 1.75))^2 = 0^2 + 0.25^2 + 0.25^2 + 0^2 = 0.125.
$$

To find the least squares line we consider the four equations in the form

$$
   \left[\begin{array}{cc}
         1 & x_1  \\ 1 &  x_2 \\ 1 &  x_3 \\ 1 &  x_4
       \end{array}\right]
       \left[\begin{array}{c}  a \\ b \end{array}\right]
   = \left[\begin{array}{c}
         y_1  \\   y_2 \\ y_3 \\ y_4
       \end{array}\right], \quad
       \,\, \text{i.e.,} \,\,
     \left[\begin{array}{cc}
         1 & 1  \\ 1 &  2 \\ 1 &  4 \\ 1 &  5
       \end{array}\right]
       \left[\begin{array}{c}  a \\ b \end{array}\right]
   = \left[\begin{array}{c}
         2  \\  2  \\ 3 \\ 3
       \end{array}\right].
$$

Since the matrix has linearly independent columns the normal equations, with augmented matrix

$$
  \left[\,A^TA \,| \,A^T \vect{b}\,\right] =
    \left[\begin{array}{cc|c}
        4 &   12 &   10 \\
        12 &   46 &   33
       \end{array}
  \right],
$$

give a unique least squares solution, and it is $\hat{a} = 1.6$, $\hat{b} = 0.3$.

{numref}`Figure %s <Fig:LeastSquares:LSline>` shows both lines.

:::{figure} Images/Fig-LeastSquares-LSLine.svg
:name: Fig:LeastSquares:LSline
:class: dark-light

Least squares line.

:::

For the line $y = \hat{a}  + \hat{b}x$ the sum of the squares of the residues becomes

$$
   (2 - (1.6+0.3\cdot1))^2 + (2 - (1.6+0.3\cdot2))^2 + (3 - (1.6+0.3\cdot4))^2 + (3 - (1.6+0.3\cdot5))^2 = 0.1^2 + 0.2^2 + 0.2^2 + 0.1^2 = 0.1.
$$

This is indeed slightly better than with the line found 'at first sight', where the sum was equal to $0.125$.
::::

We can even find a ready-made formula for the least squares line through $n$ given points
$(x_1,y_1), (x_2, y_2), \ldots, (x_n, y_n)$.

::::{prf:example}
The coefficients of the least squares line $y = \hat{a}  + \hat{b}x$ for the set of points
$(x_1,y_1), (x_2, y_2), \ldots, (x_n, y_n)$ are given by

$$
  \begin{array}{ccl}
  \hat{a} &=& \dfrac{(\sum x_i^2)(\sum y_i) -(\sum x_i)(\sum x_iy_i) }{n\sum x_i^2 - (\sum x_i)^2}, \\
  \hat{b} &=& \dfrac{n(\sum x_iy_i) -(\sum x_i)(\sum y_i) }{n\sum x_i^2 - (\sum x_i)^2}.
  \end{array}
$$

Introducing the notation

$$
 \begin{array}{lll}
  \Sigma_x = \sum x_i, &\Sigma_{xx} = \sum x_i^2, \\
  \Sigma_{y} = \sum y_i, &\Sigma_{xy} = \sum x_iy_i,& \Sigma_{yy} = \sum y_i^2,
  \end{array}
$$

the coefficients get the following more concise form,

:::{math}
:label: Eq:Leastquares:GeneralLinefit

\hat{a} = \dfrac{\Sigma_{xx}\Sigma_y - \Sigma_x\Sigma_{xy}}{n\Sigma_{xx} - \Sigma_x^2},
\quad
\hat{b} = \dfrac{n\Sigma_{xy} - \Sigma_x\Sigma_{y}}{n\Sigma_{xx} - \Sigma_x^2}.

:::

We will derive the formula by diligently working through the normal equations.

In matrix-vector form the linear system we want to solve reads

$$
  \left[\begin{array}{cccc}
         1 & x_1 \\
         1 & x_2 \\
            \vdots   & \vdots \\
         1 & x_n     \end{array}\right]
        \left[\begin{array}{c}
          a \\ b   \end{array}\right] =
        \left[\begin{array}{c}
          y_1 \\ y_2 \\ \vdots \\ y_n    \end{array}\right].
$$

Noting that

$$
\left[\begin{array}{cc}
         1 & x_1 \\
         1 & x_2 \\
            \vdots   & \vdots \\
         1 & x_n     \end{array}\right]^T
         \left[\begin{array}{cc}
         1 & x_1 \\
         1 & x_2 \\
            \vdots   & \vdots \\
         1 & x_n     \end{array}\right]
=
\left[\begin{array}{cc}
         n & \sum x_i \\
         \sum x_i & \sum x_i^2     \end{array}\right]
=
\left[\begin{array}{cc}
         n & \Sigma_x \\
         \Sigma_x & \Sigma_{xx}     \end{array}\right]
$$

and

$$
   \left[\begin{array}{cc}
         1 & x_1 \\
         1 & x_2 \\
            \vdots   & \vdots \\
         1 & x_n     \end{array}\right]^T
    \left[\begin{array}{c}
          y_1 \\ y_2 \\   \vdots   \\ y_n  \end{array}\right]
    =
    \left[\begin{array}{c}
          \sum y_i \\ \sum x_iy_i  \end{array}\right]
    =
   \left[\begin{array}{c}
          \Sigma_y \\ \Sigma_{xy}  \end{array}\right].
$$

This leads to the normal equations

$$
  \left[\begin{array}{cc}
         n & \Sigma_x \\
         \Sigma_x & \Sigma_{xx}     \end{array}\right]
           \left[\begin{array}{c}
          a\\ b  \end{array}\right]
  =  \left[\begin{array}{c}
          \Sigma_y \\ \Sigma_{xy}  \end{array}\right].
$$

If we multiply both sides of this equation by

$$
  \left[\begin{array}{cc}
         n & \Sigma_x \\
         \Sigma_x & \Sigma_{xx}     \end{array}\right] ^{-1} =
    \dfrac{1}{n\Sigma_{xx} - \Sigma_x^2}  \left[\begin{array}{cc}
         \Sigma_{xx}  & -\Sigma_x \\
         -\Sigma_x &   n  \end{array}\right],
$$

we see the expressions {eq}`Eq:Leastquares:GeneralLinefit` readily appearing.

::::

Fitting a line to a set of points, may be looked upon as fitting a linear combination of the functions $f_0(x) = 1$ and $f_1(x) = x$.
Depending on the context we may also consider fitting a
linear combination of a larger set of 'basic' functions. <BR>
For instance, when we use $f_0(x) = 1$, $f_1(x) = x$ and $f_2(x) = x^2$, we are in fact looking for a quadratic function $y = a_0 + a_1x + a_2x^2$ that best fits the set of points. <BR>
And we may even go beyond that. Then we get a more general so-called _linear model_.

::::{prf:definition} Linear Model
:label: Def:LeastSquares:LinModel

Suppose $k$ functions $f_1(x), \ldots, f_k(x)$
and $n$ points $(x_1,y_1), \ldots, (x_n,y_n)$ in the plane are given.

The **linear model** refers to the 'best' linear combination, in the least squares sense, of the form

$$
  c_1f_1(x) + c_2f_2(x) + \ldots + c_kf_k(x).
$$

That is, the linear combination that minimizes

:::{math}
:label: Eq:LeastSquares:SumResidues

\sum_{i=1}^n \big(y_i - (c_1f_1(x_i) + c_2f_2(x_i) + \ldots + c_kf_k(x_i))\,\big)^2,

:::

the sum of the squares of the errors/residues

$$
   y_i - \big(c_1f_1(x_i) + c_2f_2(x_i) + \ldots + c_kf_k(x_i)\big).
$$

::::

The epithet _linear_ refers to the fact that the parameters $c_1, \ldots, c_k$ appear in the model in a linear way. The functions $f_i$ that are used in the model definitely don't have to be linear.

::::{prf:remark}

The parameters $c_1,c_2,\ldots,c_k$ that minimize the sum
in {eq}`Eq:LeastSquares:SumResidues` coincide with the least squares solution of the linear system

:::{math}
:label: Eq:LeastSquares:DesignMatrix

\left[\begin{array}{cccc}
f_1(x_1) & f_2(x_1) & \ldots & f_k(x_1) \\
f_1(x_2) & f_2(x_2) & \ldots & f_k(x_2) \\
\vdots & \vdots & & \vdots \\
\vdots & \vdots & \ddots & \vdots \\
f_1(x_n) & f_2(x_n) & \ldots & f_k(x_n)
\end{array}\right]
\left[\begin{array}{c}
c_1 \\ c_2 \\ \vdots \\ c_k \end{array}\right] =
\left[\begin{array}{c}
y_1 \\ y_2 \\ \vdots \\ \vdots \\ y_n
\end{array}
\right].  
:::

::::

::::{prf:remark}

In practice the points $(x_1,y_2), \ldots, (x_n,y_n)$ are often called the **data**, sometimes considered to be a **sample** from some space.
The variable $x$ is then considered as the **input variable** and
the $y$ as the **output variable**. Lastly the matrix in the expression on the left of Equation {eq}`Eq:LeastSquares:DesignMatrix` is sometimes refered to as the **design matrix**.

::::

Several generalizations are possible. We mention two.

<ol>

<li>
  The input  may be multivariate.  The  set of data points then has the form
  
:::{math}
:label: Eq:LeastSquares:Data-n-dim

     \begin{array}{c} (x_{11},x_{12},\ldots,x_{1k},y_1)  \\
                      (x_{21},x_{22},\ldots,x_{2k},y_2)\\
                          \vdots \quad\quad \vdots \quad\quad \vdots\\
                      (x_{n1},x_{n2},\ldots,x_{nk},y_n),
     \end{array}

:::

and we want to find the linear combination

<BR>

$$
    \beta_1f_1(x_1, \ldots, x_{k}) + \ldots +
   \beta_{\ell}f_{\ell}(x_{1},\ldots, x_{k})
$$

that best fits these data.

For instance, to find the linear function

$$
  y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \ldots + \beta_k x_k
$$

that best fits the data in {eq}`Eq:LeastSquares:Data-n-dim`, we can take $f_0(x_1,\ldots,x_k) = 1$ and $f_i(x_1,\ldots,x_k) = x_i$, for $i = 1, \ldots, k$.

In a least squares model we then look for the parameters $\beta_1, \ldots, \beta_{\ell}$ that minimize

:::{math}
:label: Eq:LeastSquares:GeneralModel

     \sum_{i=1}^{n}  \big(y_i - \beta_1f_1(x_{i1},\ldots, x_{ik}) \,-\, \ldots \,-\,
     \beta_{\ell}f_{\ell}(x_{i1},\ldots, x_{ik})\big)^2.

:::

</li>

<li>

In a _weighted least squares model_ the terms in the
sum {eq}`Eq:LeastSquares:GeneralModel`
get different weights $w_i$. When building a statistical model this may be desirable when some data give more 'information'.

Then the expression we want to minimize is given by

$$
  \sum_{i=1}^{n}  \class{blue}{w_i} \big(y_i - \beta_1f_1(x_{i1},\ldots, x_{ik}) \,-\, \ldots \,-\,
   \beta_{\ell}f_{\ell}(x_{i1},\ldots, x_{ik})\big)^2.
$$

This approach may be relevant if the variance of some of the observations that led to them seems smaller than the variance of other observations.

</li>

</ol>

To illustrate matters we present two examples.

::::{prf:example} Fitting a plane

Suppose $n$ points $(x_i,y_i,z_i)$, $i = 1, \ldots , n$ are given and we want to fit a plane through these. In other words, we want to find a linear combination

$$
  L(x,y) = a + bx + cy
$$

of the functions $f_0(x,y) = 1$, $f_1(x,y) = x$ and $f_2(x,y) = y$ that fits these points best.

In the least square sense we would then have to solve the normal equations for the linear system

$$
 \left\{ \begin{align}
          a + bx_1 + cy_1 & = z_1 \\
          a + bx_2 + cy_2 & = z_2 \\
          \quad \vdots \quad \vdots \quad & = \,\, \vdots \\
          a + bx_n + cy_n & = z_n
          \end{align} \right.
          \quad \,\,\text{i.e.,} \quad
 \left[ \begin{array}{ccc}
             1 & x_1 & y_1 \\
             1 & x_2 & y_2 \\
             \vdots & & \vdots  \\
             1 & x_n & y_n
         \end{array}\right]
  \left[ \begin{array}{c} a \\b \\c \end{array}\right] =
  \left[ \begin{array}{c} z_1 \\z_2 \\ \vdots \\ z_n \end{array}\right].
$$

::::

::::{prf:example}
Suppose we have $n$ data points $(x_i,y_i)$, $i = 1,\ldots,n$, and taking physical conditions into account, we expect a relation of the form $ y = ax^r$ between them.

One way to go about to find suitable parameters $a$ and $r$ is to transform both $x$ and $y$ to log-scale by introducing the new variable

$$
   z = \log(y) = \ln(y).
$$

The relation between $x$ and $y$ then transforms to

$$
 z = \ln(y) = \ln(a) + r \ln(x).
$$

We can find the least squares linear fit to the points $(\ln(x_i), z_i)$.

$$
    z = \alpha + \beta x
$$

for the points

$$
  (\ln(x_1), \ln(y_1)), \quad  \ldots\,, \quad  (\ln(x_n), \ln(y_n)).
$$

If we have found the least squares parameters $\hat{\alpha}$ and $\hat{\beta}$ for the transformed problem, at the end we have to 'transform back' to find the 'best power fit'.

$$
  \ln(y) = \hat{\alpha} + \hat{\beta}\ln(x)
   \quad \Longrightarrow \quad y = ax^b, \,\,  a = e^{\hat{\alpha}},\,\,r = \hat{\beta}.
$$

{numref}`Figure %s  <Fig:LeastSquares:Powerfit>` shows what's going on.
The first plot shows the points $(x_i,y_i)$, the second plot shows the points
$(\ln(x_i), \ln(y_i))$, and the last two plots give the points with the two fits.

:::{figure} Images/Fig-LeastSquares-PowerFit.svg
:name: Fig:LeastSquares:Powerfit
:class: dark-light

Least squares fitting via logarithmic scale.
:::

::::

## Grasple Exercises (for Linear Models)

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6a2b9aeb-3c59-4b8f-8d7c-e51f651998fd?id=91883
:label: grasple_exercise_7_4_16
:dropdown:
:description: On the precise definition of the least squares line.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/254298e0-f091-4a9d-8e8a-31cc3cf11f16?id=91884
:label: grasple_exercise_7_4_17
:dropdown:
:description: Design matrix and input vector for the regression line through a set of points.

::::
::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/dad8ca0a-ef17-4757-803c-26b8ae9804de?id=91886
:label: grasple_exercise_7_4_18
:dropdown:
:description: Fitting a line through set of points and compute the residual vector.

::::
::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9ad7148d-ef39-46ef-8f14-20e97511655d?id=91889
:label: grasple_exercise_7_4_19
:dropdown:
:description: Fitting a parabola to a set of points.

::::
::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/222ee704-85f5-470a-b48f-f88d9900a8d1?id=91890
:label: grasple_exercise_7_4_20
:dropdown:
:description: Fitting a quadratic polynomial to a set of points.

::::
::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ff6329bd-f5b3-41ce-828f-2086cf651181?id=91898
:label: grasple_exercise_7_4_21
:dropdown:
:description: Design matrix to fit $y = ax + bx^3$ to a set of points.

::::
::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f75014bf-0e90-43e7-acf4-216cb38ffd11?id=91903
:label: grasple_exercise_7_4_22
:dropdown:
:description: Design matrix to fit $y = c_1 e^t + c_2 \cos(x) + c_3 \sin(x)$ to a set of points.

::::


::::
::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/741fc8fb-476b-4ab7-8a3c-fb353a00ede4?id=110657
:label: grasple_exercise_7_4_23
:dropdown:
:description: Design matrix in a context example (Ohm's law).

::::

