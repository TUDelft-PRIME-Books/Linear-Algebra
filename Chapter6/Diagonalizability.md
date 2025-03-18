(Sec:Diagonalize)=

# Diagonalizability

(Subsec:SimilarMatrices)=

## Similar matrices

::::::{prf:definition}
:label: Dfn:Diagonalizable:SimalarMatrices

Two $n \times n$ matrices $A$ and $B$ are called **similar** if they are related via the property

$$
B = PAP^{-1} \quad \text{for some invertible matrix  } P.
$$

Notation: $A \sim B$.

::::::

It is true we already used the symbol $\sim$ earlier to denote row equivalence of (augmented) matrices. When we use it, it will always be clear from the context what  the meaning is at that instance.

::::::{prf:remark}

In the definition it seems as if $A$ and $B$ play  different roles, but that is not the case. This can be seen as follows:

$$
A \sim B  \quad \iff \quad B = PAP^{-1}
\quad \iff \quad  P^{-1}BP =  P^{-1}(PAP^{-1})P = A.
$$

Since $(P^{-1})^{-1} = P$, we see that

$$
B = PAP^{-1} \quad \iff \quad A =  QBQ^{-1}, \quad \text{where  } Q = P^{-1},
$$

so similarity works both ways, that is,

$$
A \sim B  \quad \iff \quad   B \sim A.
$$

::::::

Similar matrices have similar properties. Especially as regards eigenvalues and eigenvectors.

::::::{prf:proposition}
:label: Prop:Diagonalizable:SimilarEigenvalues

If $A = PBP^{-1}$, then $A$ and $B$ have the same eigenvalues.

Moreover, if $\vect{v}$ is an eigenvector of $B$, then $P\vect{v}$ is an eigenvector of $A$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:Diagonalizable:SimilarEigenvalues`
:class: tudproof

Suppose $\lambda$ is an eigenvalue of $B$, and $\vect{v}$ is a corresponding eigenvector. We then see that

$$
B\vect{v}= \lambda\vect{v}  \quad \Longrightarrow \quad
AP\vect{v} = (PBP^{-1})P\vect{v} = PB\vect{v} =
P(\lambda\vect{v}) =  \lambda P\vect{v}
$$

So $AP\vect{v} = \lambda P\vect{v} $, and $P\vect{v} $  is an eigenvector, provided it is not the zero vector.
Since $P$ is supposed to be invertible, and $\vect{v}$ is not the zero vector, it is true that
$P\vect{v} $ is not the zero vector, and we are done.

::::::

::::::{prf:proposition}
:label: Prop:Diagonalizable:SimilarCharpoly

Similar matrices have the same characteristic polynomial.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:Diagonalizable:SimilarCharpoly`
:class: tudproof

Suppose $A = PBP^{-1}$.

Then we have

$$
\det{(A - \lambda I)} = \det{(PBP^{-1} - \lambda I)} = \det{(B - \lambda I)}.
$$

The second equality is proved by the following chain of identities.

$$
\begin{array}{rcl}
\det{(PBP^{-1} - \lambda I)} &=& \det{(PBP^{-1} - \lambda PIP^{-1})} \\
& = & \det{(P(B- \lambda I)P^{-1})} \\
& = &  \det{P}\cdot\det{(B- \lambda I)}\cdot\det{(P^{-1})} \\
& = &  \det{P}\cdot\det{(B- \lambda I)}\cdot\dfrac{1}{\det{P}} \\
& = &  \det{(B- \lambda I)}.
\end{array}
$$

In fact, the first step contains the 'smart move', to bring in convenient factors $P$ and $P^{-1}$ via

$$
I = PIP^{-1}.
$$

In the other steps we used the rule $\det{(AB)} = \det{A}\det{B}$ and its consequence that for invertible matrices $P$ we have

$$
   \det{(P^{-1})} = \dfrac{1}{\det{P}}.
$$

::::::

From {prf:ref}`Prop:Diagonalizable:SimilarCharpoly` it follows that similar matrices have the same eigenvalues with the same algebraic multiplicities.

From {prf:ref}`Prop:Diagonalizable:SimilarEigenvalues` it follows that they also have the same geometric multiplicities. That is,
if $\vect{v}_1, \ldots, \vect{v}_m$ are linearly independent eigenvectors of $B$ for the eigenvalue $\lambda_k$, and $A = PBP^{-1}$,
then the vectors $P\vect{v}_1, \ldots, P\vect{v}_m$ are linearly independent eigenvectors of $A$.
<BR>
And vice versa.

::::::{exercise}
:label: Exc:Diagonalizable:GeomMultForSimilarMatrices

Fill in the details of the last remark.

::::::

The above considerations are summarized in the following proposition.

::::::{prf:proposition}
:label: Prop:Diagonalizable:EqualMultiplicitiesSimilarMatrices

Suppose  $A$ and $B$ are similar matrices.  Then they have the same eigenvalues with the same algebraic and geometric multiplicities.

::::::



Using the properties of similar matrices we can prove the inequality

::::::{math}
:label: Eq:Diagonalizable:GeomMultversusAlgMult

\text{g.m.}(\lambda) \leq \text{a.m.}(\lambda) 
::::::

