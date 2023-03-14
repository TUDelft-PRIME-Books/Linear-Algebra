(Sec:LeastSquares)=
# Least Squares Solutions 

## Introduction 

In Chapter 2, especially {numref}`Section %s <Section:LinSystems>`,  we studied linear systems.  One way to write them down was  as a matrix-vector equation:  $A\vect{x} = \vect{b}$

A linear system could be either consistent or inconsistent. If a system were inconsistent, that would be end of story.

In this section we will reconsider the inconsistent situation and ask ourselves the question whether there is a vector $\vect{x}$  that is in a  sense the 'best possible' solution.

One common situation where an inconsistent linear system comes up quite naturally is the following.
Suppose $n \geq 3$ points  $(x_1,y_1), \ldots, (x_n,y_n)$ in the plane are given. 
Which line best fits  this set of points?

There are different ways to define what is the *best* line.   For instance,  we may mean the line that minimizes the sums of the distances of the points to the line.
Or,  we can take  the line for which the sum of vertical distances from the points to the line is minimal.
See Figure . . .

Both are sensible ideas.  However, to turn these two ideas into an algorithm to find the best line  not as straightforward as the computations that come out if we put the question into the realm of linear algebra.
And there it will turn out to be the problem of an inconsistent system.

Ideally we would find parameter  $a$ and $b$ such that the line with the equation

$$ 
    y = ax + b
$$

contains all  points  $(x_i,y_i)$.

That means that all equations

