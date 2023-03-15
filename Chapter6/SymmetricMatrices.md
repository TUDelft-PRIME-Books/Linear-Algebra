(Sec:SymmetricMat)=
# Symmetric matrices 

## Introduction 


::::{prf:definition} 
:label: Dfn:SymmetricMat:SymmetricMatrix


A matrix $A$ is called a **symmetric matrix**  if  

$$
  A^T = A.
$$

Note that this definition implies that a symmetric matrix must be a square matrix.

::::


::::{prf:example} 
:label:  Ex:SymmetricMat:SymmMat

The matrices

$$
  A_1 = \begin{bmatrix} 2&\color{blue}3&\color{red}4\\\color{blue}3&1&5 \\\color{red}4&5&7  \end{bmatrix} \quad \text{and} \quad 
  A_2 = \begin{bmatrix} 0&2&3&4\\
    2&0&\color{blue}1&5 \\
    3&\color{blue}1&0&\color{red}6 \\
    4&5&\color{red}6&7\end{bmatrix}
$$

are symmetric.  The matrices

$$
  A_3 = \begin{bmatrix} 2&3&4\\2&3&4 \\ 2&3&4 \end{bmatrix} \quad \text{and} \quad 
  A_4 = \begin{bmatrix} 0&2&3&0\\
            2&0&1&0 \\
            3&1&0&0 \\
        \end{bmatrix}
$$

are not symmetric.

::::


Symmetric matrices appear in many different contexts. In statistics the *covariance matrix* is an example of a symmetric matrix.
In  engineering the so-called *elastic strain matrix* and the *moment of inertia tensor* provide examples.


The crucial thing about symmetric matrices is stated in the  main theorem of this section.

::::{prf:theorem} 
:label: Thm:SymmetricMat:OrthogDiag

Every symmetric matrix $A$ is orthogonally diagonalizable.


By this we mean: there exist an *orthogonal* matrix $Q$ and a diagonal matrix $D$ for which

$$
   A = QDQ^{-1} = QDQ^T.
$$

Conversely, every orthogonally diagonalizable matrix is symmetric.

::::

So, for a symmetric matrix always  an orthonormal basis of eigenvectors exists.  For the inertia tensor of a 3D body such a basis corresponds to the (perpendicular) principle axes.


::::{prf:proof}  Of the converse of {prf:ref}`Thm:SymmetricMat:OrthogDiag`.

This is just a one line proof.   If  $A = QDQ^{-1} = QDQ^T$ 

then  $A^T = (QDQ^{-1} )^T = (Q^{-1} )^TD^TQ^T = (Q^T)^TD^TQ^T = QDQ^T = A$.

::::

The proof of the other implication we postpone 
till  {numref}`Subsection %s <SubSec:SymmetricMat:OrthogDiag>`. 


We end this introductory section with one representative example.



::::{prf:example} 
:label: Ex:SymmetricMat:OrthDiag2x2

Let $A$ be given by  $A = \begin{bmatrix} 1&2\\2&-2 \end{bmatrix}$.

The eigenvalues are found via

$$
 \det{(A - \lambda I)} = \begin{vmatrix} 1-\lambda&2\\2&-2-\lambda \end{vmatrix} 
   = (1-\lambda)(-2-\lambda) -4 =   \lambda^2 +\lambda -6 =  (\lambda-2)(\lambda+3) .
\nonumber
$$

They are  $\lambda_1 = 2$ and $\lambda_2 = -3$.

Corresponding eigenvectors are  $\mathbf{v}_1 = \begin{bmatrix} 2\\1 \end{bmatrix}$  for $\lambda_1$,  and 
$\mathbf{v}_2 = \begin{bmatrix} 1\\-2 \end{bmatrix}$.

The eigenvectors are orthogonal, 

$$
  \mathbf{v}_1 \ip \mathbf{v}_2 = \begin{bmatrix} 2\\1 \end{bmatrix}\ip \begin{bmatrix} 1\\-2 \end{bmatrix} = 2 - 2 = 0,   
$$

and $A$ can be diagonalized as

$$
   A = PDP^{-1} = \begin{bmatrix}2&1\\1&-2 \end{bmatrix}\begin{bmatrix}2 & 0\\0& -3 \end{bmatrix}
   \begin{bmatrix}2&1\\1&-2 \end{bmatrix}^{-1}.   
$$

Furthermore, if we normalize the eigenvectors, i.e., the columns of $P$, we find the following diagonalization of $A$ with an orthogonal matrix $Q$:

