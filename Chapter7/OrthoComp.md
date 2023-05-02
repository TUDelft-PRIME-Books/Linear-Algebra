(Sec:OrthoComp)=
# Orthogonal complements



:::{prf:definition}

Suppose $V$ is a subspace of $\R^{n}$. Then the *orthogonal complement* of $V$ is the set 

$$

V^{\bot}=\left\{\vect{u}\in\R^{n}\mid \vect{u}\ip\vect{v}=0\text{ for all } \vect{v}\text{ in }V\right\}.

$$

in other words, it is the set of all vectors that are orthogonal to all of $V$.

:::

Note that, for a vector to be in $V^{\bot}$, it suffices that it is orthogonal to all elements in a basis of $V$ or, slightly more general, to all elements in a spanning set of $V$. Let us consider some simple examples.

:::{prf:Example}
:label: Ex:Ortho:OrthoCompOfVect

<ol type="i">
<li>

Let $V$ be the subspace spanned by a single vector $\vect{v}$ in $\R^{2}$ and let $\vect{u}$ be any vector in $\R^{2}$, say:

$$
\vect{v}=
\begin{bmatrix}
1\\
2
\end{bmatrix}
\text{ and }\vect{u}=
\begin{bmatrix}
a_{1}\\
a_{2}
\end{bmatrix}.
$$

Then $\vect{u}$ is in $V^{\bot}$ is and only if $\vect{u}\ip\vect{v}=a_{1}+2a_{2}=0$. So we find that $V^{\bot}$ is the plane described by the equation $a_{1}+2a_{2}=0$. The vector $\vect{v}$ is a normal vector to this plane.

</li>

<li>
Let us now consider two vectors in $\R^{3}$, for example

$$
\vect{v}_{1}=
\begin{bmatrix}
2\\
1\\
-2
\end{bmatrix}
\quad\text{and}\quad\vect{v}_{2}=
\begin{bmatrix}
4\\
2\\
0
\end{bmatrix}.
$$

$V^{\bot}$ now consists of those vectors $\vect{u}$ that satisfy both $\vect{u}\ip\vect{v}_{1}=0$ and $\vect{u}\ip\vect{v}_{2}=0$. Solving this system of two equations in three variables, we find

$$
V^{\bot}=\left\{
    \begin{bmatrix}
    1t\\
    2t\\
    2t
    \end{bmatrix}
    \mid t\in\R
\right\},
$$

so $V^{\bot}$ is a line through the origin in three-dimensional space.

</li>

</ol>

:::

```{figure}  Images/Fig-Ortho-OrthoComp.svg
:name: Fig:Ortho:OrthoComp

The orthogonal complement of a 1-dimensional subspace of $\R^{2}$ (left) and a of a 2-dimensional subspace of $\R^{3}$ (right).
```

The plane we found for $V^{\bot}$ in {prf:ref}`Ex:Ortho:OrthoCompOfVect` is a plane through the origin. It is therefore also a subspace. This is not a coincidence, as {prf:ref}`Prop:Ortho:OrthoComplisSpace` shows.

:::{prf:proposition}
:label: Prop:Ortho:OrthoComplisSpace

For any subspace $V$ of $\R^{n}$, the orthogonal complement $V^{\bot}$ is a subspace, too. Moreover, the only vector that is both in $V$ and in $V^{\bot}$ is $\vect{0}$.

:::

:::{prf:proof}
:class: dropdown

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
:class: dropdown
 
Note that the second claim is easily derived from the first by substituting $A^{T}$ for $A$. Let $\vect{r}_{1},...,\vect{r}_{n}$ be the rows of $A$. Then $\vect{r}_{1}^{T},...,\vect{r}_{n}^{T}$ are the columns of $A^{T}$. For any vector $\vect{x}$ in $\R^{m}$, we have 

$$A\vect{x}=\begin{bmatrix}\vect{r}_{1}\vect{x}\\\vdots\\\vect{r}_{n}\vect{x}\end{bmatrix}=\begin{bmatrix}\vect{r}_{1}^{T}\ip\vect{x}\\\vdots\\\vect{r}_{n}^{T}\ip\vect{x}\end{bmatrix}.$$

Now, $\vect{x}$ is in $\mathrm{Nul}(A)$ precisely when $A\vect{x}=\vect{0}$ or, in other words, when $\vect{r}_{i}^{T}\ip\vect{x}=0$ for any $i$. Since the set $\left\{\vect{r}_{1}^{T},..,\vect{r}_{n}^{T}\right\}$ spans $\mathrm{Col}(A^{T})$, this is equivalent to $\vect{x}$ being in $\mathrm{Col}(A^{T})^{\bot}$.

:::