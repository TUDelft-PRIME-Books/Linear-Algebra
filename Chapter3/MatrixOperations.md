(Sec:MatrixOps)=

# Matrix Operations

## Introduction

In Chapter 2 matrices were introduced to represent systems of linear equations. The coefficients of a linear system were put into the coefficient matrix $A$, and a system as a whole could be squeezed into the augmented matrix. In {numref}`Sec:LinTrafo` we used matrices to construct linear transformations. In this chapter we will study matrices as entities on their own, though every now and then we will keep in mind their role in the two contexts just mentioned.

## Sum, scalar multiple and transpose

In this section we will define the sum and the product of two matrices, and the transpose of a matrix. Recall that an $m\times n$ matrix has $m$ (horizontal) rows of size $n$ or, equivalently, $n$ (vertical) columns of size $m$.

::::::{prf:definition} Equality of matrices
Two matrices are said to have the same **size** if they have the same number of rows and the same number of columns.

Two matrices $A$ and $B$ are **equal** if they have the same size, say $m$ rows and $n$ columns, and all the corresponding entries are equal, i.e.

$$
  a_{ij} = b_{ij},\,\quad  \text{for} \quad i = 1,\ldots,m, \quad j = 1,\ldots,n.
$$

::::::

::::::{prf:definition}
A **zero matrix** $O$ is a matrix with all entries equal to 0. If the context requires clarity as to its size it may be denoted by $O_{mn}$.

::::::

::::::{prf:definition} Scalar multiplication

If $A$ is an $m\times n$ matrix and $c$ is a scalar, then $cA$ is the $m \times n$ matrix that is the result of multiplying each entry of $A$ by $c$:

$$
  c \left[\begin{array}{cccc}
            a_{11} & a_{12}&   \ldots&  a_{1n} \\
            a_{21} & a_{22}&  \ldots&  a_{2n} \\
            \vdots &  \vdots&  \cdots& \vdots    \\
            a_{m1} & a_{m2}&  \ldots& a_{mn}
          \end{array}
   \right]= \left[\begin{array}{cccc}
            ca_{11} & ca_{12}&  \ldots&  ca_{1n} \\
            ca_{21} & ca_{22}&   \ldots&  ca_{2n} \\
            \vdots &  \vdots&  \cdots& \vdots    \\
            ca_{m1} & ca_{m2}&    \ldots& ca_{mn}
          \end{array}
   \right].
$$

We then say that $cA$ is a **scalar multiple** of $A$, or simply a **multiple** of $A$.

::::::

::::::{prf:definition} The sum of two matrices

If $A$ and $B$ are two $m\times n$ matrices then the **sum** $A+B$ is the
$m\times n$ matrix of which the entry on the position $(i,j)$ is the sum of the corresponding entries of $A$ and $B$:

$$
  \left[\begin{array}{cccc}
            a_{11} & a_{12}&  \ldots& a_{1n} \\
            a_{21} & a_{22}&  \ldots&   a_{2n} \\
            \vdots &  \vdots&  \cdots&  \vdots    \\
            a_{m1} & a_{m2}&  \ldots&   a_{mn}
          \end{array} \right]    +
  \left[\begin{array}{cccc}
            b_{11} & b_{12}&   \ldots&  b_{1n} \\
            b_{21} & b_{22}&   \ldots&  b_{2n} \\
            \vdots &  \vdots&   \cdots& \vdots    \\
            b_{m1} & b_{m2}&    \ldots& b_{mn}
          \end{array} \right]=
$$

$$
    = \left[\begin{array}{cccc}
            a_{11}+b_{11} & a_{12}+b_{12}&  \ldots&   a_{1n}+b_{1n} \\
            a_{21}+b_{21} & a_{22}+b_{22}&  \ldots&   a_{2n}+b_{2n} \\
            \vdots &  \vdots&  \cdots&  \vdots    \\
            a_{m1}+b_{m1} & a_{m2}+b_{m2}&   \ldots& a_{mn}+b_{mn}
          \end{array} \right].
$$

If $A$ and $B$ are not of the same size their sum is not defined.

::::::

::::::{prf:example}

$$
  \begin{bmatrix} 1 & 3 \\ 5 & 2 \\ 6 & -4 \end{bmatrix} +
  \begin{bmatrix} 3 & 2 \\ 4 & -5 \\ 2 & 5  \end{bmatrix}  =
  \begin{bmatrix} 4 & 5 \\ 9 & -3 \\ 8 & 1  \end{bmatrix},
$$

$$
  \begin{bmatrix} 1 & 3 \\ 5 & 2 \\ 6 & -4 \end{bmatrix} +
  \begin{bmatrix} 0 & 0 \\ 0 & 0 \\ 0 & 0 \end{bmatrix}  =
  \begin{bmatrix} 0 & 0 \\ 0 & 0 \\ 0 & 0 \end{bmatrix} +
  \begin{bmatrix} 1 & 3 \\ 5 & 2 \\ 6 & -4 \end{bmatrix}  =
  \begin{bmatrix} 1 & 3 \\ 5 & 2 \\ 6 & -4  \end{bmatrix},
$$

$$
  \begin{array}{lcl}
  \begin{bmatrix} 1 & 3 & 5 \\  2 & 4 & 1 \end{bmatrix} +
  (-1)\begin{bmatrix}  1 & 3 & 5 \\   2 & 4 & 1  \end{bmatrix}  &=&
  \begin{bmatrix} 1 & 3 & 5 \\  2 & 4 & 1 \end{bmatrix} +
  \begin{bmatrix}  -1 & -3 &-5 \\  -2 & -4 & -1  \end{bmatrix} \\
  &=&  \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0  \end{bmatrix}.
  \end{array}
$$

::::::

The multiple $(-1)A$ is also written as $-A$. An obvious property, illustrated
in the third example, is:

$$
    A + (-A) = O,
$$

where $O$ is the zero matrix.

::::::{prf:example}

$$
  \begin{bmatrix} 1 & 3 \\ 5 & 2 \\ 6 & -4 \end{bmatrix}  +
  \begin{bmatrix} 1 & 3 & 5 \\  2 & 4 & 1 \end{bmatrix}
$$

is not defined. This is because the matrices do not have the same size.

::::::

::::::{prf:remark}
The two definitions of sum and scalar multiple are called **componentwise** definitions. They are completely analogous to the definitions of the scalar multiples of a vector and the sum of two vectors. Hence it is not surprising that they obey exactly the same rules, as is summarized in the next proposition. (cf. Section {ref}`Sec:Vectors`.)

::::::

::::::{prf:proposition}
Suppose $A, B$ and $C$ are $m\times n$ matrices and let $c_{1},c_{2}$ be two real numbers.
Then we have:

<ul>
<li>

$A+O_{mn}=A=O_{mn}+A$

</li>
<li>

$(A+B)+C=A+(B+C)$

</li>
<li>

$A+B=B+A$

</li>
<li>

$A+(-A)=O$

</li>
<li>

$1A=A$

</li>
<li>

$c_{1}(A+B)=c_{1}A+c_{1}B$

</li>
<li>

$(c_{1}+c_{2})A=c_{1}A+c_{2}A$

</li>
<li>

$c_{1}(c_{2}A)=(c_{1}c_{2})A$.

</li>
</ul>

::::::

An operator of which the usefulness is not immediately clear, but which fits well in this section with matrix operations, is the following:

::::::{prf:definition}
The **transpose** of an $m \times n$ matrix $A$ with entries $a_{ij}$ is the
$n \times m$ matrix $B$ with entries $b_{ij}$ defined by

$$
  b_{ij} = a_{ji}, \quad  i = 1,\ldots,n,\,\,j=1,\ldots, m
$$

It is denoted by $B = A^T$.

::::::

::::::{prf:example}

