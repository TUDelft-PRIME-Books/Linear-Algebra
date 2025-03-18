(Sec:LinTrafo)=

# Linear Transformations

(Subsec:LinTrafo:MatrixTrafo)=

## Introduction

Until now we have used matrices in the context of linear systems. The equation

$$
 A\mathbf{x} = \mathbf{b},
$$

where $A$ is an $m \times n$ matrix, is just a concise way to write down a system of $m$ linear equations in $n$
unknowns.
A different way to look at this matrix equation is to consider it as an input-output system:
the left-hand side $A\mathbf{x}$
can be seen as a mapping that sends an "input" $\mathbf{x}$ to an "output" $\mathbf{y}= A\mathbf{x}$.

For instance, in computer graphics, typically points describing a 3D object have to be converted to points in 2D, to be able to visualize them on a screen. Or, in a dynamical system, a
matrix $A$ may describe how a system evolves from a "state" $\mathbf{x}_{k}$ at time $k$ to a state $\mathbf{x}_{k+1}$ at time $k+1$ via 

$$
    \mathbf{x}_{k+1} = A\mathbf{x}_{k}.
$$

A "state" may be anything ranging from a set of particles at certain positions, a set of pixels describing a minion, concentrations of chemical substances in a reactor tank, to population sizes of different species.
Thinking mathematically we would describe such an input-output interpretation as a
transformation (or: function, map, mapping, operator, .... )

$$
   T: \mathbb{R}^n \to \mathbb{R}^m.
$$

We will see that these matrix transformations have two characteristic properties  
which makes them the protagonists of the more general linear algebra concept of a **linear transformation**.

(Subsec:MatrixTrafo)=

## Matrix transformations

Let $A$ be an $m\times n$ matrix. We can in a natural way associate a transformation $T_A:\mathbb{R}^n \to \mathbb{R}^m$ &nbsp; to the matrix $A$.

::::::{prf:definition}
The transformation $T_A$ corresponding to the $m\times n$ matrix $A$
is the mapping defined by

$$
   T_A(\mathbf{x}) = A\mathbf{x} \quad \text{or } \quad  T_A:\mathbf{x} \mapsto A\mathbf{x},
$$

where $\mathbf{x} \in \mathbb{R}^n$.

We call such a mapping a **matrix transformation**. Conversely we say that the matrix $A$ **represents** the transformation $T_A$.

::::::

As a first example consider the following.

::::::{prf:example}
:label: Ex:LinTrafo:FirstMatrixTrafo

The transformation corresponding to the matrix
$A = \begin{bmatrix} 1 & 2 & 0\\ 1 & 2 & 1 \end{bmatrix}$ is defined by

$$
   T_A(\mathbf{x}) =
        \begin{bmatrix}
            1 & 2 & 0\\ 1 & 2 & 1
\end{bmatrix}\mathbf{x}.
$$

We have, for instance

$$
\begin{bmatrix}
        1 & 2 & 0\\ 1 & 2 & 1
\end{bmatrix}
\begin{bmatrix}
       1\\1\\1
\end{bmatrix} =
\begin{bmatrix}
        3 \\ 4
\end{bmatrix}
   \quad \text{and} \quad
\begin{bmatrix}
        1 & 2 & 0\\ 1 & 2 & 1
\end{bmatrix}
\begin{bmatrix}
       2\\-1\\0
\end{bmatrix} =
\begin{bmatrix}
       0\\ 0
\end{bmatrix}.
$$

According to the definition of the matrix-vector product we can also write

:::{math}
:label: Eq:LinTrafo:AxIsLinearCombination

A\mathbf{x} = \begin{bmatrix}
1 & 2 & 0\\ 1 & 2 & 1  
 \end{bmatrix}
\begin{bmatrix}
x_1\\x_2\\x_3  
 \end{bmatrix} =
x_1  
 \begin{bmatrix}
1\\ 1  
 \end{bmatrix}+
x_2  
 \begin{bmatrix}
2 \\ 2  
 \end{bmatrix}+
x_3  
 \begin{bmatrix}
0\\ 1  
 \end{bmatrix}.

:::

::::::

We recall that for a transformation $T$ from a domain $D$ to a codomain $E$ the range $R= R_T$ is defined as the set of all images of elements of $D$ in $E$:

$$
   R_T = \{\text{ all images  } T(x), \, \text{  for  } x \text{  in  }D\}.
$$

::::::{prf:remark}
:label: Ex:LinTrafo:FirstMatrixTrafoContinued

From Equation {eq}`Eq:LinTrafo:AxIsLinearCombination`
it is clear that the range of the matrix transformation in {prf:ref}`Ex:LinTrafo:FirstMatrixTrafo`
consists of all linear combinations of the three columns of $A$:

$$
\text{Range}(T_A) =
\Span{ \begin{bmatrix} 1\\ 1   \end{bmatrix}, \begin{bmatrix} 2 \\  2  \end{bmatrix}, \begin{bmatrix} 0\\  1  \end{bmatrix}}.
$$

In a later chapter ({numref}`Sec:SubspacesRn`, <FONT color ="#0076C2"> Subspaces of $\R^n$</FONT>) we will call this the **column space** of the matrix $A$.

::::::

The first example leads to a first property of matrix transformations:

::::::{prf:proposition}
:label: Prop:LinTrafo:RangeTA

Suppose

$$
A = \begin{bmatrix}
 \mathbf{a}_1 & \mathbf{a}_2 & \ldots & \mathbf{a}_n
\end{bmatrix}
$$

is an $m\times n$ matrix.

Then the range of the matrix transformation corresponding to $A$ is the span of the columns of $A$:

$$
   \text{Range}(T_A) = \Span{\mathbf{a}_1, \mathbf{a}_2,\ldots,\mathbf{a}_n }.
$$

::::::

::::::{prf:example}
:label: Ex:LinTrafo:SecondMatrixTrafo

The matrix

$$
 A = \begin{bmatrix}
 1 & 0 \\ 0 & 1 \\ 0 & 0
\end{bmatrix}
$$

leads to the transformation

$$
 T: \mathbb{R}^2 \to \mathbb{R}^3, \quad
 T \left(\begin{bmatrix}
        x \\ y
\end{bmatrix}\right)=
\begin{bmatrix}
        1 & 0 \\ 0 & 1 \\ 0 & 0
