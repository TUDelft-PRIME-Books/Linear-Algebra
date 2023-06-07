:::{review}
:::

(Sec:MatFactor)=
# Matrix Factorisation

When solving linear systems, it is very convenient to find an echelon form, so you can solve it using backward substitution as shown in {prf:ref}`Ex:LinSystems:I`. 

Consider the system $A\mathbf{x} = \mathbf{b}$ where 

$$A = 
\begin{bmatrix}
1 & 1 & 1 \\
0 & 2 & 6 \\
-1 & -1 & 3
\end{bmatrix},
\qquad
\mathbf{b} = 
\begin{bmatrix} 
3 \\ 2 \\1
\end{bmatrix}.
$$

In this section we will learn how to solve an $m\times n$ linear system $A\mathbf{x}=\mathbf{b}$ by decomposing (or factorising) a matrix into a product of two matrices. In the previous example we can express $A$ as 

$$
A = 
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
-1 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 1 & 1 \\
0 & 2 & 6 \\
0 & 0 & 4
\end{bmatrix}.
$$

When the factorisation is given, solving the system is quicker since we can solve it using backward and forward substitution. There is no need to look for an echelon form and then apply backward substitution. 

Considering the matrix above and the system 

$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
-1 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 1 & 1 \\
0 & 2 & 6 \\
0 & 0 & 4
\end{bmatrix}
\begin{bmatrix}
x_1\\ x_2 \\ x_3 
\end{bmatrix} = 
\begin{bmatrix} 
3 \\ 2 \\1
\end{bmatrix},
$$

by setting $\mathbf{y} = \begin{bmatrix} 1 & 1 & 1 \\ 0 & 2 & 6 \\ 0 & 0 & 4 \end{bmatrix} \begin{bmatrix} x_1\\ x_2 \\ x_3 \end{bmatrix}$ we have 

$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
-1 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
y_1\\y_2\\y_3
\end{bmatrix} =
\begin{bmatrix} 
3 \\ 2 \\1
\end{bmatrix}.
$$

With forward substitution we can find the solution:

$$
\begin{bmatrix}
y_1\\y_2\\y_3
\end{bmatrix} =
\begin{bmatrix}
3 \\ 2 \\ 4
\end{bmatrix},
$$

Then, solving

$$
\begin{bmatrix}
1 & 1 & 1 \\
0 & 2 & 6 \\
0 & 0 & 4
\end{bmatrix}
\begin{bmatrix}
x_1\\ x_2 \\ x_3 
\end{bmatrix} = 
\begin{bmatrix}
3 \\ 2 \\ 4
\end{bmatrix},
$$

we obtain 

$$
\begin{bmatrix}
x_1 \\ x_2 \\ x_3
\end{bmatrix}
\begin{bmatrix}
4 \\ -2 \\ 1
\end{bmatrix},
$$

which is the solution to our original system. Since the factorisation was given, we did not have to solve the system from scratch by trying to find an echelon form.

There are several methods for factorising matrices. The factorisations that we will see in this section use **direct methods**. Direct methods are methods that produce the exact solution in a finite number of steps.

There are special cases where solving linear systems can be done quickly. These cases involve triangular or trapezoidal matrices (we will discuss these matrices in the next section). In general, when the matrix associated with an $m\times n$ linear system is a trapezoidal matrix we can use backward or forward substitution for solving them. Remember the echelon forms from {numref}`Subsec:LinSystems:RowReduction`? Echelon forms are trapezoidal matrices.

The most common factorisation methods make use of this kind of matrices. This is why we will first introduce the idea of a trapezoidal and triangular matrix and then discuss the corresponding factorisation methods and their applications.


## Trapezoidal and Triangular matrices

At this point one probably figured out that when we find an echelon form for an $m\times n$ matrix, that echelon form is actually a trapezoidal matrix. However, to talk about trapezoidal matrices, first we need to revisit the concept of "main diagonal" of a matrix introduced in {prf:ref}`Def:MatrixOps:MainDiagonal`. We will extend this concept to non-square matrices.

:::{prf:definition} Main diagonal of a matrix

For an $m\times n$ matrix $A$, we call the elements $a_{ii}$ the **diagonal elements** of $A$. The (ordered) set of the diagonal elements is called the **main diagonal** of $A$.

:::

Now we are ready to define the objects that we will use during this section.

::::::{prf:definition} Trapezoidal and Triangular Matrices
<ul>
<li>

We say that an $m\times n$ matrix $U$ is an **upper trapezoidal matrix** if all the entries below the main diagonal are zero. In other words, an upper trapezoidal matrix that has the form 


$$
U=
\begin{bmatrix}
\blacksquare & \ast          & \cdots & \cdots & \ast & \cdots & \cdots & \ast \\
0            & \blacksquare  & \ddots & &\vdots & & &\vdots \\
\vdots       & \ddots        & \ddots & \ddots & \vdots & & & \vdots\\
0       & \cdots  & 0 &  \blacksquare & \ast & \cdots & \cdots & \ast
\end{bmatrix} \quad \text{for }\,\, m<n,
$$

$$
U=
\begin{bmatrix}
\blacksquare & \ast          & \cdots & \ast \\
0            & \blacksquare  & \ddots &\vdots \\
\vdots       & \ddots        & \ddots & \ast\\
0       & \cdots  & 0 &  \blacksquare \\
0  & \cdots & \cdots & 0 \\
\vdots & & & \vdots \\
\vdots & & & \vdots \\
0  & \cdots & \cdots & 0 \\
\end{bmatrix}  \quad \text{for }\,\, m>n,
$$

