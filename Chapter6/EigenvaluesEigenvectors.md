(Sec:EV-basics)=

# Definitions and Examples

## Introduction



In matrix algebra there are two basic equations. One we have amply studied in {numref}`Section:LinSystems`:

$$
A\vect{x} = \vect{b}.
$$

The other:

$$
A\vect{v} = c\vect{v} \quad \text{for some real number  } c \in \R.
$$

A setting in which the second equation plays a role is the following.

::::::{prf:example}
:label: Ex:EigenValues:ToyMigrationModel

In {numref}`Sec:LinTrafo` we introduced a simple migration model where

$$
\vect{x}_{k+1} = M\vect{x}_k
$$

described the transition of the 'state' of some system at time $k$ to the state at time $k+1$, the 'state' being the population sizes of a number of cities (or countries), or of several species in an eco system.
The dynamical system

$$
\vect{x}_{k+1} = \left[\begin{array}{cc} 0.9 & 0.2 \\ 0.1 & 0.8 \end{array}\right]\vect{x}_k, \quad
\vect{x}_k = \left[\begin{array}{c} x_k \\ y_k \end{array}\right]
$$

can be interpreted as a model of two cities where in one 'time period' $10 \%$ of city $A$ moves to city $B$,
and $20 \%$ of city $B$ moves to city $A$, namely

$$
x_{k+1} = 0.9x_k + 0.2 y_k
$$

and likewise

$$
y_{k+1} = 0.1x_k + 0.8 y_k.
$$

In this toy model there are no births or deaths, nor migrations to or from 'the outside world'.
A natural question is: is there an equilibrium state, i.e. a state $\vect{s}$ for which

$$
M\vect{s} = \vect{s} = 1 \vect{s}?
$$

You may check that all states

$$
\vect{s} = c\left[\begin{array}{c} 2\\1 \end{array}\right],
$$

have this property. Note that these represent the situation where city $A$ has twice as many citizens as city $B$. For this distribution of people over the two cities the outflow of $10 \%$ from $A$ to $B$ is exactly balanced by the outflow of $20 \%$ from $B$ to $A$.


::::::


(Subsec:EV-basics)=

## Definitions and examples

::::::{prf:definition}

Let $A$ be an $n \times n$ matrix. A real number $\lambda$ is called an **eigenvalue** of $A$ if there exists a nonzero vector $\vect{v}$ in $\R^n$ for which

$$
A\vect{v} = \lambda\vect{v}.
$$

Such a (nonzero) vector $\vect{v}$ is then called an **eigenvector** of $A$ for the eigenvalue $\lambda$.

::::::

The reason to require that an eigenvector has to be nonzero is that otherwise _every_ number $c$ would be an eigenvalue.
Namely, $A\vect{0} = \vect{0} = c\vect{0}$ for any real number $c$.
Thus then the concept of an eigenvalue would be a rather empty notion.

::::::{prf:remark}

Until now we have only been working with vectors and matrices of which all entries are real numbers. It is possible to generalize to vectors and matrices that have complex numbers as entries. If you have never seen or heard about complex numbers: don't worry,
in this chapter we will focus on the 'real universe'. However, even for matrices with real entries complex eigenvalues and eigenvectors come up in quite a natural way, and in many senses make the theory simpler.  In one or two examples we will hint at
these, but **unless specifically indicated, in this chapter eigenvalues will be real eigenvalues**.  ({numref}`Section %s <Section:ComplexEV>` is devoted to complex eigenvalues.)

::::::

In the first half of this section we will answer the following three questions.

<ul>
<li>

How to check whether a vector $\vect{v}$ is an eigenvector of a given matrix $A$.

</li>
<li>

How to check whether a number $c$ is an eigenvalue.

</li>
<li>

How to find the eigenvector(s) for a given eigenvalue.

</li>
</ul>

The (harder) question, how to actually find the eigenvalues, we postpone until the next section.

In the second half of this section we will consider a few general properties of eigenvalues and eigenvectors.

To tackle the first question, take a look at the following example.

::::::{prf:example}
:label: Ex:Eigenvalues:Eigenvectorcheck

For the matrix
$A = \left[\begin{array}{cc} 1 & 4 \\ 1 & 1 \end{array}\right]$
and the vector $\vect{u} = \left[\begin{array}{c} 2 \\1 \end{array}\right]$
we see that

$$
A\vect{u} = \left[\begin{array}{cc} 1 & 4 \\ 1 & 1 \end{array}\right]
\left[\begin{array}{c} 2 \\1 \end{array}\right]
 =\left[\begin{array}{c} 6 \\3 \end{array}\right]
= 3 \left[\begin{array}{c} 2 \\1 \end{array}\right]
 = 3 \vect{u},