\end{bmatrix}
\begin{bmatrix}
        x \\ y
\end{bmatrix}    =
\begin{bmatrix}
        x \\ y \\0
\end{bmatrix}.
$$

This transformation "embeds" the plane $\mathbb{R}^2$ into the space $\mathbb{R}^3$, as depicted in {numref}`Figure %s <Fig:LinTrafo:EmbedR2R3>`.

```{applet}
:url: linear_transformation/embed_r2_r3
:fig: Images/Fig-LinTrafo-EmbedR2R3.svg
:name: Fig:LinTrafo:EmbedR2R3
:status: reviewed
:class: dark-light

$T$  embeds  $\mathbb{R}^2$ into $\mathbb{R}^3$.
```

The range of this transformation is the span of the two vectors

$$
   \mathbf{e}_1  =
\begin{bmatrix}
 1\\ 0 \\ 0
\end{bmatrix} \quad \text{and} \quad
    \mathbf{e}_2  =
\begin{bmatrix}
 0\\ 1 \\ 0
\end{bmatrix},
$$

which is the $xy$-plane in $\mathbb{R}^3$.

::::::

For $2\times2$ and $3\times3$ matrices the transformations often have a geometric interpretation, as the following example illustrates.

::::::{prf:example}
:label: Eq:LinTrafo:SkewProjection

The transformation corresponding to the matrix

$$
A = \begin{bmatrix}
        1 &  1  \\ 0 & 0
\end{bmatrix}
$$

is the mapping

$$
  T: \mathbb{R}^2 \to \mathbb{R}^2, \quad  T\left(\begin{bmatrix}
        x \\ y
\end{bmatrix}\right)=
\begin{bmatrix}
        x +y \\ 0
\end{bmatrix}.
$$

First we observe that the range of this transformation consists of all multiples of the vector $ \begin{bmatrix} 1 \\ 0 \end{bmatrix} $, 
i.e. the $x$-axis in the plane.

Second, let us find the set of points/vectors that is mapped to an arbitrary point
$\begin{bmatrix} c \\ 0 \end{bmatrix}$ in the range. For this we solve

$$
  A\mathbf{x} = \begin{bmatrix}
                1 &  1  \\ 0 & 0
              \end{bmatrix}
\begin{bmatrix}
                  x  \\ y
\end{bmatrix} =
\begin{bmatrix}
                c \\ 0
\end{bmatrix},
  \quad \text{so} \quad
\begin{bmatrix}
        x+y \\ 0
\end{bmatrix}  =
\begin{bmatrix}
        c \\ 0
\end{bmatrix}.
$$

The points whose coordinates satisfy this equation all lie on the line described by the equation

$$
   x + y = c.
$$

So what the mapping does is to send all points on a line $\mathcal{L}:x + y = c$ to the point $(c,0)$, which is the intersecting of this line with the $x$-axis. <BR>
An alternative way to describe it: it is the skew projection, in the direction $\begin{bmatrix} 1 \\ -1 \end{bmatrix}$ onto the $x$-axis.
See {numref}`Figure %s <Fig:LinTrafo:SkewProjection>`.

::::{figure} Images/Fig-LinTrafo-SkewProjection.svg
:name: Fig:LinTrafo:SkewProjection
:class: dark-light

The transformation of {prf:ref}`Eq:LinTrafo:SkewProjection`.
::::

::::::

::::::{exercise}
:label: Exc:Lintrafo:VectorInRange?

Find out whether the vectors

$$
 \mathbf{y}_1 =
\begin{bmatrix}
 2 \\ 1 \\ 0
\end{bmatrix} \quad \text{and} \quad
 \mathbf{y}_2 =
\begin{bmatrix}
 2 \\ 0 \\ 1
\end{bmatrix}
$$

are in the range of the matrix transformation

$$
  T(\mathbf{x}) = A\mathbf{x} =
\begin{bmatrix}
 1 &1&1 \\ 1 &-1&3 \\ -1&2&-4
\end{bmatrix}\mathbf{x}.
$$

::::::

We close this subsection with an example of a matrix transformation representing a very elementary dynamical system.

::::::{prf:example}
:label: Ex:LinTrafo:MigrationModel

Consider a model with two cities between which over a fixed period of time migrations take place. Say in a period of ten years 90\% of the inhabitants in city $A$ stay in city $A$ and 10\% move to city $B$. From city $B$ 20\% of the citizens move to $A$, so 80\% stay in city $B$. <BR>  
The following table contains the relevant statistics:

$$
  \begin{array}{c|cc} & A & B \\ \hline
      A & 0.9 & 0.2 \\
      B & 0.1 & 0.8 \\ \hline
  \end{array}
$$

For instance, if at time 0 the population in city $A$ amounts to 50 (thousand) and in city $B$ live 100 (thousand) people, then at the end of one period the population in city $A$
amounts to

$$
  0.9 \times 50 + 0.2 \times 100 = 55.
$$

Likewise for city $B$.

If we denote the population sizes after $k$ periods by a vector

$$
   \mathbf{x}_k =
\begin{bmatrix}
 x_k \\ y_k
\end{bmatrix}
$$

it follows that

$$
\begin{bmatrix}
 x_{k+1} \\ y_{k+1}
\end{bmatrix} =
\begin{bmatrix}
 0.9x_k + 0.2y_k  \\0.1x_k + 0.8y_k
\end{bmatrix}, \quad
   \text{i.e.,   }
   \mathbf{x}_{k+1} =
\begin{bmatrix}
 0.9 & 0.2  \\ 0.1 & 0.8
\end{bmatrix}
\begin{bmatrix}
 x_k \\ y_k
\end{bmatrix} = M \mathbf{x}_{k}.
$$

The $M$ stands for migration matrix.

Obviously this model can be generalized to a "world" with any number of cities.

::::::

(Subsec:LinTrafo:LinTrafo)=

## Linear transformations

In the previous section we saw that the matrix transformation $\mathbf{y}=A\mathbf{x}$ can also be seen as a mapping $T(\mathbf{x}) = A\mathbf{x}$.  
This mapping has two characteristic properties on which we will focus in this section.

::::::{prf:definition}
:label: Dfn:LinTrafo:LinTrafo

A **linear transformation** is a function $T$ from $\mathbb{R}^n$ to $\mathbb{R}^m$ that has the following properties

<ol type="i">
<li>

