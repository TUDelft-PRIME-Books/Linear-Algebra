(Sec:SingValDec)=

# Singular Value Decomposition (SVD)

We have seen already how to factorise matrices in {numref}`Sec:MatFactor`, with the $LU$ and the $PLU$ factorisations. Another type of factorisation is the QR Decomposition in {numref}`Sec:Gram-Schmidt:QRdecomp`. In this section we will learn a new type of factorisation: the **singular value decomposition** (SVD). We will start with a few more properties of certain symmetric matrices followed by an algorithm for finding a SVD. The last two subsections will be devoted to understanding the decomposition and applications.

## More on Symmetric Matrices

Before we get into the singular value decomposition, we will need to further explore symmetric matrices. Let's start with a few properties that will be quite useful.

:::::{prf:proposition}
:label: Prop:SVD:propsymmat

Let $A$ be an $m\times n$ matrix with real entries. Then the following properties hold:

:::{latexlist}
:enumerated: true
:type: i

\item The matrices $AA^T$ and $A^TA$ are symmetric.
\item $\Nul{A} = \Nul{A^TA}$.
\item $\Rank{A} = \Rank{A^TA}$
\label{Item:Prop:SVD:propsymmat:samerankAandATA}
\item The eigenvalues of $A^TA$ are real and nonnegative.
\label{Item:Prop:SVD:propsymmat:nonzeroeigvals}
\item The non-zero eigenvalues of $AA^T$ are the same as the non-zero eigenvalues of $A^TA$.
\label{Item:Prop:SVD:propsymmat:sameeigvals}
:::

:::::

::::{prf:proof} (of {prf:ref}`Prop:SVD:propsymmat`)

:::{latexlist}
:enumerated: true
:type: i

\item Let's prove that $A^TA$ is symmetric. The proof for $AA^T$ is similar.
$$(A^TA)^T = A^T(A^T)^T = A^TA.$$

\item Let $\mathbf{u} \in \Nul{A}$. Then,

$$
A^TA \mathbf{u} = A^T(A\mathbf{u}) = A^T\mathbf{0} = \mathbf{0}.
$$

So $\mathbf{u} \in \Nul{A^TA}$.
Suppose that $\mathbf{v}\in \Nul{A^TA}$ Then, observe that

$$
0 = \mathbf{v}^TA^TA\mathbf{v} = \norm{A\mathbf{v}}^2,
$$

which implies that $A\mathbf{v}=\mathbf{0}$ and $\mathbf{v}\in\Nul{A}$.

\item Observe that since $A$ is an $m\times n$ matrix, we have that $A^TA$ is $n\times n$. Now, using {prf:ref}`Thm:BasisDim:RankThm` we have

$$
\Rank{A} = n - \dim{\Nul{A}} = n - \dim{\Nul{A^TA}} = \Rank{A^TA}.
$$

\item Since $A^TA$ is symmetric, the eigenvalues are real due to {prf:ref}`Prop:SymmetricMat:RealEigenvalues`. To see that they are non-negative, let $\mathbf{u}$ be an eigenvector of $A^TA$ with associated eigenvalue $\lambda$. Then,

$$0\le \mathbf{u}^TA^TA\mathbf{u} = \mathbf{u}^T\mathbf{u} = \lambda \norm{\mathbf{u}}^2.$$

Since $\mathbf{u}\ne \mathbf{0}$ it follows that $\lambda \ge 0$.

\item Let $\lambda$ be an non-zero eigenvalue of $A^TA$ with associated eigenvector $\mathbf{u}$. We will see that $\lambda$ is also an eigenvalue of $AA^T$. By definition of eigenvalue we have $A^TA\mathbf{u} = \lambda\mathbf{u}$. Then, multiplying by $A$ on both sides of the previous identity we obtain:

$$AA^TA\mathbf{u} = \lambda A\mathbf{u}.$$