$$
 A = QDQ^{-1} = \begin{bmatrix}2/\sqrt{5}&1/\sqrt{5}\\1/\sqrt{5}&-2/\sqrt{5} \end{bmatrix}\begin{bmatrix}2 & 0\\0& -3 \end{bmatrix}
   \begin{bmatrix}2/\sqrt{5}&1/\sqrt{5}\\1/\sqrt{5}&-2/\sqrt{5} \end{bmatrix}^{-1}.
$$

::::

(SubSec:SymmetricMat:EssentialProp)=
## The essential properties of symmetric matrices 


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

::::{exercise}
:label: Exc:MatrixMat:uTAv

Prove the following slight generalization of {prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors`.

If $\vect{u}$ is an eigenvector of $A$ for the eigenvalue $\lambda$, and $\vect{v}$ is an eigenvector of $A^T$  for a different eigenvalue $\mu$,  then  $\vect{u} \perp \vect{v}$.

::::


Figure!

Here should come a moving picture with the biped starting with  $\mathbf{e}_1, \mathbf{e}_2$
rotating around the origin, and temporarily standing still when eigenvectors are met.



::::{prf:proposition} 
:label: Prop:SymmetricMat:RealEigenvalues


 
All eigenvalues of symmetric matrices are real.     

::::

The easiest proof is via complex numbers.  Skip it if you like.


::::{prf:proof} 



For two vectors $\mathbf{u},\mathbf{v}$ in $\C^n$   we consider the expression

$$
  \overline{\mathbf{u}}^{T}\mathbf{v} = \overline{u_1}v_1 + \ldots + \overline{u_n}v_n.
$$


If we take  $\mathbf{v}$  equal  to $\mathbf{u}$ we get

$$
  \overline{\mathbf{u}}^{T}\mathbf{u} = \overline{u_1}u_1 + \overline{u_2}u_2 + \ldots +  \overline{u_n}u_n =
                          |u_1|^2 + |u_2|^2 + \ldots + |u_n|^2.
$$

were $|u_i|$  denotes the modulus of the complex number $u_i$.  This sum of squares is
a non-negative real number. We also see that 
$\overline{\mathbf{u}}^{T}\mathbf{u} = 0$  only holds if $\mathbf{u} = \mathbf{0}$.


It can also be verified that

$$
  \overline{\overline{\mathbf{u}}^{T}\mathbf{v}} = \overline{\mathbf{v}}^T  \mathbf{u}.  
$$

Now suppose that  $\lambda$ is an eigenvalue of the symmetric matrix $A$, and  $\mathbf{v}$ is a nonzero (possible complex) eigenvector of $A$ for the eigenvalue $\lambda$.   Note that, since  $A$ is real and symmetric,  $\overline{{A}^T} = A^T = A$.
To prove that $\lambda$ is real, we will show that $\overline{\lambda} = \lambda$.

We  use kind of the same 'trick' as in {prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors`  Equation  {eq}`Eq:SymmetricMat:Av1v2`.
On the one hand 

$$
  \overline{(A \mathbf{v})^T} \mathbf{v} = \overline{\lambda\mathbf{v}^T} \mathbf{v} = 
 \overline{\lambda}  \overline{\mathbf{v}}^T \mathbf{v}.
$$

On the other hand, 

$$
 \overline{(A \mathbf{v})^T} \mathbf{v} = \overline{\mathbf{v}^T A^T}\mathbf{v} = \overline{\mathbf{v}^T} \overline{{A}^T} \mathbf{v}  = 
 \overline{\mathbf{v}}^T A\mathbf{v}  =  \overline{\mathbf{v}}^T  \lambda\mathbf{v}  = \lambda\overline{\mathbf{v}}^T \mathbf{v}.
$$

So we have that

$$
   \overline{\lambda}  \overline{\mathbf{v}}^T \mathbf{v} = \lambda\overline{\mathbf{v}}^T \mathbf{v}.
$$

Since we assumed that $\mathbf{v}$ is not the zero vector, we have that   $\overline{\mathbf{v}}^T \mathbf{v} \neq 0$ , and so it follows that  $ \overline{\lambda} =\lambda$. Which is equivalent to $\lambda$ being real.

::::


::::{prf:example} 


Let  $A = \begin{bmatrix} a&b\\b&d \end{bmatrix} $.  

Then the characteristic polynomial is computed as

$$
  \begin{vmatrix} a-\lambda&b\\b&d-\lambda \end{vmatrix} = 
  (a-\lambda)(d-\lambda) - b^2 = \lambda^2 - (a+d)\lambda + ad - b^2.
\nonumber 
$$

The discriminant of this second order polynomial is given by

$$
  D =  (a+d)^2 -4(ad -b^2) = a^2+d^2 - 2ad + 4b^2 = (a-d)^2 + 4b^2 \geq 0.
\nonumber 
$$

The discriminant is non-negative, so the characteristic polynomial has only real roots, and consequently the eigenvalues of the matrix are real.

Obviously, an elementary approach like this will soon get very complicated for larger $n \times n$ matrices.

::::
 

Lastly we come to the third of 'the big three' of symmetric matrices.

::::{prf:proposition} 
:label: Prop:SymmetricMat:AlgGeomMultiplicity

For each  eigenvalue of a symmetric matrix the geometric multiplicity is equal to the algebraic multiplicity.    

::::

The proof of this proposition we will  incorporate in the proof of the main theorem in 
{numref}`Subsection %s <SubSec:SymmetricMat:OrthogDiag>`. For now, we will look at a few examples.  


::::{prf:example} 


We will verify that the symmetric matrix $A = \begin{bmatrix} 1 & 0 & 1\\0 & 1  & 2 \\ 1 & 2 & 5 \end{bmatrix}$
is diagonalizable and has mutually orthogonal eigenvectors.

We first compute the characteristic polynomial.

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

So $A$ has the real eigenvalues  $\lambda_{1} = 1$,   $\lambda_2 = 6$  and $\lambda_3 = 0$.  Since all eigenvalues have algebraic multiplicity 1, the corresponding eigenvectors will give a basis of eigenvectors, and we can immediately conclude that $A$ is diagonalizable.

The eigenvectors are found to be

$$
   \mathbf{v}_1 = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix} \text{ for } \lambda_1 = 1, \quad
   \mathbf{v}_1 = \begin{bmatrix} 2 \\-1 \\ 0 \end{bmatrix} \text{ for } \lambda_2, \quad  
   \mathbf{v}_3 = \begin{bmatrix} 1 \\ 2 \\ 5 \end{bmatrix} \text{ for } \lambda_3. 
