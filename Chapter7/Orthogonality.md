(Sec:Orthogonality)=

# Orthogonality

## Orthogonal complements

:::{prf:definition}

Suppose $V$ is a subspace of $\R^{n}$. Then the _orthogonal complement_ of $V$ is the set

$$

V^{\bot}=\left\{\vect{u}\in\R^{n}\mid \vect{u}\ip\vect{v}=0\text{ for all } \vect{v}\text{ in }V\right\}.


$$

in other words, it is the set of all vectors that are orthogonal to all of $V$.

:::

Note that, for a vector to be in $V^{\bot}$, it suffices that it is orthogonal to all elements in a basis of $V$ or, slightly more general, to all elements in a spanning set of $V$. Let us consider s simple example.

:::{prf:Example}
:label: Ex:Ortho:OrthoCompOfVect

Let $V$ be the subspace spanned by a single vector $\vect{v}$, say, by

$$\vect{v}=\begin{bmatrix}1\\2\\-1\end{bmatrix}\text{ and let }\vect{u}=\begin{bmatrix}a_{1}\\a_{2}\\a_{3}\end{bmatrix}\text{ be any vector in $\R^{3}$}.$$

Then $\vect{u}$ is in $V^{\bot}$ is and only if $\vect{u}\ip\vect{v}=a_{1}+2a_{2}-a_{3}=0$. So we find that $V^{\bot}$ is the plane described by the equation $a_{1}+2a_{2}-a_{3}=0$. The vector $\vect{v}$ is a normal vector to this plane.

:::

```{figure} Images/Fig-Ortho-OrthoComp.svg
:name: Fig:Ortho:OrthoComp

The orthogonal complement of a 1-dimensional subspace of $\R^{2}$ (left) and a of a 2-dimensional subspace of $\R^{3}$ (right).
```

The plane we found for $V^{\bot}$ in {prf:ref}`Ex:Ortho:OrthoCompOfVect` is a plane through the origin. It is therefore also a subspace. This is not a coincidence, as {prf:ref}`Prop:Ortho:OrthoComplisSpace` shows.

:::{prf:proposition}
:label: Prop:Ortho:OrthoComplisSpace

For any subspace $V$ of $\R^{n}$, the orthogonal complement $V^{\bot}$ is a subspace, too. Moreover, the only vector that is both in $V$ and in $V^{\bot}$ is $\vect{0}$.

:::

:::{prf:proof}

Since the zero vector is orthogonal to any vector, it is in $V^{\bot}$. Suppose now that $\vect{u}_{1}$ and $\vect{u}_{2}$ are in $V^{\bot}$. Then, for arbitrary $\vect{v}$ in $V$, $(\vect{u}_{1}+\vect{u}_{2})\ip \vect{v}=\vect{u}_{1}\ip\vect{v}+\vect{u}_{2}\ip\vect{v}=0$, so $\vect{u}_{1}+\vect{u}_{2}$ is in $V^{\bot}$.

Assume now that $\vect{u}$ is in $V^{\bot}$ and that $c$ is any scalar. Then, again for every $\vect{v}$ in $V$, $(c\vect{u})\ip\vect{v}=c(\vect{u}\ip\vect{v})=0$ so $c\vect{u}$ is in $V^{\bot}$.

If $\vect{v}$ is both in $V$ and $V^{\bot}$, then $\vect{v}\ip\vect{v}=0$ so $\vect{v}=\vect{0}$.

:::

```{margin} TODO

Add reference to Section Sec:SubspacesRn

```

As we have seen in Section, both the column space and null space of any $n\times m$ matrix are subspaces of $\R^{n}$ and $\R^{m}$, respectively. It turns out that the transposition ${}^{T}$ and the orthogonal complement ${}^{\bot}$ relate these two spaces to each other.

:::{prf:proposition}
:label: Prop:Orthogonality:OrthoComplementNulA

For any $n\times m$ matrix $M$ we have $\mathrm{Col}(A^{T})^{\bot}=\mathrm{Nul}(A)$ and $\mathrm{Col}(A)^{\bot}=\mathrm{Nul}(A^{T})$.

:::

:::{prf:proof}