that holds for the geometric and the algebraic multiplicity of an eigenvalue 
 (cf. {prf:ref}`Prop:EigenValues:SmallerGeomMultiplicity`).

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:EigenValues:SmallerGeomMultiplicity` &nbsp;  (geom.mult. $\leq$ alg.mult.)
:class: tudproof, dropdown

Suppose the $n\times n$ matrix $A$ has the eigenvalue $\lambda_1$ of geometric multiplicity $k$.  We have to show that the algebraic multiplicity of $\lambda_1$ is *at least* equal to $k$. We will do so by constructing a matrix $B$ that is similar to $A$ and for which the eigenvalue $\lambda_1$ will clearly have algebraic multiplicity at least equal to $k$. <BR>
Suppose $\vect{v}_1,\ldots,\vect{v}_k$ are $k$ linearly independent eigenvectors for $\lambda_1$.  We can extend $\{\vect{v}_1,\ldots,\vect{v}_k,\}$ to a basis $\{\vect{v}_1,\ldots,\vect{v}_k, \ldots, \mathbf{v}_n \}$   of $\mathbb{R}^n$.
Let $P$ be the matrix with  $\vect{v}_1,\ldots,\vect{v}_n$ as columns.  $P$ is invertible, and we have that

$$
\begin{array}{ccl}
AP &=&  A [\vect{v}_1\,\, \ldots \,\, \vect{v}_k\,\, \vect{v}_{k+1}\,\,\ldots \,\, \mathbf{v}_n] \\
   &=&  [A\vect{v}_1\,\, \ldots \,\, A\vect{v}_k\,\, A\vect{v}_{k+1}\,\,\ldots \,\, A\mathbf{v}_n] \\
   &=&  [\lambda_1\vect{v}_1\,\, \ldots \,\, \lambda_1\vect{v}_k\,\,A\vect{v}_{k+1}\,\, \ldots \,\, A\mathbf{v}_n],
\end{array}
$$

since  $\vect{v}_1, \ldots, \vect{v}_k$ were supposed to be eigenvectors for $\lambda_1$.
<BR>
Since $P$ is invertible, for each $j \geq k+1$ the equation $P\vect{x} = A\vect{v}_{j}$ has the (unique) solution,  $\vect{b}_j = P^{-1}A\vect{v}_{j}$.  So we see that

$$
\begin{array}{l}
  [\lambda_1\vect{v}_1\,\, \ldots \,\, \lambda_1\vect{v}_k\,\,\,A\vect{v}_{k+1}\,\, \ldots \,\, A\mathbf{v}_n] \\
  \quad = \quad [P(\lambda_1\vect{e}_1) ,\, \ldots \,\,P(\lambda_1\vect{e}_k)\,\,\,P\vect{b}_{k+1}\,\, \ldots \,\,P\vect{b}_{n}] \\
  \quad = \quad P[\lambda_1\vect{e}_1 ,\, \ldots \,\,\lambda_1\vect{e}_k\,\,\,\vect{b}_{k+1}\,\, \ldots \,\,\vect{b}_{n}] = P B.
\end{array}  
$$ 

So we have that  $A = PBP^{-1}$, which means that $A$ and $B$ are similar, hence they have the same eigenvalues with the same algebraic (and also geometric) multiplicities.

Note that $B$ is of the form

$$

  B \,=\,\, \begin{bmatrix} 
                        \lambda_1 & 0 & \ldots & 0 & * & * & \ldots & * \\
                        0 & \lambda_1 & \ldots & 0 & * & * & \ldots & * \\
                        \vdots & \vdots & \ddots & \vdots &  * & * & \ldots & * \\
                        0 & 0 & \ldots & \lambda_1 &   * & * & \ldots & * \\
                        \vdots & \vdots &  & \vdots & \vdots &  \vdots &  \vdots &  \vdots  \\
                        \vdots & \vdots &  & \vdots & \vdots &  \vdots &  \vdots &  \vdots  \\
                        0 & 0 & \ldots & 0 &   * & * & \ldots & * \\
                     \end{bmatrix},
$$

where there are $k$ entries $\lambda_1$ on the diagonal. <BR>
It follows that the characteristic polynomial  det$(B - \lambda \mathrm I)$  will have *at least*  $k$ factors $(\lambda - \lambda_1)$.
Thus the algebraic multiplicity of the eigenvalue $\lambda_1$ for the matrix $B$ is greater than or equal to $k$.  From the observed similarity  $A \sim B$ it follows that this also holds for the algebraic multiplicity of $\lambda_1$ for the matrix $A$.
So indeed the inequality

$$
   \text{a.m.}(\lambda_1) \geq  \text{g.m.}(\lambda_1)
$$

is universally true.

::::::


One way to understand the similarity of similar matrices comes from considering the linear transformations they represent.
In {numref}`Section %s <Subsec:ChangeOfBasis:RelationTETB>` it is shown that if $T:\R^n\to\R^n$ is the linear transformation that has $A$ as its standard matrix, and $P = P_{\mathcal{B}}$ is the change-of-coordinates matrix from the basis $\mathcal{B}$ to the standard matrix, then the matrix of $T$ with respect to basis $\mathcal{B}$ is given by

$$
[T]_{\mathcal{B}} = P^{-1}AP.
$$

This means that if $A$ and $B$ are related via

$$
B = PAP^{-1}
$$

then $A$ and $B$ are in fact matrices of the same linear transformation, only with respect to different bases. The fact that - for one thing - they share the same eigenvalues is then not very surprising.

The following proposition captures some other properties that similar matrices share.

::::::{prf:proposition}
:label: Prop:Eigenvalues:SimilarMatrices

Suppose $A$ and $B$ are similar matrices. Then the following statements are true.

<ol type = "i">
<li>

$\det{A} = \det{B}$.

</li>
<li>

If $A$ is invertible, then $B$ is invertible (and vice versa).

</li>
<li>

$A$ and $B$ have the same rank.

</li>
</ol>

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:Eigenvalues:SimilarMatrices`
:class: tudproof, dropdown