\nonumber
$$

We see:  the three eigenvectors form an orthogonal threesome, in accordance 
with {prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors`.

::::


::::{prf:example} 
:label: Ex:SymmetricMat:DoubleEV

Consider the matrix $A = \begin{bmatrix} 2&2&4\\2 & -1 & 2 \\ 4&2&2 \end{bmatrix}$. 

A  (rather involved) computation yields the eigenvalues   $\lambda_{1,2} = -2$ and $\lambda_3 = 7$.
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
The other eigenvalue has algebraic multiplicity 1, so its geometric  multiplicity has to be 1 as well. With this {prf:ref}`Prop:SymmetricMat:AlgGeomMultiplicity` is verified.

Lastly we leave it to you to check that an eigenvector for $\lambda_3 = 7$ is given by $\mathbf{v}_3 = \begin{bmatrix} 2 \\ 1 \\ 2\end{bmatrix}$.  And that  both  $\mathbf{v}_3 \perp \mathbf{v}_1$  and  $\mathbf{v}_3 \perp \mathbf{v}_2$, so that {prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors` is satisfied as well.
::::


(SubSec:SymmetricMat:OrthogDiag)=  
## Orthogonal Diagonalizability of Symmetric Matrices  


Let us restate the main theorem about symmetric matrices.

::::{prf:theorem} 
:label: Thm:SymmetricMat:OrthogDiag2
 
A matrix $A$ is symmetric if and only if it is orthogonally diagonalizable.

::::

Note that this also establishes the property that for each eigenvalue of a symmetric matrix 
the geometric muliplicity equals the algebraic multiplicity 
({prf:ref}`Prop:SymmetricMat:OrthogonalEigenvectors`).



We will put the intricate proof at the end, and consider two  examples first.

The first example is a continuation of the earlier  {prf:ref}`Ex:SymmetricMat:DoubleEV`.

::::{prf:example}
:label: Ex:SymmetricMat:OrthogDiag3x3

The matrix $A = \begin{bmatrix} 2&2&4\\2 & -1 & 2 \\ 4&2&2 \end{bmatrix}$ was shown to have the eigenvalues/eigenvectors

$$
  \lambda_{1,2} = -2, \quad \mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \\ -1\end{bmatrix}, \, 
  \mathbf{v}_2 = \begin{bmatrix} 1 \\ -2 \\ 0\end{bmatrix},
  \quad \lambda_3 = 7, \quad \mathbf{v}_3 = \begin{bmatrix} 2 \\ 1 \\ 2\end{bmatrix}.
$$


The pairs  $\mathbf{v}_1, \mathbf{v}_3$  and   $\mathbf{v}_2, \mathbf{v}_3$ are 'automatically' orthogonal.

For the eigenspace  $E_{-2} = \Span{\mathbf{v}_1, \mathbf{v}_2}$  we can use Gram-Schmidt to get an orthogonal basis:

$$
  \mathbf{u}_1 = \mathbf{v}_1, \quad \mathbf{u}_2 = 
         \mathbf{v}_2 - \dfrac{\mathbf{v}_2 \ip \mathbf{u}_1}{\mathbf{u}_1 \ip \mathbf{u}_1} \mathbf{u}_1 
         = \dfrac12\begin{bmatrix} 1 \\ -4 \\ 1\end{bmatrix}
$$

Normalizing the orthogonal basis $\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{v}_3\}$  and putting them side by side in a matrix yields the orthogonal matrix

