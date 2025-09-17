(Sec:LinTrafo)=

# Linear transformations

(Subsec:LinTrafo:MatrixTrafo)=

## Introduction

Until now we have used matrices in the context of linear systems. The equation

$$
 A\mathbf{x} = \mathbf{b},
$$

where $A$ is an $m \times n$-matrix, is just a concise way to write down a system of $m$ linear equations in $n$
unknowns.
A different way to look at this matrix equation is to consider it as an input-output system:
the left-hand side $A\mathbf{x}$
can be seen as a mapping that sends an "input" $\mathbf{x}$ to an "output" $\mathbf{y}= A\mathbf{x}$.

For instance, in computer graphics, typically points describing a 3D object have to be converted to points in 2D, to be able to visualise them on a screen. Or, in a dynamical system, a
matrix $A$ may describe how a system evolves from a "state" $\mathbf{x}_{k}$ at time $k$ to a state $\mathbf{x}_{k+1}$ at time $k+1$ via 

$$
    \mathbf{x}_{k+1} = A\mathbf{x}_{k}.
$$

A "state" may be anything ranging from a set of particles at certain positions, a set of pixels describing a minion, concentrations of chemical substances in a reactor tank, to population sizes of different species.
Thinking mathematically we would describe such an input-output interpretation as a
transformation (or: function, map, mapping, operator, etc. ).

$$
   T: \mathbb{R}^n \to \mathbb{R}^m.
$$

We will see that these matrix transformations have two characteristic properties  
which makes them the protagonists of the more general linear algebra concept of a **linear transformation**.

(Subsec:MatrixTrafo)=

## Matrix transformations

Let $A$ be an $m\times n$-matrix. We can in a natural way associate a transformation $T_A:\mathbb{R}^n \to \mathbb{R}^m$ to the matrix $A$.

::::::{prf:definition}
:label: Def:LinTrafo:MatrixTransformation

The transformation $T_A$ corresponding to the $m\times n$-matrix $A$
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
$A = \begin{pmatrix} 1 & 2 & 0\\ 1 & 2 & 1 \end{pmatrix}$ is defined by

$$
   T_A(\mathbf{x}) =
        \begin{pmatrix}
            1 & 2 & 0\\ 1 & 2 & 1
\end{pmatrix}\mathbf{x}.
$$

We have, for instance

$$
\begin{pmatrix}
        1 & 2 & 0\\ 1 & 2 & 1
\end{pmatrix}
\begin{pmatrix}
       1\\1\\1
\end{pmatrix} =
\begin{pmatrix}
        3 \\ 4
\end{pmatrix}
   \quad \text{and} \quad
\begin{pmatrix}
        1 & 2 & 0\\ 1 & 2 & 1
\end{pmatrix}
\begin{pmatrix}
       2\\-1\\0
\end{pmatrix} =
\begin{pmatrix}
       0\\ 0
\end{pmatrix}.
$$

According to the definition of the matrix-vector product we can also write

:::{math}
:label: Eq:LinTrafo:AxIsLinearCombination

A\mathbf{x} = \begin{pmatrix}
1 & 2 & 0\\ 1 & 2 & 1  
 \end{pmatrix}
\begin{pmatrix}
x_1\\x_2\\x_3  
 \end{pmatrix} =
x_1  
 \begin{pmatrix}
1\\ 1  
 \end{pmatrix}+
x_2  
 \begin{pmatrix}
2 \\ 2  
 \end{pmatrix}+
x_3  
 \begin{pmatrix}
0\\ 1  
 \end{pmatrix}.

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
\operatorname{Range}(T_A) =
\Span{ \begin{pmatrix} 1\\ 1   \end{pmatrix}, \begin{pmatrix} 2 \\  2  \end{pmatrix}, \begin{pmatrix} 0\\  1  \end{pmatrix}}.
$$

In a later section ({numref}`Sec:SubspacesRn`) we will call this the **column space** of the matrix $A$.


::::::

The first example leads to a first property of matrix transformations:

::::::{prf:proposition}
:label: Prop:LinTrafo:RangeTA

Suppose

$$
A = \begin{pmatrix}
 \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n
\end{pmatrix}
$$

is an $m\times n$-matrix.

Then the range of the matrix transformation corresponding to $A$ is the span of the columns of $A$:

$$
   \operatorname{Range}(T_A) = \Span{\mathbf{a}_1, \mathbf{a}_2,\ldots,\mathbf{a}_n }.
$$

::::::

::::::{prf:example}
:label: Ex:LinTrafo:SecondMatrixTrafo

The matrix

$$
 A = \begin{pmatrix}
 1 & 0 \\ 0 & 1 \\ 0 & 0
\end{pmatrix}
$$

leads to the transformation

$$
 T: \mathbb{R}^2 \to \mathbb{R}^3, \quad
 T \left(\begin{pmatrix}
        x \\ y
\end{pmatrix}\right)=
\begin{pmatrix}
        1 & 0 \\ 0 & 1 \\ 0 & 0
