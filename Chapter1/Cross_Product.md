(Sec:CrossProduct)=

# Cross Product

In this section we will look at a specific operation on vectors in $\mathbb{R}^3$. This operation is called the _cross product_ and it allows us to construct a vector that is orthogonal to two given vectors. We will use this operation in
{numref}`Section %s <SubSec:LinesAndPlanes:Plane>`
to construct a vector that is orthogonal to a given plane in $\mathbb{R}^3$. This will allow us to describe such a plane with a very simple equation.

## Definition and Basic Properties

::::{prf:definition}
:label: Def:CrossProduct:Crossproduct

Let $\mathbf{u}$ and $\mathbf{v}$ be vectors in $\mathbb{R}^3$ such that

$$
\mathbf{u}=\begin{bmatrix} a_1 \\ a_2 \\ a_3 \end{bmatrix} \textrm{ and } \mathbf{v}=\begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}.
$$

The _cross product_ $\mathbf{u} \cp \mathbf{v}$ is defined as

$$
\mathbf{u} \cp \mathbf{v} = \begin{bmatrix} a_2b_3-a_3b_2 \\ a_3b_1-a_1b_3 \\ a_1b_2-a_2b_1 \end{bmatrix}.
$$

::::

::::{prf:example}

Let us compute the cross product of the following vectors $\mathbf{u}$ and $\mathbf{v}$.

$$
\mathbf{u}=\begin{bmatrix} 2 \\ 1 \\ 4 \end{bmatrix} \textrm{ and } \mathbf{v}=\begin{bmatrix} 3 \\ 6 \\ 5 \end{bmatrix}.
$$

From the definition we obtain that $\mathbf{u}\cp \mathbf{v}$ is equal to

$$
\begin{bmatrix} 1\cdot 5-4\cdot 6 \\ 4\cdot 3-2\cdot 5 \\ 2\cdot 6-1\cdot 3 \end{bmatrix}=\begin{bmatrix} -19 \\ 2 \\ 9 \end{bmatrix}.
$$

You may notice something peculiar here. The vector $\mathbf{u} \cp \mathbf{v}$ is orthogonal to both $\mathbf{u}$ and $\mathbf{v}$. Indeed, the dot product of $\mathbf{u} \cp \mathbf{v}$ and $\mathbf{u}$ is equal to $(-19)\cdot 2+2\cdot 1+9\cdot 4=-38+2+36=0$ and the dot product $\mathbf{u} \cp \mathbf{v}$ and $\mathbf{v}$ is equal to $(-19)\cdot 3+2\cdot 6+9\cdot 5=-57+12+45=0$.
This is no coincidence, as we will see in {prf:ref}`Prop:CrossProduct:Cportho`.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c5058abb-3d5b-4e8c-b836-40aeff08a301?id=65634
:label: grasple_exercise_1_3_A
:dropdown:
:description: Just to compute a cross product.

::::

The definition of the cross product does not give us a lot of information about the properties of this vector. We already know that a vector is defined by a direction and a length. Let us try to determine the direction and the length of the cross product of two vectors. We will start with the direction.

::::{prf:proposition}
:label: Prop:CrossProduct:Cportho

