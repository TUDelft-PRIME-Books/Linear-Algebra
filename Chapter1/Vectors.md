(Sec:Vectors)=

# Vectors

## Introduction

There is little need to explain the usefulness of the ordinary (real) numbers you are familiar with. Nevertheless, they have their restrictions. For example, they can only describe one aspect of an object like the height of a person, or the age of a tree, or the weight of a car. But in many cases we also want to know a person's location, or a tree's widest circumference, or a car's width.

Quite often we are interested not just in size but also in direction. For example, if you are biking from Rotterdam to The Hague, you are probably less interested in how fast you are going than whether you are going in the right direction. Similarly, you don't just want to know the amount of energy needed to open a door, you also want to know whether you should pull or push. All this cannot be captured just by one number.

We therefore have a need for something more general. Something which allows us to express a force and a direction at once, something which allows us to collect a lot of information about an object not in one number but in one _thing_. This _thing_ turns out to be a vector. We will define vectors properly in {numref}`Subsection %s <Subsec:Vectors:ndim>`. First, in {numref}`Subsection %s <Subsec:Vectors:Plane>`, we try to get some intuition about length and direction by looking at arrows in the plane.

(Subsec:Vectors:Plane)=

## Arrows in the Plane

Consider an arrow $\mathbf{v}_{1}$ in the plane as in {numref}`Figure %s <Fig:Vectors:ArrowinPlane>`.

```{figure} Images/Fig-Vectors-ArrowinPlane.svg
:name: Fig:Vectors:ArrowinPlane
:class: dark-light

Two arrows in the plane.
```

You can think of such an arrow as a very simple route plan: it tells you in what direction to go and for how long. If you need to go in the same direction but twice as far, this corresponds to stretching the arrow $\mathbf{v}_{1}$ by a factor $2$. It makes sense to call this new arrow $2\mathbf{v}_{1}$.

Of course, such route plans can be combined. Take a look at {numref}`Figure %s <Fig:Vectors:AdditionPlane>`. If you first take the route described by $\mathbf{v}_{1}$, which takes you from $A$ to $B$, and then you take the route described by $\mathbf{v}_{2}$, which takes you from $B$ to $C$, you have in total gone from $A$ to $C$. Since the route from $A$ to $C$ is a combination of the routes given by $\mathbf{v}_{1}$ and $\mathbf{v}_{2}$, we write it as $\mathbf{v}_{1}+\mathbf{v}_{2}$.

```{figure} Images/Fig-Vectors-AdditionPlane.svg
:name: Fig:Vectors:AdditionPlane
:class: dark-light

Geometrical interpretation of addition in the plane.
```

Let us try to give this intuitive idea firm ground to stand on. We say by convention that by

$$

\mathbf{v}=\begin{bmatrix}
x\\y
\end{bmatrix}
$$

we mean an arrow pointing $x$ units to the right and $y$ units straight up. If $x$ is a negative number our arrow will point to the left and if $y$ is negative the arrow will point down. We will call such a representation of an arrow a _vector_ and the values $x$ and $y$ will be called its _entries_ (cfr. {prf:ref}`Dfn:Vectors:Vectors`).
In {numref}`Figure %s <Fig:Vectors:AdditionPlane>`, for example, we see the arrows

$$

\mathbf{v}_{1}=\begin{bmatrix}
	1\\2
\end{bmatrix}\quad\text{and}\quad\mathbf{v}_{2}=\begin{bmatrix}
	-2\\-1
\end{bmatrix}.
$$

If we glue the arrow $\mathbf{v}_{2}$ to the tip of $\mathbf{v}_{1}$, we find a new arrow, let's call it $\mathbf{v}_{3}$, that points $1$ unit to the left (which is $-1$ unit to the right) and $1$ unit straight up. So

$$

\mathbf{v}_{3}=\begin{bmatrix}
	-1\\1
\end{bmatrix}.
$$