$$
  \begin{bmatrix} 1 & 3 \\ 5 & 2 \\ 6 & 4 \end{bmatrix}^T =
    \begin{bmatrix} 1 & 5 & 6 \\  3 & 2 & 4 \end{bmatrix}
    \quad
      \text{and}
    \quad
    \begin{bmatrix} -1 & 2 & -4  & 0\end{bmatrix}^T =
    \begin{bmatrix} -1 \\ 2 \\-4 \\  0\end{bmatrix}.
$$

::::::

The following rules involving the three operators defined so far in this section are easy to prove:

::::::{prf:proposition}
:label: Prop:MatrixOps:Transpose

Let $A$ and $B$ be $m\times n$ matrices and $c$ a scalar. Then we have

<ul>

<li>

$(cA)^T = c A^T$

</li>

<li>

$(A+B)^T = A^T  + B^T$

</li>
<li>

$(A^T)^T = A$.

</li>
</ul>

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:MatrixOps:Transpose`
:class: tudproof

We will prove the second statement and leave the other two to the diligent reader. See
{numref}`Exc:MatrixOps:CheckTransposeRules`.

So, suppose $A$ and $B$ are two $m \times n$ matrices.
Then $A+B$ is an $m \times n$ matrix too, hence $(A+B)^T$ is an $n \times m$ matrix. The matrix $A^T  + B^T$ on the right side of the equation is the sum of two $n \times m$ matrices, which is again an $n \times m$ matrix. So the matrices on both sides of the equation
have the same size.

Next we have to show that they have equal entries on the corresponding positions. If we put

$$
  E = (A+B)^T \quad \text{and}\quad F = A^T  + B^T
$$

we see that

$$
 e_{ij} = \text{  entry of  } (A+B) \,\text{  on position  }(j,i)
$$

and

$$
\begin{array}{rl}
 f_{ij} &= \text{  entry of  } A^T \,\text{  on position  }(i,j)\,+
        \text{  entry of  } B^T \,\text{  on position  }(i,j) \\
        &= \text{  entry of  } A \,\text{  on position  }(j,i)\,+
        \text{  entry of  } B \,\text{  on position  }(j,i)\\
        &= \text{  entry of  } (A+B) \,\text{  on position  }(j,i)\\
        &= \,\,\,\,e_{ij},
\end{array}
$$

so we are done.

If you are lost in the forest of indices, have a look at {prf:ref}`Ex:MatrixOps:SumTranspose`.

::::::

::::::{prf:example}
:label: Ex:MatrixOps:SumTranspose

We check property (ii) for two general $3\times 4$ matrices $A$ and $B$ on the position
$(2,3)$. Let

$$
  A = \begin{bmatrix} a_{11}& a_{12} & a_{13}  & a_{14} \\  a_{21}& a_{22} & a_{23} & a_{24} \\ a_{31} & \fbox{$a_{32}$} & a_{33} & a_{34}   \end{bmatrix} \quad \text{and} \quad
  B = \begin{bmatrix} b_{11}& b_{12} & b_{13}  & b_{14} \\  b_{21}& b_{22} & b_{23} & b_{24} \\ b_{31} & \fbox{$b_{32}$} & b_{33} & b_{34}  \end{bmatrix}.
$$

Then

$$
  E = (A+B)^T = \begin{bmatrix} a_{11}+b_{11}& a_{12}+b_{12} & a_{13}+b_{13}  & a_{14} +b_{14}\\  a_{21}+b_{21}& a_{22}+b_{22} & a_{23}+b_{23} & a_{24}+b_{24} \\ a_{31}+b_{31} & \fbox{$a_{32}+b_{32}$} & a_{33}+b_{33} & a_{34}+b_{34}   \end{bmatrix}^T
$$

so

$$
  E = \begin{bmatrix}
  a_{11}+b_{11}& a_{21}+b_{21} &  a_{31}+b_{31}  \\
  a_{12}+b_{12}& a_{22}+b_{22} & \fbox{$a_{32}+b_{32}$} \\
  a_{13}+b_{13}& a_{23}+b_{23} & a_{33}+b_{33} \\
  a_{14} +b_{14}& a_{24}+b_{24} & a_{34}+b_{34} \end{bmatrix},
$$

and on position $(2,3)$ we have <span style="border-style:solid; padding:4px; border-width:1px">$a_{32}+b_{32}$</span>.

On the other hand

$$
  F = A^T + B^T =
   \begin{bmatrix}
   a_{11}& a_{21} &  a_{31}  \\
 a_{12}& a_{22} & \fbox{$a_{32}$} \\
 a_{13}& a_{23} & a_{33}\\
 a_{14}& a_{24} & a_{34}\end{bmatrix} +
  \begin{bmatrix}
  b_{11}& b_{21} &  b_{31}  \\
  b_{12}& b_{22} & \fbox{$b_{32}$} \\
  b_{13}& b_{23} & b_{33}\\
  b_{14}& b_{24} & b_{34} \end{bmatrix},
$$

with on position $(2,3)$ the value <span style="border-style:solid; padding:4px; border-width:1px">$a_{32}$</span> + <span style="border-style:solid; padding:4px; border-width:1px">$b_{32}$</span>.

::::::

::::::{exercise}
:label: Exc:MatrixOps:CheckTransposeRules

Prove statements (i) and (iii) of {prf:ref}`Prop:MatrixOps:Transpose`.

::::::

::::::{admonition} Solution to&nbsp;{numref}`Exc:MatrixOps:CheckTransposeRules`
:class: solution, dropdown

Suppose $A = \left[\begin{array}{cccc}
            a_{11} & a_{12}&  \ldots&   a_{1n}   \\
            a_{21} & a_{22}&  \ldots&   a_{2n}   \\
            \vdots &  \vdots&  \cdots&  \vdots    \\
            a_{m1} & a_{m2}&  \ldots&   a_{mn}    
          \end{array}
   \right]$ is an arbitrary $m \times n$ matrix. Then

$$
  \begin{array}{rcl}
  (cA)^T &=&  \left[\begin{array}{cccc}
            ca_{11} & ca_{12}&  \ldots& ca_{1n}   \\
            ca_{21} & ca_{22}&  \ldots& ca_{2n}   \\
            \vdots &  \vdots&  \cdots&  \vdots    \\
            ca_{m1} & ca_{m2}&  \ldots& ca_{mn}
          \end{array}^T
   \right] =
   \left[\begin{array}{cccc}
            ca_{11} & ca_{21}&  \ldots& ca_{m1}   \\
            ca_{12} & ca_{22}&  \ldots& ca_{m2}   \\
            \vdots &  \vdots&  \cdots&  \vdots    \\
            ca_{1n} & ca_{2n}&  \ldots& ca_{mn}
          \end{array}
   \right] \\
   &=&
   c \left[\begin{array}{cccc}
            a_{11} & a_{21}&  \ldots& a_{m1}   \\
            a_{12} & a_{22}&  \ldots& a_{m2}   \\
            \vdots &  \vdots&  \cdots&  \vdots    \\
            a_{1n} & a_{2n}&  \ldots& a_{mn}
          \end{array}
   \right]  = c\,A^T
   \end{array}
$$

::::::

::::::{prf:example}

We will solve the equation $A + 2X^T + B = C$ for $X$, where

$$
    A = \begin{bmatrix} 1 & 1 & 2 \\  3 & 1 & 0 \end{bmatrix}, \quad
    B = \begin{bmatrix} 2 & 0 & 3 \\  2 & 3 & 4 \end{bmatrix}, \text{  and} \quad
    C = \begin{bmatrix} 7 & 5 & 1 \\  1 & 4 & 2 \end{bmatrix}.
$$

We will extricate $X$ step by step:

$$
  A + 2X^T + B = C \,\, \iff \,\,2X^T = C-A-B \,\, \iff \,\, X^T = \tfrac12(C-A-B).
$$

Next we transpose both terms to find

$$
  X = \tfrac12(C-A-B)^T = \frac12\begin{bmatrix} 4 & 4 & -4 \\  -4 & 0 & -2 \end{bmatrix}^T
  = \begin{bmatrix} 2 & -2 \\ 2 & 0 \\  -2  & -1 \end{bmatrix}.
$$


::::::

## Grasple exercises

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bc898154-3f5e-45bd-8993-28a74bf34b5f?id=70278
:label: grasple_exercise_3_2_1
:dropdown:
:description: To compute the sum of two matrices.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bf170c2b-127b-4ce7-bd75-c9c9bdfb12f9?id=70277
:label: grasple_exercise_3_2_2
:dropdown:
:description: To compute $c_1A + c_2B$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/dd83bd83-0ce4-4dd7-84de-3472c24acbc0?id=70279
:label: grasple_exercise_3_2_3
:dropdown:
:description: To compute $c_1A + c_2B$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3e5f0674-1e9f-4349-867f-6b1d638e744b?id=82934
:label: grasple_exercise_3_2_4
:dropdown:
:description: To solve equations involving sum and transpose.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/52a8c0e8-09e8-4c46-aa43-0cee2a93e7c4?id=82931
:label: grasple_exercise_3_2_5
:dropdown:
:description: True/False questions involving sum and transpose.

::::::

(Subsec:DefMatrixProd)=

## The product of two matrices

Next we turn our attention to the most important matrix operation, namely the product $AB$ of two matrices. In the previous chapter we have already seen the special case where $B$ is a matrix of just one column, i.e.,

$$
  B = \mathbf{x} = \begin{bmatrix}x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix},
$$

a vector in $\mathbb{R}^n$, which we can identify with an $n \times 1$ matrix. We want of course the definition of the general matrix product to be consistent with this.

::::::{prf:definition}
The product of an $m\times n$ matrix $A$ and an $n\times p$ matrix $B = [\,{\vect{b}_1}\quad {\vect{b}_2}\quad \ldots \quad {\mathbf{b}_p}]$ is defined by

$$
  AB = [\,A\mathbf{b}_1\quad A\mathbf{b}_2\quad \ldots \quad A\mathbf{b}_p].
$$

So we have

$$
  j\text{-th column of  } AB = A\text{ times  $j$-th column of  } B, \quad  j = 1,2,\ldots,p.
$$

Note that this makes $AB$ an $m \times p$ matrix.

If the number of columns of $A$ is not equal to the number of rows of $B$ the product $AB$ is not defined.

::::::

::::::{prf:example}

$$
  \begin{bmatrix} 1 & -3 \\ -1 & 2 \\ 3& -2 \end{bmatrix}
  \begin{bmatrix} 2 & 1 & 1\\ 3 & 0 & 2 \end{bmatrix} =
  \begin{bmatrix} -7 & 1 & -5 \\ 4 & -1 & 3 \\ 0 & 3 &-1 \end{bmatrix}.
$$

For instance, the third column is computed as

$$
  \begin{bmatrix} 1 & -3 \\ -1 & 2 \\ 3& -2 \end{bmatrix} \begin{bmatrix} 1\\  2 \end{bmatrix}
  = 1\begin{bmatrix} 1  \\ -1  \\ 3\end{bmatrix} +
  2\begin{bmatrix}  -3 \\ 2 \\  -2 \end{bmatrix} \,\,=\, \begin{bmatrix} -5  \\ 3  \\ -1\end{bmatrix}.
$$

::::::

::::::{prf:proposition}
:label: Prop:MatrixOps:RowColExpansion

The product of the $m\times n$ matrix $A$ and the $n\times p$ matrix $B$ is the $m\times p$ matrix $C$ for which the entry on the position $(i,j)$ is given by

$$
   c_{ij} = a_{i1}b_{1j} + a_{i2}b_{2j} + \ldots + a_{in}b_{nj} =
      \begin{bmatrix}a_{i1} & a_{i2} & \ldots & a_{in} \end{bmatrix} \begin{bmatrix}  b_{1j} \\ b_{2j} \\ \vdots \\ b_{nj}\end{bmatrix}.
$$

This is sometimes called the **row-column expansion** of the product.

::::::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:MatrixOps:RowColExpansion`
:class: tudproof