where the $\blacksquare$ represent any real number in the main diagonal, and the $\ast$ represent any real number above the main diagonal. If the matrix is a square matrix, then it is an **upper triangular** matrix.


</li>
<li>

We say that an $m\times n$ matrix $L$ is a **lower trapezoidal matrix** if all the entries above the main diagonal are zero. I.e., a lower trapezoidal matrix that has the form


$$
L=
\begin{bmatrix}
\blacksquare & 0          & \cdots & \cdots & 0 & \cdots & \cdots &0\\
\ast         & \blacksquare  & \ddots & &\vdots & & & \vdots\\
\vdots       & \ddots        & \ddots & \ddots & \vdots & & & \vdots \\
\ast       &  \cdots       & \ast & \blacksquare & 0 & \cdots & \cdots & 0
\end{bmatrix}  \quad \text{for }\,\, m<n,
$$

$$
L=
\begin{bmatrix}
\blacksquare &  0 & \cdots & 0 \\
\ast            & \blacksquare  & \ddots &\vdots \\
\vdots       & \ddots        & \ddots & 0\\
\ast       & \cdots  & \ast &  \blacksquare \\
\ast  & \cdots & \cdots & \ast \\
\vdots & & & \vdots \\
\vdots & & & \vdots \\
\ast  & \cdots & \cdots & \ast \\
\end{bmatrix}  \quad \text{for }\,\, m>n,
$$

where the $\blacksquare$ represent any real number in the main diagonal, and the $\ast$ represent any real number below the main diagonal. If the matrix is a square matrix, then it is a **lower triangular** matrix.

</li>
</ul>

::::::


Observe that, when all $\ast$ are zero and the matrix is square, then the matrix is a diagonal matrix.


::::::{prf:example}

Below there are examples of trapezoidal matrices.

:::{latexlist}

\item The matrix 

$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & -9 & 0 \\
0 & 0 & 11
\end{bmatrix}
$$


is a $3\times 3$ both upper and lower triangular matrix and, therefore, it is a diagonal matrix.

\item The matrix 

$$
\begin{bmatrix}
2 &  0  &  0  & 0 \\
4 &  6  &  0  & 0 \\
8 &  10  &  12  & 0 \\
14 & 16 & 18 & 20
\end{bmatrix}
$$

is a $4\times 4$ lower triangular matrix.

\item  The matrix 

$$
\begin{bmatrix}
1 & 0  & 0 & 3  \\
0 & -3 & 0 & 0  \\
0 & 0  & 2 & 0  \\
0 & 0  & 0 & -4  \\
0 & 0 & 0 & 0 
\end{bmatrix}
$$

is a $5\times 4$ upper trapezoidal matrix.

:::

::::::



Trapezoidal matrices have nice properties with respect to their sum and their product.



::::::{prf:proposition} Properties of trapezoidal matrices
:label: prop:PropertiesTriangularMatrices


Let $A$ and $B$ be two upper trapezoidal matrices. Then the following properties hold:


:::{latexlist}
:enumerated: true
:type: i

\item $A+B$ is an upper  trapezoidal matrix (whenever the sum makes sense).
\label{Item:prop:PropertiesTriangularMatrices_sum}

\item $AB$ is an upper trapezoidal matrix (whenever the product makes sense).
\label{Item:prop:PropertiesTriangularMatrices_product}

:::

::::::

::::{prf:proposition}
:label: Prop:LUDecomp:PropertiesTriangularMatricesInverse

If $A$ is an invertible upper triangular matrix, then $A^{-1}$ is upper triangular matrix.

::::


The proof of {prf:ref}`Prop:LUDecomp:PropertiesTriangularMatricesInverse` is technical and it involves computations . 

So the reader may skip this proof and convince themselves that the properties hold true by looking at the following example.



::::::{prf:example}
Consider the matrices 

$$
A=
\begin{bmatrix}
1 & 2 & 3 \\
0 & 4 & 5 \\
0 & 0 & 6
\end{bmatrix}
, \qquad
B = 
\begin{bmatrix}
1 & 3 & 5 \\
0 & 7 & 9 \\
0 & 0 & -11
\end{bmatrix}
.
$$

We can easily see that the first two properties of the proposition hold.

$$
A+B = 
\begin{bmatrix}
2 & 5 & 8 \\
0 & 11 & 14 \\
0 & 0 & -5
\end{bmatrix}
,
$$

$$
AB = 
\begin{bmatrix}
1 & 17 & -10 \\
0 & 28 & -19 \\
0 & 0 & -66
\end{bmatrix}
.
$$

For the third one, we have that 

$$
A^{-1} = 
\begin{bmatrix}
1 & -{1}/{2} & -{1}/{12} \\
0 & {1}/{4} & -{5}/{24} \\
0 & 0 & {1}/{6}
\end{bmatrix}
,
$$


which is upper triangular. It is left to the reader to check that $AA^{-1}=I$.

::::::


::::::{prf:proof} (of {prf:ref}`prop:PropertiesTriangularMatrices`)

The proof of {itemref}`Item:prop:PropertiesTriangularMatrices_sum` follows from the fact that matrices are added component-wise. Therefore, the entries below the main diagonal of $A+B$ will be zero since both $A$ and $B$ have zero entries below the main diagonal.
 