We obtain the same result if we add the first and second entries of $\mathbf{v}_{1}$ and $\mathbf{v}_{2}$ component wise. In other words:

$$

\mathbf{v}_{3}=\begin{bmatrix}
	1+(-2)\\
	2+(-1)
\end{bmatrix}=\begin{bmatrix}
	1\\2
\end{bmatrix}+\begin{bmatrix}
	-2\\-1
\end{bmatrix}=\mathbf{v}_{1}+\mathbf{v}_{2}.
$$

As you see, it is very easy to find the sum of two arrows using our new notation. The same holds true for the stretching of an arrow. Let us try, for example, to stretch $\mathbf{v}_{3}$ to $2$ times its length, that is, let us try to find $2\mathbf{v}_{3}$. This gives an arrow pointing two units to the left and two units straight up. If we multiply both entries of $\mathbf{v}_{3}$ by $2$, we find a new vector $\mathbf{v}_{4}$ with:

$$

\mathbf{v}_{4}=\begin{bmatrix}
-2\\2
\end{bmatrix}
$$

which is precisely $2\mathbf{v}_{3}$.

We have found that the geometrical notion of an arrow in the plane with a certain length pointing in a certain direction is captured perfectly by the algebraic notion of its vector. Moreover, the natural operations of stretching and combining arrows can easily be done algebraically. In fact, there is no reason why we should restrict ourselves to arrows in the plane. We can just as well take arrows in three dimensional space and glue them together or stretch them. In {numref}`Subsection %s <Subsec:Vectors:ndim>` we will formalize this notion to $n$ dimensions -- and we will see that it is not so strange to have more than $3$ dimensions!

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/553450f1-e960-4bac-9bb4-074fe8106369?id=78688
:label: grasple_exercise_1_1_1
:dropdown:
:description: Expressing vectors in other vectors.

::::

(Subsec:Vectors:ndim)=

## Vectors and $\mathbb{R}^{n}$

The same game we played in the plane also works in $3$-dimensional space -- or even in higher dimensions. Since our intuition tends to break down in higher dimension, we want solid algebraic foundation to support us in these unfamiliar lands. Let us therefore formalize our concept of arrows.

```{prf:definition}
:label: Dfn:Vectors:Vectors


Let $n$ be a positive natural number. If $a_{1},a_{2},...,a_{n}$ are real numbers, we call

$$

\mathbf{v}=\begin{bmatrix}
a_{1}\\a_{2}\\\vdots\\a_{n}
\end{bmatrix}
$$

 a *vector* or sometimes a *column vector*. The number $n$ is called the *size* of the vector $\mathbf{v}$ and $a_{1},a_{2},...,a_{n}$ are called its *entries* or *components*. In particular, we call $a_{i}$ the *$i$-th entry* or *$i$-th component* of $\mathbf{v}$. The collection of all such vectors is written as $\mathbb{R}^{n}$. The vector for which all entries are $0$ will play a special role. We will denote it by $\mathbf{0}$.

```

Note that the order of the entries is very important. For example

$$

\begin{bmatrix}
1\\-1
\end{bmatrix}\quad\text{and}\quad\begin{bmatrix}
-1\\1
\end{bmatrix}
$$

are _not_ the same vectors. Indeed, the first one points down and to the right, while the second one points up and to the left. Two vectors are only equal if they have the same entries in the same order.