$$

so $\vect{u}$ is an eigenvector of $A$ for the eigenvalue 3.

On the other hand, for the vector $\vect{v} = \begin{bmatrix} 2 \\ -2 \end{bmatrix}$ we have

$$
A\vect{v} = \left[\begin{array}{cc} 1 & 4 \\ 1 & 1 \end{array}\right]
\left[\begin{array}{c} 2\\-2\end{array}\right]
 =\begin{bmatrix} -6 \\0 \end{bmatrix}
\quad \text{and} \quad \left[\begin{array}{c} -6 \\0 \end{array}\right]
\neq c \begin{bmatrix} 2\\-2 \end{bmatrix} = c \vect{v},
$$

since such a $c$ should simultaneously satisfy $2c = -6$ and $(-2)c = 0$.
<BR>
So $\vect{v} = \begin{bmatrix} 2\\-2 \end{bmatrix}$ is not an eigenvector of $A$.
See also {numref}`Figure %s <Fig:Eigenvalues:Eigenvector-no-Eigenvector>`

```{applet}
:url: eigenvalue_eigenvector/no_eigenvector
:fig: Images/Fig-Eigenvalues-Eigenvector-no-Eigenvector.svg
:name: Fig:Eigenvalues:Eigenvector-no-Eigenvector
:class: dark-light

To be or not to be (an eigenvector).
```

::::::

To check whether a given vector $\vect{v}$ is an eigenvector of a matrix $A$, all we have to do is compute $A\vect{v}$ and see whether it is a multiple of $\vect{v}$.

The next question is:
how to proceed to find out whether a given real number $\lambda$ is an eigenvalue of a matrix $A$?
Well, again let us consider an example first.

::::::{prf:example}
:label: Ex:Eigenvalues:VerifyEigenvalue

We will check whether $1$ and $-1$ are eigenvalues of the matrix $A = \left[\begin{array}{cc} 1 & 4 \\ 1 & 1  \end{array}\right]$ of the previous example.

For the first candidate we have to search for nonzero solutions of the equation

$$
A\vect{v} = 1\vect{v}.
$$

This is a slightly different equation from the linear equations $A\vect{x} = \vect{b}$ we studied in {numref}`Section:LinSystems`. However, we can rewrite it to a homogeneous equation:

$$
A\vect{v} = 1\vect{v} \quad \iff \quad A\vect{v} - 1\vect{v} = \vect{0}.
$$

We cannot simply rewrite this as $(A-1)\vect{v} = \vect{0}$, as the difference between a matrix and a scalar is not defined. However, by a small twist we get into well-known territory:

$$
A\vect{v} - 1\vect{v} = \vect{0} \quad \iff \quad  A\vect{v} - I\vect{v} = \vect{0}
\quad \iff \quad (A-I)\vect{v} = \vect{0}.
$$

As

$$
A - I = \left[\begin{array}{cc} 1 & 4 \\ 1 & 1  \end{array}\right]
 - \left[\begin{array}{cc} 1 & 0 \\ 0 & 1  \end{array}\right]
 =
\left[\begin{array}{cc} 0 & 4 \\ 1 & 0  \end{array}\right]
,
$$

the equation $(A-I)\vect{v} = \vect{0}$ becomes

$$
\left[\begin{array}{cc} 0 & 4 \\ 1 & 0  \end{array}\right]
 \vect{v} = \left[\begin{array}{c} 0 \\ 0 \end{array}\right]
.
$$

So the question whether 1 is an eigenvalue of the matrix $A$ is equivalent to the question whether this equation has nonzero solutions.

As the equation is homogeneous, we don't have to work with the augmented matrix. The  matrix $A - I$ has two pivots, so the only solution of the equation is the zero vector.

We may conclude that the value 1 is not an eigenvalue of the matrix $A$.

For the value $-1$ we proceed likewise:
we rewrite the equation

$$
A\vect{v} = (-1)\vect{v}
$$

via

$$
A\vect{v} - (-1)\vect{v} = \vect{0} \quad \iff \quad (A-(-1)I)\vect{v}  = \vect{0}
$$

to the linear system

$$
\quad (A-(-1)I)\vect{v} = (A+I)\vect{v} = \vect{0}.
$$

So now we have to look for nonzero solutions of

$$
(A + I)\vect{x} = \vect{0}, \quad \text{i.e.}\quad
\begin{bmatrix} 2 & 4 \\ 1 & 2 \end{bmatrix}\vect{x} =
\begin{bmatrix} 0  \\ 0 \end{bmatrix}.
$$

The solutions of this last equation are

$$
\vect{x} = x_2\begin{bmatrix} -2  \\ 1 \end{bmatrix},   x_2 \in \R.
$$

