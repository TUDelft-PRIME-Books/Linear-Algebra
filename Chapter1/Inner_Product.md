(Sec:DotProduct)=

# Dot Product

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
:class: dark-light

The length of a vector via Pythagoras' Theorem.
:::

:::{applet}
:url: dot_product/inner_product_length
:fig: Images/Fig-InnerProduct-length-3D.svg
:name: Fig:InnerProduct:length-3D
:status: approved
:class: dark-light

The length of a vector via Pythagoras' Theorem.
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

where for two points $A$ and $B$, by $AB$ we denote the length of the vector $\overrightarrow{AB}$,
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
:class: dark-light

Perpendicular versus non-perpendicular.
:::

Let us now turn our attention to another important geometric concept, namely that of
perpendicularity. It is clear from {numref}`Figure %s <Fig:InnerProduct:perp-non-perp>` that the vectors $\begin{bmatrix}2\\3\end{bmatrix}$ and $\begin{bmatrix}-3\\2\end{bmatrix}$ are perpendicular, whereas the vectors $\begin{bmatrix}2\\3\end{bmatrix}$ and $\begin{bmatrix}-1\\3\end{bmatrix}$ are not. <br />
There is another way to look at this, which will be useful for the definition of perpendicularity in higher dimensions. To that end, consider {numref}`Figure %s <Fig:InnerProduct:diagonal-parallelogram>`. Here you see two vectors $\vect{v}$ and $\vect{w}$ and the parallelogram they span. You also see the diagonals of this parallelogram, which are given by $\vect{v}+\vect{w}$ and $\vect{v}-\vect{w}$. Two vectors are perpendicular if and only if the parallelogram they span is a rectangle, and this is exacty the situation where the diagonals have the same length, i.e.,

:::{math}
:label: EqualDiagonals

\norm{\mathbf{v}+\mathbf{w}} = \norm{\mathbf{v}-\mathbf{w}}.
:::

%In the picture on the right the vectors are not perpendicular and
%
%$$
%
%  \norm{\mathbf{v}+\mathbf{w}} \neq \norm{\mathbf{v}-\mathbf{w}}.
%$$

```{applet}
:url: dot_product/diagonal_parallelogram
:fig: Images/Fig-InnerProduct-diagonal-parallelogram.svg
:name: Fig:InnerProduct:diagonal-parallelogram
:class: dark-light

The parallelogram spanned by $\vect{v}$ and $\vect{w}$ and its diagonals. How should you choose $\vect{v}$ and $\vect{w}$ such that the diagonals have the same length?
```

In the picture on the right the vectors are not perpendicular and

$$

  \norm{\mathbf{v}+\mathbf{w}} \neq \norm{\mathbf{v}-\mathbf{w}}.
$$

So far we have been talking about two (nonzero) vectors in the plane, i.e., in $\mathbb{R}^2$. However, two vectors in $\mathbb{R}^3$ form a parallelogram as well, which also becomes a rectangle if and only if the vectors are perpendicular. We introduce a notation for this: if $ \mathbf{v}$ and $\mathbf{w}$ are perpendicular, we write this as

:::{math}
:label: Eq:InnerProduct:Orthogonal

\mathbf{v} \perp \mathbf{w}.
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

\mathbf{v} \perp \mathbf{w} \iff a_1b_1 +a_2b_2+a_3b_3=0.
:::

The derivation is completely analogous to the one above, only now we have one extra term.
So to check 'algebraically' whether two vectors are perpendicular we just have to compute $a_1b_1 +a_2b_2\, (\,+\,a_3b_3\,)$
and see whether this is equal to 0.

This expression is called the _dot product_ (or _inner product_) of the vectors $\mathbf{v}$ and $\mathbf{w}$. We denote it by $\mathbf{v}\ip\mathbf{w}$.
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

The **dot product** (or _inner product_) of two vectors
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
  \mathbf{v}_1=\begin{bmatrix} 5\\3\\4\\-2\end{bmatrix}
  \quad \text{and}\quad
  \mathbf{v}_2=\begin{bmatrix} 2\\3\\0\\1\end{bmatrix}
$$

is given by

$$
  \mathbf{v}_1\ip\mathbf{v}_2 =
  5\cdot2 + 3\cdot3 +4\cdot0 + (-2)\cdot1
  = 17.
$$

And the dot product of the two vectors

$$
  \mathbf{v}_1=\begin{bmatrix} 5\\3\\4\\-2\end{bmatrix}
  \quad \text{and}\quad
  \mathbf{v}_3=\begin{bmatrix} -4\\3\\2\end{bmatrix}
$$

is not defined. In fact, the dot product of a vector $\mathbf{v}$ in $\mathbb{R}^m$ and a vector $\mathbf{w}$ in $\mathbb{R}^n$ is only defined if $m = n$.

:::

We state the characteristic rules of the dot product in $\mathbb{R}^n$, which in the sequel we will use time and again, in the following
proposition.

:::{prf:proposition}
:label: Prop:RulesInnerProduct

The following properties hold for any vectors $\mathbf{v},\mathbf{v}_1,\mathbf{v}_2,\mathbf{v}_3$ in $\mathbb{R}^n$ and scalars $c \in \mathbb{R}$:

i. $\mathbf{v}_1\ip\mathbf{v}_2 = \mathbf{v}_2\ip\mathbf{v}_1$.

ii. $(c\mathbf{v}_1)\ip\mathbf{v}_2 = c(\mathbf{v}_1\ip\mathbf{v}_2) = \mathbf{v}_1\ip(c \mathbf{v}_2)$.

iii. $(\mathbf{v}_1+\mathbf{v}_2)\ip\mathbf{v}_3 = \mathbf{v}_1\ip\mathbf{v}_3+\mathbf{v}_2\ip\mathbf{v}_3$.

