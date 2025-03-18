(Sec:SubspacesRn)=

# Subspaces of $\R^n$

## Introduction

Subspaces are structures that appear in many different subfields of linear algebra.
For instance, they appear as solution sets of homogeneous systems of linear equations, and as ranges of linear transformations, to mention two situations that we have already come across.
In this section we will define them and analyze their basic properties. In {numref}`Sec:BasisDim` we will consider the important attributes basis and dimension.

## Definition of Subspace and Basic Properties

::::::{prf:definition}
:label: Dfn:Subspaces:Subspace

A (**linear**) **subspace** of $\R^n$ is a subset $S$ of $\R^n$ with the following three properties:

<ol type = "i">

<li>

$S$ contains the zero vector.

</li>
<li>

If two vectors $\vect{u}$ and $\vect{v}$ are in $S$, then their sum is in $S$ too:

<br>

$$
\vect{u} \in S,  \vect{v} \in S \quad \Longrightarrow \quad
\vect{u}+ \vect{v} \in S.
$$

</li>
<li>

If a vector $\vect{u}$ is in $S$, then every scalar multiple of $\vect{u}$ is in $S$ too:

<br>

$$
\vect{u} \in S,  c \in \R \quad \Longrightarrow \quad
c\vect{u} \in S.
$$

</li>
</ol>

::::::

::::::{prf:remark}

Property (ii) is also expressed as: a subspace is _closed under sums_. Likewise property (iii) says that a subspace is _closed under taking scalar multiples_.

::::::

::::::{prf:example}

The set in $\R^n$ that consists of only the zero vector, i.e. $S = \{\vect{0}\}$, is a subspace.

We will check that it has the three properties mentioned in the definition:

<ol type = "i">
<li>

$S$ certainly contains the zero vector.

</li>
<li>

If two vectors $\vect{u}$ and $\vect{v}$ are in $S$, then their sum is in $S$ too:

<br>

$$

\vect{u} \in S,  \vect{v} \in S  \,\,
\Longrightarrow \,\, \vect{u} =  \vect{v}  =  \vect{0} \,\,
\Longrightarrow  \,\, \vect{u} +  \vect{v}  =  \vect{0} +  \vect{0} =
\vect{0} \in S.
$$

</li>

<li>

If a vector $\vect{u}$ is in $S$, then every scalar multiple of $\vect{u}$ is in $S$ too:

<br>

$$
\vect{u} \in S\quad
\Longrightarrow \quad \vect{u} =  \vect{0} \quad
\Longrightarrow \quad c\vect{u} =  c\vect{0} = \vect{0} \in S.
$$

</li>
</ol>

::::::

The set that only consists of the zero vector is sometimes called a **trivial** subspace.
There is one other subspace that is worthy of that name:

::::::{prf:definition}

The **trivial subspaces** of $\R^n$ are the set $\{\vect{0}\}$ and the set $\R^n$ itself.

::::::

::::::{prf:example}

In $\R^2$, a line through the origin is a non-trivial subspace. A line not containing the origin is not.
In fact, the latter does not satisfy **any** of the three properties of a subspace, as may be clear from {numref}`Figure %s <Fig:Subspaces:Lines>`.
In the picture on the right, for two vectors $\vect{u}$ and $\vect{v}$ on the line $\mathcal L$,

$$
\vect{u}+\vect{v} \, \text{ and   } \, -\tfrac32\vect{u} \, \text{    do not lie on   } \,{\mathcal L}
$$

::::{figure} Images/Fig-Subspaces-Lines.svg
:name: Fig:Subspaces:Lines
:class: dark-light

A line is a subspace of $\R^2$ if and only if it goes through $(0,0)$.
::::

::::::

::::::{prf:example}
:label: Ex:Subspaces:SubspacesR3

Examples of subspaces in $\R^3$ are lines and planes through the origin.
Try to visualize that these sets do satisfy the properties of a subspace. A sketch may help.
It is good practice to keep these examples in mind as typical examples of subspaces.

::::::

::::::{prf:example}

A disk $D$ specified by the inequality $x^2 + y^2 \leq a^2$, where $a$ is some positive number, is not a subspace of $\R^2$. It has neither of the properties
(ii) and (iii). See {numref}`Figure %s <Fig:Subspaces:SubspacesDisk>`.

::::{figure} Images/Fig-Subspaces-Disk.svg
:name: Fig:Subspaces:SubspacesDisk
:class: dark-light

A disk is not a subspace of $\R^2$.
::::

::::::