As a check:

$$
\left[\begin{array}{cc} 1 & 4 \\ 1 & 1 \end{array}\right]
\left[\begin{array}{c} -2  \\ 1 \end{array}\right]
 = \left[\begin{array}{cc} 2  \\ -1 \end{array}\right]
 = (-1)\left[\begin{array}{c} -2  \\ 1 \end{array}\right]
.
$$

So $-1$ is an eigenvalue of the matrix $\left[\begin{array}{cc} 1 & 4 \\ 1 & 1 \end{array}\right] $ and a corresponding eigenvector is the vector
$\left[\begin{array}{c} 2 \\ -1 \end{array}\right]$.  Note that the full set of eigenvectors for the eigenvalue $\lambda = -1$ is the set of all multiples of the vector $\left[\begin{array}{c} 2  \\ -1 \end{array}\right]$. Well, to be precise, all _nonzero_ multiples.

::::::

The procedure of the above example works in general:
to check whether a real number $\lambda$ is an eigenvalue of a matrix $A$ we have to find out whether the (homogeneous linear) equation

:::{math}

(A - \lambda I)\vect{x} = 0

:::

has non-trivial solutions. If it has, $\lambda$ is an eigenvalue, and the non-trivial solutions are the corresponding eigenvectors. And if it has not, $\lambda$ is not an eigenvalue.

For future reference we formulate this property as a proposition.

::::::{prf:proposition}
:label: Prop:Eigenvalues:AminusLambdaI

A real number $\lambda$ is an eigenvalue of a matrix $A$ if and only if the equation

:::{math}
:label: Eq:Eigenvalues:EigenvalueEquation

(A - \lambda I)\vect{x} = 0

:::

has non-trivial solutions.
Moreover, these non-trivial solutions are exactly the corresponding eigenvectors.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/0a053b62-1e2c-4994-93eb-10e8f99a88dc?id=93701
:label: grasple_exercise_6_1_T1
:dropdown:
:description: To verify whether a number is an eigenvalue of a (2x2) matrix.

::::::


Note that the proposition handles our third question as well. If $\lambda$ has been shown to be an eigenvalue of $A$, then the corresponding eigenvectors are the (nonzero) solutions of the homogeneous linear system {eq}`Eq:Eigenvalues:EigenvalueEquation`.

Let us now have a look at a $3\times3$ matrix.

::::::{prf:example}

Consider the matrix $A = \begin{bmatrix} -2 & 1 & 2 \\ 0 & -1 & 2 \\ -1 & 1 & 0 \end{bmatrix}$.

We will check whether $2$ and $-2$ are eigenvalues of this matrix.

For the first candidate we have to search for nonzero solutions of the equation

$$
A\vect{v} = 2\vect{v}.
$$

This equation can be rewritten as

$$
(A-2I)\vect{v} = \vect{0}.
$$

So we are looking for non-trivial solutions of the homogeneous system of linear equations with coefficient matrix $A - 2I$. Again, we can work with the augmented matrix $[A - 2I | \vect{0} ]$, or we can use the fact that we look for nonzero vectors in the null space of $A-2I$.
If we plug in the entries of $A$ and use row reduction we get

$$
A - 2I  =
\left[\begin{array}{ccc} -2-2 & 1 & 2 \\ 0 & -1-2 & 2 \\ -1 & 1 & 0-2 \end{array}\right]  =
\left[\begin{array}{ccc} -4 & 1 & 2 \\ 0 & -3 & 2 \\ -1 & 1 & -2 \end{array}\right]  \sim
\left[\begin{array}{ccc} 1 & 1 & -2  \\ 0 & -3 & 2 \\ 0 & 5 & -4 \end{array}\right].
$$

We multiply the last row by 3 (to avoid fractions), next add 5 times the second row to arrive at the echelon matrix

$$
A-2I \sim 
\left[\begin{array}{cccc} 1 & 1 & -2  \\ 0 & -3 & 2 \\ 0 & 0 & -2 \end{array}\right].
$$

This last matrix has rank 3, so its null space contains only the zero vector. Thus there are no nonzero solutions for the equation $A\vect{v} - 2\vect{v} = \vect{0}$, and we conclude that 2 is _not_ an eigenvalue of $A$.

For the other candidate we proceed in the same manner. Now we have to find the null space of the matrix

$$
(A-(-2)I) = (A+2I).
$$

For this matrix, row reduction yields

$$
A+2I = \begin{bmatrix} 0 & 1 & 2 \\ 0 & 1 & 2 \\ -1 & 1 & 2 \end{bmatrix}  \sim
\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 2 \\ 0 &0 & 0 \end{bmatrix}.