Note that the second claim is easily derived from the first by substituting $A^{T}$ for $A$. Let $\vect{r}_{1},...,\vect{r}_{n}$ be the rows of $A$. Then $\vect{r}_{1}^{T},...,\vect{r}_{n}^{T}$ are the columns of $A^{T}$. For any vector $\vect{x}$ in $\R^{m}$, we have

$$A\vect{x}=\begin{bmatrix}\vect{r}_{1}\vect{x}\\\vdots\\\vect{r}_{n}\vect{x}\end{bmatrix}=\begin{bmatrix}\vect{r}_{1}^{T}\ip\vect{x}\\\vdots\\\vect{r}_{n}^{T}\ip\vect{x}\end{bmatrix}.$$

Now, $\vect{x}$ is in $\mathrm{Nul}(A)$ precisely when $A\vect{x}=\vect{0}$ or, in other words, when $\vect{r}_{i}^{T}\ip\vect{x}=0$ for any $i$. Since the set $\left\{\vect{r}_{1}^{T},..,\vect{r}_{n}^{T}\right\}$ spans $\mathrm{Col}(A^{T})$, this is equivalent to $\vect{x}$ being in $\mathrm{Col}(A^{T})^{\bot}$.

:::

## Orthogonal and orthonormal bases

:::{prf:definition}

A subset $S$ of $\R^{n}$ is called _orthogonal_ if any two distinct vectors $\vect{v}_{1}$ and $\vect{v}_{2}$ in $S$ are orthogonal to each other. If $S$ is a basis for a subspace $V$ and $S$ is orthogonal, we say it is an _orthogonal basis_ for $V$.

:::

:::{prf:Example}
:label: Ex:Ortho:ExOfOrthoBase

Consider the plane

$$\mathcal{P}=\left\{\begin{bmatrix}x\\y\\z\end{bmatrix}\mid x+y+z=0\right\}\text{ and the vectors }\vect{v}_{1}=\begin{bmatrix}1\\-1\\0\end{bmatrix},\quad \vect{v}_{2}=\begin{bmatrix}1\\1\\-2\end{bmatrix}.$$

Both $\vect{v}_{1}$ and $\vect{v}_{2}$ lie in $\mathcal{P}$. The set $\mathcal{B}=\left\{\vect{v}_{1},\vect{v}_{2}\right\}$ is a linearly independent set of two vectors in $\mathcal{P}$. Since $\dim(\mathcal{P})=2$, it must therefore be a basis. Furthermore, $\vect{v}_{1}\ip\vect{v}_{2}=1-1-0=0$ so $\vect{v}_{1}$ is orthogonal to $\vect{v}_{2}$. Hence $\mathcal{B}$ is an orthogonal basis for $\mathcal{P}$.

:::

Since $\vect{0}$ is orthogonal to every vector, adding it to a set or removing it from a set does not change whether the set is orthogonal or not.

:::{prf:proposition}
:label: Prop:Ortho:OrthoSetLinInd

An orthogonal set $S$ which does not contain $\vect{0}$ is linearly independent.

:::

:::{prf:proof}

Assume $S$ is linearly dependent. Then there are vectors $\vect{v}_{1},...,\vect{v}_{n}$ in $S$ and scalars $c_{1},...,c_{n}$, not all zero, such that $\vect{0}=c_{1}\vect{v}_{1}+\cdots +c_{n}\vect{v}_{n}.$ But then, for any $i$:

$$0=\vect{0}\ip \vect{v}_{i}=(c_{1}\vect{v}_{1}+\cdots +c_{n}\vect{v}_{n})\ip\vect{v}_{i}=c_{i}(\vect{v}_{i}\ip\vect{v}_{i}).$$

Since no $\vect{v}_{i}$ is $\vect{0}$, all $\vect{v}_{i}\ip\vect{v}_{i}$ are non-zero, hence all $c_{i}$ must be zero, which contradicts our assumption.

:::

As a consequence of {prf:ref}`Prop:Ortho:OrthoSetLinInd`, any orthogonal set that does not contain $\vect{0}$ is an orthogonal basis for its span.

:::{prf:definition}

An orthogonal basis is called _orthonormal_ if all elements in the basis have norm $1$.

:::

:::{prf:remark}

If $\vect{v}_{1},...,\vect{v}_{n}$ is an orthogonal basis for a subspace $V$, then an orthonormal basis for $V$ can be obtained by dividing each $\vect{v}_{i}$ by its norm.