Observe that if $A\mathbf{u}=\mathbf{0}$ then $A^TA\mathbf{u} = \mathbf{0}$ and $\lambda =0$, which contradicts the hypothesis of $\lambda \ne 0$. Therefore, $A\mathbf{u}\ne \mathbf{0}$ and $A\mathbf{u}$ is an eigenvector of $AA^T$ with associated eigenvalue $\lambda$.

To prove the reverse, one can follow a similar argument.

:::

::::

We want to stress out the importance of property {itemref}`Item:Prop:SVD:propsymmat:nonzeroeigvals`. We knew from {numref}`Sec:SymmetricMat` that the eigenvalues of a symmetric matrix were real. The previous proposition tells us that, in addition, **the eigenvalues of the symmetric matrix $A^TA$ are real and non-negative**. This is a property that will be key for the singular value decomposition.

(Subsec:SVD:Algorithm)=

## SVD (Algorithm)

As stated at the beginning of this section, the objective is to factor an $m\times n$ matrix $A$ with rank $p$. In this case, we will factorise it as a product of three matrices $U$, $S$, $V$ in the following manner:

$$ A = USV^T$$

with the following properties

:::{latexlist}

\item $U$ is an $m\times m$ orthogonal matrix,

\item $V$ is an $n\times n$ orthogonal matrix,

\item $S$ is an $m\times n$ matrix has zeros in every entry except in the components $S_{ii}=s_i$ for $i=1,2,\dots,p=\Rank{A}$, with $s_1\ge s_2\ge\cdots\ge s_p > 0$.

:::

Let $r=\min\{m,n\}$. The numbers $s_1 \ge s_2 \ge \cdots \ge s_p > s_{p+1}= 0 = \stackrel{r-p}{\cdots} = s_{r}$ are the **singular values of $A$**.

In other words, the decomposition would look like this:

$$
U\begin{bmatrix}
s_1 & 0 & \cdots & \cdots& 0 \\
0  & s_2 & \ddots &  & \vdots \\
\vdots & \ddots & \ddots & \ddots &\vdots \\
\vdots & & \ddots & \ddots & 0 \\
0 & \cdots & \cdots & 0 & s_r & & & \\
\end{bmatrix} V^T, \quad m < n
$$

or

$$
U\begin{bmatrix}
s_1 & 0 & \cdots & \cdots& 0 \\
0  & s_2 & \ddots &  & \vdots \\
\vdots & \ddots & \ddots & \ddots &\vdots \\
\vdots & & \ddots & \ddots & 0 \\
0 & \cdots & \cdots & 0 & s_r   \\
\\
\\
\end{bmatrix} V^T, \quad m > n
$$

where $r=\min\{m,n\}$.

Observe that with the choices above we obtain the following property.

::::{prf:proposition} Computing Singular Values
:label: Propo:SVD:singularvalues

Let $A$ be an $m\times n$ matrix with rank $p$ and let $r=\min\{m,n\}$. Let $U$ be an $m\times m$ orthogonal matrix whose columns represent an orthonormal basis of $\mathbb{R}^m$, $V$ an $n\times n$ orthogonal matrix whose columns represent an orthonormal basis of $\mathbb{R}^n$, and $S$ an $m\times n$ matrix with zeros in every component except in $S_{ii}$ for $i=1,\dots,p$ where $S_{ii}=s_i$ are the singular values in descendent order. Suppose that $A=USV^T$. Then,
$s_i=\sqrt{\lambda_i}$ where $\lambda_i$ is a nonzero eigenvalue of $A^TA$ for $i=1,\dots, p$. The remaining $r-p$ singular values are zero.

::::

::::{prf:proof}

With these choices for $U$, $S$ and $V$ and $r=\min\{m,n\}$ we have that

$$
A^TA= (USV^T)^T(USV) = VS^T(U^TU)SV^T = V(S^TS)V^T
$$

Observe that $S^TS$ is an $n\times n$ diagonal matrix, and $V(S^TS)V^T$ is an orthogonal diagonalisation of $A^TA$.

