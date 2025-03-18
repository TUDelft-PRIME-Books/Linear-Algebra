(Sec:MatrixInv)=

# The Inverse of a Matrix

## Introduction

In {numref}`Sec:MatrixOps` we defined the sum and product of matrices (of compatible sizes), and we saw that to a certain extent matrix algebra is guided by the same rules as the arithmetic of real numbers. We can also subtract two matrices via

$$
   A - B = A + (-1)B,
$$

but we did not mention division of matrices. <BR>
For two numbers $a$ and $b$, with $a \neq 0$, the equation

$$
   ax = b
$$

has the unique solution

$$
  x = \frac{b}{a} = a^{-1}b = ba^{-1},
$$

where

$$
   a^{-1} = \frac1a
$$

is the (unique) solution of the equation

$$
   ax = 1.
$$

The bad news:

<p style="text-align:center;">
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mstyle displaystyle="true" scriptlevel="0">
    <mfrac>
      <mi>A</mi>
      <mi>B</mi>
    </mfrac>
  </mstyle>
</math> cannot be defined in any useful way!
</p>

First of all the corresponding matrix equation

$$
  AX = B, \,\, A\neq O
$$

does not always have a solution, or the solution is not unique, not even in the case of two
$n \times n$ matrices $A$ and $B$. The following two examples to illustrate this.

::::::{prf:example}
:label: Ex:MatrixInv:MatrixEqNoSolution

The matrix equation

$$
 AX = B
$$

where

$$
 A = \begin{bmatrix} 1 & 2 \\ 1 & 2 \end{bmatrix}, \quad B =  \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix}
$$

does not have a solution. Why? Well, any column of $AX$ is a linear combination of the columns of $A$,
and the columns of $B$ obviously cannot be written as such linear combinations:

$$
  \begin{bmatrix} 1  \\ 0  \end{bmatrix} \neq c_1 \begin{bmatrix} 1  \\ 1  \end{bmatrix}  + c_2 \begin{bmatrix} 2  \\ 2  \end{bmatrix}
  \quad \text{for all } c_1,c_2 \quad\text{in  } \mathbb{R}.
$$

::::::

::::::{prf:example}
:label: Ex:MatrixInv:MatrixEqInfSolutions

The matrix equation

$$
 AX = B
$$

where

$$
 A = \begin{bmatrix} 1 & 2 \\ 1 & 2 \end{bmatrix}, \quad B =  \begin{bmatrix} 1 & 4 \\ 1 & 4 \end{bmatrix}
$$

has infinitely many solutions. Two of those are for instance

$$
  X_1 = \begin{bmatrix} 1 & 0 \\ 0 & 2 \end{bmatrix} \quad \text{and} \quad X_2 = \begin{bmatrix} -1 & 2 \\ 1 & 1 \end{bmatrix}.
$$

::::::

And lastly, if there is a matrix $C$ for which

$$
   CA = I
$$

and we would adopt the notation

$$
  C = A^{-1}
$$

then

$$
    \begin{array}{rcl}
         AX = B &\Rightarrow&  C(AX) = CB \\
                &\Rightarrow& (CA)X \,=\, IX \,=\, \underline{\underline{X \,=}}\,\,\,\,\,  CB \,=\, \underline{\underline{A^{-1}B}}.
   \end{array}
$$

So $X = A^{-1}B$.
However,
it is in no way clear why $A^{-1}B$ and $BA^{-1}$
should be equal, and in general indeed they are not. So the notation

$$
  \dfrac{B}{A}
$$

will still be ambiguous.

For non-square matrices things are even worse. In this section we will only consider square matrices.

(Subsec:MatrixInv:DefInverse)=

## Definition and basic properties of the inverse

::::::{prf:definition}
:label: Dfn:MatrixInv:DefInverse

A square matrix $A$ is called invertible if there exists a matrix $B$ for which

$$
   AB = BA = I.
$$

In this situation the matrix $B$ is called the **inverse** of $A$ and we write

$$
    B = A^{-1}.
$$

A matrix that is invertible is also called a **regular** matrix, and
a non-invertible matrix is also called a **singular** matrix.

::::::

Note the use of the definite article **the** in the sentence ''$B$ is called **the** inverse of $A$''. The following proposition justifies this choice of word.

::::::{prf:proposition}
:label: Prop:MatrixInv:UniqueInverse

If an inverse of a matrix $A$ exists, then it is unique.

::::::

