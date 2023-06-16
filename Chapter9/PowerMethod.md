(Sec:PowerMethod)=
# The Power Method

The eigenvalues of an $n\times n$  matrix $A$ to a large extent characterize the matrix.  In theory they can be found as the zeros of the characteristic polynomial.  Already for $n \geq 3$  it is not an easy matter to find the exact zeros, and for $n\geq 5$ it is close to impossible. 
One way to go about is to use a numerical method to solve an  equation of degree $n$. The power method often provides at least  the eigenvalue of the largest absolute value (or, modulus).  This is in fact the most important eigenvalue concerning the stability or instability of the linear dynamical system connected to $A$.

## The basics


The idea behind the power method is really very simple.
Let us for the moment consider the case where the matrix $A$ is diagonalizable.  

The power method is based on the dynamical system

$$
    \vect{x}_0 = \vect{s}, \quad \vect{x}_{k+1} = A\vect{x}_k,\,\,  k = 1,2,3,\ldots
$$

We know from {prf:ref}`Prop:DynSystDiscrete:DiagCase`   in  {numref}`Sec:DynSystDiscrete` that for a diagonalizable matrix $A$ with eigenvalues
$\lambda_1, \ldots, \lambda_n$,  the $k$-th vector in the process is given by

::::{math}
:label: Eq:PowerMethod:GenSol

  \vect{x}_k =  c_1\lambda_1^k\vect{v}_1 + c_2\lambda_2^k\vect{v}_2 +  \ldots + c_n\lambda_n^k\vect{v}_n
::::


where  $\vect{v}_1, \ldots, \vect{v}_n$ are corresponding eigenvectors. <BR>
Now suppose the eigenvalues are ordered according to 

$$
  |\lambda_1| \geq |\lambda_2| \geq \,\,\ldots\,\,\geq |\lambda_n|
$$

and that in fact we have  $|\lambda_1| > |\lambda_2|$,  i.e. the first inequality is strict.  <BR>
We can rewrite Equation {eq}`Eq:PowerMethod:GenSol` as 

::::{math}
:label: Eq:PowerMethod:GenSol-2

  \vect{x}_k =  \lambda_1^k\left(c_1\vect{v}_1 + c_2(\lambda_2/\lambda_1)^k\vect{v}_2 +  \ldots + c_n(\lambda_n/\lambda_1)^k\vect{v}_n\right).
::::

If the coefficient  $c_1$ is not equal to zero, 
then since all  factors $(\lambda_n/\lambda_1)^k$  will go to zero for $k \to \infty$,   in the long run   $\vect{x}_k$  will behave  as  

$$
   c_1(\lambda_1)^k\vect{v}_1.
$$

That is $\vect{x}_k$ is  'almost' an eigenvector.
A minor complication:  if $|\lambda_1| > 1$,  $\vect{x}_k$ will 'go to infinity' and $|\lambda_1| < 1$,  $\vect{x}_k$ will 'go to zero'.  This complication is overcome by a proper rescaling.

We put a name to the situation where a matrix $A$ has a single eigenvalue of highest absolute value.

::::{prf:definition}
:label:  Def:PowerMethod:DominantEigenvalue

Suppose the $n\times n$ matrix $A$ has the eigenvalues $\lambda_1, \ldots, \lambda_n$  ordered according to 

$$
  |\lambda_1| \geq |\lambda_2| \geq \,\,\ldots\,\,\geq |\lambda_n|.
$$

If in fact  $|\lambda_1| > |\lambda_2|$, then $\lambda_1$ is called the **dominant eigenvalue** of $A$.<BR>
An eigenvector corresponding to $\lambda_1$ is called a **dominant eigenvector**.
::::

Consider the following algorithm.

::::{prf:algorithm}
:label: Alg:PowerMethod:PowMed

Suppose $A$ is an $n\times n$ matrix.

<u>Step 1</u>  &nbsp; Choose an arbitrary nonzero vector  $\vect{x}$ in $\R^n$.

<u>Step 2</u>  &nbsp; Repeat the following steps: <BR>
&nbsp; --- Compute  $\vect{y} = A\vect{x}$;<BR>
&nbsp; --- Find the entry $\mu$ of $\vect{y}$   of the highest absolute value; <BR>
&nbsp; --- Replace  $\vect{x}$  by $\dfrac{1}{\mu}\vect{y}$.

