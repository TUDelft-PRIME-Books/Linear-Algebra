# Lines and Planes 

Throughout this book we will regularly work with geometrical objects in $\mathbb{R}^n$ that are generalisations of lines and planes. In this section we will take a look at how lines and planes can be represented by various equations in $\mathbb{R}^2$ and $\mathbb{R}^3$. We will use these representations later on to obtain a better understanding of concepts like *subspaces* and *solution sets* of systems of equations.

(Section:LinesAndPlanes:Plane)=
## Lines in the plane $\mathbb{R}^2$  

We all know what a line looks like, but in mathematics we want to define everything in a precise way. Therefore, we will define lines in $\mathbb{R}^2$ as follows.


````{prf:definition}  

A line $\mathcal{L}$ in the plane $\mathbb{R}^2$ is a collection of points $(x, y)$ that satisfy an equation of the form 

$$

ax+by=c,
$$

 where $a$ and $b$ are not both zero. This equation is called a *Cartesian equation* of $\mathcal{L}$.

````

The point $(4, 1)$, for example, is a point on the line with equation $2x-3y=5$ because $2\cdot 4-3\cdot 1=5$, but $(6,-1)$ is not since $2\cdot 6-3\cdot (-1)$ is equal to 15 and not to 5. If we draw all points of a given line $\mathcal{L}$ in the plane $\mathbb{R}^2$, then we obtain a graphical representation of the line. In {numref}`Figure %s <Fig:LinesAndPlanes:LineInPlane>` we see the line with Cartesian equation $2x-3y=5$.


````{figure}  Images/Fig-LinesAndPlanes-LineInPlane.svg
:name: Fig:LinesAndPlanes:LineInPlane

The line $2x-3y=5$ in the plane.
````

## Intersecting lines 

Two lines can have a point of intersection. Let $\mathcal{L}_1$ and $\mathcal{L}_2$ be the lines defined by the equations $x+2y=5$ and $3x-y=1$. The point $(1, 2)$ is clearly a point on both lines. It satisfies the equation $x+2y=5$ and the equation $3x-y=1$. In {numref}`Figure %s <Fig:LinesAndPlanes:PointIntersection>` we can see that this is the unique point of intersection.


````{figure}  Images/Fig-LinesAndPlanes-PointIntersection.svg
:name: Fig:LinesAndPlanes:PointIntersection

Intersecting lines.
````

In the previous example there was exactly one point of intersection. This is not the only possibility. Two lines can have no points of intersection at all or infinitely many. If $\mathcal{L}_3$ is the line given by the equation $x+2y=2$, then $\mathcal{L}_1$ and $\mathcal{L}_3$ do not intersect. This can be seen in {numref}`Figure %s <Fig:LinesAndPlanes:ParallelLines>`, but also becomes clear when you take a good look at both equations. The lines $\mathcal{L}_1$ and $\mathcal{L}_3$ are defined by the equations  $x+2y=5$ and $x+2y=2$ respectively. Since there are no values of $x$ and $y$ for which $x+2y$ is both equal to $5$ and $2$, the two lines cannot have a point in common.


````{figure}  Images/Fig-LinesAndPlanes-ParallelLines.svg
:name: Fig:LinesAndPlanes:ParallelLines

Parallel lines.
````

Finally, let us take a look at the line $\mathcal{L}_2$, which was defined by the equation $3x-y=1$, and the line $\mathcal{L}_4$ given by the equation $-6x+2y=-2$ (see {numref}`Figure %s <Fig:LinesAndPlanes:CoincidingLines>`). The equation of $\mathcal{L}_4$ is a multiple of the equation of $\mathcal{L}_2$. This means that each point $(x, y)$ that satisfies one equation automatically satisfies the other, so the lines $\mathcal{L}_2$ and $\mathcal{L}_4$ coincide. Therefore, the lines $\mathcal{L}_2$ and $\mathcal{L}_4$ have infinitely many points of intersection.


````{figure}  Images/Fig-LinesAndPlanes-CoincidingLines.svg
:name: Fig:LinesAndPlanes:CoincidingLines

Coinciding lines.
````

(Subsec:LinesAndPlanes:ParametricLine)=
## Parametric vector equation of a line 

So far we have looked at lines as collections of points in the plane, but we can also think of them as collections of vectors. We can define the line $\mathcal{L}_1$ with equation $x+2y=5$ as the collection of all vectors 