:::

:::{prf:example}
:label: Ex:Ortho:OrthonormalBase

Consider the plane $\mathcal{P}$, the vectors $\vect{v}_{1},\vect{v}_{2}$ and the basis $\mathcal{B}$ from {prf:ref}`Ex:Ortho:ExOfOrthoBase`. This $\mathcal{B}$ is an orthogonal basis, but $\norm{\vect{v}_{1}}=\sqrt{2}$ and $\norm{\vect{v}_{2}}=\sqrt{6}$ so it is not orthonormal.

We can remedy this by considering the basis $\mathcal{B}_{2}=\left\{\vect{u}_{1},\vect{u}_{2}\right\}$ where

$$\vect{u}_{1}=\frac{\vect{v}_{1}}{\norm{\vect{v}_{1}}}=\frac{1}{\sqrt{2}}\begin{bmatrix}1\\-1\\0\end{bmatrix}\quad\text{and}\quad \vect{u}_{2}=\frac{\vect{v}_{2}}{\norm{\vect{v}_{2}}}=\frac{1}{\sqrt{6}}\begin{bmatrix}1\\1\\-2\end{bmatrix}.$$

This new basis $\mathcal{B}_{2}$ is an orthonormal basis. We have kept the directions of $\vect{v}_{1}$ and $\vect{v}_{2}$, but we have made sure that our step length is now 1.

:::

The essence of {prf:ref}`Thm:Ortho:WeightsOrthoBase` is that it is easy to find the coordinates of any vector in a subspace $V$ with respect to a given orthogonal basis of $V$. In fact, this is largely why we are interested in such bases.

:::{prf:theorem}
:label: Thm:Ortho:WeightsOrthoBase

Let $V$ be a subspace of $\R^{n}$ and assume $\vect{v}_{1},...,\vect{v}_{k}$ is an orthogonal basis for $V$. Then any vector $\vect{v}$ in $V$ can be written as:

