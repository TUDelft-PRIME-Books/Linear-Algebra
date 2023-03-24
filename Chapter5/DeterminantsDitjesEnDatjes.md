(Sec:DetExtras)=
# Overview

In this section we will address the following matters:
<ul>
<li>

 Cramer's rule.  Seemingly the ultimate solution to almost all systems of  $n$  linear  $n$  equations in  $n$  unkowns. 
 
</li>
<li>

 The generalization of the formula 

 $$ 
\left[\begin{array}{cc} a &  b \\  c & d\end{array}   \right]
^{-1} = \dfrac{1}{ad-bc}  \left[\begin{array}{cc} d & -b \\ -c & a\end{array}   \right]
 
$$  

to  $n\times n$  matrices. 
 
</li>
<li>

The determinant as a uniform 'blow-up factor' for an arbitrary linear transformation from  $\R^n$  to  $\R^n$ . 
 
</li>
<li>

A certain generalization of the cross product to  $n$  dimensions. 
 
</li>
</ul>



Before we do so, we first introduce a new notation.

::::::{prf:definition}
:label: Dfn:DetExtras:ReplaceColumn

Let  $A$ be an $n\times n$ matrix, and $\vect{v}$ a vector in $\R^n$.  Then  $A^{(i)}(\vect{v})$  denotes the matrix that results when the $i$th column of $A$  is replaced by the vector $\vect{v}$. 

::::::


::::::{prf:proposition}
:label: Prop:DetExtras:ReplaceColGivesCofactor

If  $\vect{e}_j$  denotes the $j$th vector of the standard basis of $\R^n$, then we have 

$$ 
\det{A^{(i)}(\vect{e}_j)} = (-1)^{j+i} \det{A_{ji}} = C_{ji} 
$$ 

where $A_{ji}$   is the submatrix  and  $C_{ji}$ the cofactor as introduced in the definition of the $n \times n$ determinant ({prf:ref}`Dfn:DetCofactors:Determinant`). 

::::::

The following example  shows what is going on here.


::::::{prf:example}

Let  $A =  \left[\begin{array}{rrrr} 
a_{11} &a_{12} &a_{13} &a_{14}  \\ 
a_{21} &a_{22} &a_{23} &a_{24}  \\ 
a_{31} &a_{32} &a_{33} &a_{34}  \\ 
a_{41} &a_{42} &a_{43} &a_{44} 
\end{array} \right]
$   be the most general $4 \times 4$ matrix. 
 
Then 

$$ 
A^{(4)}(\vect{e}_2) = \left[\begin{array}{rrrr} 
a_{11} &a_{12} &a_{13} &0  \\ 
a_{21} &a_{22} &a_{23} &1  \\ 
a_{31} &a_{32} &a_{33} &0  \\ 
a_{41} &a_{42} &a_{43} &0 
\end{array} \right]
. 
$$ 

Expanding along the fourth column  gives 

$$ 
\det{A^{(4)}(\vect{e}_2)} = \left|\begin{array}{rrrr} 
a_{11} &a_{12} &a_{13} &0  \\ 
a_{21} &a_{22} &a_{23} &1  \\ 
a_{31} &a_{32} &a_{33} &0  \\ 
a_{41} &a_{42} &a_{43} &0 
\end{array} \right|= (-1)^{(2+4)} \left|\begin{array}{rrr} 
a_{11} &a_{12} &a_{13} \\ 
a_{31} &a_{32} &a_{33}  \\ 
a_{41} &a_{42} &a_{43} 
\end{array} \right|= C_{24}. 
\nonumber 
$$ 

::::::


## Cramer's rule

::::::{prf:theorem}
:label: Thm:DeterminantsMisc:Cramer
 
Suppose  $A$ is an invertible matrix.  Then each linear system 

$$ 
A\vect{x} = \vect{b} 
\nonumber 
$$ 

has a unique solution. The $i$th entry of this solution is given by 

:::{math}
:label: Eq:DeterminantsMisc:Cramer

x_i = \dfrac{\det{A^{(i)}(\vect{b})}}{\det{A}}. 
 
:::

::::::


::::::{prf:example}

We use Cramer's rule to solve the system 
 
$$ 
\left\lbrace
\begin{array}{rcc} 
x_1  + 2x_2  + x_3  & = & 3 \\ 
x_1  - x_2   + 2x_3 & = & 4 \\ 
3x_1  + x_2   -5x_3  & = & 1 
\end{array} 
\right.
\quad\text{i.e.} \quad 
\begin{bmatrix} 
1 & 2 & 1 \\ 1 & -1 & 2 \\ 3 & 1 & -5 
\end{bmatrix} 
\left[\begin{array}{c} x_1 \\ x_2 \\ x_3  \end{array} \right]
 = 
\begin{bmatrix}3 \\ 4 \\ 1  \end{bmatrix}. 
$$ 
 
First of all 
 