Due to the similarity between $A^TA$ and $S^TS$, the diagonal elements of $S^TS$ are equal to the eigenvalues of $A^TA$. In other words, $(S^TS)_{ii}=\lambda_i$ where $\lambda_i$ is an eigenvalue of $A^TA$. So $s_i = \sqrt{\lambda_i}$.

By property {itemref}`Item:Prop:SVD:propsymmat:samerankAandATA` of {prf:ref}`Prop:SVD:propsymmat`, we know that $\Rank A = \Rank A^TA$. Then,

:::{latexlist}

\item If $n\le m$ we have that $r=n$, and if $p = r$, then $(S^TS)$ has non-zero elements in its main diagonal and $(S^TS)_{ii} = s_i^2 = \lambda_i$ for $i=1,\dots,p$. If $p < n$, then $A^TA$ has, in addition, a zero eigenvalue with multiplicity $r-p$.

\item If $n>m$ then $r=m$ so $p\le r < n$ and $(S^TS)$ has non-zero elements $(S^TS)_{ii}=s_i^2=\lambda_i$ for $i=1,\dots, p$ and zeros for $r\ge i > p$. In other words, $A^TA$ has a zero eigenvalue with multiplicity $r-p$.

:::

::::

Now we are ready to find a singular value decomposition of $A$.

::::{prf:algorithm}
:label: Alg:SVD:SVDalgorithm

1. Compute $A^TA$.

2. Find an orthogonal diagonalisation $QDQ^T$ of $A^TA$ in such a way that $D$ has its eigenvalues sorted in descending order in the main diagonal.

3. Construct $S$ setting zeros in every component except in the main diagonal following this rule: $S_{ii}=\begin{cases} \sqrt{\lambda_i},  & i \le \Rank A, \\ 0, &\text{otherwise}.\end{cases}$

4. Take $V=Q$.

5. Consider the basis $\lbrace\mathbf{v}_1,\dots,\mathbf{v}_n\rbrace$ the columns of $V$. Compute $\mathbf{u}_i = \frac{1}{s_i}A\mathbf{v_i}$ for $i=1,\dots,r$. If $n < m$ complete the set $\{\mathbf{u}_1,\dots,\mathbf{u}_r\}$ to an orthonormal basis of $\mathbb{R}^m$

6. Construct $U$ an $m\times m$ matrix with columns given by $\{\mathbf{u}_1,\dots,\mathbf{u}_m\}$.

::::

::::{note}

Notice that, with our choice of $V$, the vectors $\{\mathbf{v}_1,\dots,\mathbf{v}_n\}$ form an orthonormal basis of $\mathbb{R}^n$. Now let's consider the vectors $\mathbf{u}_i = \frac{1}{s_i}A\mathbf{v}_i$ and $\mathbf{u}_j = \frac{1}{s_j}A\mathbf{v}_j$. We can see that

$$
\mathbf{u}_i\cdot\mathbf{u}_j = \frac{1}{s_is_j}A\mathbf{v}_i\cdot A\mathbf{v}_j = \frac{1}{s_is_j}\mathbf{v}_i^TA^TA\mathbf{v}_j = \frac{s_j}{s_i}\mathbf{v}_i^T\mathbf{v}_j = \frac{s_j}{s_i}\mathbf{v}_i\cdot \mathbf{v}_j = \begin{cases}1&i=j\\0& i\neq j\end{cases}
$$

So the vectors $\mathbf{u}_i$ form an orthonormal set.

If we compute

$$
AA^T\mathbf{u}_i = AA^T\left(\frac{1}{s_i}A\mathbf{v_i}\right) = A\left(\frac{1}{s_i}A^TA\mathbf{v}_i\right) = \frac{1}{s_i}A(\lambda_i\mathbf{v}_i) =\lambda_i \left( \frac{1}{s_i}A\mathbf{v}_i\right)=\lambda_i \mathbf{u}_i,
$$

