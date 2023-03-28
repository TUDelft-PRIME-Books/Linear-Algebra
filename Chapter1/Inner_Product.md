(Sec:DotProduct)=
# Dot product

In this section we will consider other (geometric) properties of vectors, like the _length_ of a vector and the _angle_ between two vectors. When the angle between two vectors is equal to $\frac12\pi$, two vectors are _perpendicular_, which is also known as _orthogonal_. These properties can all be expressed using a new operator: the _inner product_ or _dot product_.

We will start by considering vectors in $\mathbb{R}^2$ and $\mathbb{R}^3$. The translation of the concepts to the general space $\mathbb{R}^n$ will then become more or less immediate.

(Subsec:InnerProduct:Length_and_perpendicular)=
## Length and perpendicularity in $\mathbb{R}^2$ and $\mathbb{R}^3$

The length of a vector

$$
\mathbf{v}=\begin{bmatrix}
a_{1}\\a_{2}
\end{bmatrix}
$$

in the plane, which we denote by $\norm{\mathbf{v}}$, can be computed using the Pythagorean theorem:

:::{math}
:label: Eq:InnerProduct:length-2D

\norm{\mathbf{v}} = \sqrt{a_1^2+a_2^2}
:::

:::{figure} Images/Fig-InnerProduct-Length-2D.svg
:name: Fig:InnerProduct:Length-2D

The length of a vector via Pythagoras' Theorem
:::

:::{applet}
:url: dot_product/inner_product_length
:fig: Images/Fig-InnerProduct-length-3D.svg
:name: Fig:InnerProduct:length-3D

The length of a vector via Pythagoras' Theorem
:::

Using this theorem twice we find a similar formula for the length of a vector

$$
\mathbf{v}=\begin{bmatrix} a_{1}\\a_{2}\\a_{3}\end{bmatrix}
 $$

in $\mathbb{R}^3$. Look at {numref}`Figure %s <Fig:InnerProduct:length-3D>`. There are two right triangles: $\Delta OPQ$ where $\angle OPQ$ is right, and
$\Delta OQA$ where $\angle OQA$ is right.

From

$$
  OQ^2 = OP^2 + PQ^2 = a_1^2 + a_2^2,
$$

where for two points $A$ and $P$, by $AB$ we denote the length of the vector $\overrightarrow{AB}$,
and

$$

  OA^2 =  OQ^2+QA^2 = a_1^2 + a_2^2+a_3^2
$$

we find that

:::{math}
:label: Eq:InnerProduct:length-3D

\norm{\mathbf{v}}= OA = \sqrt{a_1^2 + a_2^2+a_3^2}
:::

:::{figure} Images/Fig-InnerProduct-perp-non-perp.svg
:name: Fig:InnerProduct:perp-non-perp

Perpendicular versus non-perpendicular
:::

Let us now turn our attention to another important geometric concept, namely that of
perpendicularity. It is clear from {numref}`Figure %s <Fig:InnerProduct:perp-non-perp>` that the vectors $\begin{bmatrix}2\\3\end{bmatrix}$ and $\begin{bmatrix}-3\\2\end{bmatrix}$ are
perpendicular, whereas the vectors $\begin{bmatrix}2\\3\end{bmatrix}$ and $\begin{bmatrix}-1\\3\end{bmatrix}$ are not. But how does this work in $\mathbb{R}^3$?
Well, look at {numref}`Figure %s <Fig:InnerProduct:diagonal-parallelogram>`:

:::{figure} Images/Fig-InnerProduct-diagonal-parallelogram.svg
:name: Fig:InnerProduct:diagonal-parallelogram

Diagonal of a rectangle versus diagonal of a parallelogram
:::


In both pictures, let $A$ be the end point of vector $\mathbf{v}$, $B$ the end point of vector $\mathbf{w}$, and $C$ the end point of vector $\mathbf{v}+\mathbf{w}$. The diagonals are

$$

  \overrightarrow{OC} = \mathbf{v}+\mathbf{w} \quad \text{and} \quad \overrightarrow{BA} = \mathbf{v}-\mathbf{w}
$$

In the left picture of {numref}`Figure %s <Fig:InnerProduct:diagonal-parallelogram>` the vectors $\mathbf{v}$ and $\mathbf{w}$ are perpendicular, so the parallelogram $OACB$ is a rectangle. It follows that
the two diagonals have the same length:

:::{math}
:label: EqualDiagonals

\norm{\mathbf{v}+\mathbf{w}} = \norm{\mathbf{v}-\mathbf{w}}.
:::

In the picture on the left the vectors are not perpendicular and

$$

  \norm{\mathbf{v}+\mathbf{w}} \neq \norm{\mathbf{v}-\mathbf{w}}.
$$

The picture suggests that we are talking about two (non-zero) vectors in the plane, i.e., in $\mathbb{R}^2$. However, two vectors in $\mathbb{R}^3$ form a parallelogram as well, which becomes a rectangle if and only if the vectors are perpendicular. We introduce a notation for this: if $ \mathbf{v}$ and $\mathbf{w}$ are perpendicular, we write this as

:::{math}
:label: Eq:InnerProduct:Orthogonal

\mathbf{v} \perp \mathbf{w}
:::

Taking squares in Equation {eq}`EqualDiagonals`, we see that the following holds
both in $\mathbb{R}^2$ and in $\mathbb{R}^3$:

$$
 \mathbf{v} \perp \mathbf{w} \iff \norm{\mathbf{v}+\mathbf{w}}^2 = \norm{\mathbf{v}-\mathbf{w}}^2.
$$


If we write this out for two arbitrary vectors $\mathbf{v}=\begin{bmatrix} a_{1}\\a_{2}\end{bmatrix},\mathbf{w}=\begin{bmatrix} b_{1}\\b_{2}\end{bmatrix}$ in $\mathbb{R}^2$ 
we get the following:

$$
 \begin{array}{rcl} \mathbf{v} \perp \mathbf{w}  &\iff
        &\norm{\mathbf{v}+\mathbf{w}}^2 = \norm{\mathbf{v}-\mathbf{w}}^2\\
        &\iff      &(a_1+b_1)^2 + (a_2+b_2)^2 = (a_1-b_1)^2 + (a_2-b_2)^2\\
        &\iff      &a_1^2+2a_1b_1 + b_1^2 + a_2^2+2a_2b_2 + b_2^2 = a_1^2 -2a_1b_1+b_1^2+ a_2^2 -2a_2b_2+b_2^2\\
        &\iff      &4(a_1b_1 +a_2b_2)=0 \\
        &\iff      &a_1b_1 +a_2b_2=0.
 \end{array}
 $$

