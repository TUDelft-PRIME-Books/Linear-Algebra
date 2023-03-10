(Sec:SubspacesRn)=

# Subspaces of $\R^n$


## Introduction

Subspaces are structures that appear in many different subfields of linear algebra.
For instance, as solution sets of homogeneous systems of linear equations, and as ranges of linear transformations, to mention two situations that we have already come across.
In this section we will define them and analyze their basic properties, in {numref}`Sec:BasisDim` we will consider the important attributes basis and dimension.




## Definition of subspace and basic properties




::::::{prf:definition}
:label: Dfn:Subspaces:Subspace




A (linear) subspace of $\R^n$ is a subset $S$ of $\R^n$ with the following three properties:
<ol type = "i">

<li>

$S$ contains the zero vector.


</li>

<li>

 If two vectors $\vect{u}$ and $\vect{v}$ are in $S$, then their sum is in $S$ too:

$$

\vect{u} \in S,  \vect{v} \in S \quad \Longrightarrow \quad
\vect{u}+ \vect{v} \in S.
\nonumber

$$

</li>

<li>

 If a vector  $\vect{u}$ is in $S$, then every scalar multiple of $\vect{u}$ is in $S$ too:

$$

\vect{u} \in S,  c \in \R \quad \Longrightarrow \quad
c\vect{u} \in S.
\nonumber

$$

</li>
</ol>




::::::






::::::{prf:remark}


Property (ii) is also expressed as: a subspace is closed under sums.  Likewise property (iii) says that a subspace is closed under taking scalar multiples.



::::::






::::::{prf:example}


The set in $\R^n$ that  consists of only  the zero vector, i.e. $S = \{\vect{0}\}$, is a subspace.

We will check that it has the three properties mentioned in the definition:
<ol type = "i">

<li>

$S$ certainly contains the zero vector.


</li>

<li>

 If two vectors $\vect{u}$ and $\vect{v}$ are in $S$, then their sum is in $S$ too:

$$

\vect{u} \in S,  \vect{v} \in S \quad
\Longrightarrow  \vect{u} =  \vect{v}  =  \vect{0} \quad
\Longrightarrow   \vect{u} +  \vect{v}  =  \vect{0} +  \vect{0} =
\vect{0} \in S.
\nonumber

$$

</li>

<li>

 If a vector  $\vect{u}$ is in $S$, then every scalar multiple of $\vect{u}$ is in $S$ too:  again

$$

\vect{u} \in S\quad
\Longrightarrow \quad \vect{u} =  \vect{0} \quad
\Longrightarrow \quad c\vect{u} =  c\vect{0} = \vect{0} \in S.
\nonumber

$$

</li>
</ol>




::::::




The set that only consists of the zero vector is sometimes called a **trivial** subspace.
There is one other subspace that is worthy of that name:



::::::{prf:definition}


The **trivial subspaces** of $\R^n$ are the sets $\{\vect{0}\}$ and the set $\R^n$ itself.



::::::






::::::{prf:example}
:label: Fig:Subspaces:Lines



In $\R^2$, a line through the origin is a non-trivial subspace.  A line not containing the origin is not.
In fact, the latter does not satisfy **any** of the three properties of a subspace, as may be clear from {numref}`Figure %s <Fig:Subspaces:Lines>`.
In the  picture on the right, for two vectors $\vect{u}$ and $\vect{v}$ on the line $\mathcal L$,

$$

\vect{u}+\vect{v} \text{  and  }  -\tfrac32\vect{u} \text{    do not lie on  }{\mathcal L}
\nonumber

$$



::::{figure} Images/Fig-Subspaces-Lines.svg
:name: Fig:Subspaces:Lines


A line  is a subspace if and only if it goes through (0,0)
::::






::::::









::::::{prf:example}
:label: Ex:Subspaces:SubspacesR3




Examples of subspaces in $\R^3$ are lines and planes through the origin.
Try to visualize  that these sets do satisfy the properties of a subspace. A sketch  may help.
It is good practice to keep these examples in mind as typical examples of subspaces.



::::::












::::::{exercise}
:label: Exc:Subspaces:NonSubspacesR2




<ol type = "i">

<li>


Give an example of a subset in $\R^2$ that has property (i) and (ii), but not property (iii).


</li>

<li>


Also give a set with only the properties (i) and (iii).


</li>
</ol>




::::::








::::::{prf:example}
:label: Fig:Subspaces:SubspacesDisk



A disk  $D: x^2 + y^2 \leq a^2$, where $a$ is some positive number, is not a subspace of $\R^2$.  It has neither of the properties
(ii) and (iii).  See {numref}`Figure %s <Fig:Subspaces:SubspacesDisk>`.