Suppose $A = PBP^{-1}$.

<ol type = "i">
<li>

As in the proof of the equality of the characteristic polynomials ({prf:ref}`Prop:Diagonalizable:SimilarCharpoly`) we have:

<BR>

if $A = PBP^{-1}$,
then

<BR>

$$
\det{A} = \det{(PBP^{-1})}  = \det{P}\det{B}\det{(P^{-1})},
$$

which can be rewritten as follows

<BR>

$$
\det{P}\det{B}\det{(P^{-1})} = \det{P}\det{B}(\det{P})^{-1} = \det{B}.
$$

</li>
<li>

Follows immediately from i.:

matrix $A$ is invertible $\quad \iff \quad \det{(A)} \neq 0$.

</li>
<li>

If $A$ has rank $n$, then $A$ is invertible, and then $B$ is also invertible, so 
$B$  has rank $n$ too. <BR>
If $\text{rank}$ $A < n$ then $\lambda = 0$ is an eigenvalue of both $A$ and $B$.
In this case we can use

$$
   \text{rank}\,A = n - \text{dim Nul}\,A
$$
Recall that  $\text{Nul}$ $A$ is the eigenspace for the eigenvalue $\lambda = 0$, so 
$\text{dim Nul}$ $A$ is the geometric multiplicity of the eigenvalue $\lambda = 0$,
which multiplicity is the same for $A$ and $B$. We deduce that 

<BR>

$$
   \text{rank}\,A = n - \text{dim Nul}\,A = n - \text{dim Nul}\,B = \text{rank}\,B.
$$


%We can use the identities of {prf:ref}`Prop:BasisDim:RankAPEqualToRankPA` from the %section 'Basis and Dimension'. 
%Since $P$ and $P^{-1}$ are both invertible we find: if $A = PBP^{-1}$,
%then $\text{rank}(A) = \text{rank}(PBP^{-1})  = \text{rank}(PB) = \text{rank}(B)$.

</li>
</ol>

::::::

## Diagonalizability

::::::{prf:definition}
:label: Dfn:Diagonalizable:Diagonalizability

A matrix is $A$ is called **diagonalizable** if it is similar to a diagonal matrix. That means that a diagonal matrix $D$ and an invertible matrix $P$ exist such that

$$
A = PDP^{-1}.
$$

We then say that $PDP^{-1}$ is a **diagonalization** of $A$.

::::::

An equivalent alternative characterization of diagonalizability is given in the following proposition.

::::::{prf:proposition}
:label: Prop:Eigenvalues:DiagbleVersusEigenvectors

An $n \times n$  matrix $A$ is diagonalizable if and only if $A$ has $n$ linearly independent eigenvectors.
Such a set of eigenvectors then forms a basis for $\R^n$.

::::::

