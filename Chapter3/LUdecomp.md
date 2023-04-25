:::{review}
:::

# Matrix Factorisation

When solving linear systems, it is very convenient to find an echelon form, so you can solve it using backward substitution as shown in {prf:ref}`Ex:LinSystems:I`. 

In this section we will learn how to solve an $n\times n$ linear system $A\mathbf{x}=\mathbf{b}$ for which there is a unique solution, by decomposing (or factorising) the matrix $A$ into a product of two matrices. There are several methods for factorising matrices. The factorisations that we will see in this section use **direct methods**. Direct methods are methods that produce the exact solution in a finite number of steps.

There are special cases where solving linear systems can be done quickly. These cases involve triangular or trapezoidal matrices. In general, when the matrix associated with an $m\times n$ linear system is a trapezoidal matrix we can use backward or forward substitution for solving them. The most common factorisation methods make use of these kind of matrices. This is why we will first introduce the idea of a trapezoidal and triangular matrices and then discuss the corresponding factorisation methods and their applications.



## Trapezoidal and Triangular matrices

At this point one probably figured out that when we find an echelon form for an $m\times n$ matrix, that echelon form is actually a trapezoidal matrix. However, to talk about trapezoidal matrices, first we need to revisit the concept of "main diagonal" of a matrix introduced in {prf:ref}`Def:MatrixOps:MainDiagonal`. We will extend this concept to non-square matrices.

:::{prf:definition} Main diagonal of a matrix

For an $m\times n$ matrix $A$, we call the elements $a_{ii}$ the **diagonal elements** of $A$. The (ordered) set of the diagonal elements is called the **main diagonal** of $A$.

:::

Now we are ready to define the objects that we will 

::::::{prf:definition} Trapezoidal and Triangular Matrices
<ul>
<li>

We say that an $m\times n$ matrix $U$ is an **upper trapezoidal matrix** if all the entries below the main diagonal are zero. I.e., an upper trapezoidal matrix that has the form 


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

where the $\blacksquare$ represent any real number in the main diagonal, and $\ast$ represent any real number above the main diagonal. If the matrix is a squared matrix, then it is called **upper triangular**.


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

where the $\blacksquare$ represent any real number in the main diagonal, and $\ast$ represent any real number below the main diagonal. If the matrix is a squared matrix, then it is called **lower triangular**.

</li>
</ul>

::::::


Observe that, when all $\ast$ are zero and the matrix is squared, then the matrix is a diagonal matrix.


::::::{prf:example}

Below there are examples of triangular matrices.

<ul>
<li>

The matrix 

$$
\begin{bmatrix}
1 & 0 & 0 \\
0 & -9 & 0 \\
0 & 0 & 11
\end{bmatrix}
$$


is a $3\times 3$ both upper and lower triangular matrix.

</li>
<li>

The matrix 
 

$$
\begin{bmatrix}
2 &  0  &  0  & 0 \\
4 &  6  &  0  & 0 \\
8 &  10  &  12  & 0 \\
14 & 16 & 18 & 20
\end{bmatrix}
$$


is a $4\times 4$ lower triangular matrix.

</li>
<li>

The matrix 

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

</li>
</ul>

::::::



Trapezoidal matrices have nice properties with respect to their sum and their product.



::::::{prf:proposition} Properties of trapezoidal matrices
:label: prop:PropertiesTriangularMatrices


Let $A$ and $B$ be two upper trapezoidal (resp. lower trapezoidal) matrices. Then the following properties hold:

<ol type = "i">
<li id="Item:prop:PropertiesTriangularMatrices_sum">

$A+B$ is an upper (resp. lower) trapezoidal matrix (whenever the sum makes sense).


</li>
<li id="Item:prop:PropertiesTriangularMatrices_product">

$AB$ is an upper (resp. lower) trapezoidal matrix (whenever the product makes sense).


</li>
<li id="Item:prop:PropertiesTriangularMatricesInverse">

If $A$ is an invertible upper (resp. lower) triangular matrix, then $A^{-1}$ is upper (resp. lower) triangular matrix.

</li>
</ol>



::::::




The proof is technical and it involves computations (especially <a href="#Item:prop:PropertiesTriangularMatricesInverse">iii.</a>). So the reader may skip this proof and convince themselves that the properties hold true by looking at the following example.



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

Before we start the proof, we will introduce the following notation. We will 

::::::{prf:proof} (of {prf:ref}`prop:PropertiesTriangularMatrices`)

The proof of <a href="#Item:prop:PropertiesTriangularMatrices_sum">i.</a> follows from the fact that matrices are added component-wise. Therefore, the entries below the main diagonal of $A+B$ will be zero since both $A$ and $B$ have zero entries below the main diagonal.
 