iv. $\mathbf{v}\ip\mathbf{v} \geq 0$, &nbsp; and&nbsp; $\mathbf{v}\ip\mathbf{v} = 0 \iff \mathbf{v} = \mathbf{0}$.
:::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:RulesInnerProduct`
:class: tudproof

The first three properties follow from the corresponding properties of real numbers. For instance, for the first rule we simply use that $ab = ba$ holds for the product of real numbers $a$ and $b$.

i. Let

$$
\mathbf{v}_1=\begin{bmatrix} a_1\\a_2\\ \vdots\\ a_n\end{bmatrix}
  \quad \text{and}\quad
  \mathbf{v}_2=\begin{bmatrix}  b_1 \\ b_2 \\ \vdots \\ b_n \end{bmatrix}
$$

be two arbitrary vectors in $\mathbb{R}^n$. Then

$$
\begin{align*}
\mathbf{v}_1 \ip \mathbf{v}_2 &=
\begin{bmatrix}a_{1} \\ a_{2}\\ \vdots\\a_{n}\end{bmatrix} \ip \begin{bmatrix}b_{1} \\ b_{2}\\ \vdots \\ b_{n}\end{bmatrix}
            = a_1b_1 +a_2b_2+ \ldots + a_nb_n  \\
      &= b_1a_1 +b_2a_2+ \ldots + b_na_n =
               \begin{bmatrix}b_{1} \\ b_{2}\\ \vdots \\ b_{n}\end{bmatrix}\ip\begin{bmatrix}a_{1} \\ a_{2}\\ \vdots\\ a_{n}\end{bmatrix} = \mathbf{v}_2\ip\mathbf{v}_1.
\end{align*}
$$

ii. For two vectors $\vect{v}_1 = \begin{bmatrix}a_{1} \\ a_{2}\\ \vdots\\ a_{n}\end{bmatrix}$, $\vect{v}_2 = \begin{bmatrix}b_{1} \\ b_{2}\\ \vdots\\ b_{n}\end{bmatrix}$  
&nbsp;and constants $c$ we see that

$$
\begin{eqnarray*}
            (c\mathbf{v}_1)\ip\mathbf{v}_2 &=&  \begin{bmatrix}ca_{1}\\ca_{2}\\ \vdots\\ca_{n}\end{bmatrix}\ip\begin{bmatrix}b_{1}\\b_{2}\\       \vdots\\b_{n}\end{bmatrix} = (ca_1)b_1 + (ca_2)b_2+ \ldots + (ca_n)b_n \\
            &=& c\,(a_1b_1 +a_2b_2+ \ldots + a_nb_n) = c\, (\mathbf{v}_1\ip\mathbf{v}_2)
\end{eqnarray*}
$$

iii. Is proved in the same way as (ii).

iv. This consists of two statements. For the first, we note that

$$
 \mathbf{v}\ip\mathbf{v} = a_1a_1 +a_2a_2+ \ldots + a_na_n = a_1^2+a_2^2 + \ldots + a_n^2
$$

is the sum of squares of real numbers, so it is nonnegative. That is,

$$
  \mathbf{v}\ip\mathbf{v} \geq 0.
$$

To prove the second statement, we see that

$$
  \mathbf{v}\ip\mathbf{v} =  a_1^2+a_2^2 + \ldots + a_n^2 = 0
$$

if and only if all the squares are 0, which only happens if each entry $a_i$ is equal to zero, that is, if $\mathbf{v} = \mathbf{0}$.
:::

:::{exercise}
:label: Exc:InnerProduct:CheckPropInnerProd

Prove property iii.
:::

:::{admonition} Solution to&nbsp;{numref}`Exc:InnerProduct:CheckPropInnerProd`
:class: solution, dropdown

Let

$$
\mathbf{v}_1=\begin{bmatrix} a_1\\a_2\\ \vdots\\ a_n\end{bmatrix}
  \quad \text{and}\quad
  \mathbf{v}_2=\begin{bmatrix}  b_1 \\ b_2 \\ \vdots \\ b_n \end{bmatrix}
  \quad \text{and}\quad
    \mathbf{v}_3=\begin{bmatrix}  c_1 \\ c_2 \\ \vdots \\ c_n \end{bmatrix}


$$

be three arbitrary vectors in $\mathbb{R}^n$. Then

$$
\begin{align*}
\left(\mathbf{v}_1 + \mathbf{v}_2 \right) \ip \mathbf{v}_3 &=
\left(\begin{bmatrix}a_{1} \\ a_{2}\\ \vdots\\a_{n}\end{bmatrix} + \begin{bmatrix}b_{1} \\ b_{2}\\ \vdots \\ b_{n}\end{bmatrix} \right) \ip \begin{bmatrix}  c_1 \\ c_2 \\ \vdots \\ c_n \end{bmatrix} \\
&= \begin{bmatrix} a_1+b_1\\a_2+b_2\\ \vdots\\ a_n+b_n\end{bmatrix}\ip \begin{bmatrix}  c_1 \\ c_2 \\ \vdots \\ c_n \end{bmatrix} \\
            &= (a_1+b_1)c_1 +(a_2+b_2)c_2+ \ldots + (a_n+b_n)c_n  \\
      &= a_1c_1 +b_1c_1+a_2c_2+b_2c_2 \ldots + a_nc_n+b_nc_n \\
      &= a_1c_1 +a_2c_2+\ldots + a_nc_n +b_1c_1+b_2c_2 \ldots +b_nc_n \\
      &= \begin{bmatrix}a_{1} \\ a_{2}\\ \vdots\\a_{n}\end{bmatrix}\ip\begin{bmatrix}  c_1 \\ c_2 \\ \vdots \\ c_n \end{bmatrix}+\begin{bmatrix}  b_1 \\ b_2 \\ \vdots \\ b_n \end{bmatrix}\ip\begin{bmatrix}  c_1 \\ c_2 \\ \vdots \\ c_n \end{bmatrix} \\
      &= \mathbf{v}_1\ip\mathbf{v}_3+\mathbf{v}_2\ip\mathbf{v}_3.
\end{align*}
$$

:::

:::{exercise}
:label: Exc:InnerProduct:(v-w)(v+w)

Prove the identity

$$
  (\mathbf{v}_1+\mathbf{v}_2)\ip(\mathbf{v}_1-\mathbf{v}_2) = \mathbf{v}_1\ip\mathbf{v}_1-\mathbf{v}_2\ip\mathbf{v}_2.
$$


:::

:::{admonition} Solution to&nbsp;{numref}`Exc:InnerProduct:(v-w)(v+w)`
:class: solution, dropdown

First of all, because of rule i. and rule iii. of {prf:ref}`Prop:RulesInnerProduct`
it holds that

$$
   \mathbf{v}_1\ip(\mathbf{v}_2+\mathbf{v}_3) = \mathbf{v}_1\ip\mathbf{v}_2+\mathbf{v}_1\ip\mathbf{v}_3
$$

and it also follows from ii. and iii. that

$$
   \mathbf{v}_1\ip(\mathbf{v}_2-\mathbf{v}_3) = \mathbf{v}_1\ip(\mathbf{v}_2+(-1)\mathbf{v}_3) =\mathbf{v}_1\ip\mathbf{v}_2+\mathbf{v}_1\ip(-1\mathbf{v}_3) = \mathbf{v}_1\ip\mathbf{v}_2-\mathbf{v}_1\ip\mathbf{v}_3
$$

Then the statement is proved by the following chain of identities

$$
  \begin{array}{rcl}(\mathbf{v}_1+\mathbf{v}_2)\ip(\mathbf{v}_1-\mathbf{v}_2) &=&
    \mathbf{v}_1\ip(\mathbf{v}_1-\mathbf{v}_2) + \mathbf{v}_2\ip(\mathbf{v}_1-\mathbf{v}_2) \\
    &=& \mathbf{v}_1\ip\mathbf{v}_1-\mathbf{v}_1\ip\mathbf{v}_2
    + \mathbf{v}_2\ip\mathbf{v}_1-\mathbf{v}_2\ip\mathbf{v}_2\\
    &=& \mathbf{v}_1\ip\mathbf{v}_1-\mathbf{v}_2\ip\mathbf{v}_2.
  \end{array}


$$

:::

:::{exercise}
:label: Exc:InnerProduct:PargramRule

Prove the identity

$$

  \norm{\mathbf{v}_1+\mathbf{v}_2}^2 + \norm{\mathbf{v}_1-\mathbf{v}_2}^2   = 2 (\norm{\mathbf{v}_1}^2 + \norm{\mathbf{v}_2}^2),
$$

and explain why it is called the _parallelogram rule_.

:::



:::{admonition} Solution to&nbsp;{numref}`Exc:InnerProduct:PargramRule`
:class: solution, dropdown

Again it's a chain of identities using basic properties of the dot product.

$$
  \begin{array}{rcl} \norm{\mathbf{v}_1+\mathbf{v}_2}^2 + \norm{\mathbf{v}_1-\mathbf{v}_2}^2&=&  (\mathbf{v}_1+\mathbf{v}_2)\cdot(\mathbf{v}_1+\mathbf{v}_2) +
      (\mathbf{v}_1-\mathbf{v}_2)\cdot(\mathbf{v}_1-\mathbf{v}_2)     \\
    &=& \mathbf{v}_1\cdot\mathbf{v}_1 +2\mathbf{v}_1\cdot\mathbf{v}_2 + \mathbf{v}_2\cdot\mathbf{v}_2 + \mathbf{v}_1\cdot\mathbf{v}_1 -2\mathbf{v}_1\cdot\mathbf{v}_2 + \mathbf{v}_2\cdot\mathbf{v}_2  \\
    &=&   2\,\mathbf{v}_1\cdot\mathbf{v}_1 +2\,\mathbf{v}_2\cdot\mathbf{v}_2    \\
    &=&   2 (\norm{\mathbf{v}_1}^2 + \norm{\mathbf{v}_2}^2).
  \end{array}


$$


The figure explains the name. 

:::{figure} Images/Fig-InnerProduct-ParGramRule.svg
:name: Fig:InnerProduct:ParGramrule
:class: dark-light

Parallelogram rule explained.

:::

In the parallelogram  $OABC$  the sum of the squares of the lengths of the four sides equals the sum 
the squares of the lengths of the diagonals.

$$
\begin{array}{ll}
  OA^2 + AB^2 + BC^2 + CO^2 &=& 2\norm{\vect{v}_1}^2 + 2\norm{\vect{v}_2}^2 \\
      &=& \norm{\mathbf{v}_1+\mathbf{v}_2}^2 + \norm{\mathbf{v}_1-\mathbf{v}_2}^2    
      =  OB^2 + CA^2
\end{array}
$$

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

Two vectors $\mathbf{v}$ and $\mathbf{w}$ in $\mathbb{R}^n$ are called **orthogonal** if $\mathbf{v}\ip\mathbf{w} = 0$. As before, we denote this by $\mathbf{v}\perp\mathbf{w}$.

:::

:::{prf:example}
:label: Ex:InnerProduct:CheckVectorsOrthogonal

Let &nbsp; $\mathbf{u} = \begin{bmatrix} 1\\2\\-1\\-1\end{bmatrix}$, &nbsp; $\mathbf{v} = \begin{bmatrix} 3\\-1\\2\\-1\end{bmatrix}$ &nbsp; and &nbsp;
$\mathbf{w} = \begin{bmatrix} 2\\2\\-1\\2\end{bmatrix}$.

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

and conclude that $\mathbf{u}$ and $\mathbf{v}$ are orthogonal, $\mathbf{u}$ and $\mathbf{w}$ are not orthogonal, <br/> $\mathbf{v}$ and $\mathbf{w}$ are orthogonal.

:::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/59912254-6fc8-43c7-9c44-1ea7eab1c236?id=62409
:label: grasple_exercise_1_2_1T
:dropdown:
:description: To compute some dot products in $\R^2, \R^3, \R^4$.

::::

In $\mathbb{R}^2$, two nonzero vectors that are orthogonal to the same nonzero vector $\mathbf{v}$ are automatically multiples of each other (i.e. have either the same or the opposite direction). In $\mathbb{R}^n$ with $n \geq 3$ this no longer holds. In the previous example both vectors $\mathbf{u}$ and $\mathbf{w}$ are orthogonal to the vector $\mathbf{v}$, but $\mathbf{u} \neq c\mathbf{w}$.

By definition the zero vector is orthogonal to any vector, since $\mathbf{0}\ip\mathbf{v} = 0$. Moreover, the zero vector is the _only_ vector that is orthogonal to itself, which is the content of the next proposition.

:::{prf:proposition}
:label: Prop:InnerProduct:vDotv=0Impliesv=0

Suppose $\mathbf{v} \in \mathbb{R}^n$. &nbsp; Then $\mathbf{v}\perp\mathbf{v} \iff \mathbf{v} = \mathbf{0}$.

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:InnerProduct:vDotv=0Impliesv=0`
:class: tudproof

