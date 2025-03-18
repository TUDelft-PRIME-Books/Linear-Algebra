(Sec:OrthoBase)=

# Orthogonal and Orthonormal bases

## Orthogonal and Orthonormal bases

:::{prf:definition}

A subset $S$ of $\R^{n}$ is called **orthogonal** if any two distinct vectors $\vect{v}_{1}$ and $\vect{v}_{2}$ in $S$ are orthogonal to each other. If $S$ is a basis for a subspace $V$ and $S$ is orthogonal, we say it is an **orthogonal basis** for $V$.

:::

:::{prf:Example}
:label: Ex:OrthoBase:ExOfOrthoBase

Consider the plane

$$\mathcal{P}=\left\{\begin{bmatrix}x\\y\\z\end{bmatrix}\mid x+y+z=0\right\}\text{ and the vectors }\vect{v}_{1}=\begin{bmatrix}1\\-1\\0\end{bmatrix},\quad \vect{v}_{2}=\begin{bmatrix}1\\1\\-2\end{bmatrix}.$$

Both $\vect{v}_{1}$ and $\vect{v}_{2}$ lie in $\mathcal{P}$. The set $\mathcal{B}=\left\{\vect{v}_{1},\vect{v}_{2}\right\}$ is a linearly independent set of two vectors in $\mathcal{P}$. Since $\dim(\mathcal{P})=2$, it must therefore be a basis. Furthermore, $\vect{v}_{1}\ip\vect{v}_{2}=1-1-0=0$ so $\vect{v}_{1}$ is orthogonal to $\vect{v}_{2}$. Hence $\mathcal{B}$ is an orthogonal basis for $\mathcal{P}$.

:::

Since $\vect{0}$ is orthogonal to every vector, adding it to a set or removing it from a set does not change whether the set is orthogonal or not.

:::{prf:proposition}
:label: Prop:OrthoBase:OrthoSetLinInd

An orthogonal set $S$ which does not contain $\vect{0}$ is linearly independent.

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:OrthoBase:OrthoSetLinInd`
:class: tudproof

Assume $S$ is linearly dependent. Then there are vectors $\vect{v}_{1},...,\vect{v}_{n}$ in $S$ and scalars $c_{1},...,c_{n}$, not all zero, such that $\vect{0}=c_{1}\vect{v}_{1}+\cdots +c_{n}\vect{v}_{n}.$ But then, for any $i$:

$$0=\vect{0}\ip \vect{v}_{i}=(c_{1}\vect{v}_{1}+\cdots +c_{n}\vect{v}_{n})\ip\vect{v}_{i}=c_{i}(\vect{v}_{i}\ip\vect{v}_{i}).$$

Since no $\vect{v}_{i}$ is $\vect{0}$, all $\vect{v}_{i}\ip\vect{v}_{i}$ are non-zero, hence all $c_{i}$ must be zero, which contradicts our assumption.

:::

As a consequence of {prf:ref}`Prop:OrthoBase:OrthoSetLinInd`, any orthogonal set that does not contain $\vect{0}$ is an orthogonal basis for its span.

:::{prf:definition}

An orthogonal basis is called **orthonormal** if all elements in the basis have norm $1$.

:::

:::{prf:remark}

If $\vect{v}_{1},...,\vect{v}_{n}$ is an orthogonal basis for a subspace $V$, then an orthonormal basis for $V$ can be obtained by dividing each $\vect{v}_{i}$ by its norm.

:::

:::{prf:example}
:label: Ex:OrthoBase:OrthonormalBase

Consider the plane $\mathcal{P}$, the vectors $\vect{v}_{1},\vect{v}_{2}$ and the basis $\mathcal{B}$ from {prf:ref}`Ex:OrthoBase:ExOfOrthoBase`. This $\mathcal{B}$ is an orthogonal basis, but $\norm{\vect{v}_{1}}=\sqrt{2}$ and $\norm{\vect{v}_{2}}=\sqrt{6}$ so it is not orthonormal.

We can remedy this by considering the basis $\mathcal{B}_{2}=\left\{\vect{u}_{1},\vect{u}_{2}\right\}$ where

$$\vect{u}_{1}=\frac{\vect{v}_{1}}{\norm{\vect{v}_{1}}}=\frac{1}{\sqrt{2}}\begin{bmatrix}1\\-1\\0\end{bmatrix}\quad\text{and}\quad \vect{u}_{2}=\frac{\vect{v}_{2}}{\norm{\vect{v}_{2}}}=\frac{1}{\sqrt{6}}\begin{bmatrix}1\\1\\-2\end{bmatrix}.$$

This new basis $\mathcal{B}_{2}$ is an orthonormal basis. We have kept the directions of $\vect{v}_{1}$ and $\vect{v}_{2}$, but we have made sure that their norms are now $1$.

:::

The essence of {prf:ref}`Thm:OrthoBase:WeightsOrthoBase` is that it is easy to find the coordinates of any vector in a subspace $V$ with respect to a given orthogonal basis of $V$. In fact, this is largely why we are interested in such bases.

:::{prf:theorem}
:label: Thm:OrthoBase:WeightsOrthoBase

Let $V$ be a subspace of $\R^{n}$ and assume $\vect{v}_{1},...,\vect{v}_{k}$ is an orthogonal basis for $V$. Then any vector $\vect{v}$ in $V$ can be written as:

$$\vect{v}=\frac{\vect{v}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\cdots +\frac{\vect{v}\ip\vect{v}_{k}}{\vect{v}_{k}\ip\vect{v}_{k}}\vect{v}_{k}.$$

In particular, if $\vect{v}_{1},..,\vect{v}_{k}$ is an orthonormal basis, then any $\vect{v}$ in $V$ can be written as:

$$\vect{v}=(\vect{v}\ip\vect{v}_{1})\vect{v}_{1}+\cdots +(\vect{v}\ip\vect{v}_{k})\vect{v}_{k}.$$

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Thm:OrthoBase:WeightsOrthoBase`
:class: tudproof