$$\vect{v}=\frac{\vect{v}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\cdots +\frac{\vect{v}\ip\vect{v}_{k}}{\vect{v}_{k}\ip\vect{v}_{k}}\vect{v}_{k}.$$

In particular, if $\vect{v}_{1},..,\vect{v}_{k}$ is an orthonormal basis, then any $\vect{v}$ in $V$ can be written as:

$$\vect{v}=(\vect{v}\ip\vect{v}_{1})\vect{v}_{1}+\cdots +(\vect{v}\ip\vect{v}_{k})\vect{v}_{k}.$$

:::

:::{prf:proof}

Since $\vect{v}_{1},...,\vect{v}_{k}$ is a basis for $V$ and $\vect{v}$ is in $V$, there are scalars $c_{1},...,c_{k}$ such that $\vect{v}=c_{1}\vect{v}_{1}+\cdots +c_{k}\vect{v}_{k}$. We only have to show that these scalars are as claimed. For any $j$ between $1$ and $k$,

$$\vect{v}\ip\vect{v}_{j}=(c_{1}\vect{v}_{1}+\cdots +c_{k}\vect{v}_{k})\ip\vect{v}_{j}=c_{j}(\vect{v}_{j}\ip\vect{v}_{j}$$

by the orthogonality of $\left\{\vect{v}_{1},...,\vect{v}_{k}\right\}$. This implies $c_{j}=\frac{\vect{v}\ip\vect{v}_{j}}{\vect{v}_{j}\ip\vect{v}_{j}}$ as claimed.

If $\vect{v}_{1},...,\vect{v}_{k}$ is orthonormal, then $\vect{v}_{j}\ip\vect{v}_{j}=1$ for every $j$, so this reduces to $c_{j}=\vect{v}\ip\vect{v}_{j}$.

:::

## Orthogonal projections revisited

```{margin} TODO

Add reference to Section Sec:GeomLinTrans

```

In Section we have already briefly toched upon orthogonal projections in higher dimension. Now that we know about orthogonal bases, we can make this more concrete.

:::{prf:definition}
:label: Dfn:Orthogonality:OrthoProjection

Let $V$ be a subspace of $\R{n}$ and let $\vect{v}_{1},...,\vect{v}_{k}$ be an orthogonal basis for $V$. For any $\vect{w}$ in $\R^{n}$, we define the _orthogonal projection_ of $\vect{w}$ on $V$ as

$$\proj_{V}(w)=\frac{\vect{w}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\cdots +\frac{\vect{w}\ip\vect{v}_{k}}{\vect{v}_{k}\ip\vect{v}_{k}}\vect{v}_{k}.$$

:::

```{figure} Images/Fig-Ortho-DecompAs2Proj.svg
:name: Fig:Ortho:DecompAs2Proj

A vector and its orthogonal projection on the subspace $V$.
```

:::{prf:example}

Let us revisit the plane $\mathcal{P}$ with basis $\mathcal{B}=\left\{\vect{v}_{1},\vect{v}_{2}\right\}$ from {prf:ref}`Ex:Ortho:ExOfOrthoBase`. Take a vector, say, $\vect{w}=\begin{bmatrix}-1\\1\\2\end{bmatrix}$. We find $\vect{w}\ip\vect{v}_{1}=-2,\vect{w}\ip\vect{v}_{2}=-4,$ and $\vect{v}_{1}\ip\vect{v}_{1}=2,\vect{v}_{2}\ip\vect{v}_{2}=6$. Consequently,

$$
\proj_{\mathcal{P}}(\vect{w})=\frac{\vect{w}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\frac{\vect{w}\ip\vect{v}_{2}}{\vect{v}_{2}\ip\vect{v}_{2}}\vect{v}_{2}=-\frac{2}{2}\vect{v}_{1}-\frac{4}{6}\vect{v}_{2}=
\begin{bmatrix}
    -\frac{5}{3} \\
    {-\frac{1}{3}} \\
    {\frac{4}{3}}
\end{bmatrix}
$$

is the orthogonal projection of $\vect{w}$ on $\mathcal{P}$.

:::

This orthogonal projection can be thought of as the best approximation of $\vect{w}$ using vectors from $V$. Perhaps surprisingly, it is independent of the choice of the orthogonal basis $\vect{v}_{1},...,\vect{v}_{k}$ by {prf:ref}`Thm:Ortho:OrthoDecomp`. This justifies the fact that the chosen orthogonal base is left out of the notation.

:::{prf:Theorem}
:label: Thm:Ortho:OrthoDecomp

Suppose $V$ is a subpsace of $\R^{n}$ and $\vect{w}$ is a vector in $\R^{n}$. Then there is a unique decomposition

$$\vect{w}=\hat{\vect{w}}+\vect{x}\quad\text{where $\hat{\vect{w}}$ is in $V$ and $\vect{x}$ is in $V^{\bot}$.}$$

In fact, $\hat{\vect{w}}=\proj_{V}(\vect{w})$. This is called the _orthogonal decomposition_ of $\vect{w}$ with respect to $V$.

:::

:::{prf:proof}

Fix an orthogonal basis $\vect{v}_{1},..,\vect{v}_{k}$ for $V$ and put $\vect{x}=\vect{w}-\proj_{V}(\vect{w})$. Clearly, $\proj_{V}(\vect{w})$ is in $V$. If we can show $\vect{x}\bot \vect{v}_{i}$ for any $i$, it will follow that $\vect{x}$ is in $V^{\bot}$. This follows readily:

\begin{align*}
\vect{x}\ip \vect{v}*{i}&=\left(\vect{w}-\frac{\vect{w}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\cdots +\frac{\vect{w}\ip\vect{v}_{k}}{\vect{v}_{k}\ip\vect{v}_{k}}\vect{v}_{k}\right)\ip\vect{v}_{i}\\
&=\vect{w}\ip\vect{v}_{i}-\frac{\vect{w}\ip\vect{v}_{i}}{\vect{v}_{i}\ip\vect{v}_{i}}(\vect{v}_{i}\ip\vect{v}_{i})=0.
\end{align_}

The only thing left to show is that this decomposition is unique. Suppose $\vect{w}=\hat{\vect{w}}_{1}+\vect{x}_{1}$ and $\vect{w}=\hat{\vect{w}}_{2}+\vect{x}_{2}$ where $\hat{\vect{w}}_{1},\hat{\vect{w}}_{2}$ are in $V$ and $\vect{x}_{1},\vect{x}_{2}$ are in $V^{\bot}$. Then

$$\hat{\vect{w}}_{1}-\hat{\vect{w}}_{2}=\vect{x}_{2}-\vect{x}_{1}.$$

Since $V$ is a subspace, the left hand side is in $V$ and since $V^{\bot}$ is a subspace the right hand side is in $V^{\bot}$. But the only element in both $V$ and $V^{\bot}$ is $\vect{0}$. So $\vect{x}_{1}=\vect{x}_{2}$ and $\hat{\vect{w}}_{1}=\hat{\vect{w}}_{2}$.

:::

```{figure} Images/Fig-Ortho-OrthoDecomp.svg
:name: Fig:Ortho:OrthoDecomp

A vector, its orthogonal projection on a subspace, and the difference of the two. Note that the difference between the vector and its projection on $V$ if orthogonal to $V$, i.e. it is in $V^{\bot}$.
```

{prf:ref}`Thm:Ortho:OrthoDecomp` is quite a powerful tool. For example, it allows us to establish the following useful facts. Of particular interest is [iii.](#It:Ortho:ProjIsClosest), which states in essence that $\proj_{V}(\vect{w})$ is the best approximation of $\vect{w}$ with a vector from $V$ or, in other words, that the projection of $\vect{w}$ onto $V$ is the point in $V$ which is closest to $\vect{w}$.

:::{prf:Proposition}
:label: Prop:Orthogonality:BestApprox

Let $V$ be a subspace of $\R^{n}$ and let $\vect{w}$ be an arbitrary vector in $\R^{n}$. Then:

<ol type="i">
<li>

$\norm{\vect{w}}\geq \norm{\proj_{V}(\vect{w})}$.

</li>
<li>

$\vect{w}\ip\proj_{V}(\vect{w})\geq 0$ and $\vect{w}\ip\proj_{V}(\vect{w})=0$ precisely when $\vect{w}$ is in $V^{\bot}$.

</li>
<li id="It:Ortho:ProjIsClosest">

For any $\vect{v}$ in $V$, $\norm{\vect{w}-\vect{v}}\leq\norm{\vect{w}-\proj_{V}(\vect{w})}$.

</li>

</ol>

:::

:::{prf:proof}

Let $\vect{w}=\proj_{V}(\vect{w})+\vect{x}$ where $\vect{x}$ is in $V^{\bot}$.

<ol type="i">
<li>

Since the inproduct of any vector with itself is non-negative, we find:

$$
\begin{align*}
\norm{\vect{w}}&=\sqrt{\vect{w}\ip\vect{w}}=\sqrt{(\proj_{V}(\vect{w})+\vect{x})\ip(\proj_{V}(\vect{w})+\vect{x})}\\
&=\sqrt{\proj_{V}(\vect{w})\ip\proj_{V}(\vect{w})+\vect{x}\ip\vect{x}}\\
&\geq\sqrt{\proj_{V}(\vect{w})\ip\proj_{V}(\vect{w})}=\norm{\proj_{V}(\vect{w})}
\end{align*}
$$

</li>
<li>

We have:

$$
\begin{align*}
\vect{w}\ip\proj_{V}(\vect{w})&=(\proj_{V}(\vect{w})+\vect{x})\ip\proj_{V}(\vect{w})\\
&=\proj_{V}(\vect{w})\ip\proj_{V}(\vect{w})\geq 0.
\end{align*}
$$

Furthermore, $\proj_{V}(\vect{w})\ip\proj_{V}(\vect{w})=0$ implies $\proj_{V}(\vect{w})=\vect{0}$, so $\vect{w}=\vect{x}$ which is in $V^{\bot}$.

</li>
<li>

</li>

We find, for arbitrary $\vect{v}$ in $V$:

$$
\begin{align*}
\norm{\vect{w}-\vect{v}}&=\sqrt{(\proj_{V}(\vect{w})+\vect{x}-\vect{v})\ip(\proj_{V}(\vect{w})+\vect{x}-\vect{v})}\\
&=\sqrt{(\proj_{V}(\vect{w})-\vect{v})\ip(\proj_{V}(\vect{w})-\vect{v})+\vect{x}\ip\vect{x}}
\end{align*}
$$

Again using the fact that the inproduct of any vector with itself is non-negative, we conclude that this is minimal when $\proj_{V}(\vect{w})-\vect{v}=\vect{0}$, i.e. when $\proj_{V}(\vect{w})=\vect{v}$.

</ol>

:::