$$

\mathbf{v}=\begin{bmatrix} x \\ y \end{bmatrix}
$$

 of which the components $x$ and $y$ satisfy the equation $x+2y=5$. This means that the line $\mathcal{L}_1$ consists of all vectors that connect the origin with a point on the line. When we think of a line as a collection of vectors we can describe that line with a *parametric vector equation*. To do this, we need a vector that connects the origin to a point on the line and a non-zero vector $\mathbf{u}$ parallel to the line.


````{prf:definition}  

Each non-zero vector $\mathbf{u}$ that is parallel to a line $\mathcal{L}$ will be called a *directional vector* of that line.
````

The point $(5, 0)$ satisfies the equation $x+2y=5$, so it is a point on $\mathcal{L}_1$. Therefore, the vector 

$$
\mathbf{v_0}=\begin{bmatrix} 5 \\ 0 \end{bmatrix}
$$

 connects the origin with a point on the line. As we can see in {numref}`Figure %s <Fig:LinesAndPlanes:VectorEquation>` the vector 

$$

\mathbf{u}=\begin{bmatrix} -2 \\ 1 \end{bmatrix}
$$

 is a vector parallel to the same line. 


````{figure}  Images/Fig-LinesAndPlanes-VectorEquation.svg
:name: Fig:LinesAndPlanes:VectorEquation

The line $\mathcal{L}_1$.
````

How do we obtain all vectors on the line $\mathcal{L}_1$? Let us start with the vector 

$$

\mathbf{v_1}=\begin{bmatrix} 3 \\ 1 \end{bmatrix}.
$$

 Its coordinates satisfy the equation $x+2y=5$, so this vector is indeed on the line $\mathcal{L}_1$. However, if we look at {numref}`Figure %s <Fig:LinesAndPlanes:VectorEquation>` we also see that it is the sum of the vectors $\mathbf{v_0}$ and $\mathbf{u}$. It is not hard to see that whenever we add a multiple of the vector $\mathbf{u}$ to the vector $\mathbf{v_0}$, we obtain a vector on $\mathcal{L}_1$.

Take for example the vector $\mathbf{v_2}$ that we will define as $\mathbf{v_0}+2 \mathbf{u}$. If we compute the coordinates of this vector we find 

$$

\mathbf{v_2}=\begin{bmatrix} 5 \\ 0 \end{bmatrix}+2\begin{bmatrix} -2 \\ 1 \end{bmatrix}=\begin{bmatrix} 1 \\ 2 \end{bmatrix}
$$

 and we end up with another vector that satisfies the equation $x+2y=5$.

By now we have noticed that we obtain a new vector on $\mathcal{L}_1$ whenever we add a multiple of $\mathbf{u}$ to $\mathbf{v_0}$. Apparently, each vector 

$$

\mathbf{v}=\begin{bmatrix} x \\ y \end{bmatrix}
$$

 on the line $\mathcal{L}$ can be written in the form 

$$

\begin{bmatrix} x \\ y \end{bmatrix}=\begin{bmatrix} 5 \\ 0 \end{bmatrix}+r\begin{bmatrix} -2 \\ 1 \end{bmatrix}
$$

 where $r$ is a real number.


````{prf:definition}  

If $\mathbf{v_0}=\begin{bmatrix} x_0 \\ y_0 \end{bmatrix}$ is a vector on the line $\mathcal{L}$ and $\mathbf{u}=\begin{bmatrix} a \\ b \end{bmatrix}$ is a directional vector of $\mathcal{L}$, then the equation 

$$
\begin{bmatrix} x \\ y \end{bmatrix}=\begin{bmatrix} x_0 \\ y_0 \end{bmatrix}+r\begin{bmatrix} a \\ b \end{bmatrix} \qquad \textrm{$r$ in $\mathbb{R}$}
$$

will be called a *parametric vector equation* of $\mathcal{L}$.

````


````{admonition} Exercise

Let $\mathcal{L}$ be the line through the points $P=(2, 1)$ and $Q=(6, 4)$. How do we find a parametric vector equation of this line? We need a vector that connects the origin to a point on the line and a vector parallel to the line. For the first vector we can simply use the coordinates of either $P$ or $Q$. We can use either point, but let us choose $P$. We can construct a vector parallel to the line $\mathcal{L}$ by connecting two distinct points on the line by an arrow. We can use for instance the vector $\mathbf{PQ}$ that starts in $P$ and ends in $Q$. 