$$
  Q = \begin{bmatrix} \dfrac{1}{\sqrt{2}} & \dfrac{1}{\sqrt{18}} & \dfrac{2}{3} \\ 
  0 & \dfrac{-4}{\sqrt{18}} & \dfrac{-1}{3}\\ \dfrac{-1}{\sqrt{2}} &  \dfrac{1}{\sqrt{18}} & \dfrac{2}{3}
  \end{bmatrix}.
$$

The conclusion becomes that

$$
 A = QDQ^{-1} = QDQ^T, \quad \text{where still}  \,\,\, D = \begin{bmatrix} -2 & 0 & 0 \\ 0 & -2 & 0 \\ 0 & 0 & 7\end{bmatrix}.
$$
::::


One more example before we get to the proof (or you jump over to {numref}`SubSec:SymmetricMat:SpectralDecomp`).

::::{prf:example}
:label: Ex:SymmetricMat:OrthogDiag3x3bis
 
Let the symmetric matrix $A$  be given by  $     A = \begin{bmatrix} 
     1 & 2 & 2 & 0 \\ 2 & -1 & 2 & 0 \\ 2 & 0 & -1 & -2 \\ 0 & 2 & -2 & 1
    \end{bmatrix}$.

The hard part is to find the eigenvalues.  (I.e., how to solve an equation of the order four?!)
Once we know what the eigenvalues are, the other steps are 'routine'.

It appears that $A$ has the double eigenvalues $\lambda_{1,2} = 3$ and  $\lambda_{3,4} = -3$.

To find the eigenvectors for  the eigenvalue 3 we row reduce the  matrix $(A - 3I)$.

$$
\left[\begin{array}{cccc}1-3 & 2 & 2 & 0\\ 2 & -1-3 & 2 & 0 \\ 2 & 0 & -1-3 & -2 \\ 0 & 2 & -2 & 1-3  \end{array} \right]  \sim 
\left[\begin{array}{cccc}1 & 0 & -2 & -1\\ 0 & 1 & -1 & -1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0  \end{array} \right].  
$$

We can read off two linearly independent eigenvectors

$$
\vect{v}_1 = \left[\begin{array}{c} 2 \\ 1 \\ 1 \\ 0  \end{array} \right], \quad 
\vect{v}_2 = \left[\begin{array}{c} 1 \\ 1 \\ 0 \\ 1  \end{array} \right].  
$$

As in {prf:ref}`Ex:SymmetricMat:OrthogDiag3x3` we can construct an orthogonal basis for the eigenspace $E_{3}$:

$$
  \mathbf{u}_1 = \mathbf{v}_1, \quad \mathbf{u}_2 = 
         \mathbf{v}_2 - \dfrac{\mathbf{v}_2 \ip \mathbf{u}_1}{\mathbf{u}_1 \ip \mathbf{u}_1} \mathbf{u}_1 
         = \dfrac12\begin{bmatrix} 0 \\ 1 \\ -1\\ 1\end{bmatrix}
$$

Changing the order of  $\vect{v}_1, \vect{v}_2$  before applying Gram-Schmidt would give the slightly simpler basis

