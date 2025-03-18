(Sec:LinearCombinations)=

# Linear Combinations

::::{prf:definition}

Let $\mathbf{v}_1, \ldots, \mathbf{v}_n$ be vectors in $\mathbb{R}^m$. Any expression of the form

$$
x_1 \mathbf{v}_1+\cdots+x_n \mathbf{v}_n,
$$

where $x_1, \ldots, x_n$ are real numbers, is called a **linear combination** of the vectors $\mathbf{v}_1, \ldots, \mathbf{v}_n$.

::::

::::{prf:example}

The vectors $\mathbf{v}_1$ and $\mathbf{v}_2$ are two vectors in the plane $\mathbb{R}^2$. As we can see in {numref}`Figure  %s <Fig:LinearCombinations:LinearCombinations>`, the vector $\mathbf{u}$ is a linear combination of $\mathbf{v}_1$ and $\mathbf{v}_2$ since it can be written as $\mathbf{u}=2\mathbf{v}_1+\mathbf{v}_2$. The vector $\mathbf{w}$ is a linear combination of these two vectors as well. It can be written as $\mathbf{w}=-3\mathbf{v}_1+2\mathbf{v}_2$.

```{applet}
:url: linear_combinations/linearcombinations
:fig: Images/Fig-LinearCombinations-LinComb.svg
:name: Fig:LinearCombinations:LinearCombinations
:status: approved
:class: dark-light

Linear combinations of vectors in the plane.
```

::::

If we want to determine whether a given vector is a linear combination of other vectors, then we can do that using systems of equations.

::::{prf:example}

$$
\mathbf{v}_1=
\begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} \quad \mathbf{v}_2=
\begin{bmatrix} 3 \\ 1 \\ 2 \end{bmatrix} \quad \mathbf{b}=
\begin{bmatrix} -1 \\ 3 \\ 0 \end{bmatrix}
$$

Is the vector $\mathbf{b}$ a linear combination of $\mathbf{v}_1$ and $\mathbf{v}_2$? We can use the definition of a linear combination to solve this problem. If $\mathbf{b}$ is in fact a linear combination of the two other vectors, then it can be written as $x_1 \mathbf{v}_1+x_2 \mathbf{v}_2$. This means that we should verify whether the system of equations $x_1 \mathbf{v}_1+x_2 \mathbf{v}_2=\mathbf{b}$ has a solution.

The equation

$$
x_1
\begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix}+x_2
\begin{bmatrix} 3 \\ 1 \\ 2 \end{bmatrix}=
\begin{bmatrix} -1 \\ 3 \\ 0 \end{bmatrix}
$$

is equivalent to the system

$$
\left\{\begin{array}{l} x_1+3x_2=-1 \\ 2x_1+x_2=3 \\ x_1+2x_2=0\end{array} \right.
$$

The augmented matrix of this system of equations is equal to

$$
\left[\begin{array}{cc|c} 1 & 3 & -1 \\ 2 & 1 & 3 \\ 1 & 2 & 0 \end{array}\right]
$$

and its reduced echelon form is equal to

$$
\left[\begin{array}{cc|c} 1 & 0 & 2 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{array}\right].
$$

This means that $\mathbf{b}$ is indeed a linear combination of $\mathbf{v}_1$ and $\mathbf{v}_2$.

$$
2
\begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix}-
\begin{bmatrix} 3 \\ 1 \\ 2 \end{bmatrix}=
\begin{bmatrix} -1 \\ 3 \\ 0 \end{bmatrix}
$$

We have found that $\mathbf{b}$ can be written as $2\mathbf{v}_1-\mathbf{v_2}$.

::::

::::{prf:example}

$$
\mathbf{v}_1=
\begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix} \quad \mathbf{v}_2=
\begin{bmatrix} 3 \\ 0 \\ 1 \end{bmatrix} \quad \mathbf{b}=
\begin{bmatrix} 2 \\ 1 \\ 1 \end{bmatrix}
$$

In this case it is a lot easier to decide whether $\mathbf{b}$ is a linear combination of $\mathbf{v}_1$ and $\mathbf{v}_2$. Since the second component of both $\mathbf{v}_1$ and $\mathbf{v}_2$ is equal to zero, we know that the second component of each linear combination of those vectors will be zero. This means that $\mathbf{b}$ can never be a linear combination of $\mathbf{v}_1$ and $\mathbf{v}_2$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ac63b286-09e1-46e5-91fc-952b54436293?id=78560
:label: grasple_exercise_2_2_A
:dropdown:
:description: Expressing a vector as a linear combination of other vectors.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/bd263ac1-b906-48dc-a898-d959254d9681?id=70163
:label: grasple_exercise_2_2_B
:dropdown:
:description: Expressing a vector as a linear combination of other vectors.

