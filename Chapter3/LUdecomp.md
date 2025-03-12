<!-- :::{review}
::: -->

(Sec:LUdecomp)=

# The $LU$ decomposition

As we have seen, one way to solve a linear system $A\vect{x}=\vect{b}$ is to row reduce it to echelon form and then use back substitution. See for instance {prf:ref}`Ex:LinSystems:I`.  
In this section we will learn how to solve an $m\times n$ linear system $A\mathbf{x}=\mathbf{b}$ by decomposing (or factorising) a matrix into a product of two 'special' matrices $L$ and $U$. 
This is called an $LU$-*decomposition* of the matrix $A$. 
% The following example illustrates the procedure.

::::::{prf:example}
:label: Ex:LUdecomp:FirstLU
Consider the system $A\mathbf{x} = \mathbf{b}$ where

$$
A =
\begin{bmatrix}
1 &  1 & -1 \\
2 &  4 & -3 \\
1 & -1 &  -3
\end{bmatrix},
\qquad
\mathbf{b} =
\begin{bmatrix}
2 \\ 1 \\8
\end{bmatrix}.
$$



To start with, the matrix  $A$ can be factorized as

$$
A  = 
\begin{bmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
1 & -1 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 1 & -1 \\
0 & 2 & -1 \\
0 & 0 &  -3
\end{bmatrix} = LU.
$$

We will see how this helps to solve the system in an efficient way.
::::::

With this factorisation we can solve the system in two steps, using both backward and forward substitution.  In fact, the matrix $U$ is an echelon matrix equivalent to $A$.
To solve the equation  $LU\vect{x} = L(U\vect{x}) =\vect{b}$  we can introduce the auxiliary vector $\vect{y}$ via

$$
  \vect{y} = U\vect{x}.
$$

We then first solve 

::::{math}
:label: Eq:LUDecomp:Lyb

  L\vect{y} = \vect{b}

::::

and after that we find $\mathbf{x}$  by solving

$$
 U\vect{x} = \tilde{\vect{y}},
$$


for the solution  $ \tilde{\vect{y}}$  of system {eq}`Eq:LUDecomp:Lyb`.  For this solution $ \tilde{\vect{x}}$ we then have

$$
   A \tilde{\vect{x}} = L\,U\, \tilde{\vect{x}} = L(U\tilde{\vect{x}})= L\tilde{\vect{y}} = \vect{b}. 
$$


We illustrate matters with the linear system of {prf:ref}`Ex:LUdecomp:FirstLU`.


::::::{prf:example} 
:label: Ex:LUdecomp:FirstLUcontinued

The  system  $A\vect{x} = \vect{b}$ of  {prf:ref}`Ex:LUdecomp:FirstLU` can be written as

$$
\begin{bmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
1 & -1 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 1 & -1 \\
0 & 2 & -1 \\
0 & 0 &  -3
\end{bmatrix} 
\begin{bmatrix}
x_1\\ x_2 \\ x_3
\end{bmatrix} =
\begin{bmatrix}
2 \\ 1 \\8
\end{bmatrix}.
$$

By setting  

$$
 \mathbf{y} = \begin{bmatrix}
1 & 1 & -1 \\
0 & 2 & -1 \\
0 & 0 &  -3 \end{bmatrix} \begin{bmatrix} x_1\\ x_2 \\ x_3 \end{bmatrix},
$$

we have

$$
\begin{bmatrix}
1 & 0 & 0 \\
2 & 1 & 0 \\
1 & -1 & 1
\end{bmatrix}
\begin{bmatrix}
y_1\\y_2\\y_3
\end{bmatrix} =
\begin{bmatrix}
2 \\ 1 \\ 8
\end{bmatrix}, \quad \text{i.e.,}\,\,
\left\{\begin{array}{ccccccc}
             y_1 & &      & &      &=&  2 \\
            2y_1 &+&  y_2 & &      &=&  1 \\
            y_1  &-&  y_2 &+&  y_3 &=&  8.
          \end{array} \right.

$$

With forward substitution we can find the solution:

$$ 
    \begin{array}{ll} y_1 = 2 & \Longrightarrow \quad y_2 = 1 - 2y_1 = -3  \\
     & \Longrightarrow \quad  
    y_3 = 8 - y_1 + y_2  = 3  \quad    
    \Longrightarrow  \quad   \begin{bmatrix}
y_1\\y_2\\y_3
\end{bmatrix} =
\begin{bmatrix}
2 \\ -3 \\ 3
\end{bmatrix}.
\end{array}
$$


Next we solve 

$$
\begin{bmatrix}
1 & 1 & -1 \\
0 & 2 & -1 \\
0 & 0 & -3
\end{bmatrix} 
\begin{bmatrix}
x_1\\ x_2 \\ x_3
\end{bmatrix} =
\begin{bmatrix}
2 \\ -3 \\ 3
\end{bmatrix},
$$

with back substitution.  This gives the solution

$$
\begin{bmatrix}
x_1 \\ x_2 \\ x_3
\end{bmatrix} 
= 
\begin{bmatrix}
3\\ -2 \\ -1
\end{bmatrix},
$$

which is the solution to our original system. Since the factorisation was given, we did not have to solve the system from scratch by trying to find an echelon form.

::::::


Here is one to try for yourself.

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b9a339dc-721f-4c85-aa77-3455269a3b7a?id=105809
:label: grasple_exercise_3_6_1T
:dropdown:
:description: To solve a system  $LU\vect{x} = \vect{b}$.
::::::


There are several methods for factorising matrices. The factorisations that we will see in this section use **direct methods**. Direct methods are methods that produce the exact factorisations in a finite number of steps.

%There are special cases where solving linear systems can be done quickly. These cases involve %triangular or trapezoidal matrices (we will discuss these matrices in the next section). In general, %when the matrix associated with an $m\times n$ linear system is a trapezoidal matrix we can use %backward or forward substitution for solving them. Remember the echelon forms from {numref}%`Subsec:LinSystems:RowReduction`? Echelon forms are trapezoidal matrices.

%The most common factorisation methods make use of this kind of matrices. This is why we will first %introduce the idea of a trapezoidal and triangular matrix and then discuss the corresponding %factorisation methods and their applications.

In the next subsection we will address the questions of whether an $LU$ decomposition always exists and if so, how to construct it.  With an extra condition on $L$ the decomposition, if it exists, will be unique. In the case where an $LU$ decomposition does not exist we can instead consider the   slightly  more general $PLU$ decomposition. In the remainder of the section we will consider the generalization to non-square matrices and we will analyze to which extent the $(P)LU$ decomposition  can give an efficiency boost.


## $LU$ decomposition of a square matrix


::::::{prf:definition}
:label: Def:LUdecomp:DefinitionLU

Let $A$ be an $n\times n$ matrix. An  **$LU$ decomposition**  of $A$ is a factorization of the type

$$
A=LU
$$

where $L$ is  an $n\times n$ lower triangular matrix with $1$s on the diagonal, and  $U$ an $n\times n$ upper triangular matrix. So, 

$$
L=
\begin{bmatrix}
1\\
l_{21} & 1 \\
l_{31} & l_{32} & \ddots  \\
\vdots & \vdots & \ddots & \ddots\\
l_{n1} & l_{n2} &  \cdots & l_{n,n-1} & 1
\end{bmatrix}
,
\quad
U=
\begin{bmatrix}
u_{11} & u_{12} & u_{13} & \cdots &u_{1n} \\
       & u_{22} & u_{23} & \cdots & u_{2n} \\
       & & u_{33} & \cdots & u_{3n} \\
      & &  &
\ddots & \vdots \\
& & & & u_{nn}
\end{bmatrix}.
$$

For convenience we have used blanks for zeros.

Note that the condition of $1$s on the diagonal implies that the matrix $L$ is invertible.

::::::

The next proposition captures the main interest of the $LU$ decomposition, as is already illustrated in 
{prf:ref}`Ex:LUdecomp:FirstLUcontinued`


::::::{prf:algorithm}
:label: Alg:LUdecomp:Usefulness

Suppose that $A=LU$, so that the linear system of equations $A\mathbf{x}=\mathbf{b}$ can be written as $LU\mathbf{x}=\mathbf{b}$. Then, by setting $\mathbf{y} = U\mathbf{x}$, we can solve the linear system in two steps.

:::{latexlist}
:enumerated: true
:type: i

\item Solve the system $L\mathbf{y}=\mathbf{b}$ and find $\mathbf{y}$. <BR>
      Note that this system has a unique solution.
\item Solve the system $U\mathbf{x}=\mathbf{y}$ to find $\mathbf{x}$.

:::

The solution of the second system is then a solution of the system $A\mathbf{x}=\mathbf{b}$.

::::::

The next proposition tells us which matrices do have an $LU$ decomposition.


::::::{prf:proposition}
:label: Prop:LUdecomp:Existence

A matrix $A$ can be written as $A = LU$, with $L$ and $U$ as described in {prf:ref}`Def:LUdecomp:DefinitionLU`   if and only if can be row reduced to an echelon matrix with only additions of multiples of rows to rows below it. We will call this a **top-down row reduction**.
::::::

Instead of a giving a formal proof, we will illustrate matters first with an example.
In this example you will see how  an $LU$ decomposition of a matrix is found via a top-down row reduction that keeps track of the row operations involved. 

::::::{prf:example}
:label: Ex:LUdecomp:SecondLU
We consider the matrix

$$
A=
\begin{bmatrix}
3 & 1 & -2 \\
2 & 4 & 1 \\
1 & 2 & 1
\end{bmatrix}
.
$$

To find an $LU$ decomposition we will work towards an echelon form in the top-down direction. In addition, we will keep track of the actions we perform.
For the first step,

$$

\left[\begin{array}{rrr}3 & 1 & -2\\2 & 4 & 1\\1 & 2 & 1\end{array} \right]  \begin{array}{l}
[R_1] \\
{[R_2-2/3R_1]} \\
{[R_3-1/3R_1]} \\
\end{array}
\quad\sim\quad
\begin{bmatrix}
3 & 1 & -2 \\
0 & {10}/{3} & {7}/{3} \\
0 & {5}/{3} & {5}/{3}
\end{bmatrix} = A_2.
$$

The numbers $2/3$ and $1/3$ are called *multipliers*.

A second row reduction step, involving the multiplier $1/2$,  leads to an echelon/upper triangular matrix.

$$

\left[\begin{array}{rrr}3 & 1 & -2\\0 &{10}/{3}&{7}/{3}\\0 &{5}/{3}&{5}/{3}\end{array} \right]  \begin{array}{l}
[R_1] \\
{[R_2]} \\
{[R_3-1/2R_2]} \\
\end{array}\sim
\begin{bmatrix}
3 & 1 & -2 \\
0 & {10}/{3} & {7}/{3} \\
0 & 0 & {1}/{2} 
\end{bmatrix} = A_3.
$$

We can effectuate these row operations by  matrix multiplications.

$$
  A_2 = F_1A = 
\begin{bmatrix}
1 & 0 & 0 \\
-2/3 & 1 & 0 \\
-1/3 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
3 & 1 & -2 \\
2 & 4 & 1 \\
1 & 2 & 1
\end{bmatrix}
=
\begin{bmatrix}
3 & 1 & -2 \\
0 & {10}/{3} & {7}/{3} \\
0 & {5}/{3} & {5}/{3}
\end{bmatrix}.
$$

In the same way the second row reduction step can be described by


$$
  A_3 = F_2A_2 = 
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & -1/2 & 1
\end{bmatrix}
\begin{bmatrix}
3 & 1 & -2 \\
0 & {10}/{3} & {7}/{3} \\
0 & {5}/{3} & {5}/{3}
\end{bmatrix} =
\begin{bmatrix}
3 & 1 & -2 \\
0 & {10}/{3} & {7}/{3} \\
0 & 0 & {1}/{2}
\end{bmatrix}.

$$

The echelon matrix $A_3$ can act as our upper triangular matrix $U$, and the above computations
can be summarized as

$$
  U = A_3 = F_2F_1A = FA = \begin{bmatrix}
1 & 0 & 0 \\
-2/3 &     1       & 0 \\
0 & -1/2 & 1
\end{bmatrix}
A,
$$
where $F = F_2F_1$.

We conclude that 

$$
  A = F^{-1} U =   \begin{bmatrix}
1 & 0 & 0 \\
2/3 & 1 & 0 \\
1/3 & 1/2 & 1
\end{bmatrix} 
  \begin{bmatrix}
                      3 & 1 & -2 \\
                      0 & {10}/{3} & {7}/{3} \\
                      0 & 0 & {1}/{2}
\end{bmatrix}

$$

which is indeed a product of a lower triangular matrix $L$  (with 1's on its diagonal) and an upper triangular matrix $U$.

::::::

The above procedure shows how in principle an $LU$ decomposition can be computed. However, writing down the explicit elementary like matrices $F_i$, computing their product $F$, and finding the inverse of $F$ is unnecessary.  Look at the matrix $L = F^{-1}$ we found! The entries below the diagonal are exactly the numbers  $2/3$, $1/3$ and $1/2$ we called the *multipliers*.
The following algorithm describes this 'shortcut' to find an $LU$ decomposition.

::::::{prf:algorithm}
:label: Alg:LUdecomp:LUalgorithm

Suppose the $n\times n$ matrix $A$ can be row reduced top-down to the echelon matrix $U$. If the numbers $m_{jk}$ denote the multiples of the $k$th row that are subtracted from the rows below it in the $k$th step (so $1 \leq k < j \leq n$), &nbsp; then 

$$
   A = LU, \quad \text{for} \,\,
   L = \begin{bmatrix}
1\\
m_{21} & 1 \\
m_{31} & m_{32} & \ddots  \\
\vdots & \vdots & \ddots & \ddots\\
m_{n1} & m_{n2} &  \cdots & m_{n,n-1} & 1
\end{bmatrix}.
$$


::::::


Another look at  {prf:ref}`Ex:LUdecomp:SecondLU` explains why the detour via the matrices $F_i$ and the inverse of their product can be skipped, as is expressed in the above algorithm.


::::::{prf:example}
:label: Ex:LUdecomp:SecondLUSecondLook

For the matrix $A= \begin{bmatrix}
                    3 & 1 & -2 \\
                    2 & 4 & 1 \\
                    1 & 2 & 1
                  \end{bmatrix}$, the same as in {prf:ref}`Ex:LUdecomp:SecondLU`, the 'trick' is not to work with the matrices $F_1$ and $F_2$, but with their inverses.

The first row reduction step

$$
  A_2 = F_1A = 
\begin{bmatrix}
1 & 0 & 0 \\
-2/3 & 1 & 0 \\
-1/3 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
3 & 1 & -2 \\
2 & 4 & 1 \\
1 & 2 & 1
\end{bmatrix}
=
\begin{bmatrix}
3 & 1 & -2 \\
0 & {10}/{3} & {7}/{3} \\
0 & {5}/{3} & {5}/{3}
\end{bmatrix}
$$

can be rewritten as

$$
   A = F_1^{-1}A_2 = L_1A_2 = 
\begin{bmatrix}
1 & 0 & 0 \\
2/3 & 1 & 0 \\
1/3 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
3 & 1 & -2 \\
0 & {10}/{3} & {7}/{3} \\
0 & {5}/{3} & {5}/{3}
\end{bmatrix}
$$


Likewise the second row reduction step 

$$
  A_3 = F_2A_2 = 
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & -1/2 & 1
\end{bmatrix}
\begin{bmatrix}
3 & 1 & -2 \\
0 & {10}/{3} & {7}/{3} \\
0 & {5}/{3} & {5}/{3}
\end{bmatrix} =
\begin{bmatrix}
3 & 1 & -2 \\
0 & {10}/{3} & {7}/{3} \\
0 & 0 & {1}/{2}
\end{bmatrix}
$$

can be can be represented as  


$$
A_2 = F_2^{-1}A_3 = L_2U = 
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 1/2 & 1
\end{bmatrix}
\begin{bmatrix}
3 & 1 & -2 \\
0 & {10}/{3} & {7}/{3} \\
0 & {5}/{3} & {5}/{3}
\end{bmatrix}.

$$

Combining the two equations gives

$$
  A = L_2L_1U = LU = 
  \begin{bmatrix}
    1 & 0 & 0 \\
    2/3 & 1 & 0 \\
    1/3 & 1/2 & 1  
  \end{bmatrix}
  \begin{bmatrix}
    3 & 1 & -2 \\
    0 & {10}/{3} & {7}/{3} \\
    0 & 0 & {1}/{2}
  \end{bmatrix}.
$$

We see the multipliers nicely fall into place!

::::::

Here is an example where we apply the algorithm without further ado to a $4 \times 4$ matrix.

::::::{prf:example} 
:label: Ex:LUdecomp:LUviaAlgorithm
We use the $LU$-algorithm for the matrix  $A = \begin{bmatrix}
                                            2 & 1 & -2 & 3 \\
                                            2 & -3 & -4 & 7 \\
                                            -4 & 0 & -2 & -5 \\ 
                                            -6 & -1 & 8 & -8
                                        \end{bmatrix}.$

We row reduce the matrix $A$  top-down, diligently registering the multipliers.
Recall that the multiplier $m_{jk}$ is  defined as the multiple of row $k$ that is *subtracted* from row $j$ in the $k$-th step of the reduction process.

Here we go:

$$ 
\left[\begin{array}{rrrr}
            2 &  1 & -2 &  3 \\
            2 & -3 & -4 &  7 \\
           -4 &  0 &  2 & -5 \\ 
            6 &  1 & -8 &  8\end{array} \right]  \begin{array}{l}
[R_1] \\ 
{[R_2-\class{red}{1}R_1]} \\
{[R_3-\class{red}{(-2)}R_1]} \\
{[R_4-\class{red}{3}R_1]} \\
\end{array}
\sim 
\left[\begin{array}{rrrr}
            2 &  1 & -2 & 3 \\
            0 & -4 & -2 & 4 \\
            0 &  2 &  -2 & 1 \\ 
            0 & -2 & -2 &-1\end{array} \right]  \begin{array}{l}
[R_1] \\
[R_2] \\
{[R_3-\class{blue}{(-1/2)}R_2]} \\
{[R_4-\class{blue}{1/2}R_2]} \\
\end{array}
$$

$$
\sim
  \left[\begin{array}{rrrr}
            2 &  1 & -2 & 3 \\
            0 & -4 & -2 & 4 \\
            0 &  0 & -3 & 3 \\ 
            0 &  0 & -1 & -3
  \end{array} \right]  \begin{array}{l}
[R_1] \\
[R_2] \\
{[R_3]} \\
{[R_4-\class{green}{1/3}R_2]} \\
\end{array} 
\,\,\sim\,\,
    \left[\begin{array}{rrrr}
            2 &  1 & -2 & 3 \\
            0 & -4 & -2 & 4 \\
            0 &  0 & -3 & 3 \\ 
            0 &  0 & 0 & -4
    \end{array} \right]
\,\,=\,\, U.
$$

Putting every multiplier in its right place gives 

$$
   L = \left[\begin{array}{rrrr}
                    1       &       0 & 0 & 0 \\
            \class{red}{1}  &       1 & 0 & 0 \\
            \class{red}{-2} &  \class{blue}{-1/2} & 1 & 0 \\ 
            \class{red}{3}  &  \class{blue}{1/2} & \class{green}{1/3} & 1
        \end{array} \right].
$$

::::::


::::::{prf:example}
:label: Ex:LUdecomp:NoLU

For the matrix $A= \begin{bmatrix}
                    1 & 2 & 1 \\
                    4 & 8 & 6 \\
                    2 & 5 & 7
                  \end{bmatrix}$
the procedure breaks down at the second step.

$$
   \begin{bmatrix}
                    1 & 2 & 1 \\
                    4 & 8 & 6 \\
                    2 & 5 & 7
                  \end{bmatrix}
                  \begin{array}{l}
                      [R_1] \\ 
                      {[R_2-4R_1]} \\ 
                      {[R_3-2R_1]} 
                  \end{array} \quad \sim \quad
   \begin{bmatrix}
                    1 & 2 & 1 \\
                    0 & 0 & 2 \\
                    0 & 1 & 5
                  \end{bmatrix}. 
$$
The next logical step towards an echelon matrix would be a row swap.  But then the lower triangular structure of $L$ will be broken.  In {numref}`Subsection %s <Subsec:LUdecomp:PLUdecomp>`  we will study what we can do in such a situation.

::::::

Here's one to try for yourself.

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/089f5e1e-3e96-4be3-9c9c-3422a847ec72?id=109255
:label: grasple_exercise_3_6_T2
:dropdown:
:description: To compute the $LU$ decomposition of a 3x3 matrix $A$.

::::::


We collect a few properties of triangular matrices that have their value of their own right, and moreover will be used in the proofs of two properties of the $LU$ decomposition.

::::::{prf:proposition}
:label: Prop:LUdecomp:L-properties

Suppose $A$ and $B$ are lower triangular $n \times n$ matrices with $1$s on their diagonals.
Then the following properties hold.

::::{latexlist}
:enumerated: true
:type: i

\item $AB$ is also a lower triangular matrix with $1$s on its diagonal.

\item $A^{-1}$ is also a lower triangular matrix with $1$s on its diagonal.

::::

The same properties hold when each instance  of 'lower' in the above  is be replaced by 'upper'.


::::::



There are several ways to prove  {prf:ref}`Prop:LUdecomp:L-properties`.
The best would be to think of a proof yourself, but you can also have a peek at the exposition below.

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:LUdecomp:L-properties`
:class: tudproof, dropdown

:::{latexlist}
:enumerated: true
:type: i

\item  
Suppose $A$ and $B$ are lower triangular matrices with $1$s on their diagonals.

One way to prove that $AB$ also has these properties is to use the column-row expansion of the product.
(Cf. {numref}`Exc:MatrixOps:ColumnRowExpansion`.)  <br>
Let $A_{(k)}$ be the $k$th column of $A$, and $B^{(k)}$ the $k$th row of $B$.  
Then

$$
   A_{(k)} = \begin{bmatrix}0 \\ \vdots \\ 0 \\ a_{kk} \\ \vdots \\ a_{nk} \end{bmatrix} \quad
   \text{and} \quad 
    B^{(k)} = \begin{bmatrix}b_{k1} & \cdots &  b_{kk} & 0 & \cdots & 0 \end{bmatrix},
$$

where moreover  $a_{kk} = b_{kk} = 1$. So  the  $k$th term in the column-row expansion of $AB$ becomes

$$
\begin{array}{rcl}
     A_{(k)}B^{(k)} &=&
     \begin{bmatrix}b_{k1}A_{(k)} &  b_{k2}A_{(k)} &  \cdots &  b_{kk}A_{(k)} & \vect{0} & \cdots & \vect{0}\end{bmatrix} \\
     &=&
     \begin{bmatrix}
       0       &      0       & \cdots &        0    &    0      & \cdots &   0  \\
         \vdots   &     \vdots   &        & \vdots       &    \vdots      &  & \vdots \\
          0       &      0       & \cdots &     0       &   0       & \cdots  &   0    \\
      a_{kk}b_{k1} &  a_{kk}b_{k2} & \cdots & a_{kk}b_{kk} &    0    & \cdots &   0    \\
         \vdots   &     \vdots   &        &  \vdots     & \vdots  &        & \vdots \\
      a_{nk}b_{k1} &  a_{nk}b_{k2} & \cdots & a_{nk}b_{kk} &    0    & \cdots &   0  
     \end{bmatrix}
  \end{array}.
$$

This is a lower triangular matrix with a $1$ on position $(k,k)$ and for the rest $0$s on the diagonal.
Adding these $n$ column-row products gives a matrix of the required form.

\item
Next suppose that $A$ is an lower triangular matrix with $1$s on the diagonal.
If we apply the algorithm of {prf:ref}`Prop:MatrixInv:Algorithm` to find the inverse using the augmented matrix 

$$
  [\,A | I \,] = 
  \left[\begin{array}{ccccc|ccccc}  
     1   &   0    &    0   & \cdots &   0  & 1 & 0 & 0 & \cdots & 0 \\
  a_{21} &   1    &    0   & \cdots &   0  & 0 & 1 & 0 & \cdots & 0 \\
  a_{31} & a_{32} &    1   & \cdots &   0  & 0 & 0 & 1 & \cdots & 0 \\
  \vdots &\vdots  &        & \ddots &   \vdots  & \vdots & \vdots & & \ddots & \vdots \\[1ex] 
  a_{n1} &a_{n2}  & a_{n3} & \cdots &   1  & 0 & 0 & 0 & \cdots & 1
  \end{array} \right],
$$
to row reduce $A$ to $I$ we only need to subtract multiples of rows from rows below it.  Thus in the matrix to the right of the bar, where the identity matrix is transformed into the inverse matrix of $A$,  the triangular structure with $1$s on the diagonal remains.

:::

::::::




People that are not satisfied with two examples to show 
that  {prf:ref}`Alg:LUdecomp:LUalgorithm`  works can have a look at the following (informal) proof of 
{prf:ref}`Prop:LUdecomp:Existence`.  


:::::{admonition} Proof of&nbsp;{prf:ref}`Prop:LUdecomp:Existence`
:class: tudproof, dropdown

Suppose $A$ is an $n\times n$ matrix that can be row reduced top down to an  echelon matrix $U$ (which will then be an upper triangular). We can row reduce $A$ from top to bottom, where we use the same form as in {prf:ref}`Ex:LUdecomp:SecondLUSecondLook`. 
For instance the first two steps are


$$
  A  = \begin{bmatrix}
            a_{11} & a_{12}&  a_{13} & \ldots&   a_{1n}   \\
            a_{21} & a_{22}&   a_{23} & \ldots&   a_{2n}   \\
            a_{31} & a_{32}&   a_{33} & \ldots&   a_{3n}   \\
            \vdots &  \vdots&  \vdots& & \vdots    \\
            a_{n1} & a_{n2}&  a_{n3}& \ldots&   a_{nn}
       \end{bmatrix} = L_1A_2 
   =
   \begin{bmatrix}
            1      &      \\
            m_{21} &   1      \\
            m_{31} &  0   &  1     \\
            \vdots &  \vdots&   &  \ddots    \\
            m_{n1} & 0   &  \ldots&  & 1
    \end{bmatrix}A_2,
$$

where $A_2$ will be of the form

$$
  A_2 = \begin{bmatrix} a_{11} & a_{12} & a_{13} & \ldots & a_{1n} \\
                          0    & \tilde{a}_{22} &  \tilde{a}_{23} &  \ldots &\tilde{a}_{2n} \\
                          0    &    \tilde{a}_{32}     &  \tilde{a}_{33} & \ldots &\tilde{a}_{3n} \\ 
                          \vdots & \vdots &  \vdots & & \vdots \\
                          0    &    \tilde{a}_{n2}    &  \tilde{a}_{n3} & \ldots &\tilde{a}_{nn} \\ 
        \end{bmatrix}.
$$

The next step will lead to

$$
  A_2     = L_2A_3 = 
   \begin{bmatrix}
            1      &      \\
            0 & 1 &        \\ 
            0 &m_{32}   &  1     \\
            \vdots &  \vdots&  &   \ddots    \\
            0 & m_{n2} & 0   &  \ldots&  & 1
    \end{bmatrix}A_3,
$$


where $A_3$ will be of the form

$$
  A_3 = \begin{bmatrix} a_{11} & a_{12} & a_{13} & \ldots & a_{1n} \\
                          0    & \tilde{a}_{22} &  \tilde{a}_{23} &  \ldots &\tilde{a}_{2n} \\
                          0    &    0      &  \tilde{\tilde{a}}_{33} & \ldots &\tilde{\tilde{a}}_{3n} \\ 
                          \vdots & \vdots &  \vdots & & \vdots \\
                          0    &    0     &  \tilde{\tilde{a}}_{n3} & \ldots &\tilde{\tilde{a}}_{nn}
        \end{bmatrix}.
$$

We thus end up with a product

$$
  A = L_{n-1}L_{n-2}\cdots L_2L_1\,U = L\,U,
$$

where each matrix $L_k$ is a matrix containing the multipliers of the $k$th step in the proces.

The crucial thing is that in the product $L_{n-1}L_{n-2}\cdots L_2L_1$  in this order the multipliers do not 'interact'.   For instance, for $n = 4$, we would get 

::::{math}
:label: Eq:LUdecomp:multipliers

 \begin{array}{l} L = 
  \begin{bmatrix} 1 & 0 & 0 & 0 \\
                  m_{21} & 1 & 0 & 0  \\
                  m_{31} & 0 & 1 & 0  \\
                  m_{41} & 0 & 0 & 1  
        \end{bmatrix}
  \begin{bmatrix} 1 & 0 & 0 & 0 \\
                  0 & 1 & 0 & 0   \\
                  0 & m_{32} & 1 &  0 \\
                  0 & m_{42} & 0 & 1  
        \end{bmatrix}      
  \begin{bmatrix} 1 & 0 & 0 & 0 \\
                  0 & 1 & 0 & 0   \\
                  0 & 0 & 1 &  0 \\
                  0 & 0 & m_{43} & 1  
        \end{bmatrix} = \\
   =     
   \begin{bmatrix} 1 & 0 & 0 & 0 \\
                  m_{21} & 1 & 0 & 0  \\
                  m_{31} & 0 & 1 & 0  \\
                  m_{41} & 0 & 0 & 1  
        \end{bmatrix} 
  \begin{bmatrix} 1 & 0 & 0 & 0 \\
                  0 & 1 & 0 & 0   \\
                  0 & m_{32} & 1 &  0 \\
                  0 & m_{42} & m_{43} & 1  
        \end{bmatrix}  =
   \begin{bmatrix} 1 & 0 & 0 & 0 \\
                  m_{21} & 1 & 0 & 0  \\
                  m_{31} & m_{32} & 1 & 0  \\
                  m_{41} & m_{42} & m_{43} & 1  
        \end{bmatrix}. 
  \end{array}                     

::::

The pattern is clear, we skip the technical details to prove it for $n\times n$ matrices. 


To prove the converse, assume that $A$ has an $LU$ decomposition, i.e.,


$$
  A =  LU = 
     \left[\begin{array}{rrrrr}
                    1       &        &  &  \\
            \ell_{21}  &       1 &  &  \\
            \ell_{31}   &  \ell_{32} & 1 &   \\ 
            \vdots & \vdots & \vdots &  \ddots & \\ 
            \ell_{n1}   &  \ell_{n2}&  \ell_{n3} & \cdots & 1 \\ 
        \end{array} \right] \begin{bmatrix}
u_{11} & u_{12} & u_{13} & \cdots &u_{1n} \\
       & u_{22} & u_{23} & \cdots & u_{2n} \\
       & & u_{33} & \cdots & u_{3n} \\
      & &  &
\ddots & \vdots \\
& & & & u_{nn}
\end{bmatrix}.
$$

We then have to show that $A$ can be *top-down* row reduced to an echelon matrix.

By {prf:ref}`Prop:LUdecomp:L-properties` the inverse of $L$ has the same structure as $L$, i.e.,

$$
L^{-1} = \left[\begin{array}{rrrrr}
                    1       &        &  &  \\
            \ell^{\ast}_{21}  &       1 &  &  \\
            \ell^{\ast}_{31}   &  \ell^{\ast}_{32} & 1 &   \\ 
            \vdots & \vdots & \vdots &  \ddots & \\ 
            \ell^{\ast}_{n1}   &  \ell^{\ast}_{n2}&  \ell^{\ast}_{n3} & \cdots & 1 \\ 
        \end{array} \right].
$$ 

As in the proof of the first half of this proof (cf., {eq}`Eq:LUdecomp:multipliers`),  $L^{-1}$ can be factorized as       

$$
  L_1L_2\cdots L_{n-1} =
  \left[\begin{array}{rrrrr}
                    1       &        &  &  \\
            \ell^{\ast}_{21}  &       1 &  &  \\
            \ell^{\ast}_{31}   &  0 & 1 &   \\ 
            \vdots & \vdots & \vdots &  \ddots & \\ 
            \ell^{\ast}_{n1}   &  0 &  0 & \cdots & 1 \\ 
        \end{array} \right]
  \left[\begin{array}{rrrrr} 
              1       &        &  &  \\
              0     &       1 &  &  \\
              0 &  \ell^{\ast}_{32} & 1 &   \\ 
            \vdots & \vdots & \vdots &  \ddots & \\ 
              0 &  \ell^{\ast}_{n2}&  0 & \cdots & 1 \\ 
        \end{array} \right] 
        \cdots
   \left[\begin{array}{ccccc}
              1     &        &  &  &\\
              0     &   1    &  &  &\\
              0     &   0    & 1 & &  \\ 
            \vdots  & \vdots & \vdots &  \ddots & \\ 
              0     &   0 &  \cdots & \ell^{\ast}_{n,n-1} & 1 \\ 
        \end{array} \right]           
$$

Pre-multiplication of a matrix $M$ with one of the matrices  $L_k$  amounts to adding multiples of the $k$th row of $M$ to the lower rows. So the product $L_1L_2L_3\cdots L_{n-1}$ is a series of top-down operations,
and

$$
   L_1L_2L_3\cdots L_{n-1}\, A =  U
$$

amounts to a top-down row reduction of $A$ to the upper triangular matrix $U$.

::::::



The uniqueness issue is not of major importance, but for completeness' sake we phrase it in a proposition, followed by a possible argument to prove it. 

::::::{prf:proposition}
:label: Prop:LUdecomp:Uniqueness

For an invertible matrix $A$, if it has an $LU$ decomposition, it will be unique.

::::::


::::::{admonition} Proof of {prf:ref}`Prop:LUdecomp:Uniqueness`.
:class: tudproof, dropdown

Suppose $A$ is an invertible matrix with two $LU$ decompositions

$$
  A = L_1U_1, \quad A = L_2U_2.
$$

We then have to show that 

$$
  L_1=L_2  \quad \text{and} \quad  U_1 = U_2.
$$

Since $A$ is invertible, the matrices $U_1, U_2$ are also invertible. (The matrices $L_1$ and $L_2$ are always invertible, c.f., {prf:ref}`Def:LUdecomp:DefinitionLU`.) <BR>
From

$$
L_1U_1 = L_2U_2
$$

it follows that

::::{math}
:label: Eq:LUdecomp:EqualityL1L2U1U2

  L_2^{-1}L_1 = U_2U_1^{-1}.
::::

From {prf:ref}`Prop:LUdecomp:L-properties` we know that $L_2^{-1}$ is a lower triangular matrix with $1$s on the diagonal,
and that the product $L_2^{-1}L_1$ is also of this form. At the same time the product $U_2U_1^{-1}$ must be an upper triangular matrix with $1$s on its diagonal.  Then {eq}`Eq:LUdecomp:EqualityL1L2U1U2` implies that

$$
 L_2^{-1}L_1 = U_2U_1^{-1} = I,
$$

from which the identities

$$
 L_1 = L_2, \quad U_1 = U_2 
$$

immediately follow.

::::::

Lastly we give an example to show that the uniqueness may fail for a singular matrix.

::::::{prf:example}
:label: Eq:LUdecomp:NonUniqueLU

For the matrix  $A = \begin{bmatrix} 1 & 1 & 1 \\ 2 & 2 & 2 \\ 3 & 3 & 3 \end{bmatrix}$ it holds that

$$
   A = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 3 & a & 1 \end{bmatrix}\begin{bmatrix} 1 & 1 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix},
$$

where the parameter $a$ is free to choose.
::::::

(Subsec:LUdecomp:PLUdecomp)=

## Generalization to non-square matrices and $PLU$ decomposition

In this section we describe what can be said regarding $LU$ decompositions for non-square matrices,
and present a 'workaround' for matrices for which there is no top-down row reduction to echelon form. 

We start with an example to show that not much changes if we apply  {prf:ref}`Alg:LUdecomp:LUalgorithm` to non-square matrices. 

::::::{prf:example}
:label: Ex:LUdecomp:Nonsquare

The matrix $A$ is given by 

$$
A =
\begin{bmatrix}
1  &  3 &  1 & -1 \\
-1 &  1 &  1 &  2 \\
 2 & -2 & -1 &  3
\end{bmatrix}.
$$

We can row reduce $A$ top-down to an echelon matrix:

$$
\begin{array}{rcl}
\begin{bmatrix}
1  &  3 &  1 & -1 \\
-1 &  1 &  1 &  2 \\
 2 & -2 & -1 &  3
\end{bmatrix}
\begin{array}{l}
[R_1] \\
{[R_2-\class{blue}{(-1)}R_1]} \\
{[R_3-\class{blue}{2}R_1]} \\
\end{array}
& \sim &
\begin{bmatrix}
1  &  3 &  1 & -1 \\
0  &  4 &  2 &  1 \\
0  & -8 & -3 &  5
\end{bmatrix}
\begin{array}{l}
[R_1] \\
{[R_2]} \\
{[R_3-\class{blue}{(-2)}R_2]} \\
\end{array}\\
&\sim&
\begin{bmatrix}
1  &  3 &  1 & -1 \\
0  &  4 &  2 &  1 \\
0  &  0 &  1 &  7
\end{bmatrix}.
\end{array}
$$

We then have

$$
  A = LU = \begin{bmatrix}
1  &  0 & 0 \\ \class{blue}{-1} &  1 &  0  \\  \class{blue}{2} & \class{blue}{-2} & 1 \end{bmatrix}
\begin{bmatrix}
1  &  3 &  1 & -1 \\
0  &  4 &  2 &  1 \\
0  &  0 &  1 &  7
\end{bmatrix}.
$$

::::::


The two-step procedure as in  {prf:ref}`Alg:LUdecomp:Usefulness` to solve a linear system $LU\vect{x} = \vect{b}$ is also feasible for non-square matrices, as the next example shows


::::::{prf:example}
:label: Ex:LUdecomp:Nonsquare

We will solve the equation 

$$
    A\vect{x}= \vect{b},
$$

where

$$
  A = LU = \begin{bmatrix}
1  &  0 & 0 \\ -1 &  1 &  0  \\  2 & -2 & 1 \end{bmatrix}
\begin{bmatrix}
1  &  3 &  1 & -1 \\
0  &  4 &  2 &  1 \\
0  &  0 &  1 &  7
\end{bmatrix} \quad \text{and} \quad \vect{b} = \begin{bmatrix}2 \\ -2 \\ 5 \end{bmatrix}.
$$


First we solve  the system

$$
  L\vect{y} = \begin{bmatrix}
1  &  0 & 0 \\ -1 &  1 &  0  \\  2 & -2 & 1 \end{bmatrix}\vect{y} =
  \begin{bmatrix}2 \\ -2 \\ 5 \end{bmatrix}.
$$

Using forward substitution we find the solution

$$
  \tilde{\vect{y}} = \begin{bmatrix}2 \\ 0 \\ 1 \end{bmatrix} 
$$

and then the system

$$
  U\vect{x} = \begin{bmatrix}
1  &  3 &  1 & -1 \\
0  &  4 &  2 &  1 \\
0  &  0 &  1 &  7\end{bmatrix}\vect{x} = 
   \begin{bmatrix}2 \\ 0 \\ 1 \end{bmatrix}
$$

gives the solution(s)

$$
  \vect{x} = \begin{bmatrix}
    \tfrac52 -\tfrac{7}{4}x_4\\
    -\tfrac12 +\tfrac{13}{4}x_4\\
     1 - 7x_4\\
     x_4
  \end{bmatrix}, \quad  x_4 \,\, \text{free.}
$$

::::::


The generalization of {prf:ref}`Prop:LUdecomp:Existence` to non-square matrices is captured in the next proposition.

::::::{prf:proposition}
:label: Prop:LUdecomp:ExistenceNonsquare

An $m\times n$ matrix $A$, with $m \leq n$ can be written as $A = LU$, with 

<ul>

<li>

$L =  \begin{bmatrix} 1 &   \\
                  \ell_{21} & 1 &  \\
                  \ell_{31} & \ell_{32} & 1   \\
                   \vdots  & \vdots & \vdots & \ddots &  \\
                  \ell_{m1} & \ell_{m2} & \ell_{m3} & \cdots & 1  
        \end{bmatrix}$,
        
 

</li>       
 </ul>       

an $m\times m$ upper triangular matrix  with $1$s on its diagonal,        

and  
        

<ul>
<li>

$U =\begin{bmatrix}
u_{11} & u_{12} & u_{13} & \cdots &u_{1m} & \cdots & u_{1n}  \\
      & u_{22} & u_{23} & \cdots & u_{2m} & \cdots & u_{2n} \\
      &      & u_{33} & \cdots & u_{3m} & \cdots & u_{3n} \\
      &      &        &  \ddots & \vdots \\
      &      &        &         & u_{mm} & \cdots & u_{mn} 
\end{bmatrix}$  &nbsp;  an echelon matrix

</li>

</ul>

if and only if $A$  can be  row reduced top-down to the echelon matrix $U$. 


Moreover, if the rows of $A$ are linearly independent the matrices $L$ and $U$ are unique.

::::::

A similar proposition holds for $m \times n$ matrices with $m > n$.  However, in this case the systems
$A\vect{x} = \vect{b}$ are inconsistent for most vectors $\vect{b}$, and then other techniques come into play  (e.g., see {numref}`SubSec:LeastSquares:LS-solutions`).

In the remainder of this subsection we address the next best thing we can do in case a matrix does not have an $LU$ decomposition.


::::::{prf:example}
:label: Ex:LUdecomp:NoLUcontinued

Let us return to {prf:ref}`Ex:LUdecomp:NoLU` where the matrix $A$  cannot be written as $LU$.
We copy from there

$$
   A \,=\, \begin{bmatrix}
                    1 & 2 & 1 \\
                    4 & 8 & 6 \\
                    2 & 5 & 7
                  \end{bmatrix}               
                  \begin{array}{l}
                      [R_1] \\ 
                      {[R_2-4R_1]} \\ 
                      {[R_3-2R_1]} 
                  \end{array} \quad \sim \quad
   \begin{bmatrix}
                    1 & 2 & 1 \\
                    0 & 0 & 2 \\
                    0 & 1 & 5
                  \end{bmatrix}. 
$$

We need a row swap to bring the last matrix to echelon form.  The key idea is to **perform all the row exchanges first** and **then add multiples of  rows (top-down) to other rows** to obtain an echelon form.  
Here the one row exchange, swapping row 2 and row 3,  is captured by the matrix

$$
   P = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0  \end{bmatrix}.
$$


We get

$$
   PA \,=\, \begin{bmatrix}
                    1 & 2 & 1 \\
                    2 & 5 & 7 \\
                    4 & 8 & 6
                  \end{bmatrix}  \,\, = \,\, 
             \begin{bmatrix}
                    1 & 0 & 0 \\
                    2 & 1 & 0 \\
                    4 & 0 & 1
                  \end{bmatrix}\,      
             \begin{bmatrix}
                    1 & 2 & 1 \\
                    0 & 1 & 5 \\
                    0 & 0 & 2
                  \end{bmatrix}.       
$$


This is what we will call a $PLU$ decomposition  (a *permuted* $LU$ decomposition). 

<!--
Note that first subtracting row 1 four times from row 2 and two times from row 3, followed by exchanging row 2 and row 3 leads to the same echelon matrix as first swapping row 2 and 3 and then subtracting row 1  two times from row 2 and four times from row 3.
-->

::::::



A series of row swaps may lead to any reordering of the rows of a matrix. 
In mathematics the word for reordering is *permutation*, and the action of reordering can be accomplished via 
a multiplication with a permutation matrix $P$.  Before we continue with the $PLU$ decomposition we define this 
concept and derive some of its properties.

::::::{prf:definition}
:label: Def:LUdecomp:PermutationMatrix

A **permutation matrix** is an $n \times n$ matrix $P$ with only entries $0$ and $1$ in such a way that each row and each column contain exactly one $1$.

::::::

::::::{prf:example}

Two $4\times 4$ permutation matrices are

::::{math}
:label: Eq:LUdecomp:P1andP2

  P_1 = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 
          \end{bmatrix} \quad \text{and} \quad 
  P_2 = \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 
           \end{bmatrix}
::::

Note that for an arbitrary $4 \times 4$ matrix $A$ we have

$$
  P_1 A = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ \class{blue}{0} & \class{blue}{0} & \class{blue}{0} & \class{blue}{1} \\ \class{red}{0} & \class{red}{0} & \class{red}{1} & \class{red}{0} 
          \end{bmatrix}
        \begin{bmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ 
                        \class{red}{a_{31}} & \class{red}{a_{32}} & \class{red}{a_{33}} & \class{red}{a_{34}} \\ 
                        \class{blue}{a_{41}} & \class{blue}{a_{42}} & 
                        \class{blue}{a_{43}} & \class{blue}{a_{44}}
          \end{bmatrix}   =
        \begin{bmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ 
                        \class{blue}{a_{41}} & \class{blue}{a_{42}} & 
                        \class{blue}{a_{43}} & \class{blue}{a_{44}} \\ 
                        \class{red}{a_{31}} & \class{red}{a_{32}} & \class{red}{a_{33}} & \class{red}{a_{34}} 
          \end{bmatrix}   
$$

and

$$
  P_2 A = \begin{bmatrix} \class{blue}{0} & \class{blue}{1} & \class{blue}{0} & \class{blue}{0} \\ \class{red}{0} & \class{red}{0} & \class{red}{1} & \class{red}{0} \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 
            \end{bmatrix} 
          \begin{bmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ 
                          \class{blue}{a_{21}} & \class{blue}{a_{22}} & 
                          \class{blue}{a_{23}} & \class{blue}{a_{24}} \\ 
                          \class{red}{a_{31}} & \class{red}{a_{32}} & 
                          \class{red}{a_{33}} & \class{red}{a_{34}} \\ 
                          a_{41} & a_{42} & a_{43} & a_{44}
            \end{bmatrix}   = 
          \begin{bmatrix} \class{blue}{a_{21}} & \class{blue}{a_{22}} & 
                          \class{blue}{a_{23}} & \class{blue}{a_{24}} \\ 
                          \class{red}{a_{31}} & \class{red}{a_{32}} & 
                          \class{red}{a_{33}} & \class{red}{a_{34}} \\ 
                          a_{41} & a_{42} & a_{43} & a_{44} \\a_{11} & a_{12} & a_{13} & a_{14}
            \end{bmatrix}  
$$

In general (pre-)multiplication of a matrix $A$ with any permutation matrix reorders the rows of $A$. 
Try to convince yourself why this is so.

::::::


The following properties of permutation matrices come in handy.


::::::{prf:proposition}
:label:  Prop:LUdecomp:PermutationMatrices

:::{latexlist}
:enumerated: true
:type: i

\item The product of two $n\times n$ permutation matrices is again a permutation matrix.
\label{Item:Prop:LUdecomp:PermutationMatrices_Product}

\item The inverse of a permutation matrix is its transpose.  
\label{Item:Prop:LUdecomp:PermutationMatrices__Inverse}

:::

::::::

The following example provides some illustrations. 
And the interested reader may open the proof below it.


::::::{prf:example}

For the matrices $P_1$ and $P_2$ from {eq}`Eq:LUdecomp:P1andP2`  we have

$$
  P_1P_2 = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 
          \end{bmatrix}  
           \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 
           \end{bmatrix}
           =
           \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 
           \end{bmatrix}
$$

and

$$
  P_2^TP_2 = \begin{bmatrix} 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 
            \end{bmatrix}  
             \begin{bmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ 1 & 0 & 0 & 0 
           \end{bmatrix}
           =
             \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\  0 & 0 & 0 & 1 
           \end{bmatrix}.
$$

Note that from the second identity it follows that  $P_2^{-1} = P_2^T$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:LUdecomp:PermutationMatrices`
:class: tudproof, dropdown

:::{latexlist}
:enumerated: true
:type: i

\item The product of two $n\times n$ permutation matrices is again a permutation matrix.


Suppose $P_1$ and $P_2$ are permutation matrices. With the product  $P_1P_2$ the rows of $P_2$ are reordered,  and that leaves 
the three defining properties a $1$ in each row, a $1$ in each column, all other entries equal to $0$,  intact.


\item The inverse of a permutation matrix is its transpose.  Thus,  $P^{-1} = P^T$.

In a product  $A^TA$, the entry on position $(i,j)$ is the inner product of the $i$th column of $A$
with the $j$th column of $A$.  (Cf., {numref}`Exc:MatrixOps:InterpretATB`.) 
 Since the $n$ columns of $P$ are the $n$ =  columns  $\vect{e}_j$  of the identity matrix (in some order),  and  

$$
    (\vect{e}_i)^T\vect{e}_j =\vect{e}_i\ip\vect{e}_j  = \left\{\begin{array}{l}
                                    1, \,\,\text{if}\,\, i = j\\
                                    0, \,\,\text{if}\,\, i \neq j,     
                                      \end{array}
                              \right.
$$

the result immediately follows.

:::

::::::

::::::{prf:theorem} Existence of a $PLU$ Decomposition
:label: LUDecomp:existencePLU

Suppose that $A$ is an $m\times n$ matrix with real coefficients, and let $m \leq n$. Then there exist a permutation matrix $P$, a lower triangular matrix $L$ and an echelon matrix $U$ such that

$$ 
  PA = LU. 
$$

As before, $L$ may be constructed in such a way that it has $1$'s on its diagonal.
::::::

::::::{prf:remark} 

As was mentioned before, the key idea is to perform the row exchanges first. These can be put together in the permutation matrix $P$. The algorithm to actually find the $LU$ decomposition of $PA$ without doing the whole row reduction process for $PA$ all over again is rather intricate, and in our view belongs to a course of numerical linear algebra.  There it will be explained that it may also be preferable to work towards a $PLU$ decomposition instead of an $LU$ decomposition in cases where theoretically it is not absolutely necessary.  For numerical reasons, having to do with finite accuracy when representing real numbers in computers, it may be better to choose the pivots in another order than just top-down.

::::::

In the following example the matrix does have a proper $LU$ decomposition, but we will row reduce it
in another order than top-down to echelon form. It is a tiny example to illustrate that it is possible to deduce a $PLU$ decomposition from it when we keep record of both the multipliers and the positions of the pivots.

::::::{prf:example}
:label: Ex:LUdecomp:PLUexample-2

We will row reduce the matrix $ A= \begin{bmatrix}2&4&3 \\ 1&2&3\\1&3&2 \end{bmatrix}$ in an alternative order than top-down and extricate a $PLU$ decomposition from it.

$$
\left[\begin{array}{rrr}2&4&3 \\ 1&2&3\\ \fbox{$1$}&3&2 \end{array} \right]  \begin{array}{l}
[R_1-\class{blue}{2}R_3] \\
{[R_2-\class{blue}{1}R_3]} \\
{[R_3]} \\
\end{array}
\sim
\left[\begin{array}{rrr}0&\fbox{$-2$}&-1 \\ 0 & -1 &1 \\ 1&3&2\end{array} \right]  \begin{array}{l}
[R_1] \\
{[R_2-\class{red}{\frac12}R_1]} \\
{[R_3]} \\
\end{array}
\sim
\left[\begin{array}{rrr}0&-2&-1 \\ 0 & 0 &\fbox{$\frac32$} \\ 1&3&2\end{array} \right],
$$

where we have put boxes at the pivot positions.

If we put together the matrices that describe the row operations we get

:::{math} 
:label: Eq:LUdecomp:PivotStructure

 A = \begin{bmatrix}2&\fbox{$4$}&3 \\ 1&2&\fbox{$3$}\\ \fbox{$1$}&3&2\end{bmatrix} =
     \begin{bmatrix} 1 & 0 & \class{blue}{2} \\ \class{red}{\frac12} &1 & \class{blue}{1} \\ 0 & 0 & 1\end{bmatrix}
     \begin{bmatrix} 0 & -2 & -1 \\ 0 & 0 &\frac32  \\1 & 3 & 2\end{bmatrix} = \tilde{L}\tilde{U}.

:::

If we would have started from

$$
  \begin{bmatrix} 1&3&2 \\2&4&3 \\ 1&2&3\end{bmatrix} = PA = 
   \begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0\end{bmatrix} 
   \begin{bmatrix} 2&4&3 \\ 1&2&3\\1&3&2 \end{bmatrix}
$$

using the same pivots would have arrived at

$$
  \begin{bmatrix} 1&3&2 \\2&4&3 \\ 1&2&3\end{bmatrix} \sim 
  \begin{bmatrix} 1&3&2 \\0&-2&-1 \\ 0&-1&1\end{bmatrix} \sim
  \begin{bmatrix} 1&3&2 \\0&-2&-1 \\ 0&0&\frac32\end{bmatrix}, 
$$

so

$$
  PA = \begin{bmatrix} 1&3&2 \\2&4&3 \\ 1&2&3\end{bmatrix}  =
  \begin{bmatrix} 1 & 0 & 0 \\\class{blue}{2} & 1 & 0 \\ 
                  \class{blue}{1} & \class{red}{\frac12} & 1\end{bmatrix} 
  \begin{bmatrix} 1&3&2 \\0&-2&-1 \\ 0&0&\frac32\end{bmatrix} = LU. 
$$

The matrix $P$ is the inverse of (so also the transpose of) the matrix that describes the positions of the pivots as in Equation {eq}`Eq:LUdecomp:PivotStructure`. 
It asks for some careful analysis how to reconstruct $L$ from $\tilde{L}$.

::::::




<!-- 
## Efficiency Issues

To be filled in later.

-->


## Grasple Exercises

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/cca386f8-a6ff-44b6-9b83-fe96482a4763?id=108857
:label: grasple_exercise_3_6_2
:dropdown:
:description: To identify triangular matrices.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4ef9b6fe-e204-44e7-9463-3e1c3537a10b?id=82913
:label: grasple_exercise_3_6_3
:dropdown:
:description: To compute the $LU$ decomposition of a 2x2 matrix $A$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b167deea-922f-4a80-9b3e-7cbdf16f023f?id=106332
:label: grasple_exercise_3_6_4
:dropdown:
:description: To compute the $LU$ decomposition of a 3x3 matrix $A$.

::::::


::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9708bce4-5c01-4486-8f44-7ea3a5157950?id=82914
:label: grasple_exercise_3_6_5
:dropdown:
:description: To compute the $LU$ decomposition of a 3x3 matrix $A$ and use it to solve $A\vect{x} = \vect{b}$.

::::::


::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d7ec03b4-32c4-4c3e-8c1e-2714878ef558?id=82917
:label: grasple_exercise_3_6_6
:dropdown:
:description: To compute the $LU$ decomposition of a 3x3 matrix $A$ and use it to solve $A\vect{x} = \vect{b}$.

::::::




::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8fe1ca5c-3f24-4148-9725-a96c44e3f43a?id=82920
:label: grasple_exercise_3_6_8
:dropdown:
:description: To compute $A^{-1}$ using  $A = LU$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7d8c3553-18cd-4866-bfa1-9ff273ee18e8?id=82925
:label: grasple_exercise_3_6_9
:dropdown:
:description: Explorative exercise about the $LDU$ decomposition.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5bb6dcac-4575-4953-bb3a-c0e8d4594798?id=82928
:label: grasple_exercise_3_6_10
:dropdown:
:description: To compute the $LU$ decomposition of 3x4 matrix $A$ and use it to solve $A\vect{x} = \vect{b}$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9a2cb913-3462-4832-8e33-9f4b878f1da7?id=106804
:label: grasple_exercise_3_6_11
:dropdown:
:description: To compute a $PLU$ decomposition of a 3x3 matrix.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/48ef4fa5-cdcf-4449-8c5a-0d5f5d448025?id=106870
:label: grasple_exercise_3_6_12
:dropdown:
:description: To solve a system $A\vect{x} = \vect{b}$ using $ PA = LU$.

::::::
## Efficiency Issues

One way to measure the performance of an algorithm is to count the number of arithmetic operations <!-- [^flopnote] -->
that are necessary for solving a problem. By arithmetic operations we will take into account in this setting additions, multiplications and divisions. 

Let us first compute this number when we solve the (square) linear system $A\mathbf{x}=\mathbf{b}$ by taking the augmented matrix $[ A | \vect{b}]$, find an echelon form and then use  backward substitution. Let us suppose that the matrix $A$ is invertible and possesses an $LU$ decomposition.

In the worst-case scenario, for a $3\times 3$ matrix $A$, (so a $3\times 4$ augmented matrix), we need the following number of arithmetic operations:

<ul>
<li>

To convert the components $a_{21}$ and $a_{31}$ to a zero value, we need to <BR>
compute two multipliers $m_{21}$ and $m_{31}$ (2 divisions), then we need to <BR>
multiply each component of the first row, starting at $a_{12}$, by each $m_{i1}$ (this happens twice, so $2\times 3=6$ products) and then we need to <BR>
subtract the resulting values to the corresponding components in each row ($2\times 3=6$ subtractions). <BR>
Therefore, we need a total of $14$ arithmetic operations (8 products/divisions and 6 additions/subtractions).

</li>
</ul>

The result:

$$
  \begin{bmatrix}a_{11} & a_{12} &a_{12} &b_{1} \\ a_{21} & a_{22} &a_{23} &b_{2} \\ a_{31} & a_{32} &a_{33} &b_{3} 
  \end{bmatrix} \sim
  \begin{bmatrix}a_{11} & a_{12} &a_{12} &b_{1} \\ 
  0 & a_{22}-m_{21}a_{12} &a_{23}-m_{21}a_{13} &b_{2}-m_{21}b_{1} \\ 
  0 & a_{32}-m_{31}a_{12} &a_{33}-m_{31}a_{13} &b_{3}-m_{31}a_{1} 
  \end{bmatrix}  
$$

<ul>
<li>

To convert the component $a_{32}$ to a zero value, we need to compute the multiplier  $m_{32}$
(one division), then we need to multiply each component of the second row starting at $a_{23}$ (this asks for 2 products), and then we need to subtract the resulting values to the corresponding components in the third row (2 subtractions). This gives 5 arithmetic operations.

</li>
</ul>



So just to bring the augmented matrix to an echelon form requires 19 arithmetic operations (11 multiplications/divisions and 8 additions/subtractions).



Next, to solve the system we use backward substitution.

<ul>

<li>

To find $x_3$ requires one  division.

</li>

<li>

To find $x_2$ requires one multiplication, one subtraction and one division.

</li>

<li>

To find $x_1$ requires two multiplications, two subtractions and one division.<BR>
Namely,  $x_1 = (b_1-a_{12}x_2-a_{13}x_3)/a_{12}$.
</li>
</ul>


So in total, we needed $19+9=28$ arithmetic operations.

Supposing that $A=LU$ and that $L$ and $U$ are given, then, we solve first $L\mathbf{y}=\mathbf{b}$ and then $U\mathbf{x}=\mathbf{y}$.

<ul>
<li>

For $L\mathbf{y}=\mathbf{b}$ we use forward substitution. Since the elements in the main diagonal are ones, then we have that we need no operations to determine $y_1$, we need one multiplication and one subtraction for $y_2$, and two multiplication and two subtractions for $y_3$. Namely,

$$
  y_1 = b_1, \quad y_2 = b_2 - \ell_{21}y_1, \quad y_3 = b_3 - \ell_{31}y_1 - \ell_{32}y_2
$$

This totals 6 arithmetic operations.

</li>
<li>

To solve $U\mathbf{x}=\mathbf{y}$ we use backward substitution, and we have just seen that it requires 9 arithmetic operations.  (Which is 3 more than with the forward substitution because of the three divisions by the pivots $u_{ii}$.)

</li>
</ul>

So when the matrix $A$ is already $LU$ factorised, the number of operations required to solve the system is significantly lower. In the situation just analysed we found $15$ versus $28$.

Similar computations  for a non-singular $n\times n$ matrix $A$ leads to the following results.


::::::{prf:proposition}
:label: Prop:LUdecomp:CountOperations

Suppose $A$ is an invertible $n\times n$ matrix and $\vect{b}$ an arbitrary vector in $\R^n$.

:::::{latexlist}
:enumerated: true
:type: i

\item Row reduction  of  $A$ to echelon form requires  $\frac23n^3-\frac12n^2-\frac16n$ (arithmetic) operations.
\item  Row reduction of the augmented matrix  $[A | \vect{b}]$ to echelon form 
requires $\frac23n^3+\frac12n^2-\frac76n$  operations.
\item  Solving a linear system  $L\vect{y} = \vect{b}$ for  an $n \times n$  lower triangular matrix $L$ with $1$s on the diagonal requires  $n(n-1)$ operations.
\item Solving a linear system  $U\vect{x} = \vect{y}$ for  an $n \times n$  upper triangular matrix $U$  requires  $n^2$ operations.
\label{Item:Prop:LUdecomp:BasicProp:Transpose}
:::::



From ii  and iv it follows that solving the system  $A\vect{x} = \vect{b}$ by 
row reduction + backward substitution requires

$$
 \frac23n^3+\frac12n^2 -\frac76n + n^2 = \frac{4n^3+9n^2-7n}{6} 
$$

arithmetic operations.


From iii  and iv it follows that solving the system  $LU\vect{x} = \vect{b}$ requires

$$
  n(n-1) + n^2= 2n^2 - n
$$

arithmetic operations.

::::::



::::::{prf:remark}

Note that first row reducing the augmented matrix $[A | \mathbf{b}]$ to echelon form 
$[U | \tilde{\mathbf{b}}]$ and then solve  $U\mathbf{x} = \tilde{\mathbf{b}}$  by backward substituion
asks for the same number of arithmetic operations as first finding an $LU$-decomposition and then solve the two ensuing systems with forward and backward substition.  Specifically

$$
  \frac{4n^3+9n^2-7n}{6}  = \frac23n^3-\frac12n^2-\frac16n  + 2n^2 - n.  
$$ 
::::::


<!-- 
:::::{latexlist}
:enumerated: true
:type: i


\item Row reduction  of  $A$ to echelon form requires  $\frac23n^3-\frac12n^2\-\frac16n$ (arithmetic) operations
\item Row reduction of the augmented matrix  $[A | \vect{b}]$ to echelon form requires $\frac23n^3+\frac32n^2\-\frac76n$  operations.
\item Solving linear system  $L\vect{y} = \vect{b}$ for  an $n \times n$  lower triangular matrix $L$ with $1$s on the diagonal requires  $n(n-1)$ operations.
\item Solving linear system  $U\vect{y} = \vect{b}$ for  an $n \times n$  upper triangular matrix $L$ with $1$s on the diagonal requires  $n^2$ operations.
     
:::::

From ii  and iii it follows that solving the system  $A\vect{x} = \vect{b}$ by row reduction + backward substitution requires

$$
 \frac23n^3+\frac32n^2\-\frac76n + n(n-1) = \frac{4n^3+9n^2-13n}{6} 
$$

arithmetic operations.


From iii  and iv it follows that solving the system  $LU\vect{x} = \vect{b}$ requires

$$
  n(n-1) + n^2= 2n^2 - n
$$

arithmetic operations.



::::::

-->


<!--
:::{prf:remark}

The total number of arithmetic operations needed in order to solve a linear system with row reduction (without exchanging rows), and with $LU$ is the same. We leave the proof as an exercise for the reader.

:::
-->



In many applications in engineering, it is required to solve many, say $N$, linear systems  
$A\vect{x}=\vect{b}_i$, with the same coefficient matrix $A$,  where typically the vectors $\vect{b}_i$ are not known beforehand.
In this situation the $LU$ decomposition comes in handy.  Instead of solving the systems one by one, we can first find an $LU$-decomposition, and then solve the systems  $LU\vect{x}=\vect{b}_i$. 
If we compare solving $m$ linear systems with row reduction ($RR$) and 
with $LU$ decomposition ($LU$), we get

$$
   N\cdot\left(\frac{4n^3+9n^2-7n}{6}\right)  \quad (RR) 
$$

versus

$$
   \frac{4n^3-3n^2-n}{6} + N\cdot(2n^2-n) \quad (LU).
$$




In {numref}`tbl:comparison_gausselim_LU` we can see the comparison in the numbers of operations needed to solve several linear systems when using row reduction and $LU$ decomposition.

:::::{latextable} Comparison between solving linear systems by row reduction  or by $LU$ decomposition.
:header-rows: 2
:class: longtable table-bordered table-striped table-hover table
:align: right
:name: tbl:comparison_gausselim_LU


%\begin{tabular}{crrrrrr}
%$n$ & \multicolumn{2}{c}{$N=5$} & \multicolumn{2}{c}{$N=10$} & \multicolumn{2}{c}{$N=50$} \\
%& $RR$ & $LU$ & $RR$ & $LU$ & $RR$ & $LU$ \\
%$3$ & $140$ & $88$ & $280$ & $163$ & $1400$ & $763$ \\
%$10$ & $4,025$ & $1,565$ & $8,050$ & $2,515$ & $40,250$ & $10,115$ \\
%$100$ & $3.4\cdot10^6$ & $7.6\cdot10^5$ & $6.8\cdot10^6$ & $8.6\cdot10^5$ & $3.4\cdot10^7$ & $1.7\cdot10^6$ \\
%\end{tabular}


\begin{tabular}{crrrrrr}
$n$ & \multicolumn{2}{c}{$N=5$} & \multicolumn{2}{c}{$N=10$} & \multicolumn{2}{c}{$N=50$} \\
& $RR$ & $LU$ & $RR$ & $LU$ & $RR$ & $LU$ \\
$3$ & $140$ & $88$ & $280$ & $163$ & $1400$ & $763$ \\
%$5$ & $575$ & $295$ & $1,150$ & $520$ & $5,750$ & $2,320$ \\
$10$ & $4,025$ & $1,565$ & $8,050$ & $2,515$ & $40,250$ & $10,115$ \\
$100$ & $3.4\cdot10^6$ & $7.6\cdot10^5$ & $6.8\cdot10^6$ & $8.6\cdot10^5$ & $3.4\cdot10^7$ & $1.7\cdot10^6$ \\
\end{tabular}


:::::


We will mention one other advantage the $LU$ decomposition may have, namely when the coefficient matrix $A$ is a **band matrix**. In that case it is much more efficient to work with the $LU$ decomposition than with the inverse.
Such systems $A\vect{x} = \vect{b}$ for instance appear when (partial) differential equations are solved via discretizations. It falls outside the scope of this textbook to go into the details, but we consider the special case of  **tridiagonal** matrices to illustrate once more the usefulness of the $LU$ decomposition.


::::::{prf:definition}
:label: Def:LUdecomp:Tridiag

A **band matrix**  of **width** $d \geq 0$ is a matrix where only the entries  within a  distance $d$ from the diagonal are nonzero. So,  $a_{ij} = 0$  if  $|i-j|>d$. 
A **tridiagonal** matrix  $A$  is a band matrix of width 1.

::::::


::::::{prf:example}
:label: Ex:LUdecomp:Tridiag

Three examples of band matrices are

$$
   A = \begin{bmatrix} 2 & 1 & 0 & 0 \\ 1 & 3 & 2 & 0\\ 0 & 2 & 5 & 4 \\ 0 & 0 & 6 & 5
   \end{bmatrix}, \quad
   B = \begin{bmatrix} 2 & 1 & 1 & 0 & 0 \\ 1 & 3 & 2 & 2 & 0\\ 1 & 2 & 1 & 4 & 3\\ 0 & 4  & 0 & 2 & 1 \\ 0 & 0 & 3 & 3 & 5
   \end{bmatrix}
   \quad \text{and}  \quad 
   U = \begin{bmatrix}  1 & 1 & 0 & 0 \\ 0 & 2 & 2 & 0 \\ 0 & 0 & 3 & 4 \\ 0 & 0 & 0 & 5
   \end{bmatrix}.
$$

$A$ is a tridiagonal matrix, matrix $B$ is a band matrix of width 2, and the third
matrix is both upper triangular and tridiagonal.

::::::

::::::{prf:proposition}
:label: Prop:LUdecomp:Tridiag


Suppose $A$ is a band matrix of width $d$.  Then the matrices $L$ and $U$ of an $LU$ decomposition of $A$ (insofar this exists) are band matrices of width $d$ as well 

::::::


Now suppose we need to solve many linear systems  $A\vect{x} =\vect{b}_i$ where $A$ is an $n\times n$ tridiagonal matrix. We can compute $A^{-1}$ and solve the systems by computing the consecutive products $A^{-1}\vect{b}_i$, or we can find an $LU$ decomposition and use {prf:ref}`Alg:LUdecomp:Usefulness` to solve  $A\vect{x} =\vect{b}_i$.

There are two reasons why it is advantageous to work with the $LU$ decomposition here.

<ol>

<li>

To store $A^{-1}$ we need to store  $n^2$ numbers whereas to store $L$ and  $U$ only $4n-2$ memory places are asked for.  In fact, if we may assume that $L$ has ones on its diagonal, only $3n-2$ places are needed.  For large $n$ this is a significant gain.

</li>

<li>

One product  $A^{-1}\vect{b}$ involves $n^2$  products of numbers and $n(n-1)$ additions, so the total  number of arithmetic operations equals  $2n^2 - n$.

To solve 

$$
   L\vect{y} = \begin{bmatrix}
                 1  \\
                 \ell_{21} & 1 \\
                 0 &\ell_{32} & 1 \\                
                 0 & 0 & \ell_{32} & 1 \\[1ex]
                 \vdots & \vdots &  & \ddots &  \\[1ex]
                 0 & 0 & 0 & \cdots & \ell_{n,n-1} & 1
             \end{bmatrix}
             \begin{bmatrix}
                y_1 \\ y_2 \\ y_3 \\ y_4 \\[1ex] 
                \vdots \\[1ex]
                y_n
             \end{bmatrix}
             = \begin{bmatrix}
                b_1 \\ b_2 \\ b_3 \\ b_4 \\[1ex] 
                \vdots \\[1ex]
               b_n
             \end{bmatrix}
$$

by forward substitution we  find one after another


$$
  \begin{array}{lcl}
      y_1 &=& b_1 \\
      y_2 &=& b_2 - \ell_{21}y_1 \\
      y_3 &=& b_3 - \ell_{32}y_2 \\[1ex]
       \vdots & & \quad \vdots \\[1ex]  
      y_n &=& b_n - \ell_{n,n-1}y_{n-1} \\ 
  \end{array}
$$

For all but the first row we need two operations per row, so in total $2(n-1)$ operations.

Likewise, for solving $U\vect{x} = \vect{y}$ we need an extra division for each row, so the number of operations for backward substitution is $2(n-1)+n$, and the total number for the two phases becomes

$$
   2(n-1) + 2(n-1) + n = 5n-4.
$$

For large $n$ this is again much smaller than the $2n^2-n$ arithmetic operations in the computation of $A^{-1}\mathbf{b}$.

</li>

</ol>


The following exercise may supply further evidence.

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9cbcf004-bfbe-428f-927f-5c64ca802946?id=82919
:label: grasple_exercise_3_6_7
:dropdown:
:description: To decide solving $A\vect{x} = \vect{b}$ via (given) $A=LU$ or (given) $A^{-1}$.

::::::


