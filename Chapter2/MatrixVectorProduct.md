(Sec:MatVecProduct)=

# The Matrix-Vector Product $A\vect{x}$

In this section we will introduce another interpretation/representation of a system of linear equations.  
We will define the product of an $m\times n$ matrix $A$ with a vector $\vect{x}$ in $\mathbb{R}^n$. In the next chapter this will also be the stepping stone to the general matrix-matrix product.

(Subsec:MatVecProduct)=

## Definition of the Matrix-Vector Product

::::{prf:definition}
:label: Dfn:MatVectProd:ProductMatVec

The product $A\mathbf{x}$ of an $m\times n$ matrix

$$
 A = [\mathbf{a}_1 \,\,\mathbf{a}_2\, \ldots\, \mathbf{a}_n]
$$

with a vector

$$
 \mathbf{x} =
\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}\in \mathbb{R}^n
$$

is defined as

$$
  A\mathbf{x} = x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \ldots + x_n\mathbf{a}_n.
$$

So: $A\mathbf{x}$ is the linear combination of the columns of the matrix $A$ with the entries of the vector $\mathbf{x}$ as coefficients.

If the size $n$ of the vector $\mathbf{x}$ is not equal to the number of columns of the matrix $A$, then the product $A\mathbf{x}$ is not defined.

::::

::::{prf:example}
:label: Ex:MatVecProduct:FirstExample

$$
\begin{bmatrix} 2 & 3 \\ 4 & 1 \\ 3 & 5 \\ 0 & 1 \end{bmatrix}
\begin{bmatrix} 5 \\ -1 \end{bmatrix} =
   5
\begin{bmatrix} 2 \\ 4 \\ 3  \\ 0  \end{bmatrix} +
   (-1)
\begin{bmatrix} 3 \\  1 \\  5 \\  1 \end{bmatrix} =
\begin{bmatrix} 10 \\ 20 \\ 15  \\ 0  \end{bmatrix} +
\begin{bmatrix} -3 \\  -1 \\  -5 \\  -1 \end{bmatrix}
      =
\begin{bmatrix} 7 \\  19 \\  10 \\  -1 \end{bmatrix},
$$

and

$$
\begin{bmatrix}1 & 2 & 3 & 5 \end{bmatrix} 
\begin{bmatrix} 4 \\ -2 \\ -1 \\ 3\end{bmatrix} =
4[1] + (-2)[2] + (-1)[3] + 3[5] =  [12].
$$

It is customary to consider a 1x1 matrix as a number, and write the last product as 

$$
\begin{bmatrix}1 & 2 & 3 & 5 \end{bmatrix} 
\begin{bmatrix} 4 \\ -2 \\ -1 \\ 3\end{bmatrix} 
 =
  1\cdot4 +2\cdot(-2)+3\cdot(-1) + 5\cdot 3 = 12.
$$

::::

The interpretation of $A\mathbf{x}$ as a linear combination of the columns of $A$ is important to keep in mind. That is, to not forget it after the following slightly easier way to compute the matrix-vector product.

::::{prf:proposition} Row-column rule
:label: Prop:MatVecProd:Row-ColumnRule

The product of a matrix and a vector can also be computed as follows:

$$
\left[\begin{array}{ccccc}
            a_{11} & a_{12}&  \ldots& \ldots&  a_{1n} \\
            a_{21} & a_{22}&  \ldots& \ldots&  a_{2n} \\
            \vdots &  \vdots&  \ldots& \ldots& \vdots    \\
            a_{m1} & a_{m2}&  \ldots&  \ldots& a_{mn}
          \end{array}
   \right]
\begin{bmatrix}    x_1 \\ x_2 \\ \vdots \\ \vdots \\ x_n  \end{bmatrix}
   =
\begin{bmatrix}
    a_{11}x_1 + a_{12}x_2 +   \ldots+ a_{1n}x_n \\
    a_{21}x_1 + a_{22}x_2 +   \ldots+ a_{2n}x_n \\
                \vdots\\
    a_{m1}x_1 + a_{m2}x_2 +   \ldots+ a_{mn}x_n
