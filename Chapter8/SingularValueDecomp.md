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
$$ A^TA \mathbf{u} = A^T(A\mathbf{u}) = A^T\mathbf{0} = \mathbf{0}.$$
So $\mathbf{u} \in \Nul{A^TA}$.
Suppose that $\mathbf{v}\in \Nul{A^TA}$ Then, observe that 
$$ 0 = \mathbf{v}^TA^TA\mathbf{v} = \norm{A\mathbf{v}}^2,$$
which implies that $A\mathbf{v}=\mathbf{0}$ and $\mathbf{v}\in\Nul{A}$.

\item Observe that since $A$ is an $m\times n$ matrix, we have that $A^TA$ is $n\times n$. Now, using {prf:ref}`Thm:BasisDim:RankThm` we have

$$ \Rank{A} = n - \dim{\Nul{A}} = n - \dim{\Nul{A^TA}} = \Rank{A^TA}.$$

\item Since $A^TA$ is symmetric, the eigenvalues are real due to {prf:ref}`Prop:SymmetricMat:RealEigenvalues`. To see that they are non-negative, let $\mathbf{u}$ be an eigenvector of $A^TA$ with associated eigenvalue $\lambda$. Then,

$$0\le \mathbf{u}^TA^TA\mathbf{u} = \mathbf{u}^T\mathbf{u} = \lambda \norm{\mathbf{u}}^2.$$

Since $\mathbf{u}\ne \mathbf{0}$ it follows that $\lambda \ge 0$.


\item Let $\lambda$ be an non-zero eigenvalue of $A^TA$ with associated eigenvector $\mathbf{u}$. We will see that $\lambda$ is also an eigenvalue of $AA^T$. By definition of eigenvalue we have $A^TA\mathbf{u} = \lambda\mathbf{u}$. Then, multiplying by $A$ on both sides of the previous identity we obtain:

$$AA^TA\mathbf{u} = \lambda A\mathbf{u}.$$

Observe that if $A\mathbf{u}=\mathbf{0}$ then $A^TA\mathbf{u} = \mathbf{0}$ and $\lambda =0$, which contradicts the hypothesis of $\lambda \ne 0$. Therefore, $A\mathbf{u}\ne \mathbf{0}$ and $A\mathbf{u}$ is an eigenvector of $AA^T$ with associated eigenvalue $\lambda$.

To prove the reverse, one can follow a similar argument.

:::

::::

We want to stress out the importance of property {itemref}`Item:Prop:SVD:propsymmat:nonzeroeigvals`. We knew from {numref}`Sec:SymmetricMat` that the eigenvalues of a symmetric matrix were real. However, the previous proposition tells us that in addition **the eigenvalues of a symmetric matrix are real and non-negative**. This is a property that will be key for the singular value decomposition.

## SVD (Algorithm)

As stated at the beginning of this section, the objective is to factor an $m\times n$ matrix $A$. In this case, we will factorise it as a product of three matrices $U$, $S$, $V$ in the following manner:

$$ A = USV^T$$

with the following properties

:::{latexlist}

\item $U$ is an $m\times m$ orthogonal matrix,
\item $V$ is an $n\times n$ orthogonal matrix,
\item $S$ is an $m\times n$ matrix has zeros in every entry except in the main diagonal.

:::

In other words, the decomposition would look like this:

$$ 
U\begin{bmatrix}
s_1 & 0 & \cdots & \cdots& 0 \\
0  & s_2 & \ddots &  & \vdots \\
\vdots & \ddots & \ddots & \ddots &\vdots \\
\vdots & & \ddots & \ddots & 0 \\
0 & \cdots & \cdots & 0 & s_k & & & \\
\end{bmatrix} V^T, \quad m < n
$$

or

$$ 
U\begin{bmatrix}
s_1 & 0 & \cdots & \cdots& 0 \\
0  & s_2 & \ddots &  & \vdots \\
\vdots & \ddots & \ddots & \ddots &\vdots \\
\vdots & & \ddots & \ddots & 0 \\
0 & \cdots & \cdots & 0 & s_k   \\
\\
\\
\end{bmatrix} V^T, \quad m > n
$$

::::{prf:definition} Singular Values
:label: Def:SVD:singularvalues

The singular values of an $m\times n$ matrix $A$ are the square roots of the non-negative eigenvalues of the matrix $A^TA$.

::::

Now we are ready to find the matrix $S$.  The algorithm is the following:

:::{latexlist}

\item Compute $A^TA$.
\item Find the $n$ eigenvalues of $A^TA$.
\item Sort the eigenvalues in the following way:

$$\lambda_1 \ge \lambda_2\ge \cdots\ge \lambda_k \ge \lambda_{k+1} = \cdots = \lambda_{n} = 0.$$

Notice that $\lambda_k$ is the smallest non-zero eigenvalue.

\item Construct $S$ as an $m\times n$ matrix with the ordered non-zero singular values $s_k=\sqrt{\lambda_k}$ in the main diagonal and zeros everywhere else. If $k < n$, then add $n-k$ zero columns. If $k < m$ add $m-k$ rows of zeros. This ensures that we obtain an $m\times n$ matrix.