::::

## Span

In linear algebra it is often important to know whether each vector in $\mathbb{R}^n$ can be written as a linear combination of a set of given vectors. In order to investigate when it is possible to write any given vector as a linear combination of a set of given vectors we introduce the notion of a **span**.

::::{prf:definition}
:label: Dfn:LinearCombinations:Span

Let $S$ be a set of vectors. The set of all linear combinations $a_1\mathbf{v}_1+a_2\mathbf{v}_2+ \cdots +a_k \mathbf{v}_k$, where $\mathbf{v}_1, \ldots, \mathbf{v}_k$ are vectors in $S$, will be called the **span** of those vectors and will be denoted as $\Span{S}$.

When $S$ is equal to a finite set $\{\mathbf{v}_1, \ldots, \mathbf{v}_k\}$, then we will simply write $\Span{\mathbf{v}_1, \ldots, \mathbf{v}_k}$.

The span of an empty collection of vectors will be defined as the set that only contains the zero vector $\mathbf{0}$.

::::

::::{prf:remark}

The collection $\Span{\mathbf{v}_1, \ldots, \mathbf{v}_k}$ always contains all of the vectors $\mathbf{v}_1, \ldots, \mathbf{v}_k$. This is true since each vector $\mathbf{v}_i$ can be written as the linear combination

$$
  0\mathbf{v}_1+\cdots+1\mathbf{v}_i+\cdots +0\mathbf{v}_k.
$$

Moreover, the span of any set of vectors always contains the zero vector. Whatever set of vectors we start with, we can always write

$$
   \mathbf{0}=0\mathbf{v}_1+0\mathbf{v}_2+\cdots +0\mathbf{v}_k.
$$

::::

The following examples will give us a bit of an idea what spans look like.

::::{prf:example}
:label: Ex:LinearCombinations:SpanOfOneVector

What does the span of a single non-zero vector look like? A linear combination of a vector $\mathbf{v}$ is of the form $x\mathbf{v}$, where $x$ is some real number. Linear combinations of a single vector $\mathbf{v}$ are thus just multiples of that vector. This means that $\Span{\mathbf{v}}$ is simply the collection of all vectors on the line through the origin and with directional vector $\mathbf{v}$ as we can see in {numref}`Figure  %s <Fig:LinearCombinations:SpanOneVectors>`.

```{applet}
:url: linear_combinations/span_one
:fig: Images/Fig-LinearCombinations-SpanOne.svg
:name: Fig:LinearCombinations:SpanOneVectors
:status: approved
:class: dark-light

The span of a single non-zero vector.
```

::::

::::{prf:example}
:label: Ex:LinearCombinations:SpanOfTwoVectors

Let $\mathbf{u}$ and $\mathbf{v}$ be two non-zero vectors in $\mathbb{R}^3$, as depicted in {numref}`Figure  %s <Fig:LinearCombinations:SpanTwoVectors>`. What does the span of these vectors look like? By definition, $\Span{\mathbf{u}, \mathbf{v}}$ contains all linear combinations of $\mathbf{u}$ and $\mathbf{v}$. Each of these linear combinations is of the form

$$
x_1\mathbf{u}+x_2\mathbf{v} \quad \textrm{$x_1$, $x_2$ in $\mathbb{R}$}.
$$

This looks like the parametric vector equation of a plane. Since the span must contain the zero vector we find that we obtain a plane through the origin like in {numref}`Figure  %s <Fig:LinearCombinations:SpanTwoVectors>`.

```{applet}
:url: linear_combinations/span_two_plane
:fig: Images/Fig-LinearCombinations-SpanTwoPlane.svg
:name: Fig:LinearCombinations:SpanTwoVectors
:status: approved
:class: dark-light

The span of two non-zero, non-parallel vectors.
```

::::

::::{prf:example}

The span of two non-zero vectors does not need to be a plane through the origin. If $\mathbf{u}$ and $\mathbf{v}$ are parallel, as in {numref}`Figure  %s <Fig:LinearCombinations:SpanTwoParallelVectors>`, then the span is actually a line through the origin.

