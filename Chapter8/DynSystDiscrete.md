(Sec:DynSystDiscrete)=
# Discrete Dynamical Systems

## Introduction

Lesley Matrices  and  Markov Matrices

## The case where $A$ is diagonalizable

If the matrix $A$ is diagonalizable the behaviour of the dynamical system can be made completely transparent.

::::{prf:proposition}
:label: Prop:DynSystDiscrete:DiagCase

Suppose  $A$ is an $n\times n$ diagonalizable matrix.
Let $(\vect{v}_1, \ldots, \vect{v}_n)$ be a basis of eigenvectors, and let 
$\lambda_1, \ldots, \lambda_n$ be the corresponding eigenvalues.

Then the behaviour of the dynamical system 

$$
  \vect{x}_{0} = \vect{s}, \quad  \vect{x}_{k+1} = A\vect{x}_k, \quad k = 0,1,2,\ldots
$$

is as follows.


If    

:::{math}
:label: Eq:DynSystDiscrete:InitCoords

 \vect{s} =  c_1\vect{v}_1 + c_2\vect{v}_2 +  \ldots + c_n\vect{v}_n,
:::

then

:::{math}
:label: Eq:DynSystDiscrete:GenSolDiagble

 \vect{x}_k =  c_1\lambda_1^k\vect{v}_1 + c_2\lambda_2^k\vect{v}_2 +  \ldots + c_n\lambda_n^k\vect{v}_n.

:::

The last expression for  $\vect{x}_k$ is often refered to as being the **general solution** of the dynamical system.

::::

Note that the coordinates  $c_1,c_2,\ldots,c_n$  in {eq}`Eq:DynSystDiscrete:InitCoords` are uniquely determined, since $(\vect{v}_1, \ldots, \vect{v}_n)$ is assumed to be a basis.


::::{prf:proof}

There is nothing much to prove.

The vectors $\vect{v}_i$  being eigenvectors for the corresponding $\lambda_i$ means that

$$
  A\vect{v}_i = \lambda_i\vect{v}_i.
$$

Thus

$$
  A^2\vect{v}_i = A(A\vect{v}_i) = A(\lambda_i\vect{v}_i) = \lambda_iA\vect{v}_i 
  =  \lambda_i^2\vect{v}_i,
$$

and in general

$$
    A^k\vect{v}_i  =  \lambda_i^k\vect{v}_i, \quad  k = 1,2,\ldots
$$

By properties of the matrix product it readily follows that

$$
   \begin{array}{rcl}
     \vect{x}_k = A^k\vect{s} &=& A^{k}(c_1\vect{v}_1 + \ldots + c_n\vect{v}_n)  \\
     & = & c_1A^{k}\vect{v}_1 + \ldots + c_nA^{k}\vect{v}_n \\
     & = & c_1\lambda_1^{k}\vect{v}_1 + \ldots + c_n\lambda_n^{k}\vect{v}_n.
     \end{array}
$$

::::

From Equation {eq}`Eq:DynSystDiscrete:GenSolDiagble` it follows that if **all** eigenvalues have an absolute value smaller than 1, **all** solutions will approach the origin $\vect{0}$ if  $k \to \infty$.  In this case the origin is called (asymptotically) stable.  

::::{prf:definition}
:label: Def:DynSystDiscrete:Stable

Let $A$ be the matrix of a dynamical system. 
The origin is called **asymptotically stable**  if all solutions $\vect{x}_k$  go to $\vect{0}$ if $k \to \infty$.  If for some starting values $\vect{x}_0 \ \vect{s}$ the solution $\vect{x}_k$ becomes arbitrarily large, i.e., if $\norm{\vect{x}_k} \to \infty$ for $k \to \infty$, then the dynamical system is called **unstable**. In the borderline case where the highest absolute value of the eigenvalues is exactly 1, the origin is just called **stable**.

In the literature there is  quite a bit of terminology to describe the behaviour
of dynamical systems. 
In the case of asymptotic stability will call the origin an **attractor**, in the of instability we say the origin is a **repeller**.  
::::

::::{prf:remark}

This definition of stable and unstable suffices for *linear* dynamical systems.  For nonlinear systems a more subtle definition is needed. 

::::

The following proposition is an almost immediate consequence of Equation {eq}`Eq:DynSystDiscrete:GenSolDiagble`. 

::::{prf:proposition}

Suppose the matrix $A$ is diagonalizable, with eigenvalues $\lambda_i$ ordered by absolute value,

$$
   |\lambda_1| \geq |\lambda_2| \geq \ldots \geq |\lambda_n|.
$$

Then

<ol type ="i">

<li>

  If  $|\lambda_1| < 1$  the origin is asymptotically stable.

</li>

<li>

  If  $|\lambda_1| > 1$  the origin is unstable.
  
</li>

<li>

  If  $|\lambda_1| = 1$  the origin is stable but not asymptotically stable.
  
</li>

</ul>
::::

::::{prf:remark}

 The same conclusions may be drawn in the case of multiple eigenvalues or complex eigenvalues.  For  complex eigenvalues $|\lambda_i|$ then denotes the modulus of the number $\lambda_i$. 

 The argument in this more general situation becomes more involved, as we cannot use   Equation {eq}`Eq:DynSystDiscrete:GenSolDiagble` anymore.
::::


## The matrix $A$ has a complex eigenvalue