By definition

$$

 \mathbf{v}\perp\mathbf{v} \iff \mathbf{v}\ip\mathbf{v}=0
$$

In {prf:ref}`Prop:RulesInnerProduct` iv. it was stated that the last equality only holds for $\mathbf{v} = \mathbf{0}$.

:::

The fact that the zero vector is orthogonal to _any_ vector is an immediate consequence of the definition, but it
may seem counterintuitive to you. The following example illustrates a situation where this orthogonality leads to a much nicer outcome.

::::{prf:example}
:label: Ex:PerpendicularLine

Let $\mathbf{n}$ be any nonzero vector in the plane.
The set of vectors that are orthogonal to $\mathbf{n}$ all lie on a line $\mathcal{L}$ through the origin. (See {numref}`Figure %s <Fig:InnerProduct:PerpendicularLine>`.) If we agree that $\mathbf{0}\perp\mathbf{n}$, it will be the whole line.
The vector $\mathbf{n}$ is often said to be a _normal_ vector to the line.

```{applet}
:url: dot_product/perpendicularline
:fig: Images/Fig-InnerProduct-PerpendicularLine.svg
:name: Fig:InnerProduct:PerpendicularLine
:class: dark-light

The line $\mathcal{L}$ of vectors orthogonal to a nonzero vector $\mathbf{n}$ in the plane.
```