```{applet}
:url: linear_combinations/span_two_line
:fig: Images/Fig-LinearCombinations-SpanTwoLine.svg
:name: Fig:LinearCombinations:SpanTwoParallelVectors
:status: approved
:class: dark-light

The span of two non-zero, parallel vectors.
```

If two non-zero vectors $\mathbf{u}$ and $\mathbf{v}$ are parallel, then $\mathbf{v}$ can be written as a multiple of $\mathbf{u}$. Assume for example that $\mathbf{v}=2\mathbf{u}$. Any linear combination $x_1\mathbf{u}+x_2\mathbf{v}$ can then be written as $x_1\mathbf{u}+2x_2\mathbf{u}$ or $(x_1+2x_2)\mathbf{u}$. This means that in this case each vector in the span of $\mathbf{u}$ and $\mathbf{v}$ is a multiple of $\mathbf{u}$. Therefore, the span will be a line through the origin.

::::

::::{prf:example}

If we start with three non-zero vectors in $\mathbb{R}^3$, then the resulting span may take on different forms. The span of the three vectors in {numref}`Figure  %s <Fig:LinearCombinations:SpanThreeVectors1>`, for example, is equal to the entire space $\mathbb{R}^3$. In {numref}`Sec:BasisDim` we will see why this is the case.


```{applet}
:url: linear_combinations/span_three
:fig: Images/Fig-LinearCombinations-SpanThreeR3.svg
:name: Fig:LinearCombinations:SpanThreeVectors1
:status: approved
:class: dark-light

The span of three vectors.
```

On the other hand, if we start with the three vectors that you can see in {numref}`Figure  %s <Fig:LinearCombinations:SpanThreeVectors2>`, then the span is equal to a plane through the origin.

```{applet}
:url: linear_combinations/span_three_plane
:fig: Images/Fig-LinearCombinations-SpanThreePlane.svg
:name: Fig:LinearCombinations:SpanThreeVectors2
:status: approved
:class: dark-light

The span of three vectors lying in the same plane.
```

There is also a possibility where the span of three non-zero vectors in $\mathbb{R}^3$ is equal to a line through the origin. Can you figure out when this happens?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/676d672c-74fc-4545-99ba-6b308af566ce?id=78542
:label: grasple_exercise_2_2_C
:dropdown:
:description: Interpretation of Span$\{\vect{v}_1,\vect{v}_2,\vect{v}_3\}$.

::::

We will now look at a very specific set of vectors in $\mathbb{R}^n$ of which the span is always the entire space $\mathbb{R}^n$.

::::{prf:definition}

Suppose we are working in $\mathbb{R}^n$. Let $\mathbf{e}_k$ be the vector of which all components are equal to 0, with the exception that the entry on place $k$ is equal to 1. The vectors $(\mathbf{e}_1, \ldots, \mathbf{e}_n)$ will be called the **standard basis** of $\mathbb{R}^n$.

::::

::::{prf:example}

The following vectors form the standard basis for $\mathbb{R}^2$.

$$
\mathbf{e}_1=
\begin{bmatrix} 1 \\ 0 \end{bmatrix} \quad \mathbf{e}_2=
\begin{bmatrix} 0 \\ 1 \end{bmatrix} \nonumber
$$

Each vector $\mathbf{v}$ can be written as a linear combination of the vectors $\mathbf{e}_1$ and $\mathbf{e}_2$ in a unique way. Later on we will call each collection of vectors with this property a **basis** for $\mathbb{R}^2$. If

$$
\mathbf{v}=
\begin{bmatrix} a \\ b \end{bmatrix}, \nonumber
$$

then clearly we have that

$$
\mathbf{v}=a
\begin{bmatrix} 1 \\ 0 \end{bmatrix}+b
\begin{bmatrix} 0 \\ 1 \end{bmatrix}. \nonumber
$$

It is easy to see that this is the only linear combination of $\mathbf{e}_1$ and $\mathbf{e}_2$ that is equal to $\mathbf{v}$.

::::

::::{prf:example}

The three vectors below form the standard basis for $\mathbb{R}^3$.

$$
\mathbf{e}_1=
\begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} \quad \mathbf{e}_2=
\begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix} \quad \mathbf{e}_3=
\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix} \nonumber
$$

Here too, it is true that each vector in $\mathbb{R}^3$ can be written as a unique linear combination of these three vectors.

::::

::::{prf:proposition}
:label: Prop:LinearCombinations:SpanStandardBasis