We already saw this row-column expansion in {numref}`Sec:MatVecProduct`.

::::::

The following scheme nicely visualizes the row-column expansion

$$
   \begin{array}{ccc}
        &
        \begin{bmatrix}
            b_{11} & b_{12}&  \ldots& \class{red}{b_{1j}} & \ldots&  b_{1p} \\
            b_{21} & b_{22}&  \ldots&  \class{red}{b_{2j}} & \ldots&  b_{2p} \\
            \vdots &  \vdots&  \cdots&  & \ldots& \vdots    \\
            b_{n1} & b_{n2}&  \ldots&  \class{red}{b_{nj}} &  \ldots& b_{np}
          \end{bmatrix} \\
    \begin{bmatrix}
            a_{11} & a_{12}&  \ldots& \ldots&  a_{1n} \\
            a_{21} & a_{22}&  \ldots& \ldots&  a_{2n} \\
            \cdots &  \ddots&  \cdots& \cdots& \vdots    \\
              \class{red}{a_{i1}} &  \class{red}{a_{i2}}&   \class{red}{\ldots}&
              \class{red}{\ldots}&   \class{red}{a_{in}} \\
            \vdots &  \vdots&  \cdots& \cdots& \vdots    \\
            a_{m1} & a_{m2}&  \ldots&  \ldots& a_{mn}
    \end{bmatrix} \!\! &  \!
    \begin{bmatrix}
            c_{11} & c_{12}&  \ldots& c_{1j} &\ldots&  c_{1p} \\
            c_{21} & c_{22}&  \ldots&  c_{2j} &\ldots&  c_{2p} \\
            \vdots &  \vdots&  \cdots& & \cdots& \vdots    \\
             c_{i1} &  c_{i2}&  \cdots&\class{red}{c_{ij}} &\ldots&   c_{ip} \\
            \vdots &  \vdots&  \cdots& &\cdots& \vdots    \\
            c_{m1} & c_{m2}&  \ldots&  c_{mj} &\ldots& c_{mp}
    \end{bmatrix}
  \end{array}


$$

%As the scheme makes clear in a graphical way the $i$-th row of $AB$ only depends on the $i$-th row
%of $A$ and the $j$-th column of the product only depends on the $j$-th column
%of $B$. The last is of course part of the definition.\\

::::::{prf:example}
Let us consider the matrix product

$$
  \begin{bmatrix} 1 & -3 \\ -1 & 2 \\ 3& -2 \end{bmatrix}
  \begin{bmatrix} 2 & 1 & 1\\ 3 & 0 & 2 \end{bmatrix} =
  \begin{bmatrix} -7 & 1 & -5 \\ 4 & -1 & 3 \\ 0 & 3 &-1 \end{bmatrix}.
$$

The $-5$ on position $(1,3)$ and the $3$ on position $(3,2)$ in the product come from

$$
  -5 = \begin{bmatrix} 1 & -3 \end{bmatrix} \begin{bmatrix} 1\\  2 \end{bmatrix}
  \quad \text{and} \quad
  3 =  \begin{bmatrix} 3 & -2 \end{bmatrix} \begin{bmatrix} 1\\  0 \end{bmatrix}.
$$

::::::

::::::{exercise}
:label: Exc:MatrixOps:NonDefinedProduct

Explain why the product

$$
  \begin{bmatrix} 1 & -3 \\ -1 & 2 \\ 3& -2 \end{bmatrix}\begin{bmatrix} 1 & -3 \\ -1 & 2 \\ 3& -2 \end{bmatrix}
$$

is not defined.

::::::

::::::{prf:remark}
The product of a matrix $A$ with itself is only defined if $A$ is an $n \times n$ matrix. In that case we use the obvious notation

$$
   A^2 = A\cdot A.
$$

::::::

::::::{prf:example}
:label: Ex:MatrixOps:AtimesI