\end{pmatrix}
\begin{pmatrix}
        x \\ y
\end{pmatrix}    =
\begin{pmatrix}
        x \\ y \\0
\end{pmatrix}.
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
\begin{pmatrix}
 1\\ 0 \\ 0
\end{pmatrix} \quad \text{and} \quad
    \mathbf{e}_2  =
\begin{pmatrix}
 0\\ 1 \\ 0
\end{pmatrix},
$$

which is the $xy$-plane in $\mathbb{R}^3$.

::::::

For $2\times2$ and $3\times3$-matrices the transformations often have a geometric interpretation, as the following example illustrates.

::::::{prf:example}
:label: Eq:LinTrafo:SkewProjection

The transformation corresponding to the matrix

$$
A = \begin{pmatrix}
        1 &  1  \\ 0 & 0
\end{pmatrix}
$$

is the mapping

$$
  T: \mathbb{R}^2 \to \mathbb{R}^2, \quad  T\left(\begin{pmatrix}
        x \\ y
\end{pmatrix}\right)=
\begin{pmatrix}
        x +y \\ 0
\end{pmatrix}.
$$

First we observe that the range of this transformation consists of all multiples of the vector $ \begin{pmatrix} 1 \\ 0 \end{pmatrix} $, 
i.e. the $x$-axis in the plane.

Second, let us find the set of points/vectors that is mapped to an arbitrary point
$\begin{pmatrix} c \\ 0 \end{pmatrix}$ in the range. For this we solve

$$
  A\mathbf{x} = \begin{pmatrix}
                1 &  1  \\ 0 & 0
              \end{pmatrix}
\begin{pmatrix}
                  x  \\ y
\end{pmatrix} =
\begin{pmatrix}
                c \\ 0
\end{pmatrix},
  \quad \text{so} \quad
\begin{pmatrix}
        x+y \\ 0
\end{pmatrix}  =
\begin{pmatrix}
        c \\ 0
\end{pmatrix}.
$$

The points whose coordinates satisfy this equation all lie on the line described by the equation

$$
   x + y = c.
$$

So what the mapping does is to send all points on a line $\mathcal{L}:x + y = c$ to the point $(c,0)$, which is the intersecting of this line with the $x$-axis.
An alternative way to describe it: it is the skew projection, in the direction $\begin{pmatrix} 1 \\ -1 \end{pmatrix}$ onto the $x$-axis.
See {numref}`Figure %s <Fig:LinTrafo:SkewProjection>`.

::::{figure} Images/Fig-LinTrafo-SkewProjection.svg
:name: Fig:LinTrafo:SkewProjection
:class: dark-light

The transformation of {prf:ref}`Eq:LinTrafo:SkewProjection`.
::::

::::::



::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2db421fe-0649-4c7e-9624-9fdf0123565d?id=122271
:label: grasple_exercise_3_1_1T
:dropdown:
:description: Finding out which vectors are in the range of a linear transformation.

::::::

We close this subsection with an example of a matrix transformation representing a very elementary dynamical system.

::::::{prf:example}
:label: Ex:LinTrafo:MigrationModel

Consider a model with two cities between which over a fixed period of time migrations take place. Say in a period of ten years 90\% of the inhabitants in city $A$ stay in city $A$ and 10\% move to city $B$. From city $B$ 20\% of the citizens move to $A$, so 80\% stay in city $B$.

The following table contains the relevant statistics:

$$
  \begin{array}{c|cc|} & A & B \\ \hline
      A & 0.9 & 0.2 \\
      B & 0.1 & 0.8 \\ \hline
  \end{array}
$$

For instance, if at time $0$ the population in city $A$ amounts to $50$ (thousand) and in city $B$ live $100$ (thousand) people, then at the end of one period the population in city $A$
amounts to

$$
  0.9 \times 50 + 0.2 \times 100 = 65.
$$

Likewise for city $B$.

If we denote the population sizes after $k$ periods by a vector

$$
   \mathbf{x}_k =
\begin{pmatrix}
 x_k \\ y_k
\end{pmatrix}
$$

it follows that

$$
\begin{pmatrix}
 x_{k+1} \\ y_{k+1}
\end{pmatrix} =
\begin{pmatrix}
 0.9x_k + 0.2y_k  \\0.1x_k + 0.8y_k
\end{pmatrix}, \quad
   \text{i.e.,   }
   \mathbf{x}_{k+1} =
\begin{pmatrix}
 0.9 & 0.2  \\ 0.1 & 0.8
\end{pmatrix}
\begin{pmatrix}
 x_k \\ y_k
\end{pmatrix} = M \mathbf{x}_{k}.
$$

The $M$ stands for migration matrix.

Obviously this model can be generalised to a "world" with any number of cities.

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

$$
     T(\mathbf{v}_1+\mathbf{v}_2) = T(\mathbf{v}_1) + T(\mathbf{v}_2).
$$

</li>
<li>

For all vectors $\mathbf{v}$ in $\mathbb{R}^n$ and all scalars $c$ in $\mathbb{R}$:

$$
     T(c\mathbf{v}) = c\,T(\mathbf{v}).
$$

</li>
</ol>

::::::

::::::{exercise}
:label: Exc:LinTrafo:ImageofZeroVector

Show that a linear transformation from $\mathbb{R}^n$ to $\mathbb{R}^m$ always sends the zero vector $\mathbf{0}_n$ in $\R^n$ to the zero vector $\mathbf{0}_m$ in $\R^m$.

Thus, if $ T:\mathbb{R}^n \to\mathbb{R}^m$ is a linear transformation, then $T(\mathbf{0}_n) = \mathbf{0}_m$.

::::::

::::::{admonition} Solution to {numref}`Exc:LinTrafo:ImageofZeroVector`
:class: solution, dropdown

If $ T:\mathbb{R}^n \to\mathbb{R}^m$ is linear, and $\vect{v}$ is any vector in $\R^n$, then $\mathbf{0}_n = 0\vect{v}$. From the second property in {prf:ref}`Dfn:LinTrafo:LinTrafo` it follows that

$$
  T(\mathbf{0}_n) = T(0\vect{v}) = 0\,T(\vect{v}) = \mathbf{0}_m.
$$

::::::

::::::{prf:example}
:label: Ex:LinTrafo:FirstLinearMap

Consider the map $T:\mathbb{R}^2\rightarrow\mathbb{R}^3$ that sends each vector
$\begin{pmatrix}
 x \\ y 
\end{pmatrix}$
in $\mathbb{R}^2$ to the vector
$\begin{pmatrix}
 x \\ y \\ 0 
\end{pmatrix}$ in $\mathbb{R}^3$.
Let us check that this a linear map.

For that, we need to check the two properties in the definition.

For property (i) we take two arbitrary vectors

$$
\begin{pmatrix}
    x_1 \\ y_1
\end{pmatrix} \quad \text{ and }\quad
\begin{pmatrix}
 x_2 \\ y_2
\end{pmatrix}  \quad \text{in} \quad \mathbb{R}^2,
$$

and see:

$$
    T\left(\begin{pmatrix}
        x_1 \\ y_1
\end{pmatrix} +
\begin{pmatrix}
        x_2 \\ y_2
\end{pmatrix} \right)=
    T \left(\begin{pmatrix}
        x_1+x_2 \\ y_1+y_2
\end{pmatrix}\right)=
\begin{pmatrix}
            x_1 + x_2 \\ y_1 + y_2 \\ 0
\end{pmatrix} =
\begin{pmatrix}
            x_1 \\ y_1 \\ 0
\end{pmatrix} +
\begin{pmatrix}
            x_2 \\ y_2 \\ 0
\end{pmatrix}.
$$

This last vector indeed equals

$$
 T\left(\begin{pmatrix}
            x_1 \\ y_1
\end{pmatrix}\right)+
        T\left(\begin{pmatrix}
            x_2 \\ y_2
\end{pmatrix}\right).
$$

Similarly, for the second property, given any scalar $c$,

$$
    T\left(c \begin{pmatrix}
        x_1 \\ y_1
\end{pmatrix}\right)=
    T \left(\begin{pmatrix}
        c x_1 \\  cy_1
\end{pmatrix}\right)=
\begin{pmatrix}
        c x_1 \\ c y_1 \\ 0
\end{pmatrix} =
    c \begin{pmatrix}
        x_1 \\ y_1 \\ 0
\end{pmatrix}=
        cT \left(\begin{pmatrix}
            x_1 \\ y_1
\end{pmatrix}\right).
$$

So indeed $T$ has the two properties of a linear transformation.

::::::

::::::{prf:example}
:label: Ex:LinTrafo:NotLinearMap

Consider the mapping
$T:\mathbb{R}^2\rightarrow\mathbb{R}^2$ that sends each vector $ \begin{pmatrix}
x \\ y
\end{pmatrix}$
in $\mathbb{R}^2$ to the vector $\begin{pmatrix} x+y \\ xy \end{pmatrix}$:

$$
  T:  \begin{pmatrix}
 x \\ y
\end{pmatrix} \mapsto
\begin{pmatrix}
 x+y \\ xy
\end{pmatrix}
$$

This mapping is **not** a linear transformation.

$$
    T \left(\begin{pmatrix}
 1 \\ 1
\end{pmatrix} +
\begin{pmatrix}
 1 \\ 2
\end{pmatrix}\right)=
    T
\left(\begin{pmatrix}
2 \\ 3
\end{pmatrix}\right)    =
\begin{pmatrix}
 5 \\ 6
\end{pmatrix},
$$

whereas

$$
   T \left(\begin{pmatrix}
 1 \\ 1
\end{pmatrix}\right)+
   T \left(\begin{pmatrix}
 1 \\ 2
\end{pmatrix}\right)=
\begin{pmatrix}
 2 \\ 1
\end{pmatrix} +
\begin{pmatrix}
 3 \\ 2
\end{pmatrix} =
\begin{pmatrix}
 5 \\ 3