we see that, in addition, $\mathbf{u}_i$ is a unit eigenvector of $AA^T$ with associated eigenvalue $\lambda_i$.

Therefore, if need to complete the the orthonormal set $\lbrace \mathbf{u}_1,\dots, \mathbf{u}_r$ to an orthonormal basis of $\mathbb{R}^n$ we just need to find an orthonormal basis of $\Nul A$.

::::

The details on why this algorithm works will be given in {numref}`Sec:ProofSVD`. For now, let's apply this algorithm in one particular example.

::::{prf:example}

Let's find the singular values of the matrix

$$
A = \begin{bmatrix}
5 & -1 \\
-3 & 2 \\
-1 & 3
\end{bmatrix},
$$

and then construct the matrix $S$ according to the description above.

Following the steps mentioned above, we compute $A^TA$:

$$
A^TA = \begin{bmatrix}
35 & -14 \\
-14 & 14
\end{bmatrix}
$$

The eigenvalues, sorted by value, are:

$$
\lambda_1 \ge \lambda_2
$$

with $\lambda_1 = 42$, $\lambda_2 = 7$.

The singular values are $s_1 = \sqrt{42}$, and $s_2=\sqrt{7}$.

Our matrix $S$ is

:::{math}
:label: Ex:SVD:S
S = \begin{bmatrix}
\sqrt{42} & 0 \\
0 & \sqrt{7} \\
0 & 0
\end{bmatrix}.
:::

::::

Now let's find $V$.

:::{prf:remark}

When finding a orthogonal diagonalisation of $QDQ^T=A^TA$ different choices for orthonormal eigenvectors lead to different matrices $Q$, the choice for $Q$ is not unique! And neither is the singular value decomposition.

:::

::::{prf:example}

Let's compute the matrix $V$ for the previous example. We had $A^TA = \begin{bmatrix}
26 & -17 & -8 \\
-17 & 13 & 9 \\
-8 & 9 & 10
\end{bmatrix}$.

:::{latexlist}

\item We can see that for $\lambda=42$ we can take a corresponding eigenvector $\mathbf{w}_1 = \begin{bmatrix} 2 \\ -1 \end{bmatrix}$, and normalising it, $\mathbf{v}_1=\frac{1}{\sqrt{5}}\mathbf{w}_1$.

\item For $\lambda_2=7$ one possible eigenvector is $\mathbf{w}_2 = \begin{bmatrix}1 \\ 2 \end{bmatrix}$, and normalising it we can take $\mathbf{v}_2 = \frac{1}{\sqrt{5}}\mathbf{w}_2$.

:::

Therefore, our matrix $V$ will be

:::{math}
:label: Ex:SVD:matrixV

V =
\frac{1}{\sqrt{5}}\begin{bmatrix}
2 & 1\\
-1 & 2
\end{bmatrix}

:::

::::

Now let's construct $U$ according to {prf:ref}`Alg:SVD:SVDalgorithm`.

:::{prf:remark}

This is where the properties described in {prf:ref}`Prop:SVD:propsymmat` come in handy. Specially property {itemref}`Item:Prop:SVD:propsymmat:sameeigvals`. Notice that in our previous example, our matrix $A$ has dimensions $3\times 2$. This means that we will need to complete the set of vectors $\{\mathbf{u}_1,\mathbf{u}_2\}$ to an orthonormal basis of $\mathbb{R}^3$. According to {prf:ref}`Propo:SVD:singularvalues`, the matrix $AA^T$ has one zero eigenvalue. Therefore, it will be enough to find an orthonormal basis for $\Nul A$.

:::

Since the vectors $\mathbf{u}_i$ are unit eigenvectors of $AA^T$, completing the orthonormal set to an orthonormal basis of $\mathbb{R}^m$ leads to an orthogonal diagonalisation of $AA^T=U\tilde{D}U^T$. The elements in the main diagonal of $\tilde{D}$ are $\lambda_i>0$ for $i \le \Rank A$ and $0$ for $i>\Rank A$ where $\lambda_i$ is an eigenvalue of $A^TA$ (which were already computed).