$$
\begin{bmatrix} a_{11}& a_{12} & a_{13} \\  a_{21}& a_{22} & a_{23} \\ a_{31}& a_{32} & a_{33} \\ a_{41} & a_{42} & a_{43}   \end{bmatrix}
   \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 &  0\\ 0 & 0 & 1 \end{bmatrix}
   = \begin{bmatrix} a_{11}& a_{12} & a_{13} \\  a_{21}& a_{22} & a_{23} \\ a_{31}& a_{32} & a_{33} \\ a_{41} & a_{42} & a_{43}   \end{bmatrix}.
$$

::::::

This example illustrates the existence of a _unit element_ with respect to the multiplication. To identify it we first introduce some more terminology.

::::::{prf:definition}
:label: Def:MatrixOps:MainDiagonal

An $n\times n $ matrix $A$ is called a **square matrix**. So it is a matrix where the number of columns is equal to the number of rows.

For a square matrix $A$ we call the elements $a_{ii}$ the **diagonal elements**. Together the diagonal elements form the **(main) diagonal** of $A$.

A square matrix where all non-diagonal elements are equal to 0 is called a **diagonal matrix**.

::::::

::::::{prf:remark}
The other diagonal of a square matrix, the one from bottom left to top right, plays a minor role. For this reason we don't reserve a name for it. By 'diagonal' we will always mean: main diagonal.

::::::

::::::{prf:example}
Consider the matrices

$$
   A = \begin{bmatrix} 2 & 2 \\ 3 & 3 \end{bmatrix}, \quad
   B = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 6 \end{bmatrix}, \quad
   C = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix}.
$$

The matrices $A$ and $B$ are square, and only $B$ is a diagonal matrix.

::::::

::::::{exercise}
:label: Exc:MatrixOps:ZeroMatrixIsDiagonal

Is the following statement true or false?

The $n \times n$ zero matrix $O_{nn}$ is a diagonal matrix.

::::::

::::::{exercise}
:label: Exc:MatrixOps:InterpretATB

Suppose $A = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \ldots & \mathbf{a}_n \end{bmatrix} $ is an  $m\times n$ matrix and <br/>
$B= \begin{bmatrix} \mathbf{b}_1 & \mathbf{b}_2 & \ldots & \mathbf{b}_p \end{bmatrix} $  an  $n\times p$ matrix. Show that

$$
  A^TB = %\begin{bmatrix} \vect{a_1}^T \vect{b_1}  & \vect{a_1}^T \vect{b_2} & \ldots &  \vect{a_1}^T \vect{b_p} \\
         %                \vect{a_2}^T \vect{b_1}  & \vect{a_2}^T \vect{b_2} & \ldots &  \vect{a_2}^T \vect{b_p} \\
         %                     \vdots              &            \vdots       &        &        \vdots \\
         %                \vect{a_n}^T \vect{b_1}  & \vect{a_n}^T \vect{b_2} & \ldots &  \vect{a_n}^T \vect{b_p} \\
         %\end{bmatrix}
         %    =
         \begin{bmatrix} \mathbf{a}_1\ip \mathbf{b}_1  & \mathbf{a}_1\ip\mathbf{b}_2 & \ldots &  \mathbf{a}_1\ip \mathbf{b}_p \\
                         \mathbf{a}_2\ip \mathbf{b}_1  & \mathbf{a}_2\ip\mathbf{b}_2 & \ldots &  \mathbf{a}_2\ip \mathbf{b}_p \\
                              \vdots              &            \vdots       &        &        \vdots \\
                         \mathbf{a}_n\ip \mathbf{b}_1  & \mathbf{a}_n\ip\mathbf{b}_2 & \ldots &  \mathbf{a}_n\ip \mathbf{b}_p \\ 
         \end{bmatrix},


$$

where $\mathbf{a}\ip\mathbf{b}$ is the dot product of the vectors $\mathbf{a}$ and $\mathbf{b}$.

::::::

::::::{exercise}
:label: Exc:MatrixOps:InterpretATA

The special case in the previous exercise where $A = B$ will become very important when we will look at orthogonal projections.
For now, show that the columns of a matrix $A$ are orthogonal if and only if the
matrix $A^TA$ is a diagonal matrix.

::::::

::::::{prf:definition}
The **identity matrix** $I_n$ is the $n \times n$ diagonal matrix with 1's on the diagonal. If the size is irrelevant or clear from the context, we denote it simply by $I$.

::::::

::::::{exercise}
:label: Exc:MatrixOps:I4timesA

Let

$$
   I = I_4 = \begin{bmatrix}1 & 0 & 0 & 0 \\
                            0 & 1 & 0 & 0 \\
                            0 & 0 & 1 & 0 \\
                            0 & 0 & 0 & 1
            \end{bmatrix}
            \quad \text{and} \quad
   A = \begin{bmatrix} a_{11}& a_{12} & a_{13} \\  a_{21}& a_{22} & a_{23} \\ a_{31}& a_{32} & a_{33} \\ a_{41} & a_{42} & a_{43}   \end{bmatrix}.
$$

Show that $IA = A$.

::::::

The definition of the product of two matrices and the earlier definition of the product of a matrix and a vector ({prf:ref}`Dfn:MatVectProd:ProductMatVec`) immediately imply that the columns of the product of two matrices are linear combinations of the columns of the first matrix.  
As is often the case in linear algebra things can be looked at from a different perspective. From {prf:ref}`Prop:MatrixOps:RowColExpansion`
it follows that the elements $c_{i1},c_{i2},\ldots,c_{in}$ of the $i$-th row of the product $C = AB$ as far as $A$ is concerned only depend on the elements $a_{ik}$ of its $i$-th row. The following proposition explains in which way.

::::::{prf:proposition}
:label: Prop:MatrixOps:ProductRowCombinations