$$
  \mathbf{u}_1 = \mathbf{v}_2 = \begin{bmatrix} 1 \\ 1 \\ 0\\ 1\end{bmatrix}, \quad \mathbf{u}_2 = 
         \mathbf{v}_2 - \dfrac{\mathbf{v}_2 \ip \mathbf{u}_1}{\mathbf{u}_1 \ip \mathbf{u}_1} \mathbf{u}_1 
         = \dfrac12\begin{bmatrix} 1 \\ 0 \\ 1\\ -1\end{bmatrix}
$$


Likewise we can first find a 'natural' basis for the eigenspace  $E_{-3}$ by row reducing  $(A - (-3I))$:

$$
\left[\begin{array}{cccc}1+3 & 2 & 2 & 0\\ 2 & -1+3 & 2 & 0 \\ 2 & 0 & -1+3 & -2 \\ 0 & 2 & -2 & 1+3  \end{array} \right] \quad  \sim 
\left[\begin{array}{cccc}1 & 0 & 1 & -1\\ 0 & 1 & -1 & 2 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0  \end{array} \right].  
$$

Two independent eigenvectors:   $\vect{v}_3 = \left[\begin{array}{c} -1 \\ 1 \\ 1 \\ 0  \end{array} \right]$ and $\vect{v}_4 = \left[\begin{array}{c} 1 \\ -2 \\ 0 \\ 1  \end{array} \right]$.

Again these can be orthogonalized, and then we find the following complete set of  of eigenvectors, i.e., a basis for $\R^4$:

$$
  \vect{u}_1 = \begin{bmatrix} 1 \\ 1 \\ 0\\ 1\end{bmatrix}, \quad
  \vect{u}_2 = \begin{bmatrix} 1 \\ 0 \\ 1\\ -1\end{bmatrix}, \quad
  \vect{u}_3 = \begin{bmatrix} -1 \\ 1 \\ 1\\ 0\end{bmatrix}, \quad
  \vect{u}_4 = \begin{bmatrix} 0 \\ -1 \\ 1 \\ 1\end{bmatrix}.
$$

We conclude that $A = QDQ^{-1}$,  where

$$
    D = \left[\begin{array}{cccc}3 & 0 & 0 & 0\\ 0 & 3 & 0 & 0 \\ 0 & 0 & -3 & 0 \\ 0 & 0 & 0 & -3  \end{array} \right], \quad
   Q = \dfrac{1}{\sqrt{3}} \left[\begin{array}{cccc}1 & 1 & -1 & 0\\ 
                                                    1 & 0 & 1 & -1 \\ 
                                                    0 & 1 & 1 & 1 \\ 
                                                    1 & -1 & 0 & 1  \end{array} \right].
$$

::::

And now it's time for the proof of the main theorem. 

::::{prf:proof}   Of {prf:ref}`Thm:SymmetricMat:OrthogDiag`
 

Suppose that $A$ is a symmetric $n \times n$  matrix.  We know there are $n$ real eigenvalues
$\lambda_1, \lambda_2, \ldots, \lambda_n$. 
Suppose  $\vect{q}_1$ is an eigenvector for $\lambda_1$ with unit length.
We can extend  $\{\vect{q}_1\}$ to an orthonormal basis  $(\vect{q}_1,\vect{q}_2,\ldots,\vect{q}_n)$.
Let $Q_1$ be the matrix with the columns $\vect{q}_1,\vect{q}_2,\ldots,\vect{q}_n$.

It can be shown that  $A_1 = Q_1^{-1}AQ_1 = Q_1^TAQ_1$  is of the form

$$
   \left[\begin{array}{cccc} \lambda_1 & 0   & \ldots & 0 &0 \\ 
    0 &   \\
     \vdots   & & B_1 & & \\ 
    0 & 
   \end{array}\right]
$$

where  $B_1$ is an  $(n-1)\times(n-1)$ matrix that is also symmetric.  

Namely,   the first  column  of  $A_1$  can be computed as

$$
  A_1\vect{e}_1 = Q_1^{-1}AQ_1\vect{e}_1 = Q_1^{-1}A\vect{q}_1 = Q_1^{-1}\lambda_1\vect{q}_1 = 
     \lambda_1Q_1^{-1}\vect{q}_1
$$

and $Q_1^{-1}\vect{q}_1$ is the first column of  $Q_1^{-1}Q_1$, which is $\vect{e}_1$.