\end{pmatrix}
       \,\neq\,
\begin{pmatrix}
 5 \\ 6
\end{pmatrix} .
$$

The second requirement of a linear transformation is violated as well:

$$
   T\left(3
\begin{pmatrix}
 1 \\ 1
\end{pmatrix}\right)=
   T
\left(\begin{pmatrix}
 3 \\ 3
\end{pmatrix}\right)=
\begin{pmatrix}
 6 \\ 9
\end{pmatrix}
   \,\,\neq\,\,
   3\,T
\left(\begin{pmatrix}
 1 \\ 1
\end{pmatrix} \right)=
   3
\begin{pmatrix}
 2 \\ 1
\end{pmatrix} =
\begin{pmatrix}
 6 \\ 3
\end{pmatrix}.
$$

::::::

::::::{exercise}
:label: Exc:LinTrafo:T(x)=x+p

Let $\mathbf{p}$ be a non-zero vector in $\mathbb{R}^2$. Is the translation

$$
   T\!:\mathbb{R}^2 \to \mathbb{R}^2, \quad  \mathbf{x} \mapsto \mathbf{x} + \mathbf{p}
$$

a linear transformation?

::::::

::::::{admonition} Solution to {numref}`Exc:LinTrafo:T(x)=x+p`
:class: solution, dropdown

The transformation defined by $T(\vect{x}) = \vect{x} + \vect{p}$, with $\vect{p}\neq \vect{0}$ does not have any of the two properties of a linear transformation.

For instance, since $\vect{p}+\vect{p} \neq \vect{p}$,

$$
  T(\vect{x}+\vect{y}) = \vect{x}+\vect{y} + \vect{p} \neq
  T(\vect{x})+T(\vect{y}) = \vect{x}+ \vect{p} +\vect{y} + \vect{p}.
$$

::::::

Note that {prf:ref}`Ex:LinTrafo:FirstLinearMap` was in fact the first example of a matrix transformation in the Subsection {ref}`Subsec:LinTrafo:MatrixTrafo`:

$$
\begin{pmatrix}
 x \\ y
\end{pmatrix}  \mapsto
\begin{pmatrix}
 x \\ y \\ 0
\end{pmatrix}
   =
\begin{pmatrix}
 1 & 0 \\ 0&1 \\ 0&0
\end{pmatrix}
\begin{pmatrix}
 x \\ y
\end{pmatrix}
$$

As we will see: **any** linear transformation from $\mathbb{R}^n$ to $\mathbb{R}^m$ is a matrix transformation. The converse is true as well. This is the content of the next proposition.

::::::{prf:proposition}
:label: Prop:LinTrafo:MatrixTrafoIsLinear

Each matrix transformation is a linear transformation.

::::::

::::::{admonition} Proof of {prf:ref}`Prop:LinTrafo:MatrixTrafoIsLinear`
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
:label: Rmk:LinTrafo:Composition

The transformation $S\circ T$ is called the **composition** of the two transformations $S$ and $T$. It is best read as _"$S$ after $T$"_.
::::::

::::::{admonition} Proof of {prf:ref}`Prop:LinTrafo:CompositionLintrafos`
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

::::::{admonition} Solution to {numref}`Exc:LinTrafo:CombiningLinTrafos`
:class: solution, dropdown

The properties of the linear transformation $T_1$ and $T_2$ carry over to $S$ and $T_3$ in the following way.
We check the properties one by one.

For the sum $S$ we have

<ol type="i">
<li>

For all vectors $\mathbf{v}_1,\,\mathbf{v}_2$ in $\R^n$ 

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

Likewise, for all vectors $\mathbf{v}$ in $\mathbb{R}^n$ and all scalars $c$ in $\mathbb{R}$:

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


::::::{exercise}
:label: Exc:LinTrafo:LineSegments

This exercise sheds some light on the geometry behind linear transformations.
We restrict ourselves to linear transformations in the plane,  but the ideas can be generalised.

Suppose  $T$  is a linear transformation from $\R^2$ to $\R^2$.  Show that the image of a line segment $\mathcal{S}$ between two points $P$ and $Q$ is either a line segment or a single point.

::::::



::::::{admonition} Solution to {numref}`Exc:LinTrafo:LineSegments`
:class: solution, dropdown


Suppose  $\vect{p} = \overrightarrow{OP}$ and  $\vect{q} = \overrightarrow{OQ}$ are the position vectors, and let $\vect{r} = \overrightarrow{PQ}  = \vect{q} - \vect{p}$.
Then the line segment between $\vect{p}$ and $\vect{q}$ consist of all vectors  $\vect{v} = \vect{p} + t\vect{r}$, where $t$ runs from $0$ to $1$.

By the linearity of $T$ it follows that the image of $\mathcal{S}$  consist of all vectors
$T(\vect{p} + t\vect{r}) = T(\vect{p})  + tT(\vect{r})$, with $0 \leq t \leq 1$. 