The $i$-th row of the product $AB$ is the linear combination of the rows of the second matrix, $B$, with the entries of the $i$-th row of $A$ as coefficients.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:MatrixOps:ProductRowCombinations`
:class: tudproof

The indicated linear combination yields:

$$
  a_{i1} \begin{bmatrix}b_{11} & b_{12} & \ldots &b_{1p}  \end{bmatrix}  +
   a_{i2} \begin{bmatrix}b_{21} & b_{22} & \,\, \ldots \,\, &b_{2p}  \end{bmatrix} + \ldots +
   a_{in} \begin{bmatrix}b_{n1} & b_{n2} & \ldots &b_{np}  \end{bmatrix}
$$

$$
  =  \begin{bmatrix} (a_{i1}b_{11} + a_{i2}b_{21}+ \ldots +a_{in}b_{n1})  & \quad\ldots\quad & (a_{i1}b_{1p} + a_{i2} b_{2p} + \ldots + a_{in}b_{np})  \end{bmatrix}.
$$

This is a row vector with on the $j$-th position the number

$$
  (a_{i1}b_{1j} + a_{i2} b_{2j} + \ldots + a_{in}b_{nj}),
$$

and that is precisely the entry $c_{ij}$ of the matrix $C = AB$.

::::::

Interestingly this opens the way to describe the row operations of Chapter 2 via matrix multiplication. The following example illustrates this for the three basic row operations.

::::::{prf:example}
The following multiplication adds the first row of the matrix

$$
 A =   \begin{bmatrix} a_{11}& a_{12} & a_{13} \\  a_{21}& a_{22} & a_{23} \\ a_{31}& a_{32} & a_{33}   \end{bmatrix}
$$

four times to the second row:

$$
  \begin{bmatrix} 1 & 0 & 0 \\ 4 & 1 & 0 \\ 0 & 0 & 1\end{bmatrix}
  \begin{bmatrix} a_{11}& a_{12} & a_{13} \\  a_{21}& a_{22} & a_{23} \\ a_{31}& a_{32} & a_{33}  \\ \end{bmatrix}
  = \begin{bmatrix} a_{11}& a_{12} & a_{13} \\  4a_{11}+a_{21}&4a_{12} +a_{22}& 4a_{13}+a_{23}  \\ a_{31}& a_{32} & a_{33} \\ \end{bmatrix}.
$$

Here the third row is scaled with a factor 5:

$$
  \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 5\end{bmatrix}
  \begin{bmatrix} a_{11}& a_{12} & a_{13} \\  a_{21}& a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33}   \end{bmatrix}
  =  \begin{bmatrix} a_{11}& a_{12} & a_{13} \\  a_{21}& a_{22} & a_{23} \\ 5a_{31}& 5a_{32} & 5a_{33} \\ \end{bmatrix}.
$$

And with the following multiplication the first and third row of $A$ are swapped:

$$
  \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0\end{bmatrix}
  \begin{bmatrix} a_{11}& a_{12} & a_{13} \\  a_{21}& a_{22} & a_{23} \\ a_{31}& a_{32} & a_{33}   \end{bmatrix}
  =  \begin{bmatrix}a_{31}& a_{32} & a_{33}  \\  a_{21}& a_{22} & a_{23} \\ a_{11}& a_{12} & a_{13} \end{bmatrix}.
$$

::::::

For future reference we give these matrices a name:

::::::{prf:definition}
:label: Dfn:MatrixOps:ElementaryMatrix

The matrices $E$ that perform one single row operation (row replacement, row scaling, or row exchange) via $A \mapsto EA$ are called **elementary matrices**.

::::::

::::::{exercise}
:label: Exc:MatrixOps:RowOpsByElMatrices

Describe in words which row operations are the effect of pre-multiplying a $4\times n$ matrix $A$ with the following elementary matrices:

$$
  E_1 = \begin{bmatrix} 1 & 0 & 0 &  0\\
                  0 & 1 & 0 & -1\\
                  0 & 0 & 1 &  0\\
                  0 & 0 & 0 &  1
    \end{bmatrix},  \quad \quad
    E_2 = \begin{bmatrix} 1 & 0 & 0 &  0\\
                    0 & 0 & 0 &  1\\
                    0 & 0 & 1 &  0\\
                    0 & 1 & 0 &  0
    \end{bmatrix}.
$$

::::::

::::::{prf:example}
:label: Ex:MatrixOps:Product:ColumnRow

The following product may at first sight seem a bit odd, but it is exactly according to the definition:

$$
  \begin{bmatrix} 1 \\-2\\3\\4 \end{bmatrix}\begin{bmatrix} 2&4&0& -1   \end{bmatrix} =
   \begin{bmatrix}     2 &  4 & 0 & -1  \\
                      -4 & -8 & 0 &  2  \\
                       6 & 12 & 0 & -3  \\
                       8 & 16 & 0 & -4 \end{bmatrix}.
$$

::::::

The column-row product in the last example is the building block for yet another way to look at the matrix product. The next exercise explains how.

::::::{exercise}
:label: Exc:MatrixOps:ColumnRowExpansion

Column-row expansion of the product.

Denote the columns of the $m\times n$ matrix $A$ by $A_{(1)}, \ldots, A_{(n)}$, and the
rows of the $n\times p$ matrix $B$ by $B^{(1)}, \ldots, B^{(p)}$, so

$$
  A_{(j)} =   \begin{bmatrix}   a_{1j} \\ \vdots \\ a_{mj}\end{bmatrix}  \quad \text{and} \quad
  B^{(i)} =   \begin{bmatrix}   b_{i1} & b_{i2} & \ldots & b_{ip}\end{bmatrix}.
$$

Show that

$$
 AB = A_{(1)} B^{(1)}  +  A_{(2)} B^{(2)}  + \ldots + A_{(n)} B^{(n)},
$$

i.e., $AB$ is the sum of $n$ column-row products (like in {prf:ref}`Ex:MatrixOps:Product:ColumnRow`).

::::::

(Subsec:ProductProps)=

## Properties of the matrix product

Now let us have a look which of the rules of the products of numbers also hold for products of matrices. And which do not.

::::::{prf:proposition}
:label: Prop:MatrixOps:ProdProperties

For all $m \times n$ matrices $A,A_1,A_2$, all $n \times p$ matrices $B,B_1,B_2$,
all $p \times q$ matrices $C$ and all real numbers $c$ the following are true:

<ol type = "i">
<li>

$A(B_1+B_2) = AB_1 + AB_2$ and $(A_1+A_2)B = A_1B+A_2B$;

</li>
<li>

$A(cB) = c(AB) = (cA)B$;

</li>
<li>

$AI_n = A$ and $I_mA = A$ (the identity matrix $I$ acts as a **unit element**);

</li>
<li>

$A(BC) = (AB)C$.

</li>
</ol>

::::::

::::::{prf:example}
As an illustration of rule iv. we compute the two triple products for the three matrices

$$
  A = \begin{bmatrix} 3 & 1 \\
                      2 & 1 \\
                      0 & 5
        \end{bmatrix}, \quad
    B = \begin{bmatrix}  1 & 2 \\
                         3 & 0
        \end{bmatrix}, \quad
      C = \begin{bmatrix} 1 & 2 & 0 \\
                          2 & 1  & 2
           \end{bmatrix}.
$$

On the one hand

$$
 A(BC) =   \begin{bmatrix} 3 & 1 \\
                           2 & 1 \\
                           0 & 5
           \end{bmatrix}
           \begin{bmatrix} 5 & 4 & 4\\
                           3 & 6 & 0
            \end{bmatrix} =
            \begin{bmatrix} 18 & 18 & 12\\
                            13 & 14 & 8 \\
                            15 & 30 & 0
            \end{bmatrix},
$$

and on the other hand

$$
 (AB)C =   \begin{bmatrix} 6 & 6 \\
                           5 & 4 \\
                          15 & 0
           \end{bmatrix}
           \begin{bmatrix} 1 & 2 & 0 \\
                           2 & 1 & 2
           \end{bmatrix} =
           \begin{bmatrix} 18 & 18 & 12 \\
                           13 & 14 & 8  \\
                           15 & 30 & 0
           \end{bmatrix}.
$$

So the products are indeed equal. But it is not immediately clear how. For instance, the value 14 on position (2,2) comes about in two ways

$$
 \text{via  } A(BC)\!:  \,14 = 2\cdot4 + 1\cdot 6, \quad \,\, \text{via  } (AB)C\!:  \,14 = 5\cdot2 + 4\cdot1.
$$

We need a good perspective to give a proof of the general case.

::::::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:MatrixOps:ProdProperties`
:class: tudproof

Rules i. and ii. are checked in a straightforward way. See {numref}`Exc:MatrixOps:RulesProduct`.

<ol type = "i"  start = "3">

<li>

We saw instances of this property already in {prf:ref}`Ex:MatrixOps:AtimesI` and {numref}`Exc:MatrixOps:I4timesA`.
For the general case, one way to show validity of the first statement is to note that the $j$-th column of $AI_n$ is $A\mathbf{e}_j$ where $\mathbf{e}_j$ is the $j$-th column of the identity matrix $I_n$.
This gives the linear combination

<BR>

$$
 A\mathbf{e}_j =  0\mathbf{a}_1 + 0\mathbf{a}_2 + \ldots + 1\mathbf{a}_j +\dots + 0\mathbf{a}_n = \mathbf{a}_j
$$

which shows that the $j$-th column of $AI_n$ is equal to the $j$-th column of $A$. And this holds for any column.

The identity $\quad I_mA = A\quad$ is shown in an analogous way, working row by row.

</li>

<li>

First we observe that both triple products yield $m \times q$ matrices.
Then the identity can be proved 'column by column', as the previous one.

We are done if we can show that

<BR>

$$
 \begin{array}{rcl}
 k\text{-th column of  }A(BC) &=&  k\text{-th column of  }(AB)C \\
    &=&  (AB)( k\text{-th column of  }C) = (AB)\mathbf{c}_k,
 \end{array}
$$

for $ k = 1,2,\ldots q $.

Now recall that (by definition)

<BR>

$$
    k\text{-th column of  }BC = B\vect{c}_k,
$$

so

$$
 k\text{-th column of  }A(BC) = A\,(B\vect{c}_k)
$$

Making extensive use of the rule

<BR>

$$
  A(c_1\mathbf{x} + c_2\mathbf{y}) = c_1A\mathbf{x} + c_2A\mathbf{y}
