(Sec:DeterminantsViaCofactors)=

# Determinants via Cofactor Expansion

(Sec:DetCofactors:Definition)=

## Definition of an $n \times n$ determinant


In {numref}`Sec:DetGeometric` we have defined determinants of 2 by 2 and 3 by 3 matrices in a geometric way.
We start with the general definition straightaway.

::::::{prf:definition}
:label: Dfn:DetCofactors:SubmatrixAij

Let $A$ be an $n\times n$ matrix, with $n \geq 2$. The **submatrix** $A_{ij}$ is the $(n-1) \times (n-1)$ matrix that remains when the $i$th row and the $j$th column of $A$ are deleted.

::::::

::::::{prf:example}

For the matrix $A = \left[\begin{array}{cccc} 2 & 0 & 0 & 4 \\
1 & 2 & 3 & 4 \\ 2 & 1 & 0 & 3 \\ 6 & 4 & 3 & 5
\end{array}\right]
$ we have that

$$
A_{13} = \left[\begin{array}{ccc}    1 & 2  & 4 \\ 2 & 1  & 3 \\ 6 & 4& 5   \end{array}\right]
\quad \text{and} \quad
A_{42} =   \left[\begin{array}{ccc} 2  & 0 & 4 \\  1  & 3 & 4 \\ 2  & 0 & 3
\end{array}\right]
.
$$

::::::

::::::{prf:definition}
:label: Dfn:DetCofactors:Determinant

Let $A$ be an $n\times n$ matrix, with $n \geq 3$.
The **determinant** of $A$, which we denote by either $\det{A}$ or $|A|$, is defined by

$$
|A| = \det{A} = \sum_{i=1}^n   (-1)^{1+i} a_{i1}\det{A_{i1}} = \sum_{i=1}^n   a_{i1} C_{i1}.
$$

Here

$$
C_{ij} = (-1)^{i+j} \det{A_{ij}}
$$

is called the $(i,j)$th **cofactor** of $A$.

::::::

This is an example of a so-called **recursive** definition. The evaluation of an $n$ by $n$ determinant is reduced to the evaluation of $n$ determinants 'one size smaller'. By repeating this reduction we get smaller and smaller determinants and end up with 2 by 2 determinants as defined in {prf:ref}`Def:CrossProduct:2x2determinant`. 
And the formula also works for $2 \times 2$ matrices:

$$
   \text{for}  \,\,A = \begin{bmatrix}a & b \\ c & d  \end{bmatrix}, \quad
   \text{det}\,A = a\cdot\text{det}\,A_{11} - b\cdot\text{det}\,A_{12} = ad-bc.
$$

Let us now look at an example first.

::::::{prf:example}
:label: Ex:DetCofactor:4x4Det

We will compute the determinant of the matrix $A = \left[\begin{array}{cccc} 7 & 2 & 3 & 4 \\
0 & 2 & 5 & 2 \\ 0 & 1 & 4 & 3 \\ 6 & 2 & 3 & 1
\end{array}\right]$.

$$
\begin{array}{rcl}
\det{A} &=& 7\cdot\det{A_{11}} - 0\cdot\det{A_{21}} + 0\cdot\det{A_{31}} - 6\cdot\det{A_{41}} \\
&=& 7\cdot\text{det}\left[\begin{array}{ccc} 2 & 5 & 2 \\  1 & 4 & 3 \\ 2 & 3 & 1  \end{array}\right]
- 6\cdot\text{det}\left[\begin{array}{ccc} 2 & 3 &4 \\  2 & 5 & 2 \\  1 & 4 & 3   \end{array}\right]
\end{array}
$$

For the two remaining determinants we act likewise. Using the alternative notation for determinants we find

$$
\begin{array}{rcl}
\left|\begin{array}{ccc} 2 & 5 & 2 \\  1 & 4 & 3 \\ 2 & 3 & 1  \end{array}\right|&=&
2\cdot\left|\begin{array}{cc}  4 & 3 \\  3 & 1  \end{array}\right|-
1\cdot\left|\begin{array}{cc}  5 & 2 \\ 3  & 1  \end{array}\right|+
2\cdot\left|\begin{array}{cc}  5 & 2  \\ 4 & 3  \end{array}\right|\\
&=&
2\cdot (4-9) -   (5-6) + 2\cdot (15-8) = 5
\end{array}
$$

and