For all vectors $\mathbf{v}_1,\,\mathbf{v}_2$ in $\mathbb{R}^n$:

<BR>

$$
     T(\mathbf{v}_1+\mathbf{v}_2) = T(\mathbf{v}_1) + T(\mathbf{v}_2).
$$

</li>
<li>

For all vectors $\mathbf{v}$ in $\mathbb{R}^n$ and all scalars $c$ in $\mathbb{R}$:

<BR>

$$
     T(c\mathbf{v}) = c\,T(\mathbf{v}).
$$

</li>
</ol>

::::::

::::::{exercise}
:label: Exc:LinTrafo:ImageofZeroVector

Show that a linear transformation from $\mathbb{R}^n$ to $\mathbb{R}^m$ always sends the zero vector in $\R^n$ to the zero vector in $\R^m$.
<BR>
Thus, if $ T:\mathbb{R}^n \to\mathbb{R}^m$ is a linear transformation, then $T(\mathbf{0}_n) = \mathbf{0}_m$.

::::::

::::::{admonition} Solution to&nbsp;{numref}`Exc:LinTrafo:ImageofZeroVector`
:class: solution, dropdown

If $ T:\mathbb{R}^n \to\mathbb{R}^m$ is linear, and $\vect{v}$ is any vector in $\R^n$, then $\mathbf{0}_n = 0\vect{v}$. From the second property in {prf:ref}`Dfn:LinTrafo:LinTrafo` it follows that

$$
  T(\mathbf{0}_n) = T(0\vect{v}) = 0\,T(\vect{v}) = \mathbf{0}_m.
$$

::::::

::::::{prf:example}
:label: Ex:LinTrafo:FirstLinearMap

Consider the map $T:\mathbb{R}^2\rightarrow\mathbb{R}^3$ that sends each vector
$\begin{bmatrix}
 x \\ y 
\end{bmatrix}$
in $\mathbb{R}^2$ to the vector
$\begin{bmatrix}
 x \\ y \\ 0 
\end{bmatrix}$ in $\mathbb{R}^3$.
Let us check that this a linear map.

For that, we need to check the two properties in the definition.
<BR>
For property (i) we take two arbitrary vectors

$$
\begin{bmatrix}
    x_1 \\ y_1
\end{bmatrix} \quad \text{ and }\quad
\begin{bmatrix}
 x_2 \\ y_2
\end{bmatrix}  \quad \text{in} \quad \mathbb{R}^2,
$$

and see:

$$
    T\left(\begin{bmatrix}
        x_1 \\ y_1
\end{bmatrix} +
\begin{bmatrix}
        x_2 \\ y_2
\end{bmatrix} \right)=
    T \left(\begin{bmatrix}
        x_1+x_2 \\ y_1+y_2
\end{bmatrix}\right)=
\begin{bmatrix}
            x_1 + x_2 \\ y_1 + y_2 \\ 0
\end{bmatrix} =
\begin{bmatrix}
            x_1 \\ y_1 \\ 0
\end{bmatrix} +
\begin{bmatrix}
            x_2 \\ y_2 \\ 0
\end{bmatrix}.
$$

This last vector indeed equals

$$
 T\left(\begin{bmatrix}
            x_1 \\ y_1
\end{bmatrix}\right)+
        T\left(\begin{bmatrix}
            x_2 \\ y_2
\end{bmatrix}\right).
$$

Similarly, for the second property, given any scalar $c$,

$$
    T\left(c \begin{bmatrix}
        x_1 \\ y_1
\end{bmatrix}\right)=
    T \left(\begin{bmatrix}
        c x_1 \\  cy_1
\end{bmatrix}\right)=
\begin{bmatrix}
        c x_1 \\ c y_1 \\ 0
\end{bmatrix} =
    c \begin{bmatrix}
        x_1 \\ y_1 \\ 0
\end{bmatrix}=
        cT \left(\begin{bmatrix}
            x_1 \\ y_1
\end{bmatrix}\right).
$$

So indeed $T$ has the two properties of a linear transformation.

::::::

::::::{prf:example}
Consider the mapping
$T:\mathbb{R}^2\rightarrow\mathbb{R}^2$ that sends each vector $ \begin{bmatrix}
x \\ y
\end{bmatrix}$
in $\mathbb{R}^2$ to the vector $\begin{bmatrix} x+y \\ xy \end{bmatrix}$:

$$
  T:  \begin{bmatrix}
 x \\ y
\end{bmatrix} \mapsto
\begin{bmatrix}
 x+y \\ xy
\end{bmatrix}
$$

This mapping is **not** a linear transformation.

$$
    T \left(\begin{bmatrix}
 1 \\ 1
\end{bmatrix} +
\begin{bmatrix}
 1 \\ 2
\end{bmatrix}\right)=
    T
\left(\begin{bmatrix}
2 \\ 3
\end{bmatrix}\right)    =
\begin{bmatrix}
 5 \\ 6
\end{bmatrix},
$$

whereas

$$
   T \left(\begin{bmatrix}
 1 \\ 1
\end{bmatrix}\right)+
   T \left(\begin{bmatrix}
 1 \\ 2
\end{bmatrix}\right)=
\begin{bmatrix}
 2 \\ 1
\end{bmatrix} +
\begin{bmatrix}
 3 \\ 2
\end{bmatrix} =
\begin{bmatrix}
 5 \\ 3
\end{bmatrix}
       \,\neq\,
\begin{bmatrix}
 5 \\ 6
\end{bmatrix} .
$$

The second requirement of a linear transformation is violated as well:

$$
   T\left(3
\begin{bmatrix}
 1 \\ 1
\end{bmatrix}\right)=
   T
\left(\begin{bmatrix}
 3 \\ 3
\end{bmatrix}\right)=
\begin{bmatrix}
 6 \\ 9
\end{bmatrix}
   \,\,\neq\,\,
   3\,T
\left(\begin{bmatrix}
 1 \\ 1
\end{bmatrix} \right)=
   3
\begin{bmatrix}
 2 \\ 1
\end{bmatrix} =
\begin{bmatrix}
 6 \\ 3
\end{bmatrix}.
$$

::::::

::::::{exercise}
:label: Exc:LinTrafo:T(x)=x+p

Let $\mathbf{p}$ be a nonzero vector in $\mathbb{R}^2$. &nbsp;  Is the translation