To prove {itemref}`Item:prop:PropertiesTriangularMatrices_product` we fix $j < n$ and compute $AB_{(j+k)j}$ for $k=1,2,\dots, m-j$. In other words, we compute the entries below the main diagonal in column $j$:

$$
AB_{(j+k)j} = \sum_{l=1}^{n} a_{(j+k)l}b_{lj}.
$$

If we define $A = \begin{bmatrix}\mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n \end{bmatrix}$ an $m\times n$ upper trapezoidal matrix, and $B=\begin{bmatrix}\mathbf{b}_1 & \mathbf{b}_2 & \cdots & \mathbf{b}_p \end{bmatrix}$ and $n\times p$ upper trapezoidal matrix, then we can understand the previous sum as the the result of the dot product of the vectors corresponding to $\mathbf{a}_{j+k}^T$ and $\mathbf{b}_j$.

We observe that for $l\le j$ the components $a_{(j+k)l}$ are zero, and for $l>j$ the components $b_{lj}0$ are zero. Therefore,

\begin{align*}
AB_{(j+k)j} &= \sum_{l=1}^{n} a_{(j+k)l}b_{lj} \\
&= \sum_{l=1}^{j} 0 b_{lj} + \sum_{l=j+1}^n a_{(j+k)j} 0 \\
&= 0.        
\end{align*}
 
The proof for {prf:ref}`Item:prop:PropertiesTriangularMatricesInverse` is proposed as an exercise. See 
<a href="#Item:prove_statment_c_properties_triangular_matrices">Exercise 1</a>.


::::::



## LU Decomposition

As mentioned at the begining of this section, one of the ways to solve a linear system is to factorise the matrix of coefficients by "splitting" it into a product of two trapezoidal matrices. For the following factorisation, we will name these matrices $L$ and $U$, and they will have the property that $L$ is lower triangular and $U$ is upper trapezoidal.  As you probably have guessed, we call this factorisation an $LU$ decomposition.

::::::{prf:definition}
Let $A$ be an $m\times n$ matrix. We call a $LU$
decomposition of $A$ all decompositions of the type

$$
A=LU
$$

with $L$ being an $m\times m$ lower triangular matrix and $U$ an $m\times n$ upper trapezoidal matrix, both with real coefficients with the form

$$
L=
\begin{bmatrix}
1\\
l_{21} & 1 \\
l_{31} & l_{32} & \ddots  \\
\vdots & \vdots & \ddots & \ddots\\
l_{m1} & l_{m2} &  \cdots & l_{m(m-1)} & 1
\end{bmatrix}
,
\quad
U=
\begin{bmatrix}
u_{11} & u_{12} & u_{13} & \cdots &u_{1n} \\
&
u_{22}
&
u_{23} & \cdots & u_{2n} \\
& & u_{33} & \cdots & u_{3n} \\
& &  &
\ddots
&
\vdots \\
& & & & u_{mn}
\end{bmatrix}, \quad m<n
,
$$

or,

$$
U = \begin{bmatrix}
u_{11} & \cdots & \cdots & u_{1n}\\
        & \ddots &  & \vdots \\
        &       &   \ddots & \vdots \\
        &       &           & u_{nn} \\
        & \\
        & \\
        &
\end{bmatrix},\quad m>n.
$$

To not clutter and to emphasise the triangular/trapezoidal matrices, we use empty spaces instead of zeros.


::::::



Suppose that $A=LU$ so that a linear system of equations $A\mathbf{x}=\mathbf{b}$ can be written as $LU\mathbf{x}=\mathbf{b}$. Then, by setting $\mathbf{y} = U\mathbf{x}$, we can solve the linear system in two steps:

:::{latexlist}
:enumerated: true
:type: i

\item Solve the system $L\mathbf{y}=\mathbf{b}$ and find $\mathbf{y}$.
\item Solve the system $U\mathbf{x}=\mathbf{y}$ to find $\mathbf{x}$.

:::


At this point the reader may think that such a decomposition involves a lot of work.  However, it takes (roughly) the same number of operations as for finding an echelon form (see {numref}`Subsec:LinSystems:RowReduction`). In addition, this method has the advantage that once the decomposition of a matrix $A$ has been found, then it is faster to solve multiple systems involving the matrix $A$. And why is that? Well, if one thinks about it, once we have an $LU$ decomposition of $A$ then we just need to solve linear systems that involve trapezoidal/triangular matrices, which are "faster" to solve than solving $A\mathbf{x}=\mathbf{b}$. We will formalise this concept below.

The $LU$ decomposition is a particular case of the more general algorithm that we find in {numref}`Sec:PLUDecomp`

The idea behind an $LU$ decomposition is to find an echelon form of the matrix of coefficients without exchanging rows, while keeping track of those changes. Let's see how to find an $LU$ decomposition with a complete example using an square matrix of coefficients. Along the rest of this subsection, we will assume that we perform **no row scaling when preforming row operations**.

::::::{prf:example} 
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

To find an $LU$ decomposition we will find an echelon form performing row operations without exchanging rows. In addition, we will keep track of the changes we perform.
For the first step,

$$

\left[\begin{array}{rrr}3 & 1 & -2\\2 & 4 & 1\\1 & 2 & 1\end{array} \right]  \begin{array}{l}
[R_1] \\
{[R_2-2/3R_1]} \\
{[R_3-1/3R_1]} \\
\end{array}\sim
\begin{bmatrix}
3 & 1 & -2 \\
0 & {10}/{3} & {7}/{3} \\
0 & {5}/{3} & {5}/{3}
\end{bmatrix}
$$