Until the process more or less stabilizes.  For instance,  until the difference between the last two computed vectors is smaller that a pre-determined 'error' $\varepsilon$. 

::::


::::{prf:remark}
:label: Rem:Powermethod:Algorithm 

Instead of storing of the whole sequence  

$$

\vect{x}_1=A\vect{x}_0,\,\,\vect{x}_2 = A\vect{x}_1,\,\,\vect{x}_3=A\vect{x}_2,\,\ldots,

$$ 

the algorithm discards all intermediate iterates.<BR>  
We are only interested in the last iterate anyway, since we expect this to be the best approximation of an eigenvector. 

The scaling step is necessary to avoid ending up at the zero vector or 'at infinity',  where all information is lost.

::::


::::{prf:proposition} 
:label: Prop:Powermethod:Powermed



Suppose  $A$ is a diagonalizable matrix $A$ with dominant eigenvalue $\lambda_1$. <BR>
Then in general the sequence constructed by the Power Method Algorithm, will converge to an eigenvector $\vect{v}_1$ for $\lambda_1$.  <BR> 
To be more specific,  the sequence $\vect{x}_k$ will converge a dominant eigenvector $\vect{v}_1$ if  the initial  vector $\vect{x}_0$ does not lie in 
$\text{Span}\{\vect{v}_2, \vect{v}_3, \ldots, \vect{v}_n\}$.

If $\vect{x}$ is the result after a (sufficiently) large number of runs of the algorithm, <BR>
(an approximation of) the dominant eigenvalue is the entry with the highest absolute value of the vector  $\vect{y} = A\vect{x}$.


::::

::::{prf:proof}

With the scalings we consider in fact the dynamical process

$$
   \vect{x}_0 = \vect{s}, \quad \vect{x}_{k+1} = \frac{1}{\mu_k} A\vect{x}_k.
$$

This process yields a sequence of vectors with the same directions as the
vectors of the process

$$
  \vect{x}_0 = \vect{s}, \quad \vect{x}_{k+1} =  A\vect{x}_k.
$$

And we know that under the assumptions of a dominant eigenvalue $\lambda_1$ and a initial vector 

$$
   \vect{x}_0 = c_1\vect{v}_1 + c_2\vect{v}_2 +  \ldots + c_n\vect{v}_n, \quad c_1 \neq 0
$$
the  vectors  $\vect{x}_k$ in the long run behaves as $c_1\lambda_1^k\vect{v}_1$. <BR>
The effect of the scalings is that all along the way we keep vectors with largest entry 1. Thus the scaled process will converge to the dominant eigenvector with largest entry 1.

::::


::::{prf:example}
:label:  Ex:PowerMethod:FirstExample

Let  $A$ be the matrix  &nbsp;  $\begin{bmatrix}5 & 2 \\ 2 & 8 \end{bmatrix}$. <BR>
The matrix is symmetric, hence diagonalizable. Its eigenvalues are $\lambda_1 = 9$, $\lambda_2 = 4$.

If we start the process of  {prf:ref}`Alg:PowerMethod:PowMed`  from the initial vector  

$$
  \vect{x}_0 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}
$$

up to 5 decimals we find the following results


$$
  \vect{y}_1 = \begin{bmatrix} 7 \\ 10 \end{bmatrix}, \quad
  \vect{x}_1 = \begin{bmatrix} 0.7 \\ 1 \end{bmatrix},  \quad
  \vect{x}_2 = \begin{bmatrix} 0.5851 \\ 1 \end{bmatrix},  
$$

$$
  \vect{x}_3 = \begin{bmatrix} 0.5371 \\ 1 \end{bmatrix},  \quad
  \vect{x}_4 = \begin{bmatrix} 0.5164 \\ 1 \end{bmatrix},\,\,\, \ldots ,\,\,\,
  \vect{x}_{10} = \begin{bmatrix} 0.5001 \\ 1 \end{bmatrix}.
$$

The last vector is almost equal to 

$$
  \vect{v}_1 = \begin{bmatrix} 0.5 \\ 1 \end{bmatrix}, 
$$ 

