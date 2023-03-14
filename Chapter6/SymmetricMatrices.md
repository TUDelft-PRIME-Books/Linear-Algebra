(Sec:SymmetricMat)=
# Symmetric matrices 

## Overview 

::::{prf:definition} 
:label: Dfn:SymmetricMat:SymmetricMatrix



A matrix $A$ is called a **symmetric matrix**  if  

$$
  A^T = A.
\nonumber
$$

Note that this definition implies that a symmetric matrix must be a square matrix.

::::


::::{prf:example} 



The matrices

$$
  A_1 = \begin{bmatrix} 2&3&4\\3&1&5 \\4&5&7  \end{bmatrix} \quad \text{and} \quad 
  A_2 = \begin{bmatrix} 0&2&3&4\\
                                  2&0&1&5 \\
                                  3&1&0&6 \\
                                  4&5&6&7\end{bmatrix}
\nonumber
$$

are symmetric.  The matrices

$$
  A_3 = \begin{bmatrix} 2&3&4\\2&3&4 \\ 2&3&4  \end{bmatrix} \quad \text{and} \quad 
  A_4 = \begin{bmatrix} 0&2&3&0\\
                                  2&0&1&0 \\
                                  3&1&0&0 \\
                                  \end{bmatrix}
\nonumber
$$

are not symmetric.

First we will establish the following three essential properties of symmetric matrices. 

<ul>
<li>

All eigenvalues of symmetric matrices are real. 


</li>
<li>

Eigenvectors for different  eigenvalues are automatically orthogonal.


</li>
<li>

For each eigenvalue the geometric multiplicity is equal to the algebraic multiplicity.


</li>
</ul>

::::

As a consequence, symmetric matrices are

<ul>
<li>

**real diagonalizable**.


</li>
</ul>

In fact, we will see an even stronger property holds, namely


<ul>
<li>

each symmetric matrix is **orthogonally diagonalizable**.


</li>
</ul>
This 

<ul>
<li>

**orthogonal diagonalization**  of symmetric matrices, 


</li>
</ul>
leads the  way  to the so-called

<ul>
<li>

**spectral decomposition**  of symmetric matrices. An instance where  eigenvalues and orthogonality come together.


</li>
</ul>

A first example to underline a few of these these properties consider the following example.



::::{prf:example} 



Let $A$ be given by  $A = \begin{bmatrix} 1&2\\2&-2 \end{bmatrix}$.

The eigenvalues are found via

$$
 \det{(A - \lambda I)} = \begin{vmatrix} 1-\lambda&2\\2&-2-\lambda \end{vmatrix} 
   = (1-\lambda)(-2-\lambda) -4 =   \lambda^2 +\lambda -6 =  (\lambda-2)(\lambda+3) .
\nonumber
$$

They are  $\lambda_1 = 2,  \,\lambda_2 = -3$.

Corresponding eigenvectors: \, $\mathbf{v}_1 = \begin{bmatrix} 2\\1 \end{bmatrix}$  for $\lambda_1$,  and 
$\mathbf{v}_2 = \begin{bmatrix} 1\\-2 \end{bmatrix}$.\\
The eigenvectors are indeed orthogonal, 

$$
  \mathbf{v}_1 \ip \mathbf{v}_2 = \begin{bmatrix} 2\\1 \end{bmatrix}\ip \begin{bmatrix} 1\\-2 \end{bmatrix} = 2 - 2 = 0, 
 \nonumber   
$$

and $A$ can be diagonalized as

$$
   A = PDP^{-1} = \begin{bmatrix}2&1\\1&-2 \end{bmatrix}\begin{bmatrix}2 & 0\\0& -3 \end{bmatrix}
   \begin{bmatrix}2&1\\1&-2 \end{bmatrix}^{-1}.
 \nonumber   
$$


::::

## The big three (properties) of Symmetric Matrices 


::::{prf:proposition} 
:label: Prop:SymmetricMat:OrthogonalEigenvectors


 
Suppose $A$ is a symmetric matrix.
  