$$
\mathbf{PQ}=\begin{bmatrix} 6 \\ 4 \end{bmatrix}-\begin{bmatrix} 2 \\ 1 \end{bmatrix}=\begin{bmatrix} 4 \\ 3 \end{bmatrix}
$$

 If we use these vectors, then we find the following parametric equation. 

$$
\begin{bmatrix} x \\ y \end{bmatrix}=\begin{bmatrix} 2 \\ 1 \end{bmatrix}+r\begin{bmatrix} 4 \\ 3 \end{bmatrix} \qquad \textrm{$r$ in $\mathbb{R}$}
$$

````

(Subsection:LinesAndPlanes:NormalLine)=
## Normal equation of a line 

Finally, we will take a look at a *normal equation* of a line in $\mathbb{R}^2$. To obtain a parametric vector equation of a line, we used a vector parallel to that line. For the normal equation of a line we use a vector that is orthogonal to the line.


````{prf:definition}  

Any non-zero vector $\mathbf{n}$ that is orthogonal to a line $\mathcal{L}$ will be called a *normal vector* of that line.

````

Let $\mathbf{n}$ be a normal vector of a line $\mathcal{L}$ and $P$ a point on $\mathcal{L}$. Whenever we take a point $Q$ on $\mathcal{L}$, the vector $\mathbf{PQ}$ is orthogonal to $\mathbf{n}$. This means that the inner product of these vectors is zero. We find that whenever a point $Q$ is on the line $\mathcal{L}$ it satisfies 

$$
\mathbf{PQ}\ip \mathbf{n}=0.
$$

````{figure}  Images/Fig-LinesAndPlanes-NormalEquationLine.svg
:name: Fig:LinesAndPlanes:NormalEquationLine

Normal equation.
````

Let $\mathbf{v_0}$ be the vector that connects the origin to the point $P$. We can see in {numref}`Figure %s <Fig:LinesAndPlanes:NormalEquationLine>` that a vector $\mathbf{v}$ is on the line $\mathcal{L}$ whenever 

$$
(\mathbf{v}-\mathbf{v_0})\ip\mathbf{n}=0.
$$




````{prf:definition}  

Let $\mathcal{L}$ be a line in $\mathbb{R}^2$. If $\mathbf{v_0}$ is a vector on $\mathcal{L}$ and $\mathbf{n}$ is a normal vector of $\mathcal{L}$, then 

$$
(\mathbf{v}-\mathbf{v_0})\ip\mathbf{n}=0
$$

will be called a *normal equation* of $\mathcal{L}$.
````


````{admonition} Exercise  

The line $\mathcal{L}_1$ can be described by the following parametric vector equation. 

$$
\begin{bmatrix} x \\ y \end{bmatrix}=\begin{bmatrix} 5 \\ 0 \end{bmatrix}+r\begin{bmatrix} -2 \\ 1 \end{bmatrix} \qquad \textrm{$r$ in $\mathbb{R}$}
$$

Let us try to find a Cartesian equation for the line $\mathcal{L}$ through the point $P=(1, 7)$ and orthogonal to $\mathcal{L}_1$. We will start with a normal equation and then derive a Cartesian equation from that. 

```{figure} Images/Fig-LinesAndPlanes-OrthogonalLines.svg
:name: Fig:LinesAndPlanes:OrthogonalLines

A line orthogonal to $\mathcal{L}_1$.
```

Because $\mathcal{L}$ needs to be orthogonal to $\mathcal{L}_1$ we can use the directional vector $\mathbf{n}=\begin{bmatrix} -2 \\ 1 \end{bmatrix}$ as a normal vector for $\mathcal{L}$. Define $\mathbf{v_0}$ as $\begin{bmatrix} 1 \\ 7 \end{bmatrix}$. By computing the inner product we can transform the normal equation 

$$
(\mathbf{v}-\mathbf{v_0})\ip\mathbf{n}=0
$$

 into a Cartesian equation. Let $\mathbf{v}$ be the vector $\begin{bmatrix} x \\ y \end{bmatrix}$. Since $\mathbf{v}-\mathbf{v_0}$ is equal to $\begin{bmatrix} x-1 \\ y-7 \end{bmatrix}$ we can rewrite the normal equation of $\mathcal{L}$ as 