The proof is very short, when we plug in the right idea at the right place.

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:MatrixInv:UniqueInverse`
:class: tudproof

Suppose $B$ and $C$ are two matrices that satisfy the properties of being an inverse of $A$, i.e.

$$
  AB = BA = I \quad \text{and} \quad AC = CA = I.
$$

Then the following chain of identities proves that $B$ and $C$ must be equal:

$$
  B = B\,I \,= B\,(AC) = (BA)\,C= I\,C = C.
$$

::::::

::::::{prf:remark}
Actually, the proof shows slightly more, as the assumptions

$$
   CA= I, \quad AB = I
$$

are not used. In fact it shows that for three $n \times n$ matrices $A$, $B$ and $C$

$$
  \text{if} \quad BA = I \quad \text{  and  }\quad AC = I \quad\text{  then  } \quad B = C.
$$

::::::

::::::{prf:example}
:label: Ex:FirstInverse

For the matrices

$$
  A =  \begin{bmatrix} 1 & 2 \\ 3 & 5 \end{bmatrix}
    \quad \text{and} \quad
  B =   \begin{bmatrix} -5 & 2 \\ 3 & -1 \end{bmatrix}
$$

we see

$$
 \begin{bmatrix} 1 & 2 \\ 3 & 5 \end{bmatrix}
 \begin{bmatrix} -5 & 2 \\ 3 & -1 \end{bmatrix} =
 \begin{bmatrix} -5 & 2 \\ 3 & -1 \end{bmatrix}
 \begin{bmatrix} 1 & 2 \\ 3 & 5 \end{bmatrix}
 =
 \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}.
$$

So $A$ and $B$ are each other's inverse.

Another example:

$$
 \begin{bmatrix} 1 & 1 & 0 \\
                 1 & 1 & 1 \\
                 0 & 1 & 1 \end{bmatrix}
 \begin{bmatrix} 0 & 1 & -1 \\
                 1 &  -1 &  1 \\
                -1 & 1 &  0  \end{bmatrix} =
 \begin{bmatrix} 1 & 0 & 0\\
                 0 & 1 & 0 \\
                 0 & 0 & 1\end{bmatrix}.
$$

You may check for yourself that the product in the other order also gives $I$,
so

$$
 \begin{bmatrix} 1 & 1 & 0 \\
                 1 & 1 & 1 \\
                 0 & 1 & 1 \end{bmatrix}^{-1}
                 =
 \begin{bmatrix} 0 & 1 & -1 \\
                 1 & -1 &  1 \\
                -1 & 1 &  0  \end{bmatrix}
$$

It will appear ({prf:ref}`Rem:MatrixInv:RightInvLeftInv`) that for square matrices, a one-sided inverse is automatically a two-sided inverse, by which we mean

$$
  \text{if}  \quad AB = I \quad \text{then also}\quad BA = I.
$$

::::::

The first example can be generalized:

::::::{prf:proposition}
:label: Prop:MatrixInv:Inverse2x2

If $A =  \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, then $A^{-1}$
exists if and only if

$$
  ad - bc \neq 0.
$$

In that case

$$
  A^{-1} = \begin{bmatrix} a & b \\ c & d \end{bmatrix}^{-1} =
  \begin{bmatrix} \dfrac{d}{ad - bc} & \dfrac{-b}{ad - bc} \\
                  \dfrac{-c}{ad - bc} & \dfrac{a}{ad - bc} \end{bmatrix}
  =
  \frac{1}{ad-bc}\begin{bmatrix} d &- b \\ -c & a \end{bmatrix}.
$$

::::::

We leave the verification as an exercise.

::::::{exercise}
:label: Exc:MatrixInv:CheckBA=I

Verify that the matrix $B=A^{-1}$ proposed in {prf:ref}`Prop:MatrixInv:Inverse2x2` indeed satisfies

$$
  AB = BA = I.
$$

Also check that the first matrix in {prf:ref}`Ex:FirstInverse` illustrates the formula.

::::::


::::::{admonition} Solution to&nbsp;{numref}`Exc:MatrixInv:CheckBA=I`
:class: solution, dropdown

$$
\begin{array}{rcl} BA &=&
\dfrac{1}{ad-bc}\begin{bmatrix} d &-b \\ -c & a \end{bmatrix}
\begin{bmatrix} a & b \\ c & d \end{bmatrix}\\
 &=&
\dfrac{1}{ad-bc}\begin{bmatrix} da-bc &db- bd \\ -ca+ac & -cb+ad \end{bmatrix} \\
&=&
\begin{bmatrix} \dfrac{da-bc}{ad-bc} &0 \\ 0 & \dfrac{-cb+ad}{ad-bc} \end{bmatrix} = \begin{bmatrix} 1&0 \\ 0 & 1 \end{bmatrix}.
\end{array}
$$

Which is one of the two identities.

Applying the formula of {prf:ref}`Prop:MatrixInv:Inverse2x2` to the matrix $A = \begin{bmatrix} 1 & 2 \\ 3 & 5 \end{bmatrix}$ of {prf:ref}`Ex:FirstInverse` gives

$$
 A^{-1} = \dfrac{1}{1\cdot5 - 2\cdot 3}\begin{bmatrix} 5 & -2 \\ -3&1 \end{bmatrix} = -\begin{bmatrix} 5 & -2 \\ -3&1 \end{bmatrix} =  \begin{bmatrix} -5 & 2 \\ 3&-1 \end{bmatrix},
$$

which is indeed the matrix $B$ that was proposed there.
::::::

::::::{prf:remark}
:label: Rem:MatrixInvDetZeroDependentColumns

The condition

$$
   ad - bc \neq 0
$$

is equivalent to the statement

$$
 \text{the vectors  } \begin{bmatrix} a  \\ c  \end{bmatrix} \text{  and  } \begin{bmatrix} b  \\ d  \end{bmatrix} \text{  are linearly independent.}
$$

First we show that

$$
 ad - bc = 0  \text{   implies that   }
  \begin{bmatrix} a  &b\\ c&d  \end{bmatrix} \text{  has linearly dependent columns.}
$$

It is best to split this in two cases:

$$
   ad = 0 \quad \text{and} \quad  ad \neq 0.
$$

If we assume

$$
  ad - bc = 0 \quad \text{and} \quad  ad = 0,
$$

then we have

$$
  b = 0 \quad \text{or} \quad  c = 0
$$

which leads to a matrix

$$
  \begin{bmatrix} a & b \\ c & d  \end{bmatrix}
$$

with either a zero row or a zero column, which will indeed have linearly dependent columns.
Second, if we assume

$$
  ad - bc = 0 \quad\text{and} \quad  ad \neq 0
$$

then both $a \neq 0$ and $d \neq 0$, in which case

$$
  d =  \frac{bc}{a}, \quad \text{so  }
   \begin{bmatrix} b  \\ d  \end{bmatrix} =
   \begin{bmatrix} b  \\ \frac{bc}{a}  \end{bmatrix} =
    \dfrac{b}{a}\begin{bmatrix} a  \\ c  \end{bmatrix},
$$

hence the columns are again linearly dependent.
Thus we have shown:

$$
  ad-bc = 0 \quad \Longrightarrow \quad  \begin{bmatrix} a & b \\ c & d  \end{bmatrix}
  \text{  has linearly dependent columns.}
$$

Next let us consider the converse, i.e.

$$
 \begin{bmatrix} a  & b \\ c&d  \end{bmatrix} \text{  has linearly dependent columns}  \quad \text{implies: } \quad
  ad - bc = 0.
$$

If a $2 \times 2$ matrix has two linearly dependent columns, then
one of the columns will be a multiple of the other column, e.g.

$$
  \text{either } \quad  \begin{bmatrix} a  \\ c   \end{bmatrix} = k  \begin{bmatrix} b  \\ d   \end{bmatrix}  \quad
  \text{or}\quad
  \begin{bmatrix} b  \\ d   \end{bmatrix} = k  \begin{bmatrix} a  \\ c   \end{bmatrix} .
$$

In both cases it is easily checked that

$$
  ad-bc = 0.
$$

::::::

The following proposition shows that the above considerations can be generalized.

::::::{prf:proposition}
:label: Prop:MatrixInv:InvertibleIndepCols

If $A$ is a square matrix, then

$$
  AX = I
$$

has a unique solution if and only if

$$
 A \text{  has linearly independent columns.}
$$

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:MatrixInv:InvertibleIndepCols`
:class: tudproof

