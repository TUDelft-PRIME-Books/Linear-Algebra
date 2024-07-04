(Sec:SingValDec)=

# Singular Value Decomposition (SVD)

We have seen already several ways to factorise matrices. In {numref}`Sec:MatFactor`, we studied the $LU$ and the $PLU$ factorisations, and in  {numref}`Sec:Gram-Schmidt:QRdecomp`
we laid the QR Decomposition on the table. In {numref}`Sec:SymmetricMat` we showed that every symmetric (square) matrix $A$ can be written as  $A = QDQ^{-1} = QDQ^T$. In this section it is in a sense this last decomposition we will generalize to non-symmetric matrices, and even to non-square matrices.
We will introduce and study the so-called **singular value decomposition** (SVD) of a matrix.
In the first subsection ({numref}`Subsec:SVD:Definition`) we will give the definition of the SVD, and illustrate it with a few examples.  In the second subsection ({numref}`Subsec:SVD:Existence`) an algorithm to compute the SVD is presented and illustrated. And it will be shown that this algorithm always yields a proper SVD.
The last two subsections  will be devoted to understanding the SVD in a geometric way, and to possible practical uses of the SVD.

(Subsec:SVD:Definition)= 

## Definition of the Singular Value Decomposition

Let  $A$ be an $m\times n$ matrix, and let $p$ be the minimum of $m$ and $n$. 

::::{prf:definition}
:label: SymmetricMat:SVD:Definition

 A  **singular value decomposition** of  $A$ is a decomposition

$$
  A = U\Sigma V^T,
$$

where 

:::{latexlist}

\item $U$ is an $m\times m$ orthogonal matrix,

\item $V$ is an $n \times n$  orthogonal matrix,

\item $\Sigma$ is an $m\times n$ matrix which is zero everywhere, apart from the entries  $\Sigma_{ii} = \sigma_i$, $i = 1,\ldots , p$,  which are all $\geq 0$, and in decreasing order. That is,  $\sigma_1 \geq \sigma_2 \geq \ldots \geq \sigma_p$.

:::

The *nonnegative* numbers $\sigma_i$ are called the **singular values** of $A$.

::::   

So the decomposition will look like either 

::::{math}
:label: Eq:SVD:firstform

U\begin{bmatrix}
\sigma_1 & 0 & \cdots & \cdots& 0 & 0& \cdots& 0\\
0  & \sigma_2 & \ddots &  & \vdots& 0& \cdots& 0 \\
\vdots & \ddots & \ddots & \ddots &\vdots & \vdots & & \vdots\\
\vdots & & \ddots & \ddots & 0 &\vdots &  &  \vdots\\
0 & \cdots & \cdots & 0 & \sigma_p & 0& \cdots& 0\\
\end{bmatrix} V^T, \quad m \leq n

::::

or

::::{math}
:label: Eq:SVD:secondform

U\begin{bmatrix}
\sigma_1 & 0 & \cdots & \cdots& 0 \\
0  & \sigma_2 & \ddots &  & \vdots \\
\vdots & \ddots & \ddots & \ddots &\vdots \\
\vdots & & \ddots & \ddots & 0 \\
0 & \cdots & \cdots & 0 & \sigma_p   \\
 & & & &  \\
0 & 0   &  \cdots  & \cdots  & 0 \\
\vdots & \vdots & & \ &\vdots \\
0 & 0   &  \cdots  & \cdots  & 0 \\
\end{bmatrix} V^T, \quad m > n.

::::

That the singular values must be nonnegative keeps open the possibility that some of the (last) singular values may be 0.


::::{prf:example}
:label: Ex:SVD:firstSVD

For the matrix  $A = \begin{bmatrix}1&3\\2&2\\3&1  \end{bmatrix}$  a singular value decomposition is given by  $A = U\Sigma V^T$  where

$$
   U = \begin{bmatrix}\dfrac{1}{\sqrt{3}}&-\dfrac{1}{\sqrt{2}}&-\dfrac{1}{\sqrt{6}}\\
   \dfrac{1}{\sqrt{3}}&0&\dfrac{2}{\sqrt{6}}\\\dfrac{1}{\sqrt{3}}&\dfrac{1}{\sqrt{2}}&-\dfrac{1}{\sqrt{6}}  \end{bmatrix}, \quad
   \Sigma = \begin{bmatrix}\sqrt{24}&0\\0&2\\0&0  \end{bmatrix}, \quad
   V = \begin{bmatrix}\dfrac1{\sqrt{2}} &\dfrac1{\sqrt{2}} \\ \dfrac1{\sqrt{2}} & -\dfrac1{\sqrt{2}} \end{bmatrix}.
$$

Let us point out a few properties of this decomposition.

:::{latexlist}

\item The matrix $A$  has size $3\times2$, so $\Sigma$ is of the form depicted in {eq}`Eq:SVD:secondform`.



\item The third column of $U$ does not really play a role in the product,  since all its entries are multiplied by two zeros in the last row of $\Sigma$. <BR>
We can write this SVD in a more 'economic' form by leaving out the third column of $U$ and the third row of $\Sigma$: 

<BR>

$$

  A =  \begin{bmatrix}\dfrac{1}{\sqrt{3}}&-\dfrac{1}{\sqrt{2}}\\
   \dfrac{1}{\sqrt{3}}&0\\
   \dfrac{1}{\sqrt{3}}&\dfrac{1}{\sqrt{2}}  \end{bmatrix} 
  \begin{bmatrix}\sqrt{24}&0\\0&2\end{bmatrix}
   \begin{bmatrix}\dfrac1{\sqrt{2}} &\dfrac1{\sqrt{2}} \\ \dfrac1{\sqrt{2}} & -\dfrac1{\sqrt{2}} \end{bmatrix}^T

$$

\item The first two colums of $U$,  multiples of the vectors $\begin{bmatrix}1\\1\\1\end{bmatrix}$  and  $\begin{bmatrix}-1\\0\\1\end{bmatrix}$, give an orthonormal   basis of the column space of the matrix $A$.
$\begin{bmatrix}1\\1\\1\end{bmatrix} = \dfrac14\begin{bmatrix}1\\2\\3\end{bmatrix} +\dfrac14\begin{bmatrix}3\\2\\1\end{bmatrix}= \frac14\vect{a}_1 + \frac14\vect{a}_2$,
and  $\begin{bmatrix}-1\\0\\1\end{bmatrix} = \frac12\vect{a}_2 - \frac12\vect{a}_1$.

\item The two columns of the matrix $V$ give an orthonormal basis of the row space of the matrix $A$. (Which  is not so striking here, since that row space is the whole of $\R^2$.)