If $\mathbf{u}$ and $\mathbf{v}$ are vectors in $\mathbb{R}^3$, then $\mathbf{u} \cp \mathbf{v}$ is orthogonal to both $\mathbf{u}$ and $\mathbf{v}$.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:CrossProduct:Cportho`
:class: tudproof

Let $\mathbf{u}$ and $\mathbf{v}$ be vectors in $\mathbb{R}^3$ such that

$$
\mathbf{u}=\begin{bmatrix} a_1 \\ a_2 \\ a_3 \end{bmatrix} \textrm{ and } \mathbf{v}=\begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}.
$$

To establish that $\mathbf{u} \cp \mathbf{v}$ and $\mathbf{u}$ are orthogonal we need to show that their dot product is equal to zero. The dot product of these vectors is equal to

$$
\begin{align*}
(\mathbf{u} \cp \mathbf{v}) \ip \mathbf{u} &= (a_2b_3-a_3b_2)\cdot a_1+(a_3b_1-a_1b_3)\cdot a_2+(a_1b_2-a_2b_1)\cdot a_3 \\
&= a_2b_3a_1-a_3b_2a_1+a_3b_1a_2-a_1b_3a_2+a_1b_2a_3-a_2b_1a_3 \\
&= 0.
\end{align*}
$$

In a similar way we can prove that the dot product of $\mathbf{u} \cp \mathbf{v}$ and $\mathbf{v}$ is equal to zero.

::::

Knowing that the cross product of two vectors is orthogonal to these vectors does not give us all we need to know about the direction of the cross product. There are two opposite directions that are both orthogonal to two given non-parallel vectors. We can determine the correct direction of the cross product $\mathbf{u}\cp \mathbf{v}$ using the _right-hand rule_.

::::{figure} Images/Fig-CrossProduct-Righthandrule.svg
:name: Fig:CrossProduct:RightHandRule
:class: dark-light-same

The right-hand rule. Adapted from Acdx, CC BY-SA 3.0 http://creativecommons.org/licenses/by-sa/3.0/, via Wikimedia Commons.
::::

If we take our right hand, point our index finger in the direction of $\mathbf{u}$ and our middle finger in the direction of $\mathbf{v}$, as depicted in {numref}`Figure %s <Fig:CrossProduct:RightHandRule>`, then the cross product $\mathbf{u}\cp \mathbf{v}$ points in the direction of our thumb.

So far we have established what the direction is of $\mathbf{u}\cp \mathbf{v}$. Now we will take a look at its length.

::::{prf:proposition}
:label: Prop:CrossProduct:NormCrossProduct

If $\mathbf{u}$ and $\mathbf{v}$ are vectors in $\mathbb{R}^3$, then

$$
\norm{\mathbf{u} \cp \mathbf{v}}=\norm{\mathbf{u}} \norm{\mathbf{v}} |\sin(\theta)|,
$$

where $\theta$ is the angle between $\mathbf{u}$ and $\mathbf{v}$.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:CrossProduct:NormCrossProduct`
:class: tudproof

Let $\mathbf{u}$ and $\mathbf{v}$ be vectors in $\mathbb{R}^3$ such that

$$
\mathbf{u}=\begin{bmatrix} a_1 \\ a_2 \\ a_3 \end{bmatrix} \textrm{ and } \mathbf{v}=\begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}.
$$

To avoid having to work with square roots we first compute $\norm{\mathbf{u}\cp \mathbf{v}}^2$.

$$
\begin{align*}
\norm{\mathbf{u}\cp \mathbf{v}}^2 &= (a_2b_3-a_3b_2)^2+(a_3b_1-a_1b_3)^2+(a_1b_2-a_2b_1)^2 \\
&= (a^2_2b^2_3-2a_2b_3a_3b_2+a^2_3b^2_2)+(a^2_3b^2_1-2a_3b_1a_1b_3+a^2_1b^2_3)+(a^2_1b^2_2-2a_1b_2a_2b_1+a^2_2b^2_1)\\
&= (a^2_1+a^2_2+a^2_3)(b^2_1+b^2_2+b^2_3)-(a_1b_1+a_2b_2+a_3b_3)^2 \\
&= \norm{\mathbf{u}}^2 \norm{\mathbf{v}}^2-(\mathbf{u} \ip \mathbf{v})^2 \\
&= \norm{\mathbf{u}}^2 \norm{\mathbf{v}}^2-( \norm{\mathbf{u}} \norm{\mathbf{v}} \cos(\theta))^2 \\
&= \norm{\mathbf{u}}^2 \norm{\mathbf{v}}^2 (1-(\cos(\theta))^2) \\
&= \norm{\mathbf{u}}^2 \norm{\mathbf{v}}^2 (\sin(\theta))^2.
\end{align*}
$$

If we now take the square root of both sides of the equation we find

$$
\norm{\mathbf{u} \cp \mathbf{v}}=\norm{\mathbf{u}} \norm{\mathbf{v}} |\sin(\theta)|,
$$

since $\sqrt{(\sin(\theta))^2}=|\sin(\theta)|$.

::::

