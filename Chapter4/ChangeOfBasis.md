(Sec:BasisChange)=

# Change of Basis

## Introduction

As we have seen, we have freedom of choice with respect to a basis for $\R^n$ or a subspace $S$ of $\R^n$.
Depending on the context one basis may be much more convenient than another.
As a simple example -- we will come back to it later in this section ({prf:ref}`Ex:ChangeOfBasis:MatrixFRomTb1Tb2`) -- consider the reflection along a line through the origin in the plane.

For instance, consider the line $\mathcal{L}$ described by the equation $3x - 2y = 0$. We know that the reflection along this line is a linear transformation. The images of the unit vectors $\vect{e}_1$ and $\vect{e}_2$ are not immediately clear. So it takes some effort to find the standard matrix

$$
 \begin{bmatrix}
    T(\vect{e}_1) & T(\vect{e}_2)
 \end{bmatrix}.
$$

A basis that fits better here would be a basis $\{\vect{b}_1, \vect{b}_2\}$ where $\vect{b}_1$ is a direction vector for the line, and
$\vect{b}_2$ a non-zero vector perpendicular to the line.
For instance, we can take

$$
  \vect{b}_1 = \begin{bmatrix} 2\\3 \end{bmatrix}, \quad
  \vect{b}_2 = \begin{bmatrix} 3\\-2 \end{bmatrix}.
$$

See {numref}`Figure %s <Fig:ChangeOfBasis:Reflection>`.

:::{figure} Images/Fig-ChangeOfBasis-Reflection.svg
:name: Fig:ChangeOfBasis:Reflection
:class: dark-light

Reflection along the line $\mc{L}$.
:::

From the geometry involved it follows that

$$
   T(\vect{b}_1) = \vect{b}_1 \quad \text{and} \quad T(\vect{b}_2) = -\vect{b}_2.
$$

If we work with the basis $\mathcal B$ the transformation takes on a very simple form.
Any vector $\vect{v}$ can be written as

$$
  \vect{v} = c_1\vect{b}_1 + c_2\vect{b}_2,
$$

and then

$$
     T(\vect{v}) =  T(c_1\vect{b}_1 + c_2\vect{b}_2) = c_1\vect{b}_1 -  c_2\vect{b}_2.
$$

In this section we will explain how such a change of basis works.

## Coordinates with Respect to a Basis

We start with a proposition.

::::{prf:proposition}
:label: Prop:ChangeOfBasis:UniqueCoords

If $\mc{B} = \{\vect{b}_1, \vect{b}_2,\ldots,\vect{b}_m\}$ is a basis for a subspace $S$ in $\R^n$,
then any vector $\vect{v}$ in $S$ can written as a linear combination of
$\vect{b}_1, \vect{b}_2,\ldots,\vect{b}_m$ in a *unique* way, i.e.

$$
  \vect{v} = c_1\vect{b}_1 + c_2\vect{b}_2 + \ldots + c_m\vect{b}_m,
$$

for _unique_ constants $c_1,c_2,\ldots,c_m$ in $\R$.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:ChangeOfBasis:UniqueCoords`
:class: tudproof

From the definition of a basis it follows that

$$
   S = \Span{\vect{b}_1, \ldots, \vect{b}_m} \quad \text{with} \quad
              \{\vect{b}_1, \ldots, \vect{b}_m\} \text{ linearly independent}.
$$

Let $ \vect{v}$ be an arbitrary element of $S$. As $\vect{v} \in \Span{\vect{b}_1, \ldots, \vect{b}_m}$,

$$
   \vect{v} = c_1\vect{b}_1 + c_2\vect{b}_2 + \ldots + c_m\vect{b}_m
$$

for some constants $c_1,c_2,\ldots,c_m$.

To prove that the linear combination is unique, suppose that also

$$
    \vect{v} = d_1\vect{b}_1 + d_2\vect{b}_2 + \, \ldots \, + d_m\vect{b}_m
$$

for constants $d_1,d_2,\ldots,d_m$.
Then we have to show that in fact

$$
  c_1 = d_1, \quad  c_2 = d_2, \quad \ldots , \quad   c_m = d_m.
$$

This can be done as follows: subtracting the two expressions for $\vect{v}$ gives

$$
  \vect{0} = \vect{v} - \vect{v} =  (c_1-d_1)\vect{b}_1 + (c_2-d_2)\vect{b}_2 + \ldots + (c_m-d_m)\vect{b}_m.
$$

So, we have a linear combination of the vectors $\vect{b}_i$ equal to the zero vector $\vect{0}$.

From the linear independence of the vectors $\vect{b}_1, \vect{b}_2,\ldots,\vect{b}_m$ it then follows that all the coefficients
$(c_i-d_i)$ must be 0. Thus we find

$$
   (c_1-d_1) = 0, \quad \ldots\,,  \quad  (c_m-d_m) = 0,
$$

from which we can conclude that

$$
c_1 = d_1, \quad c_2 = d_2, \quad \ldots\,,  \quad c_m =d_m.
$$

and we are done.
::::

In this subsection we will be interested mainly in the case where the subspace $S$ is the whole of $\R^n$.

{prf:ref}`Prop:ChangeOfBasis:UniqueCoords` shows that the following definition makes sense.

::::{prf:definition}
:label: Dfn:ChangeOfBasis:Coordinates

Let $\mc{B} = \{\vect{b}_1, \vect{b}_2,\ldots,\vect{b}_m\}$ be a basis for a subspace $S$ in $\R^n$,
and $\vect{v}$ a vector in $S$.
Then the coefficients $c_1,c_2, \ldots, c_m$ for which

$$
  \vect{v} = c_1\vect{b}_1 + c_2\vect{b}_2 + \ldots + c_m\vect{b}_m
$$

are called the **coordinates of the vector $\vect{v}$ with respect to the basis $\mc{B}$**,

and the vector

$$
  [\vect{v}]_{\mc B} = \begin{bmatrix} c_1 \\ c_2 \\ \vdots \\ c_m\end{bmatrix}
$$

is called the **coordinate vector of $\vect{v}$ with respect to the basis $\mc{B}$**.

::::

::::{prf:example}
:label: Ex:ChangeOfBasis:BasicExampleR2

We find the coordinates of the vectors $\vect{v}= \begin{bmatrix} 6 \\ -2\end{bmatrix}$ and $\vect{w}=\begin{bmatrix} -2 \\ 4\end{bmatrix}$ with respect to the basis
$\mc{B} = \{\vect{b}_1, \vect{b}_2 \} =
\left\{ \begin{bmatrix} 1 \\ 3\end{bmatrix}, \begin{bmatrix} 2 \\ 1\end{bmatrix}  \right\}$ of $\R^2$.

For $\vect{v}$ we have to solve the vector equation

$$
   c_1\begin{bmatrix} 1 \\ 3\end{bmatrix}  + c_2\begin{bmatrix} 2 \\ 1\end{bmatrix}\,\,=\,\,\begin{bmatrix}6 \\ -2\end{bmatrix}.
$$

The solution $c_1 = -2,\,c_2 = 4$ gives the answer:

$$
  [\vect{v}]_{\mc B} = \begin{bmatrix} -2 \\ 4\end{bmatrix}.
$$

Likewise the vector $\vect{w}$ has the coordinate vector
$[\vect{w}]_{\mc B} = \begin{bmatrix} 2 \\ -2\end{bmatrix}$.

Namely,

$$
   \begin{bmatrix} -2 \\ 4\end{bmatrix} = 2\begin{bmatrix} 1 \\ 3\end{bmatrix} +(-2)\begin{bmatrix} 2 \\ 1\end{bmatrix}, \quad\text{i.e. }\,
     \vect{w} = 2\vect{b}_1 + (-2) \vect{b}_2.
$$

{numref}`Figure %s <Fig:ChangeOfBasis:AlternativeBasis>` may help to see what is going on geometrically.

```{applet}
:url: change_of_basis/alternative_basis
:fig: Images/Fig-ChangeOfBasis-AlternativeBasis.svg
:name: Fig:ChangeOfBasis:AlternativeBasis
:class: dark-light