\item The number of nonzero singular values is two, which is equal to the number of independent columns (and also rows) of $A$, which is the *rank* of $A$.

\item
The decomposition can be rewritten in a way analogous to the spectral decomposition
{prf:ref}`Thm:SymmetricMat:SpectralDecomp`.

<BR>

%%::{math}
%%:label: Eq:SVD:SpectralDecomp
$$
   \begin{array}{ccl} A &=& \sigma_1 \mathbf{u}_1\mathbf{v}_1^T + \sigma_2\mathbf{u}_2\mathbf{v}_2^T  \\
     &=&  \sqrt{24} \begin{bmatrix}\dfrac{1}{\sqrt{3}} \\ \dfrac{1}{\sqrt{3}} \\ \dfrac{1}{\sqrt{3}}\end{bmatrix}
      \begin{bmatrix}\dfrac{1}{\sqrt{2}} & \dfrac{1}{\sqrt{2}}\end{bmatrix}
     + 2\begin{bmatrix}-\dfrac{1}{\sqrt{2}} \\0\\ \dfrac{1}{\sqrt{2}}\end{bmatrix}
     \begin{bmatrix}\dfrac{1}{\sqrt{2}} & -\dfrac{1}{\sqrt{2}}\end{bmatrix}
     \end{array}.
$$
%%::

With the spectral decomposition (see {prf:ref}`Thm:SymmetricMat:SpectralDecomp`) we found that any symmetric matrix $A$ can be written as a linear combination of rank one matrices $P_i$. Moreover, these matrices $P_i$ can be interpreted as projections onto orthogonal one-dimensional subspaces of $\R^n$. Here the least we can say is that we have written the matrix  $A$ of rank 2 as a linear combination of two rank 1 matrices.
:::

::::

The properties mentioned in {prf:ref}`Ex:SVD:firstSVD`  hold more generally.  We collect a few (and add a fourth) in the next proposition.

::::{prf:proposition} Basic properties of a singular value decomposition.
:label: Prop:SVD:BasicProp

Suppose $A = U\Sigma V^T$, with $U, \Sigma, V$ as in the definition.

:::{latexlist}
:enumerated: true
:type: i

\item The number $r$ of nonzero singular values is equal to the rank of $A$.
\item The first $r$ columns of $U$ give an orthonormal basis for the column space of $A$.
\item The first $r$ columns of $V$ give an orthonormal basis for the row space of $A$.
\item A singular value decomposition of the matrix $A^T$  is given by $A^T = V\Sigma^TU^T$.
\label{Item:Prop:SVD:BasicProp:Transpose}
:::

::::

::::{dropdown} Proof of&nbsp;{prf:ref}`Prop:SVD:BasicProp`

Suppose $\sigma_1>0, \ldots, \sigma_r>0$ and $\sigma_{r+1}=0 , \ldots, \sigma_p=0$, where $p=$min$\{m,n\}$.

We have to show that 

$$
 \Rank{A} = \dim \Col{A} = n - \dim \Nul{A} = r.
 $$

Now, since both the last $m-r$ rows of $\Sigma$ and the last $n-r$ columns of $\Sigma$ are zero, we can make use the economic form as in the previous example. By this we mean

:::{math}
:label: Eq:SVD:ReducedSVD

  A = U\Sigma V^T = U_r\Sigma_{rr}V_r^T

:::

where only the first $r$ columns of $U$ and $V$ are used, and where $\Sigma_{rr}$ is the top left $r \times r$ submatrix of $\Sigma$. Note that $\Sigma_{rr}$ is a diagonal matrix with no zeros on the diagonal. <BR>
Since $U_r$ and $U_r\Sigma_{rr}$  (where only the columns of $U_r$ are scaled) have independent columns,  the only situation where $A\mathbf{x}  =U_r\Sigma_{rr}V_r^T\mathbf{x} = \mathbf{0}$ is when
$V_r^T\mathbf{x} = \mathbf{0}$. So

$$
  \dim \Nul{A} = \dim \Nul{V_r^T} = n - \Rank{V_r^T} = n - \Rank{V_r} = n - r,
$$

as the columns of $V_r$ are linearly independent (they are even orthogonal).

It follows that indeed

$$
  \dim \Col{A} = n - \dim \Nul{A} = r.
$$

This proves i.

Implicitly we also almost proved ii. We only have to 'restrict' to the matrices $U_r, \Sigma_{rr}, V_r$, as in the previous example. <BR>
Namely,  since  $\Col{A} = \Col{(U_r\Sigma_{rr}V^T)}$  is contained in $\Col{U_r}$  (in an exercise in {numref}`Sec:BasisDim` it was stated that, provided  the product is defined, $\Col{AB}  \subseteq \Col{A}$),  and as both column spaces have dimension $r$, they must be equal.

$$
   \Col{A} =  \Col{U_r}.
$$

Since $U_r$ has $r$ linearly independent columns, these columns give a basis for $\Col{A}$.  Which settles for ii.

iv.  follows immediately from the definition of the SVD.  Namely,
if  $A = U\Sigma V^T$,  then  $A^T = V\Sigma^TU^T$,  where $V, \Sigma^T, U$  are still matrices with the required properties for an SVD.

Lastly iii.  follows from  ii.  by transposing the matrix, and making use of iv.

::::


The main goal is to show that a singular value decomposition always exists, and, how to construct one. Both answers are answered in reversed order in the next subsection

(Subsec:SVD:Existence)= 

## Existence of a Singular Value Decomposition

We start with an important observation that explains the central role of the matrix $A^TA$ in the algorithm to come.

::::{prf:proposition} Computing the Singular Values
:label: Prop:SVD:singularvalues

Let $A$ be an $m\times n$ matrix.  
The singular values of a matrix $A$ are the square roots of the (nonnegative!) eigenvalues of the $(n \times n)$  matrix $A^TA$.  Thus,  if $\lambda_1 \geq \lambda_2 \geq  \cdots \geq \lambda_n$ are the eigenvalues of $A^TA$,  then  $\sigma_i = \sqrt{\lambda_i}$ are the singular values of $A$. 

More specific, if $A$ is an $m\times n$ matrix with singular value decomposition $A = U\Sigma V^T$.  Then the 'diagonal' elements $\Sigma_{ii}$ of $\Sigma$,  i.e., the singular values $  \sigma_i$,  are the square roots of the eigenvalues $\lambda_i$ of the matrix $A^TA$.  <BR> 
Moreover,  the columns of $V$ are corresponding eigenvectors  (of $A^TA$).

::::



::::{dropdown} Proof of &nbsp;{prf:ref}`Prop:SVD:singularvalues`