Likewise, for vectors $\mathbf{v}=\begin{bmatrix} a_{1}\\a_{2}\\a_{3}\end{bmatrix},\,\mathbf{w}=\begin{bmatrix} b_{1}\\b_{2}\\b_{3}\end{bmatrix}$ in $\mathbb{R}^3$:

:::{math}
:label: Eq:InnerProduct:perp-in-3D

\mathbf{v} \perp \mathbf{w}   \iff  a_1b_1 +a_2b_2+a_3b_3=0.
:::

The derivation is completely analogous to the one above, only now we have one term extra.
So to check 'algebraically' whether two vectors are perpendicular we just have to compute $a_1b_1 +a_2b_2\, (\,+\,a_3b_3\,)$
and see whether this is equal to 0.

This expression is called the _inner product_ (or _dot product_) of the vectors $\mathbf{v}$ and $\mathbf{w}$. We denote it by $\mathbf{v}\ip\mathbf{w}$.
Note that the dot product of a general vector $\mathbf{v}=\begin{bmatrix} a_{1}\\a_{2}\\a_{3}\end{bmatrix}$ in $\mathbb{R}^3$ with itself gives

$$

   \mathbf{v}\ip\mathbf{v} = a_1^2+a_2^2+a_3^2 = \norm{\mathbf{v}}^2,
$$

so the length of a vector can be expressed as follows using the dot product

:::{math}
:label: Eq:NormViaDotproduct

\norm{\mathbf{v}} = \sqrt{\mathbf{v}\ip\mathbf{v}\,}.
:::

%\todo{Exercise enlightening the connection $\norm{\vect{v}\pm\vect{w}}$ versus %perpendicularity}

Using the dot product the concepts length and perpendicular easily carry over to any $\mathbb{R}^n$, $n \geq 4$. Let's do it one by one, starting by generalizing the dot product in the next subsection.

(Subsec:Dot_product:InnerProduct_in_Rn)=

## Dot product in $\mathbb{R}^n$

::::{prf:definition}
:label: Dfn:InnerProduct:DotProduct



The *dot product* (or *inner product*) of two vectors
$\mathbf{v}=\begin{bmatrix}a_{1}\\a_{2}\\ \vdots\\a_{n}\end{bmatrix}$ and
$\mathbf{w}=\begin{bmatrix}b_{1}\\b_{2}\\ \vdots\\b_{n}\end{bmatrix}$ in $\mathbb{R}^n$ is defined as

:::{math}
:label: Eq:InnerProduct:DotProduct

\mathbf{v}\ip\mathbf{w} = a_1b_1 +a_2b_2+ \ldots + a_nb_n.
:::

::::

:::{prf:example}
:label: Ex:InnerProduct:DotProdTwoVectors

The dot product of the two vectors

$$
  \mathbf{v_1}=\begin{bmatrix} 5\\3\\4\\-2\end{bmatrix}
  \quad \text{and}\quad
  \mathbf{v_2}=\begin{bmatrix} 2\\3\\0\\1\end{bmatrix}
$$

is given by

$$
  \mathbf{v_1}\ip\mathbf{v_2} =
  5\cdot2 + 3\cdot3 +4\cdot0 + (-2)\cdot1
  = 17
$$

And the dot product of the two vectors

$$
  \mathbf{v_1}=\begin{bmatrix} 5\\3\\4\\-2\end{bmatrix}
  \quad \text{and}\quad
  \mathbf{v_3}=\begin{bmatrix} -4\\3\\2\end{bmatrix}
$$

is not defined.  In fact, the dot product of a  vector $\mathbf{v}$ in $\mathbb{R}^m$ and a  vector $\mathbf{w}$ in $\mathbb{R}^n$ is only defined if $m = n$.

:::

We state the characteristic rules of the dot product in $\mathbb{R}^n$, which in the sequel we will use time and again, in the following
proposition.

:::{prf:proposition}
:label: Prop:RulesInnerProduct

The following  properties   hold for any vectors $\mathbf{v},\mathbf{v_1},\mathbf{v_2},\mathbf{v_3}$ in $\mathbb{R}^n$ and scalars $c \in \mathbb{R}$:


  i. $\mathbf{v_1}\ip\mathbf{v_2} = \mathbf{v_2}\ip\mathbf{v_1}$.

  ii. $(c\mathbf{v_1})\ip\mathbf{v_2} = c(\mathbf{v_1}\ip\mathbf{v_2}) = \mathbf{v_1}\ip(c \mathbf{v_2})$.

  iii. $(\mathbf{v_1}+\mathbf{v_2})\ip\mathbf{v_3} = \mathbf{v_1}\ip\mathbf{v_3}+\mathbf{v_2}\ip\mathbf{v_3}$.

  iv.  $\mathbf{v}\ip\mathbf{v} \geq 0$, and  $\mathbf{v}\ip\mathbf{v} = 0 \iff \mathbf{v} = \mathbf{0}$.
:::

:::{prf:proof}
:class: dropdown

The first three properties follow from the corresponding properties of real numbers. For instance, for the first rule we simply use that  $xy = yx$ holds for the product of real numbers.

i. Let

$$
\mathbf{v_1}=\begin{bmatrix} a_1\\a_2\\ \vdots\\ a_n\end{bmatrix}
  \quad \text{and}\quad
  \mathbf{v}_2=\begin{bmatrix}  b_1 \\ b_2 \\ \vdots \\ b_n \end{bmatrix}
$$

be two arbitrary vectors in $\mathbb{R}^n$. Then

$$\begin{eqnarray*}
     \mathbf{v_1}\ip\mathbf{v_2} &=&
            \begin{bmatrix}a_{1}\\a_{2}\\ \vdots\\a_{n}\end{bmatrix}\ip\begin{bmatrix}b_{1}\\b_{2}\\ \vdots\\b_{n}\end{bmatrix}
            = a_1b_1 +a_2b_2+ \ldots + a_nb_n  \\
            &=& b_1a_1 +b_2a_2+ \ldots + b_na_n =
               \begin{bmatrix}b_{1}\\b_{2}\\ \vdots\\b_{n}\end{bmatrix}\ip\begin{bmatrix}a_{1}\\a_{2}\\ \vdots\\a_{n}\end{bmatrix} =
                \mathbf{v_2}\ip\mathbf{v_1}.