The basis $\{\vect{b}_1,\vect{b}_2\}$ of {prf:ref}`Ex:ChangeOfBasis:BasicExampleR2`.
```

::::::{prf:remark}
:label: Rem:ChangeOfBasis:ConventionBasis

A note of warning. Strictly speaking a basis is an _ordered_ set of vectors. By this we mean that the set $\mathcal{B} = \{\vect{b}_1,\vect{b}_2\}$ and the set $\mathcal{B}' = \{\vect{b}_2,\vect{b}_1\}$ are the same. However,
as bases we should consider them as different. This becomes important when we work with coordinates.
<BR>
$[\vect{v}]_{\mathcal{B}} = \begin{bmatrix}c_1\\c_2 \end{bmatrix}$ means that $\vect{v} = c_1\vect{b}_1+c_2\vect{b}_2$,
<BR>
whereas
$[\vect{v}]_{\mathcal{B}'} = \begin{bmatrix}c_1\\c_2 \end{bmatrix}$ should be interpreted $\vect{v} = c_1\vect{b}_2+c_2\vect{b}_1$.
<BR>
To avoid ambiguities like this the way out is to use the notation

$$
  \mathcal{B} = \big(\vect{b}_1,\vect{b}_2, \ldots, \vect{b}_n\big),
$$

when we talk about a basis.
However, we won't, as is quite customary. In case of a basis we will always tacitly assume that the vectors are ordered as they are written down.
::::::

Recall that the **standard basis** of $\R^n$ is given by

$$
  \mathcal{E} = \{\vect{e_1}, \vect{e_2}, \ldots, \vect{e_n}\} =
    \left\{
     \begin{bmatrix} 1 \\ 0 \\ 0\\ \vdots \\ 0 \end{bmatrix},\,
     \begin{bmatrix} 0 \\ 1 \\ 0\\ \vdots \\ 0 \end{bmatrix},\,
    \,\,\ldots\,,\,\,
     \begin{bmatrix} 0 \\ 0 \\ 0\\ \vdots \\ 1 \end{bmatrix}
  \right\}.
$$

With respect to the standard basis it is very easy to find coordinates.

::::{prf:example}
:label: Ex:ChangeOfBasis:CoordsStandardBasis

If $\vect{v} = \begin{bmatrix} a_1 \\ a_2 \\a_3\end{bmatrix}$ is an arbitrary vector in $\R^3$, then

$$
   \vect{v} = a_1 \begin{bmatrix} 1 \\ 0 \\ 0\end{bmatrix} +
               a_2 \begin{bmatrix} 0 \\ 1 \\ 0\end{bmatrix} +
                 a_3 \begin{bmatrix} 0 \\ 0 \\ 1\end{bmatrix} =
              a_1 \vect{e}_1 + a_2 \vect{e}_2 +  a_3  \vect{e}_3.
$$

This means that

$$
  [\vect{v}]_{\mc{E}} = \begin{bmatrix} a_1 \\ a_2 \\a_3\end{bmatrix} = \vect{v}.
$$

So with respect to the standard basis any vector in $\R^3$ is at the same time its coordinate vector.

::::

In fact, this last observation holds more general. That is the content of the following proposition.

::::{prf:proposition}
:label: Prop:ChangeOfBasis:CoordsStandardBasis

For each vector $\vect{v}$ in $\R^n$

$$
   [\vect{v}]_{\mc{E}} =  \vect{v},
$$

where $\mc{E}$ is the standard basis of $\R^n$.
::::

In {prf:ref}`Ex:ChangeOfBasis:BasicExampleR2` we have seen that finding the coordinates of a vector with respect to the basis
$\mc{B} = \{\vect{b}_1, \vect{b}_2 \} =
\left\{ \begin{bmatrix} 1 \\ 3\end{bmatrix}, \begin{bmatrix} 2 \\ 1\end{bmatrix}  \right\}$ amounts to solving a vector equation. The converse, finding $[\vect{w}]_{\mc{E}}$ when $[\vect{w}]_{\mc{B}}$ is given, requires less work. The following example illustrates this.

::::{prf:example}
:label: Ex:ChangeOfBasis:ToStandardBasis
Suppose that with respect to the basis $\mc{B} =      \left\{ \begin{bmatrix} 1 \\ 3\end{bmatrix}, \begin{bmatrix} 2 \\ 1\end{bmatrix}  \right\}$
it is given that

$$
 [\vect{w}]_{\mc{B}} = \begin{bmatrix} f_1 \\ f_2\end{bmatrix}.
$$

Then it follows that

$$
   \vect{w} = f_1\begin{bmatrix} 1 \\ 3\end{bmatrix} + f_2 \begin{bmatrix} 2 \\ 1\end{bmatrix}
            = \begin{bmatrix} 1 & 2 \\ 3 & 1\end{bmatrix}  \begin{bmatrix} f_1 \\ f_2\end{bmatrix}.
$$

The rule to go from basis $\mc{B}$ to the standard basis can thus be written as

:::{math}
:label: Eq:ChangeOfBasis:ToStandardBasis

[\vect{w}]_{\mc E} = P[\vect{w}]_{\mc{B}}, \quad \text{where}\quad P = \left[\,\vect{b}_1 \,\,\vect{b}_2 \,\right].
:::

::::

The procedure of {prf:ref}`Ex:ChangeOfBasis:ToStandardBasis` can be generalized to bases in $\R^n$. Before we state how, we first define another useful concept.

::::{prf:definition}
:label: Dfn:ChangeOfBasis:CoBmatrix

Let ${\mathcal B} = \{\vect{b}_1, \ldots, \vect{b}_n \}$ be a basis of $\R^n$.
The **change-of-coordinates matrix from ${\mathcal B}$ to ${\mathcal E}$** is the matrix

$$
  P_{\mc{B}} =
      \left[\,\vect{b}_1\,\,\vect{b}_1\,\, \ldots\,\, \vect{b}_n\, \right].
$$

::::

::::{prf:proposition}
:label: Prop:ChangeOfBasis:ToStandardBasis

If ${\mathcal B} = \{\vect{b}_1, \,\vect{b}_2,\, \ldots,\, \vect{b}_n \}$ is a basis of $\R^n$, then for any vector $\vect{v}$ in $\R^n$ it holds that

$$
   \vect{v} =  P_{\mc{B}} [\vect{v}]_{\mc B}.
$$

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:ChangeOfBasis:ToStandardBasis`
:class: tudproof

Suppose

$$
   [\vect{v}]_{\mc B} = \begin{bmatrix} p_1 \\ p_2 \\ \vdots \\ p_n \end{bmatrix}.
$$

This is shorthand for

$$
         \vect{v} = p_1\vect{b}_1+ p_2\vect{b}_2+\ldots + p_n\vect{b}_n,
$$

and this linear combination of $n$ vectors in $\R^n$ can be written as a matrix-vector product:

$$
   \vect{v} = \left[\begin{matrix} \vect{b}_1 \,\,\vect{b}_2  \,\,\ldots\,\,  \vect{b}_n \end{matrix}\right]\begin{bmatrix} p_1 \\  p_2 \\ \vdots \\ p_n \end{bmatrix} = P_{\mc{B}} [\vect{v}]_{\mc B}.
$$

::::

::::{exercise}
:label: Exc:ChangeOfBasis:InvertiblePB

Show that every change-of-coordinates matrix $P_{\mc{B}}$ is invertible.
::::

