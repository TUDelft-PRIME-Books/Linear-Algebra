# Injectivity, Surjectivity, and Bijectivity

When studying a linear transformation, two questions come up naturally: "Is every element in the codomain the image of some element in the domain?" and "Is every elment in the range the image of **exactly one** element in the domain?" These two questions give rise to the concepts of injective and surjective linear transformations. The two concepts are very closely related and for most statements about injective linear transformations you can find an analogous statement about surjective linear transformations and vice versa.


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

we find $T(\mathbf{v}_{1})=\mathbf{u}=T(\mathbf{v}_{2})$. Consequently, if we know that, for some input vector $\mathbf{v}$, the transformation $T$  gives $\mathbf{u}$ as output, we have no way of knowing whether the original input was $\mathbf{v}_{1}$ or $\mathbf{v}_{2}$. In fact, there are infinitely many possible inputs that yield $\mathbf{u}$ as output. To find them, it suffices to solve the system $A\mathbf{x}=\mathbf{u}$. We find


$$
\left[\begin{array}{cc|c}
	1&-1&-1\\
	-1&1&1
\end{array}\right]\sim\left[\begin{array}{cc|c}
	1&-1&-1\\
	0&0&0
\end{array}\right]
$$

so any vector  $\mathbf{v}=\begin{bmatrix}a_{1}\\a_{2}\end{bmatrix}$ with $a_{1}=a_{2}-1$ is a solution.



::::{figure} Images/Fig-InjSurj-NonInjEx.svg
:name: Fig:InjSurj:NonInjEx