$$ 
\left|\begin{array}{ccc} \fbox{1} & 2 & 1 \\ 1 & -1 & 2 \\ 3 & 1 & -5  \end{array} \right|= 
\left|\begin{array}{ccc}  1 & 0 & 0 \\ 1 & -3 & 1 \\ 3 & -5 & -8  \end{array} \right|= 
\left|\begin{array}{cc}   -3 & 1 \\  -5 & -8  \end{array} \right|= 29 \neq 0, 
$$ 
 
so the coefficient matrix is invertible and consequently system has a unique solution. 
 
According to Cramer's rule we find the first  entry of the solution: 
 
$$ 
x_1 = \dfrac{\begin{vmatrix}  3 & 2 & 1 \\ 4 & -1 & 2 \\ 1 & \fbox{1} & -5  \end{vmatrix}}{29} = 
\dfrac{\begin{vmatrix}  1 & 0 & 11 \\ 5 & 0 & -3  \\ 1 & 1 & -5  \end{vmatrix}}{29} = 
\dfrac{-\begin{vmatrix}  1 & 11 \\ 5 & -3   \end{vmatrix}}{29} = \dfrac{58}{29} = 2. 
$$ 
 
Likewise we find 
 
$$ 
x_2 = \dfrac{\begin{vmatrix}  1 & 3 & 1 \\ 1 & 4 & 2 \\ 3 & 1 & -5  \end{vmatrix}}{29} = 0 
\quad \text{and} \quad 
x_2 = \dfrac{\begin{vmatrix}  1 & 2 & 3 \\ 1 & -1 & 4 \\ 3 & 1 & 1  \end{vmatrix}}{29} = 1. 
$$ 

::::::


The proof -- you may skip it of course -- rests rather nicely on properties of the determinant function.


::::::{prf:proof}

Suppose $\vect{x} = \vect{c} = \left[\begin{array}{c}  c_1 \\ \vdots\\ c_n\end{array} \right]
$ is the unique solution of the linear system $A\vect{x} = \vect{b}$, with the invertible matrix $A = [ \vect{a}_1  \ldots  \vect{a}_n ]$. 
 
We show that Formula {eq}`Eq:DeterminantsMisc:Cramer` holds for $c_1$. The argument can be copied for the other $c_i$. 
 
We first note that 

$$ 
\begin{array}{ccl} 
A\vect{c} = \vect{b} &\iff \quad & c_1\vect{a}_1+c_2\vect{a}_2 + \ldots + c_n\vect{a}_n =\vect{b} \\ 
&\iff \quad & c_1\vect{a}_1+c_2\vect{a}_2 + \ldots + c_n\vect{a}_n - \vect{b} = \vect{0}. 
\end{array} 
\nonumber 
$$ 
 
The smart next move  is to replace the first column of $A$ by the zero column disguised as 

$$ 
c_1\vect{a}_1+c_2\vect{a}_2 + \ldots + c_n\vect{a}_n - \vect{b}. 
$$ 

So we have 

$$ 
\det{c_1\vect{a}_1+c_2\vect{a}_2 + \ldots + c_n\vect{a}_n - \vect{b}, \vect{a}_2, \ldots, \vect{a}_n} 
=\det{\vect{0}, \vect{a}_2, \ldots,\vect{a}_n}  = 0. 
$$ 

By the linearity property (in all of the columns) of the determinant we may deduce 


:::{math}
:label: Eq:DeterminantsMisc:ProofCramer

c_1\det{A} + c_2\det{A^{(1)}(\vect{a}_2)}  + \ldots + c_n\det{A^{(1)}(\vect{a}_n)}  - \det{A^{(1)}(\vect{b})} = 0. 

:::

 
Now we note that 

$$ 
\det{A^{(1)}(\vect{a}_i)} = 0, \quad  i = 2,3,\ldots n, 
$$ 

since in the matrix $A^{(1)}(\vect{a}_i)$  the first column and the $i$th column are identical. Hence all but the first and last determinant in Equation {eq}`Eq:DeterminantsMisc:ProofCramer`  drop out and we can conclude that indeed 

$$ 
c_1\det{A}  - \det{A^{(1)}(\vect{b})} = 0 
\quad \iff \quad c_1 = \dfrac{\det{A^{(1)}(\vect{b})}}{\det{A}}. 
$$ 

::::::

As an interesting corollary of Cramer's Theorem we present a ready-made formula for the inverse of an invertible matrix.
Again the ideas in the proof are rather straightforward.

::::::{prf:proposition}
:label: Prop:DeterminantsMisc:Inverse

If  $A$ is an invertible  $n \times n$ matrix then the inverse $B$ of $A$ is given by 