\end{eqnarray*}
$$

ii. Taking  $\mathbf{v_1}$, $\mathbf{v_2}$ as before

$$\begin{eqnarray*}
            (c\mathbf{v_1})\ip\mathbf{v_2} &=&  \begin{bmatrix}ca_{1}\\ca_{2}\\ \vdots\\ca_{n}\end{bmatrix}\ip\begin{bmatrix}b_{1}\\b_{2}\\                                 \vdots\\b_{n}\end{bmatrix}\\
            &=& (ca_1b_1) + (ca_2b_2)+ \ldots + (ca_n)b_n \\
            &=& c\,(a_1b_1 +a_2b_2+ \ldots + a_nb_n) = c\, (\mathbf{v_1}\ip\mathbf{v_2})
\end{eqnarray*}$$

iii. Is proved in the same way as (ii).

iv.  $\mathbf{v}\ip\mathbf{v} = a_1a_1 +a_2a_2+ \ldots + a_na_n = a_1^2+a_2^2 + \ldots + a_n^2$ is the sum of squares of real numbers, so it is nonnegative. It only becomes 0 if all the squares are 0, which only happens if each entry $a_i$ is equal to zero, that is, if $\mathbf{v} = \mathbf{0}$.
:::

:::{exercise}
:label: Exc:InnerProduct:CheckPropInnerProd

Prove property (iii).
:::

:::{exercise}
:label: Exc:InnerProduct:(v-w)(v+w)

Prove the identity

$$
  (\mathbf{v_1}+\mathbf{v_2})\ip(\mathbf{v_1}-\mathbf{v_2}) = \mathbf{v_1}\ip\mathbf{v_1}-\mathbf{v_2}\ip\mathbf{v_2}.
$$

%Explain why it is called the \emph{parallelogram rule}.

:::

:::{exercise}
:label: Exc:InnerProduct:PargramRule

Prove the identity

$$

  \norm{\mathbf{v_1}+\mathbf{v_2}}^2 + \norm{\mathbf{v_1}-\mathbf{v_2}}^2   = 2 (\norm{\mathbf{v_1}}^2 + \norm{\mathbf{v_2}}^2),
$$

and explain why it is called the *parallelogram rule*.

:::

(Subsec:InnerProduct:Orthogonality)=
## Orthogonality

In $\mathbb{R}^2$ and $\mathbb{R}^3$ the dot product gives an easy way to check whether two vectors are perpendicular:

$$

  \mathbf{v}\perp\mathbf{w} \iff \mathbf{v}\ip\mathbf{w} = 0.
$$

We use this identity to define the concept of perpendicularity in $\mathbb{R}^n$. It seems a bit 'academic', but in this more general setting the term _orthogonal_ is used.

:::{prf:definition}
:label: Dfn:InnerProduct:Orthogonality



Two vectors $\mathbf{v}$  and $\mathbf{w}$ in $\mathbb{R}^n$ are called *orthogonal* if  $\mathbf{v}\ip\mathbf{w} = 0$. As before, we denote this by $\mathbf{v}\perp\mathbf{w}$.

:::

:::{prf:example}
:label: Ex:InnerProduct:CheckVectorsOrthogonal

Let $\mathbf{u} = \begin{bmatrix} 1\\2\\-1\\-1\end{bmatrix}$,  $\mathbf{v} = \begin{bmatrix} 3\\-1\\2\\-1\end{bmatrix}$,
$\mathbf{w} = \begin{bmatrix} 2\\2\\-1\\2\end{bmatrix}$. \\
We compute

$$

  \mathbf{u}\ip\mathbf{v} = 3-2-2+1 = 0,
$$


$$

  \mathbf{u}\ip\mathbf{w} =  2+4+1-2 = 5,
$$


$$

 \mathbf{v}\ip\mathbf{w} = 6 - 2 - 2 - 2 = 0,
$$

and conclude:  $\mathbf{u}$ and $\mathbf{v}$ are orthogonal, $\mathbf{u}$ and $\mathbf{w}$ are not orthogonal, $\mathbf{v}$ and $\mathbf{w}$  are orthogonal.

In $\mathbb{R}^2$, two nonzero vectors that are orthogonal to the same nonzero vector $\mathbf{v}$ are automatically multiples of each other (i.e. have either the same or the opposite direction). In $\mathbb{R}^n$ with  $n \geq 3$ this no longer holds. In this example both  vectors $\mathbf{u}$ and  $\mathbf{w}$ are orthogonal to the vector $\mathbf{v}$, but $\mathbf{u} \neq c\mathbf{w}$.

:::

By definition the zero vector is orthogonal to any vector, since $\mathbf{0}\ip\mathbf{v} = 0$.
Moreover, the zero vector is the _only_ vector that is orthogonal to itself:

:::{prf:proposition}
:label: Prop:InnerProduct:vDotv=0Impliesv=0



Suppose  $\mathbf{v} \in \mathbb{R}^n$.  Then  $\mathbf{v}\perp\mathbf{v} \iff \mathbf{v} = \mathbf{0}$.

:::

:::{prf:proof}



By definition

$$

 \mathbf{v}\perp\mathbf{v} \iff \mathbf{v}\ip\mathbf{v}=0
$$

In {prf:ref}`Prop:RulesInnerProduct` (iv) we already showed that the last equality only holds for $\mathbf{v} = \mathbf{0}$.

:::

The fact that the zero vector is orthogonal to _any_ vector is an immediate consequence of the definition, but it
may seem counter intuitive to you. The following example illustrates a situation where this orthogonality leads to a much nicer outcome.

::::{prf:example}
:label: Ex:PerpendicularLine

Let $\mathbf{n}$ be any nonzero vector in the plane.
The set of vectors that are orthogonal to $\mathbf{n}$ all lie on a line through the origin. (See {numref}` Figure %s <Fig:InnerProduct:PerpendicularLine>`.)  If we agree that  $\mathbf{0}\perp\mathbf{n}$, it will be the whole line.
The vector $\mathbf{n}$ is often said to be  a *normal* vector to the line.




:::{figure} Images/Fig-InnerProduct-PerpendicularLine.svg
:name: Fig:InnerProduct:PerpendicularLine