::::::{exercise}
:label: Exc:Subspaces:NonSubspacesR2

<ol type = "a">
<li>

Give an example of a subset in $\R^2$ that has property i and ii, but not property iii.

</li>
<li>

Also give a set with only the properties i and iii.

</li>
</ol>

```{applet}
:url: subspaces_in_rn/the_game
:fig: Images/Fig-TheGame.svg
:name: Fig:Subspaces:SubspacesGame
:class: dark-light

A game to test your knowledge of subspaces. On the left, $\vect{u} + \vect{v}$ is computed; try to find a result where the sum is not in the subspace. On the right, a scalar multiple $c \cdot \vect{u}$ is computed; try to find a result that is not in the subspace. Confetti will appear if a solution is found that falls outside the set. Different sets can be selected with the dropdown menu.
```

<!-- You may get some inspriration from the applet below. -->

::::::

::::::{admonition} Solution to&nbsp;{numref}`Exc:Subspaces:NonSubspacesR2`&nbsp;(_click to show_)
:class: solution, dropdown

We first give an example of a subset of $\R^2$ that only has properties i. and ii.

Let $S_1$ be the vectors in $\R^2$ with non-negative entries. So, $S_1$ is the first quadrant of the $x_1$-$x_2$-plane. <BR>
For two vectors in $S_1$ their sum still lies in $S_1$.
However, if $\vect{v}\neq \vect{0}$ lies in $S_1$ and $c$ is negative, then $c\vect{v}$ is not in $S_1$.

An example of a subset of $\R^2$ that only has properties i. and iii. is the following:

$$
  S_2 = \left\{ \begin{bmatrix}x_1 \\ x_2  \end{bmatrix}\,:\,\,
  x_1x_2 = 0 \right\}.
$$

So $S_2$ consists of the two coordinate axes. <BR>
$S_2$ contains the origin, and is closed under taking multiples. <BR>
However for the two vectors $\vect{e}_1, \vect{e}_2$ in $S_2$ the sum is not:

$$
 \vect{e}_1 + \vect{e}_2 = \begin{bmatrix} 1 \\ 0 \end{bmatrix} +
  \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}.
$$

::::::

::::::{prf:proposition}
:label: Prop:Subspaces:SpanClosed

A non-empty subset $S$ of $\R^n$ is a subspace if and only if

:::{math}
:label: Eq:Subspaces:SpanClosed

\text{for all } \vect{u}, \vect{v} \in S, c_1, c_2 \in \R\,\,\text{ it holds that }\,\,
c_1\vect{u}+ c_2 \vect{v} \in S.

:::

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:Subspaces:SpanClosed`
:class: tudproof

To show that a subspace satisfies property {eq}`Eq:Subspaces:SpanClosed`,
suppose that $S$ is a subspace, $\vect{u}$ and $\vect{v}$ are vectors in $S$ and
$c_1,c_2$ are real numbers.

From property (iii) it follows that

$$
c_1\vect{u} \in S \quad \text{and} \quad  c_2\vect{v} \in S.
$$

Next property (ii) implies that

$$
c_1\vect{u} +  c_2\vect{v} \in S.
$$

Conversely,
assume $S$ is non-empty and satisfies property {eq}`Eq:Subspaces:SpanClosed`.

Taking $c_1 = c_2 = 1$ it follows that for $\vect{u},\vect{v} \in S$

$$
\vect{u}+ \vect{v} = 1\vect{u}+1\vect{v}  \in S, \text{  so  }S\text{  has property (ii)}
$$

taking $c_1 = c$, $c_2  = 0$ it follows that for $\vect{u} \in S$

$$
c\vect{u}  = c\vect{u}+0\vect{u}  \in S, \text{  so  }S\text{  has property (iii)}.
$$

Finally, to show that $S$ contains the zero vector, let $\vect{u}$ be any vector in $S$, which is possible since $S$ is non-empty. Then from property (iii), taking $c = 0$, it follows that

$$

\vect{0} = 0\vect{u}, \quad \text{so  } \,\,\vect{0} \text{  lies in  }S.


$$

::::::

::::::{prf:remark}

By repeatedly applying the last proposition, we find for any subspace $S$

$$
\vect{u}_1, \ldots , \vect{u}_k \in S,  c_1, \ldots , c_k \in \R
\quad \Longrightarrow \quad
c_1\vect{u}_1+  \ldots + c_k\vect{u}_k \in S.
$$

So we can more generally say that a subspace is _closed under taking linear combinations_. <BR>
This also means that if $\vect{u}_1, \ldots , \vect{u}_k $  are vectors in a subspace $S$, <BR>
then $\Span{\vect{u}_1, \ldots , \vect{u}_k} $ is contained in $S$.

::::::

In fact, the standard example of a subspace is as given in the next proposition.

::::::{prf:proposition}
:label: Prop:Subspaces:SpanIsSubspace

If $\vect{v}_1,\vect{v}_2, \ldots , \vect{v}_r$ are vectors in $\R^n$, then

$$
\Span{\vect{v}_1,\vect{v}_2, \ldots , \vect{v}_r} \quad \text{is a subspace in  } \R^n.
$$

In this situation the vectors are said to **generate** the subspace, or to be a **set of generators** for the subspace.
Recall {prf:ref}`Dfn:LinearCombinations:Span`: the span of zero vectors in $\R^n$ (in other words, the span of the empty set) is defined to be the set $\{\vect{0}\}$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:Subspaces:SpanIsSubspace`
:class: tudproof