As in the proof in {prf:ref}`Rem:MatrixInvDetZeroDependentColumns` we have to prove two implications:

$$
 AX = I \text{   has a unique solution } \quad\Longrightarrow \quad
 A \text{  has linearly independent columns}
$$

and

$$
  A \text{  has linearly independent columns}
\quad\Longrightarrow \quad  AX = I \text{  has a unique solution.}
$$

For the first part, assume that

$$
 AX = I \quad \text{has a (unique) solution.}
$$

That means that every column $\vect{e}_j$ of the identity matrix is a linear combination of columns $\vect{a}_1, \ldots, \vect{a}_n$ of $A$.
So the span of the columns of $A$ contains the span of the columns of
$\vect{e}_1, \ldots, \vect{e}_n$, which is the whole $\mathbb{R}^n$. Thus **every** linear system

$$
  A\vect{x} =\vect{b}, \quad \vect{b} \in \mathbb{R}^{n}
$$

has a solution.
Then the reduced echelon form of $A$ must have a pivot in every row, and, since it is a square matrix, it must be the identity matrix. Consequently, it has a pivot in every column, so
the linear system

$$
  A\vect{x} =\vect{0}
$$

only has the trivial solution, which proves that indeed the columns of $A$ are linearly independent.

For the converse, suppose that $A$ has linearly independent columns.
Then the reduced echelon form of $A$ must be the identity matrix.
This implies that for each $\vect{b}$ in $\mathbb{R}^n$