$$
   T\!:\mathbb{R}^2 \to \mathbb{R}^2, \quad  \mathbf{x} \mapsto \mathbf{x} + \mathbf{p}
$$

a linear transformation?

::::::

::::::{admonition} Solution to&nbsp;{numref}`Exc:LinTrafo:T(x)=x+p`
:class: solution, dropdown

The transformation defined by $T(\vect{x}) = \vect{x} + \vect{p}$, with $\vect{p}\neq \vect{0}$ does not have any of the two properties of a linear transformation.

For instance, since $\vect{p}+\vect{p} \neq \vect{p}$,

$$
  T(\vect{x}+\vect{y}) = \vect{x}+\vect{y} + \vect{p} \neq
  T(\vect{x})+T(\vect{y}) = \vect{x}+ \vect{p} +\vect{y} + \vect{p}.
$$

::::::

Note that {prf:ref}`Ex:LinTrafo:FirstLinearMap` was in fact the first example of a matrix transformation in the {ref}`Subsec:LinTrafo:MatrixTrafo`:

$$
\begin{bmatrix}
 x \\ y
\end{bmatrix}  \mapsto
\begin{bmatrix}
 x \\ y \\ 0
\end{bmatrix}
   =
\begin{bmatrix}
 1 & 0 \\ 0&1 \\ 0&0
\end{bmatrix}
\begin{bmatrix}
 x \\ y
\end{bmatrix}
$$

As we will see: **any** linear transformation from $\mathbb{R}^n$ to $\mathbb{R}^m$ is a matrix transformation. The converse is true as well. This is the content of the next proposition.

::::::{prf:proposition}
:label: Prop:LinTrafo:MatrixTrafoIsLinear

Each matrix transformation is a linear transformation.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:LinTrafo:MatrixTrafoIsLinear`
:class: tudproof

This is a direct consequence of the two properties of the matrix-vector product ({prf:ref}`Prop:MatVecProduct:Linearity`) that say

$$
  A\,(\mathbf{x}+\mathbf{y} ) = A\mathbf{x} + A\mathbf{y} \quad \text{and} \quad
   A\,(c\mathbf{x}) = c\,A\mathbf{x}.
$$

::::::

::::::{prf:proposition}
:label: Prop:LinTrafo:CompositionLintrafos

Suppose $T:  \mathbb{R}^n\to\mathbb{R}^m$ and $S:\mathbb{R}^m\to\mathbb{R}^p$ are linear transformations.
Then the transformation $S\circ T:\mathbb{R}^n\to\mathbb{R}^p $ defined by

$$
S\circ T(\mathbf{x}) = S(T(\mathbf{x}))
$$

is a linear transformation from $\mathbb{R}^n$ to $\mathbb{R}^p$.

::::::

::::::{prf:remark}

The transformation $S\circ T$ is called the **composition** of the two transformations $S$ and $T$. It is best read as _"$S$ after $T$"_.
::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:LinTrafo:CompositionLintrafos`
:class: tudproof

Suppose that

$$
  T(\mathbf{x}+\mathbf{y}) = T(\mathbf{x})+T(\mathbf{y})\quad \text{and} \quad T(c\mathbf{x}) = cT(\mathbf{x}), \quad \text{for}\,\, \mathbf{x}, \mathbf{y} \quad \text{in  } \mathbb{R}^n,
      \,\, c \text{  in  } \mathbb{R}
$$

and likewise for $S$. Then

$$
 \begin{array}{rl}
  S\circ T(\mathbf{x}+\mathbf{y})  = S(T(\mathbf{x}+\mathbf{y})) = S( T(\mathbf{x})+T(\mathbf{y})) \!\!\!\!&
  = S(T(\mathbf{x})) + S(T(\mathbf{y})) \\
  & = S\circ T(\mathbf{x}) + S\circ T(\mathbf{y}) \end{array}
$$

and

$$
  S\circ T(c\mathbf{x}) =  S(T(c\mathbf{x})) =  S(cT(\mathbf{x})) = c\,S(T(\mathbf{x})) = c\,S\circ T(\mathbf{x}).
$$

Hence $S\circ T$ satisfies the two requirements of a linear transformation.

::::::

In words: the composition/concatenation of two linear transformations is itself a linear transformation.

::::::{exercise}
:label: Exc:LinTrafo:CombiningLinTrafos

There are other ways to combine linear transformations.

The sum $S = T_1 + T_2$ of two linear transformation $T_1,T_2: \mathbb{R}^n \to \mathbb{R}^m$ is defined as follows

$$
   S: \mathbb{R}^n \to \mathbb{R}^m, \quad S(\mathbf{x}) = T_1(\mathbf{x}) + T_2(\mathbf{x}).
$$

And the (scalar) multiple $T_3 = cT_1$ is the transformation

$$
  T_3: \mathbb{R}^n \to \mathbb{R}^m, \quad T_3(\mathbf{x}) = cT_1(\mathbf{x}).
$$

Show that $S$ and $T_3$ are again linear transformations.

::::::

::::::{admonition} Solution to&nbsp;{numref}`Exc:LinTrafo:CombiningLinTrafos`
:class: solution, dropdown

The properties of the linear transformatiuon $T_1$ and $T_2$ carry over to $S$ and $T_3$ in the following way.
We check the properties one by one.

For the sum $S$ we have

<ol type="i">
<li>

For all vectors $\mathbf{v}_1,\,\mathbf{v}_2$ in $\R^n$ <BR>

$$
   \begin{array}{rcl}
     S(\mathbf{v}_1+\mathbf{v}_2) &=& T_1(\mathbf{v}_1+\mathbf{v}_2) +
     T_2(\mathbf{v}_1+\mathbf{v}_2)\\
     &=& T_1(\mathbf{v}_1) + T_1(\mathbf{v}_2) + T_2(\mathbf{v}_1) + T_2(\mathbf{v}_2)\\
     &=& T_1(\mathbf{v}_1) + T_2(\mathbf{v}_1) + T_1(\mathbf{v}_2)  + T_2(\mathbf{v}_2)\\
     &=& S(\mathbf{v}_1)+S(\mathbf{v}_2).
   \end{array}
$$

</li>
<li>

