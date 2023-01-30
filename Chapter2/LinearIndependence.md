# Linear independence 

As we have seen in Section , the multiples of a non-zero vector form a line. We have also seen there that, if we consider vectors of the form $c_{1}\mathbf{v_{1}}+c_{2}\mathbf{v_{2}}$ for some vectors $\mathbf{v_{1}},\mathbf{v_{2}}$ and constants $c_{1},c_{2}$ we usually get a plane. But sometimes we don't! For example, if $d\mathbf{v_{1}}=\mathbf{v_{2}}$ for some constant $d$, then all vectors of the given form can be rewritten as $(c_{1}+c_{2}d)\mathbf{v_{1}}$, so they are all contained in the line through the origin and in the direction of $\mathbf{v_{1}}$. Every vector we can make as a linear combination of $\mathbf{v_{1}}$ and $\mathbf{v_{2}}$ can also be made with $\mathbf{v_{1}}$ alone. The vector $\mathbf{v_{2}}$ is superfluous. This situation can be seen in {numref}`Figure %s <Fig:LinInd:Examplein1D>`.

::::{figure} Images/Fig-LinInd-Examplein1D.svg
:name: Fig:LinInd:Examplein1D

The set $\left\lbrace\mathbf{v}_{1},\mathbf{v}_{2}\right\rbrace$ contains two vectors, but one of them is superfluous. Every vector one can make as a linear combination of $\mathbf{v}_{1}$ and $\mathbf{v}_{2}$ can also be made with just $\mathbf{v}_{1}$.
::::


We will now formalise this concept of superfluous vectors.

::::::{prf:definition}
We will call a set $S$ of vectors **linearly dependent** if there is some $\mathbf{v}$ in $S$ such that $\Span{S}=\Span{S\setminus\left\lbrace\mathbf{v}\right\rbrace}$. In this case, we say that $\mathbf{v}$ is **linearly dependent** on $S\setminus\left\lbrace\mathbf{v}\right\rbrace$. If $S$ is not linearly dependent, we say $S$ is **linearly independent**.


::::::


In other words, a set $S$ is linearly dependent if it contains at least one superfluous vector. It may very well contain infinitely many. Let us briefly investigate linear dependence for very small sets before we get to more substantial examples.

::::::{prf:proposition}
:label: Prop:LinInd:LinIndforSmallSets

Let $S$ be a subset of $\mathbb{R}^{n}$ containing

<ul>
<li>

precisely one vector, say $\mathbf{v}$. Then $S$ is linearly dependent precisely when $\mathbf{v}=\mathbf{0}$.

</li>
<li>

precisely two vectors, say $\mathbf{u}$ and $\mathbf{v}$. Then $S$ is linearly independent unless one of these vectors is a multiple of the other.

</li>
</ul>

::::::

::::::{prf:proof}
<ul>
<li>

Assume $S=\left\lbrace\mathbf{v}\right\rbrace$. The span of $S\setminus\left\lbrace\mathbf{v}\right\rbrace$ is the span of the empty set, which is precisely $\left\lbrace\mathbf{0}\right\rbrace$. This is equal to $\Span{S}$ if and only if $\mathbf{v}=\mathbf{0}$.

</li>
<li>

If $\Span{S}=\Span{\mathbf{v}}$ then $\mathbf{u}$ is in $\Span{\mathbf{v}}$ so it is a multiple of $\mathbf{v}$. Similarly, if $\Span{S}=\Span{\mathbf{u}}$ then $\mathbf{v}$ is in $\Span{\mathbf{u}}$ so it is a multiple of $\mathbf{u}$.

</li>
</ul>

::::::

As you can see from the proof of {prf:ref}`Prop:LinInd:LinIndforSmallSets`, our definition of linear depence, while intuitive, is a bit hard to work with. In {prf:ref}`Cor:LinInd:LinIndisColwithoutPivot`, we will see a more convenient way to determine whether a given set of vectors is linearly dependent or not. But let us first consider some examples.

::::::{prf:example}
:label: Item:LinInd:LinDepExin2D

<ul>
<li id="Item:LinInd:LinDepExin2D">

Consider the vectors 

