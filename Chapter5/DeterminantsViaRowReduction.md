# Determinants via Row Reduction

In this section we will first consider the effect of row operations on the value of a determinant.
This leads the way to a more efficient way to compute $n\times n$ determinants.

It also leads the way to two very important properties of determinants, namely

<ul>
<li>

The product rule: $\det{(AB)} = \det{A}\cdot\det{B}$.

</li>
<li>

The matrix $A$ is invertible if and only if $\det{A} \neq 0$ .

</li>
</ul>

We have seen in {numref}`Sec:DeterminantsViaCofactors` that the cofactor expansion of an $n \times n$ determinant works best using a row (or a column) with many, preferably $n-1$, zeros. When solving a linear system, or finding the inverse of a matrix, we have seen how to create zeros via row reduction. The important thing: row reducing an augmented matrix does not alter the solution(s) of the corresponding linear system. The next proposition
describes the effect of row operations on a determinant.

::::::{prf:proposition} How row operations affect a determinant
:label: Prop:DetRowReduction:RowOps

For the determinant of an $n\times n$ matrix $A$ the following rules apply.

<ol type = "i">
<li>

If a row of $A$ is scaled with a factor $c$, the determinant is scaled with a factor $c$.

</li>
<li>

If a multiple of one row of $A$ is added to another row, the determinant does not change.

</li>
<li>

When two rows of $A$ are swapped, the determinant changes sign.

</li>
</ol>

::::::

We postpone the proof till the end of this section and first look at examples and a few consequences.

::::::{prf:example}
:label: Ex:DetRowReduction:RowOps

The following identities show what happens with a $4\times 4$ determinant when

<ol type="i">
<li >

the second row is scaled with a factor $c$:

$$
\left|\begin{array}{rrrr}
a_{11} &a_{12} &a_{13} &a_{14}  \\
ca_{21} &ca_{22} &ca_{23} &ca_{24}  \\
a_{31} &a_{32} &a_{33} &a_{34}  \\
a_{41} &a_{42} &a_{43} &a_{44}
\end{array} \right| = c \left|\begin{array}{rrrr}
a_{11} &a_{12} &a_{13} &a_{14}  \\
a_{21} &a_{22} &a_{23} &a_{24}  \\
a_{31} &a_{32} &a_{33} &a_{34}  \\
a_{41} &a_{42} &a_{43} &a_{44}
\end{array} \right|,
$$

</li>
<li>

the first row is added $(-k)$ times to the third row:

$$
\left|\begin{array}{llll}
a_{11} &a_{12} &a_{13} &a_{14}  \\
a_{21} &a_{22} &a_{23} &a_{24}  \\
a_{31}-ka_{11} &a_{32}-ka_{12} &a_{33}-ka_{13} &a_{34}-ka_{14}  \\
a_{41} &a_{42} &a_{43} &a_{44}
\end{array} \right| =  \left|\begin{array}{rrrr}
a_{11} &a_{12} &a_{13} &a_{14}  \\
a_{21} &a_{22} &a_{23} &a_{24}  \\
a_{31} &a_{32} &a_{33} &a_{34}  \\
a_{41} &a_{42} &a_{43} &a_{44}
\end{array} \right|,
$$

</li>
<li>

the first and the fourth row are swapped:

$$
\left|\begin{array}{rrrr}
a_{41} &a_{42} &a_{43} &a_{44} \\
a_{21} &a_{22} &a_{23} &a_{24}  \\
a_{31} &a_{32} &a_{33} &a_{34}  \\
a_{11} &a_{12} &a_{13} &a_{14}
\end{array} \right| = - \left|\begin{array}{rrrr}
a_{11} &a_{12} &a_{13} &a_{14}  \\
a_{21} &a_{22} &a_{23} &a_{24}  \\
a_{31} &a_{32} &a_{33} &a_{34}  \\
a_{41} &a_{42} &a_{43} &a_{44}
\end{array} \right|.
$$