$$
(x-1)\cdot(-2)+(y-7)\cdot(1)=0.
$$

 After some calculations we find the Cartesian equation $-2x+y=5$. In Figure \ref{Fig:LinesAndPlanes:OrthogonalLines} you can see both lines.

```` 

## Planes in the space $\mathbb{R}^3$ 

We already saw that when we are working in $\mathbb{R}^2$, we can describe lines using a Cartesian equation, a parametric vector equation or a normal equation. Planes in the three-dimensional space $\mathbb{R}^3$ can be described in similar ways. We will start by defining planes using the *Cartesian equation* and then we will explain the geometrical interpretation of this equation.


````{prf:definition}  

A plane $\mathcal{P}$ in the space $\mathbb{R}^3$ is a collection of points $(x, y, z)$ that satisfy an equation of the form 

$$
ax+by+cz=d,
$$

 where $a$, $b$ and $c$ are not all zero. This equation is called a *Cartesian equation* of $\mathcal{P}$.
````

The Cartesian equation of a plane in $\mathbb{R}^3$ resembles the Cartesian equation of a line in $\mathbb{R}^2$. So, how is it that such an equation describes a plane and not a line in $\mathbb{R}^3$? We can clarify this by looking at a *normal equation* of a plane.

In {numref}`Subsection %s <Subsection:LinesAndPlanes:NormalLine>` we saw that, given a point $P$ and a vector $\mathbf{n}$ in the plane, the collection of all points $Q$ for which the vector $\mathbf{PQ}$ is orthogonal to $\mathbf{n}$ forms a line through $P$. In the space $\mathbb{R}^3$ this is no longer true. Let us investigate what the result is when we make a similar construction with a vector $\mathbf{n}$ in $\mathbb{R}^3$, say 

$$
\mathbf{n}=\begin{bmatrix} 2 \\ 1 \\ 3 \end{bmatrix}.
$$

 As we can see in {numref}`Figure %s <Fig:LinesAndPlanes:NormalEquationPlaneOrigin>` all points $Q$ for which the vector that connects the origin to $Q$ is orthogonal to $\mathbf{n}$ form a plane through the origin.


````{figure}  Images/Fig-LinesAndPlanes-NormalEquationPlaneOrigin.svg
:name: Fig:LinesAndPlanes:NormalEquationPlaneOrigin

A plane through the origin.
````

Now let $P$ be the point with coordinates $(0, 2, 1)$ and take an arbitrary point $Q$ in $\mathbb{R}^3$. It is clear from {numref}`Figure %s <Fig:LinesAndPlanes:NormalEquationPlane>` that the vector $\mathbf{PQ}$ is orthogonal to $\mathbf{n}$ if and only if $Q$ is a point on the plane $\mathcal{P}$ orthogonal to $\mathbf{n}$ and through $P$.


````{figure}  Images/Fig-LinesAndPlanes-NormalEquationPlane.svg
:name: Fig:LinesAndPlanes:NormalEquationPlane

A plane through the point $P$.
````

What is the Cartesian equation of this plane? If the coordinates of $Q$ are $(x, y, z)$, then $\mathbf{PQ}$ is orthogonal to $\mathbf{n}$ if and only if $\mathbf{PQ}\ip \mathbf{n}=0$. If we compute this inner product we obtain the following result.

\begin{align*}
(\mathbf{v}-\mathbf{v_0})\ip \mathbf{n} &= \begin{bmatrix} x-0 \\ y-2 \\ z-1 \end{bmatrix} \ip \begin{bmatrix} 2 \\ 1 \\ 3  \end{bmatrix} \\
 &= 2(x-0)+(y-2)+3(z-1) \\
 &= 2x+y+3z-5
\end{align*}

This means that $Q$ is on the plane $\mathcal{P}$ through $P$ and orthogonal to $\mathbf{n}$ if and only if its coordinates satisfy $2x+y+3z-5=0$ or $2x+y+3z=5$. Hence, we obtain a Cartesian equation of $\mathcal{P}$.

## Normal equation of a plane 