To prove <a href="#Item:prop:PropertiesTriangularMatrices_product">ii.</a> we fix $j < n$ and compute $AB_{(j+k)j}$ for $k=1,2,\dots, n-j$. In other words, we compute the entries below the main diagonal in column $j$:

$$
AB_{(j+k)j} = \sum_{l=1}^{n} a_{(j+k)l}b_{lj}
$$

We observe that for $l\le j$ the components $a_{(i+k)l}$ are zero, and for $l>j$ the components $b_{lj}0$ are zero. Therefore,

\begin{align*}
AB_{(j+k)j} &= \sum_{l=1}^{n} a_{(j+k)l}b_{lj} \\
&= \sum_{l=1}^{j} 0 b_{lj} + \sum_{l=j+1}^n a_{(j+k)j} 0 \\
&= 0.        
\end{align*}
 
The proof for <a href="#Item:prop:PropertiesTriangularMatricesInverse">iii.</a> is proposed as an exercise. See 
<a href="#Item:prove_statment_c_properties_triangular_matrices">Exercise 1</a>.


::::::



## LU Decomposition



As mentioned at the begining of this section, one of the the easiest way to solve a linear system is to factorise the matrix of coefficients by "splitting" it into a product of two trapezoidal matrices. For the following factorisation, we will name these matrices $L$ and $U$, and they will have the property that $L$ is lower triangular and $U$ is upper trapezoidal.  As you probably have guessed, we call this factorisation an $LU$ decomposition.



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
l_{11}\\
l_{21} & l_{22} \\
l_{31} & l_{32} & l_{33} \\
\vdots & \vdots
&
\vdots & \ddots\\
l_{m1} & l_{m2} & l_{m3} & \dots & l_{mm}
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

<ol type = "i">
<li>

 Solve the system $L\mathbf{y}=\mathbf{b}$ and find $\mathbf{y}$.


</li>
<li>

 Solve the system $U\mathbf{x}=\mathbf{y}$ to find $\mathbf{x}$.


</li>
</ol>



At this point the reader may think that such a decomposition involves a lot of work.  However, it takes (roughly) the same number of operations as for finding an echelon form (see {numref}`Subsec:LinSystems:RowReduction`). In addition, this method has the advantage that once the decomposition of a matrix $A$ has been found, then it is faster to solve multiple systems involving the matrix $A$. And why is that? Well, if one thinks about it, once we have an $LU$ decomposition of $A$ then we just need to solve linear systems that involve trapezoidal/triangular matrices, which are "faster" to solve than solving $A\mathbf{x}=\mathbf{b}$. We will formalise this concept below.

First, we will start with a particular case of an LU decomposition and then we will move to the more general setting. Let's see how to find an LU decomposition with a complete example for the case when one does not need to exchange rows (which is not always possible), and with a square matrix of coefficients.


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
3 & 1 & -2 \\
0 & {10}/{3} & {7}/{3} \\
0 & {5}/{3} & {5}/{3}
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




The following example shows how we implement the $LU$ decomposition in practice,  when no row exchanges are needed.



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

We can see that, when no row exchanges are needed, finding an LU decomposition is a quick process. However, the process is slightly different when that is not the case.

::::{prf:example}

Find an $LU$ decomposition of the matrix

$$
A = \begin{bmatrix}
0 & 1 & 2 \\
3 & 4 & 5 \\
6 & 7 & 8
\end{bmatrix}.
$$

::::


At this point, there are important questions that we still need to address: when does a matrix have an $LU$ decomposition? Can a matrix have more than one $LU$ decomposition? It would be convenient if there exists an $LU$ decomposition, that such decomposition is unique.  Before answering these questions, we need to understand how to find an echelon form of a matrix without exchanging any rows in a general case.  As above, we will use a $3\times 3$ matrix as an example, but the idea works the same way for an $n\times n$ matrix.



::::::{prf:example}
:label: ex:echelonformforLUdecomp


Suppose that we have a $3\times 3$ non-singular matrix 
 
$$
A =
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33} 
\end{bmatrix}
.
$$

Since $A$ is non-singular,
there is a pivot position in every row which will allow us to follow the algorithm below. To track the changes, denote by $A^{(0)}=A$. In other words,

$$
A^{(0)}=
\begin{bmatrix}
a^{(0)}_{11}&a^{(0)}_{12}&a^{(0)}_{13} \\
a^{(0)}_{21}&a^{(0)}_{22}&a^{(0)}_{23} \\
a^{(0)}_{31}&a^{(0)}_{32}&a^{(0)}_{33}
\end{bmatrix}
 = 
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} &
a_{33} 
\end{bmatrix}
.
$$