Notice some similarities between the formula for the length of the cross product and a formula that we saw in the Section [](./Inner_Product.md). There we encountered the equality $\mathbf{u}\ip\mathbf{v} = \norm{\mathbf{u}}\norm{\mathbf{v}} \cos(\theta)$, where $\theta$ was the angle between $\mathbf{u}$ and $\mathbf{v}$.

## Geometrical Properties of the Cross Product

We can derive some interesting geometrical results from {prf:ref}`Prop:CrossProduct:NormCrossProduct`.

::::{prf:proposition}
:label: Prop:CrossProduct:Parallel

Two non-zero vectors $\mathbf{u}$ and $\mathbf{v}$ are parallel if and only if $\mathbf{u}\cp \mathbf{v}=\mathbf{0}$.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:CrossProduct:Parallel`
:class: tudproof

Let $\mathbf{u}$ and $\mathbf{v}$ be two non-zero vectors. First of all, the vector $\mathbf{u}\cp \mathbf{v}$ is equal to the zero vector if and only if $\norm{\mathbf{u} \cp \mathbf{v}}=0$. Since $\norm{\mathbf{u}}$ and $\norm{\mathbf{v}}$ are both not equal to zero, it follows from {prf:ref}`Prop:CrossProduct:NormCrossProduct` that $\norm{\mathbf{u} \cp \mathbf{v}}=0$ if and only if $\sin(\theta)=0$, where $\theta$ is the angle between the vectors. This means that $\mathbf{u}\cp \mathbf{v}=\mathbf{0}$ if and only if $\theta$ is equal to either $0$ or $\pi$, which is equivalent to saying that $\mathbf{u}$ and $\mathbf{v}$ have the same direction or the opposite direction. In both cases the vectors are parallel.

::::

::::{prf:proposition}
:label: Prop:CrossProduct:AreaParallelogram

If $\mathbf{u}$ and $\mathbf{v}$ are vectors in $\mathbb{R}^3$, then $\norm{\mathbf{u} \cp \mathbf{v}}$ is equal to the area of the parallelogram spanned by $\mathbf{u}$ and $\mathbf{v}$.

:::{figure} Images/Fig-CrossProduct-Area.svg
:name: Fig:CrossProduct:AreaParallelogram
:class: dark-light

Parallelogram spanned by two vectors.

:::

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:CrossProduct:AreaParallelogram`
:class: tudproof

The area of a parallelogram is equal to the product of the length of its base and its height. As we can see in {numref}`Figure %s <Fig:CrossProduct:AreaParallelogram>` the length of the base of the parallelogram is equal to $\norm{\mathbf{u}}$ and the height is equal to $\norm{\mathbf{h}}$. If we look at the right-angled triangle $OPP'$ we see that $\norm{\mathbf{h}}=\norm{\mathbf{v}}\sin{\theta}$. This means that the area of the parallelogram is equal to $\norm{\mathbf{u}} \norm{\mathbf{v}} \sin(\theta)$ (because we use an angle between $0$ and $\pi$ we can omit the absolute-value signs) and thus to $\norm{\mathbf{u} \cp \mathbf{v}}$.

::::

::::{prf:example}

What is the area of the parallelogram with vertices $(0,0,0)$, $(1,2,1)$, $(3,1,1)$ and $(4, 3, 2)$?

We will denote the points $(1,2,1)$, $(3,1,1)$ and $(4, 3, 2)$ as $P$, $Q$ and $R$ respectively. Because $\overrightarrow{OR}$ is equal to $\overrightarrow{OP}+\overrightarrow{OQ}$ we know that $\overrightarrow{OR}$ is a diagonal of the parallelogram and that $\overrightarrow{OP}$ and $\overrightarrow{OQ}$ are two edges with a common vertex.

This means that the area of the given parallelogram is equal to $\norm{\overrightarrow{OP}\cp \overrightarrow{OQ}}$. We find

$$
\overrightarrow{OP}\cp \overrightarrow{OQ}=
 \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} \cp \begin{bmatrix} 3 \\ 1 \\ 1 \end{bmatrix} =
\begin{bmatrix} 2\cdot 1-1\cdot 1 \\ 1\cdot 3-1\cdot 1 \\ 1\cdot 1-2\cdot 3 \end{bmatrix}=\begin{bmatrix} 1 \\ 2 \\ -5 \end{bmatrix}.
$$