Vectors orthogonal to a non-zero vector $\mathbf{n}$ in the plane
:::


::::

We conclude this subsection with another concept that we will come across later in a much more general context. Informally, it is the (orthogonal) projection of a vector onto another vector. More precisely, it is the orthogonal projection of a vector $\mathbf{w}$ onto the line $L$ generated by the nonzero vector $\mathbf{v}$, by which we mean $L= \{ c\mathbf{v}: c \in \mathbb{R}\}$.

See {numref}`Figure %s <Fig:InnerProduct:ProjectionVectorLine>`.

:::{prf:definition}
:label: Dfn:InnerProduct:OrthoProjectionOntoVector

The *orthogonal projection of a vector $\mathbf{w}$ onto the nonzero vector $\mathbf{v}$* is the vector  $\mathbf{\hat{w}} = c\mathbf{v} $ for which

$$

  (\mathbf{w} - \mathbf{\hat{w}}) \perp \mathbf{v}.
$$

Another notation for this vector:

$$

  \mathbf{\hat{w}} = \text{proj}_{\mathbf{v}}(\mathbf{w}).
$$


:::

:::{figure} Images/Fig-InnerProduct-ProjectionVectorLine.svg
:name: Fig:InnerProduct:ProjectionVectorLine

Projection of a vector $\mathbf{w}$ onto a non-zero vector $\mathbf{v}$
:::

:::{prf:proposition}
:label: Prop:InnerProduct:UniqueProjection



In  the definition above the vector $\mathbf{\hat{w}}$ with these properties is unique
and it is given by

$$

  \text{proj}_{\mathbf{v}}(\mathbf{w}) = \mathbf{\hat{w}} = \frac{\mathbf{w}\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}} \mathbf{v}.
$$


:::

:::{prf:proof}



With the rules of the dot product the vector $\mathbf{w}$ is easily constructed:
Starting from

$$

   \mathbf{\hat{w}} = t\mathbf{v}, \text{ for some } t\in\mathbb{R}
$$

and

$$

  (\mathbf{w} - \mathbf{\hat{w}}) \perp \mathbf{v}
$$

it follows that we must have

$$

   (\mathbf{w} - t\mathbf{v}) \ip \mathbf{v} =
   \mathbf{w}\ip \mathbf{v} - t \,(\mathbf{v}\ip \mathbf{v}) =  0
$$

so that  $t$ is uniquely given by

$$

  t = \frac{\mathbf{w}\ip \mathbf{v}}{\mathbf{v}\ip \mathbf{v}}
$$

and indeed  $\mathbf{\hat{w}}$ must be as stated.

:::

:::{prf:example}
:label: Ex:InnerProduct:OrthoProjectionOntoVector



We compute the orthogonal projection of the vector

$$

 \mathbf{w} = \begin{bmatrix} 2\\ -4 \\ -1 \\ -5\end{bmatrix}
$$

onto the vector

$$

   \mathbf{v} =  \begin{bmatrix} 1 \\1\\1\\1\end{bmatrix}.
$$

As follows

$$

 \mathbf{\hat{w}}  = \text{proj}_{\mathbf{v}}(\mathbf{w}) =  \frac{\mathbf{w}\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}} \mathbf{v} = \frac{-8}{4}\begin{bmatrix} 1 \\1\\1\\1\end{bmatrix} =
 \begin{bmatrix} -2\\-2\\-2\\-2\end{bmatrix}.
$$

We verify the orthogonality:

$$

  (\mathbf{w} - \mathbf{\hat{w}} )\ip \mathbf{v} = \begin{bmatrix} 4 \\-2\\1\\-3\end{bmatrix} \ip \begin{bmatrix} 1 \\1\\1\\1\end{bmatrix} = 4-2+1-3 = 0,
$$

so indeed

$$

  (\mathbf{w} - \mathbf{\hat{w}} )\perp \mathbf{v},
$$

as required.

:::

:::{exercise}
:label: Exc:InnerProduct:FindProjectionOntoLine



Find the projection $\mathbf{w} = \text{proj}_{\mathbf{v}}(\mathbf{u})$  of the vector

$$

  \mathbf{u} = \begin{bmatrix} 11\\ 8 \\ -5\end{bmatrix}  \text{ onto the vector }
  \mathbf{v} = \begin{bmatrix} 1\\2 \\ -3\end{bmatrix},
$$

and show that

$$

  \norm{\mathbf{w}} \leq \norm{\mathbf{u}}.
$$

% (Answer: $\vect{w} =  \begin{bmatrix} 3\\6 \\ -9\end{bmatrix}$.\,)

:::

:::{exercise}
:label: Exc:InnerProduct:SameProjectionThenWhat


Suppose $\text{proj}_{\mathbf{v}}(\mathbf{w_1}) = \text{proj}_{\mathbf{v}}(\mathbf{w_2}) $,
for three nonzero vectors $\mathbf{v}, \,\mathbf{w_1},\,\mathbf{w_2}$ in $\mathbb{R}^n$.
What does this say about the relative positions of the three vectors?

Verify your statement for the following three vectors

$$

 \mathbf{v} = \begin{bmatrix} 1\\ 1 \\ -2 \\ -3\end{bmatrix}, \quad
 \mathbf{w_1} = \begin{bmatrix} 6\\ 4 \\ -7 \\ -7\end{bmatrix}, \quad
 \mathbf{w_2} = \begin{bmatrix} 5\\ 6 \\ -2 \\ -10\end{bmatrix}.
$$


:::

(Subsec:InnerProduct:Norm_in_Rn)=

## Norm in $\mathbb{R}^n$

The length of a vector in the plane can be computed using the dot product: for
$\mathbf{v}=\begin{bmatrix}a_{1}\\a_{2}\end{bmatrix}$ in $\mathbb{R}^2$ we have seen that

$$

  \norm{\mathbf{v}} = \sqrt{a_1^2 + a_2^2} = \sqrt{\mathbf{v}\ip\mathbf{v}}.
  $$

The identity $\norm{\mathbf{v}}  = \sqrt{\mathbf{v}\ip\mathbf{v}}$ also holds in $\mathbb{R}^3$.

It seems natural to extend the concept to $\mathbb{R}^n$. Again, for this more general space a new word is introduced:

:::{prf:definition}
:label: Dfn:InnerProduct:NormOfVector