This describes the line segment between the points  $T(\vect{p})$ and $T(\vect{p}) + T(\vect{r})$.  Note that 
$T(\vect{p})  + T(\vect{r}) = T(\vect{p} + \vect{r}) = T(\vect{q})$.  If by any chance  $T(\vect{r}) = \mathbf{0}$,  the segment 'shrinks' to a single point.

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

T(c_1\mathbf{x}_1+c_2 \mathbf{x}_2+ \cdots +c_k \mathbf{x}_k) =
c_1T(\mathbf{x}_1)+c_2T(\mathbf{x}_2)+ \cdots +c_kT( \mathbf{x}_k).

:::::

::::::

In words: for any linear transformation
_the image of a linear combination of vectors is equal to the linear combination of their images_.

::::::{admonition} Proof of {prf:ref}`Prop:LinTrafo:ExtendedLinearity`
:class: tudproof

Suppose $T:\mathbb{R}^n\rightarrow\mathbb{R}^m$ is a linear transformation.

So we have

$$
  \text{(i) } T(\mathbf{x}+\mathbf{y}) = T(\mathbf{x})+T(\mathbf{y}) \quad\text{and} \quad \text{(ii)  }
    T(c\mathbf{x}) = c T(\mathbf{x}).
$$

First apply rule (i) to split the term on the left in Equation {eq}`Eq:LinTrafo:LinComb` into $k$ terms:

$$
\begin{array}{ccl}
T(c_1\mathbf{x}_1+c_2 \mathbf{x}_2+ \cdots +c_k \mathbf{x}_k)  &=&
  T(c_1\mathbf{x}_1)+T(c_2 \mathbf{x}_2+ \cdots +c_k \mathbf{x}_k) \\
  &\vdots&  \\
  &=& T(c_1\mathbf{x}_1)+T(c_2 \mathbf{x}_2)+ \cdots + T(c_k \mathbf{x}_k)
 \end{array}
$$

and then apply rule (ii) to each term.

::::::

::::::{prf:example}
:label: Ex:LinTrafo:ExtendedLinearity

Suppose $T: \mathbb{R}^3 \to \mathbb{R}^2$ is a linear transformation, and we know that for

$$
  \vect{a}_1 =
\begin{pmatrix}
 1 \\ 0 \\ 0
\end{pmatrix}, \quad
  \vect{a}_2 =
\begin{pmatrix}
 1 \\ 1 \\ 0
\end{pmatrix},
  \quad \vect{a}_3 =
\begin{pmatrix}
 1 \\ 1 \\ 1
\end{pmatrix}
$$

the images under $T$ are given by

$$
  T(\vect{a}_1)  = \vect{b}_1 =
\begin{pmatrix}
 1 \\ 2
\end{pmatrix}, \quad T(\vect{a}_2)  = \vect{b}_2 =
\begin{pmatrix}
 3 \\ -1
\end{pmatrix},
  \quad \text{and} \quad  T(\vect{a}_3)  = \vect{b}_3 =
\begin{pmatrix}
 2 \\ -2
\end{pmatrix}.
$$

Then for the vector

$$
 \vect{v} =
\begin{pmatrix}
 4 \\ 1 \\ -1
\end{pmatrix} = 3 \vect{a}_1 + 2 \vect{a}_2 - 1 \vect{a}_3
$$

it follows that

$$
 T(\vect{v}) =   3 \vect{b}_1 + 2 \vect{b}_2  + (-1) \vect{b}_3 =
 3
\begin{pmatrix}
 1 \\ 2
\end{pmatrix}
 + 2
\begin{pmatrix}
 3 \\ -1
\end{pmatrix}
 + (-1)
\begin{pmatrix}
 2 \\ -2
\end{pmatrix}=
\begin{pmatrix}
 7 \\ 6
\end{pmatrix}.
$$

::::::

The central idea illustrated in {prf:ref}`Ex:LinTrafo:ExtendedLinearity`, which is in fact a direct consequence of {prf:ref}`Prop:LinTrafo:ExtendedLinearity`, is the following:

a linear transformation $T$ from $\mathbb{R}^n$ to $\mathbb{R}^m$ is completely specified by the images
$ T(\mathbf{a}_1), T(\mathbf{a}_2), \ldots , T(\mathbf{a}_n)$ of a set of vectors $\{\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_n\}$ that spans $\mathbb{R}^n$. 

The simplest set of vectors that spans the whole space $\mathbb{R}^n$ is
the standard basis for $\mathbb{R}^n$ which was introduced in the Section {ref}`Sec:LinearCombinations`.

Recall that this is the set of vectors

:::{math}
:label: Eq:LinTrafo:StandardBasis

\left(\vect{e}_1,\mathbf{e}_2, \ldots, \mathbf{e}_n\right)=
\left(\begin{pmatrix}
1 \\ 0 \\ 0 \\ \vdots \\ 0
\end{pmatrix},
\begin{pmatrix}
0 \\ 1 \\ 0 \\ \vdots \\ 0
\end{pmatrix},
\quad \cdots \quad ,
\begin{pmatrix}
0 \\ 0 \\ 0 \\ \vdots \\ 1
\end{pmatrix}\right).