The numbers $2/3$ and $1/3$ are called multipliers.
Observe that the row operations can be understood as a product of matrices. Let's call

$$
F^{(1)} = 
\begin{bmatrix}
1 & 0 & 0 \\
-2/3 & 1 & 0 \\
-1/3 & 0 & 1 
\end{bmatrix}
$$


Then,


$$
F^{(1)} A =       
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

Now,

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
\end{bmatrix}
.
$$

Since an echelon form of an $n\times n$ matrix is an upper triangular matrix, we define

$$
U=    
\begin{bmatrix}
3 & 1 & -2 \\
0 & {10}/{3} & {7}/{3} \\
0 & 0 & {1}/{2}
\end{bmatrix}
.
$$

To find $L$, we observe that the last row operation that we performed can be written as a product of matrices:

\begin{align*}
U &= F^{(2)}F^{(1)}A = 
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & -1/2 & 1
\end{bmatrix}
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
 \\
&= 
\begin{bmatrix}
1 & 0 & 0 \\
-\frac{2}{3} & 1 & 0 \\
0 & -\frac{1}{2} & 1
\end{bmatrix}
A\\
&= FA.
\end{align*}

Since $F=F^{(2)}F^{(1)}$ is non-singular and lower triangular, we can compute its inverse,


$$
F^{-1} = 
\begin{bmatrix}
1 & 0 & 0 \\
{2}/{3} & 1 & 0 \\
{1}/{3} & {1}/{2} & 1        
\end{bmatrix}
,
$$

which is also lower triangular (we knew it from {prf:ref}`prop:PropertiesTriangularMatrices`). By writing $F^{-1}U=A$, we can take $L=F^{-1}$.


::::::


::::::{prf:remark}
Pay attention!

In practice, we do not need to compute the product of the matrices $F^{(k)}$, and we do not need to find any inverse. By looking at the previous example, one can see that the matrix $L$ has ones in its diagonal and the entries below the main diagonal have, in each column, the corresponding multipliers. This is true in the general case (as long as one does not need to exchange rows). We will see all the details for the general case in {prf:ref}`thm:existence_and_uniqueness_LU` below.


::::::

The following example shows how we implement the $LU$ decomposition in practice. Remember that no row exchanges are needed.


::::::{prf:example}
Find an $LU$ decomposition of the matrix

$$
A= 
\begin{bmatrix}
5 & 5 & 5 \\
3 & 4 & 1 \\
2 & 1 & 3
\end{bmatrix} .
$$

We will proceed using row operations without exchanging any rows. At the same time, we will construct the matrix $L$ using the multipliers. Our matrix $L$ will have the form 
 

$$
L=
\begin{bmatrix}
1 & 0 & 0 \\
\ast & 1 & 0 \\
\ast & \ast & 1
\end{bmatrix} .
$$


The changes we make are the following:

\begin{align*}
\left[\begin{array}{rrr}5 & 5 & 5\\3 & 4 & 1\\2 & 1 & 3\end{array} \right]  \begin{array}{l}
[R_1] \\
{[R_2-\mathbf{3/5}R_1]} \\
{[R_3-\mathbf{2/5}R_1]} \\
\end{array} &\sim 
\begin{bmatrix}
5 & 5 & 5 \\
0 & 1 & -2 \\
0 & -1 & 1
\end{bmatrix}
\\
&\longrightarrow
L = 
\begin{bmatrix}
1 & 0 & 0 \\
\mathbf{3/5} & 1 & 0 \\
\mathbf{2/5} & \ast & 1
\end{bmatrix} , \\
\left[\begin{array}{rrr}5 & 5 & 5\\0 & 1 & -2\\0 & -1 & 1\end{array} \right]  \begin{array}{l}
[R_1] \\
{[R_2]} \\
{[R_3-(\mathbf{-1})R_2]} \\
\end{array} 
&\sim 
\begin{bmatrix}
5 & 5 & 5 \\
0 & 1 & -2 \\
0 & 0 & -1
\end{bmatrix}\\
&\longrightarrow 
L = 
\begin{bmatrix}
1 & 0 & 0 \\
3/5 & 1 & 0 \\
2/5 & \mathbf{-1} & 1
\end{bmatrix} .
\end{align*}

Therefore, an $LU$ decomposition of $A$ is 

$$
L=
\begin{bmatrix}
1 & 0 & 0 \\
{3}/{5} & 1 & 0 \\
{2}/{5} & -1 & 1
\end{bmatrix}
,\qquad
U=
\begin{bmatrix}
5 & 5 & 5 \\
0 & 1 & -2 \\
0 & 0 & -1
\end{bmatrix}
.
$$


::::::


At this point, there are important questions that we still need to address: when does a matrix have an $LU$ decomposition? Can a matrix have more than one $LU$ decomposition? It would be convenient if there is an $LU$ decomposition, that such decomposition is unique.  

The case when there is a unique $LU$ decomposition is very special, as the following result indicates.


::::::{prf:theorem}
:label: thm:existence_and_uniqueness_LU


Suppose that $A$ is an
 $m\times n$ matrix with real entries. Then
<ol type = "i">
<li id="Item:thm:existence_and_uniqueness_LU:existence">