$$ 
B = \dfrac{1}{\det{A}} \left[\begin{array}{ccccc} 
C_{11} &C_{21} &C_{31} & \ldots &C_{n1}  \\ 
C_{12} &C_{22} &C_{32} & \ldots &C_{n2}  \\ 
C_{13} &C_{23} &C_{33} & \ldots &C_{n3}  \\ 
\vdots & \vdots &\vdots & \ddots & \vdots \\ 
C_{1n} &C_{2n} &C_{3n} & \ldots &C_{nn}  \\ 
\end{array} \right]
$$ 

::::::


::::::{prf:proof}

The $j$th column $\vect{b}_j$ of $B = A^{-1}$ is the solution of the linear system  $A\vect{x} = \vect{e}_j$. 
Cramer's rule then gives that  $b_{ij}$,  the $i$th entry of this column,  is equal to 
$$ 
b_{ij} = \dfrac{\det{A^{(i)}(\vect{e}_j)}}{\det{A}} = \dfrac{C_{ji}}{\det{A}}. 
$$ 
For the last step we used {prf:ref}`Prop:DetExtras:ReplaceColGivesCofactor`. 

::::::

::::::{prf:definition}

For an $n \times n$ matrix $A$  the matrix 

$$ 
\left[\begin{array}{ccccc} 
C_{11} &C_{12} &C_{13} & \ldots &C_{1n}  \\ 
C_{21} &C_{22} &C_{23} & \ldots &C_{2n}  \\ 
C_{31} &C_{32} &C_{33} & \ldots &C_{3n}  \\ 
\vdots & \vdots &\vdots & \ddots & \vdots \\ 
C_{n1} &C_{n2} &C_{n3} & \ldots &C_{nn}  \\ 
\end{array} \right]
, \quad \text{with} \quad  C_{ij} = (-1)^{i+j} \det{A_{ij}} 
$$ 

is called its **cofactor matrix**. The **adjugate matrix**  of $A$ is defined as the transpose of the cofactor matrix: 

$$ 
\text{Adj}(A) =  \left[\begin{array}{ccccc} 
C_{11} &C_{21} &C_{31} & \ldots &C_{n1}  \\ 
C_{12} &C_{22} &C_{32} & \ldots &C_{n2}  \\ 
C_{13} &C_{23} &C_{33} & \ldots &C_{n3}  \\ 
\vdots & \vdots &\vdots & \ddots & \vdots \\ 
C_{1n} &C_{2n} &C_{3n} & \ldots &C_{nn}  \\ 
\end{array} \right]
. 
$$ 

::::::


So {prf:ref}`Prop:DeterminantsMisc:Inverse` states that

$$
A^{-1} = \dfrac{1}{\det{A}} \text{Adj}(A),
$$

provided that $A$ is invertible.
In fact a slightly more general formula holds for **any** square matrix.


::::::{prf:proposition}

For any matrix  $A$ the following identity holds 

$$ 
A\cdot\text{Adj}(A) = \text{Adj}(A)\cdot A = (\det{A})\cdot I. 
$$ 
 
::::::

The proof we think, is short and instructive.

::::::{prf:proof}

For an invertible matrix the statement follows immediately from {prf:ref}`Prop:DeterminantsMisc:Inverse`. 
 
However, we can give an 'elementary'  proof, that includes the non-invertible case where $\det{A}=0$.  We will use two properties of determinants from earlier sections. 
First  {prf:ref}`Thm:DetCofactors:RowOrColumnExpansion`, that states that the  determinant of a matrix  can be found by expansion  along an arbitrary row 

$$ 
\det{A} = \sum_{j=1}^n   (-1)^{i+j} a_{ij}\det{A_{ij}} = \sum_{j=1}^n   a_{ij} C_{ij}. 
$$ 

And second {prf:ref}`Cor:DetRowReduction:EqualRows`. If a matrix  $A$  has two equal rows    (or: columns),  then  $\det{A} = 0$. 
 
Let us  consider the product    $A\cdot\text{Adj}(A)$  very carefully: 

$$ 
\left[\begin{array}{ccccc} 
a_{11} &a_{12} &a_{13} & \ldots &a_{1n}  \\ 
a_{21} &a_{22} &a_{23} & \ldots &a_{2n}  \\ 
a_{31} &a_{32} &a_{33} & \ldots &a_{3n}  \\ 
\vdots & \vdots &\vdots & \ddots & \vdots \\ 
a_{n1} &a_{n2} &a_{n3} & \ldots &a_{nn}  \\ 
\end{array} \right]
\left[\begin{array}{ccccc} 
C_{11} &C_{21} &C_{31} & \ldots &C_{n1}  \\ 
C_{12} &C_{22} &C_{32} & \ldots &C_{n2}  \\ 
C_{13} &C_{23} &C_{33} & \ldots &C_{n3}  \\ 
\vdots & \vdots &\vdots & \ddots & \vdots \\ 
C_{1n} &C_{2n} &C_{3n} & \ldots &C_{nn}  \\ 
\end{array} \right]
. 
$$ 