Since this proposition is such a pillar on which much of the theory of matrices rests, and diagonalizable matrices are important because they are in many respects easy to work with, we give two proofs.

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:Eigenvalues:DiagbleVersusEigenvectors`
:class: tudproof

The first proof is algebraic. First we note that

$$
A = PDP^{-1} \,\, \iff \,\, AP = PDP^{-1}P  \,\, \iff \,\, AP = PD.
$$

Next we write out these last matrix products column by column:

$$
AP = A [\vect{p}_1 \quad  \vect{p}_2 \quad \cdots \quad \vect{p}_n] =
[A\vect{p}_1 \quad  A\vect{p}_2 \quad  \cdots \quad  A\vect{p}_n]
$$

and

$$
PD = [\vect{p}_1 \quad  \vect{p}_2 \quad  \cdots \quad \vect{p}_n]\begin{bmatrix}
d_1 & 0 & 0  & \ldots & 0 \\
0 & d_2 & 0  & \ldots & 0 \\
0 &  0 & d_3 & \ldots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \ldots & d_n \end{bmatrix},
$$

so

$$
PD =  [d_1\vect{p}_1 \quad  d_2\vect{p}_2  \quad  \cdots  \quad d_n\vect{p}_n].
$$

Comparing $AP$ and $PD$ column by column we see that $A\vect{p}_i = d_i\vect{p}_i$ for $n$ linearly independent vectors in $\R^n$. Namely, an invertible matrix $P$ has linearly independent columns.

::::::

The second proof has a geometric flavour. Open it if you are interested.

::::::{admonition} Second proof of&nbsp;{prf:ref}`Prop:Eigenvalues:DiagbleVersusEigenvectors`
:class: tudproof, dropdown

First we show that diagonalizability implies the existence of $n$ linearly independent eigenvectors.

If $A = PDP^{-1}$ then by {prf:ref}`Prop:Eigenvalues:DiagbleVersusEigenvectors` $A$ and $D$ have the same eigenvalues and the relation between the eigenvectors is:

<ul>
<li>

if $\vect{v}$ is an eigenvector of $D$ for the eigenvalue $\lambda$
then $ P\vect{v}$ is an eigenvector of $A$ for the same $\lambda$.

</li>
</ul>

The eigenvalues of $D$ are simply the diagonal entries $d_i$ with the vectors $\vect{e}_i$ of the standard basis as corresponding eigenvectors.

$$
\left[\begin{array}{cccc}
d_1 & 0 &  \ldots & 0 \\
0 & d_2 &  \ldots & 0 \\
\vdots &  \vdots & \ddots & \vdots \\
0 & 0 & \ldots & d_n
\end{array}
\right]
  \left[\begin{array}{c} 1 \\ 0\\ \vdots \\ 0
\end{array}
\right]
 =
\left[\begin{array}{c}  d_1 \\ 0 \\   \vdots\\ 0   \end{array}
\right]
, \quad
\left[\begin{array}{cccc}
d_1 & 0 &  \ldots & 0 \\
0 & d_2 &  \ldots & 0 \\
\vdots &  \vdots & \ddots & \vdots \\
0 & 0 & \ldots & d_n
\end{array}
\right]
  \left[\begin{array}{c} 0 \\ 1  \\ \vdots \\ 0
\end{array}
\right]
 =
\left[\begin{array}{c}  0 \\ d_2 \\ \vdots \\ 0   \end{array}
\right]
,
\quad \text{etc.}
$$

Thus $A = PDP^{-1}$ has the eigenvalues $d_i$ with corresponding eigenvectors $P\vect{e}_i = \vect{p}_i$.
Thus the $n$ columns of $P$, which are linearly independent since $P$ is invertible, give a basis of eigenvectors for $A$.

The other half is a bit more involved. It relies on the transformation formula of matrix representations (see {prf:ref}`Prop:ChangeOfBasis:MatrixChangeStandardBasis`).

Let $T: \R^n \to \R^n$ be the linear transformation with standard matrix $A$, i.e., $T(\vect{x}) = A\vect{x}$, and suppose $A$ has $n$ linearly independent eigenvectors $\vect{v}_1, \ldots, \vect{v}_n$. Let $\lambda_1, \ldots, \lambda_n$ denote the eigenvalues.
So $A\vect{v}_i =\lambda_i\vect{v}_i$.

For the basis $\mathcal{B} = (\vect{v}_1, \ldots, \vect{v}_n)$ we then see that

$$
[T]_{\mathcal{B}} = D = \begin{bmatrix}
\lambda_1 & 0 & 0  & \ldots & 0 \\
0 & \lambda_2 & 0  & \ldots & 0 \\
0 &  0 & \lambda_3 & \ldots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \ldots & \lambda_n \end{bmatrix},
$$

and the transformation formula gives

:::::{math}
:label: Eq:Diagonalizable:PinvAP

D = [T]_{\mathcal{B}} = P^{-1}[T]_{\mathcal{E}}P = P^{-1}AP,

:::::

where 

$$
 P = P_{\mathcal{E} \leftarrow \mathcal{B}} =  [ \vect{v}_1 \,\,   \vect{v}_2\,    \ldots  \,\,  \vect{v}_n]
$$

is the change-of-coordinates matrix from $\mathcal{B}$ to the standard basis.

Lastly, the identity $D=P^{-1}AP$ in Equation {eq}`Eq:Diagonalizable:PinvAP` is equivalent to $A = PDP^{-1}$.

::::::

::::::{prf:example}
:label: Ex:Diagonalizable:CheckPDPinv

We verify the relation $A = PDP^{-1}$ for the matrix $A = \begin{bmatrix} 1 & 4 \\ 1 & 1 \end{bmatrix}$ we studied before.
We found that $A$ has the eigenvalues $\lambda_1 = 3$, $\lambda_2 = -1$, with corresponding eigenvectors $\vect{v}_1 = \begin{bmatrix} 2 \\1 \end{bmatrix}$ and $\vect{v}_2 = \begin{bmatrix} -2 \\1 \end{bmatrix}$.

Thus for a diagonalization of $A$ we can take

$$
P = \left[\begin{array}{cc}\vect{v}_1 & \vect{v}_2\end{array} \right]
 =
\left[\begin{array}{cc}2 & -2 \\ 1 & 1 \end{array} \right]
, \qquad  D = \left[\begin{array}{cc} 3&0 \\ 0 & -1 \end{array}
\right].
$$

We will check that this is okay. To start with,

$$
P^{-1} = \dfrac14\left[\begin{array}{cc} 1 &  2 \\ -1 & 2 \end{array}
\right],
$$

so

$$
PDP^{-1} = \underbrace{\left[\begin{array}{cc} 2 & -2 \\ 1 & 1 \end{array}
\right]
\left[\begin{array}{cc} 3&0 \\ 0 & -1 \end{array}
\right]
}
\dfrac14\left[\begin{array}{cc} 1 &  2 \\ -1 & 2 \end{array}
\right]
 =
\dfrac14 \underbrace{\left[\begin{array}{cc} 6 & 2 \\ 3 & -1 \end{array}
\right]
}
\left[\begin{array}{cc} 1 &  2 \\ -1 & 2 \end{array}
\right]
.
$$

The last product equals

$$
\dfrac14 \begin{bmatrix} 4 & 16 \\ 4 & 4 \end{bmatrix} = \begin{bmatrix} 1 & 4 \\ 1 & 1 \end{bmatrix} =
A,
$$

as it should.

Note that the diagonalization is not unique: the *order* of the eigenvalues can be changed, and the eigenvectors may be *scaled*.
However, the order of the eigenvectors in $P$ must correspond to the order of the eigenvalues on the diagonal of $D$.
For instance, for the matrix $A$ at hand, an alternative diagonalization is given by

$$
A =   \left[\begin{array}{cc} 4 & 6 \\ -2 & 3  \end{array}
\right]
   \left[\begin{array}{cc} -1 & 0 \\ 0 & 3   \end{array}
\right]
\left[\begin{array}{cc} 4 & 6 \\ -2 & 3   \end{array}
\right]
^{-1}.
$$

::::::



Are all matrices diagonalizable? Most certainly not, as the following two examples, studied before, show.

::::::{prf:example}
:label: Ex:Diagonalizable:RotationCtd

The matrix $R = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$ of {prf:ref}`Ex:EigenValues:Rotation` does not have any (real) eigenvalues, so also no eigenvectors. Hence it cannot be diagonalized.

::::::

::::::{prf:remark}
:label: Rem:Diagonalizable:RotationCtd

Things would be different if we would allow complex eigenvalues and eigenvectors. We will devote a separate section ({numref}`Section:ComplexEV`) to this. And then it will appear that the matrix $R$ is **complex diagonalizable**.

::::::

In the previous example there were not enough eigenvalues for the matrix $A$ to be real diagonalizable. In the following example there is another reason why a matrix can fail to be diagonalizable.

::::::{prf:example}

The matrix
$A = \left[\begin{array}{cc} 2 & 1 \\ 0 & 2 \end{array}
\right]$
has the double eigenvalue $\lambda_1 = \lambda_2 = 2$.
Since  
$A - 2I = \left[\begin{array}{cc} 0 & 1 \\ 0 & 0 \end{array}
\right]$
has rank 1, there is only one independent eigenvector.
Thus there does not exist a basis of eigenvectors for $A$, and consequently the matrix $A$ is not diagonalizable.

::::::

::::::{prf:example}
:label: Ex:Diagonalizable:SecondCharPolyCtd2

The matrix
$A = \left[\begin{array}{ccc} 4 & -1 & -2 \\0 & 3 & 0 \\ 1 & 2 & 1 \end{array}
\right]$
of {prf:ref}`Ex:EigenValues:SecondCharPoly`
and {prf:ref}`Ex:EigenValues:SecondCharPolyContinued`
provides another example of this phenomenon. It has the two eigenvalues, $\lambda_1=3$, of algebraic multiplicity 2, and $\lambda_2 = 2$, of algebraic multiplicity 1.
There is only one independent eigenvector for $\lambda_{1}$. This, together with the single independent eigenvector for $\lambda_2$ is a maximal set of two linearly independent eigenvectors for $A$.  So, this matrix  $A$ is again not diagonalizable.

::::::

::::::{exercise}
:label: Exc:Diagonalizable

Is the matrix
$A = \left[\begin{array}{cccc}1 & 1 & 0 & 1 \\ 0 & 2 & 0 & 0\\
0 & 0 & 2 & 1 \\ 0 & 0 & 0 & 1 \end{array} \right]$
diagonalizable?

::::::

These examples show the two causes why a matrix may not be diagonalizable, as is made explicit in the following proposition.

::::::{prf:theorem}
:label: Thm:Diagonalizable:ThirdCharacterization

The $n \times n$ matrix $A$ is (real) diagonalizable if and only if it satisfies the following two conditions.

<ol type = "i">

<li>

The characteristic polynomial of $A$ has exactly $n$  *real*  roots, counting multiplicities.

</li>

<li>

For each eigenvalue the geometric multiplicity is equal to the algebraic multiplicity.

</li>
</ol>

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Thm:Diagonalizable:ThirdCharacterization`
:class: tudproof