If the number of vectors $r$ is equal to $0$, the span is equal to $\{\vect{0}\}$, the trivial subspace.

Next let us check the three properties in {prf:ref}`Dfn:Subspaces:Subspace` in case $r \geq 1$.

Property (i):

$$
\vect{0} = 0\vect{v}_1+0\vect{v}_2+ \ldots + 0\vect{v}_r, \quad \text{so} \quad
\vect{0} \in \text{Span} \{ \vect{v}_1,\vect{v}_2, \ldots , \vect{v}_r \}.
$$

For property (ii) we just have to note that the sum of two linear combinations

$$
(c_1\vect{v}_1+ \ldots + c_r\vect{v}_r)\quad \text{and} \quad (d_1\vect{v}_1+ \ldots + d_r\vect{v}_r)
$$

of a set of vectors $ \{ \vect{v}_1,\vect{v}_2, \ldots , \vect{v}_r \}$ is again a linear combination of these vectors. This is quite straightforward:

$$
(c_1\vect{v}_1+ \ldots + c_r\vect{v}_r) + (d_1\vect{v}_1+ \ldots + d_r\vect{v}_r) =
(c_1+d_1)\vect{v}_1+ \ldots + (c_r+d_r)\vect{v}_r.
$$

Likewise you can check property (iii). This is {numref}`Exc:Subspaces:CheckPropiii`.

::::::

::::::{exercise}
:label: Exc:Subspaces:CheckPropiii

Give a proof of property (iii).

::::::

::::::{prf:remark}

In the previous proposition we do not impose any restrictions on the set of vectors
$\{ \vect{v}_1,\vect{v}_2, \ldots , \vect{v}_r \}$. In the sequel we will see that it will be advantageous to have a **linear independent** set of generators.

::::::

::::::{prf:proposition}
:label: Prop:Subspaces:AllSubspacesR3

Each subspace $S$ in $\R^3$ has one of the following forms:

:::{latextable}
:class: table-unbordered table-unstriped table

\begin{tabular}{ll}
(A) the single vector $\vect{0}$,& (B) a line through the origin, \\
(C) a plane through the origin,& (D) the whole $\R^3$.\\
\end{tabular}
:::

In other words

$$
S = \text{Span}\{\vect{v}_i\, |\,\ i = 1,\ldots, r\} \quad \text{where  }\, r = 0, 1, 2 \text{  or  } 3,
$$

and we may assume that the vectors $\vect{v}_i$ are linearly independent.

