(Sec:OrthoComp)=
# Orthogonal complements

In this section, we will introduce the orthogonal complement of a subspace. This concept will help us compute orthogonal projections easily.

:::{prf:definition}

Suppose $V$ is a subspace of $\R^{n}$. Then the **orthogonal complement** of $V$ is the set 

$$

V^{\bot}=\left\{\vect{u}\in\R^{n}\mid \vect{u}\ip\vect{v}=0\text{ for all } \vect{v}\text{ in }V\right\}.

$$

in other words, it is the set of all vectors that are orthogonal to all of $V$.

:::

:::{prf:remark}

For a vector to be in $V^{\bot}$, it suffices that it is orthogonal to all elements in a basis of $V$ or, slightly more general, to all elements in a spanning set of $V$. 

:::

Let us consider some simple examples.


:::{prf:Example}
:label: Ex:OrthoComp:OrthoCompOfVect

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

Both examples are illustrated in {numref}`Figure %s <Fig:OrthoComp:OrthoComp>`.

</ol>

:::

```{figure}  Images/Fig-OrthoComp-OrthoComp.svg
:name: Fig:OrthoComp:OrthoComp

The orthogonal complement of a 1-dimensional subspace of $\R^{2}$ (left) and of a 2-dimensional subspace of $\R^{3}$ (right).
```

In {prf:ref}`Ex:OrthoComp:OrthoCompOfVect`, we found $V^{\bot}$ to be once a plane through the origin and once a line through the origin. It was therefore, in both cases, a subspace. This is not a coincidence, as {prf:ref}`Prop:OrthoComp:OrthoComplisSpace` shows.

:::{prf:proposition}
:label: Prop:OrthoComp:OrthoComplisSpace

For any subspace $V$ of $\R^{n}$, the orthogonal complement $V^{\bot}$ is a subspace, too. Moreover, the only vector that is both in $V$ and in $V^{\bot}$ is $\vect{0}$.

:::

:::{prf:proof}
:class: dropdown

Since the zero vector is orthogonal to any vector, it is in $V^{\bot}$. Suppose now that $\vect{u}_{1}$ and $\vect{u}_{2}$ are in $V^{\bot}$. Then, for arbitrary $\vect{v}$ in $V$, $(\vect{u}_{1}+\vect{u}_{2})\ip \vect{v}=\vect{u}_{1}\ip\vect{v}+\vect{u}_{2}\ip\vect{v}=0$, so $\vect{u}_{1}+\vect{u}_{2}$ is in $V^{\bot}$.

Assume now that $\vect{u}$ is in $V^{\bot}$ and that $c$ is any scalar. Then, again for every $\vect{v}$ in $V$, $(c\vect{u})\ip\vect{v}=c(\vect{u}\ip\vect{v})=0$ so $c\vect{u}$ is in $V^{\bot}$. This shows that $V^{\bot}$ is a subspace.

If $\vect{v}$ is both in $V$ and $V^{\bot}$, then $\vect{v}\ip\vect{v}=0$ so $\vect{v}=\vect{0}$.

:::

As we have seen in {numref}`Sec:SubspacesRn`, both the column space and null space of any $n\times m$ matrix are subspaces of $\R^{n}$ and $\R^{m}$, respectively. It turns out that the transposition ${}^{T}$ and the orthogonal complement ${}^{\bot}$ relate these two spaces to each other.


:::{prf:proposition}
:label: Prop:OrthoComp:OrthoComplementNulA

For any $n\times m$ matrix $A$ we have $\mathrm{Col}(A^{T})^{\bot}=\mathrm{Nul}(A)$ and $\mathrm{Col}(A)^{\bot}=\mathrm{Nul}(A^{T})$.

:::

:::{prf:proof}
:class: dropdown
 
Note that the second claim is easily derived from the first by substituting $A^{T}$ for $A$. Let $\vect{r}_{1},...,\vect{r}_{n}$ be the rows of $A$. Then $\vect{r}_{1}^{T},...,\vect{r}_{n}^{T}$ are the columns of $A^{T}$. For any vector $\vect{x}$ in $\R^{m}$, we have 

$$A\vect{x}=\begin{bmatrix}\vect{r}_{1}\vect{x}\\\vdots\\\vect{r}_{n}\vect{x}\end{bmatrix}=\begin{bmatrix}\vect{r}_{1}^{T}\ip\vect{x}\\\vdots\\\vect{r}_{n}^{T}\ip\vect{x}\end{bmatrix}.$$

Now, $\vect{x}$ is in $\mathrm{Nul}(A)$ precisely when $A\vect{x}=\vect{0}$ or, in other words, when $\vect{r}_{i}^{T}\ip\vect{x}=0$ for any $i$. Since the set $\left\{\vect{r}_{1}^{T},..,\vect{r}_{n}^{T}\right\}$ spans $\mathrm{Col}(A^{T})$, this is equivalent to $\vect{x}$ being in $\mathrm{Col}(A^{T})^{\bot}$.

:::

:::{prf:remark}

Since, for any matrix $A$, the rows of $A$ are the columns of $A^{T}$, $\mathrm{Row}(A)=\mathrm{Col}(A^{T})$. {prf:ref}`Prop:OrthoComp:OrthoComplementNulA` then implies that $\mathrm{Row}(A)^{\bot}=\mathrm{Nul}(A)$.

:::

The strength of {prf:ref}`Prop:OrthoComp:OrthoComplementNulA` lies mainly in the fact that it allows us to actually find the orthogonal complement of a given subspace. 

:::{prf:Example}

Let $V$ be the subspace of $\R^{5}$ spanned by the vectors