::::{figure} Images/Fig-Subspaces-Disk.svg
:name: Fig:Subspaces:SubspacesDisk


A disk is not a subspace.
::::





::::::







::::::{prf:proposition}
:label: Prop:Subspaces:SpanClosed




A non-empty subset  $S$ of $\R^n$ is a subspace if and only if


:::{math}
:label: Eq:Subspaces:SpanClosed



\text{for all  } \vect{u},  \vect{v} \in S,  c_1, c_2 \in \R \text{  we have  }
c_1\vect{u}+ c_2 \vect{v} \in S.

:::





::::::





::::::{prf:proof}


To show that a subspace satisfies property {eq}`Eq:Subspaces:SpanClosed`,
suppose that $S$ is a subspace,  $\vect{u}$ and $\vect{v}$ are vectors in $S$ and
$c_1,c_2$ are real numbers.

From property (iii) it follows that

$$

c_1\vect{u} \in S \quad \text{and} \quad  c_2\vect{v} \in S.
\nonumber

$$

Next property (ii) implies that

$$

c_1\vect{u} +  c_2\vect{v} \in S.
\nonumber

$$

Conversely,
assume $S$ is non-empty and satisfies property {eq}`Eq:Subspaces:SpanClosed`.

Taking $c_1 = c_2 = 1$ it follows that for  $\vect{u},\vect{v} \in S$

$$

\vect{u}+ \vect{v} = 1\vect{u}+1\vect{v}  \in S, \text{  so  }S\text{  has property (ii)}
\nonumber

$$

taking $c_1 = c$, $c_2  = 0$ it follows that for  $\vect{u} \in S$

$$

c\vect{u}  = c\vect{u}+0\vect{u}  \in S, \text{  so  }S\text{  has property (iii)}.
\nonumber

$$

Finally, to show that $S$ contains the zero vector, let $\vect{u}$ be any vector in $S$, which is possible since $S$ is non-empty. Then from property (iii), taking $c = 0$ it follows that

$$

\vect{0} = 0\vect{u}, \quad \text{so  } \vect{0} \text{  lies in  }S.
\nonumber

$$




::::::







::::::{prf:remark}


By repeatedly applying the last proposition, for a subspace $S$ we have:

$$

\vect{u_1}, \ldots , \vect{u_k} \in S,  c_1, \ldots , c_k \in \R
\quad \Longrightarrow \quad
c_1\vect{u_1}+  \ldots + c_k\vect{u_k} \in S.
\nonumber

$$

So we can more generally say:  a subspace is closed under taking linear combinations.
This also means that if $\vect{u_1}, \ldots , \vect{u_k} $  are vectors in a subspace $S$, then
$\Span{\vect{u_1}, \ldots , \vect{u_k}} $ is contained in $S$.



::::::




In fact, the standard example of a subspace is as given in the next proposition.



::::::{prf:proposition}
:label: Prop:Subspaces:SpanIsSubspace



If  $\vect{v}_1,\vect{v}_2, \ldots , \vect{v_r}$ are vectors in $\R^n$, then

$$

\Span{\vect{v}_1,\vect{v}_2, \ldots , \vect{v_r}} \quad \text{is a subspace in  } \R^n.
\nonumber

$$

In this situation the vectors are said to **generate** the subspace, or to be a **set of generators** for the subspace.
Recall  {prf:ref}`Dfn:LinearCombinations:Span`:  the span of zero vectors in $\R^n$ (in other words: the span of the empty set) is defined to be the set $\{\vect{0}\}$.



::::::






::::::{prf:proof}


If the number of vectors  $r$ is equal to $0$, the span is equal to $\{\vect{0}\}$, the trivial subspace.

Next let us  check the  three properties in {prf:ref}`Dfn:Subspaces:Subspace`  in case  $r \geq 1$.

Property (i):

$$

\vect{0} = 0\vect{v}_1+0\vect{v}_2+ \ldots + 0\vect{v_r}, \quad \text{so} \quad
\vect{0} \in \text{Span} \{ \vect{v}_1,\vect{v}_2, \ldots , \vect{v_r} \}.
\nonumber

$$

For property (ii) we just have to note that the sum of two linear combinations

$$

(c_1\vect{v}_1+ \ldots + c_r\vect{v_r})\quad \text{and} \quad (d_1\vect{v}_1+ \ldots + d_r\vect{v_r})
\nonumber

$$

of a set of vectors $ \{ \vect{v}_1,\vect{v}_2, \ldots , \vect{v_r} \}$  is again a linear combination of these vectors. This is quite straightforward:

$$

(c_1\vect{v}_1+ \ldots + c_r\vect{v_r}) + (d_1\vect{v}_1+ \ldots + d_r\vect{v_r}) =
(c_1+d_1)\vect{v}_1+ \ldots + (c_r+d_r)\vect{v_r}.
\nonumber