This shows that the first column of $A_1$ must indeed be  $\lambda_1\vect{e}_1 = \left[\begin{array}{c}
\lambda_1 \\ 0 \\ \vdots \\ 0 \end{array}\right]$.

Since  $A$ is symmetric and $Q_1$ is by construction an orthogonal matrix,

$$
   A_1^T = (Q_1^{T}AQ_1)^T = Q_1^T A^T (Q_1^T)^T = Q_1^{T}AQ_1 = A_1.
$$

So $A_1$  is also symmetric.  Thus if the first column of $A_1$ contains  $n-1$ zeros, so does its first row.



Since  $A$ and $A_1$ are similar,  they have the same eigenvalues.
It follows that $B_1$ has the eigenvalues $\lambda_2, \ldots, \lambda_n$.

We can apply the same construction to  $B_1$, yielding 

$$
   B_2 = (\tilde{Q}_2)^{-1}B_1\tilde{Q}_2
   =    \left[\begin{array}{cccc} \lambda_2 & 0   & \ldots & 0 &0 \\ 
    0 &   \\
     \vdots   & & \tilde{B}_2 & & \\ 
    0 & 
   \end{array}\right].
$$
  
Note that in this formula the matrices have size $(n-1)$  by $(n-1)$.

If we then define  

$$
   Q_2 = 
    \left[\begin{array}{cccc} 1 & 0   & \ldots & 0 &0 \\ 
    0 &   \\
     \vdots   & & \tilde{Q}_2 & & \\ 
    0 & 
   \end{array}\right]
   
$$


it follows that

$$
  A_2 = Q_2^{-1}A_1Q_2 = 
  \left[\begin{array}{ccccccc} 
    \lambda_1 &      0    & 0  & \ldots & 0 &0 \\ 
       0      & \lambda_2 & 0  & \ldots & 0 &0 \\ 
       0      &  0  \\
    \vdots & \vdots & & \tilde{B_2}  \\
    0 & 0 &   
   \end{array}\right].
$$

Continuing in this fashion we find 

$$
  A_{n-1} = Q_{n-1}^{-1} \cdots Q_2^{-1}Q_1^{-1}A Q_1  Q_2 \cdots Q_{n-1} =
  \left[\begin{array}{ccccc} 
    \lambda_1 &      0    & 0  & \ldots &0 \\ 
       0      & \lambda_2 & 0  &\ldots &0 \\ 
     \vdots & & \ddots &  & \vdots\\
     \vdots & &  & \ddots & \vdots\\
     0 & 0 &  \ldots & 0 &\lambda_n
   \end{array}\right].

$$

This proves that $A$ is diagonalizable, with  $Q = Q_1Q_2 \cdots Q_{n-1}$  as a diagonalizing matrix.

Moreover,  since the product of orthogonal matrices is orthogonal, $A$ is in fact orthogonally diagonalizable.

::::


:::{prf:example}
:label: Ex:SymmetricMat:ConstructDiag

We will illustrate the proof for the matrix 

$$
    A = \begin{bmatrix} 
     1 & 2 & 2 & 0 \\ 2 & -1 & 0 & 2 \\ 2 & 0 & -1 & -2 \\ 0 & 2 & -2 & 1
    \end{bmatrix}.
$$

Since

$$
    \begin{bmatrix} 
     1 & 2 & 2 & 0 \\ 2 & -1 & 0 & 2 \\ 2 & 0 & -1 & -2 \\ 0 & 2 & -2 & 1
    \end{bmatrix} 
    \begin{bmatrix} 
     1 \\-1\\-1\\0
    \end{bmatrix} = 
    \begin{bmatrix} 
     -3 \\3\\3\\0
    \end{bmatrix}
$$

we have as a starter the eigenvalue and corresponding eigenvector 

$$
  \lambda_1 = -3, \quad \vect{v}_1 = \begin{bmatrix}  1 \\-1\\-1\\0   \end{bmatrix}.
$$

An orthogonal basis for  $\mathbb{R}^4$, starting with this first eigenvector is, for instance

$$
   \vect{v}_1 = \begin{bmatrix}  1 \\-1\\-1\\0   \end{bmatrix}, \quad
   \vect{v}_2 = \begin{bmatrix}  1 \\1\\0\\0   \end{bmatrix}, \quad
   \vect{v}_3 = \begin{bmatrix}  1 \\-1\\2\\0   \end{bmatrix}, \quad
   \vect{v}_4 = \begin{bmatrix}  0\\0\\0\\1   \end{bmatrix}. \quad