$$

We conclude that $A+2I$ has rank 2, thus the null space of $A+2I$ has dimension 1. From the row reduced form we read off that the null space contains all multiples of the vector
$\vect{v} = \begin{bmatrix} 0 \\ 2 \\ -1\end{bmatrix}$. These then are exactly the eigenvectors for the eigenvalue $\lambda = -2$.
Well, strictly speaking we should exclude the multiple $0\vect{v}$, as an eigenvector by definition is not the zero vector.
As a check:

$$
A\vect{v} =  \begin{bmatrix} -2 & 1 & 2 \\ 0 & -1 & 2 \\ -1 & 1 & 0 \end{bmatrix} \begin{bmatrix} 0 \\ 2 \\ -1\end{bmatrix} =
\begin{bmatrix} 0 \\ -4 \\ 2\end{bmatrix} = (-2) \begin{bmatrix} 0 \\ 2 \\ -1\end{bmatrix} = (-2)\vect{v}.
$$

::::::

In the following example the matrix has an eigenvalue for which there turn out to be two linearly independent eigenvectors.

::::::{prf:example}
:label: Ex:EigenValues:TwodimEigenspace

We will find all eigenvectors of the matrix $A = \begin{bmatrix} 1 & 2 & 2 \\ 2 & 1 & 2 \\ 2 & 2 & 1  \end{bmatrix}$
for the eigenvalue $\lambda_1 = -1$.

We know that we can do so by row reducing the augmented matrix $[A - (-1)I | \vect{0}]$.

$$
[A - (-1)I \,|\, \vect{0}] = \left[\begin{array}{ccc|c} 2 & 2 & 2 &0\\ 2 & 2 & 2 &0\\ 2 & 2 & 2&0  \end{array}\right]
 \sim
\left[\begin{array}{ccc|c} 1 & 1 & 1 &0\\ 0 & 0 & 0 &0\\ 0 & 0 & 0  &0\end{array}\right]
.
$$

You can check that two independent eigenvectors are given by

$$
\vect{v}_1 = \left[\begin{array}{c}1 \\0\\ -1  \end{array}\right]
\quad \text{and}\quad \vect{v}_2 = \left[\begin{array}{c} 0 \\1\\-1  \end{array}\right]
.
$$

::::::

So far we have defined eigenvalues and eigenvectors and we have shown how to check whether a number or a vector has one of these properties. Before we will address the question of how to find the eigenvalues, in the next subsection we will first consider a few general properties of eigenvalues and eigenvectors.

(Subsec:EigenValues:GeneralProp)=

## General properties of eigenvalues and eigenvectors

::::::{prf:proposition}
:label: Prop:EigenValues:Subspace

Let $\lambda$ be an eigenvalue of the matrix $A$. Let $S$ be the set of
solutions of the equation

$$
A\vect{x} = \lambda \vect{x}.
$$