$$

Likewise you can check property (iii).  This is {numref}`Exc:Subspaces:CheckPropiii`.



::::::






::::::{exercise}
:label: Exc:Subspaces:CheckPropiii


Give a proof of property (iii).

::::::






::::::{prf:remark}


In the previous proposition we do not impose any restrictions on the set of vectors
$\{ \vect{v}_1,\vect{v}_2, \ldots , \vect{v_r} \}$. In the sequel we will see that it will be advantageous to have a **linear independent** set of generators.



::::::








::::::{prf:proposition}
:label: Prop:Subspaces:AllSubspacesR3




Each subspace $S$ in $\R^3$ has one of the following forms:

:::{latextable}
:class: table-unbordered table-unstriped table

\begin{tabular}{ll}
(A)  the single vector $\vect{0}$,& (B)  a line through the origin, \\
(C)  a plane through the origin,& (D)  the whole $\R^3$.\\
\end{tabular}
:::

In other words:

$$
S = \text{Span}\{\vect{v_i} | i = 1,\ldots, r\} \quad \text{where  } r = 0, 1, 2 \text{  or  } 3,
$$

and we may assume that the  vectors $v_i$ are linearly independent.

Once more we recall the convention that the span of zero vectors (i.e., if $r = 0$)  is the set only containing the zero vector.



::::::


::::::{prf:proof}


of {prf:ref}`Prop:Subspaces:AllSubspacesR3`. 

We build it up from small to large. 

Suppose  $S$ is a subspace of $\R^3$.

$S$  will at least contain the zero vector. This may be all, i.e., $S   = \{\vect{0}\}$.
Then we are in case (A).  Case closed. 

If $S \neq  \{\vect{0}\}$, then $S$ contains at least one nonzero vector $\vect{v}_1$.
By property (iii) $S$ then contains all multiples $c\vect{v}_1$.
If that is all, if all vectors in $S$ are multiples of $\vect{v}_1$, then $S = \Span{\vect{v}_1}$,  a line through the origin,
and we are in case (B).

If  $S$ is larger than $\Span{\vect{v}_1}$  we continue our enumeration of possible subspaces. So suppose there is a vector $\vect{v}_2$ in $S$ that is not in $\Span{\vect{v}_1}$. By {prf:ref}`Thm:LindInd:LinIndisVectDeponPrevious` the set $\{\vect{v}_1,\vect{v}_2\}$ is linearly independent, and by virtue of {prf:ref}`Prop:Subspaces:SpanClosed`,
$S$ then contains $\Span{\vect{v}_1,\vect{v}_2}$.
Again, this may the end point, $S =  \Span{\vect{v}_1,\vect{v}_2}$, and  then we are in case (C).

If not, $S$ must contain a third linearly independent vector $\vect{v}_3$, and the same argument as before gives that $S$ contains $\text{Span}\{\vect{v}_1,\vect{v}_2,\vect{v}_3\}$. We claim that this implies that

$$

S = \Span{\vect{v}_1,\vect{v}_2,\vect{v}_3} = \R^3, \text{  i.e., we are in case (D)}
\nonumber

$$

For, if not, there must be a vector   $  \vect{v}_4 \in \R^3$  not in  $\Span{\vect{v}_1,\vect{v}_2,\vect{v}_3}$.
Then $\{\vect{v}_1,\vect{v}_2,\vect{v}_3, \vect{v}_4\}$
would be a set of four linearly independent vectors in $\R^3$,  which by {prf:ref}`Thm:LinInd:MoreRowthanColmeansLinDep` is impossible.



::::::




The  argument can be generalized to prove the following theorem.



::::::{prf:theorem}
:label: Thm:Subspaces:AllSubspacesRn




Every subspace of $\R^n$ is of the form

$$

S = \Span{\vect{v}_1, \ldots , \vect{v_r}} \quad \text{for some  } r \leq n,
\nonumber

$$

where

$$

\{\vect{v}_1, \ldots , \vect{v_r}\}  \text{    is linearly independent.}
\nonumber

$$




::::::




It may seem that with the above complete description of all possible subspaces in $\R^n$
the story of subspaces can be closed.  However, subspaces will appear in different contexts in various guises, each valuable in its own right.   One of these we will focus on immediately.

## Column space and null space of a matrix

We now turn our attention to two important subspaces closely related to an $m\times n$ matrix $A$.



::::::{prf:definition}


The **column space** of an $m\times n$ matrix $A= [ \vect{a_1}  \vect{a_2}   \ldots   \vect{a_n} ]$ is the span of the columns of $A$:

$$

\Col{A} = \Span{\vect{a}_1,\vect{a}_2,\ldots,\vect{a}_n}.
\nonumber