A line can be defined as a collection of points and as the collection of vectors that connect the origin to a point on the line. Similarly, we can identify the plane $\mathcal{P}$ as the collection of all vectors $\mathbf{v}$ that connect the origin to a point on $\mathcal{P}$. In this case we will say that $\mathbf{v}$ is a vector on the plane $\mathcal{P}$.


````{prf:definition}  

Any non-zero vector $\mathbf{n}$ that is orthogonal to a plane $\mathcal{P}$ will be called a *normal vector* of that plane.
````

Let $\mathbf{n}$ be a normal vector for a given plane $\mathcal{P}$ and $\mathbf{v_0}$ a vector on $\mathcal{P}$. {numref}`Figure %s <Fig:LinesAndPlanes:NormalEquationPlane>` tells us that any other vector $\mathbf{v}$ is on $\mathcal{P}$ whenever $(\mathbf{v}-\mathbf{v_0})\ip\mathbf{n}=0$.


````{prf:definition}  

Let $\mathcal{P}$ be a plane in $\mathbb{R}^3$. If $\mathbf{v_0}$ is a vector on $\mathcal{P}$ and $\mathbf{n}$ is a normal vector of $\mathcal{P}$, then 

$$
(\mathbf{v}-\mathbf{v_0})\ip\mathbf{n}=0
$$

 will be called a *normal equation* of $\mathcal{P}$.

````

## Parametric vector equation of a plane 

Finally, let us take a look at a *parametric vector equation* of a plane. Such an equation will be very similar to a parametric vector equation of a line in the plane $\mathbb{R}^2$, but in this case we will need two directional vectors instead of one.


````{prf:definition}  

Each non-zero vector $\mathbf{u}$ that is parallel to a plane $\mathcal{P}$ will be called a *directional vector* of that plane.
````

We can always find directional vectors of a plane by taking a vector that connects two distinct points in the plane. If we want to find two directional vectors for the plane $\mathcal{P}$ with Cartesian equation $2x+y+3z=5$, then we can use the point $P=(0, 2, 1)$ that we have been working with and choose two other points that satisfy $2x+y+3z=5$. We can use, for example, the points $Q=(0, 5, 0)$ and $R=(2, 1, 0)$. In {numref}`Figure %s <Fig:LinesAndPlanes:DirectionalVectorsPlane>` you can see that the vectors $\mathbf{PQ}$ and $\mathbf{PR}$ are two vectors that are parallel to the plane, but are not parallel to each other. 


````{figure}  Images/Fig-LinesAndPlanes-DirectionalVectorsPlane.svg
:name: Fig:LinesAndPlanes:DirectionalVectorsPlane

A parametric vector equation of a plane.
````

Any vector $\mathbf{v}$ on the plane $\mathcal{P}$ can now be written in the form 

$$
\mathbf{v_0}+r\mathbf{PQ}+s\mathbf{PR}
$$

 where $r$ and $s$ are arbitrary real numbers.


````{prf:definition}  

If $\mathbf{v_0}=\begin{bmatrix} x_0 \\ y_0 \\ z_0 \end{bmatrix}$ is a vector on the plane $\mathcal{P}$ and $\mathbf{u_1}=\begin{bmatrix} a_1 \\ b_1 \\ c_1 \end{bmatrix}$ and $\mathbf{u_2}=\begin{bmatrix} a_2 \\ b_2 \\ c_2 \end{bmatrix}$ are directional vectors of $\mathcal{P}$ that are not parallel, then the equation 

$$
\begin{bmatrix} x \\ y \\ z \end{bmatrix}=\begin{bmatrix} x_0 \\ y_0 \\ z_0 \end{bmatrix}+r\begin{bmatrix} a_1 \\ b_1 \\ c_1  \end{bmatrix}+s\begin{bmatrix} a_2 \\ b_2 \\ c_2  \end{bmatrix} \qquad \textrm{$r, s$ in $\mathbb{R}$}
$$

 will be called a *parametric vector equation* of $\mathcal{P}$.
````


````{admonition} Exercise  

In this example we will construct a parametric vector equation and a normal equation for the plane through the points $P=(1, 1, 1)$, $Q=(1, 2, 2)$ and $R=(3, 1, 2)$. The vectors $\mathbf{PQ}$ and $\mathbf{PR}$ can serve as directional vectors. We find that 