\end{bmatrix}.
$$

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:MatVecProd:Row-ColumnRule` ({prf:ref}`Row-column rule <Prop:MatVecProd:Row-ColumnRule>`)
:class: tudproof

The vector on the left-hand side of the identity is by definition equal to the linear combination

$$
  x_1
\begin{bmatrix}  a_{11} \\  a_{21}  \\  \vdots    \\ a_{m1}  \end{bmatrix} +
  x_2
\begin{bmatrix}  a_{12} \\  a_{22}  \\  \vdots    \\ a_{m2}  \end{bmatrix} +
  \,\,\ldots\,\, +
  x_n
\begin{bmatrix}  a_{1n} \\  a_{2n}  \\  \vdots    \\ a_{mn}  \end{bmatrix}.
$$

And this is indeed equal to the vector on the right.

::::

Note that the entry on the $i$-th position of the product, which is given by

$$

  a_{i1}x_1 + a_{i2}x_2 +   \,\,\ldots\,\,+ a_{in}x_n,


$$

is the 'row-column product'

$$


\begin{bmatrix}  a_{i1} & a_{i2} & \ldots & \ldots & a_{in}  \end{bmatrix}
\begin{bmatrix}    x_1 \\ x_2 \\ \vdots \\ \vdots \\ x_n  \end{bmatrix}.


$$

::::{prf:example}
:label: Ex:MatVecProd:MatVecProduct

We find a matrix-vector product using the row-column rule:

$$
\begin{bmatrix}  3 & 4 & 5 \\ 1 & 0 & -1 \\
                   2 & 2 & 4 \\ 5 & -5 & 2\end{bmatrix}
\begin{bmatrix}  3 \\ 1 \\ -4 \end{bmatrix}
       =
\begin{bmatrix}  3\cdot3\!\! &+&\!\! 4\cdot1\!\! &+&\!\! 5\cdot(-4) \\
                        1\cdot3\!\! &+& \!\!0\cdot1\!\! &+&\!\! (-1)\cdot(-4) \\
                        2\cdot3 \!\!&+&\!\! 2\cdot1 \!\! &+&\!\! 4\cdot(-4)\\
                        5\cdot3 \!\!&+& \!\!\!(-5)\cdot1 \!\!\! &+&\!\! 2\cdot(-4)  \end{bmatrix}
     =
\begin{bmatrix}  -7 \\ 7 \\ -8\\ 2\end{bmatrix}.


$$

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e9b864bf-de65-4b67-92d2-7075121ae5e5?id=70222
:label: grasple_exercise_2_4_1T
:dropdown:
:description: To check whether $A\vect{x}$ exists, and if so, to compute it.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/848de922-1bd5-48a2-806d-a2b94bd40a4b?id=70223
:label: grasple_exercise_2_4_2T
:dropdown:
:description: To check whether $A\vect{x}$ exists, and if so, to compute it.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8eb9d800-ebd8-4805-8d56-eac5150f405d?id=85094
:label: grasple_exercise_2_4_3 T
:dropdown:
:description: To check whether $A\vect{x}$ exists, and if so, to compute it.

::::

::::{prf:remark}
:label: Rem:MatVecProd:EquivalentEquations

From the above it follows that the matrix-vector equation

$$
 \left[\begin{array}{ccccc}
            a_{11} & a_{12}&  \ldots& \ldots&  a_{1n} \\
            a_{21} & a_{22}&  \ldots& \ldots&  a_{2n} \\
            \vdots &  \vdots&  \cdots& \cdots& \vdots    \\
            a_{m1} & a_{m2}&  \ldots&  \ldots& a_{mn}
          \end{array}
   \right]
\begin{bmatrix}    x_1 \\ x_2 \\ \vdots \\ \vdots \\ x_n  \end{bmatrix}
   =
\begin{bmatrix}    b_1 \\ b_2 \\ \vdots\\ b_m\end{bmatrix}
$$

and the linear system

$$
   \left\{\begin{array}{ccccccccc}
            a_{11}x_1\! & \!+\!&\!a_{12}x_2\! & \!+\!&\! \ldots\! & \!+\!&\!a_{1n}x_n  \! & \!=\!&\!  b_1 \\
            a_{21}x_1 \! & \!+\!&\!a_{22}x_2\! & \!+\!&\!\ldots\! & \!+\!&\!a_{2n}x_n  \! & \!=\!&\! b_2 \\
            \vdots \! & \! \!&\!  \vdots\! & \! \!&\!\cdots\! & \! \!&\! \vdots     \! & \! \!&\!  \vdots \\
            a_{m1}x_1 \! & \!+\!&\!a_{m2}x_2\! & \!+\!&\! \ldots\! & \!+\!&\!a_{mn}x_n \! & \!=\!&\! b_m
          \end{array}
   \right.
$$

are one and the same thing!

So, we can see this linear system as

- a vector equation:

$$
  x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \ldots + x_n\mathbf{a}_n = \mathbf{b}
$$

or

- a matrix equation:

$$
  A \mathbf{x} = \mathbf{b}.
$$

As we will see later these different interpretations may lead to different insights.

::::

::::{prf:example}
:label: Ex:MatVecProd:FromLinSystemToMatVecEquation

We want to write the system of equations

$$
\left\{\begin{array}{ccccccc}
  5x_1 & - & 3x_2 & -&2x_3 &=&  4 \\
  3x_1 & + & 7x_2 & -&2x_3 &=&  5 \\
  2x_1 & - &6x_2 & +&5x_3 &=& 6  \\
    x_1 &   &  & +& x_3 &=& 8
\end{array}
\right.
$$

in these two different forms.

The corresponding vector equation is

$$
 x_1
\begin{bmatrix} 5 \\ 3 \\ 2 \\ 1  \end{bmatrix} +
 x_2
\begin{bmatrix} -3 \\ 7 \\ -6 \\ 0  \end{bmatrix} +
 x_3
\begin{bmatrix} -2 \\ -2 \\ 5 \\ 1  \end{bmatrix}  =
\begin{bmatrix} 4 \\ 5 \\ 6 \\ 8  \end{bmatrix},
$$

and the corresponding matrix equation becomes

$$
\begin{bmatrix} 5 & -3 & -2\\ 3 &7 & -2\\ 2&-6&5 \\ 1 &0&1 \end{bmatrix}
\begin{bmatrix} x_1 \\x_2 \\ x_3 \end{bmatrix}  =
\begin{bmatrix} 4 \\ 5 \\ 6 \\ 8  \end{bmatrix}.
$$

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d9a8f246-359c-4666-bb8c-2f573e192e5c?id=68857
:label: grasple_exercise_2_4_4T
:dropdown:
:description: Rewriting a linear system to a matrix-vector equation.

::::

::::{prf:proposition}
:label: Prop:MatVecProduct:Linearity

For each $m\times n$ matrix $A$, for all vectors $\mathbf{x},\mathbf{y}$ in $\mathbb{R}^n$, and for all scalars $c$

<ol type ="i">
<li>

$A\,(\mathbf{x}+\mathbf{y} ) = A\mathbf{x} + A\mathbf{y}$;

</li>
<li>

$A\,(c\mathbf{x}) = c\,A\mathbf{x}$.

</li>
</ol>

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:MatVecProduct:Linearity`
:class: tudproof