Then $S$ is a subspace of $\R^n$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:EigenValues:Subspace`
:class: tudproof

We can proceed in two ways.

The most elementary way is to check that this set has the three properties of a subspace.

<ol type = "i">
<li>

$\vect{0} \in S$, since  $A\vect{0} = \vect{0} = \lambda \vect{0}$.
</li>

<li>

If $\vect{u}$ and $\vect{v}$ are vectors in $S$, so $A\vect{u}=\lambda\vect{u}$ and $A\vect{v}=\lambda\vect{v}$,

then

$$
A(\vect{u}+\vect{v}) = A\vect{u}+A\vect{v} = \lambda\vect{u}+\lambda\vect{v} = \lambda(\vect{u}  +\vect{v}),
$$

so $\vect{u}  +\vect{v}$ is also a (trivial or non-trivial) solution of the equation $A\vect{x}=\lambda\vect{x}$, hence lies in $S$.

</li>
<li>

In a similar way it is shown that if $\vect{u}$ lies in $S$, then so does any scalar multiple $c\vect{u}$.
Namely, if

$$
A\vect{u} = \lambda \vect{u},
$$

then

$$
A(c\vect{u}) = c A\vect{u} = c\lambda \vect{u} = \lambda (c\vect{u}).
$$

</li>
</ol>

A more 'sophisticated' argument is the following. The set $S$ is the set of all solutions (trivial or non-trivial) of the equation $A\vect{x}=\lambda\vect{x}$.
As we have seen in the previous section,

$$

A\vect{x}=\lambda\vect{x} \quad \iff \quad (A-\lambda I)\vect{x}= \vect{0}.
$$

Thus $S$ is the null space of $A - \lambda I$, and, as such, a subspace of $\R^n$.

::::::

::::::{prf:definition}
:label: Dfn:EigenValues:Eigenspace

For an eigenvalue $\lambda$ of the matrix $A$ the null space  of $A - \lambda I$ is called the **eigenspace**  $E_{\lambda}$.

$$
E_{\lambda} = \Nul{(A-\lambda I)}.
$$

::::::

Recall that the null space of $A - \lambda I$ consists of all solutions of the equation

$$
(A-\lambda I)\vect{x} = \vect{0},
$$

which equation is equivalent to

$$
A \vect{x} = \lambda \vect{x}.
$$

So an eigenspace is just the set of all eigenvectors for a given eigenvalue, with $\vect{0}$ as an extra element.

::::::{prf:example}
:label: Ex:EigenValues:TwodimEigenspaceCtd

The matrix $A = \begin{bmatrix} 1 & 2 & 2 \\ 2 & 1 & 2 \\ 2 & 2 & 1  \end{bmatrix}$
has the eigenvalues $\lambda_1 = -1$ and $\lambda_2=5$. <BR>
We have seen ({prf:ref}`Ex:EigenValues:TwodimEigenspace`) that all
eigenvectors for $\lambda = -1$ are linear combinations of the two linearly independent eigenvectors

$$
\vect{v}_1 = \begin{bmatrix} 1 \\0\\ -1  \end{bmatrix}\quad \text{and}\quad \vect{v}_2 = \begin{bmatrix} 0 \\1\\-1  \end{bmatrix}.
$$

Thus

$$
E_{-1} = \Span{\vect{v}_1, \vect{v}_2}  =
\Span{\begin{bmatrix} 1 \\0 \\-1  \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \\-1  \end{bmatrix}}.
$$

Finding a basis of the other eigenspace requires slightly more work:

$$
A - 5I = \begin{bmatrix} -4 & 2 & 2 \\ 2 & -4 & 2 \\ 2 & 2 & -4 \end{bmatrix} \sim
\begin{bmatrix} -2 & 1 & 1 \\ 0 & -3 & 3 \\ 0& 3 & -3 \end{bmatrix} \sim
\cdots  \sim
\begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & -1 \\ 0& 0&0 \end{bmatrix}.
$$

This is a matrix of rank 2, and $\begin{bmatrix} 1  \\1\\1 \end{bmatrix}$ can be taken as a basis of its nulspace, and thus of the eigenspace $E_5$.

::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/363143ee-08c2-4905-9801-474ed10f59e9?id=93697
:label: grasple_exercise_6_1_T2
:dropdown:
:description: To give a basis for the eigenspace for a given $\lambda$  for a 3x3 matrix $A$.

::::::

::::::{prf:proposition}
:label: Prop:Eigenvalues:IndepEigenvectors

Suppose that $\vect{v}_1,   \ldots,   \vect{v}_k$ are (nonzero) eigenvectors of the matrix $A$ for $k$ **different** eigenvalues $\lambda_1, \ldots, \lambda_k$.
Then $\{ \vect{v}_1,  \ldots,  \vect{v}_k  \}$ is a linearly independent set.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:Eigenvalues:IndepEigenvectors`
:class: tudproof

<BR>

We will show that the set $\{ \vect{v}_1,  \ldots,  \vect{v}_k  \}$ cannot be linearly dependent.
Namely, if it were, then one of the vectors would be a linear combination of its predecessors. Suppose $\vect{v}_{\ell}$,
is the first one,
i.e. $\vect{v}_{\ell} \in \Span{\vect{v}_1,  \ldots,  \vect{v}_{\ell-1}}$, where $\{\vect{v}_1,  \ldots,  \vect{v}_{\ell-1}\}$ is linearly independent.

So, let


:::{math}
:label: Eq:v_l-in-Span_1

\vect{v}_{\ell} = c_1 \vect{v}_1 +   \ldots + c_{\ell-1}  \vect{v}_{\ell-1}.

:::

Then

:::{math}
:label: Eq:v_l-in-Span_2

\lambda_{\ell}\vect{v}_{\ell} = c_1 \lambda_{\ell}\vect{v}_1 + \ldots + c_{\ell-1} \lambda_{\ell} \vect{v}_{\ell-1}.

:::

On the other hand, if we multiply both sides of Equation {eq}`Eq:v_l-in-Span_1` by $A$, we find that

$$

A\vect{v}_{\ell} = \underline{\lambda_{\ell}\vect{v}_{\ell}}=  A(c_1 \vect{v}_1 +   \ldots + c_{\ell-1}  \vect{v}_{\ell-1}) = \underline{c_1 \lambda_1\vect{v}_1 +   \ldots + c_{\ell-1} \lambda_{\ell-1} \vect{v}_{\ell-1}}.


$$

From this we extricate