$$
\begin{array}{rcl}
\left|\begin{array}{ccc} 2 & 3 &4 \\  2 & 5 & 2 \\  1 & 4 & 3 \end{array}\right|&=&
2\cdot\left|\begin{array}{cc}  5&2 \\ 4&3  \end{array}\right|-
2\cdot\left|\begin{array}{cc}  3&4 \\ 4&3  \end{array}\right|+
1\cdot\left|\begin{array}{cc}  3&4 \\ 5&2 \end{array}\right|\\
&=&
2\cdot (15-8) -   2\cdot (9-16) +  (6-20) = 14.
\end{array}
$$

So that

$$
\det{A} = 7\cdot 5 - 6\cdot 14 = -49.
$$

::::::

We call the procedure indicated in {prf:ref}`Dfn:DetCofactors:Determinant` **cofactor expansion along the first column**.  Note that this is exactly in line with {prf:ref}`Prop:DetGeometric:ColExpand`. 
Often the word 'cofactor' is omitted and we simply say expansion along the first column.
The signs are determined by the position in the matrix/determinant according to the following pattern

$$
\left|\begin{array}{ccccccc} + & - & + & \ldots & \ldots & \ldots & \ldots\\[.7ex]
                                - & + & - &  \ldots & \ldots& \ldots & \ldots \\[.7ex]
                                + & - & + & \ldots & \ldots& \ldots & \ldots \\[.7ex]
                                - & + & - & \ldots & \ldots& \ldots & \ldots \\[.7ex]
  \ldots  & \ldots & \ldots & \ldots & \ldots& \ldots & \ldots \\[.7ex]
  \ldots  & \ldots & \ldots & \ldots & \ldots& \ldots & \ldots \\[.7ex]
  \ldots  & \ldots & \ldots & \ldots & \ldots& + & - \\[.7ex]
  \ldots  & \ldots & \ldots & \ldots & \ldots& - & +
  \end{array} \right|
$$

For instance, on the diagonal all signs are $+$.

For the $4\times 4$ {prf:ref}`Ex:DetCofactor:4x4Det` we could take advantage of the two zeros in the first column.
For an $n\times n$ matrix without zeros the complete expansion will contain $n\cdot (n-1) \cdot \ldots \cdot 3 \cdot 2 \cdot 1 = n!$ products.
We have already seen in the previous section

$$
\left|\begin{array}{cc} a_1 & b_1 \\  a_2 & b_2
\end{array}\right| = a_1b_2 - a_2b_1,
$$

and

:::::{math}
:label: Eq:DetCofactors:3x3determinant


\left|\begin{array}{rrr} a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right|
\begin{array}{lcl}
&=&   a_{11}a_{22}a_{33} - a_{11}a_{23}a_{32} +a_ {12}a_{23}a_{31} \\
& & \quad - a_{12}a_{21}a_{33} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31}. \end{array}

:::::

They contain $2=2\cdot1$ resp. $6 = 3\cdot2\cdot1$ products.
For a larger matrix the work involved quickly runs out of hand. Luckily there are several shortcuts to compute a determinant. The first important one is that the first column does not play any special role. The determinant can be found by expanding along any column, and also along any row. This is the content of the first theorem.

::::::{prf:theorem}
:label: Thm:DetCofactors:RowOrColumnExpansion

The determinant can be found by expansion along any column. Taking the $j$th column this gives

$$
\det{A} = \sum_{i=1}^n   (-1)^{i+j} a_{ij}\det{A_{ij}} = \sum_{i=1}^n   a_{ij} C_{ij}.
$$

It can also be found by expansion along any row. For the $i$th row this gives

$$
\det{A} = \sum_{j=1}^n   (-1)^{i+j} a_{ij}\det{A_{ij}} = \sum_{j=1}^n   a_{ij} C_{ij}.
$$

::::::

We omit the proof, which is rather long and technical.

The following example illustrates the rule for the determinant of an arbitrary $3 \times 3$ matrix.

::::::{prf:example}

Let us compute the cofactor expansion of the matrix
$A = \left[\begin{array}{rrr} a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right]
$ along its third row.

$$
\left|\begin{array}{rrr} a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
\class{blue}{a_{31}} & \class{blue}{a_{32}} & \class{blue}{a_{33}}
\end{array}\right|=
\class{blue}{a_{31}}\left|\begin{array}{cc}a_{12} & a_{13}\\ a_{22} & a_{23}\end{array}\right|-
\class{blue}{a_{32}}\left|\begin{array}{cc}a_{11} & a_{13}\\ a_{21} & a_{23}\end{array}\right|+
\class{blue}{a_{33}}\left|\begin{array}{cc}a_{11} & a_{12}\\ a_{21} & a_{22}\end{array}\right|
$$