On the diagonal we see that the $i$th entry is equal to 

$$ 
a_{i1}C_{i1} + a_{i2}C_{i2} + \ldots + a_{in}{C_{in}} = \sum_{j=1}^n   a_{ij} C_{ij} = \det{A}. 
$$ 

For the off-diagonal elements we find as product of the $k$th row of $A$ with the $i$th column of $\text{Adj}(A)$ the sum 

$$ 
a_{k1}C_{i1} + a_{k2}C_{i2} + \ldots + a_{kn}{C_{in}} = \sum_{j=1}^n   a_{kj} C_{ij}. 
$$ 

This expression can be interpreted as the expansion along the $i$th row of the matrix $\tilde{A}$ that results if the $i$th row of 
$A$ is replaced by the $k$th row of $A$.  Since the matrix $\tilde{A}$ has two equal rows, this determinant must be zero! 

::::::


A few remarks, amongst which rather a downer, to conclude this subsection.

<ul>
<li>

For  $n = 2$  {prf:ref}`Prop:DeterminantsMisc:Inverse`  gives us back the old formula for the inverse. 
 
That is,  if we define the determinant of a  $1 \times 1$  matrix   $A = [a]$  as the number  $a$ . 
 
</li>
<li>

For an arbitrary invertible  $3 \times 3$  matrix 
 $A=\left[\begin{array}{ccc} a_{11} &a_{12} &a_{13}   \\ a_{21} &a_{22} &a_{23}  \\ a_{31} &a_{32} &a_{33} \end{array} \right] $  the formula yields 
 
$$ 
A^{-1}  =  \dfrac{1}{\begin{vmatrix} 
a_{11} &a_{12} &a_{13}   \\ 
a_{21} &a_{22} &a_{23}  \\ 
a_{31} &a_{32} &a_{33} 
\end{vmatrix}} 
\left[\begin{array}{ccc} 
\begin{vmatrix} a_{22} & a_{23} \\ a_{32} & a_{33}  \end{vmatrix} & 
- \begin{vmatrix} a_{12} & a_{13} \\ a_{32} & a_{33}  \end{vmatrix} & 
\begin{vmatrix} a_{12} & a_{13} \\ a_{22} & a_{23}  \end{vmatrix} \\ 
- \begin{vmatrix} a_{21} & a_{23} \\ a_{31} & a_{33}  \end{vmatrix} & 
\begin{vmatrix} a_{11} & a_{13} \\ a_{31} & a_{33}  \end{vmatrix} & 
- \begin{vmatrix} a_{21} & a_{31} \\ a_{22} & a_{32}  \end{vmatrix} \\ 
\begin{vmatrix} a_{21} & a_{22} \\ a_{31} & a_{32}  \end{vmatrix} & 
- \begin{vmatrix} a_{11} & a_{31} \\ a_{12} & a_{32}  \end{vmatrix} & 
\begin{vmatrix} a_{11} & a_{12} \\ a_{21} & a_{22}  \end{vmatrix} 
\end{array} 
\right]
$$

</li>
<li>

(Disclaimer 1)  Cramer's formula can only be used for a **square** linear system with an **invertible** matrix. 
 
</li>
<li>

(Disclaimer 2) Both Cramer's formula and the formula for the inverse are **highly inefficient**.  For instance, for a system 

$$ 
A\vect{x} = \vect{b} 
$$  

of four equations in four unknowns, to find the solution using Cramer's rule, one needs to compute five  $4 \times 4$  determinants.  Using the  good-old method  using  the augmented matrix   $[A|\vect{b}]$  only asks for one row reduction process.  And also the comparison between the efforts required when   computing the inverse via the adjugate matrix versus the  row reduction of the augmented matrix   $[A|I]$  works out rather favorably for the latter. 
 
</li>
</ul>



## Determinants and volume

We have seen in {numref}`Sec:DetGeometric` how determinants popped up in the context of areas of parallelograms and volumes of parallelepipeds.

In {numref}`Sec:Vectors` we used the inner product to define length, distance and orthogonality in $\R^n$.  Determinants are the means to define the concepts of volume and orientation in $n$ dimensions.


::::::{prf:definition} Volume and orientation in $\R^n$ 


Let $(\vect{v_1}, \ldots, \vect{v}_n)$ be an ordered set of $n$ vectors in $\R^n$. 
The $n$-dimensional parallelepiped $\mathcal{E}$  spanned by $\vect{v_1}, \ldots, \vect{v}_n$ is the set 

$$ 
\mathcal{E} = \{c_1\vect{v}_1+c_2\vect{v}_2 + \ldots + c_1\vect{v}_n | c_i \in \R,  0 \leq c_i \leq 1\}. 
$$ 

The **volume** of such a parallelepiped is defined by 
$$ 
\text{Vol}(\mathcal{E}) = |\det{\vect{v_1}, \ldots, \vect{v}_n}|. 
$$ 