</li>
</ol>

::::::

Note that these properties can be expressed using elementary matrices (cf. {numref}`Sec:MatrixOps`) .

::::::{prf:example}
:label: Ex:DetRowReduction:ElementaryMatrices

Let $A$ be an arbitrary $4\times 4$ matrix, and $E_1, E_2$ and $E_3$ the elementary matrices corresponding to the row operations in {prf:ref}`Ex:DetRowReduction:RowOps`. So

$$
E_1 = \left[\begin{array}{cccc} 1 & 0 & 0 & 0 \\ 0 & c & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1
\end{array} \right]
, \quad
E_2 = \left[\begin{array}{cccc} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ -k & 0 & 1 & 0 \\ 0 & 0 & 0 & 1
\end{array} \right]
, \quad
E_3 = \left[\begin{array}{cccc} 0 & 0 & 0 & 1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0
\end{array} \right]
.
$$

Then we have

$$
\det{(E_1A)} = c \det{A}, \quad \det{(E_2A)} = \det{A}, \quad \det{(E_3A)} = -\det{A}.
$$

Since

$$
\det{E_1} = c, \quad \det{E_2} = 1, \quad \det{E_3} = -1,
$$

we see that in all three cases we have that

:::{math}
:label: Eq:DetRowReduction:ElementaryMatrices

\det{(E_iA)} = \det{E_i} \cdot \det{A}.

:::

These are the basics for the general product rule we will see later, that states that

$$
\text{det}(AB) = \text{det}(A) \text{det} (B)
$$

for _arbitrary_ $n\times n$ matrices $A$ and $B$.

::::::

The next two examples illustrate the practical use of the three rules involving row operations.

::::::{prf:example}
:label: Ex:DetRowReduction:DetByRowRed1

$$
\left|\begin{array}{rrr}  5 & 10 & 15 \\ 3 & 8 & 6 \\ 2 & -2 & 5 \end{array} \right|\stackrel{(1)}{=} 5 \left|\begin{array}{rrr}  1 & 2 & 3 \\ 3 & 8 & 6 \\ 2 & -2 & 5 \end{array} \right|\stackrel{(2)}{=} 5 \left|\begin{array}{rrr}  1 & 2 & 3 \\ 0 & 2 & -3 \\ 0 & -6 & -1 \end{array} \right|\stackrel{(3)}{=} 5 \cdot 1 \cdot \left|\begin{array}{rr}  2 & -3 \\ -6 & -1 \end{array} \right|.
$$

The steps involved are:

:::{paren-list}
:start: 1

- take out a factor $5$ from the first row,
- subtract the first row $3$ times from the second row and $2$ times from the third row (or: add it $(-3)$ times and $(-2)$ times respectively)
- expand along the first column.

:::

Evaluating the $2\times 2$ determinant at the end leads to the answer $-100$.

Can you describe the row operations and cofactor expansions in the following computation?

$$
\begin{array}{rcl}
\left|\begin{array}{rrrr}  3 & 2 & 4 & 3 \\ 1 & 2 & 3 & -1 \\ 4&3&8&2 \\ 2&5&7&-4  \end{array} \right|&=& \left|\begin{array}{rrrr}  0 & -4 & -5 & 6 \\ 1 & 2 & 3 & -1 \\ 0 & -5 & -4 & 6  \\0 &1 & 1 & -2  \end{array} \right|= (-1)\cdot  \left|\begin{array}{rrr}   -4 & -5 & 6 \\ -5 & -4 & 6  \\ 1 & 1 & -2  \end{array} \right| \\
&=& (-1)\cdot  \left|\begin{array}{rrr}   0 & -1 & -2  \\ 0 & 1 & -4  \\ 1 & 1 & -2  \end{array} \right|= - \left|\begin{array}{rr}    -1 & -2  \\  1 & -4   \end{array} \right| = -6.
\end{array}
$$

::::::

