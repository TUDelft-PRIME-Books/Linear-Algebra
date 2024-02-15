(Sec:ProofSVD)=

# Proof of the existence of SVD

This appendix is devoted to construct the proof of {prf:ref}`Thm:SVD:ExistenceSVD`. Some new definitions will be given.

::::{prf:definition} Norm of a Linear Transformation

Let $T:\mathbb{R}^n\to \mathbb{R}^m$ be a linear transformation with standard matrix $A$. We define the **matrix norm** of $A$ as

$$
\norm{A} = \max_{{\mathbf{v}\in \mathbb{R}^n},\norm{\mathbf{v}}=1} \norm{A\mathbf{v}}.
$$

We define the the **norm of a linear transformation** $T$
as the norm of its standard matrix. That is

$$\norm{T} = \norm{A}$$

::::

Observe that the matrix norm is defined by finding a maximum. We will leave to the reader (and for a calculus course) to prove that the function

\begin{align*}
f:\mathbb{R}^n &&\to&&& \mathbb{R}\\
\mathbf{v} &&\mapsto&&& f(\mathbf{v}) = \norm{\mathbf{v}}
\end{align*}

is a continuous function.

:::{prf:remark}

The matrix norm is sometimes called **induced norm**.
:::

:::{prf:definition}

Suppose that $T:V\subset\mathbb{R}^n \to \mathbb{R}^m$ is a linear transformation with standard matrix $A$. Then we define $\norm{T}$ restricted in $V$ as

$$
     \norm{T_{|V}} = \max_{\mathbf{v}\in V,\norm{\mathbf{v}}=1} \norm{A\mathbf{v}}
$$

:::

We will proof {prf:ref}`Thm:SVD:ExistenceSVD` by using a similar algorithm to {prf:ref}`Alg:SVD:SVDalgorithm`. The proof follows the geometric interpretation described in {numref}`Subsec:SVDGeometrically`. If the reader is not familiar with it, we recommend understanding the idea before continuing.

## Construction of $V$ and $U$

Suppose that $A$ is the standard matrix of a linear transformation $T:\mathbb{R}^n \to \mathbb{R}^m$ with rank $p$.

Since the construction will be iterative we will define, for convenience, $V^{(1)} = \mathbb{R}^n$.

Let's consider "the unit sphere" in $V^{(1)}$. That is

$$
S^{(1)} = \lbrace \mathbf{v} \in V^{(1)} \,|\, \norm{\mathbf{v}}=1\rbrace
$$

Now choose $\mathbf{v}_1\in V^{(1)}$ such that $\norm{T} = \norm{A\mathbf{v}_1} = s_1$

If $s_1=0$ then we are done as $A\mathbf{v}=\mathbf{0}$ for all $\mathbf{v}\in V^{(1)}$.

Let's suppose that $s_1>0$ and define $\mathbf{u}_1 = \frac{1}{s_1}A\mathbf{v}_1$. Notice that $\mathbf{u}_1\in \mathbb{R}^m$.

Next, consider the unit sphere in the subspace $V^{(2)}=\Span{\mathbf{v}_1}^\perp$:

$$
S_2 = \lbrace \mathbf{v}\in V^{(2)}\subset\mathbb{R}^n\,|\, \norm{\mathbf{v}}=1\rbrace,
$$

and the restriction of $T$ onto the subspace $V^{(2)}$. Then choose $\mathbf{v}_2$ such that $s_2 = \norm{T_{|V^{(2)}}} = \norm{A\mathbf{v}_2}$.

Notice that, by construction, $\mathbf{v}_1 \perp \mathbf{v}_2$. If $s_2=0$ then we are done, as $A\mathbf{v} = \mathbf{0}$ for all $\mathbf{v}\in V^{(2)}$. Suppose that $s_2 >0$, and define $\mathbf{u}_2 = \frac{1}{s_2}A\mathbf{v}_2$.

Observe that since $S^{(2)} \subset S^{(1)}$ we have that $\displaystyle\max_{\mathbf{v}\in S^{(2)},\norm{\mathbf{v}}=1} \norm{A\mathbf{v}} \le \max_{\mathbf{v}\in S^{(1)},\norm{\mathbf{v}}=1}\norm{A\mathbf{v}}$. Therefore, $s_2 \le s_1$.

In addition, we can prove that $\mathbf{u}_1\perp \mathbf{u}_2$.

:::{exercise}

Prove that $\mathbf{u}_1\perp \mathbf{u}_2$. Notice that we cannot use the same argument as in {numref}`Subsec:SVD:Algorithm` since we can not use {prf:ref}`Propo:SVD:singularvalues` (it assumes that the singular value decomposition exists, and this is what we are trying to prove).

:::

Suppose that we repeat this process $r$ times. That is, we found $\mathbf{v}_1, \dots, \mathbf{v}_r$, and $\mathbf{u}_1,\dots,\mathbf{u}_r$, and the values $s_1>s_2>\cdots>s_r>0$. Now we define $V^{(r+1)} = \Span{\mathbf{v}_1,\dots,\mathbf{v}_r}^{\perp}$ and we consider again the unit sphere in this subspace:

$$
S^{(r+1)} = \lbrace \mathbf{v}\in V^{(r+1)}\,|\, \norm{\mathbf{v}}=1\rbrace.
$$

Choose $s_{r+1} = \norm{T_{|V^{(r+1)}}}$. If $s_{r+1}=0$ we are done as $A\mathbf{v}=\mathbf{0}$ for all $\mathbf{v}\in V^{(r+1)}$. Else, we continue the process until either $s_{r}=0$ for some $r$, or until we find a basis for $\mathbb{R}^n$, i.e., $r=n$.

Now we take the vectors $\lbrace\mathbf{v}_1,\dots,\mathbf{v}_r\rbrace$. If $r < n$, we complete the set until we have an orthonormal basis $\mathcal{V}$ of $\mathbb{R}^n$. Then we do the same with the vectors $\lbrace\mathbf{u}_1,\dots,\mathbf{u}_r\rbrace$ by completing the set, if needed, to an orthonormal basis $\mathcal{U}$ of $\mathbb{R}^m$.

The values $s_1 > s_2 > \cdots > s_r > 0$ are the singular values (and 0 if we had to complete the set of vectors).

What remains to prove is that we have exactly $p$ non-zero singular values.

To see that, we consider the set $\lbrace \mathbf{u}_1, \dots, \mathbf{u}_r \rbrace$.
