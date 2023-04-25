(Sec:LinearCombinations)=
# Linear combinations 

::::{prf:definition} 

Let $\mathbf{v}_1, \ldots, \mathbf{v}_n$ be vectors in $\mathbb{R}^m$. Any expression of the form 

$$
x_1 \mathbf{v_1}+\cdots+x_n \mathbf{v_n},
$$

where $x_1, \ldots, x_n$ are real numbers, is called a **linear combination** of the vectors $\mathbf{v}_1, \ldots, \mathbf{v}_n$.

::::


::::{prf:example} 

The vectors $\mathbf{v}_1$ and $\mathbf{v}_2$ are two vectors in the plane $\mathbb{R}^2$. As we can see in {numref}`Figure  %s <Fig:LinearCombinations:LinearCombinations>`, the vector $\mathbf{u}$ is a linear combination of $\mathbf{v}_1$ and $\mathbf{v}_2$ since it can be written as $\mathbf{u}=2\mathbf{v}_1+\mathbf{v}_2$. The vector $\mathbf{w}$ is a linear combination of these two vectors as well. It can be written as $\mathbf{w}=-3\mathbf{v}_1+2\mathbf{v}_2$.

:::{figure} Images/Fig-LinearCombinations-LinComb.svg
:name: Fig:LinearCombinations:LinearCombinations

Linear combinations of vectors in the plane.

:::

::::

If we want to determine whether a given vector is a linear combination of other vectors, then we can do that using systems of equations. 


::::{prf:example} 

$$
\mathbf{v_1}=
\begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix} \quad \mathbf{v_2}=
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
\mathbf{v_1}=
\begin{bmatrix} 1 \\ 0 \\ 2 \end{bmatrix} \quad \mathbf{v_2}=
\begin{bmatrix} 3 \\ 0 \\ 1 \end{bmatrix} \quad \mathbf{b}=
\begin{bmatrix} 2 \\ 1 \\ 1 \end{bmatrix}
$$

In this case it is a lot easier to decide whether $\mathbf{b}$ is a linear combination of $\mathbf{v}_1$ and $\mathbf{v}_2$. Since the second component of both $\mathbf{v}_1$ and $\mathbf{v}_2$ is equal to zero, we know that the second component of each linear combination of those vectors will be zero. This means that $\mathbf{b}$ can never be a linear combination of $\mathbf{v}_1$ and $\mathbf{v}_2$.

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

The collection $\Span{\mathbf{v}_1, \ldots, \mathbf{v}_k}$ always contains all of the vectors $\mathbf{v}_1, \ldots, \mathbf{v}_k$. This is true since each vector $\mathbf{v}_k$ can be written as the linear combination $0\mathbf{v}_1+\cdots+\mathbf{v}_k+\cdots +0\mathbf{v}_k$.

Moreover, the span of any set of vectors always contains the zero vector. Whatever set of vectors we start with, we can always write $\mathbf{0}=0\mathbf{v}_1+0\mathbf{v}_2+\cdots +0\mathbf{v}_k$.

::::

The following examples will give us a bit of an idea what spans look like.


::::{prf:example} 

What does the span of a single non-zero vector look like? A linear combination of a vector $\mathbf{v}$ is of the form $x\mathbf{v}$, where $x$ is some real number. Linear combinations of a single vector $\mathbf{v}$ are thus just multiples of that vector. This means that $\Span{\mathbf{v}}$ is simply the collection of all vectors on the line through the origin and with directional vector $\mathbf{v}$ as we can see in {numref}`Figure  %s <Fig:LinearCombinations:SpanOneVectors>`.

:::{figure} Images/Fig-LinearCombinations-SpanOne.svg
:name: Fig:LinearCombinations:SpanOneVectors

The span of a single non-zero vector.

:::

::::


::::{prf:example} 

Let $\mathbf{u}$ and $\mathbf{v}$ be two non-zero vectors in $\mathbb{R}^3$, as depicted in {numref}`Figure  %s <Fig:LinearCombinations:SpanTwoVectors>`. What does the span of these vectors look like? By definition, $\Span{\mathbf{u}, \mathbf{v}}$ contains all linear combinations of $\mathbf{u}$ and $\mathbf{v}$. Each of these linear combinations is of the form 


$$
x_1\mathbf{u}+x_2\mathbf{v} \quad \textrm{$x_1$, $x_2$ in $\mathbb{R}$}.
$$

This looks like the parametric vector equation of a plane. Since the span must contain the zero vector we find that we obtain a plane through the origin like in {numref}`Figure  %s <Fig:LinearCombinations:SpanTwoVectors>`.


:::{figure} Images/Fig-LinearCombinations-SpanTwoPlane.svg
:name: Fig:LinearCombinations:SpanTwoVectors

The span of two non-zero, non-parallel  vectors.

:::

::::


::::{prf:example} 