Once more we recall the convention that the span of zero vectors (i.e., when $r = 0$) is the set only containing the zero vector.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:Subspaces:AllSubspacesR3`
:class: tudproof

of {prf:ref}`Prop:Subspaces:AllSubspacesR3`.

We build it up from small to large.

Suppose $S$ is a subspace of $\R^3$.

$S$ will at least contain the zero vector. This may be all, i.e., $S   = \{\vect{0}\}$.
Then we are in case (A). Case closed.

If $S \neq  \{\vect{0}\}$, then $S$ contains at least one nonzero vector $\vect{v}_1$.
By property (iii) $S$ then contains all multiples $c\vect{v}_1$.
If that is all, if all vectors in $S$ are multiples of $\vect{v}_1$, then $S = \Span{\vect{v}_1}$, a line through the origin,
and we are in case (B).

If $S$ is larger than $\Span{\vect{v}_1}$ we continue our enumeration of possible subspaces. So suppose there is a vector $\vect{v}_2$ in $S$ that is not in $\Span{\vect{v}_1}$. By {prf:ref}`Thm:LindInd:LinIndisVectDeponPrevious` the set $\{\vect{v}_1,\vect{v}_2\}$ is linearly independent, and by virtue of {prf:ref}`Prop:Subspaces:SpanClosed`,
$S$ then contains $\Span{\vect{v}_1,\vect{v}_2}$.
Again, this may the end point, $S =  \Span{\vect{v}_1,\vect{v}_2}$, and then we are in case (C).

If not, $S$ must contain a third linearly independent vector $\vect{v}_3$, and the same argument as before gives that $S$ contains $\text{Span}\{\vect{v}_1,\vect{v}_2,\vect{v}_3\}$. We claim that this implies that

$$
S = \Span{\vect{v}_1,\vect{v}_2,\vect{v}_3} = \R^3, \text{  i.e., we are in case (D)}
$$

For, if not, there must be a vector $ \vect{v}_4 \in \R^3$ not in $\Span{\vect{v}_1,\vect{v}_2,\vect{v}_3}$.
Then $\{\vect{v}_1,\vect{v}_2,\vect{v}_3, \vect{v}_4\}$
would be a set of four linearly independent vectors in $\R^3$, which by {prf:ref}`Thm:LinInd:MoreRowthanColmeansLinDep` is impossible.

::::::

The argument can be generalized to prove the following theorem.

::::::{prf:theorem}
:label: Thm:Subspaces:AllSubspacesRn

Every subspace of $\R^n$ is of the form

$$
S = \Span{\vect{v}_1, \ldots , \vect{v}_r} \quad \text{for some  } \, r \leq n,
$$

where

$$
\{\vect{v}_1, \ldots , \vect{v}_r\} \,\,  \text{is linearly independent.}
$$

::::::

It may seem that with the above complete description of all possible subspaces in $\R^n$
the story of subspaces can be closed. However, subspaces will appear in different contexts in various guises, each valuable in its own right. One of these we will focus on immediately.

## Column Space and Null Space of a Matrix

We now turn our attention to two important subspaces closely related to an $m\times n$ matrix $A$.

::::::{prf:definition}

The **column space** of an $m\times n$ matrix $A=  \begin{bmatrix} \vect{a}_1 &  \vect{a}_2    & \ldots &    \vect{a}_n \end{bmatrix}$ is the span of the columns of $A$:

$$
\Col{A} = \Span{\vect{a}_1,\vect{a}_2,\ldots,\vect{a}_n}.
$$

The **null space** of an $m\times n$ matrix $A$ is the solution set of the homogeneous equation $A\vect{x} = \vect{0}$:

$$
\Nul{A} = \{\vect{x} \in \mathbb{R}^n \,|\,  A\vect{x} = \vect{0}\}.
$$

::::::

::::::{prf:remark}

For an $m\times n$ matrix $A$, Col $A$ is the set of all vectors of the form $A\vect{x}$, for $\vect{x}\in\R^n$. The column space
Col ${A}$ can also be interpreted as the range of the linear transformation $T:\R^n \to \R^m$ defined via
$T(\vect{x}) = A\vect{x}$. &nbsp; (Cf. {prf:ref}`Prop:LinTrafo:RangeTA`.)

::::::

::::::{prf:remark}

Note that for an $m\times n $ matrix  $A$ the column space is a subset of $\R^m$ and the null space lives in $\R^n$. In short,

$$
\Col{A} \subseteq \R^m ,\quad \Nul{A} \subseteq \R^n.
$$

::::::

The next proposition shows that the designation 'space' in the above definition is well justified.

::::::{prf:proposition}
:label: Prop:Subspaces:AllSubspacesRn

Let $A$ be an $m\times n$ matrix.

<ol type = "i">
<li>

The column space of $A$ is a subspace of $\R^m$.

</li>

<BR>

<li>

The null space of $A$ is a subspace of $\R^n$.

</li>
</ol>

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:Subspaces:AllSubspacesRn`
:class: tudproof

Let $A$ be an $m\times n$ matrix.<ol type = "i">

<li>

The columns of $A$ are vectors in $\R^m$. As we have seen {prf:ref}`Prop:Subspaces:SpanIsSubspace`

the span of a set of vectors in $\R^m$ is indeed a subspace of $\R^m$.

</li>
<li>

To show that the null space is a subspace, we check the requirements of the definition.

First, for $\mathbf{v} = 0$,

$$
  A\vect{v} =  A\vect{0} = \vect{0},