The *norm* of a vector $\mathbf{v}$ in $\mathbb{R}^n$, denoted by $\norm{\mathbf{v}}$,  is defined by

$$

 \norm{\mathbf{v}} = \sqrt{\mathbf{v}\ip\mathbf{v}\,}.
$$


:::

Expressed in the entries of $\mathbf{v}$ this yields

$$

  \norm{\mathbf{v}} = \sqrt{a_1^2+ a_2^2 + \ldots +a_n^2\,}\,,
$$

so for vectors in $\mathbb{R}^2$ and $\mathbb{R}^3$ the norm of a vector is just the length of the vector.

As we might expect the norm has many properties in common with length:

::::{prf:proposition}
:label: Item:Prop:InnerProduct:PropertiesNorm

For any $\mathbf{v}, \,\mathbf{w} \in \mathbb{R}^{n}$ and all $c \in \mathbb{R}$ the following holds:

i. $\norm{\mathbf{v}}\geq 0$;

ii. Scaling property:
:::{math}
:label: Item:Prop:InnerProduct:Scaling

\norm{c\mathbf{v}} = |c|\norm{\mathbf{v}}.
:::

iii. Triangle Inequality:

:::{math}
:label: Item:Prop:InnerProduct:TriangleInequality

\norm{\mathbf{v}+\mathbf{w}} \leq \norm{\mathbf{v}}+\norm{\mathbf{w}}.
:::

::::

The first two of these properties are very easy to prove. The proof of the triangle inequality we postpone until the end of the section.  {numref}`Figure %s <Fig:InnerProduct:TriangleInequality>` explains the name.

:::{figure} Images/Fig-InnerProduct-TriangleInequality.svg
:name: Fig:InnerProduct:TriangleInequality

The Triangle Inequality
:::

:::{prf:example}
:label: Ex:InnerProduct:NormsofTwoVectors

We compute the norms of the vectors

$$
\mathbf{v} = \begin{bmatrix} 1 \\ -2 \\ 3 \\ -1 \end{bmatrix} \quad \text{and} \quad  -2\mathbf{v} = \begin{bmatrix} -2 \\ 4 \\ -6 \\ 2 \end{bmatrix}. $$

As follows:

$$

  \norm{\mathbf{v}} = \sqrt{1^2 + (-2)^2 +  3^2 + (-1)^2\,} = \sqrt{15}.
$$

and

$$
\norm{-2\mathbf{v}} =
   \sqrt{(-2)^2 + 4^2 + (-6)^2 + 2^2\,} = \sqrt{60}
     = 2\sqrt{15}.
$$

The last norm can also be found via

$$

  \norm{-2\mathbf{v}} = |-2|\cdot\norm{\mathbf{v}} = 2 \sqrt{15}.
$$


:::

With the tools so far we can define a notion that comes in handy later:

:::{prf:definition}
:label: Dfn:InnerProduct:unit vector



A *unit vector* is a vector of norm 1.

Moreover, for any nonzero vector $\mathbf{v}$,
the vector

$$

  \mathbf{u} = \frac{\mathbf{v}}{\norm{\mathbf{v}}}
$$

is called the *unit vector in the direction of $\mathbf{v}$*.

:::

:::{prf:proposition}
:label: Prop:InnerProduct:unit vector for v



For a nonzero vector $\mathbf{v}$

$$

   \frac{\mathbf{v}}{\norm{\mathbf{v}}}
$$

is the unique vector $\mathbf{u}$ of norm 1
such that

$$

   \mathbf{u} = k\mathbf{v}, \text{ for some } k > 0.
$$


:::

:::{prf:proof}



Assume that $\mathbf{v} \neq \mathbf{0}$.
For  $\mathbf{u} = k\mathbf{v}$, with $\norm{\mathbf{u}} = 1$ and $k > 0$ to hold, we must have

$$

  \norm{\mathbf{u}} = \norm{k\mathbf{v}} = |k|\norm{\mathbf{v}} = k\norm{\mathbf{v}} = 1.
$$

We see that

$$

  k = \dfrac{1}{\norm{\mathbf{v}}}
$$

and consequently

$$

 \mathbf{u} = \dfrac{1}{k}\mathbf{v} = \frac{\mathbf{v}}{\norm{\mathbf{v}}}.
$$


:::

:::{prf:example}
:label: Ex:InnerProduct:UnitVector



We compute the unit vector $\mathbf{u}$  in the direction of the vector $\mathbf{v} = \begin{bmatrix}1 \\ 2 \\ 4 \\ -2 \end{bmatrix}$  in $\mathbb{R}^4$.   
As follows:

$$

\norm{\mathbf{v}} = \sqrt{1^2+2^2+4^2+(-2)^2} = \sqrt{25} = 5 \quad \Longrightarrow\quad
\mathbf{u} = \dfrac{1}{5} \begin{bmatrix}1 \\ 2 \\ 4 \\ -2 \end{bmatrix} = \begin{bmatrix}1/5 \\ 2/5 \\ 4/5 \\ -2/5 \end{bmatrix}.
$$


:::

%\begin{figure}
%\begin{center}
%\includegraphics{Images/Fig-InnerProduct-TriangleInequality.pdf}
%\caption{The Triangle Inequality}
%\label{Fig:InnerProduct:TriangleInequality}
%\end{center}
%\end{figure}

Interestingly, Pythagoras' theorem  also holds in $\mathbb{R}^n$.

:::{prf:theorem}
:label: Thm:InnerProduct:PythagorasInRn



For any two vectors  $\mathbf{v}$  and $\mathbf{w}$  in $\mathbb{R}^n$ we have

$$

 \norm{\mathbf{v}+\mathbf{w}}^2 = \norm{\mathbf{v}}^2 + \norm{\mathbf{w}}^2
    \iff \mathbf{v} \perp \mathbf{w}.
$$


:::

:::{prf:proof}



This follows quite straightforwardly from the properties of the dot product:

Let us start from the identity on the left  and work our way to the conclusion on the right, making sure that each step is reversible.
Note that from the definition of the norm it follows immediately that $\norm{\mathbf{v}}^2 = \mathbf{v}\ip\mathbf{v}$.