::::{admonition} Solution to&nbsp;{numref}`Exc:ChangeOfBasis:InvertiblePB`
:class: solution, dropdown

Let $\mc{B} = \{\vect{b}_1,\vect{b}_2, \ldots, \vect{b}_n\}$ be any basis of $\R^n$.
<BR>
By definition

$$
   P_{\mc{B}} = [\,\vect{b}_1\,\,\vect{b}_2\,\,\ldots\,\,\vect{b}_n\,].
$$

This is an $n \times n$ matrix with $n$ linearly independent columns, so it is an invertible matrix.

::::

The following proposition is an immediate consequence of
{prf:ref}`Prop:ChangeOfBasis:ToStandardBasis` and {numref}`Exc:ChangeOfBasis:InvertiblePB`.

::::{prf:proposition}

Suppose $\mc{B}$ is a basis for $\R^n$, and $P_{\mc{B}}$ is the change-of-coordinates matrix. Then the coordinates of any vector $\vect{v}$ with respect to basis $\mc{B}$ are given by

$$
   [\vect{v}]_{\mc B} = P^{-1}_{\mc{B}} \vect{v}.
$$

::::

::::{prf:example}
:label: Ex:ChangeOfBasis:PropCoB

Have another look at {prf:ref}`Ex:ChangeOfBasis:BasicExampleR2` where we found the coordinates of the vector $ \vect{v}= \begin{bmatrix} 6 \\ -2\end{bmatrix}$ with respect to the basis
$\mc{B} = \{\vect{b}_1, \vect{b}_2 \} =
    \left\{ \begin{bmatrix} 1 \\ 3\end{bmatrix}, \begin{bmatrix} 2 \\ 1\end{bmatrix}  \right\}$.

The change-of-coordinates matrix from basis $\mc{B}$ to the standard basis is given by

$$
  P_{\mc{B}} =  \begin{bmatrix} \vect{b}_1 & \vect{b}_2 \end{bmatrix} = \begin{bmatrix} 1& 2 \\ 3&1\end{bmatrix}.
$$

The inverse matrix then becomes

$$
   P^{-1}_{\mc{B}} =  \begin{bmatrix} 1& 2 \\ 3&1\end{bmatrix}^{-1} = -\frac15 \begin{bmatrix} 1& -2 \\ -3&1\end{bmatrix}.
$$

So the coordinates of the vector $\vect{v}$ can now also be found as follows:

$$
   [\vect{v}]_{\mc{B}} = P^{-1}_{\mc{B}}[\vect{v}]_{\mc{E}}
                       =  -\frac15 \begin{bmatrix} 1& -2 \\ -3&1\end{bmatrix}\begin{bmatrix} 6 \\ -2\end{bmatrix}
                       = -\frac15\begin{bmatrix} 10 \\ -20\end{bmatrix}
                       = \begin{bmatrix} -2 \\ 4\end{bmatrix}.
$$

::::

We conclude this subsection with an example from physics.

::::{prf:example}
:label: Ex:ChangeOfBasis:Lorentz

Suppose $(x,y,z,t)$ and $(x',y',z',t')$ are the coordinates of an event in two frames with the origins coinciding at $t = t'= 0$ where the primed frame is seen from the unprimed frame as moving with speed $v$ along the $x$-axis.

The connection between two systems can be rewritten by a four-dimensional 'space-time' coordinate transformation

$$
  \begin{cases}
     x'= \gamma (x - vt) \\
     y'= y \\
     z'= z \\
     t'= \gamma \left( t - \dfrac{c}{v^2} x \right)
  \end{cases}
$$

Here $c$ is the speed of light, and $\gamma = \left(\sqrt{1 - \dfrac{v^2}{c^2}}\right)^{-1}$ the so-called Lorentz factor.

Systems that move with a constant velocity with respect to each other are called **inertial systems**.
In each reference frame, an observer can use a local coordinate system (usually Cartesian coordinates in this context) to measure lengths, and a clock to measure time intervals. An event is something that happens at a point in space at an instant of time, or more formally a point in space-time. The transformation connects the space and time coordinates of an event as measured by an observers in the different frames.

::::

## The Matrix of a Linear Transformation with Respect to a Basis

In {numref}`Sec:LinTrafo` we have seen that every linear transformation $T:\R^n \to \R^m$ can be represented by its standard matrix

::::{math}
:label: Eq:ChangeOfBasis:StandardMatrix

A = \begin{bmatrix} T(\vect{e}_1) & T(\vect{e}_2) & \ldots & T(\vect{e}_n) \end{bmatrix}.

::::

This means that for each vector $\vect{v}$ in $\R^n$ it holds that

$$
   T(\vect{v}) = A\,\vect{v}.
$$

In this way we have expressed everything into coordinates with respect to the standard bases $\mc{E}$ and $\mc{E}'$ for $\R^n$ and $\R^m$ respectively.

We will see that formula {eq}`Eq:ChangeOfBasis:StandardMatrix` can be generalized almost automatically to arbitrary bases for $\R^n$ and $\R^m$.

::::{prf:proposition}
:label: Prop:ChangeOfBasis:MatrixOfTrafo

Suppose that $T:\R^n \to \R^m$ is a linear transformation, that $\mc{B} =\{\vect{b}_1, \ldots, \vect{b}_n\}$ is a basis for $\R^n$ and $\mc{C}$ a basis for $\R^m$.
Then for each vector $\vect{v}$ in $\R^n$:

$$
  [T(\vect{v})]_{\mc{C}} = \left[[T(\vect{b}_1)]_{\mc{C}} \,\rule[-.5ex]{0ex}{3ex}\,[T(\vect{b}_2)]_{\mc{C}}\,\,\ldots\,\,[T(\vect{b}_n)]_{\mc{C}}\right] [\vect{v}]_{\mc{B}}