So, it is the absolute value of a determinant. 
 
If, furthermore,  the vectors in $(\vect{v_1}, \ldots, \vect{v}_n)$  are linearly independent, then we say that 
 
$(\vect{v_1}, \ldots, \vect{v}_n)$ is **positively oriented** $\quad$ if $ \quad \det{\vect{v_1}, \ldots, \vect{v}_n}>0$. 
 
And of course, the set is called **negatively oriented** if this determinant is negative. 

::::::


::::::{prf:proposition}
:label: Prop:DetExras:DetAsBlowupFactor
 
Suppose $T$ is a linear transformation from $\R^2$ to $\R^2$, with standard matrix $A = [\vect{a}_1   \vect{a}_2]$, so 

$$ 
T(\vect{x}) = A\vect{x}, \quad  \text{for} \quad  \vect{x} \text{  in  } \R^2. 
$$ 

Let  $R$ be any region in $\R^2$ for which the area $A(R)$ is well-defined, and let $S$ be the image of $R$ under $T$. 
 
Then  for the area $A(S)$  it holds that 

$$ 
A(S) = |\det{A}|\cdot A(R). 
$$ 

::::::


::::::{prf:proof}

If the matrix $A$ is not invertible, the range of $T$, which is given by  $\text{span}\{\vect{a}_1, \vect{a}_2\}$, is contained in a line. 
Each region $R$ is then mapped onto a subset $S$ that is contained in this line, so 

$$ 
A(S) = 0 = 0\cdot A(R) =|\det{A}|\cdot A(R). 
$$ 

Next suppose that $A$ is invertible.  Then the unit grid is  mapped onto a grid with as unit region the parallelogram with sides  $\vect{a}_1 = A\vect{e}_1$  and  $\vect{a}_2 = A\vect{e}_2$ .  See {numref}`Figure %s <Fig:DetExtras:Grid>`. 
 

::::{figure} Images/Fig-DetExtras-StandardGrid.svg
:name: Fig:DetExtras:Grid

The image of the standard grid

::::

 
First we show that the formula holds if  $R$  is the unit square, i.e., the parallelogram generated by $\vect{e}_1$  and $\vect{e}_2$. \\ 
The unit square is mapped onto the parallelogram $S$ generated by $T(\vect{e}_1)=\vect{a}_1$  and $T(\vect{e}_2)=\vect{a}_2$. It follows 
that 

$$ 
A(S) = |\det{\vect{a}_1, \vect{a}_2}|  = |\det{A}| = |\det{A}| \cdot A(R), 
$$ 

since $A(R) = 1$. 
 
This then also holds for any square $R$ with sides of length $r$ that are parallel to the axes.  Namely,  such a square has area $r^2$ and can be described as the square with vertices 

$$ 
\vect{p},\quad  \vect{p}+ r\vect{e}_1, \quad \vect{p}+ r\vect{e}_1+r\vect{e}_2) \quad\text{and}\quad  \vect{p}+ r\vect{e}_2. 
$$ 

These are mapped to 

$$ 
A\vect{p},  A\vect{p}+ rA\vect{e}_1, A\vect{p}+ rA\vect{e}_1+rA\vect{e}_2 \quad\text{and}\quad  A\vect{p}+ rA\vect{e}_2. 
$$ 

This is a parallelogram with sides  $rA\vect{e}_1 = r\vect{a}_1$  and  $rA\vect{e}_2 =r \vect{a}_2$, which has area 

$$ 
A(S) =  |\det{r\vect{a}_1, r\vect{a}_2}|   = r^2 |\det{A}| =   |\det{A}|\cdot A(R). 
$$ 
 
See {numref}`Figure %s <Fig:DetExtras:ImageOfSquare>` 
 


::::{figure} Images/Fig-DetExtras-ImageOfSquare.svg
:name: Fig:DetExtras:ImageOfSquare


The image of a square with 'corner' $\vect{p}$  and radius $r$
::::

For a general (reasonable) region $R$  we sketch the idea and omit the technical details. 

The region $R$ can be approximated arbitrarily close by a collection of smaller and smaller  squares  $R_i$ of which the interiors do not overlap. 
See {numref}`Figure %s <Fig:DetExtras:Subdivision>`. 
In $\R^2$ areas of more general regions than parallelograms can be computed by subdividing and/or approximating them by parallelograms. 
We can do the same in higher dimensions, but picturing the process becomes elusive. 
 

::::{figure} Images/Fig-DetExtras-Subdivision.svg
:name: Fig:DetExtras:Subdivision

Approximating a region by smaller and smaller squares

::::

The formula holds for each of the $R_i$. Since $T$ is one-to-one, the images $S_i = T(R_i)$  will not overlap either, and the images taken together will   approximate the image $S = T(R)$ as well. We deduce that 