$$
\begin{array}{cl}
   &\norm{\mathbf{v}+\mathbf{w}}^2 = \norm{\mathbf{v}}^2 + \norm{\mathbf{w}}^2 \\
   \iff &(\mathbf{v}+\mathbf{w})\ip(\mathbf{v}+\mathbf{w}) = \mathbf{v}\ip\mathbf{v} + \mathbf{w}\ip\mathbf{w} \\
  \iff&\mathbf{v}\ip\mathbf{v} + \mathbf{v}\ip\mathbf{w}+\mathbf{w}\ip\mathbf{v}+ \mathbf{w}\ip\mathbf{w} = \mathbf{v}\ip\mathbf{v} + \mathbf{w}\ip\mathbf{w}.
  \end{array}
$$


Next we subtract $\mathbf{v}\ip\mathbf{v} + \mathbf{w}\ip\mathbf{w}$ from both sides. Thus the last identity is equivalent to

$$

\begin{array}{rcl}
 \mathbf{v}\ip\mathbf{w}+\mathbf{w}\ip\mathbf{v} = 0
  &\iff& 2\mathbf{v}\ip\mathbf{w} = 0\\
  &\iff& \mathbf{v}\ip\mathbf{w}= 0\\
  &\iff& \mathbf{v}\perp\mathbf{w}.
  \end{array}
$$


:::

:::{exercise}
:label: Ex:InnerProduct:Pythagoras_in_R^4



We verify the equality for the vectors $\mathbf{v} = \begin{bmatrix} 2 \\ -3\\ 3 \\ 1 \end{bmatrix}$
and $\mathbf{w} = \begin{bmatrix} 2 \\ 4 \\ 1 \\ 5 \end{bmatrix}$ in $\mathbb{R}^4$:

First of all

$$

  \mathbf{v} \ip \mathbf{w}  = 4 - 12 + 3 + 5  = 0,
$$

so  $\mathbf{v}\perp \mathbf{w}$, and second

$$

  \norm{\mathbf{v}} = \sqrt{2^2 + (-3)^2 + 3^2 + 1^2} = \sqrt{23}, \quad
  \norm{\mathbf{w}} = \sqrt{2^2 + 4^2 + 1^2 + 5^2} = \sqrt{46}
$$

Furthermore

$$

 \mathbf{v}+\mathbf{w} = \begin{bmatrix} 4 \\ 1 \\ 4 \\ 6 \end{bmatrix} \Longrightarrow \norm{\mathbf{v}+\mathbf{w}} = \sqrt{4^2+1^2+4^2+6^2} = \sqrt{69}

$$

and we see that indeed

$$

 \norm{\mathbf{v}+\mathbf{w}}^2 = 69 = 23 + 46 =  \norm{\mathbf{v}}^2+\norm{\mathbf{w}}^2.
$$


:::

One of the most basic properties, also one with a wide range of applications, is the so-called Cauchy-Schwarz Inequality.

:::{prf:theorem}
:label: Thm:InnerProduct:Cauchy-Schwarz



For any two vectors in $\mathbb{R}^n$

$$

    |\mathbf{v}\ip\mathbf{w}| \leq  \norm{\mathbf{v}}\,\norm{\mathbf{w}}.
$$


:::

:::{prf:proof}



There are many ways to prove the Cauchy-Schwarz inequality.  There is even a whole book devoted to it: "Cauchy Schwarz master class" by J.M.\, Steele.

The following proof is based on orthogonal projection and Pythagoras' Theorem.

If
  $\mathbf{v} = \mathbf{0}$, the zero vector, then the inequality obviously holds;  in fact it becomes an equality:

$$

  \mathbf{v} = \mathbf{0} \Longrightarrow  \norm{\mathbf{v}} = 0
  \Longrightarrow \norm{\mathbf{v}}\cdot\norm{\mathbf{w}} = 0
$$

and also

$$

 \mathbf{v} = \mathbf{0} \Longrightarrow  \mathbf{v}\ip \mathbf{w} = 0
  \Longrightarrow  |\mathbf{v}\ip \mathbf{w}| = 0.
$$


So now suppose $\mathbf{v} \neq \mathbf{0}$.

Let

$$

  \mathbf{\hat{w}} = \dfrac{\mathbf{w}\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}}\,\mathbf{v}
$$

be the projection of $\mathbf{w}$ onto $\mathbf{v}$.
Then we can apply Pythagoras Theorem!

$$

 (\mathbf{w} - \mathbf{\hat{w}}) \perp  \mathbf{\hat{w}}  \Longrightarrow \norm{\mathbf{w} - \mathbf{\hat{w}}}^2 + \norm{ \mathbf{\hat{w}}}^2 =
 \norm{(\mathbf{w} - \mathbf{\hat{w}}) + \mathbf{\hat{w}}}^2 =
 \norm{\mathbf{w}}^2
$$

It follows that

$$

  \norm{ \mathbf{\hat{w}}}^2   = \norm{\mathbf{w}}^2 - \norm{\mathbf{w} - \mathbf{\hat{w}}}^2 \leq \norm{\mathbf{w}}^2
$$

and substitution of the expression for $\mathbf{\hat{w}}$ we arrive at

$$

   \left(\dfrac{\mathbf{w}\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}}\right)^2 \norm{\mathbf{v}}^2  =
   \dfrac{(\mathbf{w}\ip\mathbf{v})^2}{(\mathbf{v}\ip\mathbf{v})^2} \norm{\mathbf{v}}^2    \leq \norm{\mathbf{w}}^2.
$$

Using

$$

  \mathbf{v}\ip\mathbf{v} = \norm{\mathbf{v}}^2
$$

we conclude that indeed

$$

   (\mathbf{w}\ip\mathbf{v})^2 \leq \norm{\mathbf{v}}^2\norm{\mathbf{w}}^2.
$$

:::

:::{prf:example}
:label: Ex:InnerProduct:Cauchy-Schwarz-Check

We verify that the inequality holds for the vectors $\mathbf{v} = \begin{bmatrix} 1 \\ -2\\ 3 \\ -4 \end{bmatrix}$
and $\mathbf{w} = \begin{bmatrix} -5 \\ 4 \\-3 \\ 0 \end{bmatrix}$ in $\mathbb{R}^4$.

As follows

$$
  \mathbf{v}\ip\mathbf{w} = -5-8-9 = -22,
  \quad \norm{\mathbf{v}} = \sqrt{30}, \quad \norm{\mathbf{w}} = \sqrt{50}
$$

and we see that indeed