The span of two non-zero vectors does not need to be a plane through the origin. If $\mathbf{u}$ and $\mathbf{v}$ are parallel, as in {numref}`Figure  %s <Fig:LinearCombinations:SpanTwoParallelVectors>`, then the span is actually a line through the origin.

:::{figure} Images/Fig-LinearCombinations-SpanTwoLine.svg
:name: Fig:LinearCombinations:SpanTwoParallelVectors

The span of two non-zero, parallel vectors.

:::

If two non-zero vectors $\mathbf{u}$ and $\mathbf{v}$ are parallel, then $\mathbf{v}$ can be written as a multiple of $\mathbf{u}$. Assume for example that $\mathbf{v}=2\mathbf{u}$. Any linear combination $x_1\mathbf{u}+x_2\mathbf{v}$ can then be written as $x_1\mathbf{u}+2x_2\mathbf{u}$ or $(x_1+2x_2)\mathbf{u}$. This means that in this case each vector in the span of $\mathbf{u}$ and $\mathbf{v}$ is a multiple of $\mathbf{u}$. Therefore, the span will be a line through the origin.

::::


::::{prf:example} 

If we start with three non-zero vectors in $\mathbb{R}^3$, then the resulting span may take on different forms. The span of the three vectors in {numref}`Figure  %s <Fig:LinearCombinations:SpanThreeVectors1>`, for example, is equal to the entire space $\mathbb{R}^3$. In {numref}`Sec:BasisDim` we will see why this is the case.

:::{figure} Images/Fig-LinearCombinations-SpanThreeR3.svg
:name: Fig:LinearCombinations:SpanThreeVectors1

The span of three  vectors.

:::

On the other hand, if we start with the three vectors that you can see in {numref}`Figure  %s <Fig:LinearCombinations:SpanThreeVectors2>`, then the span is equal to a plane through the origin.

:::{figure} Images/Fig-LinearCombinations-SpanThreePlane.svg
:name: Fig:LinearCombinations:SpanThreeVectors2

The span of three  vectors lying in the same plane.

:::

There is also a possibility where the span of three non-zero vectors in $\mathbb{R}^3$ is equal to a line through the origin. Can you figure out when this happens?

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

::::{prf:proof} 

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
&= a_n\mathbf{e}_1+a_2\mathbf{v}_2+\ldots +a_n\mathbf{e}_n.
\end{align*}

This means that $\mathbf{v}$ is in the span of $\mathbf{e}_1, \ldots, \mathbf{e}_n$.

On the other hand, each vector in $\Span{\mathbf{e}_1, \ldots, \mathbf{e}_n}$ is a linear combination of vectors in $\mathbb{R}^n$ and thus itself a vector in $\mathbb{R}^n$.

::::

In {prf:ref}`Prop:LinearCombinations:SpanStandardBasis` we saw that the span of the standard basis of $\mathbb{R}^n$ is equal to the entire space. In what follows we will try to find out when, for an arbitrary set of vectors $\mathbf{v}_1, \ldots, \mathbf{v}_k$, the collection $\Span{\mathbf{v}_1, \ldots, \mathbf{v}_k}$ contains every vector in $\mathbb{R}^n$.


::::{prf:proposition} 
:label: Prop:LinearCombinations:SpanSolution

Let $\mathbf{v}_1, \ldots, \mathbf{v}_k$ be vectors in $\mathbb{R}^n$. Define the matrix $A$ such that 

$$
A=
\begin{bmatrix} \mathbf{v}_1 & \mathbf{v}_2 & \ldots & \mathbf{v}_k \end{bmatrix}.
$$

The collection $\Span{\mathbf{v}_1, \ldots, \mathbf{v}_k}$ is equal to $\mathbb{R}^n$ if and only if the equation $A \mathbf{x}=\mathbf{b}$ has a solution for each $\mathbf{b}$ in $\mathbb{R}^n$.

::::

::::{prf:proof} 

If $\Span{\mathbf{v}_1, \ldots, \mathbf{v}_k}$ is equal to $\mathbb{R}^n$, then each vector $\mathbf{b}$ is a vector in the span of the vectors $\mathbf{v}_1, \ldots, \mathbf{v}_k$. This means that we can write $\mathbf{b}$ as a linear combination 


$$
\mathbf{b}=x_1\mathbf{v}_1+ \ldots + x_k\mathbf{v}_k.
$$

Define the vector $\mathbf{x}$ such that 


$$
\mathbf{x}=
\begin{bmatrix} x_1 \\ \vdots \\ x_k \end{bmatrix}.
$$

By definition of the matrix-vector product we now have
\begin{align*}
A\mathbf{x} &= x_1\mathbf{v}_1+ \ldots + x_k\mathbf{v}_k \\
 &= \mathbf{b}
\end{align*}
The proof of the other implication is similar.

::::


::::{prf:proposition} 
:label: Prop:LinearCombinations:PivotInEachRow


The equation $A \mathbf{x}=\mathbf{b}$ has a solution for each $\mathbf{b}$ in $\mathbb{R}^n$ if and only if $A$ has a pivot position in each row.