::::

We conclude this subsection with another concept that we will come across later in a much more general context. Informally, it is the (orthogonal) projection of a vector onto another vector. More precisely, it is the orthogonal projection of a vector $\mathbf{w}$ onto the line $\mathcal{L}$ generated by the nonzero vector $\mathbf{v}$, by which we mean $\mathcal{L}= \{ c\mathbf{v}: c \in \mathbb{R}\}$.

See {numref}`Figure %s <Fig:InnerProduct:ProjectionVectorLine>`.

:::{prf:definition}
:label: Dfn:InnerProduct:OrthoProjectionOntoVector

The _orthogonal projection of a vector $\mathbf{w}$ onto the nonzero vector $\mathbf{v}$_ is the vector $\mathbf{\hat{w}} = c\mathbf{v} $ for which

$$

  (\mathbf{w} - \mathbf{\hat{w}}) \perp \mathbf{v}.
$$

Another notation for this vector is

$$

  \mathbf{\hat{w}} = \text{proj}_{\mathbf{v}}(\mathbf{w}).
$$

:::

:::{applet}
:url: dot_product/innerproduct_projectionvectorline
:fig: Images/Fig-InnerProduct-ProjectionVectorLine.svg
:name: Fig:InnerProduct:ProjectionVectorLine
:class: dark-light

Projection of a vector $\mathbf{w}$ onto a nonzero vector $\mathbf{v}$.
:::

:::{prf:proposition}
:label: Prop:InnerProduct:UniqueProjection

In the definition above the vector $\mathbf{\hat{w}}$ with these properties is unique
and it is given by

$$

  \text{proj}_{\mathbf{v}}(\mathbf{w}) = \mathbf{\hat{w}} = \frac{\mathbf{w}\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}} \mathbf{v}.