$$
|\mathbf{v}\ip\mathbf{w}| = 22 \leq  \norm{\mathbf{v}}\,\norm{\mathbf{w}} = \sqrt{1500}.
$$


:::

With this inequality established, the Triangle Inequality
{eq}`Item:Prop:InnerProduct:TriangleInequality` is easily proved. Let's repeat it, and prove it.

:::{prf:theorem}

For any two vectors in $\mathbb{R}^n$:

$$

    \norm{\mathbf{v}+\mathbf{w}} \leq \norm{\mathbf{v}}+\norm{\mathbf{w}}.
$$


:::

:::{prf:proof}
:class: dropdown


Since all  terms involved are non-negative we may as well show that the inequality holds for the squares:

$$

  \begin{array}{l}
  \norm{\mathbf{v}+\mathbf{w}}^2 \leq (\norm{\mathbf{v}}+\norm{\mathbf{w}})^2 \\
    \iff (\mathbf{v}+\mathbf{w})\ip(\mathbf{v}+\mathbf{w}) \leq \norm{\mathbf{v}}^2 + 2\norm{\mathbf{v}}\norm{\mathbf{w}} + \norm{\mathbf{w}}^2 \\
    \iff \mathbf{v}\ip\mathbf{v} + 2\mathbf{v}\ip\mathbf{w}+\mathbf{w}\ip\mathbf{w} \leq \norm{\mathbf{v}}^2 + 2\norm{\mathbf{v}}\norm{\mathbf{w}} + \norm{\mathbf{w}}^2 \\
    \iff 2\mathbf{v}\ip\mathbf{w} \leq 2\norm{\mathbf{v}}\norm{\mathbf{w}}
  \end{array}
$$

and this, apart from the factor 2, is  the Cauchy-Schwarz Inequality.

:::

:::{prf:example}
:label: Ex:InnerProduct:TriangleInequality



We verify the inequality for the vectors
$\mathbf{v} = \begin{bmatrix} -1 \\ 2\\ 3  \end{bmatrix}$
and $\mathbf{w} = \begin{bmatrix} 4 \\ -4\\ 3  \end{bmatrix}$:

$$

  \norm{\mathbf{v} + \mathbf{w}} = \sqrt{3^2+(-2)^2+6^2} =\sqrt{49} = 7
$$

and indeed

$$

 \norm{\mathbf{v}} + \norm{\mathbf{w}} = \sqrt{14} + \sqrt{35} > 3+5 = 8 > \norm{\mathbf{v} + \mathbf{w}}.
$$


:::

(Subsec:InnerProduct:Angles_in_Rn)=

## Angles in $\mathbb{R}^n$

The first motivation to consider the dot product came from the question of perpendicularity.
We have seen that the length of a vector can also be computed using a dot product.

Below we will show that not only can the dot product be used to mark angles between vectors of $\frac12\pi$
(namely, when the vectors are perpendicular), but that it is possible to express the angle between any two (nonzero) vectors into dot products.

:::{figure} Images/Fig-InnerProduct-AngleAndProjection.svg
:name: Fig:InnerProduct:AngleAndProjection

Angle between two vectors
:::

First we will show a geometrical characterization of the dot product that holds in $\mathbb{R}^2$ as well as in $\mathbb{R}^3$.

::::{prf:proposition}
:label: Prop:InnerProduct:DotProdGeometric



For two nonzero vectors $\mathbf{v}$ and $\mathbf{w}$ in either $\mathbb{R}^2$ or $\mathbb{R}^3$ the following identity holds:

:::{math}
:label: Eq:InnerProduct:GeometricDefinition

\mathbf{v}\ip\mathbf{w} = \norm{\mathbf{v}}\norm{\mathbf{w}} \cos(\varphi)
:::

where $\varphi$ is the angle between $\mathbf{v}$ and $\mathbf{w}$.

Note that this is in line with the special case of two perpendicular vectors:

$$

  \mathbf{v}\perp\mathbf{w} \iff \mathbf{v}\ip\mathbf{w}=0 \iff  \cos(\varphi)=0.
$$



::::

:::{prf:observation}
:label: Rem:InnerProduct:AngleViaDotProd



The angle between two nonzero vectors $\mathbf{v}$ and $\mathbf{w}$ is thus determined by  dot products in the following way

$$

  \cos(\varphi) = \frac{\mathbf{w}\ip\mathbf{v}}{\norm{\mathbf{v}}\norm{\mathbf{w}}}
 $$

so

$$

  \varphi = \arccos\left(\frac{\mathbf{w}\ip\mathbf{v}}{\norm{\mathbf{v}}\norm{\mathbf{w}}}\right)= \cos^{-1}\left(\frac{\mathbf{w}\ip\mathbf{v}}{\norm{\mathbf{v}}\norm{\mathbf{w}}}\right).
$$

:::

::::{prf:proof}

Now let's derive formula {eq}`Eq:InnerProduct:GeometricDefinition`.
Assume that $\mathbf{v}$ and $\mathbf{w}$ are nonzero vectors.
Recall the formula of the orthogonal projection

$$

  \mathbf{\hat{w}} = \dfrac{\mathbf{w}\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}}\mathbf{v}.
$$

Let $\varphi \in[0,\pi]$ denote the angle between two nonzero vectors $\mathbf{v}$ and $\mathbf{w}$.


From {numref}`Figure %s <Fig:InnerProduct:AngleAndProjection>` it is clear that the factor

$$
   \dfrac{\mathbf{w}\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}}
$$

is positive if the angle is sharp, zero if the angle is right, and negative if the angle is obtuse.

In the case of a sharp angle, by considering the right triangle  $\Delta OAB$,  where $A$ is the end point of $\mathbf{\hat{w}}$,  $B$  the end point of $\mathbf{w}$ we see that on the one hand

$$

  OA = \norm{\dfrac{\mathbf{w}\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}}\mathbf{v}}
   = \dfrac{|\mathbf{w}\ip\mathbf{v}|}{\mathbf{v}\ip\mathbf{v}}\norm{\mathbf{v}} = \dfrac{\mathbf{w}\ip\mathbf{v}}{\norm{\mathbf{v}}^2} \norm{\mathbf{v}} = \dfrac{\mathbf{w}\ip\mathbf{v}}{\norm{\mathbf{v}}}
$$

and on the other hand

$$

  OA = OB\cos(\varphi) = \norm{\mathbf{w}}\cos(\varphi).