```{prf:definition}



Suppose we have two vectors

$$

\mathbf{v}_{1}=\begin{bmatrix}
a_{1}\\\vdots\\a_{n}\end{bmatrix}\quad\text{and}\quad\mathbf{v}_{2}=\begin{bmatrix} b_{1}\\\vdots \\b_{n}\end{bmatrix}
$$

 of the same size. The *sum* of $\mathbf{v}_{1}$ and $\mathbf{v}_{2}$, denoted by $\mathbf{v}_{1}+\mathbf{v}_{2}$, is the vector


$$

\mathbf{v}_{1}+\mathbf{v}_{2}=\begin{bmatrix} a_{1}+b_{1}\\\vdots\\a_{n}+b_{n}\end{bmatrix}.
$$

If $c$ is a real number, then the *scalar multiple* $c\mathbf{v}_{1}$ is the vector


$$

c\mathbf{v}_{1}=\begin{bmatrix}
ca_{1}\\\vdots\\ca_{n}
\end{bmatrix}.
$$


We will sometimes call real numbers *scalars*, because we use them to scale vectors. To lighten our notation, we will write $-\mathbf{v}_{1}$ for $(-1)\mathbf{v}_{1}$. Likewise, we will often write $\mathbf{v}_{1}-\mathbf{v}_{2}$ for $\mathbf{v}_{1}+(-\mathbf{v}_{2})$.

```

```{applet}
:url: vectors/3Daddition
:fig: Images/Fig-Vectors-3Daddition.svg
:status: approved
:class: dark-light

Geometrical interpretation of addition for three-dimensional vectors.
```

```{prf:remark}



Note that we only define the sum of two vectors if they have the same size!

```

This might look a bit scary, but is really just what we did in the plane, just with more numbers now. We now use the term vector instead of arrow. Adding two vectors is again just gluing the second one to the tip of the first one, and taking a scalar multiple of a vector is just stretching it again (or perhaps shrinking it).

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a962fb8c-89b0-4b97-b76e-8f53335cf301?id=70140
:label: grasple_exercise_1_1_2
:dropdown:
:description: To compute combinations $c_1\vect{u}+c_2\vect{v}$.

::::

Since vector addition and scalar multiplication will be used all the time in this text, it will be convenient to know how to work with these operations. Luckily, it turns out that they satisfy most of the calculation rules that you are familiar with from standard arithmetic, as you can see from the following:

````{prf:proposition}
:label:  Prop:Vectors:BasicRules



Suppose $\mathbf{v}_{1},\mathbf{v}_{2},\mathbf{v}_{3}$ are vectors in $\mathbb{R}^{n}$ for some natural number $n$ and let $c_{1},c_{2}$ be in $\mathbb{R}$. Then we have:


1. $\mathbf{v}_{1}+\mathbf{0}=\mathbf{v}_{1}=\mathbf{0}+\mathbf{v}_{1}$
2. Associativity:
	```{math}
	:label: Item:Vectors:Associativity

	(\mathbf{v}_{1}+\mathbf{v}_{2})+\mathbf{v}_{3}=\mathbf{v}_{1}+(\mathbf{v}_{2}+\mathbf{v}_{3})
	```
3. Commutativity:
	```{math}
	:label: Item:Vectors:Commutativity

	\mathbf{v}_{1}+\mathbf{v}_{2}=\mathbf{v}_{2}+\mathbf{v}_{1}
	```
4. $\mathbf{v}_{1}+(-\mathbf{v}_{1})=\mathbf{0}$
5. $1\mathbf{v}_{1}=\mathbf{v}_{1}$
6. $c_{1}(\mathbf{v}_{1}+\mathbf{v}_{2})=c_{1}\mathbf{v}_{1}+c_{1}\mathbf{v}_{2}$
7. $(c_{1}+c_{2})\mathbf{v}_{1}=c_{1}\mathbf{v}_{1}+c_{2}\mathbf{v}_{1}$
8. $c_{1}(c_{2}\mathbf{v}_{1})=(c_{1}c_{2})\mathbf{v}_{1}$



````

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:Vectors:BasicRules`
:class: tudproof

See {numref}`grasple_exercise_1_1_11`.

::::

For example, the Equation {eq}`Item:Vectors:Associativity` tells us that we do not have to worry about bracketing when adding vectors. That is, we can first add $\mathbf{v}_{1}$ to $\mathbf{v}_{2}$ and then add $\mathbf{v}_{3}$ to the result or we can first add $\mathbf{v}_{2}$ to $\mathbf{v}_{3}$ and then add the result to $\mathbf{v}_{1}$. In both cases, we will get the same answer.

````{prf:example} Application
:label: App:Vectors:ChemReac


More than three dimensions? How does that make sense? Well, it is actually not so strange at all! Here is an example in which four dimensions occur very naturally. Sodium sulfide ($\ce{Na2S}$) is a chemical used to turn wood into pulp, to bleach textile, and so on. It is produced by adding carbon ($\ce{C}$) to sodium sulfate ($\ce{Na_{2}SO_{4}}$), which gives the following reaction:

```{math}
:label: Eq:Vectors:ChemReac