$$

so $\vect{v} = \vect{0}$ is contained in the null space.

Second, to show that $\Nul{A}$ is closed under sums, suppose that
$\vect{u}$ and $\vect{v}$ are two vectors in $\Nul{A}$. Then from

<BR>

$$
A\vect{u} = \vect{0} \quad \text{and} \quad A\vect{v} = \vect{0},
$$

we deduce

$$
A(\vect{u}+\vect{v}) =  A\vect{u}+ A\vect{v} = \vect{0} +\vect{0} = \vect{0},
$$

which implies that

$$
\vect{u}+ \vect{v} \text{  also lies in  } \Nul{A}.
$$

Third, to show that $\Nul{A}$ is closed under taking scalar multiples,
suppose that
$\vect{u}$ is a vector in $\Nul{A}$, i.e.

<BR>

$$
A\vect{u} = \vect{0}
$$

and $c$ is a real number.

Then

$$

A(c\vect{u}) = c\,A(\vect{u}) = c\,\vect{0} = \vect{0},


$$

which proves that

$$
c\vect{u} \text{  also lies in  } \text{Nul} A.
$$

Hence $\Nul{A}$ has all the properties of a subspace.

</li>
</ol>

::::::

::::::{prf:remark}

The above proof, that the null space is a subspace, is as basic as possible. That is, we started from the definitions (of null space and subspace) and used properties of the matrix product to connect the two.

Alternatively we could have used knowledge already acquired earlier. In {numref}`Section:SolutionSets` we have seen that the solution set of a homogeneous
system

$$
A\vect{x} = \vect{0}
$$

can be written in parametric vector form

$$
\vect{x} = c_1\vect{u}_1 + c_2\vect{u}_2 + \ldots +  c_k\vect{u}_k.
$$

Thus: it is the span of a set of vectors, and as such
by {prf:ref}`Prop:Subspaces:SpanIsSubspace` it is a subspace.

::::::

::::::{exercise}
:label: Exc:Subspaces:ColABinColA

Suppose that $A$ and $B$ are matrices for which the product $AB$ is defined.

<ol type = "i">

<li>

Show that the column space of $AB$ is a subset of the column space of $A$, i.e.
<br><br>

$$
\Col{AB} \subseteq \Col{A}.
$$

</li>
<li>

Can you find a similar formula relating the null space of $AB$ to the null space of either $A$ or $B$ (or both)?

</li>
</ol>

::::::

::::::{admonition} Solution to&nbsp;{numref}`Exc:Subspaces:ColABinColA`&nbsp;(_click to show_)
:class: solution, dropdown

Suppose that $A$ is an $m\times n$ and $B$ an $n \times p$ matrix.
Thus $AB$ is an $m\times p$ matrix.

<ol type = "i">

<li>

The column space of an $m\times n$ matrix $M$, consists of all vectors
$\vect{w} = M\vect{v}$, where $\vect{v}$ is a vector in $\R^n$.

Suppose $\vect{w}$ is a vector in Col$(AB)$, so $\vect{w} = AB\vect{v}$ for some vector $\vect{v}$ in $\R^p$. <BR>
Then also $\vect{w} = A(B\vect{v})$, where $B\vect{v}$ is a vector in $\R^n$, which proves that $\vect{w} \in $ Col$(A)$.

With this we have shown that every vector in Col$(AB)$ also lies in Col$(A)$, i.e.,

$$
\Col{(AB)} \subseteq \Col{(A)}.
$$

</li>
<li>

The nulspace of an $m\times n$ matrix $M$ consists of all vectors $\vect{v}$ in $\R^n$ for which $M\vect{v} = \vect{0}$. &nbsp;
We show that

$$
\Nul{(B)} \subseteq \Nul{(AB)}.
$$

Suppose $\vect{v}$ is an element of $\Nul{(B)}$. &nbsp;
Then $B\vect{v}= \vect{0}$, so a fortiori $AB\vect{v}= A\vect{0} =\vect{0}$, and so $\vect{v}$ lies in $\Nul{(AB)}$.

</li>
</ol>

::::::

::::::{exercise}
:label: Exc:Subspaces:WhatIfAAeq0

For an $n\times n$ matrix $A$, the null space and the column space are both subspaces of (the same) $\R^n$. Prove or disprove the following statement.

For a square matrix $A$:

$$
A^2 = O \quad \iff \quad  \Col{(A)}  \subseteq \Nul{(A)}.
$$

::::::