$$

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:ChangeOfBasis:MatrixOfTrafo`
:class: tudproof

We use the definition of the coordinate vector and the linearity of the transformation. In fact we can play copycat with the proof of
{prf:ref}`Thm:LinTrafo:LinTrafo=MatrixTrafo` in the section of linear transformations.

Indeed, suppose that $\vect{v}$ is a vector in $\R^n$, and that

$$
    [\vect{v}]_{\mc{B}} = \begin{bmatrix} f_1 \\ \vdots \\ f_n \end{bmatrix}, \quad \text{so} \quad
    \vect{v} = f_1\vect{b}_1 + f_2\vect{b}_2 + \ldots + f_n\vect{b}_n.
$$

Because of the linearity of $T$ we then have

:::{math}
:label: Eq:ChangeOfBasis:LinearityTransform

T(\vect{v}) = f_1T(\vect{b}_1) + f_2T(\vect{b}_2) + \ldots + f_nT(\vect{b}_n).

:::

Now we take the coordinate vectors with respect to basis $\mc{C}$:

:::{math}
:label: Eq:ChangeOfBasis:LinearityCoords

[T(\vect{v})]_{\mc{C}} = f_1[T(\vect{b}_1)]_{\mc{C}} + f_2[T(\vect{b}_2)]_{\mc{C}} + \ldots + f_n[T(\vect{b}_n)]_{\mc{C}}.


:::

(See {numref}`Exc:ChangeOfBasis:LinearityOfCoords`.)

Noting that the term on the right side of Equation {eq}`Eq:ChangeOfBasis:LinearityCoords` is a linear combination of $m$-vectors, we can write the identity as

$$
    \begin{array}{rcl}
    [T(\vect{v})]_{\mc{C}} &=& \left[ [\,T(\vect{b}_1)]_{\mc{C}}\,\,\,\rule[-1ex]{0ex}{4ex}\,\ldots\,\,[T(\vect{b}_n)]_{\mc{C}}\,\right]
                                    \begin{bmatrix} f_1 \\ \vdots \\ f_n \end{bmatrix} \\
    &=& \left[\,[T(\vect{b}_1)]_{\mc{C}}\,\,\,\rule[-0.5ex]{0ex}{3ex}\,\ldots\,\,[T(\vect{b}_n)]_{\mc{C}}\,\right][\vect{v}]_{\mc{B}}.
     \end{array}
$$

::::

::::{exercise}
:label: Exc:ChangeOfBasis:LinearityOfCoords

Prove the identity

$$
   [c_1\vect{v}_1 +c_2\vect{v}_2+ \ldots + c_n\vect{v}_n ]_{\mc{B}} =
   c_1[\vect{v}_1 ]_{\mc{B}} + c_2[\vect{v}_2 ]_{\mc{B}} + \ldots + c_n[\vect{v}_n ]_{\mc{B}}
$$

that is used to go from Equation {eq}`Eq:ChangeOfBasis:LinearityTransform` to Equation {eq}`Eq:ChangeOfBasis:LinearityCoords` in the proof of {prf:ref}`Prop:ChangeOfBasis:MatrixOfTrafo`.

**Hint:** first show the correctness of the identities

$$
   [\vect{v}_1 +\vect{v}_2 ]_{\mc{B}} =
   [\vect{v}_1 ]_{\mc{B}} + [\vect{v}_2 ]_{\mc{B}}
   \quad \text{and} \quad
   [c\vect{v} ]_{\mc{B}} = c[\vect{v}]_{\mc{B}}.
$$

::::

{prf:ref}`Prop:ChangeOfBasis:MatrixOfTrafo` is fairly general. We will mostly use it in the situation where the linear transformation goes from $\R^n$ to itself, and where we use the same basis $\mc{B}$ in the domain and the codomain. Before we do so, we introduce a new notation for the general case.

::::{prf:definition}
:label: Dfn:ChangeOfBasis:Matrix-wrt-Basis

Let $T:\R^n \to \R^m$ be a linear transformation, and let $\mc{B} = \{\vect{b}_1,\ldots,\vect{b}_n\}$ be a basis for $\R^n$, $\mc{C}$ a basis for $\R^m$. Then the **matrix of $T$ with respect to bases $\mc{B}$ and $\mc{C}$** is defined by

$$
   [T]_{\mc{C}\leftarrow \mc{B}} = \big[\,[T(\vect{b}_1) ]_{\mc{C}}\,\,
   [T(\vect{b}_2 )]_{\mc{C}}\,\,\ldots \,\,[T(\vect{b}_n) ]_{\mc{C}}\,\big].
$$

In the case where $n = m$ and $\mc{B} = \mc{C}$ we will use the slightly simpler notation

$$
     [T]_{\mc{B}} = [T]_{\mc{B}\leftarrow \mc{B}} =\,
     \big[\,\,[T(\vect{b}_1) ]_{\mc{B}}\,\,\,
   [T(\vect{b}_2) ]_{\mc{B}}\,\,\,\ldots \,\,\,[T(\vect{b}_n) ]_{\mc{B}}\,\,\big],
$$

and call this simply **the matrix of $T$ with respect to basis $\mathcal{B}$**.

::::

If we let $\mc{B}$ be the standard basis $\mc{E}$ of $\R^n$ and $\mc{C}$ is the standard basis $\mc{E'}$ of $\R^m$ we get the following:

$$
    [T]_{\mc{E}'\leftarrow \mc{E}}   \,=\,\,
    \left[\,[T(\vect{e}_1) ]_{\mc{E}'}\,\,\ldots \,\rule[-.5ex]{0ex}{2.5ex}\,[T(\vect{e}_n) ]_{\mc{E}'}\,\right] \,\,=\,\,
                          \big[\,T(\vect{e}_1)  \,\,   \ldots \,\, T(\vect{e}_n)  \,\big].
$$

This is the "good old" standard matrix as in {numref}`Subsec:LinTrafo:LinTrafoeqMatrixTrafo`.

::::{prf:example}
:label: Ex:ChangeOfBasis:Reflection

Let us have a second look at the transformation mentioned in the introduction, i.e., the reflection in the plane along the line $3x-2y=0$. We found that the reflection behaves in a very simple way with respect to the basis

$$
   \mc{B} = \{\vect{b}_1, \vect{b}_2  \} =
    \left\{\begin{bmatrix} 2\\3 \end{bmatrix}, \,\begin{bmatrix} 3\\-2 \end{bmatrix}  \right\}.
$$

Recall that this basis was chosen so that $\vect{b}_1$ lies on $\mathcal{L}$ and $ \vect{b}_2$ is perpendicular to $\mathcal{L}$, from which we deduced that

$$
   T(\vect{b}_1) = \vect{b}_1 \quad \text{and} \quad T(\vect{b}_2) = -\vect{b}_2.
$$

From this we can immediately write down the matrix of $T$ with respect to $\mc{B}$:

$$
   [T]_{\mathcal{B}} = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}.
$$

::::

::::{prf:example}
:label: Ex:ChangeOfBasis:MatrixFRomTb1Tb2

We will find the matrix of the linear transformation ${T:\R^2 \to\R^2}$ sending $\vect{b}_1 = \begin{bmatrix} 1\\3\end{bmatrix}$ to $\begin{bmatrix} 5 \\ 5\end{bmatrix}$
and $\vect{b}_2 = \begin{bmatrix} 2\\1\end{bmatrix}$ to $\begin{bmatrix} 1 \\ -2\end{bmatrix}$
with respect to the basis $\mathcal{B} =\{ \vect{b}_1, \vect{b}_2\}$.

The only thing that remains to be done before we can write down

$$
   [T]_{\mc{B}} = \big[\, [T(\vect{b}_1 )]_{\mc{B}}\,\,\,[T(\vect{b}_2 )]_{\mc{B}}\,\big]
$$

is to find the coordinates of the given images with respect to the basis $\mathcal{B}$. This can be done as in {prf:ref}`Ex:ChangeOfBasis:BasicExampleR2` or by using the change-of-coordinates matrix as in {prf:ref}`Ex:ChangeOfBasis:PropCoB`:

$$
 \left[T(\vect{b}_1 )\right]_{\mc{B}} = (P_{\mc{B}})^{-1} T(\vect{b}_1)   = -\dfrac{1}{5} \begin{bmatrix}1 & -2 \\ -3 & 1  \end{bmatrix}\begin{bmatrix} 5 \\ 5\end{bmatrix} = \begin{bmatrix} 1 \\ 2\end{bmatrix},
$$

and

$$
  \left[T(\vect{b}_2) \right]_{\mc{B}}=   (P_{\mc{B}})^{-1} T(\vect{b}_2)  = -\dfrac{1}{5} \begin{bmatrix}1 & -2 \\ -3 & 1  \end{bmatrix}
  \begin{bmatrix} 1 \\ -2\end{bmatrix} = \begin{bmatrix} -1 \\ 1\end{bmatrix},
$$

so

$$
   [T]_{\mc{B}} = \left[\, [T(\vect{b}_1 )]_{\mc{B}}\,\,\,[T(\vect{b}_2 )]_{\mc{B}}\,\right] = \begin{bmatrix}1 & -1 \\ 2 & 1  \end{bmatrix}.
$$

::::

::::{grasple} 
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d6aa929c-7614-4af2-b015-31e2e6fd7b80?id=104847
:label: grasple_exercise_4_3_T1
:dropdown:
:description: Finding  $[T]_{\mathcal{B}}$ for a 'nice' linear transformation.

::::



%::::{exercise}
%:label: Exc:ChangeOfBasis:FindSimpleMatrix

%Consider the linear transformation $T$ with the standard matrix $A$ given by

%$$
%  T:\R^3 \to \R^3, \quad T(\vect{x}) = A\vect{x} =
%  \begin{bmatrix} -2 & 1 & 0 \\ -7 & 3 & 1 \\ 2 & 0 & -1
%  \end{bmatrix}\vect{x}.
%$$

%It is given that

%$$
%  A\begin{bmatrix} 0 \\0\\1  \end{bmatrix} =\begin{bmatrix} 0 \\1\\-1  \end{bmatrix},
% A\begin{bmatrix} 0\\1\\-1  \end{bmatrix} =\begin{bmatrix} 1  \\2 \\ 1  \end{bmatrix},
%  \quad \text{and } \quad
%  A\begin{bmatrix} 1 \\2\\1  \end{bmatrix} =\begin{bmatrix} 0\\0\\ 1  \end{bmatrix}.
%$$

%Find the matrix $[T]_{\mc{B}}$ for the basis

%$$
%  \mc{B} = \left\{ \begin{bmatrix} 0 \\0\\ 1  \end{bmatrix},\,\begin{bmatrix} 0 \\1\\ -1  \end{bmatrix}, \,\begin{bmatrix} 1 \\2\\1  \end{bmatrix} \right\}.
%$$

%::::

In the next example we will find the matrix of the rotation $R$ about the origin through an angle $\frac13\pi$. In {numref}`Sec:GeomLinTrans` we have already seen the standard matrix of this linear transformation, involving sines and cosines. As the example shows a change of basis may lead to an interesting alternative.

::::{prf:example}
:label: Ex:ChangeOfBasis:Rotation

Let $\mc{B}$ be the basis

$$
  \left\{\vect{b}_1, \vect{b}_2 \right\} = \left\{ \begin{bmatrix} 2 \\ 0  \end{bmatrix}, \begin{bmatrix} -1 \\ \sqrt{3}  \end{bmatrix} \right\}.
$$

Note that $\vect{b}_1$ and $ \vect{b}_2$ are two vectors of length 2 subtending an angle
$\frac23\pi$. See {numref}`Figure %s <Fig:ChangeOfBasis-TriangularGrid>`.
The vector $\vect{b}_1+\vect{b}_2 = \begin{bmatrix} 1 \\ \sqrt{3}  \end{bmatrix}$, is also indicated in the figure.

:::{figure} Images/Fig-ChangeOfBasis-TriangularGrid.svg
:name: Fig:ChangeOfBasis-TriangularGrid
:class: dark-light

Rotation in disguise.

:::

Now let us find the matrix of the rotation $R$ with respect to basis $\mc{B}$. From the figure we read off

$$
  R(\vect{b}_1) =  \vect{b}_1+\vect{b}_2
      \quad\text{and} \quad
  R(\vect{b}_2) = -\vect{b}_1.
$$

From this we can immediately write down the matrix of $R$ with respect to the $\mc{B}$-basis:

$$
   [R]_{\mc{B}} = \big[\, [R(\vect{b}_1)]_{\mc{B}} \,\, [R(\vect{b}_2)]_{\mc{B}} \,\big]
                = \begin{bmatrix} 1 & -1 \\ 1 & 0 \end{bmatrix}.
$$

::::

In {prf:ref}`Ex:ChangeOfBasis:Reflection` and {prf:ref}`Ex:ChangeOfBasis:Rotation`, the reflection and the rotation, we came up first with bases that fitted the geometric context. And then we found the (very simple) matrix with respect to these bases. However, usually we prefer to have the standard matrix. In the last section we will see how a change of basis affects the matrix of a linear transformation.

(Subsec:ChangeOfBasis:RelationTETB)=

## The relation between $[T]_{\mc{E}}$ and $[T]_{\mc{B}}$

We have seen how to convert vectors from one coordinate system (i.e., basis) to another, and also how to construct the matrix of a linear transformation with respect to an arbitrary basis. In this section we will present a ready-made formula that connects the matrices with respect to two different bases. In this subsection we will restrict ourselves to the common situation of a linear transformation from $\R^n$ to itself, where one of the bases is the standard basis.

We start with an example that illustrates the underlying ideas.

::::{prf:example}
:label: Ex:ChangeOfBasis:MatrixChangeBasisR2

Consider the linear transformation $T:\R^2\to\R^2$ with the standard matrix
$A = \begin{bmatrix}  1 & 4 \\ 2 & 1\end{bmatrix}$, i.e.

$$
  T(\vect{x}) = A\vect{x} = \begin{bmatrix}  1 & 4 \\ 2 & 1\end{bmatrix}\vect{x}.
$$

We want to find the matrix of $T$ with respect to the basis

$$
  \mc{B} = \left\{\vect{b}_1,\vect{b}_2\right\}
         = \left\{\begin{bmatrix}  2\\ -1 \end{bmatrix},\,
            \begin{bmatrix}  1\\ 1 \end{bmatrix}\right\}.
$$

Let $P_{\mc{B}}$ denote the change-of-coordinates matrix.

So we have, for each vector $\vect{x}$:

$$
   \vect{x} = [\vect{x}]_{\mc{E}} = P [\vect{x}]_{\mc{B}},\quad\text{where }\,
   P = \PB = \begin{bmatrix}  2 & 1\\ -1 & 1\end{bmatrix}.
$$

To obtain the matrix $[T]_{\mc{B}}$ we need the coordinate vectors

$$
   [T(\vect{b}_1)]_{\mc{B}} \quad \text{and} \quad [T(\vect{b}_2)]_{\mc{B}}.
$$

Let us start with the vector $\vect{b}_1$:

$$
   T(\vect{b}_1)= A\vect{b}_1  = \begin{bmatrix}  1 & 4 \\ 2 & 1\end{bmatrix} \begin{bmatrix}  2\\ -1 \end{bmatrix} =  \begin{bmatrix}  -2\\ 3 \end{bmatrix},
  \,\text{ so }\,
   \left[T(\vect{b}_1)\right]_{\mc{B}} =    P^{-1} \begin{bmatrix}  -2\\ 3 \end{bmatrix}
   = \begin{bmatrix}  -\nicefrac{5}{3}\\ \nicefrac{4}{3} \end{bmatrix}.
$$

For the second basis vector $\vect{b}_2$ we could proceed likewise.

Alternatively, we can start from the coordinates of an arbitrary vector with respect to the basis $\mc{B}$, and then step by step work our way to the matrix $[T]_{\mc{B}}$ such that:

$$
   \left[T(\vect{x}) \right]_{\mc{B}} =  [T]_{\mc{B}}\,\left[\vect{x} \right]_{\mc{B}}.
$$

<ol type="i">
<li>

First we find the coordinates of the vector $\vect{x}$ with respect to the standard basis $\mc{E}$:

$$
    \vect{x} =  \left[\vect{x}\right]_{\mc{E}} = P\left[\vect{x}\right]_{\mc{B}}.
$$

</li>
<li>

Then we use the standard matrix of $T$ to find the coordinate vector of $T(\vect{x})$
with respect to the standard basis:

$$
    T(\vect{x})  = A \vect{x}  = A\,P\left[\vect{x}\right]_{\mc{B}}.
$$

</li>
<li>

And lastly we convert back to coordinates with respect to the $\mc{B}$-basis:

$$
    \left[T(\vect{x})\right]_{\mc{B}}  = P^{-1} T(\vect{x})=  P^{-1}AP\left[\vect{x}\right]_{\mc{B}}.
$$

</li>
</ol>

We see that the matrix $P^{-1}AP$ does the job:

:::{math}
:label: Eq:ChangeOfBasis:PAPinv

[T]_{\mc{B}} \,=\, P^{-1}AP.

:::

For the given transformation and basis we find

$$
\begin{array}{rcl}
   [T]_{\mc{B}} &=& \begin{bmatrix}  2 & 1\\ -1 & 1\end{bmatrix}^{-1}
  \begin{bmatrix}  1 & 4 \\ 2 & 1\end{bmatrix}
  \begin{bmatrix}  2 & 1\\ -1 & 1\end{bmatrix}\\
  &=&
   \dfrac{1}{3}\begin{bmatrix}  1 & -1\\ 1 & 2\end{bmatrix}
  \begin{bmatrix}  1 & 4 \\ 2 & 1\end{bmatrix}
  \begin{bmatrix}  2 & 1\\ -1 & 1\end{bmatrix} =
  \dfrac{1}{3}\begin{bmatrix}  -5& 2\\ 4 & 11\end{bmatrix}
  \end{array}
$$

Verify that the first column indeed corresponds to the image of $\vect{b}_1$ as we found earlier.

::::

::::{warning}

Note that the product $PAP^{-1}$ in Equation {eq}`Eq:ChangeOfBasis:PAPinv` cannot be simplified to $PP^{-1}A$, which would be equal to $A$ itself!

::::

{prf:ref}`Ex:ChangeOfBasis:MatrixChangeBasisR2` contains an informal proof, or rather, a "proof by example", of the following proposition.

::::{prf:proposition}
:label: Prop:ChangeOfBasis:MatrixChangeStandardBasis

Suppose $\mc{B}$ is a basis of $\R^n$, and $P = P_{\mc{B}}$ is the change-of-coordinates matrix.
If $T:\R^n \to \R^n$ is a linear transformation with standard matrix $A$, then the matrix
of $T$ with respect to the basis $\mc{B}$ is given by

:::{math}
:label: Eq:ChangeOfBasis:MatrixChangeStandardBasis

[T]_{\mc{B}} = P^{-1}AP.

:::

The following diagram illustrates what is going on:

$$
\begin{array}{ccc}
\R^n & \underrightarrow {\rule{3em}{0ex} T \rule{3em}{0ex}} & \R^n \\[5ex]
\vect{x} = P[\vect{x}]_{\mc{B}} & \underrightarrow {\rule{3em}{0ex} A\rule{3em}{0ex}} &
\begin{array}[t]{l}A\vect{x} = T(\vect{x} ) \\ = AP[\vect{x}]_{\mc{B}} \end{array} \\[1ex]
P_{\mc{B}}\left  \uparrow \rule{0ex}{4em} \right. \rule{2em}{0ex}   &  &  P^{-1}_{\mc{B}}\,\left  \downarrow \rule{0ex}{4em} \right.\,
\left  \uparrow \rule{0ex}{4em} \right.P_{\mc{B}}  \\
   {[\vect{x}]}_{\mc{B}} & \underrightarrow {\rule{3em}{0ex} [T]_{\mc{B}} \rule{3em}{0ex}} & \quad
   \begin{array}{l}[T(\vect{x})]_{\mc{B}} \\
   = P^{-1}AP[\vect{x}]_{\mc{B}}\end{array}
\end{array}
$$

::::

Note that Equation {eq}`Eq:ChangeOfBasis:MatrixChangeStandardBasis` is equivalent to

$$
   A = P [T]_{\mc{B}}P^{-1}, \quad \text{or: }\,  [T]_{\mc{E}} = P_{\mc{B}}[T]_{\mc{B}}\left(P_{\mc{B}}\right)^{-1},
$$

and as such gives a quick way to go from an alternative basis to the standard basis.

::::{exercise}
:label: Exc:ChangeOfBasis:PinvAPversusPBinvP

Suppose $P$ is an invertible matrix.

Show that for matrices $A$ and $B$

$$
   B = P^{-1}A\,P \,\, \iff \,\,A = P\,B\,P^{-1}.
$$

::::

::::{admonition} Solution to&nbsp;{numref}`Exc:ChangeOfBasis:PinvAPversusPBinvP`
:class: solution, dropdown

Starting from $B = P^{-1}A\,P$   multiply both sides from the left by $P$ and from the right by $P^{-1}$,
and use that $P^{-1}P = PP^{-1} = I$:

$$
   B = P^{-1}AP  \iff  PBP^{-1} = P(P^{-1}AP)P^{-1} = PP^{-1}APP^{-1} = A.
$$

::::

::::{prf:example}
:label: Ex:ChangeOfBasis:MatrixOrthProjection

We want to find the matrix of the orthogonal projection $T$ in $\R^3$ onto the plane

$$
    V:   x - y - 2z = 0.
$$

A suitable basis here is a basis $\mc{B} = \{\vect{b}_1, \vect{b}_2,\vect{b}_3\}$ where the first two vectors lie in the plane, and the third vector is perpendicular to the plane.
See {numref}`Figure %s <Fig:ChangeOfBasis:Projection>`.

```{applet}
:url: change_of_basis/projection
:fig: Images/Fig-ChangeOfBasis-Projection.svg
:name: Fig:ChangeOfBasis:Projection
:class: dark-light