$$

The  **null space** of an $m\times n$ matrix $A$ is the solution set of the homogeneous equation $A\vect{x} = \vect{0}$:

$$

\Nul{A} = \{\vect{x} \in \mathbb{R}^n |  A\vect{x} = \vect{0}\}.
\nonumber

$$




::::::






::::::{prf:remark}


For an $m\times n$ matrix $A$, Col $A$ is the set of all vectors of the form $A\vect{x}$, for  $\vect{x}\in\R^n$.   The column space
$\Col{A}$   can also be interpreted as the range of the linear transformation $T:\R^n \to \R^m$ defined via
$T(\vect{x}) = A\vect{x}$.  (Cf. {prf:ref}`Prop:LinTrafo:RangeTA`.)



::::::






::::::{prf:remark}


Note that for an $m\times n $ matrix  $A$  the column space is a subset of $\R^m$ and the null space lives in $\R^n$.  In short:

$$

\Col{A} \subseteq \R^m ,\quad \Nul{A} \subseteq \R^n.
\nonumber

$$




::::::




The next proposition shows that the designation `space' in the above definition is well justified:



::::::{prf:proposition}


 Let $A$ be an  $m\times n$ matrix.<ol type = "i">

<li>

 The column space of  $A$ is a subspace of $\R^m$.


</li>

<li>

  The null space of  $A$ is a subspace of $\R^n$.


</li>
</ol>




::::::





::::::{prf:proof}


 Let $A$ be an  $m\times n$ matrix.<ol type = "i">

<li>

The columns of  $A$  are vectors in $\R^m$.  As we have seen {prf:ref}`Prop:Subspaces:SpanIsSubspace`:  

the span of a set of vectors in $\R^m$ is indeed a subspace of $\R^m$.


</li>

<li>

To show that the null space is a subspace, we check the  requirements  of the definition.
First, $A\vect{0} =\vect{0}$,  so $\vect{0}$ is contained in the null space.

Second,  to show that  $\Nul{A}$ is closed under sums, suppose that
$\vect{u}$ and   $\vect{v}$  are two vectors in $\Nul{A}$. Then from

$$

A\vect{u} = \vect{0} \quad \text{and} \quad A\vect{v} = \vect{0},
\nonumber

$$

we deduce

$$

A(\vect{u}+\vect{v}) =  A\vect{u}+ A\vect{v} = \vect{0} +\vect{0} = \vect{0},
\nonumber

$$

which implies that

$$

\vect{u}+ \vect{v} \text{  also lies in  } \Nul{A}.
\nonumber

$$

Third, to show that  $\Nul{A}$  is closed under taking scalar multiples,
suppose that
$\vect{u}$ is a vector  in $\Nul{A}$, i.e.

$$

A\vect{u} = \vect{0}
\nonumber

$$

and $c$ is a real number. 

Then

$$

A(c\vect{u}) = cA(\vect{u}) = c\vect{0} = \vect{0},
\nonumber

$$

which proves that

$$

c\vect{u} \text{  also lies in  } \text{Nul} A.
\nonumber

$$

Hence $\Nul{A}$  has all the properties of a subspace.


</li>
</ol>




::::::






::::::{prf:remark}


The above proof,  that the null space is a subspace,  was as basic as possible: we started from the definitions (of null space and subspace) and used properties of the matrix product to connect the two.

Alternatively we could have used knowledge already acquired:  in {numref}`Section:SolutionSets`  we have seen that the solution set of a homogeneous
system

$$

A\vect{x} = \vect{0}
\nonumber

$$

can be written in parametric vector form

$$

\vect{x} = c_1\vect{u_1} + c_2\vect{u_2} + \ldots +  c_k\vect{u_k}.
\nonumber

$$

Thus:  it is the span of a set of vectors, and as such, a subspace.



::::::







::::::{exercise}
:label: Exc:Subspaces:ColABinColA




Suppose that $A$  and $B$ are  matrices for which the product $AB$ is defined.

<ol type = "i">

<li>


Show that the column space of $AB$ is s subset of the column space of $A$, i.e.

$$

\Col{AB} \subseteq \Col{A}.
\nonumber

$$

</li>

<li>


Can you find a similar formula relating the null space of $AB$ to the null space of either $A$  or $B$(or both)?


</li>
</ol>




::::::






::::::{exercise}
:label: Exc:Subspaces:WhatIfAA=0




For an $n\times n$ matrix $A$,  the null space and the column space are both subspaces of (the same) $\R^n$.  Prove or disprove the following statement.
For a square matrix $A$:

$$

A^2 = O \quad \iff \quad  \Col{A}  \subseteq \Nul{A}.
\nonumber

$$





::::::