$$

So we may conclude that

:::{math}
:label: Eq:InnerProduct:GeometricInterpretation

\mathbf{w}\ip\mathbf{v} =  \norm{\mathbf{v}}\norm{\mathbf{w}}\cos(\varphi).

:::



In the case of an obtuse angle, we use that the projection of $\mathbf{w}$ onto $\mathbf{v}$ is equal to the projection
of $\mathbf{w}$ onto $-\mathbf{v}$, as it is in fact the projection onto the line consisting of all multiples of $\mathbf{v}$. Now look at the picture on the right of figure  {numref}`Figure %s <Fig:InnerProduct:AngleAndProjection>`
. There you see that $\mathbf{w}$  and
$-\mathbf{v}$ make a sharp angle $\psi = \pi - \phi$, so we can apply 
Equation {eq}`Eq:InnerProduct:GeometricInterpretation` to  $\mathbf{w}$  and $-\mathbf{v}$:


$$

 \begin{array}{rcl}
  \mathbf{w}\ip\mathbf{v} = - \mathbf{w}\ip(\mathbf{-v}) &=& -\norm{\mathbf{w}}\norm{\mathbf{-v}}\cos(\psi) \\
                      &=& -\norm{\mathbf{w}}\norm{\mathbf{v}}\cos(\pi-\varphi) \\
                      &=&  \norm{\mathbf{w}}\norm{\mathbf{v}}\cos(\varphi).
  \end{array}
$$

::::


::::{prf:observation}
:label: Rem:InnerProduct:Interpretation|w|cos(theta)

Note that the absolute value of $\norm{\mathbf{w}}\norm{\mathbf{v}}\cos(\varphi)$
is the length of the orthogonal projection of $\vect{w}$  onto $\vect{v}$.

::::


:::{exercise}
:label: Ex:InnerProduct:AnglesInMethaneMolecule

In a methane molecule CH${}_4$  the four H-atoms are positioned in a perfectly symmetrical way around the C-atom.
We can model this as follows:
put the C-atom at the origin of $\mathbb{R}^3$, and the H-atoms at the positions/vectors

$$
  \mathbf{v}_1 = \begin{bmatrix}1 \\ 1 \\ 1   \end{bmatrix}, \quad
  \mathbf{v}_2 = \begin{bmatrix}-1 \\ -1 \\ 1   \end{bmatrix}, \quad
  \mathbf{v}_3 = \begin{bmatrix}-1 \\ 1 \\ -1   \end{bmatrix} \quad \text{and} \quad
  \mathbf{v}_4 = \begin{bmatrix}1 \\ -1 \\ -1   \end{bmatrix}.
$$

Then all four points have the same distance $\sqrt{3}$ to the origin, and all points have the same distance to each other,  namely

$$
    \norm{v_i - v_j} = \sqrt{2^2 + 2^2 + 0^2} = \sqrt{8}, \text{ for } i \neq j.
$$

The angle between for instance $\mathbf{v_1}$ and $\mathbf{v_3}$ is determined by

$$
   \cos(\varphi) = \dfrac{\mathbf{v_1}\ip\mathbf{v_3}}{\norm{\mathbf{v_1}}\norm{\mathbf{v_3}}} = \dfrac{-1}{\sqrt{3}\cdot\sqrt{3}} = -\frac13.
$$

So

$$
  \varphi = \arccos(-\tfrac13) \approx  1.9106 \approx 109.47^{o}.
$$

:::

Since we have defined the dot product and the norm in $\mathbb{R}^n$, we can use the last formula to also define the angle between two vectors in $\mathbb{R}^n$:

:::{prf:definition}
:label: Dfn:InnerProduct:AngleInRn



For two nonzero vectors $\mathbf{v}$ and $\mathbf{w}$ in $\mathbb{R}^n$, the *angle*  between the vectors  is defined as

$$

   \varphi = \angle(\mathbf{v},\mathbf{w}) =  \arccos\left(\dfrac{\mathbf{v}\ip\mathbf{w}}{\norm{\mathbf{v}}\,\norm{\mathbf{w}}} \right)$$

This definition makes sense, since the Cauchy-Schwarz Inequality implies

$$

    -1 \leq \dfrac{\mathbf{v}\ip\mathbf{w}}{\norm{\mathbf{v}}\,\norm{\mathbf{w}}} \leq 1
$$


:::

Note that just as before in the plane and in three-dimensional space, for nonzero vectors $\mathbf{v}$ and $\mathbf{w}$ we have

$$

   \mathbf{v}\perp\mathbf{w} \iff \mathbf{v}\ip\mathbf{w}=0 \iff \dfrac{\mathbf{v}\ip\mathbf{w}}{\norm{\mathbf{v}}\,\norm{\mathbf{w}}}=0 \iff \varphi =
   \angle(\mathbf{v},\mathbf{w}) = \tfrac12\pi.
$$

:::{prf:example}
:label: Ex:InnerProduct:AngleInRn

Let  $\mathbf{e_1}$ be the vector in $\mathbb{R}^n$ with first entry equal to 1 and all other entries equal to 0, and $\mathbf{v}$ be the vector with all entries equal to 1.  We find the angle between $\mathbf{e_1}$ and $\mathbf{v}$  in all cases $n = 2,\, 3,\,4,\,\ldots$.

For each $n\geq2$ we write  $\varphi_n = \angle(\mathbf{e_1},\mathbf{v})$.  Then

$$
 \cos(\varphi_n)  = \dfrac{\mathbf{e_1}\ip\mathbf{v}}{\norm{\mathbf{e_1}}\norm{\mathbf{v}}} = \dfrac{1}{\sqrt{n}}.
$$

So:

$$
  \varphi_n = \arccos(\tfrac{1}{\sqrt{n}}), \, n = 1,2,3,\ldots
$$

For $n=1$ we find $\cos(\varphi_1) = 1$, so $\varphi_1 = 0$, which makes sense, and for $n=2$, $\cos(\varphi_2) = \frac{1}{\sqrt{2}}$, so $\varphi_2 = \frac14\pi$, which you can check by a sketch in the plane.

For $n\geq3$ we don't get easy answers, but as $\frac{1}{\sqrt{n}} \downarrow 0$ when $n$ gets large,
we may conclude that for large $n$ in $\mathbb{R}^n$ the two vectors are 'almost' orthogonal.

:::