And likewise, for all vectors $\mathbf{v}$ in $\mathbb{R}^n$ and all scalars $c$ in $\mathbb{R}$: <BR>
%$S(c\mathbf{v}) = T_1(c\mathbf{v})+T_2(c\mathbf{v}) = cT_1(\mathbf{v})+cT_2(\mathbf{v}) = c\big(T_1(\mathbf{v})+cT_2(\mathbf{v})\big)= cS(\mathbf{v})$.

$$
   \begin{array}{rcl}
     S(c\mathbf{v}) &=& T_1(c\mathbf{v})+T_2(c\mathbf{v}) \\
     &=& cT_1(\mathbf{v})+cT_2(\mathbf{v}) \\
     &=& c \big(T_1(\mathbf{v})+cT_2(\mathbf{v})\big)\\
     &=& cS(\mathbf{v}).
   \end{array}
$$

</li>
</ol>

The linearity of $T_3$ is verified in a similar manner.
::::::

And now, let us return to matrix transformations.

(Subsec:LinTrafo:LinTrafoeqMatrixTrafo)=

## Standard matrix for a linear transformation

We have seen that every matrix transformation is a linear transformation. In this subsection we will show that conversely
every linear transformation $T:\mathbb{R}^n \to \mathbb{R}^m$ can be represented by a matrix transformation.

The key to construct a matrix that represents a given linear transformation lies in the following proposition.

::::::{prf:proposition}
:label: Prop:LinTrafo:ExtendedLinearity

Suppose $T:\mathbb{R}^n\rightarrow\mathbb{R}^m$ is a linear transformation. Then the following property holds: for
each set of vectors $\mathbf{x}_1,  \ldots, \mathbf{x}_k$ in $\mathbb{R}^n$ and each set of numbers $c_1,\ldots,c_k$ in $\mathbb{R}$:

:::::{math}
:label: Eq:LinTrafo:LinComb

T(c_1\mathbf{x}_1+c_2 \mathbf{x}_2+\ldots +c_k \mathbf{x}_k) =
c_1T(\mathbf{x}_1)+c_2T(\mathbf{x}_2)+\ldots +c_kT( \mathbf{x}_k).

:::::

::::::