:::{math}
:label: Eq:v_l-in-Span_3

\lambda_{\ell}\vect{v}_{\ell} = c_1 \lambda_1\vect{v}_1 + \ldots + c_{\ell-1} \lambda_{\ell-1} \vect{v}_{\ell-1}.
:::

Subtracting Equation {eq}`Eq:v_l-in-Span_3` from Equation {eq}`Eq:v_l-in-Span_2` gives

$$
\lambda_{\ell}\vect{v}_{\ell} - \lambda_{\ell}\vect{v}_{\ell} = \vect{0} =
c_1(\lambda_1 - \lambda_{\ell})\vect{v}_1 + \ldots + c_{\ell-1}(\lambda_{\ell-1} - \lambda_{\ell}) \vect{v}_{\ell-1}.
$$

So, a linear combination of the vectors $\vect{v}_1,  \ldots,  \vect{v}_{\ell-1}$ is equal to the zero vector.
Because of the assumption of linear independence of the first $\ell-1$ vectors $\vect{v}_1,   \ldots ,  \vect{v}_{\ell-1}$, it follows that all coefficients must be zero, i.e.

$$
c_1(\lambda_1 - \lambda_{\ell}) = 0,  \quad \ldots  \,,  \quad  c_{\ell-1}(\lambda_{\ell-1} - \lambda_{\ell}) = 0.
$$

Since all $\lambda_i$ are different, all differences $(\lambda_1 - \lambda_{\ell}), \ldots, (\lambda_{\ell-1} - \lambda_{\ell})$
are nonzero,

and we can conclude that

$$
c_1 = 0, \,\ldots,\,c_{\ell -1} = 0.
$$

But then

$$
\vect{v}_{\ell} = c_1 \vect{v}_1 +   \ldots + c_{\ell-1}  \vect{v}_{\ell-1} = \vect{0},
$$

which is impossible, as the assumption was that $\vect{v}_{\ell}$ is an eigenvector.

::::::

::::::{prf:example}
:label: Ex:EigenValues:TwodimEigenspace2

For the matrix $A = \left[\begin{array}{ccc}2 & 2 & 1 \\ 0 & 1 & 2 \\ 0 & 4 & 3  \end{array}\right]$
and the vectors

$$
\vect{u} = \left[\begin{array}{c}1 \\0 \\ 0  \end{array}\right]
, \quad
\vect{v} = \left[\begin{array}{c}1 \\ -3 \\ 3  \end{array}\right]
, \quad
\vect{w} = \left[\begin{array}{c}4 \\ 3 \\ 6  \end{array}\right]
$$

it may be checked that

$$
A\vect{u} = 2\vect{u}, \quad A\vect{v} = (-1)\vect{v}, \quad A\vect{w} = 5\vect{w}.
$$

So $ \vect{u}, \vect{v}$ and $ \vect{w}$ are eigenvectors of $A$ for the eigenvalues $2, -1, 5$.

The set $\{\vect{u},  \vect{v}, \vect{w}  \}$ is seen to be linearly independent.

::::::

Since a set of linearly independent vectors in $\R^n$ can contain at most $n$ vectors, an immediate consequence of
{prf:ref}`Prop:Eigenvalues:IndepEigenvectors` is the following important property.

::::::{prf:corollary}
:label: Ex:EigenValues:MaxNumberEigenvalues

An $n \times n$ matrix $A$ can have at most $n$ different eigenvalues.

::::::

It can be shown  (as we will see in {prf:ref}`Ex:Eigenvalues:TwodimEigenspace2`)
that the $3\times 3$  matrix $A = \begin{bmatrix} 1 & 2 & 2 \\ 2 & 1 & 2 \\ 2 & 2 & 1  \end{bmatrix}$ of the previous example has no other eigenvalues than $-1$ and $5$. So $A$ is a $3 \times 3$ matrix with fewer than $3$ eigenvalues. <BR>
Things can even be 'worse' as the following example shows. The idea behind it: if $\vect{v}$ is an eigenvector of the matrix $A$, then the vector $\vect{v}$ is mapped to the multiple $\lambda\vect{v}$ by the transformation $T(\vect{x}) = A\vect{x}$.
A multiple $\lambda\vect{v}$ is a vector with the same direction as $\vect{v}$ or the  direction opposite to $\vect{v}$. With this in mind, can we construct a linear transformation of $\R^2$ to $\R^2$ that certainly does not have such vectors? Yes we can!

::::::{prf:example}
:label: Ex:EigenValues:Rotation

The matrix $R = \begin{bmatrix} 0 & -1 \\1 & 0  \end{bmatrix}$ has no (real) eigenvalues.

Namely, the corresponding transformation is a rotation around (0,0) over an angle $\frac12\pi$, and this 'moves around' all vectors.