If we can find an echelon form for the matrix $A$ without exchanging rows, then there exists an $LU$ decomposition of $A$, and it has the form
 

$$
L=
\begin{bmatrix}
1 \\
m_{21} &  1 \\
\vdots &  m_{32} &\ddots  \\
\vdots &  \vdots &\ddots & \ddots  & \\
m_{m1} & m_{m2} & \cdots & m_{m(m-1)}    &  1 
\end{bmatrix}
, \quad 
U=
\begin{bmatrix}
a^{(0)}_{11} & a^{(0)}_{12} & \cdots & a^{(0)}_{1n}\\
& a^{(1)}_{22} & \cdots & a^{(1)}_{2n}  \\
&             & \ddots  & \vdots \\
&             &              &a^{(n-1)}_{nn} \\
\\\\
\end{bmatrix}\quad (m>n),
$$

or

$$
\begin{bmatrix}
a^{(0)}_{11} & a^{(0)}_{12} & \cdots & a^{(0)}_{1m} &\cdots &a_{1n}^{(0)}\\
& a^{(1)}_{22} & \cdots & a^{(1)}_{2m} & \cdots & a_{2n}^{(1)}\\
&             & \ddots  & \vdots & & \vdots\\
&             &              &a^{(m-1)}_{mm} & \cdots & a_{mn}^{(m-1)}\\
\end{bmatrix}\quad (m<n),
$$

where the values $m_{ij}$ are the corresponding multiplers and the superscripts in $a_{ij}^{(k)}$ indicate that the value has been obtained after performing $k$ row operations.

</li>
<li id="Item:thm:existence_and_uniqueness_LU:uniqueness">

If $A$ is an $n\times n$ non-singular matrix, then the $LU$ decomposition is unique.

</li>
</ol>



::::::


::::::{prf:proof} Proof of {prf:ref}`thm:existence_and_uniqueness_LU`

We start with the proof of <a href="#Item:thm:existence_and_uniqueness_LU:uniqueness">ii. </a>. We will
proceed by contradiction. Suppose that we have two $LU$ decompositions of $A$. That is, $A= L_1U_1$ and $A=L_2U_2$. Then

$$
L_1U_1=L_2U_2.
$$


Since $A$ is non-singular, $L_{i}$ and $U_{i}$ are non-singular for $i=1,2$. Multiplying both sides of the previous identity by $L^{-1}_{2}$ to the left, and by $U^{-1}_{1}$ to the right we obtain:


:::{math}
:label: eq:lowerequalupper


L_{2}^{-1}L_{1}=U_{2}U^{-1}_{1}.

:::


Now we can visualise equation {eq}`eq:lowerequalupper` like this


$$
\begin{bmatrix}
1 \\
\ast &  1 \\
\vdots & \ast & \ddots \\
\vdots & \vdots &  \ddots   &\ddots \\
\ast & \ast & \cdots & \ast& 1 
\end{bmatrix}
 = 
\begin{bmatrix}
\blacksquare & \ast & \cdots & \cdots & \ast \\
& \blacksquare & \ast  & \cdots  & \ast \\
&       &   \ddots & \ddots & \vdots  \\
&       &          & \ddots & \ast \\
&       &          &        & \blacksquare
\end{bmatrix}
.
$$


For this identity to hold true, we need all $\blacksquare$ to be one and all $\ast$ to be zero. In other words,


$$
L^{-1}_{2}L_1 = U_{2}U^{-1}_{1} = I,
$$


which leads us to $L^{-1}_2=L^{-1}_1$ so $L_2=L_1$, and 
$U^{-1}_2=U^{-1}_1$ so $U_2=U_1$. This is a contradiction with the statement that $A$ had two different $LU$ decompositions.

To prove <a href="#Item:thm:existence_and_uniqueness_LU:existence">i. </a>, suppose that we can find an echelon form of $A$ without exchanging rows. For simplicity on the notation, we will prove the case of a squared matrix but the reader can easily adapt the proof for the non-suqared case. 

We can write the $k$-th step as a product of matrices:

\begin{align*}
&
\begin{bmatrix}
1                                   \\
& \ddots                            \\
&        &      1                    \\
&        & -m_{(k+1)k} & 1            \\
&        & \vdots      &     & \ddots  \\
&        & -m_{nk}     &     &        & 1
\end{bmatrix}
\begin{bmatrix}
a^{(0)}_{11} & \cdots & a^{(0)}_{1k} & a^{(0)}_{1(k+1)} & \cdots & a^{(0)}_{1n} \\
& \ddots & \vdots & \vdots & & \vdots \\
&    & a^{(k-1)}_{kk} & a^{(k-1)}_{k(k+1)} & \cdots & a^{(k-1)}_{kn} \\
&    & a^{(k-1)}_{(k+1)k} & a^{(k-1)}_{(k+1)(k+1)} & \cdots & a^{(k-1)}_{(k+1)n} \\
&    & \vdots & \vdots &  & \vdots \\
&    & a^{(k-1)}_{nk} & a^{(k-1)}_{n(k+1)} & \cdots & a^{(k-1)}_{nn} 
\end{bmatrix}
\\
=&
\begin{bmatrix}
a^{(0)}_{11} & \cdots & a^{(0)}_{1k} & a^{(0)}_{1(k+1)} & \cdots & a^{(0)}_{1n} \\
& \ddots & \vdots & \vdots & & \vdots \\
&    & a^{(k-1)}_{kk} & a^{(k-1)}_{k(k+1)} & \cdots & a^{(k-1)}_{kn} \\
&    & 0 & a^{(k)}_{(k+1)(k+1)} & \cdots & a^{(k)}_{(k+1)n} \\
&    & \vdots & \vdots &  & \vdots \\
&    & 0 & a^{(k)}_{n(k+1)} & \cdots & a^{(k)}_{nn} 
\end{bmatrix}
.
\end{align*}