:::

The next example gives an illustration of the above, and it also leads the way to
the construction of a matrix for an arbitrary linear transformation.

::::::{prf:example}
:label: Ex:LinTrafo:StandardMatrixIntro

Suppose $T$ is a linear transformation from $\mathbb{R}^2$ to $\mathbb{R}^2$ for which

$$
   T(\mathbf{e}_1) = \mathbf{a}_1  =
\begin{pmatrix}
1 \\2
\end{pmatrix},
   \quad
   T(\mathbf{e}_2) = \mathbf{a}_2  =
\begin{pmatrix}
4 \\3
\end{pmatrix}.
$$

Then for an arbitrary vector

$$
  \mathbf{x} =
\begin{pmatrix}
x_1\\x_2
\end{pmatrix} =
        x_1
\begin{pmatrix}
1\\0
\end{pmatrix} +
        x_2
\begin{pmatrix}
0\\1
\end{pmatrix}
     = x_1\mathbf{e}_1 + x_2\mathbf{e}_2,
$$

it follows that

$$
 \begin{array}{rcl}
  T(\mathbf{x}) &=& x_1T(\mathbf{e}_1) + x_2T(\mathbf{e}_2) \\
               &=& x_1
\begin{pmatrix}
1 \\2
\end{pmatrix}
               + x_2
\begin{pmatrix}
4 \\3
\end{pmatrix} \,\,=\,\,\,
\begin{pmatrix}
1 &4 \\2 &3
\end{pmatrix}\mathbf{x}.
  \end{array}
$$

So we see that

$$
   T(\mathbf{x}) = A \mathbf{x}, \quad\text{where} \quad
   A =
\begin{pmatrix}
 T(\mathbf{e}_1) & T(\mathbf{e}_2)
\end{pmatrix}.
$$

::::::

::::::{exercise}
:label: Exc:LinTrafo:MatrixForFirstExample

Show that the procedure of {prf:ref}`Ex:LinTrafo:StandardMatrixIntro` applied to the linear transformation of {prf:ref}`Ex:LinTrafo:FirstLinearMap` indeed yields the matrix

$$
A = \begin{pmatrix}
 1 & 0 \\ 0 & 1 \\ 0 & 0
\end{pmatrix}.
$$

::::::

::::{admonition} Solution to {numref}`Exc:LinTrafo:MatrixForFirstExample`
:class: solution, dropdown

Consider the linear transformation
$T:\mathbb{R}^2\rightarrow\mathbb{R}^3$ that sends each vector $ \begin{pmatrix}
x \\ y
\end{pmatrix}$
in $\mathbb{R}^2$ to the vector $\begin{pmatrix} x \\ y \\ 0 \end{pmatrix}$. It holds that

$$
   T(\vect{e}_1) = T\left(\begin{pmatrix} 1\\ 0 \end{pmatrix}\right) =
   \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad
   T(\vect{e}_2) = T\left(\begin{pmatrix} 0\\ 1 \end{pmatrix}\right) =
   \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}.
$$

We find that for an arbitrary vector $\begin{pmatrix} x\\ y \end{pmatrix} = x\begin{pmatrix} 1\\ 0 \end{pmatrix}+y\begin{pmatrix} 0\\ 1 \end{pmatrix}$ it holds that

$$
  T\left(\begin{pmatrix} x\\ y \end{pmatrix}\right) =
   xT(\vect{e}_1) + yT(\vect{e}_2) = x\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}+ y\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} =
   \begin{pmatrix} 1 & 0 \\ 0 & 1\\ 0 & 0 \end{pmatrix}\begin{pmatrix} x\\ y \end{pmatrix}.
$$

::::

The reasoning of {prf:ref}`Ex:LinTrafo:StandardMatrixIntro` can be generalised. This is the content of the next theorem.

::::::{prf:theorem}
:label: Thm:LinTrafo:LinTrafo=MatrixTrafo

Each linear transformation $T$ from $\mathbb{R}^n$ to $\mathbb{R}^m$ is a matrix transformation.

More specific, if $T: \mathbb{R}^n \to \mathbb{R}^m$ is linear, then for each $\mathbf{x}$ in $\mathbb{R}^n$

:::::{math}
:label: Eq:Lintrafo:StandardMatrix

T(\mathbf{x}) = A\mathbf{x}, \quad \text{where} \quad
A =
\begin{pmatrix}
T(\mathbf{e}_1) & T(\mathbf{e}_2) & \cdots & T(\mathbf{e}_n)
\end{pmatrix}.

:::::

::::::

::::::{admonition} Proof of {prf:ref}`Thm:LinTrafo:LinTrafo=MatrixTrafo`
:class: tudproof

We can more or less copy the derivation in {prf:ref}`Ex:LinTrafo:StandardMatrixIntro`.
First of all, any vector $\mathbf{x}$ is a linear combination of the standard basis:

$$
  \mathbf{x} =