See Figure {numref}`Figure %s <Fig:Eigenvalues:Eigenvector>`

::::{figure} Images/Fig-Eigenvalues-Rotation.svg
:name: Fig:Eigenvalues:Eigenvector
:class: dark-light

A rotation has no (real) eigenvectors.
::::

::::::

::::::{prf:remark}
:label: Rem:EigenValues:Rotation

This is a remark only for readers who are familiar with complex numbers.
The matrix $R = \begin{bmatrix} 0 & -1 \\1 & 0  \end{bmatrix}$ has no **real** eigenvalues. If we allow eigenvalues to be complex numbers, and vectors to have complex entries, it appears that

$$
\left[\begin{array}{cc} 0 & -1 \\1 & 0  \end{array} \right]
\left[\begin{array}{c}  1 \\ i \end{array} \right]
 =
\left[\begin{array}{c}  -i\\ 1 \end{array} \right]
 = (-i)\left[\begin{array}{c}  1\\ i \end{array} \right]
$$

and

$$
\left[\begin{array}{cc} 0 & -1 \\1 & 0  \end{array} \right]
\left[\begin{array}{c}  1 \\ -i \end{array} \right]
 =
\left[\begin{array}{c}  i\\ 1 \end{array} \right]
 = i \left[\begin{array}{c}  1\\ -i \end{array} \right]
.
$$

So it is natural to state that $R$ has the eigenvalues $\pm i$.
(As stated before, {numref}`Section %s <Section:ComplexEV>` is devoted to complex eigenvalues.)
::::::

By definition an eigenvector cannot be the zero vector. There is not such a restriction on eigenvalues. The following proposition may be seen as another characterization of invertibility of a matrix. It is just a reformulation of what we already knew.

::::::{prf:proposition}
:label: Prop:EigenValues:SingularMatrix