In words: for any linear transformation
_the image of a linear combination of vectors is equal to the linear combination of their images_.

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:LinTrafo:ExtendedLinearity`
:class: tudproof

Suppose $T:\mathbb{R}^n\rightarrow\mathbb{R}^m$ is a linear transformation.

So we have

$$
  \text{(i) } T(\mathbf{x}+\mathbf{y}) = T(\mathbf{x})+T(\mathbf{y}) \quad\text{and} \quad \text{(ii)  }
    T(c\mathbf{x}) = c T(\mathbf{x}).
$$

First apply rule (i) to split the term on the left in {eq}`Eq:LinTrafo:LinComb` into $k$ terms:

$$
\begin{array}{ccl}
T(c_1\mathbf{x}_1+c_2 \mathbf{x}_2+\ldots +c_k \mathbf{x}_k)  &=&
  T(c_1\mathbf{x}_1)+T(c_2 \mathbf{x}_2+\ldots +c_k \mathbf{x}_k) \\
  &=&  \quad  \ldots   \\
  &=& T(c_1\mathbf{x}_1)+T(c_2 \mathbf{x}_2)+\ldots + T(c_k \mathbf{x}_k)
 \end{array}
$$

and then apply rule (ii) to each term.

::::::

::::::{prf:example}
:label: Ex:LinTrafo:ExtendedLinearity

Suppose $T: \mathbb{R}^3 \to \mathbb{R}^2$ is a linear transformation, and we know that for

$$
  \vect{a}_1 =
\begin{bmatrix}
 1 \\ 0 \\ 0
\end{bmatrix}, \quad
  \vect{a}_2 =
\begin{bmatrix}
 1 \\ 1 \\ 0
\end{bmatrix},
  \quad \vect{a}_3 =
\begin{bmatrix}
 1 \\ 1 \\ 1
\end{bmatrix}
$$

the images under $T$ are given by

$$
  T(\vect{a}_1)  = \vect{b}_1 =
\begin{bmatrix}
 1 \\ 2
\end{bmatrix}, \quad T(\vect{a}_2)  = \vect{b}_2 =
\begin{bmatrix}
 3 \\ -1
\end{bmatrix},
  \quad \text{and} \quad  T(\vect{a}_3)  = \vect{b}_3 =
\begin{bmatrix}
 2 \\ -2
\end{bmatrix}.
$$

Then for the vector

$$
 \vect{v} =
\begin{bmatrix}
 4 \\ 1 \\ -1
\end{bmatrix} = 3 \vect{a}_1 + 2 \vect{a}_2 - 1 \vect{a}_3
$$

it follows that

$$
 T(\vect{v}) =   3 \vect{b}_1 + 2 \vect{b}_2  + (-1) \vect{b}_3 =
 3
\begin{bmatrix}
 1 \\ 2
\end{bmatrix}
 + 2
\begin{bmatrix}
 3 \\ -1
\end{bmatrix}
 + (-1)
\begin{bmatrix}
 2 \\ -2
\end{bmatrix}=
\begin{bmatrix}
 7 \\ 6
\end{bmatrix}.
$$

::::::

The central idea illustrated in {prf:ref}`Ex:LinTrafo:ExtendedLinearity`, which is in fact a direct consequence of {prf:ref}`Prop:LinTrafo:ExtendedLinearity`, is the following:

a linear transformation $T$ from $\mathbb{R}^n$ to $\mathbb{R}^m$ is completely specified by the images
$ T(\mathbf{a}_1), T(\mathbf{a}_2), \ldots , T(\mathbf{a}_n)$ of a set of vectors $\{\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_n\}$ that spans $\mathbb{R}^n$. 

The simplest set of vectors that spans the whole space $\mathbb{R}^n$ is
the standard basis for $\mathbb{R}^n$ which was introduced in the section {ref}`Sec:LinearCombinations`.

Recall that this is the set of vectors

:::{math}
:label: Eq:LinTrafo:StandardBasis

\left(\vect{e}_1,\mathbf{e}_2, \ldots, \mathbf{e}_n\right)=
\left(\begin{bmatrix}
1 \\ 0 \\ 0 \\ \vdots \\ 0
\end{bmatrix},
\begin{bmatrix}
0 \\ 1 \\ 0 \\ \vdots \\ 0
\end{bmatrix},
\quad \cdots \quad ,
\begin{bmatrix}
0 \\ 0 \\ 0 \\ \vdots \\ 1
\end{bmatrix}\right).

:::

The next example gives an illustration of the above, and it also leads the way to
the construction of a matrix for an arbitrary linear transformation.

::::::{prf:example}
:label: Ex:LinTrafo:StandardMatrixIntro

Suppose $T$ is a linear transformation from $\mathbb{R}^2$ to $\mathbb{R}^2$ for which

$$
   T(\mathbf{e}_1) = \mathbf{a}_1  =
\begin{bmatrix}
1 \\2
\end{bmatrix},
   \quad
   T(\mathbf{e}_2) = \mathbf{a}_2  =
\begin{bmatrix}
4 \\3
\end{bmatrix}.
$$

Then for an arbitrary vector

$$
  \mathbf{x} =
\begin{bmatrix}
x_1\\x_2
\end{bmatrix} =
        x_1
\begin{bmatrix}
1\\0
\end{bmatrix} +
        x_2
\begin{bmatrix}
0\\1
\end{bmatrix}
     = x_1\mathbf{e}_1 + x_2\mathbf{e}_2,
$$

it follows that

$$
 \begin{array}{rcl}
  T(\mathbf{x}) &=& x_1T(\mathbf{e}_1) + x_2T(\mathbf{e}_2) \\
               &=& x_1
\begin{bmatrix}
1 \\2
\end{bmatrix}
               + x_2
\begin{bmatrix}
4 \\3
\end{bmatrix} \,\,=\,\,\,
\begin{bmatrix}
1 &4 \\2 &3
\end{bmatrix}\mathbf{x}.
  \end{array}
$$

So we see that

$$
   T(\mathbf{x}) = A \mathbf{x}, \quad\text{where} \quad
   A =
\begin{bmatrix}
 T(\mathbf{e}_1) & T(\mathbf{e}_2)
\end{bmatrix}.
$$

::::::

::::::{exercise}
:label: Exc:LinTrafo:MatrixForFirstExample

Show that the procedure of {prf:ref}`Ex:LinTrafo:StandardMatrixIntro` applied to the linear transformation of {prf:ref}`Ex:LinTrafo:FirstLinearMap` indeed yields the matrix

$$
A = \begin{bmatrix}
 1 & 0 \\ 0 & 1 \\ 0 & 0
\end{bmatrix}.
$$

::::::

::::{admonition} Solution to&nbsp;{numref}`Exc:LinTrafo:MatrixForFirstExample`
:class: solution, dropdown

Consider the linear transformation
$T:\mathbb{R}^2\rightarrow\mathbb{R}^3$ that sends each vector $ \begin{bmatrix}
x \\ y
\end{bmatrix}$
in $\mathbb{R}^2$ to the vector $\begin{bmatrix} x \\ y \\ 0 \end{bmatrix}$. &nbsp; It holds that

$$
   T(\vect{e}_1) = T\left(\begin{bmatrix} 1\\ 0 \end{bmatrix}\right) =
   \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad
   T(\vect{e}_2) = T\left(\begin{bmatrix} 0\\ 1 \end{bmatrix}\right) =
   \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}.
$$

We find that for an arbitray vector $\begin{bmatrix} x\\ y \end{bmatrix} = x\begin{bmatrix} 1\\ 0 \end{bmatrix}+y\begin{bmatrix} 0\\ 1 \end{bmatrix}$ it holds that

$$
  T\left(\begin{bmatrix} x\\ y \end{bmatrix}\right) =
   xT(\vect{e}_1) + yT(\vect{e}_2) = x\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}+ y\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} =
   \begin{bmatrix} 1 & 0 \\ 0 & 1\\ 0 & 0 \end{bmatrix}\begin{bmatrix} x\\ y \end{bmatrix}.
$$

::::

The reasoning of {prf:ref}`Ex:LinTrafo:StandardMatrixIntro` can be generalized. This is the content of the next theorem.

::::::{prf:theorem}
:label: Thm:LinTrafo:LinTrafo=MatrixTrafo

Each linear transformation $T$ from $\mathbb{R}^n$ to $\mathbb{R}^m$ is a matrix transformation.

More specific, if $T: \mathbb{R}^n \to \mathbb{R}^m$ is linear, then for each $\mathbf{x}$ in $\mathbb{R}^n$

:::::{math}
:label: Eq:Lintrafo:StandardMatrix

T(\mathbf{x}) = A\mathbf{x}, \quad \text{where} \quad
A =
\begin{bmatrix}
T(\mathbf{e}_1) & T(\mathbf{e}_2) & \ldots & T(\mathbf{e}_n)
\end{bmatrix}.

:::::

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Thm:LinTrafo:LinTrafo=MatrixTrafo`
:class: tudproof

We can more or less copy the derivation in {prf:ref}`Ex:LinTrafo:StandardMatrixIntro`.
First of all, any vector $\mathbf{x}$ is a linear combination of the standard basis:

$$
  \mathbf{x} =
\begin{bmatrix}
x_1\\x_2\\ \vdots \\ x_n
\end{bmatrix} =
              x_1
\begin{bmatrix}
1 \\ 0 \\ \vdots \\ 0
\end{bmatrix} +
              x_2
\begin{bmatrix}
0 \\ 1 \\ \vdots \\ 0
\end{bmatrix} +
              \ldots +
               x_n
\begin{bmatrix}
0 \\ 0 \\ \vdots \\ 1
\end{bmatrix},
$$

i.e.,

$$
  \mathbf{x} =   x_1 \mathbf{e}_1 + x_2 \mathbf{e}_2 +  \ldots + x_n \mathbf{e}_n.
$$

From {prf:ref}`Prop:LinTrafo:ExtendedLinearity` it follows that

$$
  T( \mathbf{x}) =   x_1 T(\mathbf{e}_1) + x_2 T(\mathbf{e}_2) +  \ldots + x_n T(\mathbf{e}_n).
$$

The last expression is a linear combination of $n$ vectors in $\mathbb{R}^m$, and thus can be written as a matrix-vector product:

$$
  x_1 T(\mathbf{e}_1) + x_2 T(\mathbf{e}_2) +  \ldots + x_n T(\mathbf{e}_n) =
\begin{bmatrix}
 T(\mathbf{e}_1) & T(\mathbf{e}_2) & \ldots & T(\mathbf{e}_n)