$$

we find

$$
 \begin{array}{ccl}
     A\,(B\mathbf{c_k}) & = & A \,(c_{1k}\mathbf{b}_1 +c_{2k}\mathbf{b}_2   + \ldots + c_{pk}\mathbf{b}_p)\\
      & = & c_{1k}(A\mathbf{b}_1) +c_{2k}(A\mathbf{b}_2)   + \ldots + c_{pk}(A\mathbf{b}_p)\\
      & = & \begin{bmatrix} A\mathbf{b}_1 & A\mathbf{b}_2 & \ldots & A\mathbf{b}_p \end{bmatrix} \begin{bmatrix} c_{1k} \\ \vdots \\ c_{pk} \end{bmatrix} \\
      & = & (AB)\mathbf{c}_k.
 \end{array}
$$

</li>
</ol>

::::::

::::::{exercise}
:label: Exc:MatrixOps:RulesProduct

Prove rules i. and ii. of {prf:ref}`Prop:MatrixOps:ProdProperties`.

Recall that matrices are equal when they have the same size and the entries
on corresponding positions are equal (which may be checked column by column or row by row).

::::::

::::::{prf:remark}
:label: Rem:MatrixOps:ProdTransformation

The proof of {prf:ref}`Prop:MatrixOps:ProdProperties` iv. can be seen in another light. In the Section {ref}`Sec:LinTrafo` we saw that an $m\times n$ matrix $A$ defines a transformation $T$ from $\mathbb{R}^n$ to
$\mathbb{R}^m$, namely

$$
  \text{for  } \mathbf{x} \in \mathbb{R}^n: \quad \mathbf{x} \mapsto T(\mathbf{x}) = A\mathbf{x}.
$$

The definition of the product of two matrices then precisely matches the composition of two of such transformations:
if $A$ is an $m\times n$ matrix and $B$ is an $n\times p$ matrix

$$
  \mathbf{x}\in\mathbb{R}^p \,\,\stackrel{B}{\longrightarrow}\,\, \vect{y}_1 = B\vect{x}\in\mathbb{R}^n \,\, \stackrel{A}{\longrightarrow} \,\,\, \vect{y}_2 = A(B\mathbf{x}) \in \mathbb{R}^m\,
$$

and

$$
  \mathbf{x}\in\mathbb{R}^p\,\,\,\stackrel{AB}{\longrightarrow} \,\,\,\vect{y}_3 \,=\, (AB)\mathbf{x} \in \mathbb{R}^m
$$

yield the same vector:

$$
\vect{y}_2 = \vect{y}_3.
$$

%

::::::

So far so good: matrix multiplication behaves as multiplication of numbers.
However, in two important respects the concepts deviate.
First of all, commutativity no longer holds.

::::::{prf:example}
For the matrices

$$
A = \begin{bmatrix} 2 & 2 & 1\\ 3 & 3 & 0 \end{bmatrix} \quad \text{and} \quad
   B = \begin{bmatrix} 1 & 3 \\ 3 & 1 \\ 4 & 0 \end{bmatrix}
$$

it is clear that

$$

  AB \neq BA,


$$

simply because the two products are not of the same size: $AB$ is a $2\times 2$ matrix, $BA$ a $3\times3$ matrix.

The following example illustrates that $AB = BA$ is not even guaranteed for two $n\times n$ matrices $A$ and $B$:

$$
 \begin{bmatrix} 1 & 3 \\ 2 & 1  \end{bmatrix}
 \begin{bmatrix} 0 & 1 \\ 1 & 2  \end{bmatrix} =
 \begin{bmatrix} 3 & 7 \\ 1 & 4  \end{bmatrix} \neq
 \begin{bmatrix} 2 & 1 \\ 5 & 5  \end{bmatrix} =
  \begin{bmatrix} 0 & 1 \\ 1 & 2  \end{bmatrix}
  \begin{bmatrix} 1 & 3 \\ 2 & 1  \end{bmatrix}.
$$

::::::

The fact that $AB \neq BA$ can be understood by thinking about the composition of the two transformations corresponding to $A$ and $B$.
(See Section {ref}`Sec:LinTrafo`.)

The following two exercises shed some light on the non-commutativity.

::::::{prf:example}
:label: Ex:MatrixOps:NonCommutativeComposition

Consider the two matrices

$$
  A = \begin{bmatrix} 2 & 0 \\ 0 & 1  \end{bmatrix} \quad \text{and} \quad
  B =  \begin{bmatrix} 0 & 1 \\ 1 & 0  \end{bmatrix}
$$

and the corresponding linear transformations

$$
   T_A: \mathbb{R}^2 \to \mathbb{R}^2, \quad \mathbf{x} \mapsto T_A(\mathbf{x}) = A \mathbf{x}
$$

and

$$
T_B: \mathbb{R}^2 \to \mathbb{R}^2, \quad \mathbf{x} \mapsto T_B(\mathbf{x}) = B \mathbf{x}.
$$

We get

$$
   \mathbf{x} = \begin{bmatrix} x_1\\ x_2  \end{bmatrix} \quad \mapsto \quad A\mathbf{x} = \begin{bmatrix} 2 & 0 \\ 0 & 1  \end{bmatrix} \begin{bmatrix} x_1\\ x_2  \end{bmatrix}  \,\, = \,\,
   \begin{bmatrix} 2x_1\\ x_2  \end{bmatrix}
$$

and likewise

$$
  T_B(\mathbf{x}) =  \begin{bmatrix} 0 & 1 \\ 1 & 0  \end{bmatrix} \begin{bmatrix} x_1\\ x_2  \end{bmatrix}
   = \begin{bmatrix} x_2\\ x_1  \end{bmatrix}.
$$

::::{figure} Images/Fig-MatrixOps-NonCommutativity.svg
:name: Fig:MatrixOps:NonCommutativity
:class: dark-light

$ \begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} 0 & 1 \\ 1&0 \end{bmatrix} \neq \begin{bmatrix} 0 & 1 \\ 1&0 \end{bmatrix}\begin{bmatrix} 2 & 0 \\ 0 & 1 \end{bmatrix}$.
::::

Note that $T_A$ is a transformation that 'stretches' horizontally, and $T_B$ is a reflection. {numref}`Figure %s <Fig:MatrixOps:NonCommutativity>` visualizes the transformations corresponding to $AB$ and $BA$. When we apply the transformations one after another, the order in which we do this is important.

::::::

::::::{exercise}
:label: Exc:MatrixOps:NonCommutativeRowOps

Another way to understand why $AB\neq BA$ is the following.

Recall that the matrices

$$
   E_1 =  \begin{bmatrix} 1 & 0 \\ 2 & 1  \end{bmatrix} \quad \text{and} \quad
   E_2 =  \begin{bmatrix} 3 & 0 \\ 0 & 1  \end{bmatrix}
$$

perform row operations, when multiplied with a $2 \times n$ matrix $A$.

<ul>
<li>

Describe in words the row operations corresponding to $E_1$ and $E_2$.

</li>
<li>

Describe in words the combined row operations corresponding to $E_1E_2$ and $E_2E_1$. Can you explain why $E_1E_2 \neq E_2E_1$?

</li>
<li>

Compute $E_1E_2$ and $E_2E_1$ to double check the last non-identity.

</li>
</ul>

::::::

The second major difference between the product of numbers and the product of matrices: for two (e.g. real) numbers $a$ and $b$ it is known that

$$
\text{if} \quad a \neq 0 \quad  \text{and}  \quad b \neq 0\quad  \text{then}  \quad ab \neq 0,
$$

or, equivalently,

$$
\text{if} \quad ab = 0 \quad  \text{then}  \quad  a = 0 \,\,\text{  or  } \,\,b = 0.
$$

As the following example shows, things are different in the realm of matrices.

::::::{prf:example}

$$
\begin{bmatrix} 1 & 2 \\ 2 & 4  \end{bmatrix}
    \begin{bmatrix} 2 & 6 \\ -1 & -3  \end{bmatrix} =
      \begin{bmatrix} 0 & 0 \\ 0 & 0  \end{bmatrix}.