$$

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:InnerProduct:UniqueProjection`
:class: tudproof

With the rules of the dot product the vector $\mathbf{w}$ is easily constructed. <BR>
Starting from

$$

   \mathbf{\hat{w}} = c\mathbf{v}, \text{ for some } c\in\mathbb{R}
$$

and

$$

  (\mathbf{w} - \mathbf{\hat{w}}) \perp \mathbf{v},
$$

it follows that we must have

$$

   (\mathbf{w} - c\mathbf{v}) \ip \mathbf{v} =
   \mathbf{w}\ip \mathbf{v} - c \,(\mathbf{v}\ip \mathbf{v}) =  0.
$$

So $c$ is uniquely given by

$$

  c = \frac{\mathbf{w}\ip \mathbf{v}}{\mathbf{v}\ip \mathbf{v}}
$$

and indeed $\mathbf{\hat{w}}$ must be as stated.

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

We proceed as follows

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

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/88c460cd-36ee-49b0-8fb8-d29b55ad253a?id=84822
:label: grasple_exercise_1_2_2T
:dropdown:
:description: Computing the projection of a vector $\vect{w}$ onto a vector $\vect{v}$.

::::

:::{exercise}
:label: Exc:InnerProduct:SameProjectionThenWhat

Suppose $\text{proj}_{\mathbf{v}}(\mathbf{w}_1) = \text{proj}_{\mathbf{v}}(\mathbf{w}_2) $,
for three nonzero vectors $\mathbf{v}, \,\mathbf{w}_1,\,\mathbf{w}_2$ in $\mathbb{R}^n$.
What does this say about the relative positions of the three vectors?

Verify your statement for the following three vectors

$$

 \mathbf{v} = \begin{bmatrix} 1\\ 1 \\ -2 \\ -3\end{bmatrix}, \quad
 \mathbf{w}_1 = \begin{bmatrix} 6\\ 4 \\ -7 \\ -7\end{bmatrix}, \quad
 \mathbf{w}_2 = \begin{bmatrix} 5\\ 6 \\ -2 \\ -10\end{bmatrix}.
$$

:::

::::{admonition} Solution to&nbsp;{numref}`Exc:InnerProduct:SameProjectionThenWhat`
:class: solution, dropdown

Suppose $\text{proj}_{\mathbf{v}}(\mathbf{w}_1) = \text{proj}_{\mathbf{v}}(\mathbf{w}_2) $.  Thus  $\dfrac{\mathbf{w}_1\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}} \mathbf{v} = \dfrac{\mathbf{w}_2\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}} \mathbf{v}$.

Since $\mathbf{v}$ is not the zero vector this implies that
$\mathbf{w}_1\ip\mathbf{v} = \mathbf{w}_2\ip\mathbf{v}$. In other words,

$$
  \mathbf{w}_1\ip\mathbf{v} - \mathbf{w}_2\ip\mathbf{v} =
  (\mathbf{w}_1 - \mathbf{w}_2)\ip \mathbf{v} = 0,
$$

which expresses that &nbsp; $(\mathbf{w}_1 - \mathbf{w}_2)\perp \vect{v}$.

For the given vectors $\mathbf{v}, \mathbf{w}_1, \mathbf{w}_2$ we find

$$
  \dfrac{\mathbf{w}_1\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}} \mathbf{v} =
       \frac{\mathbf{w}_2\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}} \mathbf{v} =
       \dfrac{45}{15}\mathbf{v}
$$

and

$$
\mathbf{w}_1 - \mathbf{w}_2 = \begin{bmatrix} 6\\ 4 \\ -7 \\ -7\end{bmatrix} - \begin{bmatrix} 5\\ 6 \\ -2 \\ -10 \end{bmatrix} =
  \begin{bmatrix} 1\\ -2 \\ -5 \\ 3\end{bmatrix}.
$$

We see $(\mathbf{w}_1 - \mathbf{w}_2)\ip \mathbf{v} = 1 - 2 + 10 + 9 = 0$,
so indeed $(\mathbf{w}_1 - \mathbf{w}_2)$ and $\vect{v}$ are orthogonal.

{numref}`Figure %s <Fig:InnerProduct:SameProj>` shows what is going on.

:::{figure} Images/Fig-InnerProduct-SameProj.svg
:name: Fig:InnerProduct:SameProj
:class: dark-light

Two vectors $\vect{w}_1$, $\vect{w}_2 $  with the same projection onto $\vect{v}$.

:::

::::

(Subsec:InnerProduct:Norm_in_Rn)=

## Norm in $\mathbb{R}^n$

The length of a vector in the plane can be computed using the dot product: for
$\mathbf{v}=\begin{bmatrix}a_{1}\\a_{2}\end{bmatrix}$ in $\mathbb{R}^2$ we have seen that

$$

  \norm{\mathbf{v}} = \sqrt{a_1^2 + a_2^2} = \sqrt{\mathbf{v}\ip\mathbf{v}}.
$$

The identity $\norm{\mathbf{v}}  = \sqrt{\mathbf{v}\ip\mathbf{v}}$ &nbsp;also holds in $\mathbb{R}^3$.

It seems natural to extend the concept to $\mathbb{R}^n$. Again, for this more general space a new word is introduced.

:::{prf:definition}
:label: Dfn:InnerProduct:NormOfVector

The **norm** of a vector $\mathbf{v}$ in $\mathbb{R}^n$, denoted by $\norm{\mathbf{v}}$, is defined by

$$

 \norm{\mathbf{v}} = \sqrt{\mathbf{v}\ip\mathbf{v}\,}.
$$

:::

Expressed in the entries of $\mathbf{v}$ this yields

$$

  \norm{\mathbf{v}} = \sqrt{a_1^2+ a_2^2 + \ldots +a_n^2\,}\,,
$$

so for vectors in $\mathbb{R}^2$ and $\mathbb{R}^3$ the norm of a vector is just the length of the vector.

As we might expect the norm has many properties in common with length.

::::{prf:proposition}
:label: Prop:InnerProduct:PropertiesNorm

For any $\mathbf{v}, \,\mathbf{w} \in \mathbb{R}^{n}$ and all $c \in \mathbb{R}$ the following holds:

i. $\norm{\mathbf{v}}\geq 0$, and $\norm{\mathbf{v}} = 0$ only for $\mathbf{v}=\mathbf{0}$;

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

The first two of these properties are very easy to prove. The proof of the triangle inequality we postpone until the end of the section. {numref}`Figure %s <Fig:InnerProduct:TriangleInequality>` explains the name.

:::{applet}
:url: dot_product/triangle_inequality
:fig: Images/Fig-InnerProduct-TriangleInequality.svg
:name: Fig:InnerProduct:TriangleInequality
:position: 2,2
:class: dark-light

The Triangle Inequality.
:::

::::{prf:example}
:label: Ex:InnerProduct:NormsofTwoVectors

We compute the norms of the vectors

$$
\mathbf{v} = \begin{bmatrix} 1 \\ -2 \\ 3 \\ -1 \end{bmatrix} \quad \text{and} \quad  -2\mathbf{v} = \begin{bmatrix} -2 \\ 4 \\ -6 \\ 2 \end{bmatrix}.
$$

We find

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

::::

::::{prf:definition}
:label: Dfn:InnerProduct:Distance

The **distance** between two vectors in $\R^n$ is defined by

$$
  \text{dist}(\vect{u},\vect{v}) = \norm{\vect{v}-\vect{u}}.
$$

::::

::::{prf:example}
:label: Ex:InnerProduct:Distance

For the vectors $\vect{u} = \begin{bmatrix}1 \\ 3 \\ 2 \\ 4 \end{bmatrix}$ and
$\vect{v} = \begin{bmatrix}5 \\ 1 \\ 3 \\ 4 \end{bmatrix}$ in $\R^4$

the distance is given by

$$

  \norm{\vect{v}-\vect{u}} = \norm{\begin{bmatrix}4 \\ -2 \\ 1 \\ 0 \end{bmatrix}}
  = \sqrt{4^2 + (-2)^2 + 1^2 + 0^2} = \sqrt{21}.
$$

::::

:::{figure} Images/Fig-InnerProduct-Distance.svg
:name: Fig:InnerProduct:Distance
:class: dark-light

The distance between two vectors.
:::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5bc4274c-56a0-461b-bd3d-9f8bdb8f44e0?id=69740
:label: grasple_exercise_1_2_2
:dropdown:
:description: Computing the distance between two vectors in $\R^3$.

::::

From the rules of the norm the following rules of the distance function can be deduced.

::::{prf:proposition}
:label: Prop:InnerProduct:PropertiesDistance

For any three vectors $\mathbf{u}, \mathbf{v}$ and $\mathbf{w} \in \mathbb{R}^{n}$ the following statements hold.

i. $\text{dist}(\vect{u},\vect{v}) = \text{dist}(\vect{v},\vect{u})$;

ii. $\text{dist}(\vect{u},\vect{v}) = 0 \iff \vect{u}=\vect{v}$;

iii. $\text{dist}(\vect{u},\vect{w}) \leq \text{dist}(\vect{u},\vect{v}) + \text{dist}(\vect{v},\vect{w})$.

Rule iii. is again called the _Triangle Inequality_.

::::

::::{exercise}
:label: Exc:InnerProduct:ProofPropDist

Check the three properties of the distance function as stated in
{prf:ref}`Prop:InnerProduct:PropertiesDistance`. &nbsp;
For Rule iii., only show how it follows from the corresponding Rule iii. in
proposition  {prf:ref}`Prop:InnerProduct:PropertiesNorm`. 
::::

With the tools so far we can define a notion that comes in handy later.

:::{prf:definition}
:label: Dfn:InnerProduct:UnitVector

A **unit vector** is a vector of norm 1.

Moreover, for any nonzero vector $\mathbf{v}$,
the vector

$$

  \mathbf{u} = \frac{\mathbf{v}}{\norm{\mathbf{v}}}
$$

is called the _unit vector in the direction of $\mathbf{v}$_.

:::

:::{prf:proposition}
:label: Prop:InnerProduct:UnitVectorForv

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

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:InnerProduct:UnitVectorForv`
:class: tudproof

Assume that $\mathbf{v} \neq \mathbf{0}$.
For $\mathbf{u} = k\mathbf{v}$, with $\norm{\mathbf{u}} = 1$ and $k > 0$ to hold, we must have

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

We compute the unit vector $\mathbf{u}$ in the direction of the vector $\mathbf{v} = \begin{bmatrix}1 \\ 2 \\ 4 \\ -2 \end{bmatrix}$ in $\mathbb{R}^4$.  
As follows:

$$

\norm{\mathbf{v}} = \sqrt{1^2+2^2+4^2+(-2)^2} = \sqrt{25} = 5,
$$

so

$$
\mathbf{u} = \dfrac{1}{5} \begin{bmatrix}1 \\ 2 \\ 4 \\ -2 \end{bmatrix} = \begin{bmatrix}1/5 \\ 2/5 \\ 4/5 \\ -2/5 \end{bmatrix}.
$$