\end{bmatrix} \mathbf{x}.
$$

::::::

::::::{prf:definition}
:label: Dfn:LinTrafo:StandardMatrix

For a linear transformation $T:\mathbb{R}^n \to \mathbb{R}^m$, the matrix

:::{math}
:label: Eq:LinTrafo:StandardMatrix2

\begin{bmatrix}
T(\mathbf{e}_1) & T(\mathbf{e}_2) & \ldots & T(\mathbf{e}_n)
\end{bmatrix}

:::

is called the **standard matrix** of $T$.

::::::

In the section {ref}`Sec:GeomLinTrans` you will learn how to build standard matrices for rotations, reflections and other geometrical mappings.
For now let us look at a more "algebraic" example.

::::::{prf:example}
:label: Ex:LinTrafo:MatrixToLinearMap

Consider the transformation

$$
   T:
\begin{bmatrix}
x \\ y \\ z
\end{bmatrix} \mapsto
\begin{bmatrix}
x-y \\ 2y+3z \\ x+y-z
\end{bmatrix}.
$$

It can be checked that the transformation has the two properties of a linear transformation according to the definition.
Note that

$$
  T(\mathbf{e}_1) =
\begin{bmatrix}
1 \\ 0 \\ 1
\end{bmatrix}, \quad
  T(\mathbf{e}_2) =
\begin{bmatrix}
-1 \\ 2 \\ 1
\end{bmatrix}, \quad \text{and} \quad
  T(\mathbf{e}_3) =
\begin{bmatrix}
0 \\ 3 \\ -1
\end{bmatrix}.
$$

So we find that the matrix $[T]$ of $T$ is given by

$$
  [T] =
\begin{bmatrix}
1 & -1 & 0 \\   0 &2&3 \\ 1 & 1 & -1
\end{bmatrix}
$$

is the standard matrix of $T$.

::::::

::::::{exercise}
:label: Exc:LinTrafo:FillBlanks

In the previous example we could have found the matrix just by inspection.

For the slightly different transformation $T:\R \to \R$ given by

$$
   T:
\begin{bmatrix}
x \\ y \\ z
\end{bmatrix} \mapsto
\begin{bmatrix}
3x-z \\ y+4z \\ x-y+2z
\end{bmatrix},
$$

can you fill in the blanks in the following equation?

$$
\begin{bmatrix}
3x-z \\ y+4z \\ x-y+2z
\end{bmatrix} =
\begin{bmatrix}
.. & .. & .. \\ .. & .. & .. \\ .. & .. & ..
\end{bmatrix}
\begin{bmatrix}
x \\ y \\ z
\end{bmatrix}.
$$

If you can, you will have shown that $T$ is a matrix transformation, and as a direct consequence $T$ is a linear transformation.

::::::

To conclude we consider an example that refers back to {prf:ref}`Prop:LinTrafo:CompositionLintrafos`, and which will to a large extent pave the road for the product of two matrices.

::::::{prf:example}
:label: Ex:LinTrafo:ProductOfMatrices

Suppose $T:\mathbb{R}^2 \to \mathbb{R}^3$ and $S:\mathbb{R}^3 \to \mathbb{R}^3$ are the matrix transformations given by

$$
  T(\mathbf{x}) = A\mathbf{x} =
\begin{bmatrix}
 1&2 \\ 3&4 \\ 1&0
\end{bmatrix} \mathbf{x} \quad \text{and} \quad
  S(\mathbf{y}) = B\mathbf{y} =
\begin{bmatrix}
 1&0 &1 \\ 1 & -1 &2  \\ -1&1&-3
\end{bmatrix} \mathbf{x}
$$

From {prf:ref}`Prop:LinTrafo:CompositionLintrafos` we know that the composition
$S\circ T: \mathbb{R}^2 \to \mathbb{R}^3$ is also a linear transformation. What is the (standard) matrix of $S\circ T$?

For this we need the images of the unit vectors $\mathbf{e}_1$ and $\mathbf{e}_2$ in $\mathbb{R}^2$.
For each vector we first apply $T$ and then $S$. For $\mathbf{e}_1$ this gives

$$
  T(\mathbf{e}_1) =
\begin{bmatrix}
 1&2 \\ 3&4 \\ 1&0
\end{bmatrix}
\begin{bmatrix}
 1\\0
\end{bmatrix} =
\begin{bmatrix}
 1  \\ 3 \\ 1
\end{bmatrix},
$$

and then

$$
   S (T(\mathbf{e}_1)) =
\begin{bmatrix}
 1&0 &1 \\ 1 & -1 &2  \\ -1&1&-3
\end{bmatrix}
\begin{bmatrix}
 1  \\ 3 \\ 1
\end{bmatrix}=
\begin{bmatrix}
 2  \\ 0 \\ -1
\end{bmatrix}.
$$

Likewise for $\mathbf{e}_2$:

$$
  T(\mathbf{e}_2) =
\begin{bmatrix}
 1&2 \\ 3&4 \\ 1&0
\end{bmatrix}
\begin{bmatrix}
 0\\1
\end{bmatrix} =
\begin{bmatrix}
 2\\4\\0
\end{bmatrix} \,\,\Longrightarrow\,\,
  S (T(\mathbf{e}_2)) =
\begin{bmatrix}
 1&0 &1 \\ 1 & -1 &2  \\ -1&1&-3
\end{bmatrix}
\begin{bmatrix}
 2  \\ 4 \\ 0
\end{bmatrix}=
\begin{bmatrix}
 2  \\ -2 \\ 2
\end{bmatrix}.
$$

So the matrix of $\circ $ becomes

$$
  [S\circ T] \,= \,
\begin{bmatrix}
S\circ T(\mathbf{e_1})&S\circ T(\mathbf{e_2})
\end{bmatrix} \,\,=\,\,
\begin{bmatrix}
 2 &2 \\ 0&-2 \\ -1&2
\end{bmatrix}.
$$

In the section {ref}`Sec:MatrixOps` we will define the product of two matrices precisely in such a way that

$$
\begin{bmatrix}
 1&0 &1 \\ 1 & -1 &2  \\ -1&1&-3
\end{bmatrix}
\begin{bmatrix}
 1&2 \\ 3&4 \\ 1&0
\end{bmatrix} =
\begin{bmatrix}
 2 &2 \\ 0&-2 \\ -1&2