::::{prf:example}

Let's find a matrix $U$ that will provide an SVD for our set of examples.

Since $A = \begin{bmatrix} 
5 & -1 \\
-3 & 2 \\
-1 & 3
\end{bmatrix}$, we compute

$$
\mathbf{u}_1 = \frac{1}{s_1}\mathbf{v}_1  = \frac{1}{\sqrt{42}}\left( \frac{1}{\sqrt{5}}
\begin{bmatrix}
11 \\ -8 \\ -1
\end{bmatrix} \right) = \frac{1}{\sqrt{210}}
\begin{bmatrix}
11 \\ -8 \\ -1
\end{bmatrix}
$$

$$
\mathbf{u}_2 = \frac{1}{s_2}A\mathbf{v}_2 = \frac{1}{\sqrt{7}}\left(\frac{1}{\sqrt{5}}\begin{bmatrix} 3 \\ 1\\ 5\end{bmatrix}\right) = \frac{1}{\sqrt{35}}\begin{bmatrix} 3 \\ 1\\ 5\end{bmatrix}
$$

Now, we need to find a basis for $\Nul{AA^T}$. We need to solve

$$
AA^T\mathbf{\tilde{u}}_3 = \begin{bmatrix}
26 & -17 & -8 \\
-17 & 13 & 9 \\
-8 & 9 & 10
\end{bmatrix} \mathbf{\tilde{u}}_3 = \mathbf{0}
$$

We can see that one solution is $\mathbf{\tilde{u}}_3= \begin{bmatrix} 1 \\ 2 \\ -1\end{bmatrix}$. Since all the eigenvectors correspond to different eigenvalues, it is enough to normalize $\mathbf{\tilde{u}}_3$ to obtain the third vector:

$$
\mathbf{u}_3 = \frac{1}{\sqrt{6}}\begin{bmatrix} 1 \\ 2 \\ -1\end{bmatrix}.
$$

Then, we can write $U$ as

:::{math}
:label: Ex:SVD:matrixU

U = \begin{bmatrix}
\frac{11}{\sqrt{210}} & \frac{3}{\sqrt{35}} & \frac{1}{\sqrt{6}} \\
-\frac{8}{\sqrt{210}} & \frac{1}{\sqrt{35}} & \frac{2}{\sqrt{6}} \\
-\frac{1}{\sqrt{210}} & \frac{5}{\sqrt{35}} & \frac{-1}{\sqrt{6}} \\
\end{bmatrix}

:::

::::

With the matrices $S$, $U$ and $V$ described in {eq}`Ex:SVD:S`, {eq}`Ex:SVD:matrixV`, and {eq}`Ex:SVD:matrixU`, we have that

$$
\begin{bmatrix}
5 & -1 \\
-3 & 2 \\
-1 & 3
\end{bmatrix} =
\begin{bmatrix}
\frac{11}{\sqrt{210}} &  \frac{3}{\sqrt{35}} &  \frac{1}{\sqrt{6}} \\
-\frac{8}{\sqrt{210}} &  \frac{1}{\sqrt{35}} &  \frac{2}{\sqrt{6}} \\
-\frac{1}{\sqrt{210}} &   \frac{5}{\sqrt{35}} &  \frac{-1}{\sqrt{6}}
\end{bmatrix}
\begin{bmatrix}
        \sqrt{42} & 0 \\
        0 & \sqrt{7} \\
        0 & 0
        \end{bmatrix}
\begin{bmatrix}
\frac{2}{\sqrt{5}}  & \frac{1}{\sqrt{5}} \\
\frac{-1}{\sqrt{5}} & \frac{2}{\sqrt{5}}
\end{bmatrix}^T
$$

(Subsec:SVDGeometrically)=