First we show that a diagonalizable matrix satisfies the two conditions.

If $A$ is diagonalizable, then there must be $n$ independent eigenvectors. The sum of the dimensions $m_k$ of the eigenspaces $E_{\lambda_i}$, i.e., the sum of the geometric multiplicities must therefore be equal to $n$. Since the algebraic multiplicities are at least as large as the geometric multiplicities, the sum of the algebraic multiplicities must be $\geq n$. Since this sum cannot be larger, it means that the sum is equal to $n$. Thus all algebraic multiplicities must in fact be equal to the corresponding geometric multiplicities. This settles properties i and ii.

Conversely, conditions i. and ii. immediately imply that there must be $n$ linearly independent eigenvectors. 
The basic idea is that, since eigenvectors for different eigenvalues are automatically linearly independent, the bases for the eigenspaces put together give exactly $n$ linearly independent eigenvectors.  

::::::

::::::{admonition} (More detailed) Proof of&nbsp;{prf:ref}`Thm:Diagonalizable:ThirdCharacterization`
:class: tudproof, dropdown

Suppose that the $n \times n$ matrix $A$ has only real eigenvalues,  say  $\lambda_1,\ldots,\lambda_k$, and that for each eigenvalue $\lambda_i$ the geometric multiplicity $m_i$  is equal to the algebraic multiplicity, so