:::

Interestingly, Pythagoras' theorem also holds in $\mathbb{R}^n$.

:::{prf:theorem}
:label: Thm:InnerProduct:PythagorasInRn

For any two vectors $\mathbf{v}$ and $\mathbf{w}$ in $\mathbb{R}^n$ we have

$$

 \norm{\mathbf{v}+\mathbf{w}}^2 = \norm{\mathbf{v}}^2 + \norm{\mathbf{w}}^2
    \iff \mathbf{v} \perp \mathbf{w}.
$$

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Thm:InnerProduct:PythagorasInRn`
:class: tudproof

This follows quite straightforwardly from the properties of the dot product.

Let us start from the identity on the left and work our way to the conclusion on the right, making sure that each step is reversible.
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

 \mathbf{v}\ip\mathbf{w}+\mathbf{w}\ip\mathbf{v} = 0
$$

And then we are almost there:

$$


 \mathbf{v}\ip\mathbf{w}+\mathbf{w}\ip\mathbf{v} = 0
  \iff 2\,\mathbf{v}\ip\mathbf{w} = 0
  \iff \mathbf{v}\ip\mathbf{w}= 0
  \iff \mathbf{v}\perp\mathbf{w}.
$$

:::

:::{prf:example}
:label: Ex:InnerProduct:Pythagoras_in_R^4

We verify the equality for the vectors $\mathbf{v} = \begin{bmatrix} 2 \\ -3\\ 3 \\ 1 \end{bmatrix}$
and $\mathbf{w} = \begin{bmatrix} 2 \\ 4 \\ 1 \\ 5 \end{bmatrix}$ in $\mathbb{R}^4$.

First of all

$$

  \mathbf{v} \ip \mathbf{w}  = 4 - 12 + 3 + 5  = 0,
$$

so $\mathbf{v}\perp \mathbf{w}$, and second

$$

  \norm{\mathbf{v}} = \sqrt{2^2 + (-3)^2 + 3^2 + 1^2} = \sqrt{23}, \quad
  \norm{\mathbf{w}} = \sqrt{2^2 + 4^2 + 1^2 + 5^2} = \sqrt{46}.
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

:::{prf:theorem} Cauchy-Schwarz Inequality
:label: Thm:InnerProduct:Cauchy-Schwarz

For any two vectors in $\mathbb{R}^n$

$$

    |\mathbf{v}\ip\mathbf{w}| \leq  \norm{\mathbf{v}} \norm{\mathbf{w}}.
$$

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Thm:InnerProduct:Cauchy-Schwarz`&nbsp;({prf:ref}`Cauchy-Schwarz Inequality <Thm:InnerProduct:Cauchy-Schwarz>`)
:class: tudproof

There are many ways to prove the Cauchy-Schwarz inequality. There is even a whole book devoted to it: "Cauchy Schwarz master class" by J.M. Steele.

The following proof is based on orthogonal projection and Pythagoras' Theorem.

If
$\mathbf{v} = \mathbf{0}$, the zero vector, then the inequality obviously holds; in fact it becomes an equality:

$$

  \mathbf{v} = \mathbf{0} \Longrightarrow  \norm{\mathbf{v}} = 0
  \Longrightarrow \norm{\mathbf{v}} \norm{\mathbf{w}} = 0
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
Then we can apply Pythagoras' Theorem!

$$

 (\mathbf{w} - \mathbf{\hat{w}}) \perp  \mathbf{\hat{w}}  \Longrightarrow \norm{\mathbf{w} - \mathbf{\hat{w}}}^2 + \norm{ \mathbf{\hat{w}}}^2 =
 \norm{(\mathbf{w} - \mathbf{\hat{w}}) + \mathbf{\hat{w}}}^2 =
 \norm{\mathbf{w}}^2.
$$

It follows that

$$

  \norm{ \mathbf{\hat{w}}}^2   = \norm{\mathbf{w}}^2 - \norm{\mathbf{w} - \mathbf{\hat{w}}}^2 \leq \norm{\mathbf{w}}^2.
$$

Substitution of the expression for $\mathbf{\hat{w}}$ leads to

$$

   \left(\dfrac{\mathbf{w}\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}}\right)^2 \norm{\mathbf{v}}^2  =
   \dfrac{(\mathbf{w}\ip\mathbf{v})^2}{(\mathbf{v}\ip\mathbf{v})^2} \norm{\mathbf{v}}^2    \leq \norm{\mathbf{w}}^2.
$$

Using

$$

  \mathbf{v}\ip\mathbf{v} = \norm{\mathbf{v}}^2
$$

we deduce that

$$

   (\mathbf{w}\ip\mathbf{v})^2 \leq \norm{\mathbf{v}}^2\norm{\mathbf{w}}^2.
$$

Taking square roots we may conclude that indeed

$$
   |\mathbf{w}\ip\mathbf{v}|  \, \leq  \, \norm{\mathbf{v}} \norm{\mathbf{w}}.
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
|\mathbf{v}\ip\mathbf{w}| = 22 \leq  \norm{\mathbf{v}} \norm{\mathbf{w}} = \sqrt{1500}.
$$

:::

With this inequality established, the Triangle Inequality
{eq}`Item:Prop:InnerProduct:TriangleInequality` is easily proved. Let's repeat it, and prove it.

:::{prf:theorem}
:label: Thm:InnerProduct:TriangleInequality

For any two vectors in $\mathbb{R}^n$,

$$

    \norm{\mathbf{v}+\mathbf{w}} \leq \norm{\mathbf{v}}+\norm{\mathbf{w}}.
$$

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Thm:InnerProduct:TriangleInequality`
:class: tudproof

Since all terms involved are non-negative we may as well show that the inequality holds for the squares:

$$

  \begin{array}{l}
  \norm{\mathbf{v}+\mathbf{w}}^2 \leq (\norm{\mathbf{v}}+\norm{\mathbf{w}})^2 \\
    \iff (\mathbf{v}+\mathbf{w})\ip(\mathbf{v}+\mathbf{w}) \leq \norm{\mathbf{v}}^2 + 2\norm{\mathbf{v}}\norm{\mathbf{w}} + \norm{\mathbf{w}}^2 \\
    \iff \mathbf{v}\ip\mathbf{v} + 2\mathbf{v}\ip\mathbf{w}+\mathbf{w}\ip\mathbf{w} \leq \norm{\mathbf{v}}^2 + 2\norm{\mathbf{v}}\norm{\mathbf{w}} + \norm{\mathbf{w}}^2 \\
    \iff 2\,\mathbf{v}\ip\mathbf{w} \leq 2\norm{\mathbf{v}}\norm{\mathbf{w}}
  \end{array}
$$

and this, apart from the factor 2, is the Cauchy-Schwarz Inequality.

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

 \norm{\mathbf{v}} + \norm{\mathbf{w}} = \sqrt{14} + \sqrt{35} \approx 9.7 > \norm{\mathbf{v} + \mathbf{w}}.
$$

:::

(Subsec:InnerProduct:Angles_in_Rn)=

## Angles in $\mathbb{R}^n$

The first motivation to consider the dot product came from the question of perpendicularity of two vectors in the plane or in $\R^3$.
Perpendicularity of two vectors means that the angle between them is equal to $\frac12\pi$.
Below we will show that it is possible to express the angle between _any_ two (nonzero) vectors into dot products. And use this to define the concept of angle in a general space $\R^n$.

```{applet}
:url: dot_product/angleandprojection
:name: Fig:InnerProduct:AngleAndProjection
:fig: Images/Fig-InnerProduct-AngleAndProjection.svg
:class: dark-light