The transformation $T$ from {prf:ref}`Ex:InjSurj:InjEx` [i.](#Item:InjSurj:NonInjEx) . All vectors on the black line on the left, in particular $\mathbf{v}_{1}$ and $\mathbf{v}_{2}$, are mapped to the vector $\mathbf{u}$ on the right. Similarly, all vectors on the blue line are mapped to $\mathbf{0}$. Since there is not just one vector on the these lines, $T$ is not injective.
::::



</li>
<li id="Item:InjSurj:InjEx">

Consider now 

$$
T:\mathbb{R}^{2}\to\mathbb{R}^{2},\quad\mathbf{v}\mapsto A\mathbf{v}\quad\quad\text{where}\quad\quad A=\begin{bmatrix}
	1&-1\\
	1&1
	\end{bmatrix}.
$$

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

This system is consistent regardless of $a_{1}$ and $a_{2}$ and there are no free variables, so there is always a **unique** solution. This means that there is only one $\mathbf{x}$ with $T(\mathbf{x})=A\mathbf{x}=\mathbf{u}$, hence $T$ is injective.

::::{figure} Images/Fig-InjSurj-InjEx.svg
:name: Fig:InjSurj:InjEx

The transformation $T$ from {prf:ref}`Ex:InjSurj:InjEx` [ii.](#Item:InjSurj:InjEx)  and {prf:ref}`Ex:InjSurj:SurjEx` [ii.](#Item:InjSurj:SurjEx)  acting on some selected vectors. Note that this transformation scales vectors and rotates them. For any vector $\mathbf{u}$ on the right, you can find only one vector $\mathbf{v}$ on the left such that $T(\mathbf{v})=\mathbf{u}$. Hence $T$ is injective.
::::

</li>
</ol>

::::::


If we perform two actions which can both be undone, then we should be able to undo the combination of those two actions. That this intuitive rule really does hold is essentially the content of {prf:ref}`Prop:InjSurj:InjafterInjisInj`.


::::::{prf:proposition}
:label: Prop:InjSurj:InjafterInjisInj

If $S:\mathbb{R}^{l}\to\mathbb{R}^{m}$ and $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ are both injective, then so is $T\circ S:\mathbb{R}^{l}\to\mathbb{R}^{n}$.

::::::


::::::{prf:proof}
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


Note that $S$ is injective. This is not a coincidence, as {prf:ref}`Prop:InjSurj:CompInjFirstInj` shows.


::::::



::::::{prf:proposition}
:label: Prop:InjSurj:CompInjFirstInj

If $S:\mathbb{R}^{l}\to\mathbb{R}^{m}$ and $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ are such that $T\circ S$ is injective, then $S$ is injective.

::::::


::::::{prf:proof}
Suppose $S$ is not injective. Then there are $\mathbf{v}_{1}\neq\mathbf{v}_{2}$ in $\mathbb{R}^{l}$ such that $S(\mathbf{v}_{1})=S(\mathbf{v}_{2})$. But then $T(S(\mathbf{v}_{1}))=T(S(\mathbf{v}_{2}))$ which contradicts the assumption that $T\circ S$ is injective.

::::::


All the results we have obtained so far hold true for general transformations. But there are some extra characterizations we can prove for linear transformations.


::::::{prf:proposition}
:label: Prop:InjSurj:InjChars

Let $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ be a linear transformation with standard matrix $A$. Then the following are equivalent:
<ol type = "i">
<li>

$T$ is injective;
	

</li>
<li>

$A\mathbf{x}=\mathbf{b}$ has, for every $\mathbf{b}$ in $\mathbb{R}^{n}$, **at most** one solution;

</li>
<li>

$A$ has a pivot in every **column**.

</li>
</ol>

::::::


::::::{prf:proof}
Exercise.


::::::


::::::{prf:corollary}
If $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ is injective, then $m\leq n$.

::::::

::::::{prf:proof}
If $T$ is injective, then its standard matrix $A$ has a pivot in every column. Consequently, the number of columns of $A$, which is $m$, must be smaller than or equal to the number of rows of $A$, which is $n$.

::::::



::::::{prf:proposition}
A linear transformation $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ is injective if and only if $T(\mathbf{v})=\mathbf{0}$ implies $\mathbf{v}=\mathbf{0}$.

::::::


::::::{prf:proof}

Since $T(\mathbf{0})=\mathbf{0}$ for any linear transformation $T$, injectivity of $T$ implies that $T(\mathbf{v})=\mathbf{0}$ only occurs when $\mathbf{v}=\mathbf{0}$.

Assume now that $T(\mathbf{v})=\mathbf{0}$ implies $\mathbf{v}=\mathbf{0}$. If $T(\mathbf{v}_{1})=T(\mathbf{v}_{2})$ for some $\mathbf{v}_{1},\mathbf{v}_{2}$ in $\mathbb{R}^{m}$, then $T(\mathbf{v}_{1}-\mathbf{v}_{2})=T(\mathbf{v}_{1})-T(\mathbf{v}_{2})=\mathbf{0}$ since $T$ is linear. By our assumption, $\mathbf{v}_{1}-\mathbf{v}_{2}=\mathbf{0}$ follows. But then $\mathbf{v}_{1}=\mathbf{v}_{2}$. We have shown that two vectors can only have the same image under $T$ if they are the same to start with, i.e. we have shown $T$ to be injective.


::::::


(Subsec:InjSurj:Surj)=
## Surjectivity


In this section, we will talk about surjectivity. It is a natural complement to the concept of injectivity -- the yin to its yang, if you will.


::::::{prf:definition}
A linear transformation $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ is called **surjective** if for any vector $\mathbf{u}$ in $\mathbb{R}^{n}$ there is some vector $\mathbf{v}$ in $\mathbb{R}^{m}$ such that $T(\mathbf{v})=\mathbf{u}$. In other words, $T$ is surjective if and only if the range of $T$ is the whole codomain.

::::::

In other words, a transformation is surjective if for every potential output there is some input which really does give that output. We will now see what this concept means for the transformations from {prf:ref}`Ex:InjSurj:InjEx`.


::::::{prf:example}
:label: Ex:InjSurj:SurjEx

<ol type = "i">
<li id="Item:InjSurj:NonSurjEx">

Let us start with the transformation,  illustrated in {numref}`Figure %s <Fig:InjSurj:NonSurjEx>`, 

$$
T:\mathbb{R}^{2}\to\mathbb{R}^{2},\quad\mathbf{v}\mapsto A\mathbf{v}\quad\quad\text{where}\quad\quad A=\begin{bmatrix}
	1&-1\\
	-1&1
	\end{bmatrix}.
$$

In order to see whether $T$ is surjective, we have to check whether for every vector $\mathbf{u}$ in the codomain -- that is $\mathbb{R}^{2}$ here -- there is a vector $\mathbf{v}$ in the domain with $T(\mathbf{v})=\mathbf{u}$. So take  $\mathbf{u}=\begin{bmatrix}a_{1}\\a_{2}\end{bmatrix}$ in $\mathbb{R}^{2}$. We find 

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


::::{figure} Images/Fig-InjSurj-NonInjEx.svg
:name: Fig:InjSurj:NonSurjEx

The transformation $T$ from {prf:ref}`Ex:InjSurj:SurjEx` [i.](#Item:InjSurj:NonSurjEx) .  The green line on the right is the collection of all $\mathbf{b}$ for which the system $A\mathbf{x}=\mathbf{b}$ is consistent where $A$ is the standard matrix of $T$. Since this is not all of $\mathbb{R}^{2}$, $T$ is not surjective.
::::

</li>
<li id="Item:InjSurj:SurjEx">

We have already seen in {prf:ref}`Ex:InjSurj:InjEx` [ii.](#Item:InjSurj:InjEx)  that, for 

$$
A=\begin{bmatrix}
	1&-1\\
	1&1
	\end{bmatrix},
$$

the system $A\mathbf{x}=\mathbf{u}$ is solvable for any $\mathbf{u}$ in $\mathbb{R}^{2}$. Consequently, the linear transformation  

$$
T:\mathbb{R}^{2}\to\mathbb{R}^{2},\quad\mathbf{v}\mapsto A\mathbf{v}
$$

is surjective.


</li>
</ol>




::::{figure} Images/Fig-InjSurj-InjEx.svg
:name: Fig:InjSurj:SurjEx

The transformation $T$ from {prf:ref}`Ex:InjSurj:SurjEx` [ii.](#Item:InjSurj:SurjEx)  acting on some selected vectors. Note that this transformation scales vectors and rotates them. For any vector $\mathbf{u}$ on the right, you can find a vector $\mathbf{v}$ on the left such that $T(\mathbf{v})=\mathbf{u}$. Hence $T$ is surjective.
::::


::::::



::::::{prf:proposition}
:label: Prop:InjSurj:SurjafterSurjisSurj

If $S:\mathbb{R}^{l}\to\mathbb{R}^{m}$ and $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ are both surjective, then so is $T\circ S:\mathbb{R}^{l}\to\mathbb{R}^{n}$.


::::::


::::::{prf:proof}
Take $\mathbf{u}$ in $\mathbb{R}^{n}$. As $T$ is surjective, there is a $\mathbf{v}\in\mathbb{R}^{m}$ with $T(\mathbf{v})=\mathbf{u}$. Since $S$ is surjective, there is a $\mathbf{w}$ in $\mathbb{R}^{l}$ with $S(\mathbf{w})=\mathbf{v}$. We find $(T\circ S)(\mathbf{w})=T(\mathbf{v})=\mathbf{u}$, so $T\circ S$ is surjective, as claimed.

::::::


Here, too, it turns out that the opposite statement is not true in general as {prf:ref}`Ex:InjSurj:NonSurjSurjSurj` shows. Compare this with {prf:ref}`Ex:InjSurj:InjnonInjInj`.

::::::{prf:example}
:label: Ex:InjSurj:NonSurjSurjSurj

Put 

$$
S:\mathbb{R}^{2}\to\mathbb{R}^{3},\mathbf{v}\mapsto \begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix}\mathbf{v}\quad\text{and}\quad T:\mathbb{R}^{3}\to\mathbb{R}^{2},\mathbf{v}\mapsto \begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}\mathbf{v}.
$$


As we have seen in  {prf:ref}`Ex:InjSurj:InjnonInjInj`, $(T\circ S)(\mathbf{v})=\mathbf{v}$ for any vector $\mathbf{v}$ in $\mathbb{R}^{2}$, so $T\circ S$ is surjective. But $S$ is not! Indeed,  

$$
\text{for any}\quad \mathbf{v}=\begin{bmatrix}a_{1}\\a_{2}\end{bmatrix}\quad\text{in $\R^{2}$ we have}\quad S(\mathbf{v})=\begin{bmatrix}a_{1}\\a_{2}\\0\end{bmatrix}
$$

so any vector $\mathbf{u}$ in $\mathbb{R}^{3}$ for which the third entry is non-zero cannot be $S(\mathbf{v})$ for any $\mathbf{v}$ in $\mathbb{R}^{2}$.

::::::


The following two propositions are counterparts of {prf:ref}`Prop:InjSurj:CompInjFirstInj` and  {prf:ref}`Prop:InjSurj:InjChars`, respectively.

::::::{prf:proposition}
:label: Prop:InjSurj:CompSurjSecondSurj

If $S:\mathbb{R}^{l}\to\mathbb{R}^{m}$ and $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ are such that $T\circ S$ is surjective, then $T$ is surjective.

::::::





::::::{prf:proof}

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


::::::{prf:proof}
Exercise.

::::::


::::::{prf:corollary}
If $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ is surjective, then $m\geq n$.

::::::

::::::{prf:proof}
If $T$ is surjective, then its standard matrix $A$ has a pivot in every row. Consequently, the number of columns of $A$, which is $m$, must be greater than or equal to the number of rows of $A$, which is $n$.

::::::


## Bijectivity

In this section, we investigate what happens when injectivity and surjectivity meet. Let us start with giving that idea a name.


::::::{prf:definition}
A linear transformation $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ is called **bijective** if it is both injective and surjective.

::::::

Although we allow $m$ and $n$ to be different in the definition, it turns out that this cannot happen as the following proposition shows.


::::::{prf:proposition}
If a linear transformation $T:\mathbb{R}^{m}\to\mathbb{R}^{n}$ is bijective, then $m=n$.

::::::


::::::{prf:proof}
Let $A$ be the standard matrix of $T$, which is an $n\times m$ matrix. By {prf:ref}`Prop:InjSurj:InjChars`, the number of pivots in $A$ is $m$. By {prf:ref}`Prop:InjSurj:SurjChars`, the number of pivots in $A$ is $n$. Hence the claim follows.

::::::

If the domain and codomain are both $\mathbb{R}^{n}$ then something striking happens: injectivity, surjectivity, and bijectivity all become equivalent!


::::::{prf:proposition}
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

::::::{prf:proof}
It suffices to show that $T$ is injective if and only if it is surjective. Assume $T$ is injective. Then the standard matrix $A$ of $T$ has a pivot in each column. But as the number of columns and the number of rows are the same, there must be a pivot in each row, showing surjectivity of $T$. 

Similarly, if $T$ is surjective, then the standard matrix $A$ of $T$ has a pivot in each column. Again, the number of columns is the same as the number of rows, so there is also a pivot in every row and we conclude that $T$ must be injective.

::::::