$$
\begin{array}{cl} = & a_{31}( a_{12} a_{23} - a_{22}a_{13}) -
a_{32}( a_{11} a_{23} - a_{21}a_{13}) +
a_{33}( a_{11} a_{22} - a_{21}a_{12}) \\
=&  a_{31} a_{12} a_{23} -  a_{31} a_{22}a_{13}
-a_{32} a_{11} a_{23} +a_{32} a_{21}a_{13} +
a_{33}a_{11} a_{22} - a_{33}a_{21}a_{12}.
\end{array}
$$

Cofactor expansion along the second column yields

$$
\left|\begin{array}{rrr} a_{11} & \class{blue}{a_{12}} & a_{13} \\
a_{21} & \class{blue}{a_{22}} & a_{23} \\
a_{31} & \class{blue}{a_{32}} & a_{33}
\end{array}\right|=
-\class{blue}{a_{12}}\left|\begin{array}{cc}a_{21} & a_{23}\\ a_{31} & a_{33}\end{array}\right|+\class{blue}{a_{22}}\left|\begin{array}{cc}a_{11} & a_{13}\\ a_{31} & a_{33}\end{array}\right|-\class{blue}{a_{32}}\left|\begin{array}{cc}a_{11} & a_{13}\\ a_{21} & a_{23}\end{array}\right|
$$

$$
\begin{array}{cl} = & -a_{12}( a_{21} a_{33} - a_{31}a_{23})
+a_{22}( a_{11} a_{33} - a_{31}a_{13})
-a_{32}( a_{11} a_{23} - a_{21}a_{13}) \\
=&  -a_{12}a_{21} a_{33} + a_{12}a_{31}a_{23}
+a_{22} a_{11} a_{33} - a_{22}a_{31}a_{13}
-a_{32}a_{11} a_{23} + a_{32}a_{21}a_{13}.
\end{array}
$$

These are the same six products with the same signs as we found with the first expansion
(Equation {eq}`Eq:DetCofactors:3x3determinant`).

::::::

In the following example we use this freedom of choice to compute a determinant of a matrix that contains a lot of zeros.

::::::{prf:example}
:label: Ex:DetCofactors:FiveByFive

We will compute the determinant of the matrix

$$
A=\left[\begin{array}{rrrrr}
2 & 1 & 3 & 0  & 2 \\
5 & 4 & 0 & 0 & 0 \\
0 & 4 & 0 & 0 & 0 \\
6 & 2 & 1 & 3 & 2 \\
1 & 3 & -2 & 0 & -3
\end{array}
\right]
.
$$

With its four zeros the third row seems a good candidate to expand along.
Of the five terms

$$
a_{3j}C_{3j} = (-1)^{3+j}a_{3j}\det{A_{3j}}, \quad   j = 1,\ldots,5
$$

only the second gives a nonzero contribution:

$$
\left|\begin{array}{rrrrr}
2 & 1 & 3 & 0  & 2 \\
5 & 4 & 0 & 0 & 0 \\
0 & 4 & 0 & 0 & 0 \\
6 & 2 & 1 & 3 & 2 \\
1 & 3 & -2 & 0 & -3
\end{array} \right| =  (-1)^{3+2}\cdot4
\left|\begin{array}{rrrrr}
2 & 3 & 0  & 2 \\
5 & 0 & 0 & 0 \\
6 & 1 & 3 & 2 \\
1  & -2 & 0 & -3
\end{array} \right| =
-4 \left|\begin{array}{rrrrr}
2 & 3 & 0  & 2 \\
5 & 0 & 0 & 0 \\
6 & 1 & 3 & 2 \\
1  & -2 & 0 & -3
\end{array} \right|.
$$

As a next step we may choose the third column to expand along, and for the ensuing $3\times3$ determinant we single out the second row:

$$
-4 \left|\begin{array}{rrrr}
2 & 3 & 0  & 2 \\
5 & 0 & 0 & 0 \\
6 & 1 & 3 & 2 \\
1  & -2 & 0 & -3
\end{array} \right|=
-4\cdot(-1)^{3+3}\cdot 3
\left|\begin{array}{rrr}
2 & 3   & 2 \\
5 & 0  & 0 \\
1  & -2  & -3
\end{array} \right|=
(-12)\left|\begin{array}{rrr}
2 & 3   & 2 \\
5 & 0  & 0 \\
1  & -2  & -3
\end{array} \right|
$$