$$
  \text{g.m.}(\lambda_i)  = m_i= \text{a.m.}(\lambda_i) , \quad i = 1, \ldots, k.
$$

Since the sum of the algebraic multiplicities is equal to  $n$, the
 sum of the geometric multiplicities must be equal to $n$ too,
 
$$
  m_1 + m_2 + \ldots + m_k = n.
$$ 
 
For each $i$ let $\{\vect{v}^{(i)}_1, \ldots, \vect{v}^{(i)}_{m_i}\}$  be a basis for the eigenspace  $E(\lambda_i)$. If we can show that the union of all these bases is a basis for $\R^n$, we have a basis of eigenvectors for matrix $A$, and by   {prf:ref}`Prop:Eigenvalues:DiagbleVersusEigenvectors` $A$ is diagonalizable.  To this end it is sufficient to show that the total set

$$
  \left\{\vect{v}^{(1)}_1, \ldots, \vect{v}^{(1)}_{m_1}, .\,.\,.\,.\,., \vect{v}^{(k)}_1, \ldots, \vect{v}^{(k)}_{m_k} \right\}
$$   

is linearly independent.  So, suppose that 

:::::{math}
:label:  Eq:Diagonalizable:SumAllEigenvalues

   \underbrace{c^{(1)}_1\vect{v}^{(1)}_1+ \cdots + c^{(1)}_{m_1}\vect{v}^{(1)}_{m_1}} \,+ \,\cdot\,\cdot\,\cdot\,\cdot\,\cdot\,
+ \,  \underbrace{c^{(k)}_1\vect{v}^{(k)}_1+ \cdots + c^{(k)}_{m_k}\vect{v}^{(k)}_{m_k}}  = \vect{0}.

:::::

If we introduce

$$
   \vect{y}_i = c^{(i)}_1\vect{v}^{(i)}_1+ \cdots + c^{(i)}_{m_i}\vect{v}^{(i)}_{m_i}, \quad i = 1,\ldots,k,
$$


we have that  

$$
   \vect{y}_1 + \vect{y}_2 +  \ldots + \vect{y}_k = \vect{0}.
$$

Since each  vector  $\vect{y}_i$ lies in the eigenspace  $E(\lambda_i)$,  and by {prf:ref}`Prop:Eigenvalues:IndepEigenvectors`  eigenvectors for different eigenvalues are linearly independent, it follows that 

$$
  \vect{y}_i = \vect{0}, \quad i = 1, \ldots, k.
$$

So we have for each underbraced term  in Equation {eq}`Eq:Diagonalizable:SumAllEigenvalues`

$$
  c^{(i)}_1\vect{v}^{(i)}_1+ \cdots + c^{(i)}_{m_i}\vect{v}^{(i)}_{m_i} = \vect{0}.
$$

Since the vectors in a set $\{\vect{v}^{(i)}_1, \ldots, \vect{v}^{(i)}_{m_i}\}$ were supposed to form a basis for the eigenspace $E(\lambda_i)$, they must be linearly independent. Thus it follows for the coefficients in the last sum  that 

$$
    c^{(i)}_1 = 0, \,\ldots\,, \, c^{(i)}_{m_i}= 0.
$$

This shows that {eq}`Eq:Diagonalizable:SumAllEigenvalues`  can only hold if all coefficients  are zero, and consequently the set

$$
   \{\vect{v}^{(1)}_1, \,\ldots, \,\vect{v}^{(1)}_{m_1}, \,\,.\,.\,.\,.\,.\,\,, \,\vect{v}^{(k)}_1, \,\ldots, \, \vect{v}^{(k)}_{m_k}\} 
$$

being a linearly independent set of $n$ vectors, will indeed be a basis consisting of eigenvectors (for $\R^n$).

::::::

We saw that there is a weak connection between eigenvalues and (non-)invertibility:

{prf:ref}`Prop:EigenValues:SingularMatrix` states: a matrix is singular if and only if it has the eigenvalue $0$.


In exercise 6.3.12 below you are invited to investigate the connection (or no-connection) between diagonalizability and invertibility.

%::::::{exercise}
%:label: Exc:Diagonalizable:Invertibility
%
%Give examples of
%
%<ol type = "i">
%
%<li>
%
%A matrix that is diagonalizable but not invertible.
%
%</li>
%
%<li>
%
%A matrix that is invertible but not diagonalizable.
%
%</li>
%
%<li>
%
%A matrix that is not invertible and not diagonalizable.
%
%</li>
%
%<li>
%
%A matrix that is both invertible and diagonalizable.
%
%</li>
%</ol>


We stated that diagonalizable matrices have nice properties. Here is one: for diagonalizable matrices finding (high) powers can be done very efficiently.

::::::{prf:example}
:label: Ex:Diagonalizable:EasyPowers

If $A = PDP^{-1}$,  then $A^k =  PD^kP^{-1}$, for $k = 0,1,2,3, \ldots$

For instance,

$$
A^3 = (PDP^{-1})(PDP^{-1})(PDP^{-1}) = PD  (P^{-1}P)D (P^{-1}P)D P^{-1}  = PD^3P^{-1},
$$

since the internal factors $P^{-1}P$ reduce to the identity matrix $I$, and $ID = D$.

Check for yourself what happens if $k = 0$.