::::::{prf:remark}
:label: Rem:DetRowReduction:ColumnOperations

Because of {prf:ref}`Prop:DetCofactors:DetTranspose` that states

$$
\det{A} = \text{det}\big(A^T\big)
$$

every rule involving row operations may be transformed into a rule about column operations. It is here that computing a determinant differs strikingly from the reduction of an (augmented) matrix to an echelon matrix. Another, more subtle difference is that
a row operation applied to a matrix leads to an **equivalent** matrix, which we denote by the symbol $\sim$, whereas row or column operations on a determinant give **equal values** all the time. So then we write $=$.

::::::

In the next example column operations are used.

::::::{prf:example}

$$
\left|\begin{array}{rrrr}   1 & 1 & 1 & -1 \\ 2 & 4 & 5 & 3   \\4 & 5 & 2 & -1 \\ 5 & 7 & 4 & -2 \end{array} \right|=
\left|\begin{array}{rrrr}   1 & 0 & 0 & 0 \\ 2 & 2 & 3 & 5   \\4 & 1 & -2 & 3 \\ 5 & 2 & -1 & 3 \end{array} \right|=
\left|\begin{array}{rrr}    2 & 3 & 5   \\ 1 & -2 & 3 \\ 2 & -1 & 3 \end{array} \right|= \ldots
$$

And do you see what is happening here?

$$
\left|\begin{array}{rrrr}   1 & 2 & 3 & 4 \\ -2 & 2 & 0 & 0   \\ -1 & 0 & 1 & 0 \\ -5 & 0 & 0 & 5  \end{array} \right|=
\left|\begin{array}{rrrr}  10& 2 & 3 & 4 \\ 0 & 2 & 0 & 0   \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 5  \end{array} \right|=
10 \left|\begin{array}{rrrr}   2 & 0 & 0   \\  0 & 1 & 0 \\  0 & 0 & 5  \end{array} \right|= 100.
$$

::::::

An interesting consequence of rule (3) of {prf:ref}`Prop:DetRowReduction:RowOps` is the following.

::::::{prf:corollary}
:label: Cor:DetRowReduction:EqualRows

If a matrix $A$ has two equal rows (or columns), then $\det{A} = 0$.

::::::

::::::{prf:proof}

Suppose the $i$th and the $j$th row of $A$ are equal, and let $\det{A} = d$. Let $B$ be the matrix $A$ with the $i$th and $j$th row interchanged.

On the one hand, $B = A$, so

$$
  \det{B} = \det{A} = d,
$$

on the other hand, because of {prf:ref}`Prop:DetRowReduction:RowOps`, Rule 2, we have

$$
 \det{B} = -\det{A} = -d.
$$

We may conclude $d = -d$, which is only possible if

$$
 d = \det{A} = 0.
$$

::::::

::::::{exercise}
:label: Exc:DetRowReduction:EqualRows

Give an alternative proof of {prf:ref}`Cor:DetRowReduction:EqualRows` using Rule i. and Rule ii. of {prf:ref}`Prop:DetRowReduction:RowOps`.

::::::

::::::{solution} Exc:DetRowReduction:EqualRows
:class: dropdown

Suppose $A$ is a matrix with two equal rows, say row $i$ and row $j$ are equal.

If we subtract the $i$th row from the $j$th row, we get a matrix $A_2$ with $j$th row equal to zero, and with det$(A_2) = $ det$(A)$. If we take the factor $0$ out, we see that det$(A_2) = 0$.

For instance, with a $4\times 4$ matrix with equal second and fourth row we would have