Therefore, the area of the parallelogram is equal to

$$
\sqrt{1^2+2^2+(-5)^2}=\sqrt{30}.
$$

::::

::::{prf:example}

What is the area of the triangle with vertices $(2,1,0)$, $(2,2,2)$ and $(3, 1, 1)$? Let us denote these points as $P$, $Q$ and $R$ respectively. How can we use the cross product to determine the area of this triangle? In {numref}`Figure %s <Fig:CrossProduct:AreaTriangle>` we see that the area of the triangle is half the area of the parallelogram spanned by $\overrightarrow{PQ}$ and $\overrightarrow{PR}$, which is equal to $\norm{\overrightarrow{PQ}\cp\overrightarrow{PR}}$.

:::{figure} Images/Fig-CrossProduct-TrianglePQR.svg
:name: Fig:CrossProduct:AreaTriangle
:class: dark-light

Area of the triangle $PQR$.

:::

The vectors $\overrightarrow{PQ}$ and $\overrightarrow{PR}$ have the following entries.

$$
\overrightarrow{PQ}=\begin{bmatrix} 2-2 \\ 2-1 \\ 2-0 \end{bmatrix}=\begin{bmatrix} 0 \\ 1 \\ 2 \end{bmatrix}, \quad \overrightarrow{PR}=\begin{bmatrix} 3-2 \\ 1-1 \\ 1-0 \end{bmatrix}=\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}.
$$

The cross product of these two vectors is equal to

$$
\overrightarrow{PQ} \cp\overrightarrow{PR}=\begin{bmatrix} 1\cdot 1-2\cdot 0 \\ 2\cdot 1-0\cdot 1 \\ 0\cdot 0-1\cdot 1 \end{bmatrix}=\begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}.
$$

This means that the area of the given triangle is equal to

$$
\frac{1}{2}\norm{\overrightarrow{PQ} \cp\overrightarrow{PR}}=\frac{\sqrt{1^2+2^2+(-1)^2}}{2}=\frac{\sqrt{6}}{2}.
$$

::::

Finally, we will take a look at some algebraic properties of the cross product. Most of these are similar to the properties of the dot product, but there is one important difference. The cross product is not commutative. This means that $\mathbf{u}\cp \mathbf{v}$ is not necessarily equal to $\mathbf{v}\cp \mathbf{u}$.

::::{prf:proposition}
:label: Prop:CrossProduct:RulesCrossProduct

The following properties hold for all vectors $\mathbf{v_1}$, $\mathbf{v_2}$ and $\mathbf{v_3}$ in $\mathbb{R}^3$ and scalars $c$ in $\mathbb{R}$.

<ol type="i">
<li>

$\mathbf{v_1}\cp\mathbf{v_2} = -\mathbf{v_2}\cp\mathbf{v_1}$.

</li>
<li>

$(c\mathbf{v_1})\cp\mathbf{v_2} = c(\mathbf{v_1}\cp\mathbf{v_2}) = \mathbf{v_1}\cp(c \mathbf{v_2})$.

</li>
<li>

$(\mathbf{v_1}+\mathbf{v_2})\cp\mathbf{v_3} = \mathbf{v_1}\cp\mathbf{v_3}+\mathbf{v_2}\cp\mathbf{v_3}$.