First of all, because of the properties of the matrices $U$, $\Sigma$ and $V$ we have that

$$
A^TA= (U\Sigma V^T)^T(U\Sigma V) = V\Sigma^T(U^TU) \Sigma V^T = V(\Sigma^T\Sigma)V^T.
$$

Note that, since $\Sigma^T\Sigma$ is an $n\times n$ *diagonal* matrix,  $V(\Sigma^T\Sigma)V^T$ is an *orthogonal diagonalisation* of $A^TA$.  (Which is indeed a *symmetric* matrix.)

This immediately gives us that the columns of $V$ are eigenvectors for the eigenvalues of $A^TA$,  which  can be read off from the diagonal of $\Sigma^T\Sigma$.  That is,

$$
   A^TA \vect{v}_i = \lambda_i\mathbf{v}_i = \sigma_i^2\mathbf{v}_i,\quad  i = 1,2,\ldots,n.
$$

We can conclude that the singular values are given by  $\sigma_i = \sqrt{\lambda_i}$. <BR>
Note that by definition the square root of a number $a$ is the *nonnegative* number $b$ for which $b^2 = a$, which makes that automatically  $\sigma_i \geq 0$.

You may have a tiny tinge of worry.  How would I know that the eigenvalues $\lambda_i$  of the matrix $A^TA$ are *nonnegative*?  You may try to settle this yourself, or you can have a sneak preview at {prf:ref}`Prop:SVD:propertiesATA`.

::::

We are now ready to present the algorithm.
To be followed up by examples and some (theoretical) considerations.
Suppose $A$ is an $m\times n$ matrix of rank $r$. (The rank, as we have seen in {prf:ref}`Prop:SVD:BasicProp`, is the number of nonzero singular values.)

::::{prf:algorithm}
:label: Alg:SVD:SVDalgorithm

1. Compute $A^TA$.

2. Find the eigenvalues $\lambda_1 \geq \lambda_2 \geq \ldots \geq \lambda_n$
 of $A^TA$.

3. Construct the $m\times n$ matrix $\Sigma$,  putting zeros on every position except on  the main 'diagonal', where   $\Sigma_{ii}=\sigma_i = \sqrt{\lambda_i} $.

4. Compute a complete set of orthonormal eigenvectors $\mathbf{v}_1,\dots,\mathbf{v}_n$,
corresponding to $\lambda_1, \ldots, \lambda_n$,   and take them as columns in the matrix $V$.

5.  Compute $\mathbf{u}_i = \dfrac{1}{\sigma_i}A\mathbf{v}_i$,     for $i=1,\dots,r$,  where $r$ is the number of nonzero singular values. If $r < m$ extend the set $\{\mathbf{u}_1,\dots,\mathbf{u}_r\}$ to an orthonormal basis $\{\mathbf{u}_1, \dots ,\mathbf{u}_m\}$ of $\mathbb{R}^m$.

6. Construct the $m\times m$ matrix $U$  with columns  $\mathbf{u}_1$, $\dots$, $\mathbf{u}_m$.

::::

Apart from step 2., where we need the eigenvalues of an $n\times n$ matrix $A^TA$, every step can be worked out with pen and paper (though step 4. and step 5. can be  terribly error prone). <BR>
The step that, we think,  most needs some explaining is step 5.  Why does it lead to an *orthonormal* set of vectors $\{\mathbf{u}_1,\dots,\mathbf{u}_r\}$?  We will show that indeed it does in the proof of {prf:ref}`Thm:SVD:Existence`.  It is time for an example first  (no nice numbers though!).


::::{prf:example}
:label:  Ex:SVD:ComputeAnSVD1

We will find a singular value decomposition of the matrix
$
A = \begin{bmatrix}
5 & -1 \\
-3 & 2 \\
-1 & 3
\end{bmatrix}.
$


We follow the steps of the algorithm.

1.  We first compute $A^TA = \begin{bmatrix}
       35 & -14 \\
       -14 & 14
      \end{bmatrix}
      $.

2. The eigenvalues $\lambda_1 \ge \lambda_2$ of $A^TA$ are given by 
 $\lambda_1 = 42$, $\lambda_2 = 7$.  
 This gives us the singular values  $\sigma_1 = \sqrt{42}$, and $\sigma_2=\sqrt{7}$. 
  

3. Our matrix $\Sigma$  becomes $\Sigma = \begin{bmatrix}
\sqrt{42} & 0 \\
0 & \sqrt{7} \\
0 & 0
\end{bmatrix}$.

4.  We have to find the eigenvectors of $A^TA$ for $\lambda_1 = 42$, $\lambda_2 = 7$. <BR>
    Skipping the computations we find  $\mathbf{w}_1 = \begin{bmatrix} 2\\-1
\end{bmatrix}$ and  $\mathbf{w}_2 = \begin{bmatrix} 1\\2
\end{bmatrix}$.  <BR>
  Normalizing and putting them in a matrix gives  $V = \begin{bmatrix}
\frac{2}{\sqrt{5}} & \frac{1}{\sqrt{5}} \\[.5ex]
-\frac{1}{\sqrt{5}} & \frac{2}{\sqrt{5}}
\end{bmatrix}$.

5. We compute  <BR>
$\vect{u}_1 = \dfrac{1}{\sigma_1}A\vect{v}_1 = \dfrac{1}{\sqrt{42}}\times\dfrac{1}{\sqrt{5}} \begin{bmatrix}
5 & -1 \\
-3 & 2 \\
-1 & 3
\end{bmatrix} \begin{bmatrix} 2\\-1 \end{bmatrix} = \dfrac{1}{\sqrt{210}}\begin{bmatrix}11\\-8\\-5 \end{bmatrix}$ <BR>
and <BR>
$\vect{u}_2 = \dfrac{1}{\sigma_2}A\vect{v}_2 = \dfrac{1}{\sqrt{7}}\times\dfrac{1}{\sqrt{5}}\begin{bmatrix}
5 & -1 \\
-3 & 2 \\
-1 & 3
\end{bmatrix} \begin{bmatrix} 1\\2 \end{bmatrix} = \dfrac{1}{\sqrt{35}}\begin{bmatrix}3\\1\\5 \end{bmatrix}$.

Note that 'magically' $\{\mathbf{u}_1,  \mathbf{u}_2\}$ is indeed an orthonormal set!

We have to extend this to an orthonormal basis of $\R^3$. For this low dimensional problem we can use the cross product!  
First we compute the orthogonal vector 
 $\quad \vect{w}_3  = \begin{bmatrix}11\\-8\\-5 \end{bmatrix} \times  \begin{bmatrix}3\\1\\5 \end{bmatrix} = \begin{bmatrix}-35\\-70\\35 \end{bmatrix} = 35 \begin{bmatrix}-1\\-2\\1 \end{bmatrix}$. <BR>
 Normalizing $\vect{w}_3$ gives the third basis vector $\vect{u}_3 =  \dfrac{1}{\sqrt{6}} \begin{bmatrix}-1\\-2\\1 \end{bmatrix}$.