$$
  \begin{vmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\
                  \color{blue}a_{21} & \color{blue}a_{22} & \color{blue}a_{23} & \color{blue}a_{24} \\
                  a_{31} & a_{32} & a_{33} & a_{34} \\
                  \color{blue}a_{21} & \color{blue}a_{22} & \color{blue}a_{23} & \color{blue}a_{24}
                  \end{vmatrix} =
                  \begin{vmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\
                  a_{21} & a_{22} & a_{23} & a_{24} \\
                  a_{31} & a_{32} & a_{33} & a_{34} \\
                  \color{blue}0 & \color{blue}0 &\color{blue} 0 & \color{blue}0
                  \end{vmatrix} =
                  {\color{blue}0}\begin{vmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\
                  a_{21} & a_{22} & a_{23} & a_{24} \\
                  a_{31} & a_{32} & a_{33} & a_{34} \\
                  \ast & \ast &\ast &\ast
                  \end{vmatrix} = 0.
$$

::::::

With the knowledge built so far we can show the important property that was already hinted at in {numref}`Sec:DeterminantsViaCofactors`.

::::::{prf:theorem}
:label: Thm:DetRowReduction:Invertibility

For any square matrix $A$:

$$
   A \,\,\text{is invertible} \quad \iff \quad  \det{A} \neq 0.
$$

::::::

The proof is -- we think -- quite instructive.

::::::{prf:proof}

In the previous section we have already seen that the statement is true for triangular matrices.

Now suppose $A$ is any $n \times n$ matrix. Via row reduction $A$ can be brought to echelon form $F$,
and for a square matrix the echelon form is an upper triangular matrix (with possibly zeros on the diagonal).

From {prf:ref}`Prop:DetCofactors:InvertibleTriangular` we know that for a triangular matrix $F$ we have <BR>
'$F$ is invertible' is equivalent to '$\det{F} \neq 0$'.

The row operations transforming $A$ to $F$ can be performed by multiplications with elementary matrices $E_1, \ldots E_k$.

We have seen (Equation {eq}`Eq:DetRowReduction:ElementaryMatrices` in {prf:ref}`Ex:DetRowReduction:ElementaryMatrices`)
that

$$
\det{(E_iA)} = \det{E_i} \cdot \det{A}.
$$

Furthermore, the determinant of an elementary matrix is nonzero. Namely, for a row scaling it is equal to $c$, for a row swap it is equal to $(-1)$, and for adding a multiple of a row to another row it is equal to $1$.
Hence, if $m$ of the row operations are row scalings and $\ell$ of the row operations are row swaps, then

$$
\det{\left(E_kE_{k-1}\cdots E_1A\right)}=  c_1\cdots c_m \cdot (-1)^{\ell} \det{A}  = \alpha \det{A},
$$

with $\alpha \neq 0$.

So if $E_kE_{k-1}\cdots E_1A = F$, where $F$ is an echelon matrix, we see that

$$
\det{A} \neq 0  \quad \iff \quad  \det{F}\neq 0.
$$

We conclude that

$$
  A \,\text{is invertible}  \,\,\iff\,\, F \,\text{is invertible} \,\,\iff\,\, \det{F}  \neq 0\,\,\iff\,\,  \det{A} \neq 0.
$$

::::::

::::::{prf:theorem}
:label: Eq:DetRowReduction:ProductRule

For two $n\times n$ matrices $A$ and $B$ it always holds that

$$
\det{(AB)} = \det{A}\cdot\det{B}
$$

::::::

::::::{prf:proof}

We already know that the identity holds if $A$ is an elementary matrix.
It will also hold if $A$ is not invertible, as in that case $AB$ is also not invertible,
and we know that the determinant of any non-invertible matrix is zero. So then

$$
\det{(AB)} = 0 = \det{A}\cdot\det{B}.
$$

Hence suppose that the matrix $A$ is invertible. In that case (cf. {prf:ref}`Thm:MatrixInv:InvertibilityCharacterizations`) $A$ can be written as a product of elementary matrices.

$$
A = E_1E_2\ldots E_k.
$$

So then, step by step we find that

$$
\begin{array}{rl}
\det{A}  & = \det{(E_1E_2\cdots E_k)} = \det{(E_1(E_2\cdots E_k))} =  \\
& = \det{E_1} \det{(E_2\cdots E_k)}  = \ldots = \det{E_1} \det{E_2} \cdots \det{E_k},
\end{array}
$$

and also

$$
\begin{array}{rl}
\det{(AB)} & =  \det{(E_1E_2\cdots E_kB)} = \det{E_1} \det{(E_2\cdots E_kB)}  \\
& = \ldots = \\
& = \det{E_1} \det{E_2} \cdots \det{E_k} \det{B} \\
& = \det{A}\det{B}.
\end{array}
$$

::::::

::::::{prf:corollary}
:label: Cor:DetRowReduction:DetOfInverse

If the matrix $A$ is invertible, then $\text{det}\big(A^{-1}\big)= \dfrac{1}{\det{A}}$.

::::::

::::::{prf:proof}

We can combine the three properties

i. $AA^{-1} = I$, &nbsp; ii. $\det{(AA^{-1})} = \det{A}\det{\left(A^{-1}\right)}$
&nbsp; and &nbsp; iii. $\det{I} = 1$.

As follows:

$$
\text{det}(A)\text{det}\left(A^{-1}\right)
 =  \text{det}(AA^{-1}) = \text{det}(I) = 1,
$$

so indeed

$$
\text{det}\left(A^{-1}\right)
  = \dfrac{1}{\text{det}(A)}.
$$

::::::

::::::{exercise}
:label: Exc:DetRowReduction:PropNonProp

For each of the following statements decide whether they are true or false. In case true, give an argument, in case false, give a counterexample.

<ol type = "a">

<li>

For each $n \times n$ matrix $A$ it holds that

<BR>

$$
\text{det}\big(A^k\big)= \big(\det{A}\big)^k.
$$

</li>
<li>

For each two $n \times n$ matrices $A$ and $B$ it holds that

<BR>

$$
\det{(A+B)} = \det{A}+\det{B}.
$$

</li>
<li>

For each $n \times n$ matrix $A$ it holds that

<BR>

$$
\det{(-A)} = -\det{A}.
$$

</li>
</ol>

::::::

::::::{solution} Exc:DetRowReduction:PropNonProp
:class: dropdown

We treat the statements one by

<ol type = "a">

<li>

For each $n \times n$ matrix $A$ it holds that

<BR>

$$
\text{det}\big(A^k\big)= \big(\det{A}\big)^k.
$$

This is true, and follows from repeatedly using the property $\det(AB) = \det(A)\det(B)$. Namely,

<BR>

$$
  \det(A^k) = \det(A\cdot A \cdot A \cdots A) =
  \det(A)\cdot\det(A)\cdot\det(A)\cdots\det(A).
$$

</li>
<li>

For each two $n \times n$ matrices $A$ and $B$ it holds that

<BR>

$$
\det{(A+B)} = \det{A}+\det{B}.
$$

This statement is false. A trivial counterexample is given by $A = B = I_n$, for $n \geq 2$. Namely, for these matrices we see that

<BR>

$$
  \det{A} + \det{B} = 1 + 1 = 2 \neq \det{(A+B)} = \det{(2I)} = 2^n.
$$

</li>
<li>

For each $n \times n$ matrix $A$ it holds that

<BR>

$$
\det{(-A)} = -\det{A}.
$$

This is not true in general. The correct statement would be: for an $n \times n$ matrix $A$ <BR>

$$
  \det{(-A)} = (-1)^n\det{(A)}.
$$

One way to see this is true is to write $-A = (-I)A$ and use the product rule ({prf:ref}`Eq:DetRowReduction:ProductRule`).

</li>
</ol>

::::::

We will conclude this section, for the interested reader, with a proof of the properties of {prf:ref}`Prop:DetRowReduction:RowOps`.
In fact we will prove the column version, and we add one related rule that will be of use both immediately in the proof and also later on.

::::::{prf:proposition}
:label: Prop:DetRowReduction:SumofCols

Suppose $A$ is an $n\times n$ matrix for which the $k$th column is the sum of two vectors in $\R^n$. So

$$
\vect{a}_k = \vect{b} +\vect{c}.
$$

Then

:::{math}
:label: Eq:DetExtras:SumofCols

\begin{array}{l}
\det{[\vect{a}_1 \,\, \ldots \,\, \vect{b}+\vect{c} \,\, \ldots \,\, \vect{a}_n]} = \\
\qquad \qquad \qquad \det{[\vect{a}_1 \,\, \ldots \,\, \vect{b} \,\, \ldots \,\, \vect{a}_n]} +
\det{[\vect{a}_1 \,\, \ldots \,\, \vect{c} \,\, \ldots \,\, \vect{a}_n]}
\end{array}

:::

::::::

So, click here for the proof of {prf:ref}`Prop:DetRowReduction:RowOps` and {prf:ref}`Prop:DetRowReduction:SumofCols`.

::::::{prf:proof}

For typographical reasons we will prove the three rules stated as column operations.
For an $n \times n$ matrix

$$

 A = [\vect{a}_1 \,\,\vect{a}_2  \,\,\ldots\,\, \vect{a}_n]
$$

the rules can then be formulated as

:::{paren-list}
:start: 1

- $\det{[\vect{a}_1   \,  \vect{a}_2  \,  \ldots \, c \vect{a}_k  \,    \ldots  \,   \vect{a}_n]} = c  \det{A}$;

- $\det{[\vect{a}_1  \,  \ldots  \,   \vect{a}_k  \,    \ldots  \,   \vect{a}_j  \,   \ldots \,   \vect{a}_n]} = - \det{A}$;

- $\det{[\vect{a}_1 \,  \ldots   \,  \vect{a}_j   \,   \ldots  \,   \vect{a}_k + c\vect{a}_j  \,  \ldots  \,  \vect{a}_n]} = \det{A}$.

:::

So, let us consider them one by one.

:::{paren-list}
:start: 1

- If a column is scaled with a factor $c$, then the determinant is also scaled with a factor $c$.

:::

Suppose $\tilde{A}$ is the result of scaling the $k$th column of $A$ with a factor $c$.
Then expanding det$(\tilde{A})$ along its $k$th column, keeping in mind that $\tilde{a}_{ik} = c {a}_{ik}$ and $\tilde{A}_{ik} = {A}_{ik}$, yields

$$
\text{det}\big(\tilde{A}\big)= \sum_{i=1}^n   (-1)^{i+k} \tilde{a}_{ik}\det{\tilde{A}_{ik}}
=\sum_{i=1}^n   (-1)^{i+k} c {a}_{ik}\det{{A}_{ik}}.
$$

If we take out the constant factor $c$ we see that

$$
\text{det}\big(\tilde{A}\big) =  c\sum_{i=1}^n   (-1)^{i+k}  {a}_{ik}\det{{A}_{ik}}
= c  \det{A}.
$$

{prf:ref}`Prop:DetRowReduction:SumofCols` is proved in much the same way as rule (1) by expansion along the $k$th column.

:::{paren-list}
:start: 2

- The proof of the swapping rule is more involved.

:::

One way to set about is

<ul>
<li>

first settle the rule when the first two columns are interchanged;

</li>
<li>

next consider the swapping of two arbitrary _consecutive_ columns;

</li>
<li>

finally note that any column swap is the result of an _odd_ number of swaps of consecutive columns.

</li>
</ul>

We will consider the swapping of the first two columns in complete detail. Let $A^{\ast}$ be the result of swapping the first two columns of the matrix $A$. The crucial thing to note here is that, for each value of $i$,

$$
a_{i2}^{\ast} = a_{i1} \quad \text{and} \quad  A_{i2}^{\ast} = A_{i1}.
$$

To make this explicit for a $4\times 4$ matrix:

$$
\begin{array}{ccc}
A = \left[\begin{array}{rrrr}
a_{11} &a_{12} &a_{13} &a_{14}  \\
a_{21} &a_{22} &a_{23} &a_{24}  \\
a_{31} &a_{32} &a_{33} &a_{34}  \\
a_{41} &a_{42} &a_{43} &a_{44}
\end{array} \right]
& \Longrightarrow &
A^{\ast} = \left[\begin{array}{rrrr}
a_{12} &a_{11} &a_{13} &a_{14}  \\
a_{22} &a_{21} &a_{23} &a_{24}  \\
a_{32} &a_{31} &a_{33} &a_{34}  \\
a_{42} &a_{41} &a_{43} &a_{44}
\end{array} \right]
 \\
\Big\Downarrow && \Big\Downarrow  \\
A_{3,1} = \left[\begin{array}{rrr}
a_{12}  &a_{13} &a_{14}  \\
a_{22}  &a_{23} &a_{24}  \\
a_{42}  &a_{43} &a_{44}
\end{array} \right]
  &= &
A_{3,2}^{\ast} = \left[\begin{array}{rrr}
a_{12}  &a_{13} &a_{14}  \\
a_{22}  &a_{23} &a_{24}  \\
a_{42}  &a_{43} &a_{44}
\end{array} \right]
.
\end{array}
$$

Expanding det$(A^{\ast})$ along its second column yields

$$
\text{det}\big(A^{\ast} \big)= \sum_{i=1}^n   (-1)^{i+2}  a_{i2}^{\ast}\text{det}\big(A_{i2}^{\ast} \big)=
\sum_{j=1}^n   (-1)^{i+2}  {a}_{i1}\text{det}\big({A}_{i1}\big).
$$

Noting that $(-1)^{i+2} = (-1)\cdot (-1)^{i+1}$ and taking out the common factor $(-1)$ from the sum yields

$$
\text{det}\big(A^{\ast} \big)=
- \sum_{i=1}^n   (-1)^{i+1}  {a}_{i1}\text{det}\big({A}_{i1}\big)=
- \text{det}\big({A}\big).
$$

The same argument works for the interchanging of two arbitrary consecutive columns.
<BR> As stated the swapping of two arbitrary columns can be accomplished via an odd number of 'consecutive swaps', so then the determinant changes sign an odd number of times.
And for an odd number $n$ we have that $(-1)^n = -1$. <BR>
Convince yourself of this!

Lastly we have to prove

:::{paren-list}
:start: 3

- If the multiple of one column of $A$ is added to another column, the determinant does not change.

:::

First Rule (2) implies, as in {prf:ref}`Cor:DetRowReduction:EqualRows`, that a determinant with two equal columns has the value 0.

We then proceed as follows for Rule (3):

$$
\begin{array}{l}
\det{[\vect{a}_1  \,  \ldots \,    \vect{a}_j  \,    \ldots  \,   \vect{a}_k + c\vect{a}_j   \, \ldots  \,  \vect{a}_n]} = \\
\quad =
\det{[\vect{a}_1  \,  \ldots  \,  \vect{a}_j   \,  \ldots  \,   \vect{a}_k  \,  \ldots  \,  \vect{a}_n]} +
\det{[\vect{a}_1   \, \ldots  \,   \vect{a}_j  \,    \ldots   \,   c \vect{a}_j    \,\ldots  \,  \vect{a}_n]}  \\
\quad =
\det{[\vect{a}_1 \,   \ldots  \,   \vect{a}_j  \,   \ldots  \,   \vect{a}_k  \,  \ldots  \,  \vect{a}_n]} +
c \det{[\vect{a}_1  \,  \ldots  \,   \vect{a}_j   \,   \ldots  \,    \vect{a}_j  \,  \ldots  \,  \vect{a}_n]}\\
\quad =
\det{[\vect{a}_1  \,  \ldots \,    \vect{a}_j  \,   \ldots   \,  \vect{a}_k  \,  \ldots   \, \vect{a}_n]} + 0.
\end{array}
$$

This settles all matters.

::::::