A matrix $A$ is invertible if and only if 0 is not an eigenvalue of $A$.
Equivalently: a matrix $A$ is singular (non-invertible) if and only if 0 is an eigenvalue of $A$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:EigenValues:SingularMatrix`
:class: tudproof

We prove the second statement.

If a matrix $A$ is singular, then the columns of $A$ are linearly dependent.

So then there is a non-trivial solution $\vect{v}$ of the equation $A\vect{x} = \vect{0} = 0\vect{x}$.

This non-trivial solution $\vect{v}$ is then an eigenvector for the eigenvalue 0.

All steps can be reversed:
if $\vect{v}$ is an eigenvector for the eigenvalue 0, then $A\vect{v} = 0\vect{v}=\vect{0} $,  for a nonzero vector $\vect{v}$.
<BR>
This implies that the matrix $A$ has linearly dependent columns. And that in its turn is equivalent to the statement that the matrix $A$ is singular.

::::::

::::::{prf:example}
:label: Ex:EigenValues:SingularMatrix

The matrix $A = \begin{bmatrix} 1 & 3 \\ 2 & 6 \end{bmatrix}$
has rank 1, so according to {prf:ref}`Prop:EigenValues:SingularMatrix` it has eigenvalue 0.

The equation $A\vect{x} = \vect{0}$ has the nonzero solution
$\vect{x} = \begin{bmatrix} 3 \\ -1 \end{bmatrix}$,
so this vector is an eigenvector for the eigenvalue 0.

::::::



A matrix gives rise to a linear transformation.
Eigenvalues and eigenvectors make transparent how a matrix/transformation 'works'. The next exposition captures some of the ideas of the rest of the chapter.

::::::{prf:example}
:label: Ex:Eigenvalues:GeomInterpEarlierExample

We have seen that the matrix $A = \begin{bmatrix} 1 & 4 \\ 1 & 1 \end{bmatrix}$ has the eigenvalues
$\lambda_1 = 3$ with corresponding eigenvector $\vect{v}_1 = \begin{bmatrix} 2\\1 \end{bmatrix} $ and
$\lambda_2 = -1$ with corresponding eigenvector $\vect{v}_2 = \begin{bmatrix} -2\\1 \end{bmatrix}$.

So for the linear transformation $T:\R^2 \to \R^2$ defined by $T(\vect{x}) = A\vect{x}$ it holds that

$$
T(\vect{v}_1)  = 3\vect{v}_1 \quad\text{and}\quad T(\vect{v}_2)  = (-1)\vect{v}_1.
$$

If we take the basis $\mathcal{B} = (\vect{v}_1, \vect{v}_2 )$ for $\R^2$, then the transformation does the following:
for an arbitrary vector $\vect{w}$, which is a unique linear combination $\vect{w} = c_1\vect{v}_1+c_2\vect{v}_2$,
the image of $\vect{w}$ under $T$ becomes

$$
T(c_1\vect{v}_1+c_2\vect{v}_2) = c_1T(\vect{v}_1)+c_2T(\vect{v}_2) = 3c_1\vect{v}_1+(-1)c_2\vect{v}_2,
$$

i.e., the component of $\vect{w}$ in the direction of the first basis vector is multiplied by 3, the other component gets a factor
$(-1)$.

In a later section we will study matrices $A$ for which such a basis of eigenvectors exists (and call them diagonalizable).

::::::


## Grasple Exercises 

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c99f6e1b-cec6-4be8-828f-7f93fde00a3b?id=91537
:label: grasple_exercise_6_1_1
:dropdown:
:description:  To check whether a vector is an eigenvector of a matrix.

::::::


::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d858b381-992c-4af3-972d-62a39c4b7a09?id=91538
:label: grasple_exercise_6_1_2
:dropdown:
:description:  To check whether a vector is an eigenvector of a matrix.

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/51a282db-b59f-4bd3-b4b8-fa1f38e402cc?id=91539
:label: grasple_exercise_6_1_3
:dropdown:
:description:  To check whether a vector is an eigenvector of a matrix. 

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fcb91395-9bf7-4fbe-8cb5-100e2c2ad010?id=91540
:label: grasple_exercise_6_1_4
:dropdown:
:description:  To check whether a vector is an eigenvector of a matrix. 

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/860849b2-5787-47d1-9ae8-a663123a86d6?id=91541
:label: grasple_exercise_6_1_5
:dropdown:
:description:  Is a given $\lambda$ an eigenvalue of a matrix? If so, give an eigenvector.

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fa1470cd-81c9-4926-a8a4-587939f4d891?id=91542
:label: grasple_exercise_6_1_6
:dropdown:
:description:   Is a given $\lambda$ an eigenvalue of a matrix? If so, give an eigenvector.

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2faed848-2a76-4853-a998-4167399c1f68?id=91543
:label: grasple_exercise_6_1_7
:dropdown:
:description:   Is a given $\lambda$ an eigenvalue of a matrix? If so, give an eigenvector.

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bb20d21d-7eb6-4e3e-8104-05d276883162?id=91544
:label: grasple_exercise_6_1_8
:dropdown:
:description:   Is a given $\lambda$ an eigenvalue of a matrix? If so, give an eigenvector.

::::::


::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/79980409-fec9-4ab0-9fe1-d1a3d334bb0a?id=92492
:label: grasple_exercise_6_1_9
:dropdown:
:description:   If $\vect{v}$ is an eigenvector of $A$, is it also an eigenvector of $A^T$?

::::::

::::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a467e69f-6a78-4595-a22f-5b68314c04d4?id=92494
:label: grasple_exercise_6_1_10
:dropdown:
:description:  If $W$ is an eigenspace of $A$, is it also an eigenspace of $2A$? And of $A^2$?  

::::::


To conclude, one non-Grasple exercise

::::::{exercise}
:label: Exc:EigenValues:EigenvaluesInverse

Prove the following statements.

If the matrix $A$ is invertible, and $\lambda$ is an eigenvalue of $A$, then $\dfrac{1}{\lambda}$ is an eigenvalue of the inverse of $A$.

Moreover,  if  $\vect{v}$ is an eigenvector of $A$ for eigenvalue $\lambda$, then $\vect{v}$ is also an eigenvector of $A^{-1}$ for eigenvalue $\lambda^{-1}$.

::::::

::::::{admonition} Solution to&nbsp;{numref}`Exc:EigenValues:EigenvaluesInverse`
:class: solution, dropdown

Suppose the nonzero vector $\vect{v}$ is an eigenvector for the eigenvalue $\lambda$ of the invertible matrix $A$.  From {prf:ref}`Prop:EigenValues:SingularMatrix` we know that $\lambda \neq 0$. From

$$
   A\vect{v} = \lambda\vect{v}
$$

it follows that 

$$
   A^{-1}A\vect{v} = \vect{v} = A^{-1}\lambda\vect{v} = \lambda A^{-1}\vect{v}.
$$

And lastly, since $\lambda \neq 0$, we may divide by $\lambda$:

$$
   \vect{v} =  \lambda A^{-1}\vect{v}  \quad \iff \quad  \frac{1}{\lambda}\vect{v} = A^{-1}\vect{v} \quad \iff \quad A^{-1}\vect{v} = \frac{1}{\lambda}\vect{v},
$$

which settles at one stroke that the (same) vector $\vect{v}$ is an eigenvector of the inverse matrix  $A^{-1}$ for the eigenvalue $\lambda^{-1}$.

::::::