Thus we end up with the matrix  $U = \begin{bmatrix}\frac{11}{\sqrt{210}}&\frac{3}{\sqrt{35}} &-\frac{1}{\sqrt{6}}\\ -\frac{8}{\sqrt{210}}&\frac{1}{\sqrt{35}} &-\frac{2}{\sqrt{6}}\\-\frac{5}{\sqrt{210}}&\frac{5}{\sqrt{35}} & \frac{1}{\sqrt{6}}\end{bmatrix}$.

::::

Along the way we came along some explicit and implicit properties of the matrix  $A^TA$.  We have collected them in the following proposition.


:::::{prf:proposition}  Properties of the matrix $A^TA$
:label: Prop:SVD:propertiesATA

Let $A$ be an $m\times n$ matrix with real entries. Then the following properties hold:

:::{latexlist}
:enumerated: true
:type: i

\item The matrices $AA^T$ and $A^TA$ are symmetric.
\item $\Nul{A} = \Nul{(A^TA)}$.
\item $\Rank{A} = \Rank{(A^TA)}$.
\label{Item:Prop:SVD:propertiesATA:samerankAandATA}
\item The eigenvalues of $A^TA$ are real and nonnegative.
\label{Item:Prop:SVD:propertiesATA:nonzeroeigvals}
\item The non-zero eigenvalues of $AA^T$ are the same as the non-zero eigenvalues of $A^TA$.  Moreover the algebraic and geometric multiplicities of these eigenvalues are the same. 
\label{Item:Prop:SVD:propertiesATA:sameeigvals}
:::


:::::

::::{dropdown} Proof of &nbsp;{prf:ref}`Prop:SVD:propertiesATA` 

:::{latexlist}
:enumerated: true
:type: i

\item Let's prove that $A^TA$ is symmetric. The proof for $AA^T$ is similar.

$$
 (A^TA)^T = A^T(A^T)^T = A^TA.
$$

\item Let $\mathbf{u} \in \Nul{A}$. Then,

$$
A^TA \mathbf{u} = A^T(A\mathbf{u}) = A^T\mathbf{0} = \mathbf{0}.
$$

So $\mathbf{u} \in \Nul{(A^TA)}$.

Conversely suppose that $\mathbf{v}\in \Nul{(A^TA)}$,  i.e., $A^TA\vect{v} = \vect{0}$.  Then, from the chain of identities

$$
0 = \mathbf{v}^T\vect{0} = \mathbf{v}^TA^TA\mathbf{v} = \norm{A\mathbf{v}}^2,
$$

it follows that  $\norm{A\mathbf{v}}=0$, implying $A\mathbf{v}=\mathbf{0}$.  So  $\mathbf{v}$ lies in $\Nul{A}$.

All in all we have shown that all vectors in $\Nul{A}$ lie in $\Nul{A^TA}$ and that all vectors in $\Nul{A^TA}$ lie in $\Nul{A}$.  Thus $\Nul{A}=\Nul{A^TA}$.

(Note that this was already mentioned in {numref}`Subsection %s <SubSec:LeastSquares:NormalEquations>`, 
equation {eq}`Eq:LeastSquares:InvertibilityATA`.)
\item Observe that since $A$ is an $m\times n$ matrix, we have that $A^TA$ is $n\times n$. Now, using {prf:ref}`Thm:BasisDim:RankThm` we have

$$
\Rank{A} = n - \dim{\Nul{A}} = n - \dim{\Nul{(A^TA)}} = \Rank{(A^TA)}.
$$

\item Since $A^TA$ is symmetric, the eigenvalues are real due to {prf:ref}`Prop:SymmetricMat:RealEigenvalues`. To see that they are non-negative, let $\mathbf{u}$ be an eigenvector of $A^TA$ with associated eigenvalue $\lambda$. Then,

$$0\le \norm{A\vect{u}}^2 = \mathbf{u}^TA^TA\mathbf{u} = \mathbf{u}^T\lambda \mathbf{u} = \lambda \norm{\mathbf{u}}^2.$$

Since $\mathbf{u}\ne \mathbf{0}$ it follows that $\lambda \ge 0$.

\item Let $\lambda$ be a non-zero eigenvalue of $A^TA$ with associated eigenvector $\mathbf{u}$. We will see that $\lambda$ is also an eigenvalue of $AA^T$. By definition of eigenvalue we have $A^TA\mathbf{u} = \lambda\mathbf{u}$. Then, multiplying by $A$ on both sides of the previous identity we obtain:

$$AA^TA\mathbf{u} = \lambda A\mathbf{u}.$$

Observe that if $A\mathbf{u}=\mathbf{0}$ then $A^TA\mathbf{u} = \mathbf{0}$ and $\lambda =0$, which contradicts the hypothesis of $\lambda \ne 0$. <BR>
Therefore, $A\mathbf{u}\ne \mathbf{0}$ and $A\mathbf{u}$ is an eigenvector of $AA^T$ with associated eigenvalue $\lambda$. 
To prove the converse, one can use a similar argument.


Now let's have a look at the multiplicities.   Since $A^TA$ is symmetric, hence diagonalizable, for each eigenvalue $\lambda$, the geometric and algebraic multiplicity are equal. And the same holds, of course, for the matrix $AA^T$.  So we are done if we can show that for each eigenvalue $\lambda_i \neq 0$,

$$
    \text{g.m.}_{A^TA}(\lambda_i) = \text{g.m.}_{AA^T}(\lambda_i) 
$$

Suppose   $\{\mathbf{v}_1, \dots , \mathbf{v}_g\}$   is a maximal set of linearly
independent eigenvectors of $A^TA$  for some eigenvalue $\lambda_i \neq 0$.  The above argument shows that  $A\mathbf{v}_1, \dots , A\mathbf{v}_g$  are eigenvectors for $A^TA$.
To show that they are linearly independent,  suppose that

$$
  c_1A\mathbf{v}_1+ \cdots + c_gA\mathbf{v}_g = \mathbf{0}.
$$

Then

$$
   \begin{array}{rcl}A^T(c_1A\mathbf{v}_1+ \cdots + c_gA\mathbf{v}_g) &=& 
  c_1A^TA\mathbf{v}_1+ \cdots + c_gA^TA\mathbf{v}_g\\
  &=&
  \lambda_i(c_1\mathbf{v}_1+ \cdots + c_g\mathbf{v}_g) =  \mathbf{0}
  \end{array}