$$
\mathbf{PQ}=\begin{bmatrix} 1-1 \\ 2-1 \\ 2-1 \end{bmatrix}=\begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix} \quad \mathbf{PR}=\begin{bmatrix} 3-1 \\ 1-1 \\ 2-1 \end{bmatrix}=\begin{bmatrix} 2 \\ 0 \\ 1 \end{bmatrix}.
$$

This means that 

$$
\begin{bmatrix} x \\ y \\ z \end{bmatrix}=\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}+r\begin{bmatrix} 0 \\ 1 \\ 1  \end{bmatrix}+s\begin{bmatrix} 2 \\ 0 \\ 1  \end{bmatrix} \qquad \textrm{$r, s$ in $\mathbb{R}$}
$$

is a parametric vector equation of the plane through the given points.

In order to find a normal equation we need to construct a normal vector. We can do this by computing the cross product of the two directional vectors. After all, we know that the cross product of $\mathbf{PQ}\cp\mathbf{PR}$ is orthogonal to $\mathbf{PQ}$ and $\mathbf{PR}$ and thus to the entire plane. We find 

$$
\mathbf{PQ}\cp\mathbf{PR}=\begin{bmatrix} 1\cdot 1-1\cdot 0 \\ 1\cdot 2-0\cdot 1 \\ 0\cdot 0-1\cdot 2 \end{bmatrix}=\begin{bmatrix} 1 \\ 2 \\ -2 \end{bmatrix}.
$$

Because the point $P(1, 1, 1)$ needs to be on the plane we can conclude that 

$$
x+2y-2z=1
$$

is a normal equation of the plane that contains $P$, $Q$ and $R$.
````

## Intersecting planes 

We already established that two lines in the plane can have zero, one or infinitely many points of intersection, but what's the deal when we are working with planes? How many points of intersection can two planes in $\mathbb{R}^3$ have?

It is of course possible that two planes have no points in common at all. Take a look at {numref}`Figure %s <Fig:LinesAndPlanes:TwoDisjointPlanes>`. There we see two parallel planes that do not coincide. These planes have no points of intersection.


````{figure}  Images/Fig-LinesAndPlanes-TwoDisjointPlanes.svg
:name: Fig:LinesAndPlanes:TwoDisjointPlanes

Two planes without a common point in common.
````

Two planes in $\mathbb{R}^3$ can never have a single point of intersection. They can, however, have infinitely many common points. This can occur when the two planes have a line of intersection, as we can see in {numref}`Figure %s <Fig:LinesAndPlanes:TwoPlanesLineIntersection>`. On the other hand, it is also possible that two planes coincide, see {numref}`Figure %s <Fig:LinesAndPlanes:TwoPlanesCoincide>`. In this case each point on one of the two planes is an intersection point.


````{figure}  Images/Fig-LinesAndPlanes-TwoPlanesLineIntersection.svg
:name: Fig:LinesAndPlanes:TwoPlanesLineIntersection

Two planes with a line of intersection.
````

<div style="margin:auto; text-align:center"><iframe height="300px" src="https://3d-graph-yustarandomname.vercel.app/applet/lines_and_planes/two_plane_line_intersection/" width="500px"></iframe></div>

````{figure}  Images/Fig-LinesAndPlanes-TwoPlanesCoincide.svg
:name: Fig:LinesAndPlanes:TwoPlanesCoincide

Two planes that coincide.
````

Now what happens when we take three arbitrary planes $\mathcal{P}_1$, $\mathcal{P}_2$ and $\mathcal{P}_3$ in the space $\mathbb{R}^3$? How many points can we find that are on all three planes?

First of all, it is possible that there are no points that are on $\mathcal{P}_1$, $\mathcal{P}_2$ and $\mathcal{P}_3$ simultaneously. This is the case for the three planes in {numref}`Figure %s <Fig:LinesAndPlanes:DisjointPlanes>`. Notice that $\mathcal{P}_1$ and $\mathcal{P}_2$ do have points in common, but there are no points that are on all three planes.


````{figure}  Images/Fig-LinesAndPlanes-DisjointPlanes.svg
:name: Fig:LinesAndPlanes:DisjointPlanes

Three planes without a point in common.
````

In {numref}`Figure %s <Fig:LinesAndPlanes:PlanesPointIntersection>` we see three planes $\mathcal{P}_1$, $\mathcal{P}_2$ and $\mathcal{P}_3$ in $\mathbb{R}^3$ that have exactly one point in common. This is the only possibility where three planes have a finite number of points in common. The number of points in common can never be more than one, but less than infinite.