Since $\vect{v}_{1},...,\vect{v}_{k}$ is a basis for $V$ and $\vect{v}$ is in $V$, there are scalars $c_{1},...,c_{k}$ such that $\vect{v}=c_{1}\vect{v}_{1}+\cdots +c_{k}\vect{v}_{k}$. We only have to show that these scalars are as claimed. For any $j$ between $1$ and $k$,

$$\vect{v}\ip\vect{v}_{j}=(c_{1}\vect{v}_{1}+\cdots +c_{k}\vect{v}_{k})\ip\vect{v}_{j}=c_{j}(\vect{v}_{j}\ip\vect{v}_{j})$$

by the orthogonality of $\left\{\vect{v}_{1},...,\vect{v}_{k}\right\}$. This implies $c_{j}=\frac{\vect{v}\ip\vect{v}_{j}}{\vect{v}_{j}\ip\vect{v}_{j}}$ as claimed.

If $\vect{v}_{1},...,\vect{v}_{k}$ is orthonormal, then $\vect{v}_{j}\ip\vect{v}_{j}=1$ for every $j$, so this reduces to $c_{j}=\vect{v}\ip\vect{v}_{j}$.

:::

In this theorem, it is vital that $\vect{v}$ is known to be in $V$. If $\vect{v}$ is not in $V$, then it can definitely not be expressed as a linear combination of basis elements of $V$. However, the right hand side appearing in {prf:ref}`Thm:OrthoBase:WeightsOrthoBase` is still very important. It comes back in {prf:ref}`Thm:OrthoBase:OrthoDecomp`.

## Orthogonal Projections Revisited

In {numref}`Subsec:GeomLinTrans:Proj`, we have already briefly touched upon orthogonal projections in higher dimension. Now that we know about orthogonal bases, we can make this more concrete. Let us start with a general definition of the orthogonal projection.

:::{prf:definition}
:label: Dfn:OrthoBase:OrthoProjection