$$

as well.  As $\lambda_i$ was suppose to be unequal to zero, and the vectors $\mathbf{v}_k$ linearly independent,  it follows that 

$$
 c_1 = c_2   = \cdots = c_g =  0,
$$

which shows that the vectors $A\mathbf{v}_1, \ldots, A\mathbf{v}_g$ are $g$ *linearly independent* eigenvectors  (of $AA^T$).  So the geometric multiplicity $g_2$ of $\lambda_i$ for $AA^T$
is at least as large as the geometric multiplicity $g$ of $\lambda_i$ for $A^TA$.
Again, by the inherent symmetry the argument can be reversed, and we find that the geometric multiplicity of $\lambda_i$  is the same for $A^TA$ as for $AA^T$. 
:::

::::

We want to stress  the importance of property {itemref}`Item:Prop:SVD:propertiesATA:nonzeroeigvals`. We know from {numref}`Sec:SymmetricMat` that the eigenvalues of a symmetric matrix are real. The previous proposition tells us that, in addition, **the eigenvalues of the symmetric matrix $A^TA$ are non-negative**. This property is the key for the singular value decomposition.


::::{prf:theorem}  Existence of a singular value decomposition
:label:  Thm:SVD:Existence

For every $m \times n$ matrix $A$  a singular value decomposition exists

::::

The proof consists in showing that all steps in the algorithm do what they are supposed to do, and that the final result consists of three matrices  $U, \Sigma, V$ that can act as a 
singular value decomposition of $A$.  

::::{dropdown} Proof of&nbsp;{prf:ref}`Thm:SVD:Existence`

Let us first consider the six steps of the algorithm.

Step 1. Offers no difficulties.

Step 2. Here we must check that the eigenvalues of the matrix $A^TA$ are *nonnegative*. This is exactly the content of  {prf:ref}`Prop:SVD:propertiesATA` {itemref}`Item:Prop:SVD:propertiesATA:nonzeroeigvals` 

Step 3. Offers no difficulties.

Step 4. Since $A^TA$ is symmetric, an orthonormal basis of eigenvectors exists.

Step 5. Here we have to show that the vectors  $A\vect{v}_1, \ldots, A\vect{v}_r$, corresponding to the nonzero eigenvalues of $A^TA$ are *orthogonal*.  (We called  this 'magical' in {prf:ref}`Ex:SVD:ComputeAnSVD1`). 
Well,  just consider the inner products!  For  $i \neq j$ we have

$$
  A\vect{v}_i\ip A\vect{v}_j = (A\vect{v}_i)^TA\vect{v}_j = \vect{v}_i^T A^TA \vect{v}_j = \vect{v}_i \ip  (\lambda_j\vect{v}_j) = \lambda_j \vect{v}_i \ip \vect{v}_j = 0,
$$

since  the vectors $\vect{v}_1, \ldots, \vect{v}_n$ are orthogonal. <BR>
Thus the vectors $\vect{u}_1, \ldots, \vect{u}_r$  are orthogonal to start with.
Finding their norms, noting that the vectors $\vect{v}_i$ already have unit length, and that $A^TA\vect{v}_i = \lambda_i \vect{v}_i$ we see that,  for $1 \leq i \leq r$,

$$
 \norm{\vect{u}_i}^2 = \left(\frac{1}{\sigma_i} A\vect{v}_i \right) \ip \left(\frac{1}{\sigma_i} A\vect{v}_i\right) = \frac{1}{\sigma_i^2} \vect{v}_i^T A^TA \vect{v}_i =
 \frac{1}{\sigma_i^2} \lambda_i \vect{v}_i^T \vect{v}_i = 1.
$$

To turn the orthonormal set  $\vect{u}_1, \ldots, \vect{u}_r$ into an orthonormal basis 
$\vect{u}_1, \ldots, \vect{u}_m$  of $\R^m$ , we can use techniques from {numref}`Sec:BasisDim`  (especially  {prf:ref}`Prop:BasisDim:Thinning`) and {numref}`Sec:Gram-Schmidt`.  Keep adding linearly independent vectors until the whole of $\R^m$ is spanned, and then orthogonalize using the Gram-Schmidt process.

This leaves us with

Step 6,   which is no big deal.


To conclude we have to show that for the matrices found indeed we have

$$
   A = U\Sigma V^T.
$$

By construction we have that  $A\vect{v}_i = \sigma_i \vect{u}_i$,  $i = 1, \ldots, r$,  which can be written in matrix form as  

$$
  AV_r = U_r\Sigma_{rr}, 
$$

where we introduced   $U_r, V_r$  for the matrices with only the first $r$ columns of $U$ and $V$, and $\Sigma_{rr}$ the  $r\times r$ diagonalmatrix with $\sigma_1, \ldots, \sigma_r$,  in that order, on the diagonal.

If $r<n$, which means that there are singular values equal to $0$  (equivalently, $\Rank{A} < n$ ), we can add the columns  $\vect{v}_{r+1}, \ldots, \vect{v}_n$ to $V_r$, and add $n-r$ zero columns to $\Sigma_{rr}$.  We denote the extended last matrix by $\Sigma_r$.
We thus arrive at

$$
   AV = U_r\Sigma_r.
$$

Next we add the remaining columns (if any)   $\vect{u}_{r+1}, \ldots, \vect{u}_{m}$ to $U_r$, and add $m-r$ zero rows to the bottom of $\tilde{\Sigma}_r$.  Thus we have built the matrix  $\Sigma$ exactly as in the algorithm (Step 3).  Moreover,   $U_r\tilde{\Sigma}_r = U\Sigma$, so we see that

$$
  AV = U_r\Sigma_r = U\Sigma.
$$

Multiplying both terms from the right by  $V^T$,  keeping in mind that  $V$ is an orthogonal matrix, we arrive at our final destination.  From  $U\Sigma = AV $ it follows that

$$
    U\Sigma V^T = A V V^T  = A.
$$
::::


Some concluding remarks concerning the algorithm.

::::{prf:remark}
:label: Rem:SVD:PracticalHints

 1. Because of the basic property that says that transposing an SVD of an $m \times n$ matrix $A$ gives an SVD  of $A^T$
 ({prf:ref}`Prop:SVD:BasicProp` {itemref}`Item:Prop:SVD:BasicProp:Transpose`)
 it may be profitable to  find an SVD for $A^T$ first, and then transpose this. <BR>
 The singular values of $A$ are the eigenvalues of $A^TA$, an $n \times n$ matrix, the singular values of $A^T$ are the eigenvalues of $AA^T$, an
 $m \times m$ matrix.  The smaller the better! <BR>
 In most applications the singular value decomposition will be applied to  $m\times n$ matrices $A$  with much more rows that columns,  so  $m \gg n$. For such  matrix $A$ 
 working with $A^TA$ is the best bet.

 2. The normalization of the vectors  $\mathbf{v}_i$ and $\mathbf{u}_j$ may be postponed till the end of step 5.  That prevents dragging along
 the obnoxious square root denominators.