$$
=
-12 \cdot  (-1)^{2+1} \cdot 5 \left|\begin{array}{rr} 3   & 2 \\     -2  & -3       \end{array} \right|=
60 \cdot\big(3\cdot(-3) - 2 \cdot(-2)\big)= -300.
$$

::::::

(Sec:DetCofactors:Triangular)=

## Determinants of triangular matrices

The next example is meant to illustrate a more general property.

::::::{prf:example}
:label: Ex:DetCofactors:Triangular

The determinant of the matrix $A = \left[\begin{array}{cccc}
2 & 3 & -1 & 2 \\
0 & 3 & 5 & -9 \\
0 & 0 & 4 & 2 \\
0  & 0 & 0 & -1
\end{array} \right]$  
can be quickly found by expanding along columns from left to right.

$$
\left|\begin{array}{cccc}
2 & 3 & -1 & 2 \\
0 & 3 & 5 & -9 \\
0 & 0 & 4 & 2 \\
0  & 0 & 0 & -1
\end{array} \right|=
2 \left|\begin{array}{ccc}   3 & 5 & -9 \\0 & 4 & 2 \\0 & 0 & -1  \end{array} \right|=
2 \cdot 3 \left|\begin{array}{cc}   4 & 2 \\0 & -1  \end{array} \right|=
2 \cdot 3 \cdot 4 \cdot (-1).
$$

Alternatively, we can expand along rows from bottom till top.

$$
\left|\begin{array}{cccc}
2 & 3 & -1 & 2 \\
0 & 3 & 5 & -9 \\
0 & 0 & 4 & 2 \\
0  & 0 & 0 & -1
\end{array} \right|=
(-1) \left|\begin{array}{ccc}  2 & 3 & -1 \\ 0 & 3 & 5 \\ 0 & 0 & 4  \end{array} \right|=
(-1) \cdot 4 \left|\begin{array}{cc}   2 & 3 \\0 & 3  \end{array} \right|=
(-1) \cdot 4  \cdot 3 \cdot 2.
$$

::::::

The matrix $A$ is an example of what is called an upper triangular matrix.

::::::{prf:definition}
:label: Dfn:DetCofactors:TriangularMatrix

A square matrix $A$ is called an **upper triangular matrix**, if all the elements below the diagonal are 0.
Formally, for an upper triangular matrix we have

$$
a_{ij} = 0 \quad \text{if} \quad i > j.
$$

In the same manner we can define **lower triangular matrices**.

A **triangular matrix** is a matrix that is either an upper triangular or a lower triangular matrix.

::::::

Note that a diagonal matrix is both upper and lower triangular.

The property we hinted at in {prf:ref}`Ex:DetCofactors:Triangular` is captured in the following proposition.

::::::{prf:proposition}
:label: Prop:DetCofactors:TriangularMatrices

For a triangular matrix the determinant is equal to the product of the entries on the diagonal.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:DetCofactors:TriangularMatrices`
:class: tudproof

We can use the same strategy as in {prf:ref}`Ex:DetCofactors:Triangular`.
That is, for an upper triangular matrix expand along the columns from left to right, for a lower triangular matrix
expand along the rows from top to bottom.

::::::

In {numref}`Sec:DetGeometric` we have seen that for $2 \times 2$ and $3 \times 3$ matrices $A$ it holds that $A$ is invertible if and only if $\det{A} \neq 0$.

From {prf:ref}`Prop:DetCofactors:TriangularMatrices` it follows that this property still holds for **triangular** matrices.

::::::{prf:proposition}
:label: Prop:DetCofactors:InvertibleTriangular

A triangular matrix is invertible if and only if it has a non-zero determinant.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:DetCofactors:InvertibleTriangular`
:class: tudproof

Let us first consider the case of an $n \times n$ upper triangular matrix $U$, with entries $u_{ij}$. Such a matrix is an echelon matrix. It is invertible if and only if it has $n$ linearly independent columns, which is the case if all diagonal elements $u_{ii}$ are nonzero. And this last is equivalent to

$$
u_{11}\cdot u_{22}  \cdot  \ldots \cdot u_{nn} = \det{U} \neq 0.
$$