$$
\vect{v}_{1}=
\begin{bmatrix}
1\\
3\\
-1\\
5\\
2
\end{bmatrix},\vect{v}_{2}=
\begin{bmatrix}
2\\
5\\
4\\
-1\\
-3
\end{bmatrix}, \quad\text{and}\quad\vect{v}_{3}
\begin{bmatrix}
4\\
11\
2\\
9\\
1
\end{bmatrix}.
$$

$V$ is, by definition, the column space of the matrix $A=[\vect{v}_{1}\,\vect{v}_{2}\,\vect{v}_{3}]$. By {prf:ref}`Prop:OrthoComp:OrthoComplementNulA`, we can find the orthogonal complement of $V$ by finding the null space of $A^{T}$. By standard computations we find:

$$
A^{T}=\begin{bmatrix}
1&3&-1&5&2\\
2&5&4&-1&-3\\
4&11&2&9&1
\end{bmatrix}\sim
\begin{bmatrix}
1&0&17&-28&-19\\
0&1&-6&11&7\\
0&0&0&0&0
\end{bmatrix},
$$

so

$$
V^{\bot}=\mathrm{Nul}(A^{T})=\left\{
    \begin{bmatrix}
    -17x_{3}+28x_{4}+19x_{5}\\
    6x_{3}-11x_{4}-7x_{5}\\
    x_{3}\\
    x_{4}\\
    x_{5}
    \end{bmatrix}\mid x_{3},x_{4},x_{5}\in\R
\right\}.
$$

:::



:::{prf:proposition}

If $V$ is a subspace of $\R^{n}$, then $\dim(V)+\dim(V^{\bot})=n$.

:::

:::{prf:proof}
:class: dropdown


Let $A$ be a matrix for which the columns are a basis of $V$. Then $n$ is the number of rows of $A$ which in turn is the number of columns of $A^{T}$. By {prf:ref}`Thm:BasisDim:DimensionTheorem` and {prf:ref}`Prop:OrthoComp:OrthoComplementNulA`, we find 

$$
n=\dim(\mathrm{Col}(A^{T}))+\dim(\mathrm{Nul}(A^{T}))=\dim(\mathrm{Col}(A^{T}))+\dim(\mathrm{Col}(A)^{\bot}).
$$

Using {prf:ref}`Prop:BasisDim:EqualDimRowColSpace` and $\mathrm{Row}(A^{T})=\mathrm{Col}(A)$, we find therefore:

$$
n=\dim(\mathrm{Row}(A^{T}))+\dim(\mathrm{Col}(A)^{\bot})=\dim(\mathrm{Col}(A))+\dim(\mathrm{Col}(A)^{\bot}).
$$

:::

:::{prf:proposition}
:label: Prop:OrthoComp:PrthoDecomp

Let $V$ be a subspace of $\R^{n}$. For an arbitrary vector $\vect{u}$ in $\R^{n}$, there exist _unique_ vectors $\vect{u}_{V}$ and $\vect{u}_{V^{\bot}}$ in $V$ and $V^{\bot}$, respectively, such that $\vect{u}=\vect{u}_{V}+\vect{u}_{V^{\bot}}$. This is called the **orthogonal decomposition** of $\vect{u}$ with respect to $V$.

:::

:::{prf:proof}
:class: dropdown

Let $\vect{v}_{1},...,\vect{v}_{k}$ be a basis for $V$ and let $\vect{v}_{k+1},...,\vect{v}_{n}$ be a basis for $V^{\bot}$. We claim that the vectors $\vect{v}_{1},...,\vect{v}_{k},\vect{v}_{k+1},...,\vect{v}_{n}$ are linearly independent. Indeed, if there were a linear combination 

$$
c_{1}\vect{v}_{1}+\cdots+c_{k}\vect{v}_{k}+c_{k+1}\vect{v}_{k+1}+\cdots +c_{n}\vect{v}_{n}=\vect{0}
$$

we would find that

$$
\vect{w}=c_{1}\vect{v}_{1}+\cdots+c_{k}\vect{v}_{k}=-c_{k+1}\vect{v}_{k+1}-\cdots -c_{n}\vect{v}_{n}
$$

is in both $V$ and $V^{\bot}$. By {prf:ref}`Prop:OrthoComp:OrthoComplisSpace`, $\vect{w}=\vect{0}$. Since $\vect{v}_{1},...,\vect{v}_{k}$ and $\vect{v}_{k+1},...,\vect{v}_{n}$ are bases, it follows that all $c_{i}$ are $0$.

Since $\vect{v}_{1},...,\vect{v}_{k},\vect{v}_{k+1},...,\vect{v}_{n}$ is a linearly independent set of $n$ vectors in $n$-dimensional space, it must be a basis. Consequently, every vector $\vect{u}$ in $\R^{n}$ can be written in a unique way as a linear combination

$$
\vect{u}=c_{1}\vect{v}_{1}+\cdots+c_{k}\vect{v}_{k}+c_{k+1}\vect{v}_{k+1}+\cdots +c_{n}\vect{v}_{n}.
$$

Putting $\vect{u}_{V}=c_{1}\vect{v}_{1}+\cdots+c_{k}\vect{v}_{k}$ and $\vect{u}_{V^{\bot}}=c_{k+1}\vect{v}_{k+1}+\cdots +c_{n}\vect{v}_{n}$ finishes the proof.

:::

```{figure}  Images/Fig-OrthoComp-OrthoDecomp.svg
:name: Fig:OrthoBase:OrthoDecomp

A subspace $V$, a vector $\vect{u}$ and the orthogonal decomposition of $\vect{u}$ with respect to $V$.
```