$$ 
A(S) \approx \sum A(S_i) = \sum  |\det{A}|\cdot A(R_i) = |\det{A}| \sum  A(R_i) \approx  |\det{A}|\cdot A(R). 
$$ 

By taking an appropriate limit one can show that in fact 

$$ 
A(S) = |\det{A}|A(R). 
$$ 

::::::


{prf:ref}`Prop:DetExras:DetAsBlowupFactor`  can be generalized to larger dimensions $n$.  E.g., for $n = 3$ it states that for any   linear transformation  $T$ from $\R^3$ to $\R^3$, with standard matrix $A$, and any 'reasonable' region $R$ in $\R^3$
it is true that

$$
\text{Vol}(S) = |\det{A}|\cdot \text{Vol}(R),  \quad \text{where  } S \text{  is the image of
}R: \quad S = T(R).
$$



## Determinant and cross product

In {numref}`Sec:DetGeometric`  we defined the determinant of the ordered set $(\vect{a},\vect{b},\vect{c})$  in $\R^3$  via

$$
\begin{array}{rcl}
\det{\vect{a},\vect{b},\vect{c}} &=& (\vect{a}\times\vect{b})\ip\vect{c} =
\left|\begin{array}{ccc}  a_1 & b_1 &c_1 \\ a_2 & b_2 &c_2 \\ a_3 & b_3 & c_3   \end{array}\right|\\
&=&
\left|\begin{array}{cc}  a_2 & a_3   \\b_2 & b_3      \end{array}\right| c_1
- \left|\begin{array}{cc}  a_1 & a_3   \\b_1 & b_3      \end{array}\right| c_2
+ \left|\begin{array}{cc}  a_1 & a_2   \\b_1 & b_2      \end{array}\right| c_3.
\end{array}
$$

Conversely, we can write the cross product  in terms containing determinants.

:::{math}
:label: Eq:DetExtras:DetCrossProd

\begin{array}{rcl} 
\left[\begin{array}{c} a_1 \\ a_2 \\ a_3         \end{array}\right] \times 
\left[\begin{array}{c}b_1 \\ b_2 \\ b_3         \end{array}\right] 
&=& \left[\begin{array}{c}a_2b_3-a_3b_2 \\ a_3b_1 - a_1b_3 \\ a_2b_1-a_2b_1        \end{array}\right] \\ 
&=& 
\left|\begin{array}{cc}  a_2 & a_3   \\b_2 & b_3      \end{array}\right|\vect{e}_1 
- \left|\begin{array}{cc}  a_1 & a_3   \\b_1 & b_3      \end{array}\right|\vect{e}_2 
+ \left|\begin{array}{cc}  a_1 & a_2   \\b_1 & b_2      \end{array}\right|\vect{e}_3. 
\end{array} 
 
:::

The last expression can formally be written as

$$
\left|\begin{array}{ccc}  a_1 & b_1 &\vect{e}_1 \\ a_2 & b_2 &\vect{e}_2 \\ a_3 & b_3 & \vect{e}_3   \end{array}\right|.
$$

In exactly the same fashion, for $n-1$ vectors $\vect{a}_1, \ldots, \vect{a}_{n-1}$  in $\R^n$,  say

$$
\vect{a}_1 = \left[\begin{array}{c}  a_{11} \\ a_{21} \\ \vdots \\  a_{n1}      \end{array}\right], \quad
\vect{a}_2 = \left[\begin{array}{c}  a_{12} \\ a_{22} \\ \vdots \\  a_{n2}      \end{array}\right], \quad
\ldots \quad , \quad
\vect{a}_{n-1} = \left[\begin{array}{c}  a_{1,(n-1)} \\ a_{2(n-1)} \\ \vdots \\  a_{n,(n-1)}      \end{array}\right]
$$

we can define

:::{math}
:label: Eq:DetExtras:DetCrossProd-ndim

\vect{N}(\vect{a}_1, \ldots, \vect{a}_{n-1}) = \vect{a^{\ast}}_n = \left|\begin{array}{ccccc} 
a_{11} & a_{12} & \ldots & a_{1,(n-1)} & \vect{e}_1 \\ 
a_{21} & a_{22} & \ldots & a_{2,(n-1)} & \vect{e}_2 \\ 
\vdots & \vdots &        &    \vdots   &  \vdots \\ 
a_{n1} & a_{n2} & \ldots & a_{2,(n-1)} & \vect{e}_n 
\end{array}\right|. 

:::


With some effort it can be shown that the following properties hold:


::::::{prf:proposition}
:label: Prop:DetExtras:Properties-ndimCrossProd

Suppose that $\vect{a}_1, \ldots, \vect{a}_{n-1}$ are vectors in $\R^n$ and $\vect{a^{\ast}}_n$ is defined as in Equation {eq}`Eq:DetExtras:DetCrossProd-ndim`.  Then the following properties hold. 
<ol type = "i">
<li>