If $\mathbf{v}_1$  and $\mathbf{v}_2$  are eigenvectors of $A$ for different eigenvalues,  then  $\mathbf{v}_1\perp \mathbf{v}_2$.
::::


::::{prf:proof} 



Suppose   $\mathbf{v}_1$  and $\mathbf{v}_2$  are eigenvectors of the symmetric matrix $A$ for the different eigenvalues  $\lambda_1,\lambda_2$.
We want to show that  $\mathbf{v}_1 \ip \mathbf{v}_2 = 0$.

The trick is to consider the expression 

:::{math} 
:label: Eq:SymmetricMat:Av1v2


 (A\mathbf{v_1}) \ip \mathbf{v}_2.



:::

On the one hand

$$
   (A\mathbf{v_1}) \ip \mathbf{v}_2 = (\lambda_1\mathbf{v_1}) \ip \mathbf{v}_2 =  \lambda_1(\mathbf{v_1} \ip \mathbf{v}_2).
\nonumber
$$

On the other hand

$$
   (A\mathbf{v_1}) \ip \mathbf{v}_2 = (A\mathbf{v_1})^T \mathbf{v}_2 =\mathbf{v_1}^TA^T \mathbf{v}_2. 
\nonumber
$$

Since  we assumed that $A^T = A$  we can extend the chain of identities:

$$
  \mathbf{v_1}^TA^T \mathbf{v}_2 =   \mathbf{v_1}^T A \mathbf{v}_2 =\mathbf{v_1}^T (A \mathbf{v}_2) =
  \mathbf{v_1}^T (\lambda_2 \mathbf{v}_2) =  \lambda_2(\mathbf{v_1}^T  \mathbf{v}_2) =  \lambda_2(\mathbf{v_1} \ip \mathbf{v}_2).
\nonumber
$$

So we have shown that

$$
    (A\mathbf{v_1}) \ip \mathbf{v}_2  = \lambda_1(\mathbf{v_1} \ip \mathbf{v}_2) = \lambda_2(\mathbf{v_1} \ip \mathbf{v}_2).
\nonumber
$$

Since   

$$
\lambda_1 \neq \lambda_2,
\nonumber
$$

it follows that indeed 

$$
\mathbf{v_1} \ip \mathbf{v}_2 = 0,
\nonumber
$$

as was to be shown.

::::


::::{prf:proposition} 
:label: Prop:SymmetricMat:RealEigenvalues


 
All eigenvalues of symmetric matrices are real.     

::::

The easiest proof is via complex numbers.  Skip it if you like.


::::{prf:proof} 



In fact, the shortest proof uses the complex inner product.
For two vectors $\mathbf{u},\mathbf{v}$ in $\C^n$  the inner product is defined via

$$
  \mathbf{u} \ip \mathbf{v}  = \overline{u_1}v_1 + \ldots + \overline{u_n}v_n = \overline{\mathbf{u}}^{T}\mathbf{v}.
\nonumber
$$


Note that   the inner product of any vector $\mathbf{u}$ with itself is then a non-negative real number:

$$
  \mathbf{u} \ip \mathbf{u} = \overline{u_1}u_1 + \overline{u_2}u_2 + \ldots +  \overline{u_n}u_n =
                          |u_1|^2 + |u_2|^2 + \ldots + |u_n|^2,
\nonumber
$$

where now  $|u_i|$  denotes the modulus of the complex number $u_i$. From the expression with the sum of squares it follows that 
$\mathbf{u} \ip \mathbf{u} = 0$  only holds if $\mathbf{u} = \mathbf{0}$.

The complex inner product is not symmetric, however the following holds 

$$
  \mathbf{v} \ip \mathbf{u} = \overline{\mathbf{u} \ip \mathbf{v}}.
\nonumber  
$$

Now suppose that  $\lambda$ is an eigenvalue of the symmetric matrix $A$, and  $\mathbf{v}$ is a nonzero (possible complex) eigenvector of $A$ for the eigenvalue $\lambda$.   Note that, since  $A$ is real and symmetric,  $\overline{A}^T = A^T = A$.
We will show that $\overline{\lambda} = \lambda$.