## Understanding SVD Geometrically

In this section we will have a deeper look to the decomposition and its meaning. As we have done previously, let's think about our $m\times n$ matrix $A$ as the standard matrix of a linear transformation from $R^n$ to $R^m$.

Observe that, in order to find a SVD in the previous example for a matrix $A$ we took the matrices $U$, whose columns represent an orthogonal basis of $R^m$; and $V$, whose columns represent an orthogonal basis of $R^n$. Then, we think of our decomposition $USV^T$ as a composition of transformations that we can visualise using the graph in {numref}`Figure %s <Fig:SVD:decomposition>`:

:::{figure} Images/Fig-SVD-Decomposition.svg
:width: 300px
:name: Fig:SVD:decomposition

Diagram showing the SVD as a composition of linear transformations.

:::

To better understand it, let's visualise how the unit circle changes under these transformations.

::::{prf:example}
Let $A$ be the standard matrix of a linear transformation given by:

$$
A = \begin{bmatrix}
1 & -1 \\
2 & 2
\end{bmatrix}.
$$

The singular values for this matrix are $s_1 = 2\sqrt{2}$, and $s_2 = \sqrt{2}$. We choose

$$
V =\begin{bmatrix} \frac{1}{2} \, \sqrt{2} & \frac{1}{2} \, \sqrt{2} \\
\frac{1}{2} \, \sqrt{2} & -\frac{1}{2} \, \sqrt{2} \end{bmatrix}
$$

and

$$
U = \begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}
$$

{numref}`Figure %s <Fig:SVD:decompositioneffects>` shows how the unit circle changes under the singular value decomposition.

Notice that $V^T$ corresponds to a transformation consisting in a reflection over the line $y=x$ followed by a rotation of angle $-\frac{\pi}{4}$. So the unit circle is mapped on the unit circle.

The matrix $S$ contains the singular values. We can observe that the unit circle is mapped into an ellipse whose positive semi-axes have length equal to the singular values.

Finally, the matrix $U$ can be interpreted as a reflection over the line $y=x$.

:::{figure} s
:name: Fig:SVD:decompositioneffects

Effects of the transformations on the unit circle.
:::
::::

In general, since $V^T$ is an orthogonal matrix, it will map the $\mathbb{R}^n$ to itself and it will preserve the norm of vectors. We have seen in the example above that the unit circle in $\mathbb{R}^2$ was mapped into itself since $V^T$ was a rotation plus a reflection. This is true in general in any dimension. The same can be said for $U$. However, for $S$, we can see that the unit circle was mapped into an ellipse in $\mathbb{R}^2$ with the length of the semi-axes equal to the singular values. In general, the effect of $S$ is to change the length of the standard unit vectors according to the singular values. So, the unit circle would be mapped to an ellipsoid. It is important to notice that the number of non-zero eigenvalues is equal to the rank of the matrix $A$.

## SVD (Mathematical Details)

In the previous subsections we have explored how to compute a singular value decomposition and we understood it geometrically. We also saw that if an SVD exists, then it is not unique. In this subsection we discuss the existence.

::::{prf:theorem} Existence of SVD
:label: Thm:SVD:ExistenceSVD

Let $A$ be an $m\times n$ matrix of rank $p$ with real coefficients. Then there exist orthogonal matrices $V$ and $U$ with real coefficients, with dimensions $n\times n$ and $m\times m$ respectively, and unique real numbers $s_1\ge s_2 \ge \cdots \ge s_p > 0$ such that

$$
A = USV^T,
$$

where S is an $m\times n$ matrix whose components $S_{ii}=s_i$ for $i = 1,\dots ,p$ and zeros everywhere else.

::::

The proof of this theorem is not trivial and it requires some work. If the reader is interested in the proof, it could be found in {numref}`Sec:ProofSVD`.

What we can take out of this theorem is that there always exists a singular value decomposition of a matrix.

## Linear Least Squares Revisited