$\vect{a}_i \perp\vect{a^{\ast}}_n$ ,  for   $i = 1,2,\ldots, n-1$ . 
 
</li>
<li>

$ \{\vect{a}_1, \ldots, \vect{a}_{n-1}\}$   is linearly dependent if and only if   $\det{\left[\vect{a}_1, \ldots, \vect{a}_{n-1}, \vect{a^{\ast}}_n\right]
} = 0$ . 
 

</li>
<li>

If   $ \{\vect{a}_1, \ldots, \vect{a}_{n-1}\}$   is linearly independent, then   $\det{\left[\vect{a}_1, \ldots, \vect{a}_{n-1}, \vect{a^{\ast}}_n\right]
} > 0$ . 
 
</li>
<li>

The norm of the vector  $\vect{a^{\ast}}_n$   is equal to the  $(n-1)$ -dimensional volume of the  $(n-1)$ -dimensional parallelepiped  generated by  $\vect{a}_1, \ldots, \vect{a}_{n-1}$ . 
 
</li>
</ol>

::::::


In fact,  for an independent set of vectors $\{\vect{a}_1, \ldots, \vect{a}_{n-1}\}$ in $\R^n$, these properties uniquely determine $\vect{a^{\ast}}_n$
as the vector $\vect{v}$ that is orthogonal to $ \vect{a}_1, \ldots, \vect{a}_{n-1}$, has a prescribed length, and makes the  ordered set
$(\vect{a}_1, \ldots, \vect{a}_{n-1}, \vect{v}) $ positively oriented.


::::::{prf:example}

For  $n = 2$  we get, for an arbitrary vector  $\vect{v} = 
\left[\begin{array}{c}   a \\ b   \end{array}\right]
 \neq \left[\begin{array}{c}   0\\0  \end{array}\right]
$: 

$$ 
\vect{w} = \vect{N}\left(\vect{v}\right)
 = 