$$

Rescaling and putting them into a matrix yields

$$
    Q_1 = \begin{bmatrix}  
             1/\sqrt{3} & 1/\sqrt{2} & 1/\sqrt{6} & 0 \\
             -1/\sqrt{3} & 1/\sqrt{2} & -1/\sqrt{6} & 0 \\
             -1/\sqrt{3} & 0 & 2/\sqrt{6} & 0 \\
             0 & 0 & 0 & 1    
        \end{bmatrix}
$$

Next we compute  

$$
   A_1 = Q_1^{-1}AQ_1 = Q_1^TAQ_1 = \begin{bmatrix}  
             -3 &  0 & 0 & 0 \\
             0 & 2 & \sqrt{3} & \sqrt{2} \\
             0 & \sqrt{3} & 0  & -\sqrt{6} \\
             0 & \sqrt{2} & -\sqrt{6} & 1    
        \end{bmatrix}.
$$

This is indeed of the form stated in the proof. 

We continue with the matrix  $B_1 = \left[\begin{array}{ccc}
                  2 & \sqrt{3} & \sqrt{2} \\ 
                  \sqrt{3} & 0  & -\sqrt{6} \\
                  \sqrt{2} & -\sqrt{6} & 1
                  \end{array}   \right]$.

$B_1$  has eigenvalue $-3$ with eigenvector  $\vect{u}_1 = \left[\begin{array}{c}
                                            1 \\   -\sqrt{3} \\ -\sqrt{2}  
                                            \end{array}   \right]$.


Again we extend to an orthogonal basis for $\mathbb{R}^3$.  For instance,

$$
    \vect{u}_1, \quad \vect{u}_2 = \left[\begin{array}{c}
                                            \sqrt{2} \\   0\\ 1 
                                    \end{array}   \right], \quad 
                      \vect{u}_3 = \left[\begin{array}{c}
                                            1 \\ \sqrt{3} \\  -\sqrt{2} 
                                    \end{array}   \right].
$$

If we normalize and use them as the columns of $\tilde{Q}_2$ as in the proof, we find as second matrix in that construction

$$

   Q_2 = \left[\begin{array}{cccc} 1 & 0 & 0 & 0 \\
                  0 & \dfrac{1}{\sqrt{6}} &  \dfrac{\sqrt{2}}{\sqrt{3}} & -\dfrac{1}{\sqrt{6}} \\
                  0 & \dfrac{-1}{\sqrt{2}} &  0 & \dfrac{1}{\sqrt{2}} \\
                  0 & \dfrac{1}{\sqrt{3}} &  \dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{3}}
                                    \end{array}   \right].
                                    
$$

And then

$$
   A_2 = Q_2^TQ_1^T A Q_1Q_2 = \left[\begin{array}{cccc} -3 & 0 & 0 & 0 \\
       0 & -3 & 0 & 0 \\ 0 & 0 & 3 & 0\\ 0 & 0 & 0 & 3
                                    \end{array}   \right] = D!
$$

For this example  the matrix has the second double eigenvalue $\lambda_{3,4} = 3$.  Because of that, the construction takes one step less than in the general case.  
Defining  $Q = Q_1Q_2$, we see that 

$$
  Q^{-1}AQ = D, \,\,\text{ so }\,\,
  A = QDQ^{-1} = QDQ^T  
$$

for the matrix  $Q = Q_1Q_2$, which is the matrix


$$
  Q =  \left[\begin{array}{cccc} \dfrac{1}{\sqrt{3}} & 0 & \dfrac{1}{\sqrt{3}} & \dfrac{1}{\sqrt{3}} \\
                 -\dfrac{1}{\sqrt{3}} & \dfrac{1}{\sqrt{3}} & \dfrac{1}{\sqrt{3}} & 0 \\ 
                 -\dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{3}} & 0 & \dfrac{1}{\sqrt{3}} \\ 
                 0 & -\dfrac{1}{\sqrt{3}} & \dfrac{1}{\sqrt{3}} & -\dfrac{1}{\sqrt{3}}
                                    \end{array}   \right] =
        \dfrac{1}{\sqrt{3}}\left[\begin{array}{cccc} 1 & 0 & 1 & 1 \\
                 -1 & 1 & 1 & 0 \\ -1 & -1 & 0 & 1 \\ 0 & -1 & 1 & -1
                                    \end{array}   \right].                            