Let $V$ be a subspace of $\R^{n}$, let $\vect{u}$ be a vector in $\R^{n}$, and let $\vect{u}=\vect{u}_{V}+\vect{u}_{V^{\bot}}$ be the orthogonal decomposition of $\vect{u}$ with respect to $V$ as defined in {prf:ref}`Prop:OrthoComp:PrthoDecomp`. We call $\vect{u}_{V}$ the **orthogonal projection** of $\vect{u}$ on $V$.

:::

We now establish the following useful facts about the orthogonal projection. Of particular interest is [iii.](#It:OrthoBase:ProjIsClosest), which states in essence that $\vect{u}_{V}$ is the best approximation of $\vect{u}$ with a vector from $V$ or, in other words, that the projection of $\vect{u}$ onto $V$ is the point in $V$ which is closest to $\vect{u}$.

:::{prf:Proposition}
:label: Prop:Orthogonality:BestApprox

Let $V$ be a subspace of $\R^{n}$ and let $\vect{u}$ be an arbitrary vector in $\R^{n}$ with orthogonal decomposition $\vect{u}=\vect{u}_{V}+\vect{u}_{V^{\bot}}$. Then:

<ol type="i">
<li>

$\norm{\vect{u}}\geq \norm{\vect{u}_{V}}$.

</li>
<li>

$\vect{u}\ip\vect{u}_{V}\geq 0$ and $\vect{u}\ip\vect{u}_{V}=0$ precisely when $\vect{u}$ is in $V^{\bot}$.

</li>
<li id="It:OrthoBase:ProjIsClosest">

For any $\vect{v}$ in $V$, $\norm{\vect{u}-\vect{u}_{V}}\leq \norm{\vect{u}-\vect{v}}$.

</li>

</ol>

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:Orthogonality:BestApprox`
:class: tudproof

Recall that the inner product of any vector with itself is non-negative and that $\vect{u}_{V}\ip\vect{u}_{V^{\bot}}=0$.

<ol type="i">
<li>

We find:

$$
\begin{align*}
\norm{\vect{u}}&=\sqrt{\vect{u}\ip\vect{u}}=\sqrt{(\vect{u}_{V}+\vect{u}_{V^{\bot}})\ip(\vect{u}_{V}+\vect{u}_{V^{\bot}})}\\
&=\sqrt{\vect{u}_{V}\ip\vect{u}_{V}+2\vect{u}_{V}\ip\vect{u}_{V^{\bot}}+\vect{u}_{V^{\bot}}\ip\vect{u}_{V^{\bot}}}=\sqrt{\vect{u}_{V}\ip\vect{u}_{V}+\vect{u}_{V^{\bot}}\ip\vect{u}_{V^{\bot}}}\\
&\geq\sqrt{\vect{u}_{V}\ip\vect{u}_{V}}=\norm{\vect{u}_{V}}
\end{align*}
$$

</li>
<li>

We have:

$$
\begin{align*}
\vect{u}\ip\vect{u}_{V}&=(\vect{u}_{V}+\vect{u}_{V^{\bot}})\ip\vect{u}_{V}\\
&=\vect{u}_{V}\ip\vect{u}_{V}\geq 0.
\end{align*}
$$

Furthermore, $\vect{u}_{V}\ip\vect{u}_{V}=0$ implies $\vect{u}_{V}=\vect{0}$, so $\vect{u}=\vect{u}_{V^{\bot}}$ which is in $V^{\bot}$.

</li>
<li>

For arbitrary $\vect{v}$ in $V$, $\vect{u}_{V}-\vect{v}$ is in $V$. As $\vect{u}_{V^{\bot}}$ is in $V^{\bot}$, this implies $(\vect{u}_{V}-\vect{v})\ip \vect{u}_{V^{\bot}}=0$. Therefore,

$$
\begin{align*}
\norm{\vect{u}-\vect{v}}&=\sqrt{(\vect{u}_{V}+\vect{u}_{V^{\bot}}-\vect{v})\ip(\vect{u}_{V}+\vect{u}_{V^{\bot}}-\vect{v})}\\
&=\sqrt{(\vect{u}_{V}-\vect{v})\ip(\vect{u}_{V}-\vect{v})+\vect{u}_{V^{\bot}}\ip\vect{u}_{V^{\bot}}}\\
&\geq\sqrt{\vect{u}_{V^{\bot}}\ip\vect{u}_{V^{\bot}}}=\norm{\vect{u}-\vect{u}_{V}}.
\end{align*}
$$

</li>

</ol>

:::

Naturally, we want to know how to find such an orthogonal projection. If we have an orthogonal basis for $V$, there turns out to be a convenient way to compute it, as per {prf:ref}`Thm:OrthoBase:OrthoDecomp`.

::::{prf:Theorem}
:label: Thm:OrthoBase:OrthoDecomp

Suppose $V$ is a subspace of $\R^{n}$ with orthogonal basis $\vect{v}_{1},...,\vect{v}_{k}$ and let $\vect{u}$ be a vector in $\R^{n}$. Then

:::{math}
:label: Eq:OrthoBase:OrthoProj

\vect{u}_{V}=\text{proj}\_V(\vect{u}) = \frac{\vect{u}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\cdots +\frac{\vect{u}\ip\vect{v}_{k}}{\vect{v}_{k}\ip\vect{v}_{k}}\vect{v}\_{k}.

:::

::::

:::{admonition} Proof of&nbsp;{prf:ref}`Thm:OrthoBase:OrthoDecomp`
:class: tudproof

Put

$$\vect{w}=\frac{\vect{u}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\cdots +\frac{\vect{u}\ip\vect{v}_{k}}{\vect{v}_{k}\ip\vect{v}_{k}}\vect{v}_{k}.$$

Since all the $\vect{v}_{i}$'s are in $V$, so is $\vect{w}$. It suffices to show that $\vect{u}-\vect{w}$ is in $V^{\bot}$, because then $\vect{u}=\vect{w}+(\vect{u}-\vect{w})$ must be the decomposition as in {prf:ref}`Prop:OrthoComp:PrthoDecomp`.

To prove this, we check that $\vect{u}-\vect{w}$ is orthogonal to all the $\vect{v}_{i}$'s, which form a basis of $V$. This follows readily:

$$
\begin{align*}
    (\vect{u}-\vect{w})\ip \vect{v}_{i}&=\left(\vect{u}-\frac{\vect{u}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\cdots +\frac{\vect{u}\ip\vect{v}_{k}}{\vect{v}_{k}\ip\vect{v}_{k}}\vect{v}_{k}\right)\ip\vect{v}_{i}\\
    &=\vect{u}\ip\vect{v}_{i}-\frac{\vect{u}\ip\vect{v}_{i}}{\vect{v}_{i}\ip\vect{v}_{i}}(\vect{v}_{i}\ip\vect{v}_{i})=0.
\end{align*}
$$

:::

It is worthwhile to compare this result to the formula for the projection of one vector on another given in {prf:ref}`Prop:InnerProduct:UniqueProjection`. What {prf:ref}`Thm:OrthoBase:OrthoDecomp` states is essentially this: if $V$ has an orthogonal basis $\vect{v}_{1},...,\vect{v}_{k}$, then the projection of any vector $\vect{u}$ onto $V$ is the sum of the projections of $\vect{u}$ on the $\vect{v}_{i}$'s. This is illustrated in {numref}`Figure %s <Fig:OrthoBase:DecompAs2Proj>`

```{applet}
:url: ortho/decompas2proj
:fig: Images/Fig-OrthoBase-DecompAs2Proj.svg
:name: Fig:OrthoBase:DecompAs2Proj
:position: -5.49,7.46,20.08
:class: dark-light

A vector and its orthogonal projection on the subspace $V$. Note that this projection is the sum of the projections of $\vect{u}$ on the orthogonal basis $\vect{v}_{1},\vect{v}_{2}$.
```

:::{prf:example}
:label: Ex:OrthoBase:ExofOrthoProj

Let us revisit the plane $\mathcal{P}$ with orthogonal basis $\mathcal{B}=\left\{\vect{v}_{1},\vect{v}_{2}\right\}$ from {prf:ref}`Ex:OrthoBase:ExOfOrthoBase`, i.e.

$$
\vect{v}_{1}=
\begin{bmatrix}
    1\\
    -1\\
    0
\end{bmatrix},\quad \vect{v}_{2}=
\begin{bmatrix}
    1\\
    1\\
    -2
\end{bmatrix}.\text{ Take another vector, say }\vect{u}=
\begin{bmatrix}
    -1\\
    1\\
    2
\end{bmatrix}.
$$

We find $\vect{u}\ip\vect{v}_{1}=-2,\vect{u}\ip\vect{v}_{2}=-4,$ and $\vect{v}_{1}\ip\vect{v}_{1}=2,\vect{v}_{2}\ip\vect{v}_{2}=6$. Consequently,

$$\vect{u}_{\mathcal{P}}=\frac{\vect{u}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\frac{\vect{u}\ip\vect{v}_{2}}{\vect{v}_{2}\ip\vect{v}_{2}}\vect{v}_{2}=-\frac{2}{2}\vect{v}_{1}-\frac{4}{6}\vect{v}_{2}=\begin{bmatrix}-\frac{5}{3}\\\frac{1}{3}\\\frac{4}{3}\end{bmatrix}$$

is the orthogonal projection of $\vect{u}$ on $\mathcal{P}$.

:::

:::{prf:remark}

If $V$ is a subspace of $\R^{n}$, then

$$T:\R^{n}\to\R^{n},\vect{u}\mapsto\vect{u}_{V}$$

is a linear transformation. It is called the **orthogonal projection** on $V$. The standard matrix of this transformation is the matrix for which the $i$-th column is:

$$
\frac{\vect{e}_{i}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\cdots +\frac{\vect{e}_{i}\ip\vect{v}_{k}}{\vect{v}_{k}\ip\vect{v}_{k}}\vect{v}_{k}.
$$

Here the $\vect{v}_{1},...,\vect{v}_{k}$ are an arbitrary orthogonal basis for $V$.

:::

:::{prf:example}
:label: Ex:OrthoBase:OrthoProjMat

Let us once more consider the {prf:ref}`Ex:OrthoBase:ExOfOrthoBase` and let us find the standard matrix corresponding to the linear transformation $T:\R^{3}\to\R^{3}, \vect{u}\mapsto\vect{u}_{V}.$ In {prf:ref}`Ex:OrthoBase:ExOfOrthoBase`, we already found that $\vect{v}_{1}\ip\vect{v}_{1}=2$ and $\vect{v}_{2}\ip\vect{v}_{2}=6$. Standard computations yield:

$$\vect{e}_{1}\ip\vect{v}_{1}=1\quad\text{and}\quad \vect{e}_{1}\ip\vect{v}_{2}=1,$$

so the first column of the standard matrix will be :

$$
\frac{1}{2}
\begin{bmatrix}
    1\\\
    -1\\
    0
\end{bmatrix}+\frac{1}{6}\begin{bmatrix}
    1\\
    1\\
    -2
\end{bmatrix}=
\begin{bmatrix}
    \frac{2}{3}\\
    -\frac{1}{3}\\
    -\frac{1}{3}
\end{bmatrix}.
$$

Similarly, we find

$$\vect{e}_{2}\ip\vect{v}_{1}=-1\quad\text{and}\quad \vect{e}_{2}\ip\vect{v}_{2}=1.$$

so the second column of the standard matrix will be :

$$
\frac{-1}{2}
\begin{bmatrix}
    1\\\
    -1\\
    0
\end{bmatrix}+\frac{1}{6}\begin{bmatrix}
    1\\
    1\\
    -2
\end{bmatrix}=
\begin{bmatrix}
    -\frac{1}{3}\\
    \frac{2}{3}\\
    -\frac{1}{3}
\end{bmatrix}.
$$

Finally,

$$\vect{e}_{3}\ip\vect{v}_{1}=0\quad\text{and}\quad \vect{e}_{3}\ip\vect{v}_{2}=-2$$

so the last column of the standard matrix will be:

$$
\frac{0}{2}
\begin{bmatrix}
    1\\\
    -1\\
    0
\end{bmatrix}+\frac{-2}{6}\begin{bmatrix}
    1\\
    1\\
    -2
\end{bmatrix}=\begin{bmatrix}
    -\frac{1}{3}\\
    -\frac{1}{3}\\
    \frac{2}{3}
\end{bmatrix}.
$$

Let us verify that, for the vector $\vect{u}$ from {prf:ref}`Ex:OrthoBase:ExofOrthoProj` we do indeed get the right answer:

$$
T(\vect{u})=\frac{1}{3}\begin{bmatrix}
    2&-1&-1\\
    -1&2&-1\\
    -1&-1&2
\end{bmatrix}
\begin{bmatrix}
    -1\\
    1\\
    2
\end{bmatrix}=
\frac{1}{3}\begin{bmatrix}
    -5\\
    1\\
    4
\end{bmatrix}.
$$

:::

## Orthogonal Matrices

Square matrices for which the columns are orthonormal turn out to be of particular importance. For instance, they turn up in numerical linear algebra, where using them can speed up certain computations considerably.

:::{prf:definition}

We call a square matrix **orthogonal** if its columns form an ortho*normal* set.

:::

:::{prf:remark}

A matrix for which the columns are orthogonal is not necessarily an orthogonal matrix! It is vital that the columns are ortho*normal*. The terminology is somewhat confusing, but it has become standard.

:::

Let us consider some examples and non-examples.

:::{prf:example}

<ol type="i">

<li>

The identity matrix $I_{n}$ is an orthogonal matrix for any $n$.

</li>

<li id="It:OrthoBase:ColsNotNormal">

The matrix

$$
A=\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix}
$$

is _not_ orthogonal. Its columns are pairwise orthogonal, but neither columns has norm 1. Indeed, the norm of both columns is $\sqrt{2}$.

</li>

<li id="It:OrthoBase:ColsNormal">

If we consider the matrix from [ii.](#It:OrthoBase:ColsNotNorm) but we divide both columns by their norms, we obtain:

$$
B=\begin{bmatrix}
\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\\
\frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{2}}
\end{bmatrix}.
$$

This matrix really is orthogonal.

</li>

</ol>

:::

What we did in going from [ii.](#It:OrthoBase:ColsNotNorm) to [iii.](#It:OrthoBase:ColsNorm) works in general: if we have a matrix $A$ with orthogonal columns, we can turn it into an orthogonal matrix $B$ by dividing every column by its norm. Under one condition, though: none of the columns of $A$ may be the zero vector, for then we would need to divide by $0$, which is impossible.

:::{prf:proposition}
:label: Prop:OrthoBase:OrthoMat

An $n\times n$-matrix $A$ is orthogonal if and only if $A^{T}A=I_{n}$.

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:OrthoBase:OrthoMat`
:class: tudproof

Let $\vect{v}_{1},\vect{v}_{2}...,\vect{v}_{n}$ be the columns of $A$, so $\vect{v}_{1}^{T},\vect{v}_{2}^{T},...,\vect{v}_{n}^{T}$ are the rows of $A^{T}$. Consequently,

$$
A^{T}A=\begin{bmatrix}
    \vect{v}_{1}^{T}\\
    \vect{v}_{2}^{T}\\
    \vdots\\
    \vect{v}_{n}^{T}
\end{bmatrix}\begin{bmatrix}
    \vect{v}_{1}&\vect{v}_{2}&\cdots&\vect{v}_{n}
\end{bmatrix}=\begin{bmatrix}
    \vect{v}_{1}^{T}\vect{v}_{1}&\vect{v}_{1}^{T}\vect{v}_{2}&\cdots&\vect{v}_{1}^{T}\vect{v}_{n}\\
    \vect{v}_{2}^{T}\vect{v}_{1}&\vect{v}_{2}^{T}\vect{v}_{2}&\cdots&\vect{v}_{2}^{T}\vect{v}_{n}\\
    \vdots&\vdots&\ddots&\vdots\\
    \vect{v}_{n}^{T}\vect{v}_{1}&\vect{v}_{n}^{T}\vect{v}_{2}&\cdots&\vect{v}_{n}^{T}\vect{v}_{n}
\end{bmatrix}.
$$

The matrix on the right hand side is $I_{n}$ if and only if all diagonal entries are $1$ and all off-diagonal entries are $0$. This happens precisely when

$$
\vect{v}_{i}\ip\vect{v}_{j}=\vect{v}_{i}^{T}\vect{v}_{j}=\begin{cases}
    1&\text{ if $i=j$}\\
    0&\text{ if $i\neq j$}
\end{cases}
$$

that is, when $\left\{\vect{v}_{1},\vect{v}_{2},...,\vect{v}_{k}\right\}$ is an orthonormal set.

:::

:::{prf:corollary}
:label: Cor:OrthoBase:TransisInv

A square matrix $A$ is orthogonal if and only if $A^{T}=A^{-1}$.

:::

The main reason orthogonal matrices are so useful is that they preserve lengths and angles. That this is so, is shown in {prf:ref}`Prop:OrthoBase:OrthoMatandInnerProd`.

:::{prf:proposition}
:label: Prop:OrthoBase:OrthoMatandInnerProd

Let $A$ be an orthogonal $n\times n$-matrix and let $\vect{v}_{1},\vect{v}_{2}$ be arbitrary vectors in $\R^{n}$. Then:

<ol type="i">

<li id="It:OrthoBase:OrthoMatandInnerProd">

$(A\vect{v}_{1})\ip(A\vect{v}_{2})=\vect{v}_{1}\ip\vect{v}_{2}$,

</li>

<li>

$\norm{A\vect{v}_{1}}=\norm{\vect{v}_{1}}$,

</li>

<li>

$\angle(A\vect{v}_{1},A\vect{v}_{2})=\angle(\vect{v}_{1},\vect{v}_{2})$.

</li>

</ol>

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:OrthoBase:OrthoMatandInnerProd`
:class: tudproof

Using $A^{T}A=I_{n}$, we find:

$$(A\vect{v}_{1})\ip(A\vect{v}_{2})=(A\vect{v}_{1})^{T}(A\vect{v}_{2})=\vect{v}_{1}^{T}A^{T}A\vect{v}_{2}=\vect{v}_{1}^{T}\vect{v}_{2}=\vect{v}_{1}\ip\vect{v}_{2},$$

which establishes [i.](#It:OrthoBase:OrthoMatandInnerProd) The other points are direct consequences of [i.](#It:OrthoBase:OrthoMatandInnerProd); we leave their proofs to the reader.

:::

:::{prf:Remark}

Many statements about orthogonal matrices still hold for non-square matrices, as long as the columns form an orthonormal set. Both {prf:ref}`Prop:OrthoBase:OrthoMat` and {prf:ref}`Prop:OrthoBase:OrthoMatandInnerProd` remain precisely the same, with the same proof, for an $m\times n$ matrix $A$. {prf:ref}`Cor:OrthoBase:TransisInv` doesn't hold for non-square matrices, as the inverse of a non-square matrix cannot exist.

:::

You could of course also consider matrices for which the _rows_ are orthonormal. It turns out, however, that this yields the exact same concept.

:::{prf:proposition}
:label: Prop:OrthoBase:Rows

An $n\times n$-matrix $A$ is orthogonal if and only if its rows are orthonormal.

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:OrthoBase:Rows`
:class: tudproof

We know that $A$ is orthogonal if and only if $A^{T}A=I_{n}$. But this implies $A^{T}=A^{-1}$ and therefore also $AA^{T}=I_{n}$. Since $(A^{T})^{T}A^{T}=AA^{T}=I_{n}$, $A^{T}$ must be orthogonal by {prf:ref}`Prop:OrthoBase:OrthoMat`. Hence the columns of $A^{T}$, which are the rows of $A$, must be orthonormal.

:::

## Grasple Exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b818021a-4d58-4bc2-a135-9300283e10b1?id=110499
:label: grasple_exercise_7_2_1
:dropdown:
:description: To check whether a set of vectors is orthonormal.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c3115c3e-433c-491a-9f68-3ca7cb689d7d?id=110501
:label: grasple_exercise_7_2_2
:dropdown:
:description: To check whether a set of vectors is orthogonal.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d75f6fb9-c532-420e-8f54-0eafa066a7c1?id=108960
:label: grasple_exercise_7_2_3
:dropdown:
:description: Extending a vector in $\R^3$  to an orthogonal basis for $\R^3$.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/207ce8e6-6bea-4f43-bff4-8b7c3f9d0c11?id=108979
:label: grasple_exercise_7_2_4
:dropdown:
:description: Extending a set of 2 orthogonal vectors in $\R^4$  to an orthogonal basis of $\R^4$. 

::::




::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/057814d7-ee5a-4c4b-940c-af1705a7ed6a?id=110503
:label: grasple_exercise_7_2_5
:dropdown:
:description: Find the projection of a vector onto a 2-dimensional subspace in $\R^3$.

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/54d95c2b-d7a9-4bce-a11e-a70b0bc09d0a?id=109005
:label: grasple_exercise_7_2_6
:dropdown:
:description:  Find the projection of a vector onto a 2-dimensional subspace in $\R^4$.

::::




::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4e18b85b-5462-4652-bfd3-262976403c49?id=110505
:label: grasple_exercise_7_2_7
:dropdown:
:description: Find the projection of a vector onto a 3-dimensional subspace in $\R^4$.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/694b757f-b2a0-449b-806f-624fe9e78a6c?id=109007
:label: grasple_exercise_7_2_8
:dropdown:
:description: Compute the projection onto the null space of a matrix.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/dab23aa3-6004-4ce6-a027-6c5e7c564102?id=109008
:label: grasple_exercise_7_2_9
:dropdown:
:description:  Find the matrix of the projection onto a plane in $\R^3$.

::::

The following exercises are more conceptual than computational.

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c443c628-427c-4ba6-a55b-d7fd0a562904?id=87842
:label: grasple_exercise_7_2_10
:dropdown:
:description: Orthogonal basis and scalar multiplication.

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/825980e7-e25f-497e-a077-e009cedd55c4?id=87843
:label: grasple_exercise_7_2_11
:dropdown:
:description: Projection formula in case of a non-orthogonal basis?

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c815026e-df41-461c-b0dc-0b06a387d0c9?id=91876
:label: grasple_exercise_7_2_12
:dropdown:
:description: Alternative definition of an orthogonal matrix?

::::    

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3b34a2bb-8a8a-4174-829a-85aa44e9d53d?id=109002
:label: grasple_exercise_7_2_13
:dropdown:
:description: Ponderings about orthogonal matrices.

::::





::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/19fc60e5-6d07-4a9e-983e-a096ae23aa9f?id=110500
:label: grasple_exercise_7_2_14
:dropdown:
:description: Can the projection of a vector depend on the chosen orthogonal basis?

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e5bf92ed-3aa8-4b56-b548-1b7776deefad?id=110504
:label: grasple_exercise_7_2_15
:dropdown:
:description: Which conclusion holds if  $\text{proj}_W(\vect{y}) = \vect{y}$?

::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bad4391e-1cd7-4f6e-a8a8-7e6b2603e14d?id=110510
:label: grasple_exercise_7_2_16
:dropdown:
:description: When can the projection formula be used to find coordinates?

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fc2476b2-e27f-468d-a923-f54d1132891d?id=110511
:label: grasple_exercise_7_2_17
:dropdown:
:description: Is a diagonal matrix always an orthogonal matrix ?

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e58fcd10-f537-4bdd-a39d-2173520acce9?id=110512
:label: grasple_exercise_7_2_18
:dropdown:
:description: Considerations concerning  $UU^T$ and $U^TU$.

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4d215852-069a-4b2e-ae63-c6c700d0e4ae?id=110516
:label: grasple_exercise_7_2_19
:dropdown:
:description: To find the standard matrix of the projection onto plane in $\R^3$.

::::