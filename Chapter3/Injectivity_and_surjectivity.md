# Injectivity, Surjectivity, and Bijectivity

Since matrices correspond to linear transformations, we can translate questions about matrices to questions about linear transformations. For example: under what conditions on $A$ is the system $A\vect{x}=\vect{b}$ consistent for all $\vect{b}$? This question, which deals with a matrix $A$, is equivalent to the following question about linear transformations: when is every element in the codomain of a linear tranformation the image of some element in the domain?

Or, similarly: under what conditions on $A$ is every consistent system $A\vect{x}=\vect{b}$ uniquely solvable? In the language of linear transformations, this becomes: is every element in the range of a linear transformation the image of a unique element in the domain?

These two questions give rise to the concepts of injective and surjective linear transformations. The two concepts are very closely related and for most statements about injective linear transformations you can find an analogous statement about surjective linear transformations and vice versa.

%When studying a linear transformation, the following questions come up naturally: "Is every element in the codomain the image of some element in the domain?" and "Is every element in the range the image of **exactly one** element in the domain?" These two questions give rise to the concepts of injective and surjective linear transformations. The two concepts are very closely related and for most statements about injective linear transformations you can find an analogous statement about surjective linear transformations and vice versa.

(Subsec:InjSurj:Inj)=

## Injectivity

::::::{prf:definition}
We call a linear transformation $T:\mathbb{R}^{n}\to\mathbb{R}^{m}$ **injective** or **one-to-one** if $T(\mathbf{v}_{1})=T(\mathbf{v}_{2})$ implies $\mathbf{v}_{1}=\mathbf{v}_{2}$.

::::::

Intuitively, a transformation $T$ is injective if it can be undone without ambiguity. Let us see what this means for some concrete examples.

::::::{prf:example}
:label: Ex:InjSurj:InjEx

<ol type = "i">
<li id="Item:InjSurj:NonInjEx">

Consider the linear transformation, illustrated in {numref}`Figure %s <Fig:InjSurj:NonInjEx>`,

$$
T:\mathbb{R}^{2}\to\mathbb{R}^{2},\quad\mathbf{v}\mapsto A\mathbf{v}\quad\quad\text{where}\quad\quad A=\begin{bmatrix}
	1&-1\\
	-1&1
	\end{bmatrix}.
$$

This is not an injective transformation. Indeed, if we put for example

$$
\mathbf{v}_{1}=\begin{bmatrix}1\\2\end{bmatrix},\quad\mathbf{v}_{2}=\begin{bmatrix}-3\\-2\end{bmatrix},\quad\text{and}\quad\mathbf{u}=\begin{bmatrix}-1\\1\end{bmatrix}
$$

we find $T(\mathbf{v}_{1})=\mathbf{u}=T(\mathbf{v}_{2})$. Consequently, i $T(\vect{v})=\vect{u}$, we have no way of knowing whether the $\vect{v}=\mathbf{v}_{1}$ or $\vect{v}=\mathbf{v}_{2}$. Or perhaps some other vector, because there are infinitely many possible inputs that yield $\mathbf{u}$ as output. To find them, it suffices to solve the system $A\mathbf{x}=\mathbf{u}$. We find

$$
\left[\begin{array}{cc|c}
	1&-1&-1\\
	-1&1&1
\end{array}\right]\sim\left[\begin{array}{cc|c}
	1&-1&-1\\
	0&0&0
\end{array}\right]
$$

so any vector $\mathbf{v}=\begin{bmatrix}a_{1}\\a_{2}\end{bmatrix}$ with $a_{1}=a_{2}-1$ is a solution.

::::{figure} Images/Fig-InjSurj-NonInjEx.svg
:name: Fig:InjSurj:NonInjEx
:class: dark-light