Projection with respect to a suitable basis.
```

For instance, we can take

$$
   \vect{b}_1 = \begin{bmatrix}2\\0\\1  \end{bmatrix}, \quad
   \vect{b}_2 = \begin{bmatrix}1\\1\\0  \end{bmatrix}, \quad
   \vect{b}_3 = \begin{bmatrix}1\\-1\\-2  \end{bmatrix}.
$$

The orthogonal projection maps $\vect{b}_3$ to the origin and leaves the other two basis vectors invariant:

$$
  T(\vect{b}_1) = \vect{b}_1, \quad  T(\vect{b}_2) = \vect{b}_2, \quad
   T(\vect{b}_3) = \vect{0}.
$$

Hence

$$
  [T]_{\mc{B}} =  \begin{bmatrix}1 & 0 & 0\\0& 1& 0\\0&0&0  \end{bmatrix},
$$

and we can write down the standard matrix in one stroke:

:::{math}
:label: Eq:ChangeOfBasis:ProjMatrix

[T]_{\mc{E}} = P_{\mc{B}}[T]_{\mc{B}}\left(P_{\mc{B}}\right)^{-1} =
\begin{bmatrix}2 & 1 & 1\\0& 1& -1\\1&0&-2 \end{bmatrix}
\begin{bmatrix}1 & 0 & 0\\0& 1& 0\\0&0&0 \end{bmatrix}
\begin{bmatrix}2 & 1 & 1\\0& 1& -1\\1&0&-2 \end{bmatrix}^{-1}.
:::

This can be evaluated to yield 

:::{math}
:label: Eq:ChangeOfBasis:ProjMatrix2
  [T]_{\mc{E}} = \frac16 \begin{bmatrix}5 & 1 & 2\\1& 5& -2\\2&-2&2 \end{bmatrix}.
:::

::::

::::{exercise}
:label: Exc:ChangeOfBasis:CheckIdempotent

As was shown in {prf:ref}`Prop:GeomLinTrans:ProjSquaredisProj` of {numref}`Subsec:GeomLinTrans:Proj` the matrix $A$ of a projection has to satisfy the identity
$A^2=A$. Show that the matrix $[T]_{\mc{E}}$ of {prf:ref}`Ex:ChangeOfBasis:MatrixOrthProjection` indeed satisfies this identity.

(To verify this you don't have to compute the matrix as given by Equation {eq}`Eq:ChangeOfBasis:ProjMatrix2`.)

::::

::::{admonition} Solution to&nbsp;{numref}`Exc:ChangeOfBasis:CheckIdempotent`
:class: solution, dropdown

Obviously the matrix $B = [T]_{\mc{B}} =  \begin{bmatrix}1 & 0 & 0\\0& 1& 0\\0&0&0  \end{bmatrix}$ has the property $B^2 = B$.

It follows that the matrix $A = P_{\mathcal{B}} B P_{\mathcal{B}}^{-1} = PBP^{-1}$ has it too:

$$
   A^2 = PBP^{-1}PBP^{-1} = PB^2 P^{-1} = PBP^{-1} = A. 
$$

::::

In the last subsection we will generalize the formula to the more general situation of a linear transformation from $\R^n$ to $\R^m$ and arbitrary bases $\mc{B},\mc{B}'$ for $\R^n$, and bases
$\mc{C},\mc{C}'$ for $\R^m$.

(Subsec:ChangeOfBasis:GeneralTransformationFormula)=

## General Transformation Formula for Matrices of Linear Transformation

In the previous subsections we studied the relations of the coordinates with respect to the standard basis and one other alternative basis $\mc{B}$. In this section we go one step further and omit the restriction that one of the bases is the standard basis. We will see that the generalizations are pretty straightforward.

First of all we will extend the notion of a change-of-coordinates matrix.

::::{prf:definition}
:label: Dfn:ChangeOfBasis:CoBmatrixGeneral

Let ${\mathcal B} = \{\vect{b}_1, \ldots, \vect{b}_n \}$ and ${\mathcal C} = \{\vect{c}_1, \ldots, \vect{c}_n \}$ be two bases of $\R^n$. The **change-of-coordinates matrix from ${\mathcal B}$ to ${\mathcal C}$** is the matrix

$$
  P_{\mc{C} \leftarrow \mc{B}} =
      \left[\,[\vect{b}_1]_{\mc{C}} \,\, [\vect{b}_2]_{\mc{C}}  \,\, \rule[-1ex]{0ex}{3ex}\,\,\, \ldots \,\,\,[\vect{b}_n]_{\mc{C}}\right].
$$

Note that in the situation where $\mc{C}$ is the standard basis, we have that

$$
   P_{\mc{C} \leftarrow \mc{B}} = P_{\mc{E} \leftarrow \mc{B}} =  P_{\mc{B}}.
$$

::::

Again, as the name suggests, the change-of-coordinates matrix can be used to switch from coordinates with respect to one basis to coordinates with respect to another basis.

::::{prf:proposition}
:label: Prop:ChangeOfBasis:CoBmatrix

If ${\mathcal B} = \{\vect{b}_1, \ldots, \vect{b}_n \}$ and ${\mathcal C} = \{\vect{c}_1, \ldots, \vect{c}_n \}$ are two bases of $\R^n$, then for any vector $\vect{v}$ in $\R^n$ it holds that

$$
     [\vect{v}]_{\mc{C}} = \CoBmatrix{B}{C} [\vect{v}]_{\mc{B}}.
$$

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:ChangeOfBasis:CoBmatrix`
:class: tudproof