For a lower triangular matrix $L$ a similar argument can be given.

(Or we can consider $L^T$, which is an upper triangular matrix, and make use of the upcoming {prf:ref}`Prop:DetCofactors:DetTranspose`.)

::::::

We need to know a little more about determinants to establish this connection with invertibility for all matrices.

(Sec:DetCofactors:Transpose)=

## The determinant of the transpose of a matrix


The last property that may be expected to hold as a consequence of {prf:ref}`Thm:DetCofactors:RowOrColumnExpansion` where the rows and the columns play interchangeable roles is the following.

::::::{prf:proposition}
:label: Prop:DetCofactors:DetTranspose

For any $n\times n$ matrix $A$ the determinant of $A$ is equal to the determinant of its transpose. In a formula

$$
\det{A} = \text{det}\big(A^T\big).
$$

::::::

::::::{prf:example}

Take the matrix $A = \left[\begin{array}{ccc}  1 & 3 & 4 \\ 5 & 6 & 7 \\ 2 & 1 & 0  \end{array} \right]
$.

Expanding along the first _row_ we find that

$$
\begin{array}{rcl}
\left|\begin{array}{ccc}  1 & 3 & 4 \\ 5 & 6 & 7 \\ 2 & 1 & 0  \end{array} \right|&=&
1 \left|\begin{array}{cc}    6 & 7 \\  1 & 0  \end{array} \right|-
3  \left|\begin{array}{cc}  5 &  7 \\ 2  & 0  \end{array} \right|+
4  \left|\begin{array}{cc}  5 & 6 \\ 2 & 1   \end{array} \right|\\
&=& 1\cdot(-7) - 3\cdot(-14) + 4\cdot(-7).
\end{array}
$$

For the determinant of the transpose $A^T$ we find, expanding along the first _column_:

$$
\begin{array}{rcl}
\left|\begin{array}{ccc}  1 &  5 & 2\\ 3 & 6 & 1 \\ 4 & 7 & 0  \end{array} \right|&=&
1 \left|\begin{array}{cc}   6 & 1 \\ 7 & 0   \end{array} \right|-
3  \left|\begin{array}{cc}  5 &  2 \\ 7  & 0  \end{array} \right|+
4  \left|\begin{array}{cc}  5 & 2 \\ 6 & 1   \end{array} \right|\\
&=& 1\cdot(-7) - 3\cdot(-14) + 4\cdot(-7).
\end{array}
$$

Which gives the same value.

::::::

In fact, by looking at the structure rather than at the numbers, we see the example illustrates that the theorem holds for
$3 \times 3$ determinants since it holds for $2 \times 2$ determinants.
In a similar way, the property $\text{det}\big(A^T\big) = \text{det}(A)$ for $4 \times 4$ matrices follows from the correctness for $3 \times 3$ matrices, and this can be (either formally or informally) lifted up to determinants of an arbitrary size.


## Grasple exercises

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/34eb983b-c7e7-40f3-a983-6bfb970f6836?id=93135
:label: grasple_exercise_5_2_1
:dropdown:
:description: To compute the determinant of 2x2 matrix.

::::::


::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b86bd320-47cd-45cb-ab88-81b20a48c427?id=93136
:label: grasple_exercise_5_2_2
:dropdown:
:description: To compute the determinant of 3x3 matrix.

::::::


::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2f993d71-6a19-435d-a449-cc0dbb8237d5?id=93137
:label: grasple_exercise_5_2_3
:dropdown:
:description: To compute the determinant of 4x4 matrix (with many zeros).

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/40de4737-1823-425b-b997-a07c53cb2f96?id=93138
:label: grasple_exercise_5_2_4
:dropdown:
:description: To compute the determinant of 4x4 matrix.

::::::


::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/57cd522b-6096-416a-a739-fea5cbbc77c9?id=93139
:label: grasple_exercise_5_2_5
:dropdown:
:description: To compute the determinant of an almost upper triangular 4x4 matrix 

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/25c54a22-eb00-4cbf-ac0c-21b4974a48ff?id=92927
:label: grasple_exercise_5_2_6
:dropdown:
:description: To compute the determinant of 5x5 'structured' matrix.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/48fedcac-0039-4eaa-9f71-20fa86ed4536?id=93142
:label: grasple_exercise_5_2_7
:dropdown:
:description: To compute the determinant of the products of certain matrices.

::::::