::::

To illustrate {prf:ref}`Rem:SVD:PracticalHints` and to conclude this subsection let us consider a second example.

::::{prf:example}
:label:  Ex:SVD:ComputeAnSVD2

We will find a singular value decomposition of the matrix
$
A = \begin{bmatrix}
1 & 1 & 0 &-1\\
-1 & 1 & 0&3\\
-2 & 1 & 2&0
\end{bmatrix}
$.

Following the suggestion of the remark we first construct an SVD of the matrix
$B = A^T = \begin{bmatrix}
1 & -1 &-2 \\
1 & 1 &1 \\
0 & 0 & 2 \\
-1 & 3 & 0
\end{bmatrix}$.

We will pass along all steps of {prf:ref}`Alg:SVD:SVDalgorithm`.

Step 1.  $B^TB = AA^T = \begin{bmatrix}
3 & -3 & -1\\
-3 &11 &3 \\
-1 & 3 & 9
\end{bmatrix}$.  This is straightforward.


Step 2.  Computing the characteristic polynomial is already quite a task here, but it is doable.  The result: 

$$
\det(B^TB - \lambda \mathrm{I}) = \lambda^3 -23\lambda^2 +140 \lambda -196.
$$

Without a computer we would be stuck. How to find the zeros of this polynomial? However, we have come up with a *very*  special matrix $A$ here,
for which the squares of all the singular values are  *integers*. (So in that sense, this is not a very representative example, and in general the
computations will be even worse, not to say impossible.)  Here, the eigenvalues of $B^TB$ are given by  $\lambda_1 = 14, \lambda_2 = 7,
\lambda_3 = 2$.  Which finishes step 2.

Step 3  is straightforward:  $\Sigma = \begin{bmatrix}
\sqrt{14} & 0 & 0 \\
0 & \sqrt{7} & 0 \\
0 & 0 & \sqrt{2} \\
0 & 0 & 0
\end{bmatrix}$.

Step 4. With some effort we can find eigenvectors: <BR>
$\vect{v}_1 = \begin{bmatrix} 1 \\ -3 \\ -2 \end{bmatrix}$, for $\lambda_1 = 14$,
  $\vect{v}_2 = \begin{bmatrix} 1 \\ -3 \\ 5 \end{bmatrix}$, for $\lambda_2 = 7$, and
$\vect{v}_3 = \begin{bmatrix} 3 \\ 1 \\ 0 \end{bmatrix}$, for $\lambda_3 = 2$. <BR>
Note that these are indeed three orthogonal vectors, which
we do not immediately normalize!

Step 5.  Next we compute the vectors $\vect{u}_i$, again without normalizing, and also for the moment not taking the (ugly!) factors
$\frac{1}{\sigma_i} $ into account. Since the singular values are nonzero, we use all three vectors $\vect{v}_i$: <BR>
This gives 

$$ \mathbf{u}_1 = B\mathbf{v}_1 = \begin{bmatrix} 8 \\ -4 \\ -4 \\ -10 \end{bmatrix}, \quad \mathbf{u}_2 = B\mathbf{v}_2 =
\begin{bmatrix}-6 \\ 3 \\ 10 \\ -10 \end{bmatrix}, \quad \mathbf{u}_3 = B\mathbf{v}_3 = \begin{bmatrix} 2 \\ 4 \\ 0 \\ 0 \end{bmatrix}. 
$$
It should not come as a surprise that these vectors are orthogonal! <BR>
We have to find a fourth orthogonal vector $\vect{u}_4$.   One way is to look for a nonzero vector in the nulspace of the matrix $\begin{bmatrix}
8 & -4 & -4 &-10 \\ -6 & 3 & 10 & -10 \\ 2 & 4 & 0 & 0\end{bmatrix}$. <BR>
 You may check that the vector $\vect{u}_4 = \begin{bmatrix} 4 \\ -2 \\ 5 \\ 2 \end{bmatrix}$  does the trick.

Step 6.  (Where we also still have to present our $V$.)  <BR>
We rescale all vectors to unit vectors and put them side by side, to arrive at the matrices

$$
   V = \begin{bmatrix} \frac{1}{\sqrt{14}} &\frac{1}{\sqrt{35}} &  \frac{3}{\sqrt{10}} \\ -\frac{3}{\sqrt{14}}  & -\frac{3}{\sqrt{35}}
   &\frac{1}{\sqrt{10}} \\ -\frac{2}{\sqrt{14}} & \frac{5}{\sqrt{35}} & 0 \end{bmatrix}, \quad
   U = \begin{bmatrix}
            \frac{4}{7}  & -\frac{6}{\sqrt{245}} & \frac{1}{\sqrt{5}} & \frac{4}{7}\\
            -\frac{2}{7} & \frac{3}{\sqrt{245}}  & \frac{2}{\sqrt{5}}& -\frac{2}{7}\\
            -\frac{2}{7} & \frac{10}{\sqrt{245}} &   0        &\frac{5}{7} \\
            -\frac{5}{7} & -\frac{10}{\sqrt{245}}&   0        & \frac{2}{7}\\
       \end{bmatrix}.
$$

And then we must not forget that we have just constructed an SVD for $A^T$ instead of $A$!

From  $A^T = U\Sigma V^T$  it follows swiftly that  $A = V \Sigma^TU^T$ is an SVD for $A$.

::::


(Subsec:SVDGeometrically)=

## Understanding the SVD Geometrically

In this section we will have a deeper look at the decomposition and its meaning. As we have done previously, we can think about an $m\times n$ matrix $A$ as the standard matrix of a linear transformation from $\R^n$ to $\R^m$.

By definition, the matrices $U$ and $V$ in the SVD of an $m\times n$ matrix $A$ 
are orthogonal matrices. Thus the columns of $U$ give an orthonormal basis of $\R^m$,  the columns of $V$ an orthonormal basis of $\R^n$. The decomposition $U\Sigma V^T$ then becomes a composition of transformations. We can visualise this using the graph in {numref}`Figure %s <Fig:SVD:decomposition>`:

:::{figure} Images/Fig-SVD-Decomposition.svg
:width: 300px
:name: Fig:SVD:decomposition

Diagram showing the SVD as a composition of linear transformations.