\end{bmatrix}.
$$

::::::

## Grasple exercises

%::::::{grasple}
%:iframeclass: dark-light
%:url: https://embed.grasple.com/exercises/97a589a8-54f9-4688-bd4d-a17a9585813b?id=69465
%:label: grasple_exercise_3_1_1
%:dropdown:
%:description: This is {prf:ref}`Ex:LinTrafo:SecondMatrixTrafo`.
%::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3f14573a-1d4c-4a4b-ae48-ccb168005702?id=70373
:label: grasple_exercise_3_1_2
:dropdown:
:description: To specify the domain and the codomain of a linear transformation.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b80d9889-bd46-45c6-a9cb-d056aa315232?id=70374
:label: grasple_exercise_3_1_3
:dropdown:
:description: To find the size of the matrix of a linear transformation.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/be6a768d-c60d-4ed6-81a7-5dea71b4a1a5?id=70375
:label: grasple_exercise_3_1_4
:dropdown:
:description: To find image of two vectors under $T(\vect{x}) = A\vect{x}$.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c8bb24f6-d357-4571-adb3-39ea0fa9e4ee?id=70395
:label: grasple_exercise_3_1_5
:dropdown:
:description: For linear map $T$, find $T(c\vect{u})$ and $T(\vect{u}+\vect{v})$ if $T(\vect{u})$ and $T(\vect{v})$ are given.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/93048f7c-b755-4445-a532-949f34136096?id=70398
:label: grasple_exercise_3_1_6
:dropdown:
:description: For linear map $T:\R^2 \to \R^2$, find $T((x1,x2))$ if $T(\vect{e}_1)$ and $T(\vect{e}_2)$ are given.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2af6559f-8871-494d-abce-d4263d530c69?id=70381
:label: grasple_exercise_3_1_7
:dropdown:
:description: Find all vectors $\vect{w}$ for which $T(\vect{w}) = \vect{u}$.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ce6e4a52-c985-43ee-92cb-2762a467ac5a?id=70383
:label: grasple_exercise_3_1_8
:dropdown:
:description: Find vectors $\vect{w}$ for which $T(\vect{w}) = \vect{u}$.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/37b6bd46-8cfc-4c98-a5e8-53aa41c87dcf?id=70384
:label: grasple_exercise_3_1_10
:dropdown:
:description: Find vectors $\vect{w}$ for which $T(\vect{w}) = \vect{u}$.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c5b2a642-fd50-43f6-9346-c37a0ffe1a40?id=70386
:label: grasple_exercise_3_1_10b
:dropdown:
:description: Find vectors $\vect{w}$ for which $T(\vect{w}) = \vect{u}$.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c3d009c0-62d6-4ae3-8ca1-04a5d2730455?id=70406
:label: grasple_exercise_3_1_11
:dropdown:
:description: To show that a given transformation is non-linear.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b9a4b128-f2c2-4612-a7f5-271c4e69aa70?id=70418
:label: grasple_exercise_3_1_12
:dropdown:
:description: Finding an image and a pre-image of $T:\R^2 \to \R^2$ using a picture.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4058e54a-74f2-414e-9693-420abbc62677?id=70391
:label: grasple_exercise_3_1_13
:dropdown:
:description: 'To give a geometric description of $T: \vect{x} \mapsto A\vect{x}$.'
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/990bf561-629e-430f-b8d0-e757c63fe15c?id=70392
:label: grasple_exercise_3_1_14
:dropdown:
:description: 'To give a geometric description of $T: \vect{x} \mapsto A\vect{x}$.'
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4e5d3f55-9257-4023-9739-5df0a1a9f277?id=70410
:label: grasple_exercise_3_1_15
:dropdown:
:description: To find the matrix of the transformation that sends $(x,y)$ to $x\vect{a}_1 + y\vect{a}_2$.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9efa96e2-483d-4b2c-a58a-ba197bc09a81?id=70411
:label: grasple_exercise_3_1_16
:dropdown:
:description: To find the matrix of the transformation that sends $(x,y)$ to $x\vect{a}_1 + y\vect{a}_2$.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/729cba57-72d1-4d54-8cf9-c9946952bf9d?id=70412
:label: grasple_exercise_3_1_17
:dropdown:
:description: To rewrite $T:\R^3 \to \R^2$ to standard form.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b4bb3730-f14c-4a60-a8b8-6b895cf93ac5?id=70413
:label: grasple_exercise_3_1_18
:dropdown:
:description: To find the standard matrix for $T:\R^4 \to \R$.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/34bb6386-7e7c-411b-83a1-09bbaf1106c5?id=70415
:label: grasple_exercise_3_1_19
:dropdown:
:description: To find the standard matrix for $T:\R^2 \to \R^2$ if $T(\vect{v}_1)$ and $T(\vect{v}_2)$ are given.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ce8ba17c-0a17-4d5e-b4b7-5c277c7e8df8?id=70416
:label: grasple_exercise_3_1_20
:dropdown:
:description: To find the standard matrix for $T:\R^2 \to \R^3$ if $T(\vect{v}_1)$ and $T(\vect{v}_2)$ are given.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2de4f8d1-ab3d-4d3a-94e4-5e414e2da3d9?id=70372
:label: grasple_exercise_3_1_21
:dropdown:
:description: If $T(\vect{0}) = \vect{0}$, is $T$ (always) linear?
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3f992e7a-19e3-4b83-8d90-db86e323ea94?id=69296
:label: grasple_exercise_3_1_22
:dropdown:
:description: To show that $T(\vect{0}) = \vect{0}$ for a linear transformation.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/94d618e0-de21-491c-ad44-8e29974e0303?id=71098
:label: grasple_exercise_3_1_23
:dropdown:
:description: (T/F) If $\{\vect{v}_1,\vect{v}_2,\vect{v}_3\}$ is linearly dependent, then $\{T(\vect{v}_1),T(\vect{v}_2),T(\vect{v}_3)\}$ is also linearly dependent?
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f983b627-10c2-4dd6-a273-2a33e99d0ded?id=71101
:label: grasple_exercise_3_1_24
:dropdown:
:description: (T/F) If $\{\vect{v}_1,\vect{v}_2,\vect{v}_3\}$ is linearly independent, then $\{T(\vect{v}_1),T(\vect{v}_2),T(\vect{v}_3)\}$ is also linearly independent?
::::::
