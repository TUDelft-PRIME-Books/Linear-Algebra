(Sec:OrthoBase)=


## Orthogonal and orthonormal bases

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

:::{prf:proof}
:class: dropdown

Assume $S$ is linearly dependent. Then there are vectors $\vect{v}_{1},...,\vect{v}_{n}$ in $S$ and scalars $c_{1},...,c_{n}$, not all zero, such that $\vect{0}=c_{1}\vect{v}_{1}+\cdots +c_{n}\vect{v}_{n}.$ But then, for any $i$:

$$0=\vect{0}\ip \vect{v}_{i}=(c_{1}\vect{v}_{1}+\cdots +c_{n}\vect{v}_{n})\ip\vect{v}_{i}=c_{i}(\vect{v}_{i}\ip\vect{v}_{i}).$$

Since no $\vect{v}_{i}$ is $\vect{0}$, all $\vect{v}_{i}\ip\vect{v}_{i}$ are non-zero, hence all $c_{i}$ must be zero, which contradicts our assumption.

:::

As a consequence of {prf:ref}`Prop:OrthoBase:OrthoSetLinInd`, any orthogonal set that does not contain $\vect{0}$ is an orthogonal basis for its span. 

:::{prf:definition}

An orthogonal basis is called *orthonormal* if all elements in the basis have norm $1$.

:::

:::{prf:remark}

If $\vect{v}_{1},...,\vect{v}_{n}$ is an orthogonal basis for a subspace $V$, then an orthonormal basis for $V$ can be obtained by dividing each $\vect{v}_{i}$ by its norm.

:::

:::{prf:example}
:label: Ex:OrthoBase:OrthonormalBase

Consider the plane $\mathcal{P}$, the vectors $\vect{v}_{1},\vect{v}_{2}$ and the basis $\mathcal{B}$ from {prf:ref}`Ex:OrthoBase:ExOfOrthoBase`. This $\mathcal{B}$ is an orthogonal basis, but $\norm{\vect{v}_{1}}=\sqrt{2}$ and $\norm{\vect{v}_{2}}=\sqrt{6}$ so it is not orthonormal. 

We can remedy this by considering the basis $\mathcal{B}_{2}=\left\{\vect{u}_{1},\vect{u}_{2}\right\}$ where 

$$\vect{u}_{1}=\frac{\vect{v}_{1}}{\norm{\vect{v}_{1}}}=\frac{1}{\sqrt{2}}\begin{bmatrix}1\\-1\\0\end{bmatrix}\quad\text{and}\quad \vect{u}_{2}=\frac{\vect{v}_{2}}{\norm{\vect{v}_{2}}}=\frac{1}{\sqrt{6}}\begin{bmatrix}1\\1\\-2\end{bmatrix}.$$

This new basis $\mathcal{B}_{2}$ is an orthonormal basis. We have kept the directions of $\vect{v}_{1}$ and $\vect{v}_{2}$, but we have made sure that their norms are now 1.

:::

The essence of {prf:ref}`Thm:OrthoBase:WeightsOrthoBase` is that it is easy to find the coordinates of any vector in a subspace $V$ with respect to a given orthogonal basis of $V$. In fact, this is largely why we are interested in such bases.

:::{prf:theorem}
:label: Thm:OrthoBase:WeightsOrthoBase

Let $V$ be a subspace of $\R^{n}$ and assume $\vect{v}_{1},...,\vect{v}_{k}$ is an orthogonal basis for $V$. Then any vector $\vect{v}$ in $V$ can be written as:

$$\vect{v}=\frac{\vect{v}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\cdots +\frac{\vect{v}\ip\vect{v}_{k}}{\vect{v}_{k}\ip\vect{v}_{k}}\vect{v}_{k}.$$

In particular, if $\vect{v}_{1},..,\vect{v}_{k}$ is an orthonormal basis, then any $\vect{v}$ in $V$ can be written as:

$$\vect{v}=(\vect{v}\ip\vect{v}_{1})\vect{v}_{1}+\cdots +(\vect{v}\ip\vect{v}_{k})\vect{v}_{k}.$$

:::

:::{prf:proof}
:class: dropdown

Since $\vect{v}_{1},...,\vect{v}_{k}$ is a basis for $V$ and $\vect{v}$ is in $V$, there are scalars $c_{1},...,c_{k}$ such that $\vect{v}=c_{1}\vect{v}_{1}+\cdots +c_{k}\vect{v}_{k}$. We only have to show that these scalars are as claimed. For any $j$ between $1$ and $k$,

$$\vect{v}\ip\vect{v}_{j}=(c_{1}\vect{v}_{1}+\cdots +c_{k}\vect{v}_{k})\ip\vect{v}_{j}=c_{j}(\vect{v}_{j}\ip\vect{v}_{j})$$

by the orthogonality of $\left\{\vect{v}_{1},...,\vect{v}_{k}\right\}$. This implies $c_{j}=\frac{\vect{v}\ip\vect{v}_{j}}{\vect{v}_{j}\ip\vect{v}_{j}}$ as claimed.

If $\vect{v}_{1},...,\vect{v}_{k}$ is orthonormal, then $\vect{v}_{j}\ip\vect{v}_{j}=1$ for every $j$, so this reduces to $c_{j}=\vect{v}\ip\vect{v}_{j}$.

:::
 
## Orthogonal projections revisited

In {numref}`Subsec:GeomLinTrans:Proj`, we have already briefly touched upon orthogonal projections in higher dimension. Now that we know about orthogonal bases, we can make this more concrete. Let us start with a general definition of the orthogonal projection.

:::{prf:definition}
:label: Dfn:OrthoBase:OrthoProjection

Let $V$ be a subspace of $\R^{n}$, let $\vect{u}$ be a vector in $\R^{n}$, and let $\vect{u}=\vect{u}_{V}+\vect{u}_{V^{\bot}}$ be the orthogonal decomposition of $\vect{u}$ with respect to $V$ as defined in {prf:ref}`Prop:OrthoComp:PrthoDecomp`. We call $\vect{u}_{V}$ the **orthogonal projection** of $\vect{u}$ on $V$.

:::

This orthogonal projection can be thought of as the best approximation of $\vect{w}$ using vectors from $V$. Naturally, we want to know how to find such an orthogonal projection. If we have an orthogonal basis for $V$, there turns out to be a convenient way to compute it, as per {prf:ref}`Thm:OrthoBase:OrthoDecomp`.

:::{prf:Theorem}
:label: Thm:OrthoBase:OrthoDecomp

Suppose $V$ is a subspace of $\R^{n}$ with orthogonal basis $\vect{v}_{1},...,\vect{v}_{k}$ and let $\vect{u}$ be a vector in $\R^{n}$. Then  

$$\vect{u}_{V}=\frac{\vect{u}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\cdots +\frac{\vect{u}\ip\vect{v}_{k}}{\vect{v}_{k}\ip\vect{v}_{k}}\vect{v}_{k}.$$

:::


:::{prf:proof}
:class: dropdown

Put 

$$\vect{w}=\frac{\vect{u}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\cdots +\frac{\vect{u}\ip\vect{v}_{k}}{\vect{v}_{k}\ip\vect{v}_{k}}\vect{v}_{k}.$$

Since all the $\vect{v}_{i}$'s are in $V$, so is $\vect{w}$. It suffices to show that $\vect{u}-\vect{w}$ is in $V^{\bot}$, because then $\vect{u}=\vect{w}+(\vect{u}-\vect{w})$ must be the decomposition as in {prf:ref}`Prop:OrthoComp:PrthoDecomp`.

To prove this, we check that $\vect{w}$ is orthogonal to all the $\vect{v}_{i}$'s, which form a basis of $V$. This follows readily: 

$$\begin{align*}
    \vect{w}\ip \vect{v}_{i}&=\left(\vect{u}-\frac{\vect{u}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\cdots +\frac{\vect{u}\ip\vect{v}_{k}}{\vect{v}_{k}\ip\vect{v}_{k}}\vect{v}_{k}\right)\ip\vect{v}_{i}\\
    &=\vect{u}\ip\vect{v}_{i}-\frac{\vect{u}\ip\vect{v}_{i}}{\vect{v}_{i}\ip\vect{v}_{i}}(\vect{v}_{i}\ip\vect{v}_{i})=0.
\end{align*}$$

:::

```{figure}  Images/Fig-OrthoBase-DecompAs2Proj.svg
:name: Fig:OrthoBase:DecompAs2Proj

A vector and its orthogonal projection on the subspace $V$.
```

:::{prf:example}

Let us revisit the plane $\mathcal{P}$ with basis $\mathcal{B}=\left\{\vect{v}_{1},\vect{v}_{2}\right\}$ from {prf:ref}`Ex:OrthoBase:ExOfOrthoBase`. Take a vector, say, $\vect{u}=\begin{bmatrix}-1\\1\\2\end{bmatrix}$. We find $\vect{u}\ip\vect{v}_{1}=-2,\vect{u}\ip\vect{v}_{2}=-4,$ and $\vect{v}_{1}\ip\vect{v}_{1}=2,\vect{v}_{2}\ip\vect{v}_{2}=6$. Consequently,

$$\vect{u}_{\mathcal{P}}=\frac{\vect{u}\ip\vect{v}_{1}}{\vect{v}_{1}\ip\vect{v}_{1}}\vect{v}_{1}+\frac{\vect{u}\ip\vect{v}_{2}}{\vect{v}_{2}\ip\vect{v}_{2}}\vect{v}_{2}=-\frac{2}{2}\vect{v}_{1}-\frac{4}{6}\vect{v}_{2}=\begin{bmatrix}-\frac{5}{3}\\-\frac{1}{3}\\\frac{4}{3}\end{bmatrix}$$

is the orthogonal projection of $\vect{u}$ on $\mathcal{P}$.

:::



{prf:ref}`Thm:OrthoBase:OrthoDecomp` is quite a powerful tool. For example, it allows us to establish the following useful facts. Of particular interest is [iii.](#It:OrthoBase:ProjIsClosest), which states in essence that $\proj_{V}(\vect{w})$ is the best approximation of $\vect{w}$ with a vector from $V$ or, in other words, that the projection of $\vect{w}$ onto $V$ is the point in $V$ which is closest to $\vect{w}$.

:::{prf:Proposition}
:label: Prop:Orthogonality:BestApprox

Let $V$ be a subspace of $\R^{n}$ and let $\vect{u}$ be an arbitrary vector in $\R^{n}$ with orthogonal decomposition $\vect{u}=\vect{u}_{V}+\vect{u}_{V^{\bot}}$. Then: 

<ol type="i">
<li>

$\norm{\vect{u}}\geq \norm{\proj_{V}(\vect{u})}$.

</li>
<li>

$\vect{u}\ip\vect{u}_{V}\geq 0$ and $\vect{u}\ip\vect{u}_{V}=0$ precisely when $\vect{u}$ is in $V^{\bot}$.

</li>
<li id="It:OrthoBase:ProjIsClosest">

For any $\vect{v}$ in $V$, $\norm{\vect{u}-\vect{u}_{V}}\leq \norm{\vect{u}-\vect{v}}$.

</li>

</ol>

:::

:::{prf:proof}
:class: dropdown

Recall that the inner product of any vector with itself is non-negative and that $\vect{u}_{V}\ip\vect{u}_{V^{\bot}}=0$.

<ol type="i">
<li>

We find:

$$\begin{align*}
\norm{\vect{u}}&=\sqrt{\vect{u}\ip\vect{u}}=\sqrt{(\vect{u}_{V}+\vect{u}_{V^{\bot}})\ip(\vect{u}_{V}+\vect{u}_{V^{\bot}})}\\
&=\sqrt{\vect{u}_{V}\ip\vect{u}_{V}+2\vect{u}_{V}\ip\vect{u}_{V^{\bot}}+\vect{u}_{V^{\bot}}\ip\vect{u}_{V^{\bot}}}=\sqrt{\vect{u}_{V}\ip\vect{u}_{V}+\vect{u}_{V^{\bot}}\ip\vect{u}_{V^{\bot}}}\\
&\geq\sqrt{\vect{u}_{V}\ip\vect{u}_{V}}=\norm{\vect{u}_{V}}
\end{align*}$$

</li>
<li>

We have:

$$\begin{align*}
\vect{u}\ip\vect{u}_{V}&=(\vect{u}_{V}+\vect{u}_{V^{\bot}})\ip\vect{u}_{V}\\
&=\vect{u}_{V}\ip\vect{u}_{V}\geq 0.
\end{align*}$$

Furthermore, $\vect{u}_{V}\ip\vect{u}_{V}=0$ implies $\vect{u}_{V}=\vect{0}$, so $\vect{u}=\vect{u}_{V^{\bot}}$ which is in $V^{\bot}$.

</li>
<li>

</li>

We find, for arbitrary $\vect{v}$ in $V$:

$$\begin{align*}
\norm{\vect{u}-\vect{v}}&=\sqrt{(\vect{u}_{V}+\vect{u}_{V^{\bot}}-\vect{v})\ip(\vect{u}_{V}+\vect{u}_{V^{\bot}}-\vect{v})}\\
&=\sqrt{(\vect{u}_{V}-\vect{v})\ip(\vect{u}_{V}-\vect{v})+\vect{u}_{V^{\bot}}\ip\vect{u}_{V^{\bot}}}
\end{align*}$$

since $\vect{u}_{V}-\vect{v}$ is in $V$ and therefore orthogonal to $\vect{u}_{V^{\bot}}$. Again using the fact that the inproduct of any vector with itself is non-negative, we conclude that this is minimal when $\vect{u}_{V}-\vect{v}=\vect{0}$, i.e. when $\vect{u}_{V}=\vect{v}$.

</ol>

:::