The transformation $T$ from {prf:ref}`Ex:InjSurj:InjEx` [i.](#Item:InjSurj:NonInjEx) . All vectors on the <span class="only-light">black</span><span class="only-dark">white</span> line on the left, in particular $\mathbf{v}_{1}$ and $\mathbf{v}_{2}$, are mapped to the vector $\mathbf{u}$ on the right. Similarly, all vectors on the blue line are mapped to $\mathbf{0}$. Since there is not just one vector on these lines, $T$ is not injective.
::::

</li>
<li id="Item:InjSurj:InjEx">

Consider now the transformation

$$
T:\mathbb{R}^{2}\to\mathbb{R}^{2},\quad\mathbf{v}\mapsto A\mathbf{v}\quad\quad\text{where}\quad\quad A=\begin{bmatrix}
	1&-1\\
	1&1
	\end{bmatrix}
$$

which is illustrated in {numref}`Figure %s <Fig:InjSurj:InjEx>`.

This is an injective transformation. Indeed, if we take an arbitrary vector $\mathbf{v}=\begin{bmatrix}a_{1}\\a_{2}\end{bmatrix}$ in $\mathbb{R}^{2}$ and we try to solve $A\mathbf{x}=\mathbf{u}$, we find

$$
\left[\begin{array}{cc|c}
	1&-1&a_{1}\\
	1&1&a_{2}
\end{array}\right]\sim\left[\begin{array}{cc|c}
	1&-1&a_{1}\\
	0&2&a_{2}-a_{1}
\end{array}\right].
$$

There are no free variables, so if there is a solution to the system $A\vect{x}=\vect{v}$ (which, in this case, is true for all $\vect{v}$) it will be unique. This means that there is only one $\mathbf{x}$ with $T(\mathbf{x})=A\mathbf{x}=\mathbf{u}$, hence $T$ is injective.

```{applet}
:url: injectivity_and_surjectivity/injsurj-injex-example3
:fig: Images/Fig-InjSurj-InjEx.svg
:name: Fig:InjSurj:InjEx
:class: dark-light

The transformation $T$ from {prf:ref}`Ex:InjSurj:InjEx` [ii.](#Item:InjSurj:InjEx) and {prf:ref}`Ex:InjSurj:SurjEx` [ii.](#Item:InjSurj:SurjEx) acting on some selected vectors. Note that this transformation scales vectors and rotates them. For any vector $\mathbf{u}$ on the right, you can find only one vector $\mathbf{v}$ on the left such that $T(\mathbf{v})=\mathbf{u}$. Hence $T$ is injective.
```

</li>

<li id="Item:InjSurj:InjExNonEqDim">

Let us consider now a transformation for which the domain and the codomain are different. Take, for example,

$$
S:\R^{2}\to\R^{3},\vect{v}\mapsto A\vect{v}\quad\text{where}\quad A=\begin{bmatrix}
1&0\\
0&1\\
0&0
\end{bmatrix}.
$$

Then $S$ is an injective transformation. Indeed, take an arbitrary vector

$$
\vect{v}=\begin{bmatrix}
a_{1}\\
a_{2}\\
a_{3}
\end{bmatrix}\text{ in }\R^{3}.\quad\text{Then}\quad\left[\begin{array}{cc|c}
	1&0&a_{1}\\
	0&1&a_{2}\\
	0&0&a_{3}
	\end{array}\right]
$$

</li>
has, when it is consistent, a unique solution as there are no free variables.

</ol>

::::::

::::{exercise}

```{applet}
:url: injectivity_and_surjectivity/injsurj-injex-example
:fig: Images/Fig-InjSurj-InjEx.svg
:name: Fig:InjSurj:InjExExample
:class: dark-light

 You can select any of three transformations using the dropdown menu on the bottom. Find out which of these are injective by seeing whether you can find vectors $\vect{v}_{1}\neq \vect{v}_{2}$ that have the same image under $T$ by dragging the vectors on the left.
```

::::

If we perform two actions which can both be undone, then we should be able to undo the combination of those two actions. That this intuitive rule really does hold is essentially the content of {prf:ref}`Prop:InjSurj:InjafterInjisInj`.

::::::{prf:proposition}
:label: Prop:InjSurj:InjafterInjisInj

If $S:\mathbb{R}^{l}\to\mathbb{R}^{m}$ and $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ are both injective, then so is $T\circ S:\mathbb{R}^{l}\to\mathbb{R}^{n}$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:InjSurj:InjafterInjisInj`
:class: tudproof

Take $\mathbf{v}_{1}$ and $\mathbf{v}_{2}$ in $\mathbb{R}^{l}$ such that $(T\circ S)(\mathbf{v}_{1})=(T\circ S)(\mathbf{v}_{2})$, i.e. $T(S(\mathbf{v}_{1}))=T(S(\mathbf{v}_{2}))$. Since $T$ is injective, we must have $S(\mathbf{v}_{1})=S(\mathbf{v}_{2})$. As $S$ is also injective, this in turn implies $\mathbf{v}_{1}=\mathbf{v}_{2}$ which establishes injectivity of $T\circ S$.

::::::

You may think that, similarly, if the combination of two actions can be undone, you must be able to undo both. This, however, is generally not true, as {prf:ref}`Ex:InjSurj:InjnonInjInj` shows.

::::::{prf:example}
:label: Ex:InjSurj:InjnonInjInj

Consider

$$
S:\mathbb{R}^{2}\to\mathbb{R}^{3},\mathbf{v}\mapsto \begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix}\mathbf{v}\quad\text{and}\quad T:\mathbb{R}^{3}\to\mathbb{R}^{2},\mathbf{v}\mapsto \begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}\mathbf{v}.
$$

You can verify yourself that $(T\circ S)\mathbf{v}=\mathbf{v}$ for any vector $\mathbf{v}$ in $\mathbb{R}^{2}$, so $T\circ S$ is injective. But $T$ itself definitely isn't! Indeed

$$
T\left(\begin{bmatrix}0\\0\\a_{3}\end{bmatrix}\right)=\mathbf{0}\quad\text{for any $a_{3}$ in $\R$}.
$$

Note that $S$ is injective by {prf:ref}`Ex:InjSurj:InjEx` [iii.](#Item:InjSurj:InjExNonEqDim) This is not a coincidence, as {prf:ref}`Prop:InjSurj:CompInjFirstInj` shows.

::::::


::::::{prf:proposition}
:label: Prop:InjSurj:CompInjFirstInj

If $S:\mathbb{R}^{l}\to\mathbb{R}^{m}$ and $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ are such that $T\circ S$ is injective, then $S$ is injective.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:InjSurj:CompInjFirstInj`
:class: tudproof

Suppose $T\circ S$ is injective but $S$ is not. Then there are $\mathbf{v}_{1}\neq\mathbf{v}_{2}$ in $\mathbb{R}^{l}$ such that $S(\mathbf{v}_{1})=S(\mathbf{v}_{2})$. But then $T(S(\mathbf{v}_{1}))=T(S(\mathbf{v}_{2}))$ which contradicts the assumption that $T\circ S$ is injective.

::::::

All the results we have obtained so far hold true for general transformations. But there are some extra characterizations we can prove for linear transformations.

::::::{prf:proposition}
:label: Prop:InjSurj:InjChars

Let $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ be a linear transformation with standard matrix $A$. Then the following are equivalent:

<ol type = "i">
<li>

$T$ is injective;

</li>
<li id="Item:InjSurj:InjisUniqueSol">

$A\mathbf{x}=\mathbf{b}$ has, for every $\mathbf{b}$ in $\mathbb{R}^{n}$, **at most** one solution;

</li>
<li>

$A$ has a pivot in every **column**.

</li>
</ol>

::::::

::::{exercise}
:label: Exc:InjSurj:InjChars

Prove {prf:ref}`Prop:InjSurj:InjChars`.

::::

:::{admonition} Solution to&nbsp;{numref}`Exc:InjSurj:InjChars`
:class: solution, dropdown

Assume $T$ is injective and $A\vect{x}=\vect{b}$ has solutions $\vect{x}_{1}$ and $\vect{x}_{2}$. Then $T(\vect{x}_{1})=T(\vect{x}_{2})$, so $\vect{x}_{1}=\vect{x}_{2}$ by injectivity of $T$. Similarly, if we assume that $A\vect{x}=\vect{b}$ has at most one solution, then $T(\vect{x}_{1})=T(\vect{x}_{2})$ would imply $\vect{x}_{1}=\vect{x}_{2}$, hence $T$ is injective.

If $A$ has a column without pivot, then there is a free variable. Consequently, if $A\vect{x}=\vect{b}$ has a solution, it has infinitely many, contradicting [ii.](#Item:InjSurj:InjisUniqueSol). Similarly, if $A\vect{x}=\vect{b}$ has at most one solution, then there cannot be a free variable, hence $A$ has no column without pivot.

:::

::::::{prf:corollary}
:label: Col:InjSurj:mgreatern
If $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ is injective, then $m\leq n$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Col:InjSurj:mgreatern`
:class: tudproof

If $T$ is injective, then its standard matrix $A$ has a pivot in every column. Consequently, the number of columns of $A$, which is $m$, must be smaller than or equal to the number of rows of $A$, which is $n$.

::::::

::::::{prf:proposition}
:label: Col:InjSurj:viszero

A linear transformation $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ is injective if and only if $T(\mathbf{v})=\mathbf{0}$ implies $\mathbf{v}=\mathbf{0}$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Col:InjSurj:viszero`
:class: tudproof

Since $T(\mathbf{0})=\mathbf{0}$ for any linear transformation $T$, injectivity of $T$ implies that $T(\mathbf{v})=\mathbf{0}$ only occurs when $\mathbf{v}=\mathbf{0}$.

Assume now that $T(\mathbf{v})=\mathbf{0}$ implies $\mathbf{v}=\mathbf{0}$. If $T(\mathbf{v}_{1})=T(\mathbf{v}_{2})$ for some $\mathbf{v}_{1},\mathbf{v}_{2}$ in $\mathbb{R}^{m}$, then $T(\mathbf{v}_{1}-\mathbf{v}_{2})=T(\mathbf{v}_{1})-T(\mathbf{v}_{2})=\mathbf{0}$ since $T$ is linear. By our assumption, $\mathbf{v}_{1}-\mathbf{v}_{2}=\mathbf{0}$ follows. But then $\mathbf{v}_{1}=\mathbf{v}_{2}$. We have shown that two vectors can only have the same image under $T$ if they are the same to start with, i.e. we have shown $T$ to be injective.

::::::

(Subsec:InjSurj:Surj)=

## Surjectivity

In this section, we will talk about surjectivity. It is a natural complement to the concept of injectivity -- the yin to its yang, if you will. This duality becomes apparent when comparing {prf:ref}`Prop:InjSurj:InjChars` to {prf:ref}`Prop:InjSurj:SurjChars`.

::::::{prf:definition}
A linear transformation $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ is called **surjective** if for any vector $\mathbf{u}$ in $\mathbb{R}^{n}$ there is some vector $\mathbf{v}$ in $\mathbb{R}^{m}$ such that $T(\mathbf{v})=\mathbf{u}$. In other words, $T$ is surjective if and only if the range of $T$ is the whole codomain.

::::::

In other words, a transformation is surjective if for every potential output there is some input which really does give that output. We will now see what this concept means for the transformations from {prf:ref}`Ex:InjSurj:InjEx`.

::::::{prf:example}
:label: Ex:InjSurj:SurjEx

<ol type = "i">
<li id="Item:InjSurj:NonSurjEx">

Let us start with the transformation, illustrated in {numref}`Figure %s <Fig:InjSurj:NonSurjEx>`,

$$
T:\mathbb{R}^{2}\to\mathbb{R}^{2},\quad\mathbf{v}\mapsto A\mathbf{v}\quad\quad\text{where}\quad\quad A=\begin{bmatrix}
	1&-1\\
	-1&1
	\end{bmatrix}.
$$

In order to see whether $T$ is surjective, we have to check whether for every vector $\mathbf{u}$ in the codomain -- that is $\mathbb{R}^{2}$ here -- there is a vector $\mathbf{v}$ in the domain with $T(\mathbf{v})=\mathbf{u}$. So take $\mathbf{u}=\begin{bmatrix}a_{1}\\a_{2}\end{bmatrix}$ in $\mathbb{R}^{2}$. We find

$$
\left[\begin{array}{cc|c}
	1&-1&a_{1}\\
	-1&1&a_{2}
\end{array}\right]\sim\left[\begin{array}{cc|c}
	1&-1&-1\\
	0&0&a_{1}+a_{2}
\end{array}\right],
$$

so the system $A\mathbf{x}=\mathbf{u}$ can only be solved if $a_{1}+a_{2}=0$. This transformation is therefore not surjective.

```{applet}
:url: injectivity_and_surjectivity/injsurj-nonsurjex
:fig: Images/Fig-InjSurj-NonSurjEx.svg
:name: Fig:InjSurj:NonSurjEx
:class: dark-light

The transformation $T$ from {prf:ref}`Ex:InjSurj:SurjEx` [i.](#Item:InjSurj:NonSurjEx) . The green line is the collection of all $\mathbf{b}$ for which the system $A\mathbf{x}=\mathbf{b}$ is consistent where $A$ is the standard matrix of $T$. Since this is not all of $\mathbb{R}^{2}$, $T$ is not surjective.
```

</li>
<li id="Item:InjSurj:SurjEx">

We have already seen in {prf:ref}`Ex:InjSurj:InjEx` [ii.](#Item:InjSurj:InjEx) that, for

$$
A=\begin{bmatrix}
	1&-1\\
	1&1
	\end{bmatrix},
$$

the system $A\mathbf{x}=\mathbf{u}$ is consistent for any $\mathbf{u}$ in $\mathbb{R}^{2}$. Consequently, the linear transformation

$$
T:\mathbb{R}^{2}\to\mathbb{R}^{2},\quad\mathbf{v}\mapsto A\mathbf{v}
$$

is surjective.

</li>
</ol>

```{applet}
:url: injectivity_and_surjectivity/injsurj-injex
:fig: Images/Fig-InjSurj-InjEx.svg
:name: Fig:InjSurj:SurjEx
:class: dark-light

The transformation $T$ from {prf:ref}`Ex:InjSurj:SurjEx` [ii.](#Item:InjSurj:SurjEx) acting on some selected vectors. Note that this transformation scales vectors and rotates them. For any vector $\mathbf{u}$ on the right, you can find a vector $\mathbf{v}$ on the left such that $T(\mathbf{v})=\mathbf{u}$. Hence $T$ is surjective.
```

::::::


::::{exercise}

```{applet}
:url: injectivity_and_surjectivity/injsurj-injex-example2
:fig: Images/Fig-InjSurj-InjEx.svg
:name: Fig:InjSurj:InjExExample
:class: dark-light

 You can select any of three transformations using the dropdown menu on the bottom. Find out for which of these $\vect{u}$ is in the range of $T$ by dragging the vector on the left.
```

::::

::::::{prf:proposition}
:label: Prop:InjSurj:SurjafterSurjisSurj

If $S:\mathbb{R}^{l}\to\mathbb{R}^{m}$ and $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ are both surjective, then so is $T\circ S:\mathbb{R}^{l}\to\mathbb{R}^{n}$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:InjSurj:SurjafterSurjisSurj`
:class: tudproof

Take $\mathbf{u}$ in $\mathbb{R}^{n}$. As $T$ is surjective, there is a $\mathbf{v}\in\mathbb{R}^{m}$ with $T(\mathbf{v})=\mathbf{u}$. Since $S$ is surjective, there is a $\mathbf{w}$ in $\mathbb{R}^{l}$ with $S(\mathbf{w})=\mathbf{v}$. We find $(T\circ S)(\mathbf{w})=T(\mathbf{v})=\mathbf{u}$, so $T\circ S$ is surjective, as claimed.

::::::

Here, too, it turns out that the opposite statement is not true in general as {prf:ref}`Ex:InjSurj:NonSurjSurjSurj` shows. Compare this with {prf:ref}`Ex:InjSurj:InjnonInjInj`.

::::::{prf:example}
:label: Ex:InjSurj:NonSurjSurjSurj

Put

$$
S:\mathbb{R}^{2}\to\mathbb{R}^{3},\mathbf{v}\mapsto \begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix}\mathbf{v}\quad\text{and}\quad T:\mathbb{R}^{3}\to\mathbb{R}^{2},\mathbf{v}\mapsto \begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}\mathbf{v}.
$$

As we have seen in {prf:ref}`Ex:InjSurj:InjnonInjInj`, $(T\circ S)(\mathbf{v})=\mathbf{v}$ for any vector $\mathbf{v}$ in $\mathbb{R}^{2}$, so $T\circ S$ is surjective. But $S$ is not! Indeed,

$$
\text{for any}\quad \mathbf{v}=\begin{bmatrix}a_{1}\\a_{2}\end{bmatrix}\quad\text{in $\R^{2}$ we have}\quad S(\mathbf{v})=\begin{bmatrix}a_{1}\\a_{2}\\0\end{bmatrix}
$$

so any vector $\mathbf{u}$ in $\mathbb{R}^{3}$ for which the third entry is non-zero cannot be $S(\mathbf{v})$ for any $\mathbf{v}$ in $\mathbb{R}^{2}$.

::::::

The following two propositions are counterparts of {prf:ref}`Prop:InjSurj:CompInjFirstInj` and {prf:ref}`Prop:InjSurj:InjChars`, respectively.

::::::{prf:proposition}
:label: Prop:InjSurj:CompSurjSecondSurj

If $S:\mathbb{R}^{l}\to\mathbb{R}^{m}$ and $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ are such that $T\circ S$ is surjective, then $T$ is surjective.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:InjSurj:CompSurjSecondSurj`
:class: tudproof

Take $\mathbf{u}\in\mathbb{R}^{n}$. Since $T\circ S$ is surjective, there is a $\mathbf{w}$ in $\mathbb{R}^{l}$ with $\mathbf{u}=(T\circ S)(\mathbf{w})=T(S(\mathbf{w}))$. Hence $\mathbf{u}=T(\mathbf{v})$ for $\mathbf{v}=S(\mathbf{w})$, which shows $T$ to be surjective.

::::::

::::::{prf:proposition}
:label: Prop:InjSurj:SurjChars

Let $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ be a linear transformation with standard matrix $A$. Then the following are equivalent:

<ol type = "i">
<li>

$T$ is surjective;

</li>
<li>

$A\mathbf{x}=\mathbf{b}$ has, for every $\mathbf{b}$ in $\mathbb{R}^{n}$, **at least** one solution;

</li>
<li>

$A$ has a pivot in every **row**.

</li>
</ol>

::::::

::::{exercise}
:label: Exc:InjSurj:SurjChars

Prove {prf:ref}`Prop:InjSurj:SurjChars`.

::::

:::{admonition} Solution to&nbsp;{numref}`Exc:InjSurj:SurjChars`
:class: solution, dropdown

Assume $T$ is surjective and take an arbitrary $\vect{b}$ in $\R^{n}$. Then there is an $\vect{x}$ in $\mathbb{R}^{m}$ such that $T(\vect{x})=\vect{b}$, i.e. $\vect{x}$ is a solution of $A\vect{x}=\vect{b}$. Similarly, if $A\vect{x}=\vect{b}$ has a solution for any $\vect{b}$ in $\R^{n}$, then $\vect{b}=T(\vect{x})$ which establishes surjectivity of $T$.

If $A$ has a row without pivot, then, for a well-chosen $\vect{b}$, a pivot can appear in the last column of the augmented matrix $[A|\vect{b}]$. This means that $A\vect{x}=\vect{b}$ has no solutions. Similarly, if $A\vect{x}=\vect{b}$ always has a solution, then $[A|\vect{b}]$ can never have a pivot in the lost column. Consequently, $A$ must have a pivot in every row.

:::

::::::{prf:corollary}
:label: Col:InjSurj:mn2

If $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ is surjective, then $m\geq n$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Col:InjSurj:mn2`
:class: tudproof

If $T$ is surjective, then its standard matrix $A$ has a pivot in every row. Consequently, the number of columns of $A$, which is $m$, must be greater than or equal to the number of rows of $A$, which is $n$.

::::::

## Bijectivity

In this section, we investigate what happens when injectivity and surjectivity meet. Let us start with giving that idea a name.

::::::{prf:definition}
A linear transformation $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ is called **bijective** if it is both injective and surjective.

::::::

Although we allow $m$ and $n$ to be different in the definition, it turns out that this cannot happen as the following proposition shows.

::::::{prf:proposition}
:label: Prop:InjSurj:mequaln

If a linear transformation $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ is bijective, then $m=n$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:InjSurj:mequaln`
:class: tudproof

Let $A$ be the standard matrix of $T$, which is an $n\times m$ matrix. By {prf:ref}`Prop:InjSurj:InjChars`, the number of pivots in $A$ is $m$. By {prf:ref}`Prop:InjSurj:SurjChars`, the number of pivots in $A$ is $n$. Hence the claim follows.

::::::

If the domain and codomain are both $\mathbb{R}^{n}$ then something striking happens: injectivity, surjectivity, and bijectivity all become equivalent!

::::::{prf:proposition}
:label: Prop:InjSurj:Equiv

Let $T:\mathbb{R}^{n}\to\mathbb{R}^{n}$ be a linear transformation. The following are equivalent:

<ol type = "i">

<li>

$T$ is injective;

</li>

<li>

$T$ is surjective;

</li>

<li>

$T$ is bijective.

</li>

</ol>

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:InjSurj:Equiv`
:class: tudproof

It suffices to show that $T$ is injective if and only if it is surjective. Assume $T$ is injective. Then the standard matrix $A$ of $T$ has a pivot in each column. But as the number of columns and the number of rows are the same, there must be a pivot in each row, showing surjectivity of $T$.

Similarly, if $T$ is surjective, then the standard matrix $A$ of $T$ has a pivot in each column. Again, the number of columns is the same as the number of rows, so there is also a pivot in every row and we conclude that $T$ must be injective.

::::::

The content of {prf:ref}`Prop:InjSurj:BijIsInv` is, intuitively, that a transformation is bijective if and only if it can be undone by some linear transformation.

:::{prf:proposition}
:label: Prop:InjSurj:BijIsInv

For a linear transformation $T:\R^{n}\to\R^{n}$ with standard matrix $A$ the following are equivalent:

<ol type="i">
<li id="It:InjSurj:TBij">

$T$ is bijective.

</li>

<li id="It:InjSurj:AInv">

$A$ is invertible.

</li>

<li id="It:InjSurj:TInv">

There exists a transformation $S:\R^{n}\to\R^{n}$ such that

$$ST(\vect{v})=\vect{v}=TS(\vect{v})$$

for any vector $\vect{v}$ in $\R^{n}$.

</li>

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:InjSurj:BijIsInv`
:class: tudproof

By {prf:ref}`Thm:MatrixInv:InvertibilityCharacterizations`, we know that $A$ is invertible if and only if the system $\vect{x}=\vect{b}$ has a unique solution for each $\vect{b}$ in $\R^{n}$. The existence of a solution is equivalent to surjectivity of $T$ and its uniqueness is equivalent to injectivity of $T$. This establishes the equivalence of [i.](#It:InjSurj:TBij) and [ii.](#It:InjSurj:AInv)

We will now show that [ii.](#It:InjSurj:AInv) and [iii.](#It:InjSurj:TInv) are equivalent, too. The invertibility of $A$ is equivalent to the existence of an $n\times n$-matrix $B$ such that $AB=I$. Define

$$S:\R^{n}\to\R^{n},\vect{v}\mapsto B\vect{v}.$$

Then $TS(\vect{v})=AB\vect{v}=\vect{v}$ for any $\vect{v}$ in $\R^{n}$. The only thing left to show is $ST(\vect{v})=\vect{v}$ or, in other words, $BA(\vect{v})=\vect{v}$ for any $\vect{v}$ in $\R^{n}$. For this, we argue as follows. Since $AB=I$, $ABA=A$ follows. But then $A(BA-I)=0$, hence $A((BA-I)\vect{v})=\vect{0}$ for all $\vect{v}$ in $\R^{n}.$ Since $A$ is invertible, $A\vect{x}=\vect{0}$ only has the trivial solution $\vect{x}=\vect{0}$. Therefore $(BA-I)\vect{v}=\vect{0}$ for all $\vect{v}$ which implies $BA\vect{v}=\vect{v}$ for all $\vect{v}$ in $\R^{n}$.

:::

## Grasple Exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a5fcbee0-9af1-4596-b3d4-05dcdf7640b3?id=92235
:label: grasple_exercise_3_5_1
:dropdown:
:description: Is $T$ injective, surjective, bijective, or neither?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ba7d83d3-c00a-4d8b-910e-84e6a12b28e4?id=92236
:label: grasple_exercise_3_5_2
:dropdown:
:description: Is $T$ injective, surjective, bijective, or neither?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a92c3a97-1bf0-47dc-a549-c1130d053e33?id=92237
:label: grasple_exercise_3_5_3
:dropdown:
:description: Is $T$ injective, surjective, bijective, or neither?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a18a8d11-11f0-4bce-96f9-39946d6543a9?id=92238
:label: grasple_exercise_3_5_4
:dropdown:
:description: What can we conclude if the composition of two transformations is bijective?

::::