\ce{Na2SO4 + 2 C -> Na2S + 2 CO2}.
```

Note that for every molecule of sodium sulfate we need two molecules of carbon in this reaction and that for every molecule of sodium sulfate, two molecules of carbon dioxide ($\ce{CO2}$) are produced.

```{figure} Images/Fig-Vectors-ChemRec.svg
:name: Fig:Vectors:ChemRec

The chemical reaction given in {eq}`Eq:Vectors:ChemReac`.
```

There are four different chemical elements involved in this reaction: sodium ($\ce{Na}$), sulfide ($\ce{S}$), oxygen ($\ce{O}$), and carbon. Each of our molecules can be written as a vector of size four with the entries giving the number of sodium, sulfide, oxygen, and carbon atoms (in that order) in the molecule. This gives:


$$

\ce{Na2SO4}: \begin{bmatrix}
2\\1\\4\\0
\end{bmatrix}\quad \ce{C}:\begin{bmatrix}
0\\0\\0\\1
\end{bmatrix}\quad
\ce{Na2S}:\begin{bmatrix}
2\\1\\0\\0
\end{bmatrix}\quad\text{and}\quad \ce{CO2}:\begin{bmatrix}
0\\0\\2\\1
\end{bmatrix}.
$$



In order for the reaction given in {eq}`Eq:Vectors:ChemReac` to be balanced, we need to know that there are no atoms on the left which are not present on the right and vice versa. That is, we need to have the following vector equation:


$$

\begin{bmatrix}
2\\1\\4\\0
\end{bmatrix}+2\begin{bmatrix}
0\\0\\0\\1
\end{bmatrix}=\begin{bmatrix}
2\\1\\0\\0
\end{bmatrix}+2\begin{bmatrix}
0\\0\\2\\1
\end{bmatrix}
$$


which indeed holds.

The reaction under consideration here is a very simple one. It is not at all rare for seven or eight different elements to be involved in a chemical reaction. This naturally gives rise to a seven- or eight-dimensional vector equation.

````

## Points and Vectors

Vectors are quite easy to work with, even in more than three dimensions. It will therefore be convenient to relate the familiar concepts from plain old plane geometry and the somewhat more advanced three-dimensional geometry in terms of vectors. In this section, we will establish a link between points and vectors by introducing a sort of common anchor point for all vectors. In {numref}`SubSec:LinesAndPlanes:Plane`, we will relate lines and planes to vectors.

Suppose we fix an arbitrary point in the plane. Let us call it the _origin_ and write it as $O$. Every other point can now be fully determined by its displacement from $O$. In other words, any point $P$ in the place can be described by saying how far it is to the right of $O$ and how far it is up from $O$. If $a_{1}$ is the former quantity and $a_{2}$ is the latter, we will write $P=(a_{1},a_{2})$. If $P$ happens to be to the left of the origin, $a_{1}$ will be negative. Similarly, if $P$ is lower than $O$, $a_{2}$ will be negative. In {numref}`Figure %s <Fig:Vectors:PointandVect>`, you can see the point $P=(-1,2)$. For the point $O$ itself, we have $O=(0,0)$ since the displacement from $O$ to $O$ is $0$ in both directions.

```{figure} Images/Fig-Vectors-PointandVec.svg
:name: Fig:Vectors:PointandVect
:class: dark-light