Angle between two vectors.
```

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

The angle between two nonzero vectors $\mathbf{v}$ and $\mathbf{w}$ is thus determined by dot products in the following way

$$

  \cos(\varphi) = \frac{\mathbf{w}\ip\mathbf{v}}{\norm{\mathbf{v}}\norm{\mathbf{w}}}.
$$

The value of $\varphi$ between $0$ and $\pi$ is then uniquely determined by

$$

  \varphi = \arccos\left(\frac{\mathbf{w}\ip\mathbf{v}}{\norm{\mathbf{v}}\norm{\mathbf{w}}}\right)= \cos^{-1}\left(\frac{\mathbf{w}\ip\mathbf{v}}{\norm{\mathbf{v}}\norm{\mathbf{w}}}\right).
$$

:::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:InnerProduct:DotProdGeometric`
:class: tudproof

We will derive formula {eq}`Eq:InnerProduct:GeometricDefinition`.
Assume that $\mathbf{v}$ and $\mathbf{w}$ are nonzero vectors.
Recall the formula of the orthogonal projection of $\mathbf{w}$ onto $\mathbf{v}$,

$$

  \mathbf{\hat{w}} = \dfrac{\mathbf{w}\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}}\mathbf{v}.
$$

Let $\varphi \in[0,\pi]$ denote the angle between two nonzero vectors $\mathbf{v}$ and $\mathbf{w}$.

From {numref}`Figure %s <Fig:InnerProduct:AngleAndProjection>` it is clear that the factor

$$
   \dfrac{\mathbf{w}\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}}
$$

is positive if the angle is acute, zero if the angle is right, and negative if the angle is obtuse.

In the case of an acute angle, by considering the right triangle $\Delta OAB$, where $A$ is the end point of $\mathbf{\hat{w}}$ and $B$ is the end point of $\mathbf{w}$, we see that on the one hand

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

\mathbf{w}\ip\mathbf{v} = \norm{\mathbf{v}}\norm{\mathbf{w}}\cos(\varphi).

:::

In the case of an obtuse angle, we use that the projection of $\mathbf{w}$ onto $\mathbf{v}$ is equal to the projection
of $\mathbf{w}$ onto $-\mathbf{v}$, as it is in fact the projection onto the line consisting of all multiples of $\mathbf{v}$. Now look at the picture on the right of {numref}`Figure %s <Fig:InnerProduct:AngleAndProjection>`
. There you see that $\mathbf{w}$ and
$-\mathbf{v}$ make an acute angle $\psi = \pi - \varphi$, so we can apply
Equation {eq}`Eq:InnerProduct:GeometricInterpretation` to $\mathbf{w}$ and $-\mathbf{v}$:

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

Note that the absolute value of the expression

$$
 \norm{\mathbf{w}}\cos(\varphi)
$$

is the length of the orthogonal projection of $\vect{w}$ onto $\vect{v}$.

::::

:::{prf:example}
:label: Ex:InnerProduct:AnglesInMethaneMolecule

In a methane molecule $\ce{CH_4}$ the four $\ce{H}$-atoms are positioned in a perfectly symmetrical way around the $\ce{C}$-atom.
We can model this as follows:
put the $\ce{C}$-atom at the origin of $\mathbb{R}^3$, and the $\ce{H}$-atoms at the positions/vectors

$$
  \mathbf{v}_1 = \begin{bmatrix}1 \\ 1 \\ 1   \end{bmatrix}, \quad
  \mathbf{v}_2 = \begin{bmatrix}-1 \\ -1 \\ 1   \end{bmatrix}, \quad
  \mathbf{v}_3 = \begin{bmatrix}-1 \\ 1 \\ -1   \end{bmatrix} \quad \text{and} \quad
  \mathbf{v}_4 = \begin{bmatrix}1 \\ -1 \\ -1   \end{bmatrix}.
$$

Then all four points have the same distance $\sqrt{3}$ to the origin, and all points have the same distance to each other, namely

$$
    \norm{\vect{v}_i - \vect{v}_j} = \sqrt{2^2 + 2^2 + 0^2} = \sqrt{8}, \text{ for } i \neq j.
$$

The angle between, for instance, $\mathbf{v}_1$ and $\mathbf{v}_3$ is determined by

$$
   \cos(\varphi) = \dfrac{\mathbf{v}_1\ip\mathbf{v}_3}{\norm{\mathbf{v}_1}\norm{\mathbf{v}_3}} = \dfrac{-1}{\sqrt{3}\cdot\sqrt{3}} = -\frac13.
$$

So

$$
  \varphi = \arccos(-\tfrac13) \approx  1.9106 \approx 109.47^{o}.
$$

:::

Since we have defined the dot product and the norm in $\mathbb{R}^n$, we can use the last formula to also define the angle between two vectors in $\mathbb{R}^n$.

:::{prf:definition}
:label: Dfn:InnerProduct:AngleInRn

For two nonzero vectors $\mathbf{v}$ and $\mathbf{w}$ in $\mathbb{R}^n$, the **angle** between the vectors is defined as

$$

   \varphi = \angle(\mathbf{v},\mathbf{w}) =  \arccos\left(\dfrac{\mathbf{v}\ip\mathbf{w}}{\norm{\mathbf{v}} \norm{\mathbf{w}}} \right).
$$

This definition makes sense, since the Cauchy-Schwarz inequality ({prf:ref}`Thm:InnerProduct:Cauchy-Schwarz`)
implies

$$
    -1 \leq \dfrac{\mathbf{v}\ip\mathbf{w}}{\norm{\mathbf{v}}\,\norm{\mathbf{w}}} \leq 1.