$$

So we see  that $A$ has the 'simpler' eigenvectors

$$
  \vect{v}_1 = \left[\begin{array}{c} 1 \\ -1 \\ -1 \\ 0
                                    \end{array}   \right], \quad
  \vect{v}_2 = \left[\begin{array}{c} 0 \\ 1 \\ -1 \\ -1 
                                    \end{array}   \right], \quad
  \vect{v}_3 = \left[\begin{array}{c} 1 \\ 1 \\ 0 \\ 1
                                    \end{array}   \right], \quad
  \vect{v}_4 = \left[\begin{array}{c} 1 \\ 0 \\ 1 \\ -1
                                    \end{array}   \right].
$$

Note:  given the eigenvalues, these eigenvectors could have been found more efficiently by solving the systems
$(A - \lambda_iI)\vect{x} = \vect{0}$, and then orthogonalize by the Gram-Schmidt procedure. As is done in 
{prf:ref}`Ex:SymmetricMat:OrthogDiag3x3`.

The importance of the step-by-step reduction is that it shows that from the 'minimal' assumptions of symmetry and the existence of real eigenvalues it is possible to create an orthogonal diagonalization.

:::



  


In the last subsection we will show how the orthogonal diagonalization can be rewritten in an interesting and meaningful way.

(SubSec:SymmetricMat:SpectralDecomp)=
## The Spectral Decomposition of a Symmetric Matrix.

Let's take up an earlier example  ({prf:ref}`Ex:SymmetricMat:OrthDiag2x2`) to illustrate what the spectral decomposition is about.

::::{prf:example}
:label: Ex:SymmetricMat:SpectralDecomp

For the matrix  $A = \begin{bmatrix} 1&2\\2&-2 \end{bmatrix}$    we found the orthogonal diagonalization

$$
 A = QDQ^T = \begin{bmatrix} 2/\sqrt{5}& 1/\sqrt{5}\\1/\sqrt{5}& -2/\sqrt{5} \end{bmatrix}
             \begin{bmatrix} 2 & 0 \\ 0 & -3 \end{bmatrix}
             \begin{bmatrix} 2/\sqrt{5}& 1/\sqrt{5}\\1/\sqrt{5}& -2/\sqrt{5} \end{bmatrix}^T.
$$

This is of the form

$$
  \begin{array}{rcl}
  A &=& [\,\mathbf{q}_1\,\mathbf{q}_2\,]\begin{bmatrix} 2 & 0 \\ 0 & -3 \end{bmatrix}
             [\,\mathbf{q}_1\,\mathbf{q}_2\,]^T =
     [\,2\mathbf{q}_1\,(-3)\mathbf{q}_2]\begin{bmatrix}\mathbf{q}_1^T \\ \mathbf{q}_2^T  \end{bmatrix}.   
     \end{array}
$$

We bring in mind the column-row expansion of the matrix product. For two  $2\times 2$ matrices this reads

$$
 \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}
 \begin{bmatrix} b_{11} &b_{12} \\ b_{21} & b_{22} \end{bmatrix} =
 \begin{bmatrix} a_{11} \\ a_{21} \end{bmatrix}
 \begin{bmatrix} b_{11} &b_{12}  \end{bmatrix}  + 
 \begin{bmatrix} a_{12} \\ a_{22} \end{bmatrix}
 \begin{bmatrix} b_{21} &b_{22}  \end{bmatrix}.
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

Exactly as in {prf:ref}`Ex:SymmetricMat:SpectralDecomp` we can use the column-row expansion of the matrix product  to derive

$$
A =  \lambda_1 \mathbf{q}_1\mathbf{q}_1^T + \lambda_2\mathbf{q}_2\mathbf{q}_2^T + \ldots + \lambda_n\mathbf{q}_n\mathbf{q}_n^T,
$$

where  the vectors  $\mathbf{q}_i$  of course are the (orthonormal) columns of the diagonalizing matrix $Q$. This is indeed a linear combination of orthogonal projections, as was to be shown.
::::

[to the reviewers] Also include a remark about the non-uniqueness and a way to make it unique by aggregating the projections corresponding to the same eigenvalue?

::::{exercise}

The eigenvalues of the matrix $A=\begin{bmatrix} 2 & 1 & 0 \\ 1 & 3 &  1\\ 0 & 1& 2 \end{bmatrix}$ are 1, 2 and 4. 

Find the spectral decomposition of   $A$.
::::