The point $P=(-1,2)$ and its associated vector $\mathbf{v}=\begin{bmatrix}-1\\2\end{bmatrix}$.
```

This might call to mind the vectors we saw in {numref}`Subsection %s <Subsec:Vectors:Plane>`. Remember that a vector in the plane was given by two displacements. A point $P=(a_{1},a_{2})$ is given by the displacement from $O$, so if we take $O$ as the starting point of the vector

$$

\mathbf{v}_{P}=\begin{bmatrix}a_{1}\\a_{2}\end{bmatrix},
$$

its end point will be precisely $P$.

By fixing our origin $O$, we have therefore introduced a natural correspondence between points in the plane and vectors with two components: a point $P=(a_{1},a_{2})$ corresponds to the vector pointing from $O$ to $P$, which is given by $\mathbf{v}$.

In a similar vein, we can associate vectors with three components to points in three-dimensional space. We again fix an origin $O=(0,0,0)$. Any other point $P$ is given by its displacement from $O$ to the front ($a_{1}$), to the right ($a_{2}$), and upward ($a_{3}$). To this point, we can associate the vector

$$

\mathbf{v}_{P}=\begin{bmatrix}
a_{1}\\a_{2}\\a_{3}
\end{bmatrix}.
$$

If we let $\mathbf{v}$ start in $O$, its end point will be precisely $P$. This method works just as well for points on the line, which correspond to vectors with just one component. In fact, it works for any $\mathbb{R}^{n}$. We fix an origin $O=(0,\ldots,0)$. A point $P=(a_{1},\ldots,a_{n})$ then corresponds to the vector $\mathbf{v}_{p}$ pointing from $O$ to $P$, i.e. the vector

$$

\mathbf{v}_{P}=\begin{bmatrix}
a_{1}\\\vdots\\ a_{n}
\end{bmatrix}.
$$

## Grasple Exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/670148b0-07cb-4f0c-861f-0ac6fbc83fb2?id=70141
:label: grasple_exercise_1_1_3
:dropdown:
:description: To compute combinations $c_1\vect{u}+c_2\vect{v}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/f85678d3-21f1-484f-a589-4e2fc5b0f76d?id=73610
:label: grasple_exercise_1_1_4
:dropdown:
:description: To compute $\vect{u}-\vect{v}$ and $\vect{v}-\vect{u}$ in $\R^4$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9c3a037d-7bcb-49c7-a167-baffbae14d46?id=70142
:label: grasple_exercise_1_1_5
:dropdown:
:description: To solve for $\vect{x}$ an equation $a(\vect{x}-\vect{u})= b(\vect{x}-\vect{v}) + c\vect{u}+d\vect{u}$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a33e81af-5670-421f-96a0-d4ed40f5e79b?id=74451
:label: grasple_exercise_1_1_6
:dropdown:
:description: Expressing $\vect{w}$ as $c_1\vect{u} +c_2\vect{v}$ from a picture.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b212a5ff-ea16-47a9-bc71-8e2b21944c9d?id=69732
:label: grasple_exercise_1_1_7
:dropdown:
:description: Computing the vector from point $A$ to point $B$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a56eb5e4-62c9-4dfa-9f9c-e53c1f1c913a?id=69479
:label: grasple_exercise_1_1_8
:dropdown:
:description: To check whether two vectors are on the same line through $(0,0)$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e1df17bf-cfb6-4dde-ae63-c424b5e149ba?id=73622
:label: grasple_exercise_1_1_9
:dropdown:
:description: When do two vectors (with a parameter $k$) lie on a line through $(0,0)$?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ff44880f-1ce0-428e-8bb2-42898b66e76f?id=78691
:label: grasple_exercise_1_1_10
:dropdown:
:description: Another hexagon 'puzzle'.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/65b17e6e-b9e1-44de-9445-578c5ee1f633?id=62390
:label: grasple_exercise_1_1_11
:dropdown:
:description: To prove the basic properties ({prf:ref}`Prop:Vectors:BasicRules`) of vector sum and multiple.

::::