The advantage is the following. Normally, multiplication of two $n \times n$ matrices requires $n$ multiplications per entry (or $2n-1$ operations, if additions are counted as well), and there are $n\times n$ entries to be computed. So for the $k$th power that requires about $k\times n^3$ multiplications of numbers.
To compute $PD^kP^{-1}$ we need $n$ $k$th powers to find $D^k$, and we are left with one 'simple' matrix product $PD^k$ and one 'full' matrix product.

::::::

::::::{prf:example}
:label: Eq:Diagonalizable:10thPowerofA

We compute $A^{10}$ for the matrix $A = \left[\begin{array}{cc} 1 & 4 \\ 1 & 1 \end{array} \right]$
of {prf:ref}`Ex:Diagonalizable:CheckPDPinv`.

There we already settled that $A = PDP^{-1}$, with

$$
  P = \left[\begin{array}{cc} 2 & -2 \\ 1 & 1 \end{array}
\right]
,
\quad D = \left[\begin{array}{cc} 3&0 \\ 0 & -1 \end{array}
\right]
, \quad P^{-1} =
\dfrac14\left[\begin{array}{cc} 1 &  2 \\ -1 & 2 \end{array}
\right]
.
$$

We see that

:::{math}
:label: Eq:Diagonalizable:10thPowerofA

A^{10} = \left[\begin{array}{cc} 2 & -2 \\ 1 & 1 \end{array} \right]
\left[\begin{array}{cc} 3^{10}&0 \\ 0 & (-1 )^{10} \end{array} \right]
\dfrac14\left[\begin{array}{cc} 1 & 2 \\ -1 & 2 \end{array} \right].

:::

This can be evaluated to yield

$$
A^{10} = \frac14 \left[\begin{array}{cc} 2\cdot 3^{10} & -2 \\ 3^{10} & 1\end{array}
\right]
\left[\begin{array}{cc} 1 &  2 \\ -1 & 2 \end{array}
\right]
= \frac14 \left[\begin{array}{cc} 2\cdot 3^{10}+2 & 4\cdot 3^{10}-4 \\ 3^{10}-1 & 2\cdot 3^{10}+2  \end{array}
\right]
.
$$

An alternative way to denote the last matrix:

$$
A^{10} = \frac{3^{10}}{4} \left[\begin{array}{cc} 2 & 4 \\ 1 & 2 \end{array}
\right]
+
\frac{1}{4}\left[\begin{array}{cc} 2 &  -4 \\ -1 & 2 \end{array}
\right]
.
$$

Note that we could have found any power of $A$ just as easily: replacing $10$ by $n$ in Equation {eq}`Eq:Diagonalizable:10thPowerofA` gives

$$
\begin{array}{rcl}
A^{n} &=& \left[\begin{array}{cc} 2 & -2 \\ 1 & 1 \end{array}
\right]
\left[\begin{array}{cc} 3^{n}&0 \\ 0 & (-1 )^{n} \end{array}
\right]
\dfrac14\left[\begin{array}{cc} 1 &  2 \\ -1 & 2\end{array}
\right]
 \\
&=& \dfrac14 \left[\begin{array}{cc} 2\cdot 3^{n}+2\cdot(-1)^n & 4\cdot 3^{n}-4\cdot(-1)^n \\
3^{n}- (-1)^n & 2\cdot 3^{n}+2\cdot(-1)^n \end{array}
\right]
\end{array}
$$

::::::

To conclude this section we return to the 'toy' migration model ({prf:ref}`Ex:EigenValues:ToyMigrationModel`) of this chapter to illustrate the power of diagonalization.

::::::{prf:example}
:label: Ex:Diagonalize:DiagonalizeMigration

Suppose the migrations between two cities $A$ and $B$ are described by the model

$$
\left[\begin{array}{c} x_{k+1} \\y_{k+1}\end{array}
\right]
 =
\left[\begin{array}{c} 0.9x_{k} + 0.2 y_k\\0.1x_{k} + 0.8 y_k\end{array}
\right]
  =
\left[\begin{array}{cc} 0.9 & 0.2 \\ 0.1 & 0.8 \end{array}
\right]
\left[\begin{array}{c} x_{k} \\y_{k}\end{array}
\right]
.
$$

In short

$$
\vect{x}_{k+1} = \left[\begin{array}{cc} 0.9 & 0.2 \\ 0.1 & 0.8 \end{array}
\right]
\vect{x}_{k} = M\vect{x}_{k},
$$

where

$$
\vect{x}_k = \left[\begin{array}{c} x_{k} \\y_{k}\end{array}
\right]
 =
\left[\begin{array}{c} \text{population in city  } A \text{  at time  } k \\
\text{population in city  } B \text{  at time  } k\end{array}
\right]
.
$$

It can be shown that $M$ has the eigenvalues $\lambda_1 = 1$ and $\lambda_2 = 0.7$, with corresponding eigenvectors

$$
\vect{v}_1 = \left[\begin{array}{c} 2 \\1\end{array}
\right]
, \quad
\vect{v}_2 = \left[\begin{array}{c} 1 \\-1\end{array}
\right]
 \quad \text{respectively.}
$$

Since $\{\vect{v}_1, \vect{v}_2\}$ is a basis of eigenvectors, the matrix $M$ is diagonalizable, and in fact we have

$$
M = PDP^{-1} = \left[\begin{array}{cc} 2 &1\\1&-1\end{array}
\right]
\left[\begin{array}{cc} 1&0\\0&0.7\end{array}
\right]
\left[\begin{array}{cc} 2 &1\\1&-1\end{array}
\right]
^{-1}.
$$