:::

::::{prf:example}

Let's find the singular values of the matrix

$$A = \begin{bmatrix} 
5 & -1 \\
-3 & 2 \\
-1 & 3
\end{bmatrix},$$

and then construct the matrix $S$ according to the description above.

Following the steps mentioned above, we compute $A^TA$:

$$A^TA = \begin{bmatrix}
35 & -14 \\
-14 & 14
\end{bmatrix}$$

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

Now let's find $V$. By {prf:ref}`Thm:SymmetricMat:OrthogDiag` the matrix $A^TA$ orthogonally diagonalizes. That is, 

$$ A^TA = Q_1 D Q_1^{T} $$

where $Q_1$ is an orthogonal matrix. Therefore, find $Q_1$ with the following procedure:

:::{latexlist}

\item Find the eigenvalues of $A^TA$.
\item Construct $D$ by constructing a diagonal matrix with the eigenvalues in the main diagonal in descendant order.
\item Find $Q_1$ the corresponding orthogonal matrix.
\item Take $V=Q_1$.

:::


:::{prf:remark} 

Since different choices for eigenvectors lead to different matrices $Q$, the choice for $Q$ is not unique! And neither is the singular value decomposition.

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

To find $U$, we will consider the matrix $AA^T$. Since $AA^T$ is symmetric, it orthogonally diagonalises. We will take $U=Q_2$ where $Q_2$ is an orthogonal matrix such that $AA^T=Q_2 D Q_2^T$.

:::{prf:remark}

This is where the properties described in {prf:ref}`Prop:SVD:propsymmat` come in handy. Specially property {itemref}`Item:Prop:SVD:propsymmat:sameeigvals` since it tells us that we do not need to worry about finding the eigenvalues of $AA^T$, since the non-zero eigenvalues are the same as the eigenvalues of $A^TA$, which we already have computed.

:::

::::{prf:example}

Let's find a matrix $U$ that will provide a SVD for our set of examples.

Since $A = \begin{bmatrix} 
5 & -1 \\
-3 & 2 \\
-1 & 3
\end{bmatrix}$, we compute

$$
AA^T = \begin{bmatrix}
26 & -17 & -8 \\
-17 & 13 & 9 \\
-8 & 9 & 10
\end{bmatrix}
$$

We have three eigenvalues, but and two of them are non-zero $\lambda_1=42$, and $\lambda_2=7$ (as the non-zero eigenvalues coincide with the ones in $A^TA$). The third eigenvalue is $\lambda_3 = 0$.

We leave the computations of the eigenvectors to the reader. Our choice for $U$ is 

:::{math}
:label: Ex:SVD:matrixU

U = \begin{bmatrix}
\frac{11}{\sqrt{210}} &  \frac{3}{\sqrt{35}} &  \frac{1}{\sqrt{6}} \\
-\frac{8}{\sqrt{210}} &  \frac{1}{\sqrt{35}} &  \frac{2}{\sqrt{6}} \\
\frac{5}{\sqrt{210}} &   \frac{5}{\sqrt{35}} &  \frac{-1}{\sqrt{6}} \\
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
\frac{5}{\sqrt{210}} &   \frac{5}{\sqrt{35}} &  \frac{-1}{\sqrt{6}} 
\end{bmatrix}
\begin{bmatrix} 
        \sqrt{42} & 0 \\
        0 & \sqrt{7} \\
        0 & 0
        \end{bmatrix}
\begin{bmatrix}
\frac{2}{\sqrt{5}}  & \frac{1}{\sqrt{5}} \\
\frac{-1}{\sqrt{5}} & \frac{2}{\sqrt{5}}
\end{bmatrix}
$$


## Understanding SVD

In this section we will have a deeper look to the decomposition and its meaning. As we have done previously, let's think about our $m\times n$ matrix $A$ as the standard matrix of a linear transformation from $R^n$ to $R^m$.

Observe that, in order to find a SVD in the previous example for a matrix $A$ we took the matrices $U$, whose columns represent an orthogonal basis of $R^m$; and $V$, whose columns represent an orthogonal basis of $R^n$. Then, we think of our decomposition $USV^T$ as a composition of transformations that we can visualise using the graph in {numref}`Figure %s <Fig:SVD:decomposition>`:

:::{figure} Images/Fig-SVD-Decomposition.svg
:width: 300px
:name: Fig:SVD:decomposition

Diagram showing the SVD as a composition of linear transformations.

:::

To better understand it, let's visualise how the unit circle changes under these transformations.

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

We have seen these transformations before. Notice that $V^T$ corresponds to a transformation consisting in a reflection over the line $y=x$ followed by a rotation of angle $-\frac{\pi}{4}$. The matrix $U$ is just a reflection over the line $y=x$. We can see that the unit circle does not change for $V^T$. However, the matrix $S$ transforms the unit circle into an ellipse, whose positive semi-axes have length equal to the singular values.