$$

So the product of two nonzero matrices may be the zero matrix.

::::::

The following example shows that things are even 'worse':

::::::{prf:example}

$$
  \begin{bmatrix} 1 & -3 & 2 \\ 1 & -3 & 2 \\ 1 & -3 & 2  \end{bmatrix}
  \begin{bmatrix}1 & -3 & 2 \\ 1 & -3 & 2 \\ 1 & -3 & 2  \end{bmatrix} =
  \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix},
$$

which shows that we cannot even conclude from $A\cdot A = O$ that $A$ itself must be the zero matrix.

::::::

And here is another example of a nonzero matrix whose square is the zero matrix. In this case it can be seen geometrically what is going on.

::::::{prf:example}

For the matrix $A = \begin{bmatrix} 0 & 1 \\ 0 & 0  \end{bmatrix}$ we again have that

$$
A^2 = \begin{bmatrix} 0 & 1 \\ 0 & 0  \end{bmatrix}^2 = \begin{bmatrix} 0 & 0 \\ 0 & 0  \end{bmatrix}.
$$

It holds that

$$
A = A_2A_1  = \begin{bmatrix} 0 & 1 \\ -1 & 0  \end{bmatrix}\begin{bmatrix} 0 & 0 \\ 0 & 1  \end{bmatrix}
$$

Now consider the transformations corresponding to the matrices
$A_1$ and $A_2$.

$$
T_1(\vect{x}) = A_1\vect{x} = \begin{bmatrix} 0 & 0 \\ 0 & 1  \end{bmatrix}\begin{bmatrix} x_1 \\ x_2  \end{bmatrix} = \begin{bmatrix} 0\\ x_2 \end{bmatrix}
$$

is the projection onto the $x_2$-axis, and

$$
T_2(\vect{x}) = A_2\vect{x} = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2  \end{bmatrix} = \begin{bmatrix} x_2\\ -x_1 \end{bmatrix}
$$

is the clockwise rotation about an angle $\frac12\pi$.

Now let us see, step by step, what is the effect of the transformation $T_2T_1T_2T_1$, corresponding to $A^2$.

An arbitrary vector $\vect{x}$ is sent to a vector $T_1(\vect{x})$ on the $x_2$ axis by $T_1$.

The rotation sends this to a vector $T_2(T_1(\vect{x}))$ on the $x_1$-axis. Projecting onto the $x_2$-axis again, will bring this to $T_1(T_2(T_1(\vect{x}))) = \vect{0}$.  
Lastly, applying $T_2$ leaves the zero vector where it is.

So $A^2\vect{x} = T_2(T_1(T_2(T_1(\vect{x})))) = \vect{0}$, for each vector $\vect{x}$.

See {numref}`Figure %s <Fig:MatrixOps:NilPotent>`.

```{applet}
:url: matrix_operations/nilpotent
:fig: Images/Fig-MatrixOps-Nilpotent.svg
:name: Fig:MatrixOps:Nilpotent
:class: dark-light

Visualisation of $\vect{x} \mapsto A^2\vect{x}$.
```

::::::

::::::{prf:remark}
The next list gives six situations where matrix multiplication acts differently than multiplication of numbers.  
In fact, all statements can be related to one of the first two.

<ol>
<li>

In general, $AB = BA$ **does not hold** for two $n\times n$ matrices $A$ and $B$.

</li>
<li>

In general, from $AB = O$ it **does not follow** that either $A =O$ or $B = O$.

</li>
<li>

In general, $(A+B)(A+B) = A^2 + 2AB + B^2$ **does not hold** for two $n\times n$ matrices $A$ and $B$.

</li>
<li>

In general, $(A+B)(A-B) = A^2 - B^2$ **does not hold** for two $n\times n$ matrices $A$ and $B$.

</li>
<li>

In general, from $AB = AC$ and $A \neq O$ it **does not follow** that $B = C$.

</li>
<li>

In general, from $A^2 = I$ it **does not follow** that either $A = I$ or $A = -I$.

</li>
</ol>

For each statement counterexamples can be given, as we already did for the first two.
To get more insight in what is really going on, we can also
try to find out how the third till the sixth statement relate to the first two statements.

For instance, the third statement is closely related to the first. Let us check where 'things go wrong'.

$$
  \begin{array}{cl}
      (A+B)(A+B)& = A(A+B) +B(A+B)\\
                & = A^2 + AB + BA + B^2
  \end{array}
$$

The last expression is only equal to

$$
 A^2 + 2AB + B^2
$$

if

$$
 AB + BA = 2AB
$$

And that is only the case if

$$
   BA = AB.
$$

So any pair of two matrices $A$ and $B$ with

$$
  AB \neq BA
$$

provides a counterexample where

$$
  (A+B)(A+B) \neq A^2 + 2AB + B^2.
$$

Likewise, v. follows from ii. Namely,

$$
  AB = AC \iff AB - AC = O \iff A(B-C) = O.
$$

According to ii. from the last equation we **cannot** deduce
that

$$
 \text{either  } A = O \quad \text{or}\quad B-C = O.
$$

We can create a counterexample by taking for
$A$ and $B$ nonzero matrices for which

$$
  AB = O,
$$

and let $C$ be the zero matrix.
Then $B \neq C$, whereas

$$
  AB = AC =  O \quad  \text{and} \,\,\text{(by assumption)} \quad A \neq O.
$$

Statement vi. also relates to ii. Namely,

$$
  A^2 = I \quad \iff \quad A^2 - I = (A+I)(A-I) = O.
$$

From the last equality we **cannot** conclude that one of the factors
$(A+I)$ or $(A-I)$ must be the zero matrix. In this case we do not get a counterexample for free. You are asked to construct counterexamples in {numref}`Exc:MatrixOps:CounterExamples`.

::::::

::::::{exercise}
:label: Exc:MatrixOps:CounterExamples

<ol type = "i"> 
<li>

Give a $2 \times 2$ matrix $A \neq \pm\, I$ for which $A^2 = I$.

</li>
<li>

Give a $2 \times 2$ matrix $A$ not containing any zeros, for which $A^2 = I$.

</li>
<li>

%And this one also shows that matrix algebra has interesting additional features: \,
Give a $2 \times 2$ matrix $B$ for which $B^2 = -I$.

</li>
</ol>

::::::

The following property connects the two operations matrix transposition and matrix multiplication.

::::::{prf:proposition}
:label: Prop:MatrixOperations:TransposeProduct

If $A$ is an $m\times n$ matrix and $B$ an $n\times p$ matrix, then

$$
   (AB)^T = B^TA^T.
$$

::::::

Before we present the proof, we consider a typical example.

::::::{prf:example}
:label: Ex:TransposeProduct

We verify the rule for the two matrices

$$
   A =  \begin{bmatrix}  2 & 1 & -1 \\ 1 & -1 & 3  \end{bmatrix}   \quad\text{and}\quad
   B = \begin{bmatrix} 1 & -3 & 0\\  4 & 2 & -1  \\ 5  & 2  & 1\end{bmatrix}.
$$

We compute:

$$
  AB = \begin{bmatrix}  2 & 1 & -1 \\ 1 & -1 & 3 \end{bmatrix}
         \begin{bmatrix} 1 & -3 & 0  \\  4 &  2 & -1\\ 5 & 2  &  1 \end{bmatrix} =
  \begin{bmatrix} 1 & -6 & -2 \\  12 & 1 &   4\end{bmatrix}
$$

and

$$
  B^TA^T = \begin{bmatrix}  1 & 4 & 5 \\ -3 & 2 & 2  \\ 0 & -1 & 1 \end{bmatrix}
           \begin{bmatrix}     2& 1 \\
                               1 & -1 \\
                              -1 & 3  \end{bmatrix} =
  \begin{bmatrix} 1 & 12  \\ -6 & 1  \\ -2 & 4  \end{bmatrix},
$$