````{figure}  Images/Fig-LinesAndPlanes-PlanesPointIntersection.svg
:name: Fig:LinesAndPlanes:PlanesPointIntersection

Three planes with one point in common.
````

There are several circumstances where three planes have an infinite number of points in common. It is, for example, possible that the three planes have a common line of intersection, such as in {numref}`Figure %s <Fig:LinesAndPlanes:PlanesLineIntersection>`.


````{figure}  Images/Fig-LinesAndPlanes-PlanesLineIntersection.svg
:name: Fig:LinesAndPlanes:PlanesLineIntersection

Three planes with line of intersection.
````

It is of course also possible that the three planes coincide. In this case the points that all three planes have in common do not form a line, but an entire plane in $\mathbb{R}^3$. Take for example the planes that are defined by the Cartesian equations $-x+2y+z=1$, $2x-4y-2z=-2$ and $-3x+6y+3z=3$. Since the three equations are multiples of each other we know that they all describe the same collection of points.

## Lines in the space $\mathbb{R}^3$ 

There are multiple ways to describe a line in $\mathbb{R}^3$, but for us the parametric will suffice. In {numref}`Subsec:LinesAndPlanes:ParametricLine` we saw that we can describe a line in $\mathbb{R}^2$ with a parametric vector equation using a vector $\mathbf{v_0}$ that connects the origin to a point on the line and a vector parallel to the given line. The same idea works in the space $\mathbb{R}^3$.


````{prf:definition}  

Each non-zero vector $\mathbf{u}$ that is parallel to a line $\mathcal{L}$ will be called a *directional vector* of that line.
````

Let $\mathcal{L}$ be a line in $\mathbb{R}^3$, $\mathbf{v_0}$ a vector that connects the origin to a point on the line and $\mathbf{u}$ a directional vector of $\mathcal{L}$. In {numref}`Figure %s <Fig:LinesAndPlanes:ParametricLineSpace>` we can see that each vector $\mathbf{v}$ that connects the origin to a point on the line $\mathcal{L}$ can be written as the sum of the vector $\mathbf{v_0}$ and a multiple of the vector $\mathbf{u}$. This means that $\mathbf{v}=\mathbf{v_0}+r\mathbf{u}$ for some real number $r$.


````{figure}  Images/Fig-LinesAndPlanes-ParametricLineSpace.svg
:name: Fig:LinesAndPlanes:ParametricLineSpace

The line $\mathcal{L}$ in $\mathbb{R}^3$.
````


````{prf:definition}  

If $\mathbf{v_0}=\begin{bmatrix} x_0 \\ y_0 \\ z_0 \end{bmatrix}$ is a vector on the line $\mathcal{L}$ and $\mathbf{u}=\begin{bmatrix} a \\ b \\ c \end{bmatrix}$ is a directional vector of $\mathcal{L}$, then the equation 

$$
\begin{bmatrix} x \\ y \\ z \end{bmatrix}=\begin{bmatrix} x_0 \\ y_0 \\ z_0 \end{bmatrix}+r\begin{bmatrix} a \\ b \\ c \end{bmatrix} \qquad \textrm{$r$ in $\mathbb{R}$}
$$

will be called a *parametric vector equation* of $\mathcal{L}$.
````


````{admonition} Exercise  

How can we find a parametric vector equation for the line $\mathcal{L}$ that contains the points $P=(1, 2, 4)$ and $Q=(5, 3, 1)$? The vector $\mathbf{PQ}$ is parallel to $\mathcal{L}$ and therefore a directional vector. The components of this vector are equal to 

$$
\mathbf{PQ}=\begin{bmatrix} 5-1 \\ 3-2 \\ 1-4 \end{bmatrix}=\begin{bmatrix} 4 \\ 1 \\ -3 \end{bmatrix}.
$$

The equation 

$$
\begin{bmatrix} x \\ y \\ z \end{bmatrix}=\begin{bmatrix} 1 \\ 2 \\ 4 \end{bmatrix}+r\begin{bmatrix} 4 \\ 1 \\ -3 \end{bmatrix} \qquad \textrm{$r$ in $\mathbb{R}$}
$$

is thus a possible parametric vector equation of $\mathcal{L}$.
````