We will use kind of the same 'trick' as in {prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors`  Equation  {eq}`Eq:SymmetricMat:Av1v2`.
On the one hand 

$$
 (A\mathbf{v}) \ip \mathbf{v} = \overline{(A \mathbf{v})} \mathbf{v} = \overline{\lambda}  \overline{\mathbf{v}} \mathbf{v} = 
 \overline{\lambda}  \mathbf{v}\ip \mathbf{v}.
\nonumber
$$

On the other hand

$$
 (A\mathbf{v}) \ip \mathbf{v} = \overline{A\mathbf{v}}^T \mathbf{v} = \overline{\mathbf{v}}^T \overline{A}^T \mathbf{v} = 
 \overline{\mathbf{v}}^T A \mathbf{v} =  \overline{\mathbf{v}}^T \lambda\mathbf{v} 
 = \lambda\overline{\mathbf{v}}^T \mathbf{v} = \lambda \mathbf{v}\ip \mathbf{v}.
\nonumber
$$

So we have that

$$
   \overline{\lambda}  \mathbf{v}\ip \mathbf{v} = \lambda \mathbf{v}\ip \mathbf{v}
\nonumber
$$

Since we assumed that $\mathbf{v}$ is not the zero vector, we have that   $\mathbf{v}\ip \mathbf{v} \neq 0$  it follows that  $ \overline{\lambda} =\lambda$.

::::




::::{prf:example} 



Let  $A = \begin{bmatrix} a&c\\c&b \end{bmatrix} $.  

Then the characteristic polynomial is computed as

$$
  \begin{vmatrix} a-\lambda&c\\c&b-\lambda \end{vmatrix} = 
  (a-\lambda)(b-\lambda) - c^2 = \lambda^2 - (a+b)\lambda + ab - c^2.
\nonumber 
$$

The discriminant of this second order polynomial is given by

$$
  D =  (a+b)^2 -4(ab -c^2) = a^2+b^2 - 2ab + 4c^2 = (a-b)^2 + 4c^2 \geq 0.
\nonumber 
$$

The discriminant is non-negative, so the characteristic polynomial has only real roots, and consequently the eigenvalues of the matrix are real.

Obviously, an elementary approach like this will not work for larger $n \times n$ matrices.

::::

Next we come to the third of 'the big three' of symmetric matrices.

::::{prf:proposition} 
:label: Prop:SymmetricMat:AlgGeomMultiplicity


 
For each  eigenvalue of a symmetric matrix the geometric multiplicity is equal to the algebraic multiplicity.    

::::


Combining {prf:ref}`Prop:SymmetricMat:RealEigenvalues` and {prf:ref}`Prop:SymmetricMat:AlgGeomMultiplicity` leads to 
the following important theorem about (real) symmetric matrices.


::::{prf:theorem} 
:label: Thm:SymmetricMat:Diagonalizable



Every symmetric matrix is  diagonalizable

::::

We will first look at a  few examples.  After that we will give  a sketch of the elaborate proof of this theorem. 


::::{prf:example} 

Consider the matrix $A = \begin{bmatrix} 1 & 0 & 1\\0 & 1  & 2 \\ 1 & 2 & 5 \end{bmatrix}$.

We first find the characteristic polynomial.

Expansion along the first row gives
    
$$
      \begin{array}{rcl}
        \begin{vmatrix}    1-\lambda & 0 & 1\\0 & 1-\lambda  & 2 \\ 1 & 2 & 5-\lambda \end{vmatrix}
        &=&
        (1-\lambda)\begin{vmatrix}    1-\lambda  & 2 \\ 2 & 5-\lambda\end{vmatrix} + 
        1\cdot\begin{vmatrix}     0 & 1 \\ 1-\lambda  & 2\end{vmatrix} \\
        &=& 
         (1-\lambda)\big((1-\lambda)(5-\lambda) -4 \big)- (1-\lambda)  \\
        &=& 
         (1-\lambda) (\lambda^2-6\lambda) =  (1-\lambda) (\lambda-6)\lambda.
        \end{array}
    \nonumber
    $$

So $A$ has the real eigenvalues  $\lambda_{1} = 1$,   $\lambda_2 = 6$  and $\lambda_3 = 0$, and {prf:ref}`Prop:SymmetricMat:AlgGeomMultiplicity` is satisfied as well.

The eigenvectors are found to be

$$
   \mathbf{v}_1 = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix} \text{ for } \lambda_1 = 1, \quad
   \mathbf{v}_1 = \begin{bmatrix} 2 \\-1 \\ 0 \end{bmatrix} \text{ for } \lambda_2, \quad  
   \mathbf{v}_3 = \begin{bmatrix} 1 \\ 2 \\ 5 \end{bmatrix} \text{ for } \lambda_3. 
\nonumber
$$

We see:  the three eigenvectors form an orthogonal threesome, in accordance with {prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors`.

::::


::::{prf:example} 
:label: Ex:SymmetricMat:DoubleEV

Consider the matrix $A = \begin{bmatrix} 2&2&4\\2 & -1 & 2 \\ 4&2&2 \end{bmatrix}$.\\
We first find the characteristic polynomial.

$$
\begin{array}{rcl}
  \begin{vmatrix} 2-\lambda&2&4\\2 & -1-\lambda & 2 \\ 4&2&2-\lambda \end{vmatrix}
  &=&
  \begin{vmatrix} 2-\lambda&2&4\\2 & -1-\lambda & 2 \\ 2+\lambda&0&-2-\lambda \end{vmatrix}\\
  &=& \,\,
  \begin{vmatrix} 2-\lambda&2&6-\lambda\\2 & -1-\lambda & 4 \\ 2+\lambda&0&0 \end{vmatrix}
\end{array}
$$

Where first we subtracted the first row from the third row and second we added the first column to the third column. 
Expansion along the third row yields
    
$$ 
\begin{array}{rcl}
  (2+\lambda)\begin{vmatrix}2&6-\lambda\\ -1-\lambda & 4 \end{vmatrix} 
  &=&  (2+\lambda) \big(8 - (6-\lambda)( -1-\lambda) \big)\\&=&  (2+\lambda) ( 14 +5\lambda - \lambda^2) \\
  &=&  -(2+\lambda) (\lambda+2) (\lambda-7).
\end{array}
$$

So $A$ has the eigenvalues  $\lambda_{1,2} = -2$ and $\lambda_3 = 7$.
Indeed all eigenvalues are real, conforming to {prf:ref}`Prop:SymmetricMat:RealEigenvalues`.

Next we find the eigenvectors and the geometric multiplicities of the eigenvalues.

For $\lambda = -2$ we find via row reduction
    
$$
    [A - (-2)I\,|\,\mathbf{0}] = 
    \left[\begin{array}{ccc|c} 2+2&2&4&0\\2 & -1+2 & 2 &0\\ 4&2&2+2&0\end{array}\right]       \sim
    \left[\begin{array}{ccc|c} 2&1&2&0\\0&0&0&0 \\0&0&0&0\end{array}\right]    \nonumber
$$

the two linearly independent eigenvectors $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \\ -1\end{bmatrix}$ and 
$\mathbf{v}_2 = \begin{bmatrix} 1 \\ -2 \\ 0\end{bmatrix}$.  The geometric multiplicity of $\lambda_{1,2}$ is equal to 2.
The other eigenvalue had algebraic multiplicity 1, so the geometric  multiplicity has to be 1 as well. With this {prf:ref}`Prop:SymmetricMat:AlgGeomMultiplicity` is verified.

Lastly we leave it to you to check that an eigenvector for $\lambda_3 = 7$ is given by $\mathbf{v}_3 = \begin{bmatrix} 2 \\ 1 \\ 2\end{bmatrix}$.  And that  both  $\mathbf{v}_3 \perp \mathbf{v}_1$  and  $\mathbf{v}_3 \perp \mathbf{v}_2$, so that {prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors` is satisfied as well.
::::



::::{prf:proof} 

We sketch the main ideas. 
The essential tool we will invoke is the so-called **Schur factorization** of a matrix.  We have not included this in this course.
For the interested reader we refer to .\,.\,.\,.
  
The Schur factorization states that every complex matrix $A$ can be factorized as
  
:::{math} 
:label: Eq:SymmetricMat:SchurFactorization

      A = URU^{-1} = UR(\overline{U})^T 
:::

where $R$ is an upper triangular matrix and $Q$ a **unitary** matrix. A unitary matrix is the complex equivalent of an orthogonal matrix:

<div style="text-align: center;">

A matrix  $U$ is a **unitary matrix**  if  ...

</div>
<br>

Since $A$ and $R$ are similar,  $A$ and $R$  have the same eigenvalues, and for an upper triangular matrix the eigenvalues are just the diagonal entries.
So the diagonal entries of $R$ are real.

Next it can be shown that in the case of a real matrix $A$ there is also a real matrix $U$ that can be constructed  for which Equation {eq}`Eq:SymmetricMat:SchurFactorization` holds. As a consequence
  
$$
         A = QRQ^{-1} = QRQ^{T} \quad \text{which is equivalent to} \quad R = Q^TAQ.
$$

It then follows that  
  
$$
        R^T = (Q^TAQ)^T  = (Q^T)A^T(Q^T)^T = Q^TAQ = R,

$$

so that  $R$  is a symmetric upper triangular matrix,  which must then be a diagonal matrix $D$. 

And then we may conclude that
  
$$
  A = QRQ^{-1} = QDQ^{-1},
$$

which shows that $A$  is indeed diagonalizable.

And this  implies both {prf:ref}`Prop:SymmetricMat:RealEigenvalues`  and {prf:ref}`Prop:SymmetricMat:AlgGeomMultiplicity`.
  
::::

  
## Orthogonal Diagonalizability of Symmetric Matrices    

If we combine the statements of {prf:ref}`Thm:SymmetricMat:Diagonalizable` and {prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors`,
or  look into the details of the proof of the theorem, we see that the property of diagonalizability can be strengthened.
Diagonalizability of a matrix means that there exists a basis of eigenvectors. For symmetric matrices there always exists an orthogonal such basis.
By scaling this can be turned into an orthonormal basis  $\{\mathbf{q}_1, \ldots, \mathbf{q}_n\}$ of eigenvectors.

Recall that an **orthogonal matrix** is a (square) matrix  $Q$ for which  $   Q^{-1} = Q^T$. 
And this means that an orthogonal matrix has ortho**normal** columns.


::::{prf:theorem} 

A matrix is symmetric if and only if there exist an orthonormal basis of eigenvectors.

Equivalently,  a matrix $A$ is symmetric if and only if it can be written as
    
:::{math} 
:label: Eq:SymmetricMat:QDQinv

         A = QDQ^{-1}
::: 

with $D$ a diagonal matrix and $Q$ an orthogonal matrix.
A diagonalization as in Equation {eq}`Eq:SymmetricMat:QDQinv` is called an **orthogonal diagonalization**

::::


::::{prf:proof} 

One direction is proved in a very elementary way:    

If  

$$ 
    A = QDQ^{-1} = QDQ^{T}
$$

then 
        
$$  
    A^T = (QDQ^{T})^T = (Q^T)^TD^TQ^{T} = QDQ^{T} = A,
$$

so then  $A$ is symmetric.
        
For the other direction we already sketched the argument in the proof of {prf:ref}`Thm:SymmetricMat:Diagonalizable`.
We will now show the construction of such a matrix $Q$.  Note that the columns of $Q$ must be  eigenvectors of the matrix $A$, and that they must be orthonormal.

If  the $n\times n$ matrix $A$ is symmetric it is diagonalizable.  
That means that  the dimensions of the eigenspaces add up to $n$.      

For each eigenspace there exists an orthonormal basis.  
Since the eigenvectors for different eigenvalues are orthogonal, by {prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors`, 
putting all these bases together gives a set of $n$ orthonormal eigenvectors $\mathbf{q}_1, \ldots, \mathbf{q}_n$  of $A$.
::::


::::{prf:example} 

We will find an orthogonal diagonalization of the matrix

$A = \begin{bmatrix} 2&2&4\\2 & -1 & 2 \\ 4&2&2 \end{bmatrix}$. 

This is the same matrix as in {prf:ref}`Ex:SymmetricMat:DoubleEV`.  There we already established that $A$ has the eigenvalues/eigenvectors

$$
  \lambda_{1,2} = -2,  \text{ with }\mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \\ -1\end{bmatrix}, \,\,
                                        \mathbf{v}_2 = \begin{bmatrix} 1 \\ -2 \\ 0\end{bmatrix}, 
  \quad \lambda_3 = 7,  \text{ with }\mathbf{v}_3 =\begin{bmatrix} 2 \\ 1 \\ 2\end{bmatrix}.
$$

This gives the diagonalization

$$
   A = PDP^{-1} = \begin{bmatrix} 1 &1&2 \\ 0&-2&1 \\  -1 & 0 & 2\end{bmatrix}
       \begin{bmatrix} -2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 7\end{bmatrix}
       \begin{bmatrix} 1 &1&2 \\ 0&-2&1 \\  -1 & 0 & 2\end{bmatrix}^{-1}.
$$

To find an orthogonal diagonalization we first have to find an orthogonal basis for $E_{-2}$,  the eigenspace for $\lambda_{1,2}$.
We can use the Gram-Schmidt algorithm to construct such a basis:

$$
   \begin{array}{l}
       \mathbf{b}_1 = \mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \\ -1\end{bmatrix},\\
       \mathbf{b}_2 = \mathbf{v}_2 - \dfrac{ \mathbf{v}_2\ip\mathbf{b_1}}{ \mathbf{b}_1\ip\mathbf{b_1}}\mathbf{b_1} =
                   \begin{bmatrix} 1 \\ -2 \\ 0\end{bmatrix} - \dfrac{1}{2}\begin{bmatrix} 1 \\ 0 \\ -1\end{bmatrix} =
                   \begin{bmatrix} 1/2 \\ -2 \\ 1/2\end{bmatrix} = \dfrac12\begin{bmatrix} 1 \\ -4 \\ 1\end{bmatrix}.
  \end{array}
$$

Normalizing the orthogonal basis $\{\mathbf{b}_1, \mathbf{b}_2, \mathbf{b}_3\}$  and putting them side by side in a matrix yields the orthogonal matrix

$$
  Q = \begin{bmatrix} \dfrac{1}{\sqrt{2}} & \dfrac{1}{\sqrt{18}} & \dfrac{2}{3} \\ 
  0 & \dfrac{-4}{\sqrt{18}} & \dfrac{-1}{3}\\ \dfrac{-1}{\sqrt{2}} &  \dfrac{1}{\sqrt{18}} & \dfrac{2}{3}
  \end{bmatrix}
$$

And then we have

$$
 A = QDQ^{-1} = QDQ^T, \quad \text{where still}  \,\, D = \begin{bmatrix} -2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 7\end{bmatrix}.
$$
::::

The orthogonal decomposition can be rewritten in an equivalent and more meaningful way.
We will first illustrate this for a $2\times2$ matrix we studied earlier.


::::{prf:example} 
:label: Ex:SymmetricMat:OrthogProj

For the matrix $A = \begin{bmatrix} 1&2\\2&-2 \end{bmatrix}$ we showed that the eigenvalues/eigenvectors are given by

$$
\lambda_1 = 2,  \,\mathbf{v}_1 = \begin{bmatrix} 2\\1 \end{bmatrix}, \quad \lambda_2 = -3, \,\mathbf{v}_2 = \begin{bmatrix} 1\\-2 \end{bmatrix} 
$$

The vectors $\mathbf{v}_1,\mathbf{v}_2$ are  'automatically'  orthogonal.  Normalizing them gives the orthonormal basis

$$
  \{\mathbf{q}_1,\mathbf{q}_2\} = \left\{\begin{bmatrix} 2/\sqrt{5}\\1/\sqrt{5} \end{bmatrix},
                               \begin{bmatrix} 2/\sqrt{5}\\1/\sqrt{5} \end{bmatrix}\right\}$$

and with that the orthogonal diagonalization

$$
 A = QDQ^T = \begin{bmatrix} 2/\sqrt{5}& 1/\sqrt{5}\\1/\sqrt{5}& -2/\sqrt{5} \end{bmatrix}
             \begin{bmatrix} 2 & 0 \\ 0 & -3 \end{bmatrix}
             \begin{bmatrix} 2/\sqrt{5}& 1/\sqrt{5}\\1/\sqrt{5}& -2/\sqrt{5} \end{bmatrix}^T
$$

This can be rewritten as

$$
  \begin{array}{rcl}
  A &=& [\,\mathbf{q}_1\,\mathbf{q}_2\,]\begin{bmatrix} 2 & 0 \\ 0 & -3 \end{bmatrix}
             [\,\mathbf{q}_1\,\mathbf{q}_2\,]^T =
     [\,2\mathbf{q}_1\,(-3)\mathbf{q}_2]\begin{bmatrix}\mathbf{q}_1^T \\ \mathbf{q}_2^T  \end{bmatrix}.   
     \end{array}
$$

We bring in mind the column-row expansion of the matrix product.

$$
 \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}
 \begin{bmatrix} b_{11} &b_{12} \\ b_{21} & b_{22} \end{bmatrix} =
 \begin{bmatrix} a_{11} \\ a_{21} \end{bmatrix}
 \begin{bmatrix} b_{11} &b_{12}  \end{bmatrix}  + 
 \begin{bmatrix} a_{12} \\ a_{22} \end{bmatrix}
 \begin{bmatrix} b_{21} &b_{22}  \end{bmatrix}
$$


Applying this to the last expression for $A = QDQ^T$ we find

$$
  A = 2 \mathbf{q}_1\mathbf{q}_1^T + (-3)\mathbf{q}_2\mathbf{q}_2^T .
$$

The matrices

$$
   \mathbf{q}_1\mathbf{q}_1^T = \frac15 \begin{bmatrix} 4 & 2  \\ 2 & 1 \end{bmatrix}
   \quad \text{and} \quad  
   \mathbf{q}_2\mathbf{q}_2^T = \frac15 \begin{bmatrix} 1 & -2  \\ -2 & 4 \end{bmatrix}
$$

represent the orthogonal projections on the one-dimensional subspaces  $\Span{\mathbf{q}_1}$  and  $\Span{\mathbf{q}_2}$.

Furthermore these one-dimensional subspaces are orthogonal to each other.

So we have  that this symmetric matrix can be written as a linear combination of matrices  that represent orthogonal projections. 
::::

The construction we performed in the last example can be generalized. As is the content of the last theorem in this section.

::::{prf:theorem} 
:label: Thm:SymmetricMat:OrthogDecomp2

Every $n \times n$ symmetric matrix  $A$ is the linear combination 

$$
    A = \lambda_1P_1 +  \lambda_2P_2 + \ldots +  \lambda_nP_n
$$

of $n$  matrices $P_i$ that represent orthogonal projections onto one-dimensional subspaces that are mutually orthogonal.
::::

::::{prf:proof}
For a general $n\times n$ symmetric matrix $A$, there exists an orthogonal diagonalization

$$
   A = QDQ^{-1} = QDQ^{T}.
$$

Exactly as in {prf:ref}`Ex:SymmetricMat:OrthogProj` we can use the column-row expansion of the matrix product  to derive

$$
A =  \lambda_1 \mathbf{q}_1\mathbf{q}_1^T + \lambda_2\mathbf{q}_2\mathbf{q}_2^T + \ldots + \lambda_n\mathbf{q}_n\mathbf{q}_n^T,
$$

where  the vectors  $\mathbf{q}_i$  of course are the (orthonormal) columns of the diagonalizing matrix $Q$.
::::