If $(\mathbf{e}_1, \ldots, \mathbf{e}_n)$ is the standard basis for $\mathbb{R}^n$, then $\Span{\mathbf{e}_1, \ldots, \mathbf{e}_n}$ is equal to $\mathbb{R}^n$.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:LinearCombinations:SpanStandardBasis`
:class: tudproof

Take an arbitrary vector $\mathbf{v}$ in $\mathbb{R}^n$ with

$$
\mathbf{v}=
\begin{bmatrix} a_1 \\ \vdots \\ a_n \end{bmatrix}.\nonumber
$$

The vector $\mathbf{v}$ can be written as

\begin{align*}
\mathbf{v} &= a_1
\begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix}+a_2
\begin{bmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{bmatrix}+ \ldots a_n
\begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix} \\
&= a_n\mathbf{e}_1+a_2\mathbf{e}_2+\ldots +a_n\mathbf{e}_n.
\end{align*}

This means that $\mathbf{v}$ is in the span of $\mathbf{e}_1, \ldots, \mathbf{e}_n$.

On the other hand, each vector in $\Span{\mathbf{e}_1, \ldots, \mathbf{e}_n}$ is a linear combination of vectors in $\mathbb{R}^n$ and thus itself a vector in $\mathbb{R}^n$.

::::

In {prf:ref}`Prop:LinearCombinations:SpanStandardBasis` we saw that the span of the standard basis of $\mathbb{R}^n$ is equal to the entire space. In {numref}`Sec:MatVecProduct`, we will find out when, for an arbitrary set of vectors $\mathbf{v}_1, \ldots, \mathbf{v}_k$, the collection $\Span{\mathbf{v}_1, \ldots, \mathbf{v}_k}$ contains every vector in $\mathbb{R}^n$.

## Grasple Exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9c780d10-9a8f-4fd6-9471-3f1a0e46c009?id=70171
:label: grasple_exercise_2_2_1
:dropdown:
:description: Is $\vect{b}$ an element of Span$\{\vect{a}_1,\vect{a}_2,\vect{a}_3\}$?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f74168ff-a448-4420-88d9-ebe7365a00a9?id=70172
:label: grasple_exercise_2_2_2
:dropdown:
:description: Is $\vect{b}$ an element of Span$\{\vect{a}_1,\vect{a}_2,\vect{a}_3\}$?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b760d9b9-d0ba-4875-b828-397e7a045283?id=70175
:label: grasple_exercise_2_2_3
:dropdown:
:description: Generate your own linear combinations.

::::

% ------------------------------------------------

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a8175390-3844-408c-b192-c4b05f9beb7b?id=70170
:label: grasple_exercise_2_2_4
:dropdown:
:description: Is the span of two vectors always a plane?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fab5c526-91ed-407b-9faa-645f40c22b8b?id=70169
:label: grasple_exercise_2_2_5
:dropdown:
:description: Checking whether a vector is in the span of other vectors.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2167085c-2498-4694-9eac-abfeeb0ec307?id=70162
:label: grasple_exercise_2_2_6
:dropdown:
:description: About the interpretation of Span$\{\vect{a}_1,\vect{a}_2\}$.

::::

% ------------------------------------------------

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/493831d9-ab4a-4f78-b9ea-7b707aa9f4c2?id=70174
:label: grasple_exercise_2_2_7
:dropdown:
:description: Checking whether a vector is a linear combination of the columns of a matrix $A$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c008320d-9d0e-463f-8bb7-344988f10438?id=70176
:label: grasple_exercise_2_2_8
:dropdown:
:description: About the difference between $\{\vect{a}_1,\vect{a}_2,\vect{a}_3\}$ and Span$\{\vect{a}_1,\vect{a}_2,\vect{a}_3\}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b4f4dc1f-4f56-41e8-b16d-a2694e90890c?id=70181
:label: grasple_exercise_2_2_9
:dropdown:
:description: When do the columns of a matrix span all of $\R^m$?

::::

% ------------------------------------------------

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/45bc5527-e79b-4198-b6b7-9b3168d9d1ff?id=70182
:label: grasple_exercise_2_2_10
:dropdown:
:description: About removing vectors without reducing the span.

::::

% ------------------------------------------------

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7fcebe18-474c-4995-9c81-f1da7ab4cc5e?id=70360
:label: grasple_exercise_2_2_11
:dropdown:
:description: Conversion between vector equation and linear system.

::::