::::

::::{prf:proof} 

Suppose that $A$ does not contain a pivot position in each row. By definition of the reduced echelon form we know that the last row of $A$ does not have a pivot position. If $E$ is the reduced echelon form of $A$, then this means that the bottom row of $E$ contains only zeros. Let $\mathbf{e}_n$ be again the vector of which the last entry is equal to 1 and all other entries are equal to zero.

Since $E$ is the reduced form of $A$ we can find a sequence of elementary row operations $R_1, \ldots , R_m$ that transform in $A$ into $E$. Now take the augmented matrix $[E \, | \, \mathbf{e}_n]$ and perform the row operations $R_m^{-1}, \ldots , R_1^{-1}$, where $R_i^{-1}$ is the inverse row operation of $R_i$. We obtain a matrix $[A \, | \, \mathbf{b}]$, where $\mathbf{b}$ is a vector in $R^n$. Because $[E \, | \, \mathbf{e}_n]$ is the reduced echelon form of the augmented matrix $[A \, | \, \mathbf{b}]$ and $[E \, | \, \mathbf{e}_n]$ has a pivot in the last column, we know that $[A \, | \, \mathbf{b}]$ is inconsistent. This means that $A\mathbf{x}=\mathbf{b}$ does not have a solution.

On the other hand, if we assume that $A\mathbf{x}=\mathbf{b}$ does not have a solution for some $\mathbf{b}$ in $\mathbb{R}^n$, then the reduced echelon form $[E \, | \, \mathbf{c}]$ of the augmented matrix $[A \, | \, \mathbf{b}]$ has a pivot in the last column. Let us assume that this pivot is located in row $m$. The matrix $E$ cannot have a pivot in row $m$, but $E$ is also the reduced echelon form of $A$. This means that $A$ has no pivot position in row $m$.

::::


::::{prf:proposition} 
:label: Prop:LinearCombinations:PivotSpanSolution


Let $\mathbf{v}_1, \ldots, \mathbf{v}_k$ be vectors in $\mathbb{R}^n$. Define the matrix $A$ such that 

$$
A=
\begin{bmatrix} \mathbf{v}_1 & \mathbf{v}_2 & \ldots & \mathbf{v}_k \end{bmatrix}.
$$


The following statements are equivalent: 

<ol type ="i">
<li>

The cset $\Span{\vect{v}_1, \ldots, \vect{v}_k}$ is equal to $\R^n$. 


</li>
<li>

The equation $A \vect{x}=\vect{b}$ has a solution for each $\vect{b}$ in $\R^n$.


</li>
<li>

The matrix $A$ has a pivot position in each row.


</li>
</ol>

::::


::::{prf:proof} 

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

The three given vectors span the entire space $\mathbb{R}^3$ if and only if the matrix $A$ has three pivot positions. Using elementary row operations we find that A has the following reduced echelon form. 


$$

A=
\begin{bmatrix} 1 & 0 & 3 \\ 1 & 1 & 5 \\ -1 & 1 & -1 \end{bmatrix}\sim 
\begin{bmatrix} 1 & 0 & 3 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{bmatrix}

$$

Since there are only two pivots in the reduced echelon form, we know that $\mathbf{v}_1$, $\mathbf{v}_2$ and $\mathbf{v}_3$ do not span the space $\mathbb{R}^3$.

::::


::::{prf:proposition} 

If $\mathbf{v}_1, \dots ,\mathbf{v}_k$ are vectors in $\mathbb{R}^n$ and $k<n$, then the span of $\mathbf{v}_1, \dots ,\mathbf{v}_k$ is not equal to $\mathbb{R}^n$.

::::

::::{prf:proof} 

Use the vectors $\mathbf{v}_1, \dots ,\mathbf{v}_k$ as the columns for a matrix $A$. By definition, the matrix $A$ is an $n\times k$ matrix. Let $E$ be the reduced echelon form of $A$. Since $E$ has $k$ columns we know that $E$ can have at most $k$ pivots. Because $k<n$ this means that the number of pivots is less than $n$. Therefore, we find that the number of pivots is less than the number of rows in $E$. This implies that it is impossible for $E$ to have a pivot in each row. {prf:ref}`Prop:LinearCombinations:PivotSpanSolution` now tells us that the span of the vectors $\mathbf{v}_1, \dots ,\mathbf{v}_k$ cannot be equal to $\mathbb{R}^n$.

::::

## Grasple Exercises

<iframe id="grasple_exercise_221" height="560" src="https://embed.grasple.com/exercises/2fe8b445-bb2e-412b-a2b8-593e2a0214cf?id=76698" title="Grasple Exercise 76698" width="100%"></iframe>
<br>
<hr style="height:5px; border-width:5px">
<iframe id="grasple_exercise_222" height="560" src="https://embed.grasple.com/exercises/f365becd-ee34-4fe9-854c-38fd188bb397?id=76699" title="Grasple Exercise 76699" width="100%"></iframe>