which is the dominant eigenvector with largest entry 1. <BR>
For this specific example the 'convergence to an eigenvector' goes very quickly!

Two circumstances help this rapid convergence.
First of all, and most importantly,  the *ratio* $\lambda_2/\lambda_1$ of the two eigenvalues plays a role.  Second, the 'arbitrarily' chosen initial vector does have a substantial component in the direction of the eigenvector for the largest eigenvalue.

For the given matrix $A$ this can be analysed in detail. A complete set of  eigenvalues and eigenvectors is given by

$$
  \lambda_1 = 9,\,\,\vect{v}_1 = \begin{bmatrix} 1 \\ 2 \end{bmatrix}, \quad
  \lambda_1 = 4,\,\,\vect{v}_2 = \begin{bmatrix} 2 \\ -1 \end{bmatrix}.
$$

At the start we have

$$
   \vect{x}_0 = \begin{bmatrix} 1 \\ 1 \end{bmatrix} = 
   c_1\begin{bmatrix} 1 \\ 2 \end{bmatrix} + c_2\begin{bmatrix} 2 \\ -1 \end{bmatrix} = 
   \frac35\begin{bmatrix} 1 \\ 2 \end{bmatrix} + \frac15\begin{bmatrix} 2 \\ -1 \end{bmatrix}.  
$$

And then after $k$ steps

$$
  \vect{x}_0 = c_19^k\begin{bmatrix} 1 \\ 2 \end{bmatrix} + c_24^k\begin{bmatrix} 2 \\ -1 \end{bmatrix}
  = 9^k \left( c_1\begin{bmatrix} 1 \\ 2 \end{bmatrix} + 
   c_2\left(\frac49\right)^k\begin{bmatrix} 2 \\ -1 \end{bmatrix}  \right)
$$

That we have such a rapid convergence in the example is due to the two circumstances mentioned:  <BR>
(1) the ratio  $|\lambda_1/\lambda_2| = 4/9$ is smaller than $0.5$, <BR>
and <BR>
(2) the coefficient  $c_1 = \frac13$  is not too close to zero.<BR>
Thus the  term with the eigenvector $\mathbf{v}_2$ in the expression within the parentheses 

$$
   c_1 \vect{v}_1 + 
   c_2\left(\frac{\lambda_2}{\lambda_1}\right)^k\vect{v}_1   =
    \frac35\begin{bmatrix} 1 \\ 2 \end{bmatrix} + 
   \frac15\left(\frac49\right)^k\begin{bmatrix} 2 \\ -1 \end{bmatrix}  
$$

soon becomes negligibly small compared to the term with the eigenvector $\vect{v}_1$. <BR>
In the exceptional situation where the 'first guess' was exactly a multiple of the second eigenvector  $\vect{v}_2$  all vectors $\mathbf{x}_k$ would remain on the line generated by $\vect{v}_2$. In theory, that is.  In practice, even then, owing to  minor round-off errors in the long long (no typo) run the process would probably converge to a multiple of $\vect{v}_1$.

::::


::::{prf:example}
:label:  Ex:PowerMethod:SecondExample
Let us apply the power method to the following matrix plus 'initial guess

$$
  A = \begin{bmatrix} 
     7  &  -1  &   5\\
    -2  &   7  &   6\\
     2  &  -2  &   6\\'
       \end{bmatrix}, \quad
       \vect{x}_0 = \begin{bmatrix} 
         1 \\ 1 \\ 1        \end{bmatrix}.
$$

We will continue refreshing the vector $\vect{x}$ until two consectutive
iterates satisfy

$$
  \norm{\vect{x}_{k+1} - \vect{x}_{k+1}} \leq 10^{-4}.
$$

This restriction is met after 23 iterations.  The current value of $\vect{x}$,
up to four decimals  is then

$$
    \vect{x} = \begin{bmatrix} 
         1.0000 \\ 0.3612 \\ 0.4456  \end{bmatrix}.
$$

And by computing $A\vect{x}$, which yields

$$
  A\vect{x} = \begin{bmatrix} 
         8.8668 \\ 3.2024 \\ 3.9512  \end{bmatrix},
$$
we read off that the dominant eigenvalue is (approximately) 
$\lambda_1 = 8.8668$.