If the initial populations are given by

$$
\vect{x}_0 = \left[\begin{array}{c} x_{0} \\y_{0}\end{array}
\right]
,
$$

then

$$
\vect{x}_k = M^k\vect{x}_0 = PD^kP^{-1}\vect{x}_0.
$$

In this case we can clearly see what happens in the long run, i.e. when we let $k$ go to infinity:

$$
D^k = \left[\begin{array}{cc} 1^k&0\\0&0.7^k\end{array}
\right]
 \longrightarrow
\left[\begin{array}{cc} 1&0\\0&0\end{array}
\right]
, \quad \text{if  } k \to \infty.
$$

By computing $P^{-1}$ and the product of the three matrices $P$, $D$ and $P^{-1}$ we find that if $ k \to \infty$,

$$
M^k  = PD^kP^{-1} \longrightarrow       P\left[\begin{array}{cc} 1&0\\0&0\end{array}
\right]
P^{-1}
= \frac13 \left[\begin{array}{cc} 2&2 \\ 1&1\end{array}
\right].


$$

We may conclude that, for $ k \to \infty$,

$$
\vect{x}_k = M^k\vect{x}_0 \longrightarrow \frac13 \left[\begin{array}{cc} 2&2 \\ 1&1\end{array}
\right]
\left[\begin{array}{c} x_{0} \\y_{0}\end{array}
\right]
 =
\frac13\left[\begin{array}{c} 2x_{0}+2y_{0} \\ x_{0}+y_{0}\end{array}
\right]
 =
\frac13(x_{0}+y_{0}) \left[\begin{array}{c} 2 \\ 1\end{array}
\right]
.
$$

The interpretation: in the long run the distribution of the people over the two cities approaches the
steady state distribution where city $A$ has twice as many inhabitants as city $B$. Moreover,
the total number of inhabitants of the two cities is still the same as at the beginning:

$$
x_{\infty} + y_{\infty} = \tfrac13(2x_{0}+2y_{0}) + \tfrac13(x_{0}+y_{0}) = x_{0}+y_{0}.
$$

::::::

## Grasple Exercises 

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bd1c8f7a-917f-431f-889b-463ab7a7c6f6?id=91486
:label: grasple_exercise_6_3_1
:dropdown:
:description: Given a $2\times 2$ matrix $A$ and 'diagonalizer' $P$, to find the diagonal matrix $D$ such that $A=PDP^{-1}$.  

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5bcb24df-9cfd-4e4b-bcae-b550fb0fad63?id=91488
:label: grasple_exercise_6_3_2 
:dropdown:
:description:  To find a diagonalization of a $2\times 2$ matrix (insofar it exists).

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c0d56365-5434-45b0-9c82-805112428024?id=91489
:label: grasple_exercise_6_3_3 
:dropdown:
:description:  To find a diagonalization of a $2\times 2$ matrix (insofar it exists).

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5a71e703-acd5-48b1-9b6d-8a51f4f8cf95?id=91501
:label: grasple_exercise_6_3_4 
:dropdown:
:description: To investigate the diagonalizability of a ($3 \times 3$) matrix. 

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/537a306b-47d1-422a-bc15-c7a75b81c24b?id=91496
:label: grasple_exercise_6_3_5 
:dropdown:
:description:  To investigate the diagonalizability of a ($3 \times 3$) matrix.

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5a71e703-acd5-48b1-9b6d-8a51f4f8cf95?id=91501
:label: grasple_exercise_6_3_6
:dropdown:
:description:  To investigate the diagonalizability of a ($3 \times 3$) matrix.

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f61dfb8f-db65-4f17-80c7-b1702b0c2c07?id=104493
:label: grasple_exercise_6_3_7 
:dropdown:
:description:  To investigate the diagonalizability of a 3x3 matrix of rank 1. 

::::::


::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/70b5964e-b6c7-4a64-a2e3-d10dc915f324?id=91503
:label: grasple_exercise_6_3_8 
:dropdown:
:description:  To investigate the diagonalizability of a ($3 \times 3$) matrix. 

::::::


::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/534ce865-0960-403a-affc-0f23f2d14110?id=91521
:label: grasple_exercise_6_3_9 
:dropdown:
:description: For which $\alpha$ is given (upper triangular) $4 \times 4$ matrix diagonalizable?

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f3cdb060-469a-4a30-be46-1ecc7197d66a?id=91522
:label: grasple_exercise_6_3_10 
:dropdown:
:description: True/False question (about a $4\times4$ matrix with $3$ distinct eigenvalues).  

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d1cb7e54-6c99-4a01-b161-832b37d650d0?id=91523
:label: grasple_exercise_6_3_11 
:dropdown:
:description:  True/False question (invertibilty implies diagonalizability?)

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4398c155-7971-42f6-b809-31ae507c0326?id=87331
:label: grasple_exercise_6_3_12 
:dropdown:
:description:  Creating examples of all cases (non-)invertible versus (non-)diagonalizable.

::::::
::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9aca77fa-a7c8-4998-be00-a55c19e9fd70?id=62419
:label: grasple_exercise_6_3_13 
:dropdown:
:description:  To draw conclusions from a diagonalization  $A = PDP^{-1}$.

::::::