We denote the previous product by $A^{(k)}=F^{(k)}A^{(k-1)}$. Since finding an echelon form is an iterative process, we can find $A^{(n)}$ by multiplying $A^{(0)}$ by the corresponding $F^{(k)}$ matrices to the left:


$$
A^{(n)} = F^{(n-1)}F^{(n-2)}\cdots F^{(3)}F^{(2)}F^{(1)}A^{(0)}  
$$


Since $A^{(n)}$ is an upper triangular matrix, we can take it as $U$. Since all matrices $F^{(k)}$ are invertible, we can recover $A^{(0)}$ multiplying $U$ to the left by the corresponding inverse matrices:


$$
A=A^{(0)}={F^{(1)}}^{-1}{F^{(2)}}^{-1}\cdots{F^{(n-2)}}^{-1}{F^{(n-1)}}^{-1}A^{(n)}
$$


So we can define $L={F^{(1)}}^{-1}{F^{(2)}}^{-1}\cdots{F^{(n-2)}}^{-1}{F^{(n-1)}}^{-1}$.
We just need to see that $L$ is, indeed, lower triangular with ones on the diagonal, and that it has the multipliers $m_{ij}$ in the entries below it. To see that, we write $F^{(k)} = I - M_k E_k$ where 

$$
M_k = 
\begin{bmatrix}
0\\ \vdots\\ 0\\m_{(k+1)k}\\m_{(k+2),k}\\ \vdots \\ m_{nk}
\end{bmatrix}
,\qquad E_k = 
\begin{bmatrix}
0 & \cdots & 0 & \stackrel{\text{$k$-th}}{1} & 0 & \cdots & 0
\end{bmatrix}
.
$$

Observe that the matrix $I-M_kE_k$ is the matrix

$$
\begin{bmatrix}
1 &  &  &  &  &  \\
 & \ddots &  &  &  &  \\
 &  & 1 & & & \\
 &  & -m_{(k+1)k} &  \\
 &  & -m_{(k+2)k} & \ddots &  \\
 &  & \vdots &  &  & \ddots \\
 &  & -m_{nk} & & & & 1
\end{bmatrix},
$$

and that $E_iM_j = 0$ for $i \le j$.

Now, we take the following product:

\begin{align*}
(I-M_kE_k)(I+M_kE_k) &= I - M_kE_k + M_kE_k -M_kE_kM_kE_k \\
&= I - M_kE_k M_kE_k \\
&= I - M_k(E_k M_k)E_k \\
&= I - M_k 0 E_k \\
&= I,
\end{align*}


where the zero in the second from the last identity is the zero matrix, we deduce that ${F^{(k)}}^{-1} = I + M_k E_k$. 
Then,


\begin{align*}
L &= {F^{(1)}}^{-1}{F^{(2)}}^{-1}\cdots{F^{(n-1)}}^{-1}{F^{(n-1)}}^{-1}\\
&= \prod_{k=1}^{n-1} (I+M_kE_k) \\ 
&= I + \sum_{k=1}^{n-1} M_kE_k,
\end{align*}


where we have used that fact that, for $i < j$ $E_iM_j=0$.
Thus,


\begin{align*}
L &= I + M_1E_1 + \cdots M_{n-1}E_{n-1} \\
&= 
\begin{bmatrix}
1 \\
m_{21} &  1 \\
\vdots &  m_{32} &\ddots  \\
\vdots &  \vdots &\ddots & \ddots  & \\
m_{n1} & m_{n2} & \cdots & m_{n(n-1)}    &  1 
\end{bmatrix}
.
\end{align*}


::::::

(Sec:PLUDecomp)=
## PLU Decomposition

The LU decomposition is quite limiting in the sense that it requires to be able to find an echelon form of the matrix of coefficients without exchanging any rows in the process. Clearly, it is not always possible to find an echelon form of a matrix without exchanging rows. Let's see what happens when we encounter this situation.

::::{prf:example}

We can try to find an $LU$ decomposition of the matrix

$$
A = \begin{bmatrix}
0 & 1 & 2 \\
3 & 4 & 5 \\
6 & 7 & 8
\end{bmatrix}.
$$

In this case, we can not find an echelon form for this matrix without exchanging rows. Let's perform the following row operations:

\begin{align*}
&\begin{bmatrix}
0 & 1 & 2 \\
3 & 4 & 5 \\
6 & 7 & 8
\end{bmatrix}
\begin{array}{l}
[R_1] \\
{[R_2]}\\ 
{[R_3-2 R_2]} 
\end{array} &\sim & 
\begin{bmatrix}
0 & 1 & 2 \\
3 & 4 & 5 \\
0 & -1 & -2
\end{bmatrix}
\begin{array}{l}
[R_1 \leftrightarrow R_2] \\
{[R_2 \leftrightarrow R_1]} \\
{[R_3]} \\
\end{array} \\
&\begin{bmatrix}
3 & 4 & 5 \\
0 & 1 & 2 \\
0 & -1 & -2
\end{bmatrix}
\begin{array}{l}
[R_1]\\
{[R_2]} \\
{[R_3 + R_2]}
\end{array} &\sim &
\begin{bmatrix}
3 & 4 & 5 \\
0 & 1 & 2 \\
0 & 0 & 0
\end{bmatrix}
\end{align*}