In this example the actual eigenvalues up to four decimals are given by

$$
  \lambda_1 = 8.8675, \quad  \lambda_{2,3} =  5.5663 \pm 1.8164i. 
$$

So the matrix is not real diagonalizable, but it is complex diagonalizable.
Since the dominant eigenvalue is real, and the ratio

$$
  \frac{|\lambda_{2,3}|}{|\lambda_{1}|} \approx 0.66 
$$

we can still use Equation {eq}`Eq:PowerMethod:GenSol-2` to conclude that, except for very unfortunate initial vectors,  the method will lead to a dominant eigenvector. As it did indeed.


::::

::::{prf:example}
:label: Ex:PowerMethod:BadMatrix-1

Consider the matrix  $A = \begin{bmatrix}
     3 &4 &-1& 3 \\ 
     4 &-2& 3& 2\\
     2 & 1& 6& 3\\
     3 & 4& 2&-7 \end{bmatrix}$, and the initial vector 
     $\mathbf{x}_0 = \begin{bmatrix}   2 \\ 2 \\ 4 \\ 1 \end{bmatrix}$   

If we (let some computer program) run one hundred cycles of the power method algorithm, the last two iterates are

$$
   \vect{x}_{99} = \begin{bmatrix}   0.3345 \\ 0.5096 \\ 1.0000 \\ 0.6336 \end{bmatrix}, \quad 
   \vect{x}_{100} = \begin{bmatrix}   0.4343 \\ 0.5051 \\ 1.0000 \\ 0.0668 \end{bmatrix}.
$$

The process has by far not reached its 'steady state'.  Look at the change in the fourth entry. 

After one hundred extra cycles, the output is stil pretty bad:

$$
   \vect{x}_{199} = \begin{bmatrix}   0.1374 \\ 0.3626 \\ 0.7028 \\1.0000 \end{bmatrix}, \quad 
   \vect{x}_{200} = \begin{bmatrix}   0.5297 \\ 0.5007 \\ 1.0000 \\ -0.4751 \end{bmatrix}.
$$

Only after 700 to 800 iterations  the process starts to stabilize:

$$
   \vect{x}_{799} = \begin{bmatrix}   -0.2506 \\ -0.0763 \\ -0.1672 \\1.0000 \end{bmatrix} \,\, \approx \,\,
   \vect{x}_{800} = \begin{bmatrix}   -0.2515 \\ -0.0773 \\ -0.1691 \\ 1.0000 \end{bmatrix} \,\, \approx\,\, 
   \mathbf{v}_1 = \begin{bmatrix}  -0.2510 \\ -0.0768 \\ -0.1682 \\ 1.0000 \end{bmatrix}.
$$

To find the corresponding eigenvalue we compute 

$$
  \vect{y} = A\vect{x}_{800} = \begin{bmatrix}   2.1083 \\ 0.6458 \\ 1.4137 \\
  -8.3955 \end{bmatrix} \,\,\approx \,\,-8.3955\vect{x}_{800} \,=\,
  \begin{bmatrix}   2.1067 \\ 0.6440 \\ 1.4100 \\
  -8.3955 \end{bmatrix}.
$$

So the largest eigenvalue $\lambda_1 \approx -8.3955$,  and the above equations also shows that $\vect{x}_{800}$  is approximately an eigenvector for it.

Now why are things going so slowly here?

Well, up to four decimals, the largest and the second largest eigenvalues are given by $\lambda_1 = -8.3967$ and $\lambda_2 = 8.27974$. The ratio of the absolute values of these two is very close to 1, namely

$$
  \frac{|\lambda_2|}{|\lambda_1|} = 0.9882.
$$

So the factor $\left(\dfrac{\lambda_2}{\lambda_1} \right)^k$ goes to $0$ *very slowly*.

Moreover, to aggreviate matters, we have chosen the initial vector very much in the direction of an eigenvector  $\vect{v}_2$ for $\lambda_2$.  

$$
  \vect{x}_0 = \begin{bmatrix}   2 \\ 2 \\ 4 \\ 1 \end{bmatrix}, \quad
  \vect{v}_2 = \begin{bmatrix}   1.5453 \\ 2.0291 \\ 4.0000 \\ 1.3566  
  \end{bmatrix}.