We will prove the first of the two statements; the other statement goes in a similar fashion.
There are several ways to derive the formula. Via the linear combination idea it may be the easiest.
So assume

$$
  A = [\,\mathbf{a}_1\,\,\,\mathbf{a}_2\,\,\,\ldots\,\,\,\mathbf{a}_n\,], \quad \mathbf{x} =
\begin{bmatrix}    x_1 \\ x_2 \\ \vdots \\ \vdots \\ x_n  \end{bmatrix},
  \quad
  \mathbf{y} =
\begin{bmatrix}    y_1 \\ y_2 \\ \vdots \\ \vdots \\ y_n  \end{bmatrix}.
$$

Then

$$
  A\,(\mathbf{x}+\mathbf{y} ) =
  A\,
\begin{bmatrix}    x_1+y_1 \\ x_2+y_2 \\ \vdots \\ \vdots \\ x_n+y_n  \end{bmatrix} =
  (x_1+y_1 )\mathbf{a}_1 + (x_2+y_2 )\mathbf{a}_2 + \ldots
  + (x_n+y_n )\mathbf{a}_n.
$$

Changing the order of the terms, putting the terms involving $x_i$ to the front, shows that the last expression is equal to

$$
 \big(x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \ldots
  + x_n\mathbf{a}_n\big)+
  \big(y_1\mathbf{a}_1 + y_2\mathbf{a}_2 + \ldots
  + y_n\mathbf{a}_n\big).