</li>
</ol>

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:CrossProduct:RulesCrossProduct`
:class: tudproof

Let $\mathbf{v_1}$, $\mathbf{v_2}$ and $\mathbf{v_3}$ be vectors in $\mathbb{R}^3$ such that

$$
\mathbf{v_1}=\begin{bmatrix} a_1 \\ a_2 \\ a_3 \end{bmatrix} \quad \mathbf{v_2}=\begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix} \quad \mathbf{v_3}=\begin{bmatrix} c_1 \\ c_2 \\ c_3 \end{bmatrix}.
$$

i. Intuitively, this follows from the right-hand rule. If we switch our index and middle finger, then our thumb points in the opposite direction. This equality is easy to prove if we use the definition of the cross product and rearrange the components a little.

$$
  \begin{array}{rcccr}
    \mathbf{v_1}\cp\mathbf{v_2} &=& \begin{bmatrix} a_2b_3-a_3b_2 \\ a_3b_1-a_1b_3 \\ a_1b_2-a_2b_1 \end{bmatrix} &=&
\begin{bmatrix} -(a_3b_2-a_2b_3) \\ -(a_1b_3-a_3b_1) \\ -(a_2b_1-a_1b_2) \end{bmatrix} \\
&=& -\begin{bmatrix} a_3b_2-a_2b_3 \\ a_1b_3-a_3b_1 \\ a_2b_1-a_1b_2 \end{bmatrix}
&=& -\mathbf{v_2}\cp\mathbf{v_1}.
  \end{array}
$$

ii. Here too, we can use our intuition. We know that the length of the cross product is equal to the area of a parallelogram. If we make one side of the parallelogram $c$ times longer, then we multiply the area with a factor $c$ too. Using the definition of the cross product and factoring out the constant $c$ we find the following equalities.

$$
  \begin{array}{rcccr}
   (c\mathbf{v_1})\cp\mathbf{v_2} &=& \begin{bmatrix} (ca_2)b_3-(ca_3)b_2 \\ (ca_3)b_1-(ca_1)b_3 \\ (ca_1)b_2-(ca_2)b_1 \end{bmatrix}
&=& \begin{bmatrix} c(a_2b_3-a_3b_2) \\ c(a_3b_1-a_1b_3) \\ c(a_1b_2-a_2b_1) \end{bmatrix} \\
&=& c\begin{bmatrix} a_2b_3-a_3b_2 \\ a_3b_1-a_1b_3 \\ a_1b_2-a_2b_1 \end{bmatrix}
&=& c(\mathbf{v_1}\cp\mathbf{v_2})\\
&=& \begin{bmatrix} c(a_2b_3-a_3b_2) \\ c(a_3b_1-a_1b_3) \\ c(a_1b_2-a_2b_1) \end{bmatrix}
&=& \begin{bmatrix} a_2(cb_3)-a_3(cb_2) \\ a_3(cb_1)-a_1(cb_3) \\ a_1(cb_2)-a_2(cb_1) \end{bmatrix} \\
&=& \mathbf{v_1}\cp(c \mathbf{v_2}).
  \end{array}
$$

iii. This follows from the distributivity of the real numbers.

\begin{align*}
(\mathbf{v_1}+\mathbf{v_2})\cp \mathbf{v_3} &= \begin{bmatrix} (a_2+b_2)c_3-(a_3+b_3)c_2 \\ (a_3+b_3)c_1-(a_1+b_1)c_3 \\ (a_1+b_1)c_2-(a_2+b_2)c_1 \end{bmatrix} \\
&= \begin{bmatrix} a_2c_3+b_2c_3-a_3c_2-b_3c_2 \\ a_3c_1+b_3c_1-a_1c_3-b_1c_3 \\ a_1c_2+b_1c_2-a_2c_1-b_2c_1 \end{bmatrix} \\
&= \begin{bmatrix} a_2c_3-a_3c_2 \\ a_3c_1-a_1c_3 \\ a_1c_2-a_2c_1 \end{bmatrix}+\begin{bmatrix} b_2c_3-b_3c_2 \\ b_3c_1-b_1c_3 \\ b_1c_2-b_2c_1 \end{bmatrix} \\
&= \mathbf{v_1}\cp\mathbf{v_3}+\mathbf{v_2}\cp\mathbf{v_3}.
\end{align*}

::::

In {numref}`Chapter:Determinants` we will take a look at the determinant of a matrix. For $2 \times 2$ matrices the definition is as follows.

::::{prf:definition}
:label: Def:CrossProduct:2x2determinant

Let $a$, $b$, $c$ and $d$ be real numbers. The expression

$$
\begin{vmatrix} a & b \\ c & d  \end{vmatrix}
$$

is equal to the value $ad-bc$. Such an expression is called a _determinant_.

::::

The entries of the cross product of two vectors can also be computed using determinants.

::::{prf:proposition}
:label: Prop:CrossProduct:dets

Let $\mathbf{u}$ and $\mathbf{v}$ be vectors in $\mathbb{R}^3$ such that

$$
\mathbf{u}=\begin{bmatrix} a_1 \\ a_2 \\ a_3 \end{bmatrix} \textrm{ and } \mathbf{v}=\begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}.
$$

If

$$
\mathbf{u} \cp \mathbf{v} = \begin{bmatrix} x \\ y \\ z \end{bmatrix},
$$

then

$$
x=\begin{vmatrix} a_2 & b_2 \\ a_3 & b_3  \end{vmatrix}, \quad y=-\begin{vmatrix} a_1 & b_1 \\ a_3 & b_3  \end{vmatrix}, \quad z=\begin{vmatrix} a_1 & b_1 \\ a_2 & b_2  \end{vmatrix}.
$$

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:CrossProduct:dets`
:class: tudproof