::::


Let us first consider the case where $A$ is a  $2 \times 2$ matrix, as in that case everything takes place in the plane, and we can make an exact drawing of what is going on. 
Every  $2\times 2$  orthogonal matric has one of the two forms

$$
   \begin{bmatrix} \cos({\varphi})&-\sin({\varphi}) \\
   \sin({\varphi}) &  \cos({\varphi})\end{bmatrix}, \quad \quad
   \begin{bmatrix} \cos({\varphi})&\sin({\varphi}) \\
   -\sin({\varphi}) &  \cos({\varphi})\end{bmatrix}.
$$

The first matrix represents a rotation, the second matrix represents a reflection.  In an SVD of $A$, we can always construct $V$ to be a rotation.  Namely, the columns of $V$ must be eigenvectors of the matrix $A^TA$, and eigenvectors remain eigenvectors if one multiplies  them with a factor $(-1)$.
In that case  $V^T$, which is just $V^{-1}$, is also a rotation.
Since the matrix $U$ in general is uniquely determined once $V$ is chosen (the exception being the case where $A$ has  zero as a singular value),  $U$ is either a rotation (when det$(A)>0$) or a reflection  (when det$(A)<0$). 
The workings of the concatenation  $U\Sigma V^T$ are then
1. Multiplication by $V^T$ rotates the eigenvectors $\mathbf{v}_1$ and  $\mathbf{v}_2$   of  $A^TA$
    to the standard basis vectors $\mathbf{e}_1$ and  $\mathbf{e}_2$.
2. Multiplication by $\Sigma$ stretches the basic vectors $\mathbf{e}_1$ and  $\mathbf{e}_2$ with factors $\sigma_1$ and $\sigma_2$.
3. Multiplication by $U$ rotates or reflects the  vectors $\sigma_1\mathbf{e}_1$ and  $\sigma_2\mathbf{e}_2$ to the vectors
$\sigma_1\mathbf{u}_1$ and  $\sigma_2\mathbf{u}_2$. 

If we consider the total effect on the unit circle (i.e., all vectors of length 1), then
1. is a rotation of the circle,  
2. shrinks or stretches the unit circle to an ellipse,  and 
3. rotates or reflects this ellipse.

Let us consider a numerical example.



::::{prf:example}
:label: Ex:SVD:GeometricView

We will analyze the SVD of the matrix
  $A = \dfrac{1}{\sqrt{5}}\begin{bmatrix} 5 & 2 \\ 0 & 6 \end{bmatrix}$.

The matrix  

$$
 A^TA =  \begin{bmatrix} 5 & 2 \\ 2 & 8 \end{bmatrix} 
$$

has the eigenvalues

$$
  \lambda_1 = 9, \quad \lambda_2 = 4,
$$

with corresponding eigenvectors

$$
  \mathbf{v}_1 = \begin{bmatrix} 1  \\ 2 \end{bmatrix}, \quad \mathbf{v}_2 = \begin{bmatrix} 2  \\ -1 \end{bmatrix}.
$$

Normalizing them, and giving the second vector a minus sign,
we find for an SVD

$$
 V = \dfrac{1}{\sqrt{5}} \begin{bmatrix} 1 & -2 \\ 2 & 1 \end{bmatrix}, \quad \Sigma = \begin{bmatrix} 3 & 0\\0 & 2 \end{bmatrix}.
$$

Applying  the last two steps of {prf:ref}`Alg:SVD:SVDalgorithm` we find that

$$
   U = \dfrac{1}{5} \begin{bmatrix} 3 & -4 \\ 4 & 3 \end{bmatrix}.
$$

So,  $V$ represents a rotation about an angle  $\varphi = \arccos\left(\frac{1}{\sqrt{5}}\right) \approx 63^{o}$, and 
$U$ represents a rotation about an angle  $\psi = \arccos\left(\frac{3}{5}\right) \approx 53^{o}$.  Between those two rotations,  $\Sigma$  'stretches' vectors with a factor $3\sqrt{5}$ in the $x$-direction and a factor $2\sqrt{5}$ in the $y$-direction.

Note that  $V$ maps $\vect{e}_1,\vect{e}_2$  to  $\vect{v}_1,\vect{v}_2$, &nbsp;  so  $V^T = V^{-1}$ maps $\vect{v}_1,\vect{v}_2$  to  $\vect{e}_1,\vect{e}_2$.

{numref}`Figure %s <Fig:SVD:GeometricView>` visualizes what is going on.  Note that at the end the vector $\vect{e}_1$  comes to rest on the $x$-axis,  as it should, since

$$
   A\vect{e}_1 \,=\, \dfrac{1}{\sqrt{5}}\begin{bmatrix} 5 & 2 \\ 0 & 6 \end{bmatrix}\begin{bmatrix} 1\\ 0 \end{bmatrix} \,=\, \begin{bmatrix} \sqrt{5}\\ 0 \end{bmatrix}.
$$

:::{figure} Images/Fig-SVD-GeometricView.svg
:name: Fig:SVD:GeometricView

Geometric decomposition of $A = \dfrac{1}{\sqrt{5}}\begin{bmatrix} 5 & 2 \\ 0 & 6 \end{bmatrix}$ 
:::

::::

In general, for an $m\times n$ matrix $A$ of say rank $r$, suppose

$$
   A = U\Sigma V^T
$$

is a singular value decomposition.
Since $V^T$ is an orthogonal matrix, it will map the $\mathbb{R}^n$ to itself and it will preserve the norms of all vectors. 
More precisely, it will map the 'principal axes' corresponding to  $\vect{v}_1,\ldots,\vect{v}_n$  onto the coordinate axes generated by  $\vect{e}_1, \ldots, \vect{e}_n$. With that, the $n$-dimensional unit sphere, consisting of all vectors of norm 1, is mapped onto itself.

The $m \times n$ matrix $\Sigma$ maps the first $r$ basis vectors 
$\vect{e}_1, \ldots, \vect{e}_r$ in $\R^n$ to the vectors 
$\sigma_1\vect{e}_1, \ldots, \sigma_r\vect{e}_r$ in $\R^m$.  The remaining (if any) basis vectors $\vect{e}_{r+1}, \ldots, \vect{e}_n$
are mapped to $\vect{0}\in \R^{m}$.  All in all, $\Sigma$ maps the unit sphere in $\R^n$ onto an $r$-dimensional 'ellipsoid' in $\R^m$.

Lastly the orthogonal matrix $U$ rotates/reflects this ellipsoid
in $\R^m$.

<BR>


## Applications of the SVD

There will be two applications described in this section.

1.  Data compression

2.  Linear Least Squares.