In the first step of finding an echelon form (without exchanging rows), we subtract the first row multiplied by
$m_{21}={a^{(0)}_{21}}/{a^{(0)}_{11}}$ 
to the second one, and we subtract the
first row multiplied by $m_{31} = {a^{(0)}_{31}}/{a^{(0)}_{11}}$
to the third
row. We call the $m_{ij}$ multipliers. Using these multipliers we obtain
$A^{(1)}$:
 

$$
\left[\begin{array}{rrr}a^{(0)}_{11}& a^{(0)}_{12}& a^{(0)}_{13}\\a^{(0)}_{21}& a^{(0)}_{22}& a^{(0)}_{23}\\a^{(0)}_{31}& a^{(0)}_{32}&
a^{(0)}_{33}\end{array} \right]  \begin{array}{l}
[R_1] \\
{[R_2-m_{21}R_1]} \\
{[R_3-m_{31}R_1]} \\
\end{array} \sim 
\begin{bmatrix}
a^{(0)}_{11}&a^{(0)}_{12}&a^{(0)}_{13} \\ 
0&a^{(1)}_{22}&a^{(1)}_{23} \\
0&a^{(1)}_{32}&a^{(1)}_{33}
\end{bmatrix}
 =
A^{(1)}
$$



And with a second step, when subtracting the second row of $A^{(1)}$ multiplied
by $m_{32} = {a^{(1)}_{32}}/{a^{(1)}_{22}}$ to the third one,
we obtain an echelon form:
 

$$

\left[\begin{array}{rrr}a^{(0)}_{11}&a^{(0)}_{12}&a^{(0)}_{13}\\0&a^{(1)}_{22}&a^{(1)}_{23}\\0&a^{(1)}_{32}&a^{(1)}_{33}\end{array} \right]  \begin{array}{l}
[R_1] \\
{[R_2]} \\
{[R_3-m_{32}R_2]} \\
\end{array}\sim
\begin{bmatrix}
a^{(0)}_{11}&a^{(0)}_{12}&a^{(0)}_{13} \\
0&a^{(1)}_{22}&a^{(1)}_{23} \\
0&0&a^{(2)}_{33}
\end{bmatrix}
 = A^{(2)}
$$


In the previous computations, $a^{(1)}_{22} = a^{(0)}_{22}-m_{21}a^{(0)}_{12}$,
$a^{(1)}_{32} = a^{(0)}_{32}-m_{31}a^{(0)}_{12}$, etc.


::::::




With the previous example we got acquainted with the notation that we will use. And now we are ready for answering the questions above.



::::::{prf:theorem}
:label: thm:existence_and_uniqueness_LU


Suppose that $A$ is a
non-singular $n\times n$ matrix with real entries. Then
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
m_{n1} & m_{n2} & \cdots & m_{n(n-1)}    &  1 
\end{bmatrix}
, \qquad 
U=
\begin{bmatrix}
a^{(0)}_{11} & a^{(0)}_{12} & \cdots & a^{(0)}_{1n}\\
& a^{(1)}_{22} & \cdots & a^{(1)}_{2n} \\
&             & \ddots  & \vdots \\
&             &              &a^{(n-1)}_{nn}
\end{bmatrix}
$$

</li>
<li id="Item:thm:existence_and_uniqueness_LU:uniqueness">

The $LU$ decomposition is unique.

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

To prove <a href="#Item:thm:existence_and_uniqueness_LU:existence">i. </a>, suppose that $A$ is non-singular and that we can find an echelon form of $A$ without exchanging rows. Following the notation introduced in {prf:ref}`ex:echelonformforLUdecomp`, we can write the $k$-th step as a product of matrices:



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



We denote the previous product by $A^{(k)}=E^{(k)}A^{(k-1)}$. Since finding an echelon form is an iterative process, we can find $A^{(n)}$ by multiplying $A^(0)$ by the corresponding $E^{(k)}$ matrices to the left:


$$


A^{(n)} = F^{(n-1)}F^{(n-2)}\cdots F^{(3)}F^{(2)}F^{(1)}A^{(0)}  


$$


Since $A^{(n-1)}$ is an upper triangular matrix, we can take it as $U$. Since all matrices $E^{(k)}$ are invertible, we can recover $A^{(0)}$ multiplying $U$ to the left by the corresponding inverse matrices:


$$


A=A^{(0)}={F^{(1)}}^{-1}{F^{(2)}}^{-1}\cdots{F^{(n-1)}}^{-1}{F^{(n-1)}}^{-1}A^{(n)}


$$


So we can define $L={F^{(1)}}^{-1}{F^{(2)}}^{-1}\cdots{F^{(n-1)}}^{-1}{F^{(n-1)}}^{-1}$.
We just need to see that $L$ is, indeed, lower triangular with ones under the diagonal, and it has the multipliers $m_{ij}$ in the entries below it. To see that, we write $F^{(k)} = I - M_k E_k$ where 

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

Observing that

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