This follows from the definition.

::::

::::{prf:example}

Let us compute the cross product of the following vectors $\mathbf{u}$ and $\mathbf{v}$ using determinants.

$$
\mathbf{u}=\begin{bmatrix} 2 \\ 3 \\ 2 \end{bmatrix} \textrm{ and } \mathbf{v}=\begin{bmatrix} 5 \\ 2 \\ 3 \end{bmatrix}.
$$

The first entry of $\mathbf{u} \cp \mathbf{v}$ is equal to

$$
\begin{vmatrix} 3 & 2 \\ 2 & 3 \end{vmatrix}=9-4=5.
$$

For the second entry we find

$$
-\begin{vmatrix} 2 & 5 \\ 2 & 3 \end{vmatrix}=-(6-10)=4.
$$

The last entry is equal to

$$
\begin{vmatrix} 2 & 5 \\ 3 & 2 \end{vmatrix}=4-15=-11.
$$

Therefore, we find that

$$
\mathbf{u} \cp \mathbf{v} = \begin{bmatrix} 5 \\ 4 \\ -11 \end{bmatrix}.
$$

::::

## Grasple Exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9c5285e7-3c47-4201-a22f-d4db7985b9fc?id=114534
:label: grasple_exercise_1_3_1
:dropdown:
:description: Just to compute $\vect{u}\times\vect{v}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/529702ff-6fc3-46ab-a148-7d93d081870b?id=63138
:label: grasple_exercise_1_3_2
:dropdown:
:description: Compute $\vect{u}\times\vect{v}$ and $\vect{v}\times\vect{u}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/48448d89-c286-45c5-9af4-780329a8821f?id=65637
:label: grasple_exercise_1_3_3
:dropdown:
:description: Compute $\vect{u}\times\vect{v}$ when $\vect{u}= c\vect{v}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f6c1bb4b-e63e-492e-910a-5a8c433de281?id=75093
:label: grasple_exercise_1_3_4
:dropdown:
:description: Cross product in $\R^4$?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/84b635e4-2278-4882-915d-6f8b253213a3?id=78749
:label: grasple_exercise_1_3_5
:dropdown:
:description: Find alle values of parameter $p$ for which either $\vect{u}\ip\vect{v}= 0$ or $\vect{u}\times\vect{v} = \vect{0}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6b660feb-fc36-47a0-bf86-e424d28edf6f?id=63354
:label: grasple_exercise_1_3_6
:dropdown:
:description: To compute the area of a paralellogram given by four points in $\R^3$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8a0fc383-dd10-4f31-931a-c62c0d650bd9?id=63479
:label: grasple_exercise_1_3_7
:dropdown:
:description: To compute the area of a triangle given by three points in $\R^3$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3e62cc2d-5860-43c2-b8aa-e54ab3a9a981?id=79268
:label: grasple_exercise_1_3_8
:dropdown:
:description: To compute and compare $(\vect{u}\times\vect{v})\times\vect{w}$ and $\vect{u}\times(\vect{v}\times\vect{w})$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/122013a2-1012-4203-99c7-ed5deafd82a4?id=78786
:label: grasple_exercise_1_3_9
:dropdown:
:description: What to conclude from $\vect{a}\ip\vect{c} = \vect{b}\ip\vect{c}$, from $\vect{a}\times\vect{c} = \vect{b}\times\vect{c}$, from both\,?

::::