$$
\mathbf{v_{1}}=
\begin{bmatrix}1\\0\end{bmatrix}\quad\mathbf{v_{2}}=
\begin{bmatrix}0\\1\end{bmatrix}
\quad\mathbf{v_{3}}=
\begin{bmatrix}1\\1\end{bmatrix},
$$

which are shown on the left in {numref}`Figure %s <Fig:LinInd:Examplein2D>`. The set $S=\left\lbrace\mathbf{v_{1}},\mathbf{v_{2}},\mathbf{v_{3}}\right\rbrace$ is linearly dependent in view of the following equalities:

:::{math}
:label: Eq:LinInd:LinIndEx1

		\mathbf{v_{1}}=-\mathbf{v_{2}}+\mathbf{v_{3}},
	
:::

:::{math}
:label: Eq:LinInd:LinIndEx2

		\mathbf{v_{2}}=-\mathbf{v_{1}}+\mathbf{v_{3}},
	
:::

:::{math}
:label: Eq:LinInd:LinIndEx3

		\mathbf{v_{3}}=\mathbf{v_{1}}+\mathbf{v_{2}}.
	
:::

Indeed, if we take an arbitrary vector $\mathbf{v}$ in $\Span{S}$, we can write it as 

\begin{align*}
	\mathbf{v}&=c_{1}\mathbf{v}_{1}+c_{2}\mathbf{v}_{2}+c_{3}\mathbf{v}_{3}\\
	&=(c_{2}-c_{1})\mathbf{v}_{2}+(c_{3}+c_{1})\mathbf{v}_{3}
\end{align*}

in view of equation {eq}`Eq:LinInd:LinIndEx1`. This means that $\mathbf{v}$ is also in $\Span{S\setminus\left\lbrace\mathbf{v}_{1}\right\rbrace}$ and consequently that $\mathbf{v}_{1}$ is linearly dependent on $\mathbf{v}_{2}$ and $\mathbf{v}_{3}$.
Similarly, equation {eq}`Eq:LinInd:LinIndEx2` shows that $\mathbf{v_{2}}$ is linearly dependent on $\mathbf{v_{1}}$ and $\mathbf{v_{3}}$ and equation {eq}`Eq:LinInd:LinIndEx3` shows that $\mathbf{v_{3}}$ is linearly dependent on $\mathbf{v_{1}}$ and $\mathbf{v_{2}}$ .

However, every subset of $S$ containing precisely two vectors will be linearly independent, as $S$ contains no two vectors that are multiples of each other.

</li>
<li id="Item:LinInd:LinDepandIndDepExin2D">

Consider now the vectors 

$$
	\mathbf{v_{1}}=
	\begin{bmatrix}1\\0\end{bmatrix}\quad\mathbf{v_{2}}=
	\begin{bmatrix}2\\0\end{bmatrix}\quad
	\mathbf{v_{3}}=
	\begin{bmatrix}0\\1\end{bmatrix}
$$

which are shown on the right in {numref}`Figure %s <Fig:LinInd:Examplein2D>`.
The set $S=\left\lbrace\mathbf{v_{1}},\mathbf{v_{2}},\mathbf{v_{3}}\right\rbrace$ is again linearly dependent since 

$$
\mathbf{v}_{2}=2\mathbf{v}_{1}+0\mathbf{v}_{3}\nonumber
$$

but now the subset $\left\lbrace\mathbf{v_{1}},\mathbf{v_{2}}\right\rbrace$ is a linearly dependent subset of $S$. On the other hand, the subsets $\left\lbrace\mathbf{v_{1}},\mathbf{v_{3}}\right\rbrace$ and $\left\lbrace\mathbf{v_{2}},\mathbf{v_{3}}\right\rbrace$ are linearly independent.

::::{figure} Images/Fig-LinInd-Examplein2D.svg
:name: Fig:LinInd:Examplein2D