\left|\begin{array}{cc} 
a & \vect{e}_1\\ 
b & \vect{e}_2 
\end{array}\right|=  a\vect{e}_1 - b\vect{e}_2 = \left[\begin{array}{c}    -b \\ a          \end{array}\right|. 
$$ 

This is indeed an vector orthogonal to $\vect{v}$ with the same 'one-dimensional volume', i.e., length,  as the vector $\vect{v}$. 

Moreover,  $\left(\vect{v}, \vect{w}\right)
 =  \left(\left[\begin{array}{c}   a \\ b   \end{array}\right]
,  \left[\begin{array}{c} -b \\ a   \end{array}\right]
 \right)
$ 
is positively oriented. 

This shows that the construction also works in $\R^2$. 

::::::


::::::{prf:proof} (Proof of {prf:ref}`Prop:DetExtras:Properties-ndimCrossProd`)

The properties follow from the observation that for each vector $\vect{v}$ in $\R^n$ 
 
$$ 
\begin{array}{rcl} 
\vect{a^{\ast}}_n \ip \vect{v} 
&=&  \vect{N}(\vect{a}_1, \ldots, \vect{a}_{n-1})\ip\vect{v} \\ 
&=& \left|\begin{array}{ccccc} 
a_{11} & a_{12} & \ldots & a_{1,(n-1)} & v_1 \\ 
a_{21} & a_{22} & \ldots & a_{2,(n-1)} & v_2 \\ 
\vdots & \vdots &        &    \vdots   &  \vdots \\ 
a_{n1} & a_{n2} & \ldots & a_{2,(n-1)} & v_n 
\end{array}\right|\\ 
&=& \det{\vect{a}_1, \ldots, \vect{a}_{n-1},\vect{v}}. 
\end{array} 
\nonumber 
$$ 
 
This  immediate generalization of the identity  $(\vect{a}\times\vect{b})\ip\vect{c} = \det{[\vect{a},\vect{b},\vect{c}] }$ follows if 
we write Equation {eq}`Eq:DetExtras:DetCrossProd-ndim`    as in equation {eq}`Eq:DetExtras:DetCrossProd`. 
<ol type = "i">

<li>

Take any of the vectors   $a_j$ . Then 

$$ 
\vect{N}(\vect{a}_1, \ldots, \vect{a}_{n-1})  \ip \vect{a}_j= \det{ \left[\vect{a}_1, \ldots, \vect{a}_{n-1},\vect{a}_j \right]
 } = 0, 
$$  

since the determinant has two equal columns. 
So indeed 
 
$$ 
\vect{N}(\vect{a}_1, \ldots, \vect{a}_{n-1})  \perp \vect{a}_j,\quad j = 1, \ldots, n-1. 
$$

</li>
<li>

  First suppose that  the columns of the matrix 
 
$$ 
\begin{bmatrix} 
a_{11} & a_{12} & \ldots & a_{1,(n-1)} \\ 
a_{21} & a_{22} & \ldots & a_{2,(n-1)}  \\ 
\vdots & \vdots &        &      \vdots \\ 
a_{n1} & a_{n2} & \ldots & a_{2,(n-1)} 
\end{bmatrix} 
$$ 

are linearly dependent.  Then for  each vector  $\vect{v}$  in  $\R^n$

$$ 
\vect{a^{\ast} }_n \ip \vect{v}  =  \det{ \left[\vect{a}_1, \ldots, \vect{a}_{n-1},\vect{v} \right]
 }  =  0. 
$$ 

This implies that  $\vect{a^{\ast}}_n$   must be the zero vector. 
 
Conversely, if the vectors   $\{ \vect{a}_1, \ldots, \vect{a}_{n-1} \}$   are linearly independent, 
then the  $n \times (n-1)$  matrix   $A = [ \vect{a}_1   \ldots   \vect{a}_{n-1}  ] $  
has rank  $n-1$ .  The matrix  $A$  must have  $n-1$  linearly independent rows.  Say, if we delete the  $k$ -th row we have an  $(n-1) \times (n-1)$  sub-matrix  with independent rows. 
Then the coefficient of  $\vect{e}_k$  in the expansion of 
 $ \vect{N} ( \vect{a}_1, \ldots, \vect{a}_{n-1} ) $ , 
which is precisely the determinant of this submatrix, is nonzero. 
 

</li>
<li>

This is a consequence of the observation 
 
$$ 
\det{ \left[\vect{a}_1, \ldots, \vect{a}_{n-1},\vect{a^{\ast}}_n \right]
 } = \vect{a^{\ast}}_n \ip \vect{a^{\ast}}_n 
= \norm{\vect{a^{\ast}}_n}^2 \geq 0 
$$ 

and the already established fact that   $\vect{a^{\ast}}_n  \neq \vect{0}$  
if    $\{\vect{a}_1, \ldots, \vect{a}_{n-1}\}$   is linearly independent. 
 
</li>
<li>

We sketch the idea, which we lend from volume versus area considerations in  $\R^2$   and  $\R^3$ . 
We defined the volume of the  $n$ -dimensional parallelepiped  $\mathcal{P} \left(\vect{a}_1, \ldots, \vect{a}_{n} \right) $  
generated by the   $n$   vectors  $\vect{a}_1, \ldots, \vect{a}_{n}$   as the absolute value of the determinant: 
 
$$ 
\text{Vol}\left(\mathcal{P}(\vect{a}_1, \ldots, \vect{a}_{n}) \right)
 = |\det{\left[\vect{a}_1, \ldots, \vect{a}_{n}\right]
 }|. 
$$ 

The height times base principle in  $\R^n$  must be: 
 
if 
 
$$ 
a_{n} \perp \mathcal{P}(\vect{a}_1, \ldots, \vect{a}_{n-1}) 
$$ 

then 
 
$$ \text{Vol} \left(\mathcal{P}(\vect{a}_1, \ldots, \vect{a}_{n} \right)
 = 
\text{Vol} \left(\mathcal{P}(\vect{a}_1, \ldots, \vect{a}_{n-1}) \right)
\cdot \norm{\vect{a}_{n}}. 
$$ 

If we apply this to the vector   $\vect{a}_{n} = \vect{a^{\ast}}_n = \vect{N}(\vect{a}_1, \ldots, \vect{a}_{n-1})$ , which is orthogonal to all vectors 
 $\vect{a}_1, \ldots, \vect{a}_{n-1}$ , we have on the one hand that 
 
$$ 
\text{Vol}\left(\mathcal{P}(\vect{a}_1, \ldots, \vect{a}_{n-1}, \vect{a^{\ast}}_n) \right)
 = 
\text{Vol}\left(\mathcal{P}(\vect{a}_1, \ldots, \vect{a}_{n-1}) \right)
\cdot \norm{\vect{a^{\ast}}_n} 
$$ 

and on the other hand 
 
$$ 
\begin{array}{rcl} 
\text{Vol}\left(\mathcal{P}(\vect{a}_1, \ldots, \vect{a}_{n-1}, \vect{a^{\ast}}_n \right)
 &=& 
|\det{ \left[\vect{a}_1, \ldots, \vect{a}_{n-1}, \vect{a^{\ast}}_n \right]
 }| \\ 
&=& 
| \vect{a^{\ast}}_n\ip \vect{a^{\ast}}_n| = \norm{\vect{a^{\ast}}_n}^2. 
\end{array}. 
$$ 

Equating the two expressions for  $\text{Vol} \left(\mathcal{P} (\vect{a}_1, \ldots, \vect{a}_{n-1}, \vect{a^{\ast}}_n) \right) $  
we conclude that indeed 
 
$$ 
\norm{\vect{a^{\ast}}_{n}} = \text{Vol} \left(\mathcal{P} (\vect{a}_1, \ldots, \vect{a}_{n-1}) \right)
. 
$$

</li>
</ol>
 
::::::