We start with the first.  
Numerical data can be stored in a matrix.
A black-and-white picture/photo can be stored 'pixel by pixel', by numbers that indicate the gray scale, which may for instance be any integer from 0 (completely white) to 31 (completely black). A 9:16 photo may then be stored as a 1080x1350 matrix.


The results of some survey with $n$ question that had to be answered using a 1-5 scale.  If the numbers of respondents is $N$, the data correspond to a $N \times n$ matrix.

In the first situation there will be both a high correlation between columns that are close to each other, as well as between nearby rows.  If the picture is a true photo the matrix will be far from a 'random' matrix.
In the second context  one might expect that the columns will highly correlate:  people that agree on certain issues are more likely to agree on other issues as well.  

The main features of the data may be filtered out by analyzing an SVD of the matrix at hand.

The basic idea comes from the 'spectral decomposition' as in the last observation of {prf:ref}`Ex:SVD:firstSVD`.  Suppose $A$ is a matrix of  rank $r$,  with nonzero singular values  $\sigma_1 \geq \sigma_2 \geq \ldots \geq \sigma_r > 0$.  Furthermore, let  $U\Sigma V^T$  be a singular value decomposition of the matrix $A$. Let 

$$
  \Delta = \begin{bmatrix} \sigma_1 &   0   &  0   & \cdots & 0 \\ 
                              0 & \sigma_2  &  0   & \cdots & 0 \\
                              0 &  0  & \sigma_3 & \cdots   & 0 \\
                              \vdots & \vdots &  & \ddots &\vdots \\
                              0  & 0  & 0 & \ldots & \sigma_r 
           \end{bmatrix}.   
$$

So $\Delta$ is the diagonal matrix that remains if all the zero rows and zero columns (if any) of $\Sigma$ are removed. If $U_r$  and  $V_r$  is the matrix with the first $r$ colums of $U$, and  $V_r$  is the matrix with the first $r$ colums of $V$, then as in {prf:ref}`Ex:SVD:firstSVD`  we have that

$$
  A = U\Sigma V^T = U_r\Delta V_r
$$

which can be rewritten as

::::{math}
:label: Eq:SVD:SpectralDecompAlg

   A = \sigma_1 \vect{u}_1\vect{v}_1^T + \sigma_2 \vect{u}_2\vect{v}_2^T + \cdots +
   \sigma_r \vect{u}_r\vect{v}_r^TA.

::::

Here $A$ is written as a sum of rank 1 matrices, and because of the decreasing singular values, these rank 1 matrices get less and less 'important'.  If the $\sigma_i$ become very small for, say, $k < i \leq r$,  we might expect that the sum

$$
\sigma_1 \vect{u}_1\vect{v}_1^T + \ldots + \sigma_k \vect{u}_k\vect{v}_k^T 
$$

of the first $k$ terms gives a good approximation of the matrix $A$.

The gain is this:  if the data is put in the form of an $m \times n$ matrix $A$,  
then it needs $m \times n$ memory cells to store $A$.  If $k$  is much smaller than $r = $ rank $A$
(which in general will be equal to the smallest of $m$ and $n$),  then $U_k$,  $V_k$  and the $k$ largest singular values only take up $m\times k + n\times k + k  = (m+n+k)k$,  memory cells. <BR>
If, for instance, a 1080x1350 ( $\approx$ 1.45 MB) image is stored using the thirty per cent highest singular values,  the storage space reduces to  324x(1080+1350+320) $\approx$ 7.78 MB.  So the  *data* as been *compressed' by more or less a factor 0.54.

In general, the higher the correlation/dependency between the columns (or, for that matter, the rows) of a matrix $A$, the fewer singular values are needed for a good approximation of $A$.

## Grasple Exercises


::::{grasple}
:url: https://embed.grasple.com/exercises/27adae2a-db2a-46fa-800f-49e4c0dfe4fa?id=93487
:label: grasple_exercise_8_3_9
:dropdown:
:description: If $A = U\Sigma V^T$   for an  mxn matrix $A$, what are the sizes of  $U$, $Σ$ and $V$?
::::


::::{grasple}
:url: https://embed.grasple.com/exercises/caac29d1-9700-4a30-8c7c-19ea6148258f?id=93490
:label: grasple_exercise_8_3_10
:dropdown:
:description: To describe the meaning of the singular values of a matrix.
::::



::::{grasple}
:url: https://embed.grasple.com/exercises/e4c651aa-a998-4e19-957b-20ddf41509bf?id=93468
:label: grasple_exercise_8_3_2
:dropdown:
:description: To find the singular values of a 2x2 matrix $A$
::::

::::{grasple}
:url: https://embed.grasple.com/exercises/47ebaa77-9f3c-4363-a57e-d37242c6e598?id=93471
:label: grasple_exercise_8_3_3
:dropdown:
:description: To compute the singular values of a 3x2 matrix $A$.
::::

::::{grasple}
:url: https://embed.grasple.com/exercises/79d22478-56e3-49ee-9b19-77ab1ad06eaf?id=93470
:label: grasple_exercise_8_3_4
:dropdown:
:description:  To compute an SVD for a 2x3 matrix $A$. 
::::



::::{grasple}
:url: https://embed.grasple.com/exercises/10affbae-4221-40f8-bf0e-df626a0e64ae?id=93479
:label: grasple_exercise_8_3_5
:dropdown:
:description: To compute an SVD for a 2x3 matrix $A$ (of rank 1).
::::


::::{grasple}
:url: https://embed.grasple.com/exercises/37ea17f1-1bfb-4a19-b9e2-1292a593dfa3?id=93480
:label: grasple_exercise_8_3_6
:dropdown:
:description: To compute an SVD for a 3x2 matrix $A$ (of rank 1).
::::


::::{grasple}
:url: https://embed.grasple.com/exercises/20dd219a-35f3-48d7-ad9d-35038047336b?id=92586
:label: grasple_exercise_8_3_7
:dropdown:
:description: To compute an SVD for a matrix $A$ with orthogonal columns.
::::


::::{grasple}
:url: https://embed.grasple.com/exercises/9848d7be-1530-46b0-941f-9ae76e95abfa?id=93481
:label: grasple_exercise_8_3_8
:dropdown:
:description: To draw conclusion(s) about $A$ from a given SVD of $A$.
::::


::::{grasple}
:url: https://embed.grasple.com/exercises/3fdad317-fc18-4f88-b416-87cbd1d5e708?id=93495
:label: grasple_exercise_8_3_1
:dropdown:
:description: Finding maximal value of $\norm{A\vect{x}}$, if $\norm{\vect{x}}$ ,  $A$ a 3x2 matrix.
::::