so that indeed

$$
B^TA^T =  \begin{bmatrix} 1 & 12  \\ -6 & 1  \\ -2 & 4  \end{bmatrix}  =
    \begin{bmatrix} 1 & -6 & -2 \\  12 & 1 &   4\end{bmatrix}^T = (AB)^T.
$$

Careful inspection learns that for the two matrix products exactly the same sums and products of numbers have to be computed.
For instance, in both products $12$ is the sum of products

$$
12 = 1\cdot1 +4\cdot(-1) +5\cdot3 =  1\cdot1 +(-1)\cdot4 +3\cdot5.
$$

::::::

As {prf:ref}`Ex:TransposeProduct` illustrates the rule is not restricted to square matrices $A$ and $B$.
The proof for general matrices $A$ and $B$ for which the product $AB$ is well defined is as follows

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:MatrixOperations:TransposeProduct`
:class: tudproof

To show that

$$
(AB)^T = B^TA^T
$$

we have to show that the matrices have the same size, and are equal entry by entry.
First, we see that $AB$ is an $m \times p$ matrix, so $(AB)^T$ is a $p \times m$ matrix, and $B^TA^T$, being the product of a $p \times n$ matrix
with an $n \times m$, is also a $p \times m$ matrix.

Second, the $(i,j)$ entry of $(AB)^T$ is the $(j,i)$ entry of $AB$, which is the (row-column) product of the $j$-th row of $A$ and the $i$-th column of $B$:

$$
[(AB)^T]_{ij} = \begin{bmatrix}  a_{j1} & a_{j2} & \ldots &  a_{jn} \end{bmatrix}\begin{bmatrix}  b_{1i} \\ b_{2i} \\ \vdots \\ b_{ni} \end{bmatrix}.
$$

The $(i,j)$ entry of $B^TA^T$ is the product of the $i$-th row of $B^T$ and the $j$-th column of $A^T$.  
Now
the $i$-th row of $B^T$ is the $i$-th column of $B$ written as a row, and the $j$-th column of $A^T$ is the $j$-th row of $A$ written as a column:
%Now
%the $i$-th row of $B^T$ ($j$-th column of $A^T$) is the $i$-th column %of $B$ ($j$-th row of $A$) written as a row (column):

$$
[B^TA^T]_{ij} = \begin{bmatrix}   b_{1i} & b_{2i} & \ldots &  b_{ni}   \end{bmatrix}\begin{bmatrix}  a_{j1} \\ a_{j2} \\ \vdots \\  a_{jn} \end{bmatrix}.
$$

Both row-column products end up as the same value

$$
a_{j1}b_{1i} + a_{j2}b_{2i} + \ldots +   a_{jn}b_{ni} =  b_{1i}a_{j1} + b_{2i}a_{j2} + \ldots +   b_{ni}a_{jn}.
$$

::::::

::::::{prf:remark}
We already defined $A^2$ for a square matrix $A$.
We can extend this to higher powers of $A$ in an obvious way:

$$
A^3 = A(A^2),\quad A^4 = A(A^3), \,\,.\,.\,.\,.
$$

Since

$$
A(A^2) = A(AA) = (AA)A,
$$

we can do without the parentheses.

For the same reason

$$
A^kA^{\ell} = A^{k+\ell},  \quad \text{for integers}  \quad k,\ell \geq 1.
$$

If we define

$$
A^0 = I,
$$

then

$$
A^kA^{\ell} = A^{k+\ell}   \quad \text{holds  for all integers} \quad \quad k,\ell \geq 0.
$$

And what can we say about $A^{-1}$?

We will dedicate {numref}`Sec:MatrixInv` to this topic.

::::::

## Grasple exercises

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/262bcea8-548b-45c2-8c37-b4cb3cb03ddc?id=70281
:label: grasple_exercise_3_2_6
:dropdown:
:description: To compute a product $AB$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/718bda8a-9e75-495a-8aea-506788d46432?id=70282
:label: grasple_exercise_3_2_7
:dropdown:
:description: To compute a product $AB$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e5799b3f-53f6-4095-bb96-bc2f4febde30?id=70284
:label: grasple_exercise_3_2_8
:dropdown:
:description: To compute a product $AB$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9d1526f4-777b-4a41-8b8e-c0746f7503c9?id=70285
:label: grasple_exercise_3_2_9
:dropdown:
:description: To compute a product $AB$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d03c79a5-4936-41ae-8129-96ea9dee875a?id=82963
:label: grasple_exercise_3_2_10
:dropdown:
:description: To compute several matrix products.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9fd59a3b-bdc6-42c5-af90-da9b0541437b?id=70291
:label: grasple_exercise_3_2_11
:dropdown:
:description: To compute $\vect{u}^T\vect{v}$ and $\vect{u}\vect{v}^T$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6e4d152b-1eae-480b-a40c-ca8846ed6612?id=70286
:label: grasple_exercise_3_2_12
:dropdown:
:description: To find $k$ for which $AB=BA$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/65f960ef-01a1-4c81-b053-8c93c66504db?id=70287
:label: grasple_exercise_3_2_13
:dropdown:
:description: To find $k$ for which $AB=BA$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d2ccfcf5-7aaf-4859-8219-392abad68e79?id=82853
:label: grasple_exercise_3_2_14
:dropdown:
:description: To find two products $AD_1$ and $D_2A$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2fc08e2c-b3ad-4a2b-8077-ce66abc466d7?id=82936
:label: grasple_exercise_3_2_15
:dropdown:
:description: To find a high power of a special matrix.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6bd96baf-1862-40c7-a21d-24c1dada9078?id=82937
:label: grasple_exercise_3_2_16
:dropdown:
:description: To find a high power of a special matrix.

::::::

The remaining exercises are less of a compuational character.

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/786324ef-8706-4f4d-ac06-f6b4360a70d8?id=69285
:label: grasple_exercise_3_2_17
:dropdown:
:description: Is the zero matrix a diagonal matrix?

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/14b6af51-de5f-4e6c-bfb8-20a018fce053?id=69458
:label: grasple_exercise_3_2_18
:dropdown:
:description: To explain why a certain product does not exist.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/cdb5014d-eace-489e-9616-45e03bb6e95e?id=69295
:label: grasple_exercise_3_2_19
:dropdown:
:description: To find a matrix $A \neq \pm I$ for which $A^2 = I$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7f91a5d2-e1c9-422e-b0f9-ba0b22936e2a?id=69456
:label: grasple_exercise_3_2_20
:dropdown:
:description: To show that $(cA)^T = cA^T$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/78c129ac-644d-4fbd-bf47-c2283d0e1f7a?id=69460
:label: grasple_exercise_3_2_21
:dropdown:
:description: 'To show: $A^TA = D \iff A$ has orthogonal columns.'

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9fe5f92d-54f9-4794-a2e8-c21a24a5a8cf?id=70288
:label: grasple_exercise_3_2_22
:dropdown:
:description: To find the size of $C$ if $AC = B$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bbed8637-4110-4e90-a1dc-a5960a405caf?id=70289
:label: grasple_exercise_3_2_23
:dropdown:
:description: Number of columns of $C$ if $AC=B$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/eb4b9e6e-0436-466c-bb1f-7e596b43ec34?id=70290
:label: grasple_exercise_3_2_24
:dropdown:
:description: To find the number of rows of $B$ if $BC$ is an $m\times n$ matrix.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/deea79ca-ba41-46fc-b75b-4cd109fc0513?id=71118
:label: grasple_exercise_3_2_25
:dropdown:
:description: Finding $E$ such that $EA = M$ &nbsp; (or $AE = M$).

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/0b27fa70-e097-4090-b57e-7225019a4624?id=78589
:label: grasple_exercise_3_2_26
:dropdown:
:description: A bit like the previous one 'by inspection'.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/958761d7-421f-40f1-b3be-3535bf71422b?id=82968
:label: grasple_exercise_3_2_27
:dropdown:
:description: Two True/False questions about products and symmmetric matrices.

::::::