\begin{pmatrix}
x_1\\x_2\\ \vdots \\ x_n
\end{pmatrix} =
              x_1
\begin{pmatrix}
1 \\ 0 \\ \vdots \\ 0
\end{pmatrix} +
              x_2
\begin{pmatrix}
0 \\ 1 \\ \vdots \\ 0
\end{pmatrix} +
              \cdots +
               x_n
\begin{pmatrix}
0 \\ 0 \\ \vdots \\ 1
\end{pmatrix},
$$

i.e.,

$$
  \mathbf{x} =   x_1 \mathbf{e}_1 + x_2 \mathbf{e}_2 + \cdots + x_n \mathbf{e}_n.
$$

From {prf:ref}`Prop:LinTrafo:ExtendedLinearity` it follows that

$$
  T( \mathbf{x}) =   x_1 T(\mathbf{e}_1) + x_2 T(\mathbf{e}_2) + \cdots + x_n T(\mathbf{e}_n).
$$

The last expression is a linear combination of $n$ vectors in $\mathbb{R}^m$, and thus can be written as a matrix-vector product:

$$
  x_1 T(\mathbf{e}_1) + x_2 T(\mathbf{e}_2) + \cdots + x_n T(\mathbf{e}_n) =
\begin{pmatrix}
 T(\mathbf{e}_1) & T(\mathbf{e}_2) & \cdots & T(\mathbf{e}_n)
\end{pmatrix} \mathbf{x}.
$$

::::::

::::::{prf:definition}
:label: Dfn:LinTrafo:StandardMatrix

For a linear transformation $T:\mathbb{R}^n \to \mathbb{R}^m$, the matrix

:::{math}
:label: Eq:LinTrafo:StandardMatrix2

\begin{pmatrix}
T(\mathbf{e}_1) & T(\mathbf{e}_2) & \cdots & T(\mathbf{e}_n)
\end{pmatrix}

:::

is called the **standard matrix** of $T$.

::::::

In the Section {ref}`Sec:GeomLinTrans` you will learn how to build standard matrices for rotations, reflections and other geometrical mappings.
For now let us look at a more "algebraic" example.

::::::{prf:example}
:label: Ex:LinTrafo:MatrixToLinearMap

Consider the transformation

$$
   T:
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix} \mapsto
\begin{pmatrix}
x-y \\ 2y+3z \\ x+y-z
\end{pmatrix}.
$$

It can be checked that the transformation has the two properties of a linear transformation according to the definition.
Note that

$$
  T(\mathbf{e}_1) =
\begin{pmatrix}
1 \\ 0 \\ 1
\end{pmatrix}, \quad
  T(\mathbf{e}_2) =
\begin{pmatrix}
-1 \\ 2 \\ 1
\end{pmatrix}, \quad \text{and} \quad
  T(\mathbf{e}_3) =
\begin{pmatrix}
0 \\ 3 \\ -1
\end{pmatrix}.
$$

So we find that the standard matrix $[T]$ of $T$ is given by

$$
  [T] =
\begin{pmatrix}
1 & -1 & 0 \\   0 &2&3 \\ 1 & 1 & -1
\end{pmatrix}.
$$

::::::

::::::{exercise}
:label: Exc:LinTrafo:FillBlanks

In the previous example we could have found the matrix just by inspection.

For the slightly different transformation $T:\R^3 \to \R^3$ given by

$$
   T:
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix} \mapsto
\begin{pmatrix}
3x-z \\ y+4z \\ x-y+2z
\end{pmatrix},
$$

can you fill in the blanks in the following equation?

$$
\begin{pmatrix}
3x-z \\ y+4z \\ x-y+2z
\end{pmatrix} =
\begin{pmatrix}
\ldots & \ldots & \ldots \\ \ldots & \ldots & \ldots \\ \ldots & \ldots & \ldots
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}.
$$

If you can, you will have shown that $T$ is a matrix transformation, and as a direct consequence $T$ is a linear transformation.

::::::

:::{admonition} Solution to {numref}`Exc:LinTrafo:FillBlanks`
:class: solution, dropdown

$$
\begin{pmatrix}
3x-z \\ y+4z \\ x-y+2z
\end{pmatrix} =
\begin{pmatrix}
3 & 0 & -1\\
0 & 1 & 4 \\
1 & -1 & 2
\end{pmatrix}
\begin{pmatrix}
x \\ y \\ z
\end{pmatrix}.
$$

:::


To conclude we consider an example that refers back to {prf:ref}`Prop:LinTrafo:CompositionLintrafos`, and which will to a large extent pave the road for the product of two matrices.

::::::{prf:example}
:label: Ex:LinTrafo:ProductOfMatrices

Suppose $T:\mathbb{R}^2 \to \mathbb{R}^3$ and $S:\mathbb{R}^3 \to \mathbb{R}^3$ are the matrix transformations given by

$$
  T(\mathbf{x}) = A\mathbf{x} =
\begin{pmatrix}
 1&2 \\ 3&4 \\ 1&0