::::::{admonition} Solution to&nbsp;{numref}`Exc:Subspaces:WhatIfAAeq0`&nbsp;(_click to show_)
:class: solution, dropdown

First we show that

$$
A^2 = O \quad \Rightarrow \quad  \Col{(A)}  \subseteq \Nul{(A)}.
$$

Let $\vect{w}\in\Col{(A)}$. <BR>
Then there is a vector $\vect{v}$ in $\R^n$ for which $\vect{w} = A\vect{v}$. <BR>
It follows that $A\vect{w} = A^2\vect{v} = O\vect{v} = \vect{0}$. Thus $\vect{w} \in \Nul{(A)}$.

Next we have to we show that

$$
\Col{(A)}  \subseteq \Nul{(A)} \quad \Rightarrow \quad  A^2 = O.
$$

If we can show that $A^2\vect{x}= \vect{0}$ for every vector $\vect{x}$ in $\R^n$, we're done. <br>
So let $\vect{x}$ be any vector in $\R^n$. Then $\vect{y} =A\vect{x}$ lies in the column space of $A$, which is contained in the nulspace of $A$. <br>
So $A\vect{y} = A^2\vect{x} = \vect{0}$, and we may conclude that indeed $A^2 = O$.

::::::

## Grasple Exercises

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/66b4134c-20e3-4a38-8f14-a32aa472aece?id=70616
:label: grasple_exercise_4_1_1
:dropdown:
:description: To check whether a vector is in a subspace spanned by two vectors.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/aa71ac1a-d82d-4c6d-a6af-7af0c25422b1?id=70617
:label: grasple_exercise_4_1_2
:dropdown:
:description: To check whether a vector is in a subspace spanned by two vectors.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2a08d069-ac34-4f9f-8479-85896ade75da?id=70621
:label: grasple_exercise_4_1_3
:dropdown:
:description: To decide whether a vector $\vect{p}$ is in Col$(A)$.

::::::

::::::{grasple}  
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9470136c-b9ce-4664-937c-fad9da7963cb?id=70622
:label: grasple_exercise_4_1_4
:dropdown:
:description: To decide whether a vector $\vect{p}$ is in Col$(A)$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8756aa45-07b2-40f1-8fbe-aae7c140ae19?id=70625
:label: grasple_exercise_4_1_5
:dropdown:
:description: To give a vector in Nul$(A)$ and a vector not in Nul$(A)$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c32e1656-5d38-4708-a55d-22ced9a9b254?id=70623
:label: grasple_exercise_4_1_6
:dropdown:
:description: To decide whether a vector $\vect{p}$ is in Nul$(A)$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ab566408-ef8d-4b99-9f96-ceb29dcc234b?id=70624
:label: grasple_exercise_4_1_7
:dropdown:
:description: To decide whether a vector $\vect{p}$ is in Nul$(A)$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2a3d5aaf-c0f1-4596-a3e7-3876c786544a?id=70615
:label: grasple_exercise_4_1_8
:dropdown:
:description: Can two subspaces of $\R^n$ be disjoint?

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f880df03-c9b6-4c69-bc94-ea0c6d273b24?id=70627
:label: grasple_exercise_4_1_9
:dropdown:
:description: For an $m\times n$ matrix, in which $\R^p$ lies Nul$(A)$? And Col$(A)$?

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8bf246d1-8aad-448f-842a-8cc20c21b99a?id=70629
:label: grasple_exercise_4_1_10
:dropdown:
:description: To find $p$ such that Nul$(A)$ lies in $\R^p$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3eb1c09d-b39f-4eb8-8968-804469666617?id=83365
:label: grasple_exercise_4_1_11
:dropdown:
:description: To find a parameter such that Nul$(A)=$ Col$(A)$ for a $2\times2$ matrix $A$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/958bc91a-84e2-48e8-8cdf-b26514c41df0?id=83371
:label: grasple_exercise_4_1_12
:dropdown:
:description: To find a parameter such that Nul$(A)=$ Col$(A)$ for a $2\times2$ matrix $A$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3b5196d2-1219-494e-a445-9dcadd8f19a0?id=88181
:label: grasple_exercise_4_1_13
:dropdown:
:description: To check whether certain subsets $S_i$ of $\mathbb{R}^3$ are subspaces.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/66eb42d3-ed92-45aa-8576-d6c4b86c8502?id=88184
:label: grasple_exercise_4_1_14
:dropdown:
:description: To check whether certain subsets $S_i$ of $\mathbb{R}^3$ are subspaces.

::::::