Again we will make use of the identity

$$
[p_1\vect{v}_1+\ldots + p_k\vect{v_k}]_{\mc B}  =  p_1[\vect{v}_1]_{\mc B}+ \ldots +p_k[\vect{v}_k]_{\mc B}.
$$

Thus, suppose that

$$
   [\vect{v}]_{\mc B} = \begin{bmatrix} p_1 \\ \vdots \\ p_n \end{bmatrix} \quad \text{i.e.} \quad
      \vect{v} = p_1\vect{b}_1+ \ldots + p_n\vect{b}_n.
$$

Then

$$
   [\vect{v}]_{\mc C} = [p_1\vect{b}_1+ \ldots + p_n\vect{b}_n]_{\mc C} = p_1[\vect{b}_1]_{\mc C}+ \ldots + p_n[\vect{b}_n]_{\mc C}.
$$

The last expression is a linear combination of $n$ vectors in $\R^n$ and consequently can be written as a matrix-vector product:

$$
   [\vect{v}]_{\mc C} = \big[ \,[\vect{b}_1]_{\mc C}\,\, \ldots \,\, [\vect{b}_n]_{\mc C} \,\big] \begin{bmatrix} p_1 \\ \vdots \\ p_n \end{bmatrix} =
        \CoBmatrix{B}{C}[\vect{v}]_{\mc B},