$$

The last sum of two vectors can be identified as being

$$
  A\mathbf{x} + A\mathbf{y}.
$$

::::

::::{exercise}
:label: Exc:MatVecProduct:CheckLinearity(ii)

Prove statement (ii) of the previous proposition.

::::

:::{admonition} Solution to&nbsp;{numref}`Exc:MatVecProduct:CheckLinearity(ii)`
:class: solution, dropdown

Assume

$$
  A = [\,\mathbf{a}_1\,\,\,\mathbf{a}_2\,\,\,\ldots\,\,\,\mathbf{a}_n\,], \quad \mathbf{x} =
\begin{bmatrix}    x_1 \\ x_2 \\ \vdots \\ \vdots \\ x_n  \end{bmatrix},
$$

and let $c$ be any real number.

Then

$$
  A\,(c\mathbf{x}) =
  A\,
\begin{bmatrix}    cx_1 \\ cx_2 \\ \vdots \\ \vdots \\ cx_n  \end{bmatrix} =
  cx_1\mathbf{a}_1 + cx_2\mathbf{a}_2 + \ldots
  + cx_n\mathbf{a}_n.
$$

In the last expression we can take the common factor $c$ out to the front,
and we see that it becomes equal to

$$
  c(x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \ldots
  + x_n\mathbf{a}_n) = cA\mathbf{x}.
$$

::::

Using the above rules we can give shorter proofs of statements concerning linear systems. We illustrate this by having a second look at {prf:ref}`Prop:SolSet:SolplusHom`:

::::{prf:example}
:label: Ex:MatVecProduct:SolplusHomRevisited

The contents of that proposition: suppose $(c_{1},...,c_{n})$ is a solution of a linear system. Then $(c_{1}',...,c_{n}')$ is also a solution of the linear system if and only if there exists a solution $(d_{1},...,d_{n})$ of the associated homogeneous system such that $c'_{i}=c_{i}+d_{i}$ for all $i$.

Using the matrix-vector product we can derive this property as follows: &nbsp;we can consider the solutions in vector form,

$$
  \mathbf{c} =