$$
   \left\{\begin{array}{ccc} 
                     y_1 &=& ax_1 + b \\
                     y_2 &=& ax_2+ b \\
                      \vdots & & \vdots \\
                      y_n &=& ax_n + b \\
                     \end{array}\right.
$$

will be satisfied simultaneously.  This only happens if the matrix-vector equation

:::{math} 
:label: Eq:LeastSquares:Linefit

  \left[\begin{array}{cc} 
        1 & x_1 \\ 1 & x_2 \\ \vdots & \vdots \\ 1 & x_n 
       \end{array}\right]
       \left[\begin{array}{c} 
        a \\ b
       \end{array}\right] =
        \left[\begin{array}{c} 
        y_1 \\ y_2 \\  \vdots \\ y_n 
       \end{array}\right] 
:::

is consistent.



We will come back to this question in   {numref}`Subsection %s <SubSec:LeastSquares:LinearModels>`.



(SubSec:LeastSquares:Normal Equations)=
## Normal Equations

We start by defining what we consider to be the 'optimal' solution of a linear system   $A\vect{x} = \vect{b}$. 

::::{prf:definition} 
:label: Dfn:LeastSquares:LS-Solution

Let $A$ be an $m\times n$ matrix and $\vect{b}$  a vector in $\R^{m}$.
A vector  $\hat{\vect{x}}$ is called a **least squares solution**  of the linear system   $A\vect{x} = \vect{b}$
if for every  $\vect{x}$ in $\R^n$  the inequality

$$
   \norm{A\hat{\vect{x}} - \vect{b}} \leq \norm{A\vect{x} - \vect{b}}
$$

holds.

::::

::::{prf:remark}
:label:  Rem:LeastSquares:BestLinComb

Note that  

$$
   A\hat{\vect{x}} - \vect{b} = \hat{x}_1\vect{a}_1 + \ldots +  \hat{x}_n\vect{a}_n - \vect{b}.
$$ 

So a least squares solution yields a linear combination  of the columns of $A$ that has a minimal distance to 
$\vect{b}$.   The distance between two vectors  $\vect{u}$ and $\vect{v}$ in $\R^n$ is defined as   

$$
   \norm{\vect{u} - \vect{v}} = \sqrt{(u_1-v_1)^2 + (u_2-v_2)^2 + \ldots + (u_n-v_n)^2},
$$

In a way we are minimizing a sum of of squares, which explains the name *least squares* solution.

In the situation where we want to fit a line, and we have the linear system as in Equation 
{eq}`Eq:LeastSquares:Linefit`, the expression  $\norm{A\vect{x} - \vect{b}}$  comes down to

$$
  \sqrt{ (y_1 - (ax_1+b))^2 + \ldots + (y_n - (ax_n+b))^2}.
$$

The differences  

$$
 y_i - (ax_i+b)
$$ 

are called the *residues*.  So if we use this approach to find a best possible solution, we are in fact minimizing the sum of the squares of the residues.


::::


The questions we will answer in this subsection are

<ol type ="i">
<li>

Does a least squares solution always exist?

</li>

<li>

If a least squares solution exists,  is it unique?

</li>

<li>

How to compute the least squares solution(s)?

</li>

</ol>

So let us consider these questions one by one.

::::{prf:proposition} 
:label: Prop:LeastSquares:Existence

For each linear system $A\vect{x} = \vect{b}$, where $A$ is an $m \times n$ matrix, a least squares solution always exists.  Moreover the least squares solution is unique if and only if the columns of $A$ are linearly independent.

::::

::::{prf:proof}
In {prf:ref}`Rem:LeastSquares:BestLinComb` it was noted that a least squares solution corresponds to the vector in Col $A$  that is closest to $\vect{b}$.   From Section . . . (orthogonal projections)  we know that the vector in Col $A$  that is closest to $\vect{b}$  is precisely the orthogonal projection of $\vect{x}$ onto the Span$\{\vect{a}_1,\ldots,\vect{a}_n\}$.

This projection, a linear combination of the colums of $A$, always exists.

The coefficients of this linear combination then give a least squares solution.  

Lastly, these coefficients are unique if and only if the columns of $A$ are linearly independent. 

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
  \right.$$

According to {prf:ref}`Prop:LeastSquares:Existence` the least squares solution contains the coefficients of the orthogonal projection of  the vector 
$
  \vect{b} = \left[ \begin{array}{c} 9 \\ 7 \\ 11 \end{array}   \right]
$
onto
$
 \Span{\vect{a}_1, \vect{a}_2} = 
\Span{\left[ \begin{array}{c} 1 \\ 2 \\ 3 \end{array}   \right], \left[ \begin{array}{c} 1 \\ -2 \\ 1 \end{array} \right]}
$.

Since the vectors $\vect{a}_1$ and $\vect{a}_2$ are orthogonal, this projection is given by

$$
   \dfrac{\vect{b}\ip\vect{a}_1}{\vect{a}_1\ip\vect{a}_1}\vect{a}_1 +
   \dfrac{\vect{b}\ip\vect{a}_2}{\vect{a}_2\ip\vect{a}_2}\vect{a}_2 =
   \dfrac{56}{14}\vect{a}_1 + \dfrac{6}{6}\vect{a}_2 = 4\vect{a}_1 + 1\vect{a}_2.
$$

So the least squares solution is found to be  $\hat{\vect{x}} = \left[ \begin{array}{c} 4 \\ 1 \end{array}   \right]$.

For this vector we find 

$$
  A\hat{\vect{x}} = \left[ \begin{array}{c} 5  \\ 6 \\ 13 \end{array}   \right], \quad
  \norm{A\hat{\vect{x}} - \vect{b}} = \sqrt{(-4)^2 + (-1)^2 + 2^2 } = \sqrt{21}.
$$

 {prf:ref}`Prop:LeastSquares:Existence` tells us this is the closest we can get.
::::


In {prf:ref}`Ex:LeastSquares:OrthogExample` the coefficients of the orthogonal projection were quickly found due to the fact that the vectors  $\vect{a}_1$ and $\vect{a}_2$ were orthogonal. 
In  {numref}`Section %s <Sec:Gramschmidt>` we saw how we can construct an orthogonal basis from an arbitrary basis. And then we can use the projection formula of  {prf:ref}`Section %s <Sec:OrthogonalProjection>` to find the orthogonal projection.  However, we will see that this is an unnecessarry detour.

::::{prf:proposition} 
:label: Prop:LeastSquares:InvertibleATA

Suppose  $A$ is an $m \times n$ matrix.  If  the columns of $A$ are linearly independent then
the matrix  $A^TA$  is invertible.

::::


::::{prf:proof}

In fact, something stronger holds:  

:::{math} 
:label: Eq:LeastSquares:InvertibilityATA

   A\vect{x}= \vect{0}  \quad \iff \quad A^TA\vect{x} = \vect{0}.
:::

First  if  $A\vect{x}= \vect{0}$,  then clearly   $A^TA\vect{x} = A^T\vect{0} = \vect{0}$.

To prove the converse, suppose $A^TA\vect{x} = \vect{0}$,  then $\vect{x}^TA^TA\vect{x} = \vect{x}^T\vect{0} = \vect{0}$ too.  Now realize that  $\vect{x}^TA^TA\vect{x} = (A\vect{x})^TA\vect{x} = \norm{A\vect{x}}^2$.
So  $A^TA\vect{x} = \vect{0} \Rightarrow \norm{A\vect{x}^2} = 0 \Rightarrow \vect{x}=0$.


The equivalence  {eq}`Eq:LeastSquares:InvertibilityATA` implies:  if  $A$ has linearly independent columns,
then  $A\vect{x} = \vect{0}$ has  $\vect{x}= \vect{0}$ as only solution, so $A^TA\vect{x} = \vect{0}$  has
$\vect{x}= \vect{0}$ as only solution.  This means that  $A^TA$ is invertible.

::::









::::{prf:theorem} Normal Equations
:label: Thm:LeastSquares:NormalEquations

Suppose  $A$ is an $m \times n$  matrix and  $\vect{b}$  in a vector in $\R^m$.

Then the  system of linear equations

:::{math} 
:label: Eq:LeastSquares:NormalEquations

A^TA\vect{x} = A^T\vect{b}
:::

is always  consistent.  This system is called the system of *normal equations*.

Any solution $\hat{\vect{x}}$ of the normal equations is a least squares solution.

Moreover, if the columns of $A$ are linearly independent, then the solution $\hat{\vect{x}}$ is unique. 

::::

::::{prf:example}
:label: Ex:LeastSquares:NormalEqs-1

Empty example
::::

::::{prf:proof}  Of {prf:ref}`Thm:LeastSquares:NormalEquations`

As usual we denote the columns of the $m \times n$ matrix $A$ by  $\vect{a}_1, \ldots, \vect{a}_n$.

From the section about orthogonal projections, we know that the orthogonal projection of $\vect{b}$ 
onto the column space of $A$ exists.  This projection will be a vector of the form

$$
   c_1\vect{a}_1 + \ldots + c_n\vect{a}_n
$$

for certain constants  $c_1, \ldots c_n$.  If $A$ has independent columns, these constants are unique.

By the definition of the orthogonal projection we have that $(\vect{b} - (c_1\vect{a}_1 + \ldots + c_n\vect{a}_n))$ lies in the orthogonal complement of Col$ A$, i.e.,

$$
  \vect{a}_i \ip (\vect{b} - (c_1\vect{a}_1 + \ldots + c_n\vect{a}_n))   = 0, \quad  i = 1, \ldots, n.
$$

This leads to $n$ linear equations

$$
   \vect{a}_i^T (\vect{b} - c_1\vect{a}_1 + \ldots + c_n\vect{a}_n) = 0  
$$

which can be rewritten as

$$
    \vect{a}_i^T\vect{a}_1 c_1 + \ldots + \vect{a}_i^T\vect{a}_n c_n = \vect{a}_i^T\vect{b}.
$$

In matrix-vector form this becomes

$$
 \left[  \begin{array}{cccc}  
     \vect{a}_1^T\vect{a}_1 &  \vect{a}_1^T\vect{a}_2 & \ldots & \vect{a}_1^T\vect{a}_n \\
     \vect{a}_2^T\vect{a}_1 &  \vect{a}_2^T\vect{a}_2 & \ldots & \vect{a}_2^T\vect{a}_n \\
        \vdots        &  \vdots        & & \vdots      \\
     \vect{a}_n^T\vect{a}_1 &  \vect{a}_n^T\vect{a}_2 & \ldots & \vect{a}_1^T\vect{a}_n \\
  \end{array} \right]
  \left[  \begin{array}{c}   c_1 \\ c_2 \\ \ldots \\ c_n   \end{array} \right] =
  
  \left[  \begin{array}{c}  \vect{a}_1^T\vect{b} \\ \vect{a}_2^T\vect{b} \\ \ldots \\ \vect{a}_n^T\vect{b}   \end{array} \right].
$$

Which leads to the following very concise form.

$$
   A^TA \vect{c} = A^T\vect{b}.
$$

So, to find the least squares solution(s) of the linear system   $A\vect{x} = \vect{b}$,  we have to solve the normal equations

$$
  A^TA \vect{x} = A^T\vect{b}.
$$

::::

::::{prf:example}

We compute the least squares solution of the linear system


$$
  \left\{       \begin{array}{ccccccc} 
        x_1  &+&  2x_2  & +& x_3& =& 20 \\
        2x_1 &+&  x_2 &+& x_3&=& 20 \\
        3x_1 &+&2 x_2 & +& 4x_3&=& 40\\
        2x_1 &+& x_2 & +& 3x_3&=& 30
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

The least squares solution is the last column in this matrix.

::::


::::{prf:remark}

As stated, the least squares solution of a system  $A\vect{x} = \vect{b}$ consists of the coefficients $c_i$
of the orthogonal projection 


$$
   \text{proj}_{\text{Col}\,A}(\vect{b}) = c_1\vect{a}_1 + c_2\vect{a}_2 + \ldots c_n\vect{a}_n = A \vect{c}
$$

of $\vect{b}$ onto the column space of $A$.

For a matrix $A$ with linearly independent columns,  $\vect{c}$ is unique, and given by

$$
  \vect{c} = (A^TA)^{-1}A^T\vect{b}.
$$

So for a matrix $A$ with linearly independent columns the projection of a vector $\vect{b}$ onto Col $A$ is given by

:::{math} 
:label: Eq:LeastSquares:ProjbColA

  \hat{\vect{b}} = \text{proj}_{\text{Col }A}(\vect{b}) = (A^TA)^{-1}A^T \vect{b}. 

:::

::::




We already knew how to find this projection if the columns are orthogonal. Using the normal equations we don't need orthogonality.  
The next example, the one from the introduction  ({prf:ref}`Ex:LeastSquares:OrthogExample`),
shows that in this case there is actually nothing new.

::::{prf:example}
:label: Ex:LeastSquares:OrthogExample2

Find the least squares solution of the linear system 

$$
  \left\{       \begin{array}{ccccccc} 
        x_1 &+&  x_2  &=& 9 \\
        2x_1 &-& 2x_2 &=& 7 \\
        3x_1 &+& x_2 &=& 11
       \end{array}
  \right.
$$

The normal equations become

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

Note that the orthogonality of the columns lead to a  coefficient matrix  $A^TA$ that is a diagonal matrix.
Whence  the normal equations can be solved in one stroke.

This yields (again) yields the least squares 
solution  $\hat{x} =\left[\begin{array}{c} 4 \\ 1  \end{array}   \right]$.


::::

The previous example can be generalized as follows.

If the columns  $\{\vect{a}_1, \ldots, \vect{a}_n\}$ of an $m \times n$ matrix $A$  form a set of non-zero, orthogonal vectors in $\R^m$,  then the orthogonal projection 

$$
   c_1\vect{a}_1 + c_2\vect{a}_2 + \ldots c_n\vect{a}_n
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

Since the columns are orthogaonal, all products  $\vect{a}_i^{T}\vect{a}_j = \vect{a}_i\ip\vect{a}_j$ with  $i \neq j$  are zero.  Using the notation with inner products we find

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

Which leads to  the good old expressions  $x_i = \dfrac{\vect{a}_i\ip\vect{b}}{\vect{a}_i\ip\vect{a}_i}$.

And as before the orthogonal projection becomes

$$
   \text{proj}(\vect{b}) =  \dfrac{\vect{b}\ip\vect{a}_1}{\vect{a}_1\ip\vect{a}_1}\vect{a}_1 +
    \dfrac{\vect{b}\ip\vect{a}_2}{\vect{a}_2\ip\vect{a}_2}\vect{a}_2 + \ldots +
     \dfrac{\vect{b}\ip\vect{a}_n}{\vect{a}_n\ip\vect{a}_n}\vect{a}_n. 
$$

::::{prf:example}
:label: Ex:LeastSquares:QR


Show that Formula {eq}`Eq:LeastSquares:ProjbColA`  for a matrix $A$ with linearly independent columns and  qr-decomposition $A = QR$  (see {prf:ref}`Thm:GramSchmidt:QR-decomp`)  simplifies  to  

$$
  \hat{\vect{b}} = \text{proj}_{\text{Col} A}(\vect{b}) =  QQ^T \vect{b}. 
$$

Also explain this simpler formula by interpreting the $QR$ decomposition in a suitable way.
::::

To conclude this section we will consider the situation where the matrix $A$ has linearly *dependent* columns.
Then the least squares solution is not unique.

Let us look at an example first.



::::{prf:example}
:label: Ex:LeastSquares:NonUnique

We find the least squares solutions of the linear system  $A\vect{x} = \vect{b}$, where

$$
   A = \left[\begin{array}{cc} 
                     1 & -2 \\ 2 & -4 
                     \end{array}\right], \quad
   \vect{b} =    \left[\begin{array}{c}  2\\-4 \end{array}\right]               
$$

Note that the columns of $A$ are indeed linearly dependent.

For the least squares solution we have to solve the system with augmented matrix

$$
   \left[\,A^TA \,| \,A^T \vect{b}\,\right] = 
    \left[  \begin{array}{cc|c} 
        5 & -10 &  10 \\
        -10 & -20 & 20 
       \end{array}
  \right].
$$ 

The augmented matrix can be row reduced  to

$$
   \left[  \begin{array}{cc|c} 
        1 & -2  & 2 \\
        0 &  0  & 0
       \end{array}
  \right].
$$

From this we can read off all least squares solutions.  They are given by

$$
   \hat{\vect{x}} = \hat{\vect{x}}_0 + \vect{x}_H = \left[\begin{array}{c}  2 \\ 0 \end{array}\right] + 
   c\left[\begin{array}{c}  2 \\ 1 \end{array}\right], \,\, c\in \R.
$$



We can ask the question: what is the least squares solution of minimal length?

For this low-dimensional problem we can draw a picture.


:::{figure}  Images/Fig-LeastSquares-NonUnique2D.svg
:name: Fig:LeastSquares:NonUnique2D

:::


The least squares solutions are depicted as the line $\ell:  \vect{x} = \hat{\vect{x}}_0 + c\left[\begin{array}{c}  2 \\  1 \end{array}\right]$.

The solution of smallest length is found by intersecting the normal 
line $m:  \vect{x} = k\left[\begin{array}{c}  1 \\  -2 \end{array}\right]$ with $\ell$. 

This give the (unique) solution of shortest length $\hat{\vect{x}}_1 = \dfrac25\left[\begin{array}{c}  1 \\  -2 \end{array}\right]$

::::

We can analyse {prf:ref}`Ex:LeastSquares:NonUnique` from a higher perspective.
In the general solution of the normal equations 

$$
   \vect{x} = \hat{\vect{x}}_0 + c\left[\begin{array}{c}  2 \\  1 \end{array}\right],
$$

the 'homogeneous' part  $\vect{x}_H = c\left[\begin{array}{c}  2 \\  1 \end{array}\right]$ is the nulspace of  $A^TA$.  Because of the equivalence {eq}`Eq:LeastSquares:InvertibilityATA` this is equal to the nulspace of $A$.
To find the point on this line closest to the origin, we intersect with the orthogonal complement of this nulspace.  Now from  {numref}`Section %s <Sec:Orthogonality>`, {prf:ref}`Prop:Orthogonality:OrthoComplementNulA`, we know that 

$$
   (\text{Nul}\,A)^{\perp} = \text{Row}\,A
$$

This means that the intersection of  $\hat{\vect{x}}_0 + \text{Nul}\,A$  and  $\text{Nul} A$  is the projection of $\hat{\vect{x}}_0$  onto the rowspace of $A$.  This is also visualized 
in {numref}`Figure %s <Fig:LeastSquares:NonUnique2D>`.

We put the conclusion of this into a proposition.

::::{prf:proposition}
:label: Prop:LeastSquares:SmallestLS


::::


::::{prf:example}
:label: Ex:LeastSquares:NonUnique

We find the least squares solutions of the linear system  $A\vect{x} = \vect{b}$, where

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
        2 & 2 & 0 & 0 \\
        2 & 0 & 2
       \end{array}
  \right].
$$ 

The augmented matrix can be row reduced  to

$$
   \left[  \begin{array}{ccc|c} 
        1 & 0 & 3 & 5 \\
        0 & 1 & -1 & -1 \\
        0 & 0 & 0 & 0
       \end{array}
  \right].
$$

From this we can read off all least squares solutions.  They are given by

$$
   \hat{\vect{x}} = \hat{\vect{x}}_0 + \vect{x}_H = \left[\begin{array}{c}  3 \\ -1 \\ 0 \end{array}\right] + c\left[\begin{array}{c}  1 \\ -1 \\ -1 \end{array}\right], \,\, c \in \R.
$$

The 'homogeneous' part  $\vect{x}_H = c\left[\begin{array}{c}  1 \\ -1 \\ -1 \end{array}\right]$ is the nulspace of  $A^TA$, which, because of the equivalence {eq}`Eq:LeastSquares:InvertibilityATA` is equal to the nulspace of $A$.

We can ask the question: what is the least squares solution of minimal length?

(SubSec:LeastSquares:LinearModels)=
## Linear Models









%::::{prf:definition} 
%:label: Dfn:SymmetricMat:SymmetricMatrix