$$

as this is exactly how $\CoBmatrix{B}{C}[\vect{v}]$ was defined in {prf:ref}`Dfn:ChangeOfBasis:CoBmatrix`.
::::

::::{exercise}
:label: Exc:ChangeOfBasis:InverseOfMatrixCoB

Suppose $\mc{B}$ and $\mc{C}$ are two bases of $\R^n$.
Show that the change-of-coordinates matrix $P_{\mc{C}\leftarrow\mc{B}}$ is invertible, and that

$$
   P_{\mc{B}\leftarrow\mc{C}} = \left(P_{\mc{C}\leftarrow\mc{B}}\right)^{-1}.
$$

::::

::::{exercise}
:label: Exc:ChangeOfBasis:RelationMatricesCoB

Suppose $\mc{B}, \mc{C}$ and $\mc{D}$ are three bases of $\R^n$.
What is the relation between the
change-of-coordinates matrices
$ P_{\mc{B}\leftarrow\mc{C}}, \quad
P_{\mc{B}\leftarrow\mc{D}} \quad \text{and} \quad P_{\mc{C}\leftarrow\mc{D}}$?

::::

::::{admonition} Solution to&nbsp;{numref}`Exc:ChangeOfBasis:RelationMatricesCoB`
:class: solution, dropdown

The defining relation of  a change-of-coordinates matrix like   $P_{\mc{B}\leftarrow\mc{D}}$ is that for every vector $\vect{x}$ in $\R^n$ we have

$$
    P_{\mc{B}\leftarrow\mc{D}}[\vect{x}]_{\mc D} = [\vect{x}]_{\mc B}.
$$

As such, we see that for every vector $\vect{x}$   it also holds that

$$
  [\vect{x}]_{\mc B} = P_{\mc{B}\leftarrow\mc{C}}[\vect{x}]_{\mc C} =
   P_{\mc{B}\leftarrow\mc{C}} \left(P_{\mc{C}\leftarrow\mc{D}}[\vect{x}]_{\mc D}\right) =   
   \left(P_{\mc{B}\leftarrow\mc{C}} P_{\mc{C}\leftarrow\mc{D}}\right)[\vect{x}]_{\mc D}.
$$

From these identities it follows that

$$
   P_{\mc{B}\leftarrow\mc{D}} = P_{\mc{B}\leftarrow\mc{C}} P_{\mc{C}\leftarrow\mc{D}}.
$$

Note how nicely the notation for change-of-coordinates matrices comes out here.

::::

With the chosen notation for the change-of-coordinates matrix, the transformation formula for the matrices of a linear transformation with respect to different bases
becomes very natural as well. As is stated in the next theorem.

::::{prf:theorem}
:label: Thm:ChangeOfBasis:MatrixChangeGeneralBasis

Suppose $\mc{B}$ and $\mc{B}'$ are two bases of $\R^n$,
and $\mc{C}$ and $\mc{C}'$ are two bases of $\R^m$.
If $T:\R^n \to \R^m$ is a linear transformation, then the relation between the two
matrices $A = [T]_{\mc{C}\leftarrow \mc{B}}$ and $A' = [T]_{\mc{C}'\leftarrow \mc{B}'}$
is as follows

:::{math}
:label: Eq:ChangeOfBasis:MatrixChangeGeneralBasis