$$

If we write the initial vector as a linear combination of four unit eigenvectors

$$
  c_1 \vect{u}_1 + c_2 \vect{u}_2 + c_3 \vect{u}_3 + c_4 \vect{u}_4
$$

the coefficient  $c_2$ will be large compared to the coefficient $c_1$, so the
contribution of the term

$$
   c_2 \lambda_2^k \vect{u}_2
$$

for a long time will be noticeable compared to the contribution of the term

$$
   c_1 \lambda_1^k \vect{u}_1.
$$

::::

(Sec:PowerMethodExtras)=
## Some extensions


In the previous section the power method was used find the dominant (real) eigenvalue of a matrix $A$. <BR>
In this subsection we will consider three extensions:

--- To find the *smallest* eigenvalue of a matrix $A$.

--- To find a second eigenvalue of $A$ by using a *shift* of $A$.

---  To find the dominant *complex*  eigenvalue <BR>
&nbsp; &nbsp; (provided the eigenvalue with largest modulus is complex). <BR>


The first issue is covered by the next proposition.



::::{prf:proposition}  Inverse Power Method
:label: Prop:PowerMethod:SmallestEigenvalue

Suppose $A$ is an $n\times n$ matrix with $n$ eigenvalues ordered via

$$
  |\lambda_1| \geq |\lambda_2| \geq  \ldots \geq |\lambda_{n-1}| > |\lambda_{n}| > 0.
$$

Here $|\lambda|$ denotes the modulus of $\lambda$. <BR>
 Note that the last two *strict* inequalities
imply that $A$  has a single smallest eigenvalue which is not equal to $0$.
<BR>
Since $0$ is not an eigenvalue, we may conclude that $A$ is invertible.

Then the power method applied to $A^{-1}$  converges (apart from the usual exceptional cases) to an eigenvector $\vect{v}_n$  for the *smallest* eigenvalue $\lambda_n$.
::::


::::{prf:proof}

We make us of the property in {numref}`Exc:EigenValues:EigenvaluesInverse` in 
{numref}`Sec:EV-basics`, which states that  $A^{-1}$ has the eigenvalues 


$$
  \frac{1}{\lambda_1}, \,\frac{1}{\lambda_2},\,\ldots\,,\,\frac{1}{\lambda_n}
$$

where the order of the moduli is

$$
   \frac{1}{|\lambda_1|}\leq \frac{1}{|\lambda_{2}|} \leq \,\ldots\, \leq \,\frac{1}{|\lambda_{n-1}|} \,< \, \frac{1}{|\lambda_n|}.
$$

Thus,  $A^{-1}$  has the dominant eigenvalue $\dfrac{1}{\lambda_n} = \lambda_n^{-1}$

Moreover,  the exercise gives that the eigenvectors of  $A^{-1}$  for eigenvalue $\lambda_i^{-1}$ are exactly the eigenvectors of $A$ for 
eigenvalue $\lambda_i$.


Thus if we apply the algorithm of the power method to the matrix $A^{-1}$, we will find an eigenvector  $\mathbf{v}_n$ of $A^{-1}$ for the eigenvalue $\lambda_n^{-1}$. <BR>
This is then an eigenvector of $A$  for  the smallest eigenvalue  $\lambda_n$.

::::




::::{prf:example}
:label:  Ex:PowerMethod:FirstExampleContd

Let  $A$ be the matrix  &nbsp;  $\begin{bmatrix}5 & 2 \\ 2 & 8 \end{bmatrix}$
of the earlier example {prf:ref}`Ex:PowerMethod:FirstExample`. <BR>
We saw that $A$ has the eigenvalues  $\lambda_1 = 9$ and $\lambda_2 = 4$.

If we apply the Inverse Power Method, starting from 

$$
  \vect{x}_0 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}
$$

we find 

$$
  \vect{x}_{12} = \begin{bmatrix} 1.0000 \\ -0.4998 \end{bmatrix}.
$$

This is indeed very close to the eigenvector

$$
   \vect{v}_2 = \begin{bmatrix} 1.0 \\ -0.5 \end{bmatrix}
$$

for the eigenvalue  $4$ of the matrix $A$.

::::