\begin{bmatrix}    c_1 \\ c_2 \\ \vdots \\ \vdots \\ c_n  \end{bmatrix}, \quad
   \mathbf{c'} =
\begin{bmatrix}    c'_1 \\ c'_2 \\ \vdots \\ \vdots \\ c'_n  \end{bmatrix},
$$

and let $A$ and $\mathbf{b}$ have the obvious meanings.

It is then given that both

$$
  A\mathbf{c} = \mathbf{b} \quad \text{and} \quad  A\mathbf{c'} = \mathbf{b}.
$$

From the rules just found it follows that

$$
 A(\mathbf{c} -\mathbf{c'}) = A\mathbf{c}  -A\mathbf{c'} =
 \mathbf{b} - \mathbf{b} = \mathbf{0},


$$

which show that the vector

$$
   (\mathbf{c} -\mathbf{c'}) = \mathbf{d}
$$

is a solution of the homogeneous system.
Note that

$$

  (\mathbf{c} -\mathbf{c'}) = \mathbf{d} \iff  \mathbf{c} = \mathbf{c'}+\mathbf{d}   \,\,\iff \,\,c_i = c'_i + d_i,\,i=1,\ldots, n.


$$

On the other hand, if $\mathbf{c'}$ is a solution of the linear system

$$
 A\mathbf{x} = \mathbf{b}
$$

and $\mathbf{d}$ is a solution of the homogeneous system

$$
A\mathbf{x} = \mathbf{0},
$$

then

$$
A(\mathbf{c'}+\mathbf{d}) = A\mathbf{c'}+A\mathbf{d} = \mathbf{b} + \mathbf{0} = \mathbf{b},
$$

so

$$
  \mathbf{c} = \mathbf{c'} + \mathbf{d}
$$

is a solution of the system

$$
 A\mathbf{x} = \mathbf{b}.
$$

The proof is basically the same as before, but using the matrix-vector product it can be written more concisely.

::::

::::{exercise}
:label: Exc:MatVecProduct:PracticeWithProp

(To practice with a proof as in the previous proposition.)

Suppose the linear system

$$
   \left\{\begin{array}{ccccccccc}
            a_{11}x_1\! & \!+\!&\!a_{12}x_2\! & \!+\!&\! \ldots\! & \!+\!&\!a_{1n}x_n  \! & \!=\!&\!  p_1 \\
            a_{21}x_1 \! & \!+\!&\!a_{22}x_2\! & \!+\!&\!\ldots\! & \!+\!&\!a_{2n}x_n  \! & \!=\!&\! p_2 \\
            \vdots \! & \! \!&\!  \vdots\! & \! \!&\!\cdots\! & \! \!&\! \vdots     \! & \! \!&\!  \vdots \\
            a_{m1}x_1 \! & \!+\!&\!a_{m2}x_2\! & \!+\!&\! \ldots\! & \!+\!&\!a_{mn}x_n \! & \!=\!&\! p_m \\
          \end{array}
   \right.
$$

is consistent and the linear system

$$
   \left\{\begin{array}{ccccccccc}
            a_{11}x_1\! & \!+\!&\!a_{12}x_2\! & \!+\!&\! \ldots\! & \!+\!&\!a_{1n}x_n  \! & \!=\!&\!  q_1 \\
            a_{21}x_1 \! & \!+\!&\!a_{22}x_2\! & \!+\!&\!\ldots\! & \!+\!&\!a_{2n}x_n  \! & \!=\!&\! q_2 \\
            \vdots \! & \! \!&\!  \vdots\! & \! \!&\!\cdots\! & \! \!&\! \vdots     \! & \! \!&\!  \vdots \\
            a_{m1}x_1 \! & \!+\!&\!a_{m2}x_2\! & \!+\!&\! \ldots\! & \!+\!&\!a_{mn}x_n \! & \!=\!&\! q_m \\
          \end{array}
   \right.
$$

is inconsistent. Show that the system

$$
   \left\{\begin{array}{ccccccccc}
            a_{11}x_1\! & \!+\!&\!a_{12}x_2\! & \!+\!&\! \ldots\! & \!+\!&\!a_{1n}x_n  \! & \!=\!&\!  r_1 \\
            a_{21}x_1 \! & \!+\!&\!a_{22}x_2\! & \!+\!&\!\ldots\! & \!+\!&\!a_{2n}x_n  \! & \!=\!&\! r_2 \\
            \vdots \! & \! \!&\!  \vdots\! & \! \!&\!\cdots\! & \! \!&\! \vdots     \! & \! \!&\!  \vdots \\
            a_{m1}x_1 \! & \!+\!&\!a_{m2}x_2\! & \!+\!&\! \ldots\! & \!+\!&\!a_{mn}x_n \! & \!=\!&\! r_m \\
          \end{array}
   \right.
$$

where $r_i = p_i - q_i,\,i=1,\ldots,\,m$ \, is inconsistent.

::::

:::{admonition} Solution to&nbsp;{numref}`Exc:MatVecProduct:PracticeWithProp`
:class: solution, dropdown

We start with some notations.

$$
 A = \left[\begin{array}{cccc}
            a_{11} & a_{12}&  \ldots&   a_{1n}   \\
            a_{21} & a_{22}&  \ldots&   a_{2n}   \\
            \vdots &  \vdots&  \cdots&  \vdots    \\
            a_{m1} & a_{m2}&  \ldots&   a_{mn}
          \end{array}   \right],
          \quad \mathbf{p} =
          \left[\begin{array}{c}
            p_1 \\ p_2 \\ \vdots \\ p_n
          \end{array}\right],
          \quad \mathbf{q} =
          \left[\begin{array}{c}
            q_1 \\ q_2 \\ \vdots \\ q_n
          \end{array}\right]
          \quad \mathbf{r} =
          \left[\begin{array}{c}
            r_1 \\ r_2 \\ \vdots \\ r_n
          \end{array}\right].
$$

In matrix-vector form the assumptions are that the system $A\vect{x}=\vect{p}$ is consistent and that the system $A\vect{x}=\vect{q}$ is inconsistent. Morever, $\vect{r} = \vect{p} - \vect{q}$.

We have to show that the system $A\vect{x}=\vect{r}$ cannot be consistent.

Let $\vect{x}_1$ be a solution for the (consistent) system $A\vect{x}=\vect{p}$.
If $\vect{x}_2$ would be a solution for the system $A\vect{x}=\vect{r}$, i.e.,
if $A\vect{x}_2=\vect{r}$, then $A(\vect{x}_1 -\vect{x}_2) = A\vect{x}_1 - A\vect{x}_2 = \vect{p} - \vect{r} = \vect{q}$, <BR>
so then the system $A\vect{x}=\vect{q}$ would be consistent. This is in clear contradiction we the assumption that the last system is inconsistent. <BR>
So a solution for the system $A\vect{x}=\vect{r}$ cannot exist.

::::

We now revisit the question we left open at the end of {numref}`Sec:LinearCombinations`: when is the span of a set of vectors in $\R^{n}$ all of $\R^{n}$?

::::{prf:proposition}
:label: Prop:LinearCombinations:SpanSolution

Let $\mathbf{v}_1, \ldots, \mathbf{v}_k$ be vectors in $\mathbb{R}^n$. Define the matrix $A$ such that

$$
A=
\begin{bmatrix} \mathbf{v}_1 & \mathbf{v}_2 & \ldots & \mathbf{v}_k \end{bmatrix}.
$$

The collection $\Span{\mathbf{v}_1, \ldots, \mathbf{v}_k}$ is equal to $\mathbb{R}^n$ if and only if the equation $A \mathbf{x}=\mathbf{b}$ has a solution for each $\mathbf{b}$ in $\mathbb{R}^n$.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:LinearCombinations:SpanSolution`
:class: tudproof

If $\Span{\mathbf{v}_1, \ldots, \mathbf{v}_k}$ is equal to $\mathbb{R}^n$, then each vector $\mathbf{b}$ in  $\mathbb{R}^n$  is a vector in the span of the vectors $\mathbf{v}_1, \ldots, \mathbf{v}_k$. This means that we can write $\mathbf{b}$ as a linear combination

$$
\mathbf{b}=x_1\mathbf{v}_1+ \ldots + x_k\mathbf{v}_k.
$$

Define the vector $\mathbf{x}$ such that

$$
\mathbf{x}=
\begin{bmatrix} x_1 \\ \vdots \\ x_k \end{bmatrix}.
$$

By definition of the matrix-vector product we now have

$$
A\mathbf{x} = x_1\mathbf{v}_1+ \ldots + x_k\mathbf{v}_k
 = \mathbf{b}.
$$

The proof of the other implication is similar.

::::

::::{prf:proposition}
:label: Prop:LinearCombinations:PivotInEachRow

The equation $A \mathbf{x}=\mathbf{b}$ has a solution for each $\mathbf{b}$ in $\mathbb{R}^n$ if and only if $A$ has a pivot position in each row.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:LinearCombinations:PivotInEachRow`
:class: tudproof

Suppose that $A$ does not contain a pivot position in each row. By definition of the reduced echelon form we know that the last row of $A$ does not have a pivot position. If $E$ is the reduced echelon form of $A$, then this means that the bottom row of $E$ contains only zeros. Let $\mathbf{e}_n$ be again the vector of which the last entry is equal to 1 and all other entries are equal to zero.

Since $E$ is the reduced form of $A$ we can find a sequence of elementary row operations $R_1, \ldots , R_m$ that transform in $A$ into $E$. Now take the augmented matrix $[E \, | \, \mathbf{e}_n]$ and perform the row operations $R_m^{-1}, \ldots , R_1^{-1}$, where $R_i^{-1}$ is the inverse row operation of $R_i$. We obtain a matrix $[A \, | \, \mathbf{b}]$, where $\mathbf{b}$ is a vector in $R^n$. Because $[E \, | \, \mathbf{e}_n]$ is the reduced echelon form of the augmented matrix $[A \, | \, \mathbf{b}]$ and $[E \, | \, \mathbf{e}_n]$ has a pivot in the last column, we know that $[A \, | \, \mathbf{b}]$ is inconsistent. This means that $A\mathbf{x}=\mathbf{b}$ does not have a solution.

On the other hand, if we assume that $A\mathbf{x}=\mathbf{b}$ does not have a solution for some $\mathbf{b}$ in $\mathbb{R}^n$, then the reduced echelon form $[E \, | \, \mathbf{c}]$ of the augmented matrix $[A \, | \, \mathbf{b}]$ has a pivot in the last column. Let us assume that this pivot is located in row $m$. The matrix $E$ cannot have a pivot in row $m$, but $E$ is also the reduced echelon form of $A$. This means that $A$ has no pivot position in row $m$.

::::

::::{prf:proposition}
:label: Prop:LinearCombinations:PivotSpanSolution

Let $\mathbf{v}_1, \ldots, \mathbf{v}_k$ be vectors in $\mathbb{R}^n$. Define the matrix $A$ by

$$
A=
\begin{bmatrix} \mathbf{v}_1 & \mathbf{v}_2 & \ldots & \mathbf{v}_k \end{bmatrix}.
$$

The following statements are equivalent:

<ol type ="i">
<li>

The set $\Span{\vect{v}_1, \ldots, \vect{v}_k}$ is equal to $\R^n$.

</li>
<li>

The equation $A \vect{x}=\vect{b}$ has a solution for each $\vect{b}$ in $\R^n$.

</li>
<li>

The matrix $A$ has a pivot position in each row.

</li>
</ol>

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:LinearCombinations:PivotSpanSolution`
:class: tudproof

This follows from {prf:ref}`Prop:LinearCombinations:SpanSolution` and {prf:ref}`Prop:LinearCombinations:PivotInEachRow`.

::::

::::{prf:example}

Is the span of the following three vectors equal to $\mathbb{R}^3$?

$$

\mathbf{v}_1=
\begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix} \quad \mathbf{v}_2=
\begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix} \quad \mathbf{v}_3=
\begin{bmatrix} 3 \\5 \\-1 \end{bmatrix}


$$

We can use {prf:ref}`Prop:LinearCombinations:PivotSpanSolution` to solve this problem. We will first use these vectors as the columns of a matrix $A$.

$$

A=
\begin{bmatrix} 1 & 0 & 3 \\ 1 & 1 & 5 \\ -1 & 1 & -1 \end{bmatrix}


$$

The three given vectors span the entire space $\mathbb{R}^3$ if and only if the matrix $A$ has three pivot positions. Using elementary row operations we find that A has the following reduced echelon form:

$$

A=
\begin{bmatrix} 1 & 0 & 3 \\ 1 & 1 & 5 \\ -1 & 1 & -1 \end{bmatrix}\sim
\begin{bmatrix} 1 & 0 & 3 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{bmatrix}.
$$

Since there are only two pivots in the reduced echelon matrix, we know that $\mathbf{v}_1$, $\mathbf{v}_2$ and $\mathbf{v}_3$ do not span the space $\mathbb{R}^3$.

::::

::::{prf:proposition}
:label: Prop:LinearCombinations:SpanNotRn

If $\mathbf{v}_1, \dots ,\mathbf{v}_k$ are vectors in $\mathbb{R}^n$ and $k<n$, then the span of $\mathbf{v}_1, \dots ,\mathbf{v}_k$ is not equal to $\mathbb{R}^n$.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:LinearCombinations:SpanNotRn`
:class: tudproof

Use the vectors $\mathbf{v}_1, \dots ,\mathbf{v}_k$ as the columns for a matrix $A$. By definition, the matrix $A$ is an $n\times k$ matrix. Let $E$ be the reduced echelon form of $A$. Since $E$ has $k$ columns we know that $E$ can have at most $k$ pivots. Because $k<n$ this means that the number of pivots is less than $n$. Therefore, we find that the number of pivots is less than the number of rows in $E$. This implies that it is impossible for $E$ to have a pivot in each row. {prf:ref}`Prop:LinearCombinations:PivotSpanSolution` now tells us that the span of the vectors $\mathbf{v}_1, \dots ,\mathbf{v}_k$ cannot be equal to $\mathbb{R}^n$.

::::

## Grasple Exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5708acc0-9a35-429b-85ff-43139eed1722?id=85086
:label: grasple_exercise_2_4_1
:dropdown:
:description: For a given matrix $A$, does the equation $A\vect{x}=\vect{b}$ have a solution for every $\vect{b}$?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3cb73c25-fa69-4cf1-a686-1e71f2f0bf89?id=85092
:label: grasple_exercise_2_4_2
:dropdown:
:description: For a given matrix $A$, does the equation $A\vect{x}=\vect{b}$ have a solution for every $\vect{b}$?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/56cf013b-dc6a-4774-ac1e-fa694b16a2a8?id=85089
:label: grasple_exercise_2_4_3
:dropdown:
:description: For a given matrix $A$, does the equation $A\vect{x}=\vect{b}$ have a solution for every $\vect{b}$?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/dba850cd-e353-4339-9811-656a565e7270?id=85091
:label: grasple_exercise_2_4_4
:dropdown:
:description: Using a vector equation to find solution of a linear system.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/194dcee8-b5e7-42af-8ab0-c40c4fce47a4?id=114628
:label: grasple_exercise_2_4_5
:dropdown:
:description: Between matrox-vector and vector-vector equation.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6332f523-a152-4be7-b160-bb0bab18a4a0?id=69773
:label: grasple_exercise_2_4_6
:dropdown:
:description: If $A\vect{x}=\vect{b}$ has a unique solution, what about $A\vect{x}=\vect{0}$?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/cd77f0bd-bd35-4674-9524-38a9446cd076?id=70183
:label: grasple_exercise_2_4_7
:dropdown:
:description: What if the zero vector is a solution to $A\vect{x}=\vect{b}$?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5bdcebc9-3ab6-4b64-9f30-033cb9f79b80?id=76273
:label: grasple_exercise_2_4_8
:dropdown:
:description: About the 'sum' of two systems $A_1\vect{x}=\vect{b}_1$, $A_2\vect{x}=\vect{b}_2$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5ccac4fe-bf25-471e-b268-5add4b06ecfe?id=76278
:label: grasple_exercise_2_4_9
:dropdown:
:description: About the 'stack' of two systems $A_1\vect{x}=\vect{b}_1$, $A_2\vect{x}=\vect{b}_2$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e8dfc02b-2628-44f0-8a57-bed3fb0cbb26?id=77658
:label: grasple_exercise_2_4_10
:dropdown:
:description: What if $A\vect{v}= A\vect{w} = \vect{b}$?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/525d98b9-7cd3-40be-80e9-6d2f65f26002?id=77661
:label: grasple_exercise_2_4_11
:dropdown:
:description: Given $ A\vect{v} = A\vect{w} = \vect{b}$, how to create more solutions.

::::