[T]_{\mc{C}'\leftarrow \mc{B}'} = P_{\mc{C}'\leftarrow\mc{C}}[T]_{\mc{C}\leftarrow \mc{B}} P_{\mc{B}\leftarrow\mc{B}'} =
\left(P_{\mc{C} \leftarrow\mc{C}'}\right)^{-1}[T]_{\mc{C}\leftarrow \mc{B}} P_{\mc{B}\leftarrow\mc{B}'}.

:::

::::

The following diagram, strikingly similar to the diagram in {prf:ref}`Prop:ChangeOfBasis:MatrixChangeStandardBasis`, illustrates what is going on.

$$
  \begin{array}{ccc}
      \R^n & \underrightarrow {\rule{3em}{0ex} T \rule{3em}{0ex}} & \R^m \\[2ex]
      \R^n_{\mc{B}} & \underrightarrow {\rule{3em}{0ex} A\rule{3em}{0ex}} & \R^m_{\mc{C}} \\[1ex]
      P_{\mc{B}\leftarrow\mc{B'}}\left  \uparrow \rule{0ex}{4em} \right. \rule{2em}{0ex}   &  & \rule{2em}{0ex} \left  \uparrow \rule{0ex}{4em} \right.P_{\mc{C}\leftarrow\mc{C'}}  \\
      \R^n_{\mc{B}' } & \underrightarrow {\rule{3em}{0ex} A' \rule{3em}{0ex}} & \R^m_{\mc{C}'} \\[1ex]
      [\vect{x}]_{\mc{B}'} & &  [T(\vect{x})]_{\mc{C}'}
  \end{array}
$$

::::{admonition} Proof of&nbsp;{prf:ref}`Thm:ChangeOfBasis:MatrixChangeGeneralBasis`
:class: tudproof

<!-- prettier-ignore -->
To find $[T(\vect{x})]_{\mc{C}'}$ when $ [\vect{x}]_{\mc{B}'}$ is given one can either

<ul>
<li>

<!-- prettier-ignore -->
Multiply by $A'= [T]_{\mc{C}'\leftarrow \mc{B}'} $

</li>
</ul>

or else

<ul>
<li>

Find the coordinates of $\vect{x}$ with respect to basis $\mc{B}$:

$$
    [\vect{x}]_{\mc{B}} = P_{\mc{B}\leftarrow\mc{B'}}  [\vect{x}]_{\mc{B}'}
$$

</li>
<li>
  
Multiply by  $A$ to find  $ [T(\vect{x})]_{\mc{C}}$

$$
[T(\vect{x})]_{\mc{C}} = A[\vect{x}]_{\mc{B}} = AP_{\mc{B}\leftarrow\mc{B'}}  [\vect{x}]_{\mc{B}'}
$$

</li>
<li>

Convert to coordinates with respect to basis $\mc{C}'$:

$$
    [T(\vect{x})]_{\mc{C}'} = P_{\mc{C}'\leftarrow\mc{C}}  [T(\vect{x})]_{\mc{C}}
    = \left( P_{\mc{C}\leftarrow\mc{C}'}\right)^{-1}AP_{\mc{B}\leftarrow\mc{B'}}  [\vect{x}]_{\mc{B}'}
$$

</li>
</ul>

Since we have that

$$
  [T(\vect{x})]_{\mc{C}'} = [T]_{\mc{C}'\leftarrow \mc{B}'}[\vect{x}]_{\mc{B}'} =
   \left( P_{\mc{C}\leftarrow\mc{C}'}\right)^{-1}AP_{\mc{B}\leftarrow\mc{B'}}  [\vect{x}]_{\mc{B}'}
$$

for each coordinate vector $[\vect{x}]_{\mc{B}'} $, that is, for each vector in $\R^n$, it follows that the two matrices

$$
   [T]_{\mc{C}'\leftarrow \mc{B}'} \quad \text{and} \quad
     \left( P_{\mc{C}\leftarrow\mc{C}'}\right)^{-1}AP_{\mc{B}\leftarrow\mc{B'}}
$$

must be equal.
::::

## Grasple Exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b19d38ef-60cf-4581-a4b2-9aa2efcf6f30?id=90868
:label: grasple_exercise_4_3_1
:dropdown:
:description: To find $[\vect{x}]_{\mathcal{B}}$ for some vector $\vect{x}$ and basis $\mathcal{B}$ in $\R^2$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3008a6aa-58ee-4182-8fd1-9d452ac3e9f0?id=90867
:label: grasple_exercise_4_3_2
:dropdown:
:description: One more like the previous.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/18d96cbf-6158-4800-9a10-3ec7f6e933f8?id=90885
:label: grasple_exercise_4_3_3
:dropdown:
:description: To find  $[\vect{v}_i]_{\mathcal{B}}$ for several vectors $\vect{v}_i$ in $\R^2$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/dfad4903-b2a8-4f67-979e-5651cf4072ec?id=90872
:label: grasple_exercise_4_3_4
:dropdown:
:description: Finding $[\vect{x}]_{\mathcal{B}}$ using a figure.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d6e53d94-578e-48fe-96b6-aca26f4eca1c?id=90870
:label: grasple_exercise_4_3_5
:dropdown:
:description: One more like the previous.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/75c6d18b-8a54-4592-97f4-edd77169cc10?id=90876
:label: grasple_exercise_4_3_6
:dropdown:
:description: Given $\vect{x} $  and some basis  $\mathcal{B}$ for a subspace in $\R^3$, to find $[\vect{x}]_{\mathcal{B}}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c45ea239-1e90-4d1f-ae08-323e595bd53a?id=104827
:label: grasple_exercise_4_3_7   
:dropdown:
:description: Expressing a vector $\vect{v} \in \R^3$  in  a basis $\mathcal{B} = \{\vect{b}_1,\vect{b}_2,\vect{b}_3\}$  (and vice versa).

::::




::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/39e1af19-0a32-456b-a414-20056e6b7f16?id=85157
:label: grasple_exercise_4_3_8
:dropdown:
:description: Expressing a vector $\vect{v} \in \R^3$  in  a basis $\mathcal{B} = \{\vect{b}_1,\vect{b}_2,\vect{b}_3\}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b03d9983-3ef2-4d45-82b3-6c1762510561?id=90875
:label: grasple_exercise_4_3_9
:dropdown:
:description: To explain the relation between $\vect{x}$  and $[\vect{x}]_{\mathcal{B}}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/784bba91-a0be-4076-9918-63b8ab2fbc49?id=90881
:label: grasple_exercise_4_3_10
:dropdown:
:description: To find out how coordinates change when a basis is reordered.
::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d8894445-4426-4694-8500-229cd47a5288?id=85165
:label: grasple_exercise_4_3_11
:dropdown:
:description: To commute between  $[\vect{v}]_{\mathcal{B}}$  and $[\vect{v}]_{\mathcal{C}}$  in $\R^2$.  

::::

The remaining exercises are about matrix representations of linear transformations.

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2de2a3b5-1d3f-4e79-9421-393d59b9dc87?id=93047
:label: grasple_exercise_4_3_12
:dropdown:
:description:  To transform from $[T]_{\mathcal{E}}$  to  $[T]_{\mathcal{B}}$  for $T$ from $\R^2$ to $\R^2$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/01e5c371-0139-458c-8f0a-25f35bc03fcb?id=93053
:label: grasple_exercise_4_3_13
:dropdown:
:description: To transform from $[T]_{\mathcal{E}}$  to  $[T]_{\mathcal{B}_2\leftarrow\mathcal{B}_1}$ for $T$ from $\R^2$ to $\R^3$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/dd1af96d-34d7-407e-9877-c1e8b6495e6f?id=85167
:label: grasple_exercise_4_3_14
:dropdown:
:description: To compute $[T]_{\mathcal{C}\leftarrow\mathcal{B}}$  for $T$ from $\R^2$ to $\R^2$  with respect to several bases. 

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/933f3e07-36b6-4db5-a47d-91e276185269?id=85159
:label: grasple_exercise_4_3_15
:dropdown:
:description: To compute $[T]_{\mathcal{C}\leftarrow\mathcal{B}}$, for $T$ from $\R^2$ to $\R^2$.  with respect to several bases. 

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7985ac3f-c432-4b48-9ef1-8ce0914b0f97?id=85162
:label: grasple_exercise_4_3_16
:dropdown:
:description: Like the previous, for a linear transformation $T$ from $\R^3$ to $\R^2$.

::::