\end{pmatrix} \mathbf{x} \quad \text{and} \quad
  S(\mathbf{y}) = B\mathbf{y} =
\begin{pmatrix}
 1&0 &1 \\ 1 & -1 &2  \\ -1&1&-3
\end{pmatrix} \mathbf{y}.
$$

From {prf:ref}`Prop:LinTrafo:CompositionLintrafos` we know that the composition
$S\circ T: \mathbb{R}^2 \to \mathbb{R}^3$ is also a linear transformation. What is the (standard) matrix of $S\circ T$?

For this we need the images of the unit vectors $\mathbf{e}_1$ and $\mathbf{e}_2$ in $\mathbb{R}^2$.
For each vector we first apply $T$ and then $S$. For $\mathbf{e}_1$ this gives

$$
  T(\mathbf{e}_1) =
\begin{pmatrix}
 1&2 \\ 3&4 \\ 1&0
\end{pmatrix}
\begin{pmatrix}
 1\\0
\end{pmatrix} =
\begin{pmatrix}
 1  \\ 3 \\ 1
\end{pmatrix},
$$

and then

$$
   S (T(\mathbf{e}_1)) =
\begin{pmatrix}
 1&0 &1 \\ 1 & -1 &2  \\ -1&1&-3
\end{pmatrix}
\begin{pmatrix}
 1  \\ 3 \\ 1
\end{pmatrix}=
\begin{pmatrix}
 2  \\ 0 \\ -1
\end{pmatrix}.
$$

Likewise for $\mathbf{e}_2$:

$$
  T(\mathbf{e}_2) =
\begin{pmatrix}
 1&2 \\ 3&4 \\ 1&0
\end{pmatrix}
\begin{pmatrix}
 0\\1
\end{pmatrix} =
\begin{pmatrix}
 2\\4\\0
\end{pmatrix} \,\,\Longrightarrow\,\,
  S (T(\mathbf{e}_2)) =
\begin{pmatrix}
 1&0 &1 \\ 1 & -1 &2  \\ -1&1&-3
\end{pmatrix}
\begin{pmatrix}
 2  \\ 4 \\ 0
\end{pmatrix}=
\begin{pmatrix}
 2  \\ -2 \\ 2
\end{pmatrix}.
$$

So the matrix of $S\circ T$ becomes

$$
  [S\circ T] \,= \,
\begin{pmatrix}
S\circ T(\mathbf{e}_1)&S\circ T(\mathbf{e}_2)
\end{pmatrix} \,\,=\,\,
\begin{pmatrix}
 2 &2 \\ 0&-2 \\ -1&2
\end{pmatrix}.
$$

In the Section {ref}`Sec:MatrixOps` we will define the product of two matrices precisely in such a way that

$$
\begin{pmatrix}
 1&0 &1 \\ 1 & -1 &2  \\ -1&1&-3
\end{pmatrix}
\begin{pmatrix}
 1&2 \\ 3&4 \\ 1&0
\end{pmatrix} =
\begin{pmatrix}
 2 &2 \\ 0&-2 \\ -1&2
\end{pmatrix}.
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
:description: To find the image of two vectors under $T(\vect{x}) = A\vect{x}$.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c8bb24f6-d357-4571-adb3-39ea0fa9e4ee?id=70395
:label: grasple_exercise_3_1_5
:dropdown:
:description: For a linear map $T$, find $T(c\vect{u})$ and $T(\vect{u}+\vect{v})$ if $T(\vect{u})$ and $T(\vect{v})$ are given.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/93048f7c-b755-4445-a532-949f34136096?id=70398
:label: grasple_exercise_3_1_6
:dropdown:
:description: For a linear map $T:\R^2 \to \R^2$, find $T((x_1,x_2))$ if $T(\vect{e}_1)$ and $T(\vect{e}_2)$ are given.
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
:description: To give a geometric description of $T: \vect{x} \mapsto A\vect{x}$.
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

%::::::{grasple}
%:iframeclass: dark-light
%%:url: https://embed.grasple.com/exercises/3f992e7a-19e3-4b83-8d90-db86e323ea94?id=69296
%:label: grasple_exercise_3_1_21
%:dropdown:
%:description: To show that $T(\vect{0}) = \vect{0}$ for a linear transformation.
%::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/94d618e0-de21-491c-ad44-8e29974e0303?id=71098
:label: grasple_exercise_3_1_22
:dropdown:
:description: True or false? If $\{\vect{v}_1,\vect{v}_2,\vect{v}_3\}$ is linearly dependent, then $\{T(\vect{v}_1),T(\vect{v}_2),T(\vect{v}_3)\}$ is also linearly dependent.
::::::

::::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f983b627-10c2-4dd6-a273-2a33e99d0ded?id=71101
:label: grasple_exercise_3_1_23
:dropdown:
:description: True or false? If $\{\vect{v}_1,\vect{v}_2,\vect{v}_3\}$ is linearly independent, then $\{T(\vect{v}_1),T(\vect{v}_2),T(\vect{v}_3)\}$ is also linearly independent.
::::::