The vectors from [i.](#Item:LinInd:LinDepExin2D)  on the left and from [ii.](#Item:LinInd:LinDepandIndDepExin2D)  on the right. On the left, there is no vector which is a multiple of another vector so every set of two vectors is linearly independent. On the right this is not the case. The vectors $\mathbf{v_{1}}$ and $\mathbf{v_{2}}$ are multiples of each other and therefore $\left\lbrace\mathbf{v_{1}},\mathbf{v_{2}}\right\rbrace$ is linearly dependent.
::::



</li>
<li id="Item:LinInd:LinDepExin3D">

Put 

$$
	\mathbf{v_{1}}=
	\begin{bmatrix}1\\0\\0\end{bmatrix},\quad\mathbf{v_{2}}=
	\begin{bmatrix}0\\1\\0\end{bmatrix},\quad\mathbf{v_{3}}=
	\begin{bmatrix}1\\2\\0\end{bmatrix},\quad \text{and}\quad\mathbf{v_{4}}=
	\begin{bmatrix}1\\2\\1\end{bmatrix}.
$$

The set $\left\lbrace\mathbf{v_{1}},\mathbf{v_{2}},\mathbf{v_{3}}\right\rbrace$ is linearly dependent. The set $\left\lbrace\mathbf{v_{1}},\mathbf{v_{2}},\mathbf{v_{4}}\right\rbrace$, however, is not. This is illustrated in {numref}`Figure %s <Fig:LinInd:Examplein3D>`. 

::::{figure} Images/Fig-LinInd-Examplein3D.svg
:name: Fig:LinInd:Examplein3D

The four vectors from [iii.](#Item:LinInd:LinDepExin3D). Note that $\mathbf{v_{3}}$ lies in the plane spanned by $\mathbf{v_{1}}$ and $\mathbf{v_{2}}$ but $\mathbf{v_{4}}$ does not. This means that $\left\lbrace\mathbf{v_{1}},\mathbf{v_{2}},\mathbf{v_{3}}\right\rbrace$ is linearly dependent but $\left\lbrace\mathbf{v_{1}},\mathbf{v_{2}},\mathbf{v_{4}}\right\rbrace$ is not.
::::



</li>
</ul>



::::::


The following elementary properties of linear dependence and linear independence will be used throughout the text, often tacitly.

::::::{prf:proposition}
:label: Prop:LinInd:LinDepSets

Let $S$ be a subset of $\mathbb{R}^{n}$.
<ul>
<li>

If $S$ contains $\mathbf{0}$, then it is a linearly dependent set.
	

</li>
<li>

If $S$ is linearly dependent and $S\subseteq T$, then $T$ is linearly dependent.
	

</li>
<li>

If $T$ is linearly independent and $S\subseteq T$, then $S$ is linearly independent.


</li>
</ul>

::::::

::::::{prf:proof}
:label: Proof:LinInd:LinDepSets

Exercise.


::::::


But how do you determine whether a set of vectors is linearly independent or not? Like so many problems in linear algebra, it comes down to solving a system of linear equations, as {prf:ref}`Prop:LinInd:LinIndisNonTrivSol` shows.  

::::::{prf:proposition}
:label: Prop:LinInd:LinIndisNonTrivSol


A set $\left\lbrace\mathbf{v_{1}},...,\mathbf{v_{k}}\right\rbrace$ of vectors in $\mathbb{R}^{n}$ is linearly dependent if and only if the vector equation



:::{math}
:label: Eq:LinInd:VecEqisZero

c_{1}\mathbf{v}_{1}+\cdots +c_{k}\mathbf{v}_{k}=\mathbf{0}

:::

has a non-trivial solution.

::::::

::::::{prf:proof}
If $\left\lbrace\mathbf{v_{1}},...,\mathbf{v_{k}}\right\rbrace$ is linearly dependent, one of these vectors, say $\mathbf{v}_{i}$, is linearly dependent on the others, i.e. it is in $\Span{\mathbf{v}_{1},...,\mathbf{v}_{i-1},\mathbf{v}_{i+1},...\mathbf{v}_{k}}$. Therefore, there exist some scalars $c_{1},...,c_{i-1},c_{i+1},...,c_{k}$ such that 

$$
\mathbf{v_{i}}=c_{1}\mathbf{v_{1}}+\cdots +c_{i-1}\mathbf{v_{i-1}}+c_{i+1}\mathbf{v_{i+1}}+\cdots +c_{k}\mathbf{v_{k}}
$$

or equivalently

$$
0=c_{1}\mathbf{v_{1}}+\cdots +c_{i-1}\mathbf{v_{i-1}}-\mathbf{v_{i}}+c_{i+1}\mathbf{v_{i+1}}+\cdots +c_{k}\mathbf{v_{k}}.
$$

This means that $(c_{1},...,c_{i-1},-1,c_{i+1},...,c_{k})$ is a solution of the equation {eq}`Eq:LinInd:VecEqisZero`. It is a non-trivial one since the $i$-th coefficient is $-1$ which is non-zero.

If {eq}`Eq:LinInd:VecEqisZero` has a non-trivial solution then there are $c_{1},...,c_{k}$, not all $0$, such that $c_{1}\mathbf{v_{1}}+\cdots +c_{k}\mathbf{v_{k}}=\mathbf{0}$. Take any $i$ such that $c_{i}\neq0$. Then 

$$

\mathbf{v_{i}}=\frac{c_{1}}{c_{i}}\mathbf{v_{1}}-\cdots -\frac{c_{i-1}}{c_{i}}\mathbf{v_{i-1}}-\frac{c_{i+1}}{c_{i}}\mathbf{v_{i}}-\cdots -\frac{c_{k}}{c_{i}}\mathbf{v_{k}}.
$$

This implies $\mathbf{v}_{i}$ is in $\Span{\mathbf{v}_{1},...,\mathbf{v}_{i-1},\mathbf{v}_{i+1},...,\mathbf{v}_{k}}$ so $\left\lbrace\mathbf{v}_{1},...,\mathbf{v}_{k}\right\rbrace$ is linearly dependent.


::::::




::::::{prf:corollary}
:label: Cor:LinInd:LinIndisColwithoutPivot



A set 
$\left\lbrace\mathbf{v}_{1},\dots,\mathbf{v}_{k}\right\rbrace$
of vectors in $\mathbb{R}^{n}$ is linearly dependent if and only if the matrix equation 
$A\mathbf{x}=\mathbf{0}$ with 
$A=\begin{bmatrix}\mathbf{v}_{1}& \cdots &\mathbf{v}_{k}\end{bmatrix}$ 
has a non-trivial solution, i.e. if $A$ has a column without a pivot.


::::::




::::::{prf:proof}
:label: Proof:LinInd:LinIndisColwithoutPivot


Exercise.


::::::




::::::{prf:example}
Consider the following three vectors in $\mathbb{R}^{4}$: 

$$
\mathbf{v_{1}}=
\begin{bmatrix}
1\\1\\0\\-2
\end{bmatrix}\quad\mathbf{v_{2}}=
\begin{bmatrix}-1\\2\\3\\-2\end{bmatrix}\quad\mathbf{v_{3}}=
\begin{bmatrix} 4\\1\\-3\\-4\end{bmatrix}.
$$

Do these vectors form a linearly dependent set? How do we find out? Well, we use the vectors as the columns of a matrix $A$ and compute an echelon form using standard techniques

$$

A=
\begin{bmatrix}1&-1&4\\1&2&1\\0&3&-3\\-2&-2&-4 \end{bmatrix}\sim\cdots\sim 
\begin{bmatrix} 1&-1&4\\0&3&-3\\0&0&0\\0&0&0\end{bmatrix}.
$$

The third column has no pivot, so the system $A\mathbf{x}=\mathbf{0}$ has infinitely many solutions. In particular, it therefore has a non-trivial one. Consequently, the set $\left\lbrace\mathbf{v_{1}},\mathbf{v_{2}},\mathbf{v_{3}}\right\rbrace$ is linearly dependent.

From the reduced echelon form, we can easily find a way to write $\mathbf{v_{3}}$ as a linear combination of $\mathbf{v_{1}}$ and $\mathbf{v_{2}}$. In this case, the reduced echelon form is


$$

A=
\begin{bmatrix}1&-1&4\\1&2&1\\0&3&-3\\-2&-2&-4 \end{bmatrix}\sim\cdots\sim 
\begin{bmatrix} 1&0&3\\0&1&-1\\0&0&0\\0&0&0\end{bmatrix}.
$$


If we put the free variable $x_{3}$ equal to 1, we find $x_{1}=-3$ and $x_{2}=1$, which gives: 

$$

-3\mathbf{v_{1}}+\mathbf{v_{2}}+\mathbf{v_{3}}=\mathbf{0}\quad\text{hence}\quad
\mathbf{v_{3}}=3\mathbf{v_{1}}-\mathbf{v_{2}}.
$$




::::::


There now follow a couple of statements which can be helpful in determining whether a given set of vectors is linearly dependent or not. The first one tells us that an ordered set is linearly dependent precisely when there is a vector which depends on the preceding vectors.

::::::{prf:theorem}
:label: Thm:LindInd:LinIndisVectDeponPrevious

An ordered set $S=(\mathbf{v_{1}},...,\mathbf{v_{n}})$ is linearly dependent if and only if there is a $k$ such that $\mathbf{v_{k}}$ is a linear combination of $\mathbf{v_{1}},...,\mathbf{v_{k-1}}$.


::::::




::::::{prf:proof}
:label: Eq:LinInd:vkLinCombofOthers

Let us assume $v_{k}=c_{1}\mathbf{v}_{1}+\cdots+c_{k-1}\mathbf{v}_{k-1}$ for some scalars $c_{1},...,c_{k-1}$. An arbitrary element $\mathbf{v}$ of $\Span{S}$ is a linear combination of $\mathbf{v}_{1},...,\mathbf{v}_{n}$, so it is 

$$

\mathbf{v}=d_{1}\mathbf{v}_{1}+\cdots+d_{k-1}\mathbf{v}_{k-1}+d_{k}\mathbf{v}_{k}+d_{k+1}\mathbf{v}_{k+1}+\cdots+
d_{n}\mathbf{v}_{n}
$$

for certain scalars $d_{1},...,d_{n}$. We can now rewrite $\mathbf{v}$ as


$$

\mathbf{v}=d_{1}\mathbf{v}_{1}+\cdots+d_{k-1}\mathbf{v}_{k-1}+d_{k}(c_{1}\mathbf{v}_{1}+\cdots+c_{k-1}\mathbf{v}_{k-1})+d_{k+1}\mathbf{v}_{k+1}+\cdots+
d_{n}\mathbf{v}_{n}
$$


so $\mathbf{v}$ is in $\Span{S\setminus\left\lbrace\mathbf{v}_{k}\right\rbrace}$.

Suppose now that $S$ is linearly dependent. Let $k$ be maximal such that $\Span{S}=\Span{S\setminus\left\lbrace\mathbf{v}_{k}\right\rbrace}$. Since $\mathbf{v}_{k}$ is in $S$, it is in $\Span{S\setminus\left\lbrace\mathbf{v}_{k}\right\rbrace}$. So there exist scalars $c_{1},..,c_{k-1},c_{k+1},...,c_{n}$ such that 


:::{math}
:label: Eq:LinInd:vkLinCombofOthers

\mathbf{v}_{k}=c_{1}\mathbf{v}_{1}+\cdots+c_{k-1}\mathbf{v}_{k-1}+c_{k+1}\mathbf{v}_{k+1}+\cdots+
c_{n}\mathbf{v}_{n}.

:::



If we can show that $c_{k+1}=...=c_{n}=0$ we are done, because then we have written $\mathbf{v}_{k}$ as a linear combination of $\mathbf{v}_{1},...,\mathbf{v}_{k-1}$. We will prove by contraposition that this is impossible. Assume $c_{j}\neq0$ for some $j$ greater than $k$. Then Equation {eq}`Eq:LinInd:vkLinCombofOthers` yields 

$$

\mathbf{v}_{j}=\frac{1}{c_{j}}(c_{1}\mathbf{v}_{1}-\cdots -c_{k-1}\mathbf{v}_{k-1}+\mathbf{v}_{k}-c_{k+1}\mathbf{v}_{k+1}-\cdots-c_{j-1}\mathbf{v}_{j-1}-c_{j+1}\mathbf{v}_{j+1}-\cdots -c_{n}\mathbf{v}_{n}).
$$


Consequently, any linear combination of $S$ can be rewritten as a linear combination of $\mathbf{v}_{1},...,\mathbf{v}_{j-1},\mathbf{v}_{j+1},...,\mathbf{v}_{n}$, i.e. $\Span{S}=\Span{S\setminus\left\lbrace\mathbf{v}_{j}\right\rbrace}$. But $j$ is larger than $k$ and we have assumed $k$ to be maximal with this property! This is impossible, so $c_{j}=0$ for all $j$ greater than $k$.


::::::


{prf:ref}`Thm:LindInd:LinIndisVectDeponPrevious` together with {prf:ref}`Cor:LinInd:LinIndisColwithoutPivot` implies that the columns of a matrix are linearly dependent if and only if there is some column which is linearly dependent on the preceding ones. This observation will allow us to simplify certain arguments.  The following result essentially claims that if $k$ vectors suffice to span a set $S$ and you have more than $k$ vectors in $S$, then at least one of them must be superfluous.

::::::{prf:theorem}
:label: Thm:LinInd:TooManyVectsimpliesLinDep

Suppose $\mathbf{u_{1}},...,\mathbf{u_{k}}$ and $\mathbf{v_{1}},...,\mathbf{v_{l}}$ are all vectors in $\mathbb{R}^{n}$. If $k<l$ and $\Span{\mathbf{u_{1}},...,\mathbf{u_{k}}}$ contains $\Span{\mathbf{v_{1}},...,\mathbf{v_{l}}}$ then the set $\left\lbrace\mathbf{v_{1}},...,\mathbf{v_{l}}\right\rbrace$ is linearly dependent.


::::::




::::::{prf:proof}
Consider the matrices 

$$

A=\left[\vect{u_{1}}\cdots\mathbf{u_{k}}\right],\quad B=\left[\vect{v_{1}}\cdots\mathbf{v_{l}}\right]\quad \text{and}\quad C=[A\backslash B].
$$

Bringing $C$ in echelon form gives 

$$

C\sim D=[E\backslash F]
$$

where $D$ is the echelon form of $C$, $E$ is an echelon form of $A$, and $F$ is equivalent to $B$. 

We claim that all of the pivot positions of $D$ are in $E$. Indeed, suppose that the $i$-th column of $F$, let's call it $f_{i}$, contains a pivot. Then $E\mathbf{x}=\mathbf{f_{i}}$ is inconsistent and therefore $A\mathbf{x}=\mathbf{v_{i}}$ is also inconsistent since the elementary row operations preserve linear combinations. But this implies that $\mathbf{v_{i}}$ is not a linear combination of $\mathbf{u_{1}},...,\mathbf{u_{k}}$ hence it is not in $\Span{\mathbf{u_{1}},...,\mathbf{u_{k}}}$. This is a contradiction.

Since $F$ contains no pivot positions of $D$, it has at least as many zero rows as $E$. This implies that an echelon form $G$ of $B$, which is necessarily also an echelon form of $F$, must also have at least as many zero rows as $E$. Therefore, $G$ has no more pivots than $E$. Since $E$ has at most $k$ pivots and $k<l$, $G$ must have a column without pivot. So $B\mathbf{x}=\mathbf{0}$ has a non-trivial solution and by {prf:ref}`Cor:LinInd:LinIndisColwithoutPivot` the set $\left\lbrace\mathbf{v_{1}},...,\mathbf{v_{l}}\right\rbrace$ must be linearly dependent.


::::::




::::::{prf:corollary}
:label: Thm:LinInd:MoreRowthanColmeansLinDep

Let $S$ be a subset of $\mathbb{R}^{n}$. If there are more than $n$ vectors in $S$, then $S$ is linearly dependent.


::::::




::::::{prf:proof}
Take distinct vectors $\mathbf{v_{1}},...,\mathbf{v_{n+1}}$ in $S$. $\Span{\mathbf{v_{1}},...,\mathbf{v_{n+1}}}$ is contained in $\Span{\mathbf{e_{1}},..,\mathbf{e_{n}}}$ and $n+1>n$, so $\left\lbrace\mathbf{v_{1}},..,\mathbf{v_{n+1}}\right\rbrace$ is linearly dependent by {prf:ref}`Thm:LinInd:TooManyVectsimpliesLinDep`. Since this set is contained in $S$, $S$ must be linearly dependent, too, by {prf:ref}`Prop:LinInd:LinDepSets`.




::::::




::::::{prf:example}
To illustrate the strength of {prf:ref}`Thm:LinInd:MoreRowthanColmeansLinDep`, consider the following set of vectors in $\mathbb{R}^{5}$:


$$

\left\lbrace
\begin{bmatrix}5\\-2\\3\\1\\0\end{bmatrix},
\begin{bmatrix}-47\\8\\12\\-3\\4\end{bmatrix},
\begin{bmatrix}12\\-3\\-2\\-1\\11\end{bmatrix},
\begin{bmatrix}42\\-7\\-52\\2\\16\end{bmatrix},
\begin{bmatrix}87\\56\\-32\\1\\0\end{bmatrix},
\begin{bmatrix}-48\\2\\35\\156\\8\end{bmatrix}\right\rbrace.
$$


If we had to bring the matrix with these six vectors as columns to echelon form, we would have our work cut out for us! Fortunately, we can just remark that there are six vectors with five entries each. Since $6>5$, {prf:ref}`Thm:LinInd:MoreRowthanColmeansLinDep` guarantees that this set is linearly dependent.


::::::




::::::{prf:example} Application
:label: Example:Tab:LinInd:SoccerExample

Often, on news sites or in newspapers, you might see the standings of a football tournament displayed in a large table, as in {numref}`Tab:LinInd:SoccerExample`. Quite a lot of the information in such a table is redundant because some of the columns are linearly dependent.


:::{csv-table} The final standings of the first season of the Eredivisie football played in 1956-57, as shown on <a href=https://en.wikipedia.org/wiki/1992-93_FA_Premier_League>Wikipedia</a> on Wednesday, March 23rd 2022.
:class: longtable table-bordered table-striped table-hover
:name: Tab:LinInd:SoccerExample
:header-rows: 1

" ", "Team", "Pld", "W", "D", "L", "GF", "GA", "GD", "Pts"
"1", "AFC Ajax", "34", "22", "5", "7", "64", "40", "24", "49"
"2", "Fortuna '54", "34", "20", "5", "9", "76", "48", "28", "45"
"3", "SC Enschede", "34", "15", "11", "8", "81", "47", "34", "41"
"4", "MVV Maastricht", "34", "15", "10", "9", "53", "42", "11", "40"
"5", "PSV Eindhoven", "34", "18", "3", "13", "93", "71", "22", "39"
"6", "Feijenoord", "34", "15", "9", "10", "79", "58", "21", "39"
"7", "VVV '03", "34", "16", "6", "12", "50", "53", "-3", "38"
"8", "Sparta Rotterdam", "34", "12", "12", "10", "66", "59", "7", "36"
"9", "NAC", "34", "14", "8", "12", "59", "61", "-2", "36"
"10", "DOS", "34", "17", "1", "16", "79", "75", "4", "35"
"11", "Rapid JC", "34", "13", "7", "14", "64", "63", "1", "33"
"12", "NOAD", "34", "12", "7", "15", "54", "64", "-10", "31"
"13", "BVC Amsterdam", "34", "11", "8", "15", "49", "67", "-18", "30"
"14", "GVAV", "34", "9", "10", "15", "52", "66", "-14", "28"
"15", "BVV", "34", "11", "4", "19", "70", "76", "-6", "26"
"16", "Elinkwijk", "34", "10", "4", "20", "52", "87", "-35", "24"
"17", "Willem II", "34", "8", "6", "20", "59", "79", "-20", "22"
"18", "FC Eindhoven", "34", "8", "4", "22", "39", "83", "-44", "20"
:::

Each of the eight columns on the right can be interpreted as a vector with one entry per team, so a vector in $\mathbb{R}^{18}$. Using the column headers from {numref}`Tab:LinInd:SoccerExample` as the names of these vectors, we find:


$$

\mathbf{Pts}=2\mathbf{W}+1\mathbf{D}+0\mathbf{L}
$$

since a win yielded 2 points, a draw 1 point, and a loss 0 points. This means that $\left\lbrace\mathbf{W},\mathbf{D},\mathbf{L},\mathbf{Pts}\right\rbrace$ is a linearly dependent subset of $\mathbb{R}^{18}$. In fact, the smaller set $\left\lbrace\mathbf{W},\mathbf{D},\mathbf{Pts}\right\rbrace$ is already linearly dependent. Similarly, the column $\mathbf{GD}$, which gives the goal difference for each team, can be obtained by subtracting the column  $\mathbf{GA}$, which gives the goals conceded, from $\mathbf{GF}$, which gives the goals scored.


::::::