$$

:::

Note that just as before in the plane and in three-dimensional space, for nonzero vectors $\mathbf{v}$ and $\mathbf{w}$ we have

$$

   \mathbf{v}\perp\mathbf{w} \iff \mathbf{v}\ip\mathbf{w}=0 \iff \dfrac{\mathbf{v}\ip\mathbf{w}}{\norm{\mathbf{v}}\,\norm{\mathbf{w}}}=0 \iff \varphi =
   \angle(\mathbf{v},\mathbf{w}) = \tfrac12\pi.
$$

:::{prf:example}
:label: Ex:InnerProduct:AngleInRn

Let $\mathbf{e_1}$ be the vector in $\mathbb{R}^n$ with first entry equal to 1 and all other entries equal to 0, and $\mathbf{v}$ be the vector with all entries equal to 1. We find the angle between $\mathbf{e}_1$ and $\mathbf{v}$ in all cases $n = 2, 3, 4,\ldots$

For each $n\geq2$ we write $\varphi_n = \angle(\mathbf{e}_1,\mathbf{v})$. Then

$$
 \cos(\varphi_n)  = \dfrac{\mathbf{e}_1\ip\mathbf{v}}{\norm{\mathbf{e}_1}\norm{\mathbf{v}}} = \dfrac{1}{\sqrt{n}}.
$$

So:

$$
  \varphi_n = \arccos(\tfrac{1}{\sqrt{n}}), \, n = 1,2,3,\ldots
$$

For $n=1$ we find $\cos(\varphi_1) = 1$, so $\varphi_1 = 0$, which makes sense, and for $n=2$, $\cos(\varphi_2) = \frac{1}{\sqrt{2}}$, so $\varphi_2 = \frac14\pi$, which you can check by a sketch in the plane.

For $n\geq3$ we don't get easy answers, but as $\frac{1}{\sqrt{n}} \downarrow 0$ when $n$ gets large,
we may conclude that for large $n$ in $\mathbb{R}^n$ the two vectors are 'almost' orthogonal.

:::

## Grasple Exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7bb32c8c-9a2e-49bd-85fa-b7d205949510?id=114535
:label: grasple_exercise_1_2_4
:dropdown:
:description: To compute dot products in $\R^2$, $\R^3$ and $\R^4$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7b49e0f5-ae8b-4e92-8878-665dc080b7ee?id=65601
:label: grasple_exercise_1_2_5
:dropdown:
:description: To find a vector orthogonal to a given vector in $\R^2$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c8b4eed4-179f-42ab-9ec9-07f66445c960?id=69482
:label: grasple_exercise_1_2_6
:dropdown:
:description: To find a vector orthogonal to two given vectors in $\R^2$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b5a4e1c0-92ca-4307-9eb0-25a3a5807fc7?id=62415
:label: grasple_exercise_1_2_7
:dropdown:
:description: To find a vector orthogonal to a given vector in $\R^3$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/34bbb9e1-207e-4c06-8686-1c32b3f3d0aa?id=78751
:label: grasple_exercise_1_2_8
:dropdown:
:description: To find a vector orthogonal to a given vector in $\R^4$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/30a7abfe-9d40-4faa-a848-83bd67e024a0?id=62406
:label: grasple_exercise_1_2_7
:dropdown:
:description: To compute the norms of vectors in $\R^2$, $\R^3$, $\R^4$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7dc339bb-fe79-4eb9-914c-ea1a7ca85a85?id=69737
:label: grasple_exercise_1_2_9
:dropdown:
:description: To find the norm of the 'all one' vector in $\mathbb{R}^n$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8de90b0e-e89a-49a6-aa63-1b1e39f6e98e?id=79262
:label: grasple_exercise_1_2_10
:dropdown:
:description: To find the distance between two vectors in $\mathbb{R}^4$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d4dd1154-a3ec-497e-bc73-1cd96529f0e7?id=69741
:label: grasple_exercise_1_2_11
:dropdown:
:description: Find $h$ such that the distance between two points has a given value $d$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c2242315-7e4f-463b-b3cf-09e9e15c8b2b?id=69739
:label: grasple_exercise_1_2_12
:dropdown:
:description: To find a unit vector on a given line through $(0,0)$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/67334454-d109-45a2-b640-545041ff896d?id=62416
:label: grasple_exercise_1_2_13
:dropdown:
:description: Find $\text{proj}_{\mathbf{v}}(\mathbf{w})$ in $\R^2$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9705b078-6c91-42c6-9768-8a043115b881?id=62658
:label: grasple_exercise_1_2_14
:dropdown:
:description: Find $\text{proj}_{\mathbf{v}}(\mathbf{w})$ in $\R^4$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/531d3be2-dd62-4c21-b023-70e0b63809be?id=78747
:label: grasple_exercise_1_2_15
:dropdown:
:description: Regarding norm and orthogonality of $\vect{u}$, $\vect{v}$, $\vect{u}-\vect{v}$ and $\vect{u}+\vect{v}$.

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c4d2743f-5f14-4812-9531-1a40c28c15cb?id=62413
:label: grasple_exercise_1_2_17
:dropdown:
:description: To prove that &nbsp;$(\vect{v}+\vect{w})\ip\vect{x} = \vect{v}\ip\vect{x}+\vect{w}\ip\vect{x}$.

::::

% swapped with previous;  27-02-2025

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/161ecdf6-4cfb-41ba-bc16-685fe8532471?id=62414
:label: grasple_exercise_1_2_16
:dropdown:
:description: To show that &nbsp;$(\vect{v}+\vect{w})\ip(\vect{v}-\vect{w}) = \norm{\vect{v}}^2 - \norm{\vect{w}}^2$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/407cb45d-2baf-4b0d-a1eb-6e51186e19f3?id=69738
:label: grasple_exercise_1_2_18
:dropdown:
:description: What to conclude from &nbsp;$\norm{\vect{v}+\vect{w}} = \norm{\vect{v}}+\norm{\vect{w}}$?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c4c1c609-b1dd-4588-865f-53d7e8221f88?id=62689
:label: grasple_exercise_1_2_19
:dropdown:
:description: To prove that $-1 \leq \dfrac{\vect{u}\ip\vect{v}}{\norm{\vect{u}} \norm{\vect{v}}} \leq  1$.
::::


::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2a2423c3-0907-40b7-bd5f-7607baf7cc09?id=62668
:label: grasple_exercise_1_2_20
:dropdown:
:description: What to conclude from $\text{proj}_{\mathbf{v}}(\mathbf{w}_1 ) = \text{proj}_{\mathbf{v}}(\mathbf{w}_2)$?

::::