$$
  [\,A\,|\,\vect{b}\,] \sim[\,I\,|\,\vect{b'}\,],
$$

and in particular, each linear system

$$
  A\vect{x} =\vect{e}_j
$$

has a unique solution. If we denote this solution by $\vect{c}_j$ we have that

$$
  A[\,\vect{c}_1\,\,\vect{c}_2\,\, \ldots \,\, \vect{c}_n\,] =
   [\,A\vect{c}_1\,\,A\vect{c}_2\,\, \ldots \,\, A\vect{c}_n\,] =
    [\,\vect{e}_1\,\,\vect{e}_2\,\, \ldots \,\, \vect{e}_n\,] = I.
$$

Since all solutions $\vect{c}_j$ are unique, the solution of the equation

$$

  AX = I


$$

is unique as well.

::::::

It makes sense that the solution $B$ of this matrix equation will be the inverse of $A$, and it is, but it takes some effort to show that the other requirement,

$$
  BA = I
$$

is also fulfilled. In the next subsection we will see that the matrix equation

$$
  AX = I
$$

will lead the way to an algorithm to compute the inverse of a matrix.
Before we go there we will look at some general properties of invertible matrices.

::::::{prf:proposition}
:label: Prop:SolutionViaInverse

If the $n \times n$ matrix $A$ is invertible and $B$ is an $n \times p$ matrix, then the solution of the matrix equation

$$
  AX = B
$$

is unique, and given by

$$
  X = A^{-1}B.
$$

In particular, if the matrix $B$ has only one column, i.e., if it is a vector, then

$$
  A\mathbf{x} = \mathbf{b} \quad \text{has the unique solution} \quad \mathbf{x} = A^{-1}\mathbf{b}.
$$

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:SolutionViaInverse`
:class: tudproof

We multiply both sides of the equation

$$
  AX = B
$$

by $A^{-1}$ and use the fact that the matrix product has the associative property:

$$
\begin{array}{rl}
  AX = B \quad\Longrightarrow\quad A^{-1}(AX) = A^{-1}B & \Longrightarrow\quad (A^{-1}A)X = IX = A^{-1}B \\
  &\Longrightarrow \quad X = A^{-1}B.
\end{array}
$$

::::::

We illustrate the proposition by an example.

::::::{prf:example}
:label: Ex:MatrixInv:SolutionViaInverse

Suppose the matrix $A$ and the vectors $\mathbf{b}_1$ and $\mathbf{b}_1$ are given by

$$
 A=\begin{bmatrix}1 & 2 \\ 3 & 4 \end{bmatrix}, \quad
        \mathbf{b}_1= \begin{bmatrix}-1  \\ 1 \end{bmatrix} \quad \text{and} \quad
        \mathbf{b}_2=\begin{bmatrix}2  \\ 10 \end{bmatrix}.
$$

Consider the two linear systems

$$
 A\mathbf{x} =\mathbf{b}_1\quad \text{and} \quad
 A\mathbf{x} = \mathbf{b}_2.
$$

Using the inverse matrix

$$
  A^{-1} = \frac{1}{-2}\begin{bmatrix}4 & -2 \\ -3 & 1 \end{bmatrix} =
   \frac{1}{2}\begin{bmatrix}-4 & 2 \\ 3 & -1 \end{bmatrix},
$$

the two solutions are quickly written down:

$$
  \vect{x}_1= A^{-1}\vect{b}_1=
  \frac{1}{2}\begin{bmatrix}-4 & 2 \\ 3 & -1 \end{bmatrix}
  \begin{bmatrix}-1  \\ 1 \end{bmatrix} =
  \begin{bmatrix}3  \\ -2 \end{bmatrix}
$$

and likewise

$$
  \vect{x}_2=  A^{-1}\vect{b}_2= \frac{1}{2}\begin{bmatrix}-4 & 2 \\ 3 & -1 \end{bmatrix}
  \begin{bmatrix}2  \\ 10 \end{bmatrix} =
  \begin{bmatrix}6  \\ -2 \end{bmatrix}.
$$

::::::

A note of **warning**: the proof of {prf:ref}`Prop:SolutionViaInverse`
is based on the **existence** of the inverse of the matrix $A$. Beware of this: never start using the expression $A^{-1}$ unless you have made sure first that the matrix $A$ is indeed invertible.
If not, you may lead yourself into inconsistencies like in the following
example.

::::::{prf:example}
:label: Ex:MatrixInv:FallaciousProof

What goes wrong in the following 'proof' of the statement:

$$
\text{ if } \quad A^2 = A  \quad\text{ and }  \quad A\neq O,   \quad\text{ then }  \quad
A = I.
$$

'Fallacious proof':

Assume $A^2 = A$.

Then

$$
   A^{-1}A^2 = A^{-1}A = I.
$$

On the other hand

$$
   A^{-1}A^2 = A^{-1}(A\,A) = (A^{-1}A)A = IA = A.
$$

So

$$
   I = A^{-1}A^2  = A,
$$

which 'proves' that $A=I$.

Somewhere something **must** have gone wrong, as the following counterexample shows.

For the matrix $B = \begin{bmatrix} \frac12 & \frac12 \\ \frac12 & \frac12  \end{bmatrix}$

it can be checked that

$$
   B^2 = B,
$$

whereas obviously

$$
   B \neq O, \quad B \neq I.
$$

So, where exactly did it go wrong?!

::::::

The next proposition contains a few rules to manipulate inverse matrices.

::::::{prf:proposition}
:label: Prop:MatrixInv:ElemProperties

If $A$ is invertible and $c \neq 0$, then the following is true

<ol type="i">
<li>

The matrix $cA$ is invertible, and

$$
   (cA)^{-1} = \dfrac1c A^{-1}.
$$

</li>
<li id="Item:MatrixInv:TransposeInverse">

The matrix $A^T$ is invertible, and

$$
      (A^T)^{-1} = (A^{-1})^T.
$$

</li>
<li>

The matrix $A^{-1}$ is invertible, and

$$
     (A^{-1})^{-1} = A.
$$

</li>
</ol>

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:MatrixInv:ElemProperties`
:class: tudproof

All statements can be proved by verifying that the relevant products are equal to $I$.

<ol type="i">
<li>

The matrix $A^{-1}$ exists, and so does $\dfrac1c A^{-1}$. We find:

$$
   (cA) \cdot \dfrac1c A^{-1} = c\cdot \dfrac1c A\cdot A^{-1} = 1 \cdot I = I,
$$

and likewise $\dfrac1c A^{-1}\cdot (cA) = I$,

which proves that indeed $\dfrac1c A^{-1} = (cA)^{-1}$.

</li>

<li>

Since it is given that $A^{-1}$ exists we can proceed as follows, where we make use of the characteristic property
$ B^TA^T = (AB)^T$.

$$
(A^{-1})^TA^T = ( AA^{-1})^T = I^T = I
$$

and

$$
A^T(A^{-1})^T =( A^{-1}A)^T = I^T = I,
$$

which settles the second statement.

</li>

</ol>

To prove iii., see {numref}`Exc:MatrixInv:Ainvinv`.

::::::

::::::{exercise}
:label: Exc:MatrixInv:Ainvinv

Prove the last statement of the previous proposition.

::::::

::::::{admonition} Solution to&nbsp;{numref}`Exc:MatrixInv:Ainvinv`
:class: solution, dropdown

For the inverse $C = (A^{-1})^{-1}$ of $A^{-1}$, it should hold that

$$
 CA^{-1} = A^{-1}C = I.
$$

The matrix $C = A$ has these properties.

::::::

The next example gives an illustration of [ii.](#Item:MatrixInv:TransposeInverse) in {prf:ref}`Prop:MatrixInv:ElemProperties`.

::::::{prf:example}
:label: Ex:MatrixInv:TransposeInverse

We consider the matrix

$$
   A =  \begin{bmatrix} 2 & 6 & 5  \\ 0 & 2 & 2 \\ 0 & 0 & 3 \end{bmatrix}.
$$

It has the inverse matrix

$$
   B = \begin{bmatrix} 1/2 & -3/2 & 1/6  \\ 0 & 1/2 & -1/3 \\ 0 & 0 & 1/3 \end{bmatrix},
$$

which can be checked by showing that $AB$ and $BA$ are equal to $I$.

So $B = A^{-1}$, and $B^T = (A^{-1})^T$.

We also have

$$
  A^TB^T  =  \begin{bmatrix} 2 & 0 & 0  \\ 6 & 2 & 0 \\ 5 & 2 & 3 \end{bmatrix}
  \begin{bmatrix} 1/2 & 0 & 0  \\ -3/2 & 1/2 & 0 \\ 1/6 & -1/3 & 1/3 \end{bmatrix} =
  \begin{bmatrix} 1 & 0 & 0  \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{bmatrix},
$$

as well as $B^TA^T = I$, which proves that $B^T = (A^T)^{-1}$.

As we already saw that $B^T = (A^{-1})^{T}$, the matter is settled:

$$
  (A^{-1})^T =  (A^T)^{-1}.
$$

::::::

The last property we mention and prove is the product rule for the matrix inverse.

::::::{prf:proposition}
:label: Prop:MatrixInv:ProductRule

If $A$ and $B$ are invertible $n \times n$ matrices then the matrix $AB$ is also invertible, and

$$
    (AB)^{-1} = B^{-1}A^{-1}.
$$

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:MatrixInv:ProductRule`
:class: tudproof

Again we just check that the properties of the definition hold.

Suppose that $A$ and $B$ are invertible with inverses $A^{-1}$ and $B^{-1}$.

Then using the associative property we find

$$
  (B^{-1}A^{-1})(AB) = B^{-1}A^{-1}AB =  B^{-1}(A^{-1}A)B = B^{-1}IB = B^{-1}B = I,
$$

and along the same lines

$$
  (AB) B^{-1}A^{-1} = I.
$$

This shows that $B^{-1}A^{-1}$ is indeed the inverse of $AB$.

::::::

::::::{exercise}
:label: Exc:MatrixInv:(AB)Tinv

Is the identity

$$
    ((AB)^T)^{-1} = (A^T)^{-1}(B^T)^{-1}
$$

true or false?

In case it is true, give an argument, when false, give a counterexample.

::::::

::::::{admonition} Solution to&nbsp;{numref}`Exc:MatrixInv:(AB)Tinv`
:class: solution, dropdown

The statement is _true_. <BR>
From the two properties

$$
   (AB)^T = B^TA^T, \quad (AB)^{-1} = B^{-1}A^{-1}
$$

it follows that

$$
    ((AB)^T)^{-1} = (B^TA^T)^{-1} = (A^T)^{-1}(B^T)^{-1}.
$$

::::::

(Subsec:MatrixInverse:ComputeInverse)=

## How to compute the inverse

The construction of the inverse of a matrix was already present implicitly in {prf:ref}`Prop:MatrixInv:InvertibleIndepCols`.

The inverse of the matrix $A$ must satisfy the equation $AX = I$.  
Written out column by column this means that

$$
  AX = I \quad  \iff \quad A[\,\mathbf{x}_1\,\,\mathbf{x}_2\, \ldots\, \mathbf{x}_n\,] = 
  [\,\mathbf{e}_1\,\mathbf{e}_2\, \ldots\, \mathbf{e}_n\,].
$$

For the existence of a solution of this Equation {prf:ref}`Prop:MatrixInv:InvertibleIndepCols` tells us
it is <u>necessary</u> that $A$ has linearly independent columns, and we can furthermore read off that the columns of the matrix
$X$ will be the (unique) solutions of the linear systems

$$
   A\mathbf{x}_k = \mathbf{e}_k,
$$

where $k = 1,2,\ldots, n$.

Let us first focus on this equation by considering a fairly general $3\times 3$ matrix $A$.

::::::{prf:example}
:label: Ex:MatrixInv:SolveAX=I

For the matrix

$$
  A = \begin{bmatrix} 1 & 1 & 4 \\ 1 & -1 & -1 \\ 2 & -2 & -4  \end{bmatrix}
$$

we find the solution $B$ of the matrix equation (which will appear to exist)

$$
  AX = I
$$

and then check whether

$$
 BA = I
$$

also holds. In which case we can truthfully assert that $B = A^{-1}$.

Instead of finding the solution $X$ column by column, which gives three linear systems with the same coefficient matrix,

$$
\left[\begin{array}{rrr|r}1 &  1 & 4  & 1\\1 & -1 & -1 & 0\\2 & -2 & -4 & 0\\\end{array}\right],
\quad
\left[\begin{array}{rrr|r}1 &  1 & 4  & 0\\1 & -1 & -1 & 1\\2 & -2 & -4 & 0\\\end{array}\right],
\quad
\left[\begin{array}{rrr|r}1 &  1 & 4  & 0\\1 & -1 & -1 & 0\\2 & -2 & -4 & 1\\\end{array}\right],
$$

we can solve the three linear systems simultaneously using a combined augmented matrix which we may denote by either

$$
\left[\begin{array}{rrr|r|r|r}1 &  1 & 4  & 1 & 0 & 0\\1 & -1 & -1 & 0 & 1 & 0\\2 & -2 & -4 & 0 & 0 & 1\\\end{array}\right]
\quad \text{or} \quad
\left[\begin{array}{rrr|rrr}1 &  1 & 4  & 1 & 0 & 0\\1 & -1 & -1 & 0 & 1 & 0\\2 & -2 & -4 & 0 & 0 & 1\\\end{array}\right]= \left[\, A \rule[-1.5ex]{0ex}{4ex}\,\,\,\,\rule[-.5ex]{0.1ex}{2.5ex}\,\,\rule[-1.5ex]{0ex}{4ex}\,\,I\,\right].
$$

Let us first row reduce this matrix and then draw conclusions:

$$
\left[\, A \rule[-1.5ex]{0ex}{4ex}\,\,\,\,\rule[-.5ex]{0.1ex}{2.5ex}\,\,\rule[-1.5ex]{0ex}{4ex}\,\,I\,\right]=
\left[\begin{array}{rrr|rrr}1 &  1 & 4  & 1 & 0 & 0\\1 & -1 & -1 & 0 & 1 & 0\\2 & -2 & -4 & 0 & 0 & 1
\end{array}\right]\begin{array}{l}
[R_1] \\
{[R_2-1R_1]} \\
{[R_3-2R_1]}
\end{array}
$$

$$
   \sim
\left[\begin{array}{rrr|rrr}1 &  1 & 4  & 1 & 0 & 0\\0 & -2 & -5 & -1 & 1 & 0\\0 & -4 & -12 & -2 & 0 & 1
\end{array}\right]\begin{array}{l}
[R_1+\nicefrac12R_2] \\
{[R_2]} \\
{[R_3-2R_2]}
\end{array}
$$

$$
   \sim
\left[\begin{array}{rrr|rrr}1 &  0 & 3/2  & 1/2 & 1/2 & 0\\0 & -2 & -5 & -1 & 1 & 0\\0 & 0 & -2 & 0 & -2 & 1
\end{array}\right]\begin{array}{l}
[R_1+\nicefrac34R_3] \\
{[R_2-\nicefrac52R_3]} \\
{[R_3]}
\end{array}
$$

$$
 \sim
\left[\begin{array}{rrr|rrr}1 &  0 & 0  & 1/2 & -1 & 3/4\\0 & -2 & 0  & -1 & 6 & -5/2\\0 & 0  & -2  & 0 & -2 & 1
\end{array}\right]\begin{array}{l}
[R_1] \\
{[(-\nicefrac12)R_1]} \\
{[(-\nicefrac12)R_2]}
\end{array}
$$

$$
 \sim
\left[\begin{array}{rrr|rrr}1 &  0 & 0  & 1/2 & -1 & 3/4\\0 & 1 & 0 & 1/2 & -3 & 5/4\\0 & 0 & 1 & 0 & 1 & -1/2
\end{array}\right] = \left[\, I \rule[-1.5ex]{0ex}{4ex}\,\,\,\,\rule[-.5ex]{0.1ex}{2.5ex}\,\,\rule[-1.5ex]{0ex}{4ex}\,\,B\,\right].
$$

By construction we have that the matrix

$$
  B =  \begin{bmatrix}
                1/2 & -1 & 3/4  \\  1/2 & -3 & 5/4  \\ 0 & 1 & -1/2
    \end{bmatrix}
    = \frac14 \begin{bmatrix}
                    2 & -4 & 3 \\ 2 & -12 & 5 \\ 0 & 4 & -2
              \end{bmatrix}
$$

satisfies

$$
  AB = I.
$$

Let us check the product in the other order

$$
  BA =
    \frac14 \begin{bmatrix}
                2 & -4 & 3 \\ 2 & -12 & 5 \\ 0 & 4 & -2
    \end{bmatrix}
    \begin{bmatrix}
              1 &  1 & 4  \\  1 & -1 & -1  \\ 2 & -2 & -4
    \end{bmatrix} =
    \frac14 \begin{bmatrix}
                4 & 0 & 0 \\0 & 4 & 0 \\ 0 & 0 & 4
    \end{bmatrix} = I.
$$

So indeed we can conclude

$$
  \begin{bmatrix}
              1 &  1 & 4  \\  1 & -1 & -1  \\ 2 & -2 & -4
    \end{bmatrix}^{-1} \,=\,
    \frac14 \begin{bmatrix}
                2 & -4 & 3 \\ 2 & -12 & 5 \\ 0 & 4 & -2
    \end{bmatrix}\,.
$$

::::::

Now was this just beginners' luck?
It wasn't, as the next proposition shows.

::::::{prf:proposition}
:label: Prop:MatrixInv:Algorithm

A square matrix $A$ is invertible if and only it has linearly independent columns.

In that case the inverse can be found by reducing the matrix

$$
    \left[\, A \rule[-1.5ex]{0ex}{4ex}\,\,\,\,\rule[-.5ex]{0.1ex}{2.5ex}\,\,\rule[-1.5ex]{0ex}{4ex}\,\,I\,\right]
$$

to the reduced echelon form

$$
   \left[\, I \rule[-1.5ex]{0ex}{4ex}\,\,\,\,\rule[-.5ex]{0.1ex}{2.5ex}\,\,\rule[-1.5ex]{0ex}{4ex}\,\,B\,\right],
$$

and then

$$
   B = A^{-1}.
$$

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:MatrixInv:Algorithm`
:class: tudproof

We have already seen ({prf:ref}`Prop:MatrixInv:InvertibleIndepCols`) that an invertible matrix has  linearly independent columns,
which implies that the reduced echelon form of $A$ is indeed the identity matrix. It is then clear that via row operations we get

$$
  \left[\, A \rule[-1.5ex]{0ex}{4ex}\,\,\,\,\rule[-.5ex]{0.1ex}{2.5ex}\,\,\rule[-1.5ex]{0ex}{4ex}\,\,I\,\right]\sim \quad .\,.\,.\,.\,. \quad \sim
  \left[\, I \rule[-1.5ex]{0ex}{4ex}\,\,\,\,\rule[-.5ex]{0.1ex}{2.5ex}\,\,\rule[-1.5ex]{0ex}{4ex}\,\,B\,\right],
$$

where the matrix $B$ satisfies $AB = I$.

What we have to show is that

$$
  BA = I
$$

as well.

To understand that this is indeed true, we recall ({prf:ref}`Dfn:MatrixOps:ElementaryMatrix`) that row operations can be effectuated via multiplications with elementary matrices. Furthermore, since the matrix product is defined column by column, i.e.

$$
    MX = M\left[\begin{array}{cccc}\mathbf{x_1} &\mathbf{x_2} &\ldots &\mathbf{x_p} \end{array}\right]=
        \left[\begin{array}{cccc}M\mathbf{x_1} &M\mathbf{x_2} &\ldots &M\mathbf{x_p} \end{array}\right],
$$

we also have

$$

  E\left[\, A_1 \,\, \rule[-.5ex]{0.1ex}{2.5ex}\,\,\,A_2\,\right]=
   \left[\, EA_1 \,\, \rule[-.5ex]{0.1ex}{2.5ex}\,\,\,\,EA_2\,\right].




$$

A series of $k$ row operations can be mimicked by $k$ multiplications with elementary matrices:

$$
 \begin{array}{ccl}
   \left[\, A \,\, \rule[-.5ex]{0.1ex}{2.5ex}\,\, I\,\right]&\sim&
   \left[\, E_1A \,\, \rule[-.5ex]{0.1ex}{2.5ex}\,\, E_1I\,\right]  \sim
   \left[\,E_2 E_1A \,\, \rule[-.5ex]{0.1ex}{2.5ex}\,\, \,E_2E_1I\,\right]\sim
   \ldots  \sim \\
   &\sim&
   \left[\,E_k\cdots E_2 E_1A \,\,\, \rule[-.5ex]{0.1ex}{2.5ex}\,\,\, E_k\cdots E_2E_1I\,\right]   =
    \left[\, I \,\, \rule[-.5ex]{0.1ex}{2.5ex}\,\,B\,\right].
 \end{array}
$$

So the matrix $B$ that was found as the solution of the matrix equation

$$
  AX = I
$$

is the product of all the elementary matrices by which $A$ is reduced to the identity matrix. Thus we have shown that indeed

$$
  BA = (E_k\cdots E_2 E_1)A = I.
$$

::::::

::::::{prf:remark}
:label: Rem:MatrixInv:RightInvLeftInv

In the proof we in fact showed that for a **square** matrix $A$:

$$
   \text{if} \quad AB = I \quad \text{then} \quad BA = I.
$$

For non-square matrices this statement is not correct. The interested reader is invited to take a look at the last exercises in the Grasple subsection
({numref}`Subsec:MatrixInverse:Grasple`).
%{prf:ref}`grasple_exercise_3_4_23` and {prf:ref}`grasple_exercise_3_4_24`.

::::::

::::::{prf:remark}
If $A$ is not invertible, then the outcome of the row reduction of

$$
    \left[\, A \,\,\rule[-.5ex]{0.1ex}{2.5ex}\,\,\,I\,\right]
$$

will also lead to the correct answer: as soon as it is clear that $A$ cannot be row reduced to $I$ we can conclude that $A$ is not invertible.

::::::

To help understand the above exposition let us run through the whole procedure for a specific matrix .

::::::{prf:example}
:label: Ex:MatrixInverse:InverseInTwoWays

We want to compute the inverse of the matrix

$$
A =  \begin{bmatrix}
              1 &  4  \\  2 & 6
    \end{bmatrix}.
$$

The short way:

$$
 \begin{array}{rcl}
\left[\begin{array}{rr|rr}1 &  4 & 1 &  0\\2 & 6 & 0 & 1
\end{array}\right]
\begin{array}{l}
[R_1] \\
{[R_2-2R_1]} \\
\end{array} \!\!\!
&\sim&
\left[\begin{array}{rr|rr}
    1 &  4 & 1 &  0 \\
    0 & -2 & -2 & 1
\end{array}\right]
\begin{array}{l}
[R_1+2R_2] \\
{[R_2]} \\
\end{array} \\
    &\sim&
\left[\begin{array}{rr|rr}1 &  0 & -3 &  2\\0 & -2 & -2 & 1
\end{array}\right]
\begin{array}{l}
[R_1] \\
{[(-\frac12)R_2]} \\
\end{array} \\
    &\sim&
\left[\begin{array}{rr|rr}1 &  0 & -3 &  2\\0 & 1 & 1 & -\nicefrac12
\end{array}\right]
\end{array}
$$

So:

$$
A^{-1} =
\begin{bmatrix}
  -3 &  2  \\  1 & -\frac12
\end{bmatrix}.
$$

End of story.

To see how the proof of {prf:ref}`Prop:MatrixInv:Algorithm` works for this specific matrix, we will
give a derivation using elementary matrices.

First step: row replacement with the entry on position (1,1) as a first pivot:

$$
  \begin{bmatrix}
              1 &  0  \\  -2 & 1
    \end{bmatrix}\,
\left[\begin{array}{rr|rr}1 &  4 & 1 &  0\\2 & 6 & 0 & 1
\end{array}\right]     \,\,=\,\,
\left[\begin{array}{rr|rr}1 &  4 & 1 &  0\\0 & -2 & -2 & 1
\end{array}\right], \quad E_1 = \begin{bmatrix} 1 &  0  \\  -2 & 1 \end{bmatrix}.
$$

Second step: another row replacement, using the entry on position (2,2) as pivot:

$$
  \begin{bmatrix}
              1 &  2  \\  0 & 1
    \end{bmatrix}\,
\left[\begin{array}{rr|rr}1 &  4 & 1 &  0\\0 & -2 & -2 & 1
\end{array}\right]
     \,\,=\,\,
\left[\begin{array}{rr|rr}1 &  0 & -3 &  2\\0 & -2 & -2 & 1
\end{array}\right], \quad E_2 = \begin{bmatrix} 1 &  2 \\  0 & 1 \end{bmatrix}.
$$

Third step: the scaling of the second row:

$$
  \begin{bmatrix}
              1 &  0  \\  0 & -\nicefrac12
    \end{bmatrix}\,
\left[\begin{array}{rr|rr}1 &  0 & -3 &  2\\0 & -2 & -2 & 1
\end{array}\right]
    \,\,=\,\,
\left[\begin{array}{rr|rr}1 &  0 & -3 &  2\\0 & 1 & 1 & -\nicefrac12
\end{array}\right],\quad E_3 = \begin{bmatrix} 1 &  0  \\   0 & -\nicefrac12 \end{bmatrix}.
$$

All in all

$$
 (E_3E_2E_1)A = \left(\begin{bmatrix}    1 &  0  \\  0 & -\nicefrac12    \end{bmatrix}
    \begin{bmatrix} 1 &  2  \\  0 & 1  \end{bmatrix}
     \begin{bmatrix}  1 &  0  \\  -2 & 1 \end{bmatrix}\right)\,A
     =
      \begin{bmatrix}   -3 &  2  \\  1 & -\nicefrac12  \end{bmatrix}A
     = I,
$$

which reconfirms

$$
   E_3E_2E_1 = A^{-1} = \begin{bmatrix}   -3 &  2  \\  1 & -\tfrac12  \end{bmatrix}.
$$

::::::

::::::{exercise}
:label: Exc:MatrixInv:ConverseProdRule

Prove the following converse of {prf:ref}`Prop:MatrixInv:ProductRule`.

If $A$ and $B$ are $n\times n$ matrices for which the product $AB$ is invertible, then $A$ and $B$ are both invertible.

Make sure that you do not use $A^{-1}$ or $B^{-1}$ prematurely, i.e., before you have established that they exist.

::::::

::::::{admonition} Solution to&nbsp;{numref}`Exc:MatrixInv:ConverseProdRule`
:class: solution, dropdown

Suppose $A$ and $B$ are two $n \times n$ matrices for which $AB$ is invertible. Let $C=(AB)^{-1}$ be the inverse of $AB$. We claim that
$BC$ is the inverse of $A$.

Now since

$$
 A(BC) = (AB)C = AB(AB)^{-1} = I,
$$

it follows from {prf:ref}`Rem:MatrixInv:RightInvLeftInv` that $(BC)A=I$ also holds. So we have

$$
 A(BC) = (BC)A = I,
$$

which means that $A$ is invertible and has as inverse the matrix $BC$.

In the same vein it is shown that $CA$ is the inverse of $B$.

::::::

(Subsec:MatrixInverse:Summary)=

## Characterizations of invertibility

In the previous subsections quite a few properties of invertible matrices came along, either explicitly or implicitly. For future reference we list them in a theorem.

Recall that by definition a (square) matrix $A$ is invertible (or regular) if and only if there exists a matrix $B$ for which

$$
  AB = BA= I.
$$

::::::{prf:theorem}
:label: Thm:MatrixInv:InvertibilityCharacterizations

For an $n\times n$ matrix $A$, the following statements are equivalent.
<br/>
That is, each of the following properties is a characterization of invertibility of a square matrix $A$.

<ol>
<li>

$A$ is invertible;

</li>
<li>

there exists a matrix $B$ for which $AB = I$;

</li>
<li>

for each $\mathbf{b}\in\mathbb{R}^n$ the linear system $A\mathbf{x} = \mathbf{b}$ has a unique solution;

</li>
<li>

$A$ is row equivalent to the identity matrix $I_n$;

</li>
<li>

$A$ has linearly independent columns;

</li>

<li>

the equation $A\vect{x} = \vect{0}$ has only the trivial solution $\vect{x} = \vect{0}$;

</li>

<li>

$A$ can be written as a product of elementary matrices: $A = E_1E_2\cdots E_k$.

</li>
</ol>

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Thm:MatrixInv:InvertibilityCharacterizations`
:class: tudproof

It is a good exercise to find out where the evidence of each characterization is found,
and wherever necessary to fill in the missing details.

::::::

There are many variations on {prf:ref}`Thm:MatrixInv:InvertibilityCharacterizations`.
The following exercise contains a few.

::::::{exercise}
:label: Exc:MatrixInv:LastEquivalencesInvertibility

Show that invertibility of an $n\times n$ matrix $A$ is also equivalent to

<ul>
<li>

there exists a matrix $B$ such that $BA = I$;

</li>
<li>

$A$ has linearly independent rows;

</li>
<li>

each column of the matrix $A$ is a pivot column;

</li>
<li>

the columns of $A$ span the whole $\mathbb{R}^n$.

</li>
</ul>

Again it may very well be that you have to resort to previous sections.

::::::

(Subsec:MatrixInverse:Grasple)=

## Grasple exercises

The first exercises are quite straightfordwardly computational.
The remaining exercises tend to be more theoretic.

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6683a2f9-7b6b-4dd1-bec1-1e8b894fa3bb?id=71086
:label: grasple_exercise_3_4_1
:dropdown:
:description: To compute the inverse of a $2 \times 2$ matrix.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1bbca38b-a734-4049-b8a2-f79d4bf1b098?id=71087
:label: grasple_exercise_3_4_2
:dropdown:
:description: To compute the inverse of a $2 \times 2$ matrix.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/045cd183-ab19-4675-908c-26c41298bade?id=83051
:label: grasple_exercise_3_4_3
:dropdown:
:description: To compute the inverse of a $2 \times 2$ matrix.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/82c06a56-8ee8-4f36-8173-e5d56da1e8e3?id=71073
:label: grasple_exercise_3_4_4  
:dropdown:
:description: To compute  the inverse of a $3 \times 3$ matrix step by step.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/551172d9-861c-4958-9b17-dfa828acdabe?id=71088
:label: grasple_exercise_3_4_5  
:dropdown:
:description: To compute the inverse of a $3 \times 3$ matrix.

::::::
::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9174c68c-e2d5-4c23-af96-e3fe3dd36f42?id=71089
:label: grasple_exercise_3_4_6
:dropdown:
:description: To compute the inverse of a $3 \times 3$ matrix.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/800dc2f9-227e-401b-818b-093fc9647dd9?id=83083
:label: grasple_exercise_3_4_7
:dropdown:
:description: To compute the inverse of a $4 \times 4$ matrix.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9146f49d-74a5-4fda-a641-181c4536fe01?id=83086
:label: grasple_exercise_3_4_8
:dropdown:
:description: To find $p$ for which a matrix $A$ is singular.

::::::

The remaining exercises have more theoretic flavour.

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/677aa3ee-4594-4d77-ace6-583a1efcba59?id=71090
:label: grasple_exercise_3_4_9
:dropdown:
:description: True/False question about invertibility versus consistent linear systems.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f789ebd5-171b-4556-83a9-eefc5ef830ef?id=71092
:label: grasple_exercise_3_4_10
:dropdown:
:description: 'To show: if $A$ is invertible, then so is $A^T$.'

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/29dc7c2f-6636-493e-9c97-da1847a336b7?id=68908
:label: grasple_exercise_3_4_11
:dropdown:
:description: 'To show: if $AB$ is invertible, then so are $A$ and $B$.'

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8f3feb75-b41b-42e0-b574-f6442da253ce?id=70272
:label: grasple_exercise_3_4_12
:dropdown:
:description: What about $(AB)^{-1} = A^{-1}B^{-1}$?

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5185c5c0-4d92-4e0e-92a7-6dc5eed8f7cf?id=68896
:label: grasple_exercise_3_4_13
:dropdown:
:description: What about $((AB)^T)^{-1} = (A^T)^{-1}(B^T)^{-1}$?

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ee4bb61e-6939-4074-a556-b82f3d0e8c28?id=71091
:label: grasple_exercise_3_4_14
:dropdown:
:description: 'True/False: Every elementary matrix is invertible.'
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1732d75b-2027-4a92-b8bb-c98bda62475d?id=71093
:label: grasple_exercise_3_4_15
:dropdown:
:description: 'True/False: If $A$ and $B$ are invertible, then so is $A+B$.'
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f8602d4f-57b7-4752-9edc-69c83069fe36?id=71095
:label: grasple_exercise_3_4_16
:dropdown:
:description: 'True/False: If $A$ and $B$ are singular, then so is $A+B$.'
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a8ea864d-1164-4afc-9a24-c0a126ee8e54?id=71097
:label: grasple_exercise_3_4_17
:dropdown:
:description: 'True/False: If $A$ is row equivalent to $I$, then so is $A^2$. '
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/73a16f62-28d7-4a4c-baf5-7ce3be9272ce?id=71104
:label: grasple_exercise_3_4_18
:dropdown:
:description: To find 'by inspection' inverses of elemenatry matrices.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a8c2b8ed-9961-4779-8841-491a9529b71c?id=71466
:label: grasple_exercise_3_4_19
:dropdown:
:description: To find the inverses of $AE$ and $EA$, when $A^{-1}$ is given.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/dfe429bd-1ab9-47f7-8f6c-06150c468645?id=71468
:label: grasple_exercise_3_4_20
:dropdown:
:description: Finding the inverses of (almost) elementary matrices.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9af5928a-7ecb-478e-a896-7c66d16d9d09?id=71463
:label: grasple_exercise_3_4_21
:dropdown:
:description: Distilling $A^{-1}$ from a relation $c_2A^2 + c_1A + c_0I = 0$.
::::::

In the last two exercises (non-)invertibility of non-square matrices is considered.

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ca504661-cc62-454f-8035-04a9bef85f91?id=61170
:label: grasple_exercise_3_4_22
:dropdown:
:description: To explore invertibility for a $2\times 3$ matrix.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4e9b4ec1-f775-430f-b81f-c76c42fcbc76?id=60136
:label: grasple_exercise_3_4_23
:dropdown:
:description: To explore invertibility for a $3\times 2$ matrix.
::::::