Observe that we obtained an upper triangular matrix $U$ (echelon form). However, if we consider the changes we performed to the matrix $A$, we will see that

$$
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0 \\
0 & 1 & 1
\end{bmatrix}
\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & -2 & 1
\end{bmatrix}
=
\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
1 & -2 & 1
\end{bmatrix}
$$

is not a lower triangular matrix.

:::::

To find a lower triangular matrix we observe the following fact: subtracting $2$ times the second row to the third and then exchanging the first and second rows is equivalent to first exchanging the first and second rows and then subtracting $2$ times the first row to the third.

::::{prf:example}

$$
\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & -2 & 1
\end{bmatrix}=
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
-2 & 0 & 1
\end{bmatrix} 
\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}.
$$

::::

So we found an alternative order of row operations that brought us to the same echelon form. The key idea is to **perform all the row exchanges first** and **then add multiples of one row to another** to obtain an echelon form. Let's see the results:

:::{math}
:label: eq:LUDecomp:almostPLU

\begin{array}{rcl}
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0 \\
0 & 1 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
-2 & 0 & 1
\end{bmatrix} 
\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}A &= \begin{bmatrix}
3 & 4 & 5 \\
0 & 1 & 2 \\
0 & 0 & 0
\end{bmatrix} \\\\
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
-2 & 1 & 1
\end{bmatrix}
\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}A &= 
\begin{bmatrix}
3 & 4 & 5 \\
0 & 1 & 2 \\
0 & 0 & 0
\end{bmatrix}
\end{array}

:::


Now we see that on the left-hand side of {eq}`eq:LUDecomp:almostPLU` we obtain a lower triangular matrix, for which we can find an inverse to obtain:

$$
\begin{bmatrix}
0 & 1 & 0 \\
1 & 0 & 0 \\
0 & 0 & 1
\end{bmatrix}A = 
\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
2 & -1 & 1
\end{bmatrix}
\begin{bmatrix}
3 & 4 & 5 \\
0 & 1 & 2 \\
0 & 0 & 0
\end{bmatrix}
$$

This is not an $LU$ decomposition, but almost! This is what we call a **PLU** decomposition. The following result summarizes it:

:::::{prf:theorem} Existence of a PLU Decomposition
:label: LUDecomp:existencePLU

Suppose that $A$ is an $m\times n$ matrix with real coefficients. Then there exist matrices $P$, $L$ and $U$ such that 

$$ PA = LU, $$

where $P$ is an $m\times m$ matrix that exchanges the rows of $A$, $L$ is an $m\times m$ lower triangular matrix obtained inverting the product matrices that perform row operations to that only add multiples of a row to other rows in the matrix $PA$, and the matrix $U$ is an $m\times n$ upper-trapezoidal matrix (echelon form) that is obtained after performing the corresponding row operations to $PA$.

:::::

## Application of the (P)LU decomposition

One way to measure the performance of an algorithm is counting the number of arithmetic operations [^flopnote] that are necessary for solving a problem. By arithmetic operations we will take into account sums, products, multiplications and divisions. Suppose that we want to solve the linear system $A\mathbf{x}=\mathbf{b}$ by taking the augmented matrix $[ A | \mathbf{b}]$, finding an echelon form with the same solution set, and then using backward substitution.

In the worst-case scenario, for a $3\times 3$ matrix $A$, ($3\times 4$ augmented matrix), we need the following number of arithmetic operations:
<ul>
<li>

To convert the components $a_{21}$ and $a_{31}$ to a zero value, we need to compute two $m_{ij}$(two divisions), then we need to multiply each component of the first row, starting at $a_{12}$, by each $m_{ij}$(this happens twice, so $2\times 3=6$ products) and then we need to subtract the resulting values to the corresponding components in each row ($2\times 3=6$ subtractions). Therefore, we need a total of $14$ arithmetic operations(8 products/divisions and 6 additions/subtractions).


</li>
<li>

To convert the component $a_{32}$ to a zero value, we need to compute one $m_{ij}$(one division), then we need to multiply each component of the second row starting at $a_{23}$(this is 2 products), and then we need to subtract the resulting values to the corresponding components in the third row (2 subtractions). This totals 5 arithmetic operations.

</li>
</ul>

So just to bring the augmented matrix to an echelon form requires 19 arithmetic operations (11 multiplications/divisions and 8 additions/subtractions).

Now, to solve the system we use backward substitution:
<ul>
<li>

 To find $x_3$ requires one division.


</li>
<li>

 To find $x_2$ requires (one multiplication, one subtraction, and one division).


</li>
<li>

 To find $x_1$ requires (two multiplications, two subtractions, and one division).


</li>
</ul>



This means that solving a linear system with a $3\times 3$ matrix of coefficients in echelon form requires 9 arithmetic operations.

So in total, we needed 28 arithmetic operations.

Supposing that $A=LU$ and that $L$ and $U$ are given, then, we solve first $L\mathbf{y}=\mathbf{b}$ and then $U\mathbf{x}=\mathbf{y}$.
<ul>
<li>

 For $L\mathbf{y}=\mathbf{b}$ we use forward substitution. Since the elements in the main diagonal are ones, then we have that we need no operations to determine $y_1$, we need one subtraction and one division for $y_2$, and two subtractions and one division for $y_3$. This totals 6 arithmetic operations.