## Application of the $LU$ decomposition


One way to measure the performance of an algorithm is counting the number of arithmetic operations\footnote{In some books they use the word flop (floating point operations).} that are necessary for solving a problem. By arithmetic operations we will take into account sums, products, multiplications and divisions. Suppose that we want to solve the linear system $A\mathbf{x}=\mathbf{b}$ by taking the augmented matrix $[ A | \mathbf{b}]$, finding an echelon form with the same solution set, and then using backward substitution.

In the worst-case scenario, for a $3\times 3$ matrix $A$, ($3\times 4$ augmented matrix), we need the following number of arithmetic operations:
<ul>
<li>

 To convert the components $a_{21}$ and $a_{31}$ to a zero value, we need to compute two $m_{ij}$(two divisions), then we need to multiply each component of the first row, starting at $a_{12}$, by each $m_{ij}$(this happens twice, so $2\times 3=6$ products) and then we need to subtract the resulting values to the corresponding components in each row ($2\times 3=6$ subtractions). Therefore, we need a total of $14$ arithmetic operations(8 products/divisions and 6 additions/subtractions).


</li>
<li>

 To convert the component $a_{32}$ to a zero value, we need to compute one $m_{ij}$(one division), then we need to multiply each component of the second row starting at $a_{23}$(this is 2 products), and then we need to subtract the resulting values to the corresponding components in the third row (2 subtractions). This totals 5 arithmetic operations.


</li>
</ul>



So just to bring the augmented matrix to an echelon form requires 19 arithmetic operations (17 multiplications/divisions and 11 additions/subtractions).

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


So when the matrix $A$ is factorised, the number of operations required to solve the system is significantly lower.

Suppose now that $A$ is a non-singular $n\times n$ matrix.
Let's count the number of operations in a general case, and we can see how advantageous it is to factorise our matrix $A$.

<ul>
<li>

 For solving the system directly, for each column $j$ we need to compute the $m_{ij}$($(n-1)$ divisions), then multiply $m_{ij}$ by all the components of row $i$ except for the first $i$, so that is $(n-i)(n-i+1)$ products, and then we need to perform the same number of subtractions. This totals $(n-i)(n-i+2)$ products/divisions and $(n-i)(n-i+2)$ additions/subtractions. Now we need to add these values for all the rows.

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

If we just count the number of arithmetic operations to compute the $LU$ decomposition then we need 
 

$$
\frac{4n^3-3n^2-n}{6}
$$

arithmetic operations.

Using similar reasoning we can calculate the number of arithmetic operations needed to solve an upper triangular linear system, which gives us $n^2$. And solving a lower triangular system with ones in the main diagonal requires $n^2-n$ arithmetic operations.
 
:::{prf:remark}

The total number of arithmetic operations needed to solve a linear system with row reduction (without exchanging rows), and with $LU$ is the same. We leave the proof as an exercise for the reader.

:::

In many applications in engineering, it is required to solve $m$ linear systems, $[A|b_1\,b_2\,\dots b_m]$, that have the same matrix of coefficients. In this situation is where the $LU$ Decomposition comes in handy. In {numref}`tbl:comparison_gausselim_LU` we can see the efficiency of the $LU$ decomposition.


:::{latextable} Comparison between solving linear systems with row reduction (RR) and with $LU$ decomposition ($LU$)
:header-rows: 2
:class: longtable table-bordered table-striped table-hover table
:align: right
:name: tbl:comparison_gausselim_LU

\begin{tabular}{crrrrrr}
$n$ &   \multicolumn{2}{c}{$m=5$} &   \multicolumn{2}{c}{$m=10$} &   \multicolumn{2}{c}{$m=50$} \\
& RR & $LU$   & RR & $LU$   & RR & $LU$ \\ 
$3$ & $140$ & $88$ & $280$ & $163$ & $1400$ & $763$ \\
$5$ & $575$ & $295$ & $1150$ & $520$ & $5750$ & $2320$ \\
$10$ & $4025$ & $1565$ & $8050$ & $2515$ & $40250$ & $10115$ \\
\end{tabular}

:::

</li>
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


## Theoretical Exercises


<ol type="1">
<li id="Item:prove_statment_c_properties_triangular_matrices">

 Prove statement <a href="#Item:prop:PropertiesTriangularMatricesInverse">iii.</a> of {prf:ref}`prop:PropertiesTriangularMatrices` about properties of triangular matrices. **Hint:** Write the matrix $[A\vert I]$ and apply row operations to compute $A^{-1}$. The idea is similar to the one used in the proof of {prf:ref}`thm:existence_and_uniqueness_LU`.

</li>
<li>

Check that the number of arithmetic operations needed to solve a linear system using row reduction (without exchanging rows) and with $LU$ decomposition is the same.

</li>
</ol>