</li>
<li>

 To solve $U\mathbf{x}=\mathbf{y}$ we use backward substitution, and we have just seen that it requires 9 arithmetic operations.


</li>
</ul>


So when the matrix $A$ is already $LU$ factorised, the number of operations required to solve the system is significantly lower.

Suppose now that $A$ is a non-singular $n\times n$ matrix.  Let's count the number of operations in a general case, and we can see how advantageous it is to factorise our matrix $A$.

<ul>
<li>

For solving the system directly, for each column $j$ we need to compute the $m_{ij}$($(n-1)$ divisions), then multiply $m_{ij}$ by all the components of row $i$ except for the first $i$, so that is $(n-i)(n-i+1)$ products, and then we need to perform the same number of subtractions. This totals $(n-i)(n-i+2)$ products/divisions and $(n-i)(n-i+2)$ additions/subtractions. Now we need to add these values for all the columns.

<ul>
<li>

For the products/divisions we have:

\begin{align*}
\sum_{i=1}^{n-1}(n-i)(n-i+2) &= \sum_{i+1}^{n-1} i^{2} - 2 i n + n^{2} - 2 i + 2 n \\
&=\sum_{i=1}^{n-1}(n^2-2ni+i^2)+\sum_{i=1}^{n-1}(2n-2i)\\
&=\sum_{i=1}^{n-1}(n-i)^2 + 2\sum_{i=1}^{n-1}(n-i) \\
&=\sum_{i=1}^{n-1}i^2 +2\sum_{i=1}^{n-1}i \\
&\frac{n(n-1)(2n-1)}{6}+2\frac{n(n-1)}{2} \\
&\frac{2n^3+3n^2-5n}{6}.
\end{align*}

</li>
<li>

For the additions/subtractions we have:

\begin{align*}
\sum_{i=1}^{n-1}(n-i)(n-i+1) &= \sum_{i=1}^{n-1} i^{2} - 2 i n + n^{2} - i + n \\
&=\sum_{i=1}^{n-1}(n^2-2in+i^2) + \sum_{i=1}^{n-1}(n-i) \\
&=\sum_{i=1}^{n-1}(n-i)^2 + \sum_{i=1}^{n-1}(n-i)\\
&=\sum_{i=1}^{n-1}i^2 + \sum_{i=1}^{n-1}i \\
&=\frac{n(n-1)(2n-1)}{6}+\frac{n(n-1)}{2}\\
&=\frac{n^3-n}{3}.
\end{align*}

</li>
</ul>

So in total we have to perform
 

$$
\frac{4n^3-3n^2-7n}{6}
$$

arithmetic operations to bring the matrix to echelon form.

If we just count the number of arithmetic operations to compute the $LU$ decomposition, then we need 
 

$$
\frac{4n^3-3n^2-n}{6}
$$

arithmetic operations.

Using similar reasoning, we can calculate the number of arithmetic operations needed to solve an upper triangular linear system, which gives us $n^2$. And solving a lower triangular system with ones in the main diagonal requires $n^2-n$ arithmetic operations.
 
:::{prf:remark}

The total number of arithmetic operations needed in order to solve a linear system with row reduction (without exchanging rows), and with $LU$ is the same. We leave the proof as an exercise for the reader.

:::

In many applications in engineering, it is required to solve $m$ linear systems, $[A|\mathbf{b}_1\,\mathbf{b}_2\,\dots \mathbf{b}_m]$, that have the same matrix of coefficients. In this situation is where the $LU$ Decomposition comes in handy. In {numref}`tbl:comparison_gausselim_LU` we can see the comparison in the number of operations need to solve several linear systems when using row reduction and $LU$ decomposition.


:::{latextable} Comparison between solving linear systems with row reduction (RR) and with $LU$ decomposition ($LU$)
:header-rows: 2
:class: longtable table-bordered table-striped table-hover table
:align: right
:name: tbl:comparison_gausselim_LU

\begin{tabular}{crrrrrr}
$n$ &   \multicolumn{2}{c}{$m=5$} &   \multicolumn{2}{c}{$m=10$} &   \multicolumn{2}{c}{$m=50$} \\
& RR & $LU$   & RR & $LU$   & RR & $LU$ \\ 
$3$ & $140$ & $88$ & $280$ & $163$ & $1400$ & $763$ \\
$5$ & $575$ & $295$ & $1,150$ & $520$ & $5,750$ & $2,320$ \\
$10$ & $4,025$ & $1,565$ & $8,050$ & $2,515$ & $40,250$ & $10,115$ \\
\end{tabular}

:::

</li>
</ul>


## Theoretical Exercises


<ol type="1">
<li id="Item:prove_statment_c_properties_triangular_matrices">

 Prove {prf:ref}`Prop:LUDecomp:PropertiesTriangularMatricesInverse`. **Hint:** Write the matrix $[A\vert I]$ and apply row operations to compute $A^{-1}$. The idea is similar to the one used in the proof of {prf:ref}`thm:existence_and_uniqueness_LU`.

</li>
<li>

Check that the number of arithmetic operations needed to solve a linear system using row reduction (without exchanging rows) and with $LU$ decomposition is the same.

</li>
</ol>

[^flopnote]: In some books they use the abbreviation flop (floating point operations).