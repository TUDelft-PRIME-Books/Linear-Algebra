(Sec:GeomLinTrans)=

# Some Important Classes of Linear Transformations

We have seen in {numref}`Subsec:LinTrafo:LinTrafo` that any matrix corresponds to a linear transformation and that vice versa every linear transformation corresponds to a matrix. In this section, we will study some particularly noteworthy classes of linear transformations in more depth.

(Subsec:GeomLinTrans:Proj)=

## Projections

One of the simplest types of linear transformation takes a vector and sets one of its entries equal to $0$. For example, we can look at the linear transformation

$$
T:\mathbb{R}^{2}\to\mathbb{R}^{2},\quad\begin{bmatrix}a_{1}\\a_{2}\end{bmatrix}\mapsto \begin{bmatrix}a_{1}\\0\end{bmatrix}.
$$

Geometrically, this is the linear transformation which squashes the plane flat onto the $x$-axis. In slightly less informal terms, it is the transformation which projects the plane onto the $x$-axis.

Using the orthogonal projections defined
in {prf:ref}`Dfn:InnerProduct:OrthoProjectionOntoVector`, this can be generalised as follows. If $\mathbf{v}$ if a vector in $\mathbb{R}^{n}$, then

$$
T_{\mathbf{v}}:\mathbb{R}^{n}\to\mathbb{R}^{n},\quad\mathbf{w}\mapsto\text{proj}_{\mathbf{v}}(\mathbf{w})
$$

is the linear transformation which projects the vector $\mathbf{w}$ onto the line through $\mathbf{v}$. In other words, it maps a vector $\mathbf{w}$ to the closest multiple of $\mathbf{v}$. This transformation with

$$
\mathbf{v}=\begin{bmatrix}2\\1\end{bmatrix}
$$

can be seen on the left in {numref}`Figure %s <Fig:GeomLinTrans:ProjinR2>`. Let us briefly verify that it really is a linear transformation.

::::::{prf:proposition}
:label: Prop:Geometry:Projection

For any vector $\mathbf{v}$ in $\mathbb{R}^{n}$, the map

$$
T_{\mathbf{v}}:\mathbf{w}\mapsto\proj_{\mathbf{v}}(\mathbf{w})
$$

is a linear transformation.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:Geometry:Projection`
:class: tudproof

The proof is a simple application of the definitions. For any $\mathbf{w}_{1},\mathbf{w}_{2}$ in $\mathbb{R}^{n}$, we have

$$
\begin{align*}
T_{\mathbf{v}}(\mathbf{w}_{1}+\mathbf{w}_{2})&=\proj_{\mathbf{v}}(\mathbf{w}_{1}+\mathbf{w}_{2})=\frac{(\mathbf{w}_{1}+\mathbf{w}_{2})\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}}\mathbf{v}=\frac{\mathbf{w}_{1}\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}}\mathbf{v}+\frac{\mathbf{w}_{2}\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}}\mathbf{v}\\
&=\proj_{\mathbf{v}}(\mathbf{w}_{1})+\proj_{\mathbf{v}}(\mathbf{w}_{2})=T_{\mathbf{v}}(\mathbf{w}_{1})+T_{\mathbf{v}}(\mathbf{w}_{2}).
\end{align*}
$$

Similarly, for any $\mathbf{w}$ in $\mathbb{R}^{n}$ and any $c$ in $\mathbb{R}$ we have

$$
\begin{align*}
T_{\mathbf{v}}(c\mathbf{w})&=\proj_{\mathbf{v}}(c\mathbf{w})=\frac{(c\mathbf{w})\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}}=c\,\frac{\mathbf{w}\ip\mathbf{v}}{\mathbf{v}\ip\mathbf{v}}\mathbf{v}\\
&=c\,\proj_{\mathbf{v}}(\mathbf{w})=c\,T_{\mathbf{v}}(\mathbf{w}),
\end{align*}
$$

which finishes the proof.

::::::

The following proposition allows us to quickly find the standard matrix of the projection onto an arbitrary line in $\mathbb{R}^{2}$. This will be useful later on in this section, e.g. in the proof of {prf:ref}`Prop:GeomLinTrans:MatofReflinPlane`.

::::::{prf:proposition}
:label: Prop:GeomLinTrans:MatofProjonLine

Let $\mathcal{L}$ be the line in the plane that passes through the origin and that makes an angle of $\theta$ with the positive $x$-axis. The projection $T_{\mathcal{L}}$ on $\mathcal{L}$ has standard matrix

$$
P=\begin{bmatrix}\cos^{2}(\theta)&\sin(\theta)\cos(\theta)\\\sin(\theta)\cos(\theta)&\sin^{2}(\theta)\end{bmatrix}.
$$

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:GeomLinTrans:MatofProjonLine`
:class: tudproof

The vector

$$
\mathbf{v}=\begin{bmatrix}\cos(\theta)\\\sin(\theta)\end{bmatrix}
$$

is a unit vector on $\mathcal{L}$. Using the fact that $\mathbf{u}-\proj_{\mathcal{L}}(\mathbf{u})$ makes a right angle with $\mathcal{L}$ for any vector $\mathbf{u}$, we find that $\proj_{\mathcal{L}}(\mathbf{e}_{1})$ has length $\cos(\theta)$ (cf. {numref}`Figure %s <Fig:GeomLinTrans:MatofProjonLine>`). Since $\proj_{\mathcal{L}}(\mathbf{e}_{1})$ is a vector in the direction of $\mathbf{v}$ and since $\mathbf{v}$ has length $1$, the first column of $P$ is as claimed.

::::{figure} Images/Fig-GeomLinTrans-MatofProjonLine.svg
:name: Fig:GeomLinTrans:MatofProjonLine
:class: dark-light

The projection of $\mathbf{e}_{1}$ on the line $\mathcal{L}$ that makes an angle $\theta$ with the positive $x$-axis. Note that the length of $T_{\mathcal{L}}(\mathbf{e}_{1})$ is $\cos(\theta)$ since the length of $\mathbf{e}_{1}$ is $1$.
::::

That the second column is as claimed, too, can be shown analogously. We leave it as an exercise for the interested reader.

::::::

Often, you might have not the angle $\mathcal{L}$ makes with the positive $x$ axis, but rather a vector $\mathbf{v}$ on $\mathcal{L}$. In this case, too, you can find the standard matrix of the projection on $\mathcal{L}$ quite easily.

::::::{prf:proposition}
:label: Prop:GeomLinTrans:ProjMat2
Let $\mathcal{L}$ be a line that passes through the origin in the direction of $\mathbf{v}=\begin{bmatrix} v_{1}\\v_{2}\end{bmatrix}$. The projection $T_{\mathcal{L}}$ has standard matrix

$$
P=\frac{1}{v_{1}^{2}+v_{2}^{2}}\begin{bmatrix}
v_{1}^{2}&v_{1}v_{2}\\
v_{1}v_{2}&v_{2}^{2}
\end{bmatrix}.
$$

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:GeomLinTrans:ProjMat2`
:class: tudproof

It suffices to find the cosine and sine of the angle $\mathcal{L}$ makes with the positive $x$-axis in terms of $v_{1}$ and $v_{2}$. We leave this as an exercise.

::::::

One salient fact about these projections is that they act as the identity on their range. That is, for any vector $\mathbf{w}$ in the range of $T$ we have $T(T(\mathbf{w}))=T(\mathbf{w})$. This leads us to the following definition:

::::::{prf:definition}
A linear transformation $T:\mathbb{R}^{n}\to\mathbb{R}^{n}$ is called a **projection** if $T\circ T=T$.

::::::

::::::{prf:proposition}
:label: Prop:GeomLinTrans:ProjSquaredisProj

An $n\times n$-matrix $P$ is the standard matrix of a projection if and only if $P^{2}=P$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:GeomLinTrans:ProjSquaredisProj`
:class: tudproof

We leave this as an exercise.

::::::

It turns out that not all projections look like the ones discussed in Section {numref}`Sec:DotProduct`, not even if we restrict ourselves to a plane. Consider for example the following construction. Let $\mathbf{v}$ be any non-zero vector in $\mathbb{R}^{2}$ and let $\mathcal{L}$ be the line through $\mathbf{v}$ and the origin. Let $\mathbf{w}$ be a vector in $\mathbb{R}^{2}$ which does not lie on $\mathcal{L}$. For any vector $\mathbf{u}$, we define $\mathcal{L}_{\mathbf{u}}$ as the line through $\mathbf{u}$ in the direction $\mathbf{w}$. We now define the transformation $T$ which maps a vector $\mathbf{u}$ to the intersection of $\mathcal{L}_{\mathbf{u}}$ and $\mathcal{L}$. For

$$
\mathbf{v}=\begin{bmatrix}2\\1\end{bmatrix}\quad\text{and}\quad\mathbf{w}=\begin{bmatrix}-2\\1\end{bmatrix}
$$

this projection is depicted on the right in {numref}`Figure %s <Fig:GeomLinTrans:ProjinR2>`. It is an example of a non-orthogonal (or **oblique**) projection. Of course, we again have to check that this is really a linear transformation.

```{applet}
:url: geom_lin_trans/proj_in_r2
:fig: Images/Fig-GeomLinTrans-ProjinR2.svg
:name: Fig:GeomLinTrans:ProjinR2
:class: dark-light

On the left an orthogonal projection $T_{1}$ acting on a few selected vectors $\mathbf{u}_{1}$, $\mathbf{u}_{2}$, and $\mathbf{u}_{3}$. On the right a non-orthogonal projection $T_{2}$ acting on some selected vectors $\mathbf{v}_{1}$, $\mathbf{v}_{2}$, and $\mathbf{v}_{3}$. In both cases, the blue line represents the line $\mathcal{L}$ in the direction of $\begin{bmatrix}2\\1\end{bmatrix}$. On the left, every vector $\mathbf{u}_{i}$ is mapped to the closest vector that lies on $\mathcal{L}$. On the right, every vector $\mathbf{v}_{i}$ is mapped to the intersection of $\mathcal{L}$ wih the line through $\mathbf{v}_{i}$ in the direction given by $\begin{bmatrix}-2\\1\end{bmatrix}$.
```

::::::{prf:proposition}
:label: Prop:GeomLinTrans:MapToLine

Let $\mathcal{L}$ be a line through the origin and let $\mathbf{w}$ be a vector not on $\mathcal{L}$. The transformation $T:\mathbb{R}^{2}\to\mathbb{R}^{2}$ which maps a vector $\mathbf{u}$ to the intersection of $\mathcal{L}$ and the line through $\mathbf{u}$ in the direction of $\mathbf{w}$ is a linear transformation.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:GeomLinTrans:MapToLine`
:class: tudproof

For any vector $\mathbf{u}$, there is a unique pair of real numbers $(c_{\mathbf{u}},d_{\mathbf{u}})$ such that $\mathbf{u}+c_{\mathbf{u}}\mathbf{w}=d_{\mathbf{u}}\mathbf{v}$. What $T$ does is map $\mathbf{u}$ to $d_{\mathbf{u}}\mathbf{v}$. Hence, for any two vectors $\mathbf{u}_{1},\mathbf{u}_{2}$ in $\mathbb{R}^{2}$, we have
\begin{align*}
\mathbf{u}_{1}+c_{\mathbf{u}_{1}}\mathbf{w}&=d_{\mathbf{u}_{1}}\mathbf{v}=T(\mathbf{u}_{1})\quad\text{and}\\
\mathbf{u}_{2}+c_{\mathbf{u}_{2}}\mathbf{w}&=d_{\mathbf{u}_{2}}\mathbf{v}=T(\mathbf{u}_{2}).\\
\end{align*}
Clearly, we also have

$$
(\mathbf{u}_{1}+\mathbf{u}_{2})+(c_{\mathbf{u}_{1}}+c_{\mathbf{u}_{2}})\mathbf{w}=(d_{\mathbf{u}_{1}}+d_{\mathbf{u}_{2}})
\mathbf{v}
$$

so $T(\mathbf{u}_{1}+\mathbf{u}_{2})=(d_{\mathbf{u}_{1}}+d_{\mathbf{u}_{2}})
\mathbf{v}=T(\mathbf{u_{1}})+T(\mathbf{u}_{2})$. The proof that $T(c\mathbf{u})=cT(\mathbf{u})$ for any $\mathbf{u}$ in $\mathbb{R}^{2}$ and any scalar $c$ is analogous. We leave it as an exercise.

::::::

Let us try to find the standard matrix of the transformation $T$ we just defined. Its first column is the intersection of $\mathcal{L}$ with $\mathcal{L}_{e_{1}}$. This intersection is given by:

$$
\begin{bmatrix}1\\0\end{bmatrix}+t\begin{bmatrix}-2\\1\end{bmatrix}=s\begin{bmatrix}2\\1\end{bmatrix} \Longleftrightarrow \begin{cases} 1=2s+2t\\0=s-t\end{cases}\Longleftrightarrow s=t=\frac{1}{4}
$$

so $T(e_{1})=\begin{bmatrix}\frac{1}{2}\\\frac{1}{4}\end{bmatrix}$. The second column of the standard matrix of $T$ is the intersection of $\mathcal{L}$ with $\mathcal{L}_{e_{2}}$. We find this intersection in a similar fashion:

$$
\begin{bmatrix}0\\1\end{bmatrix}+t\begin{bmatrix}-2\\1\end{bmatrix}=s\begin{bmatrix}2\\1\end{bmatrix}
\Longleftrightarrow \begin{cases}0=2s+2t\\1=s-t\end{cases}\Longleftrightarrow \frac{1}{2}=s=-t
$$

so $T(e_{2})=\begin{bmatrix}1\\\frac{1}{2}\end{bmatrix}$ and we conclude that the standard matrix of $T$ is

$$
P=\begin{bmatrix}
\frac{1}{2}&1\\\frac{1}{4}&\frac{1}{2}\label{Eq:GeomLinTrans:StandMatofProj}
\end{bmatrix}.
$$

We can also consider projections in three dimensional space (cf. {numref}`Figure  %s <Fig:GeomLinTrans:3DProj>`). If $\mathbf{v}$ is a vector in $\mathbb{R}^{3}$ and $\mathcal{L}$ is the line in the direction of $\mathbf{v}$, then

$$
P:\mathbb{R}^{3}\to\mathbb{R}^{3},\quad\mathbf{w}\mapsto \proj_{\mathbf{v}}(\mathbf{w})
$$

gives the orthogonal projection of the vector $\mathbf{w}$ on $\mathcal{L}$.
We can also consider the orthogonal projection on a plane in three dimensional space. Suppose the plane $\mathcal{P}$ is spanned by $\mathbf{v}_{1}$ and $\mathbf{v}_{2}$ and assume $\mathbf{v}_{1}\ip\mathbf{v}_{2}=0$, that is, assume $\mathbf{v}_{1}$ and $\mathbf{v}_{2}$ are orthogonal and non-zero. Then

$$
P:\mathbb{R}^{3}\to\mathbb{R}^{3},\mathbf{w}\mapsto \proj_{\mathbf{v}_{1}}(\mathbf{w})+\proj_{\mathbf{v}_{2}}(\mathbf{w})
$$

gives the projection on $\mathcal{P}$.

```{applet}
:url: geom_lin_trans/3d_proj_on_line
:fig: Images/Fig-GeomLinTRans-3DProjonLine.svg
:name: Fig:GeomLinTrans:3DProj
:status: reviewed
:class: dark-light

Projections on a line $\mathcal{L}$ in three dimensional space. 
```

Let us briefly discuss what happens in higher dimensions.
Suppose $\mathbf{v}_{1},...,\mathbf{v}_{k}$ are non-zero
vectors in $\mathbb{R}^{n}$ which are all orthogonal to each other,
i.e. $\mathbf{v}_{i} \ip\mathbf{v}_{j}=0$ for all $i$ and $j$.
Put $V=\Span{\mathbf{v}_{1},...,\mathbf{v}_{k}}$.
For any vector $\mathbf{w}$ in $\mathbb{R}^{n}$ we can define the
**orthogonal projection** on $V$ as

$$
\proj_{V}(\mathbf{w})=\proj_{\mathbf{v}_{1}}(\mathbf{w})+\proj_{\mathbf{v}_{2}}(\mathbf{w})+\cdots+\proj_{\mathbf{v}_{k}}(\mathbf{w}).
$$

Projections, especially orthogonal projections, play a very important role in linear algebra and we will encounter them quite a bit more in later sections.

## Reflections

A second important class of linear transformations with a very natural geometric interpretation is that of reflections. Let us consider a simple example. Suppose we let $\mathcal{L}$ be the line in the plane through

$$
\mathbf{0}\quad\text{and in the direction of}\quad \mathbf{v}=\begin{bmatrix}1\\1\end{bmatrix}.
$$

We can define a transformation $T$ which reflects points in the plane along $\mathcal{L}$. That is, we can imagine $\mathcal{L}$ to act as a kind of mirror, sending points on one side of $\mathcal{L}$ to their reflection on the other side. (See {numref}`Figure %s <Fig:GeomLinTrans:ReflinR2>`.) It is easy to find the standard matrix $M$ of this transformation: the first standard basis vector $\mathbf{e}_{1}$ is mapped to $\mathbf{e}_{2}$ and, similarly, $\mathbf{e}_{2}$ is mapped to $\mathbf{e}_{1}$, so

$$
M=\begin{bmatrix}0&1\\1&0\end{bmatrix}.
$$

```{applet}
:url: geom_lin_trans/reflect_in_r2
:fig: Images/Fig-GeomLinTrans-ReflinR2.svg
:name: Fig:GeomLinTrans:ReflinR2
:status: reviewed
:class: dark-light

The reflection along the line $\mathcal{L}$ in the direction of $\mathbf{v}=\begin{bmatrix}1\\1\end{bmatrix}$. The vectors in red are mapped to the vector in blue by this reflection.
```

So far so good. But how do we find the reflection over an arbitrary line $\mathcal{L}$? It turns out that the projections we have seen in Section {ref}`Subsec:GeomLinTrans:Proj` will help us out. Consider a line $\mathcal{L}$ and a vector $\mathbf{v}$ not in $\mathcal{L}$, as in {numref}`Figure %s <Fig:GeomLinTrans:ReflFromDoubleProj>`. In order to reflect $\mathbf{v}$ over $\mathcal{L}$, we first move it to the closest point on $\mathcal{L}$ and then move it the same distance again in the same direction.

The closest point to $\mathbf{v}$ on $\mathcal{L}$ is the orthogonal projection $\text{proj}_{\mathcal{L}}(\mathbf{v})$. To get from $\mathbf{v}$ to the closest point on $\mathcal{L}$, we therefore have to subtract $\mathbf{v}-\text{proj}_{\mathcal{L}}(\mathbf{v})$ from $\mathbf{v}$ (See {numref}`Figure %s <Fig:GeomLinTrans:ReflFromDoubleProj>`.). So in order to reflect $\mathbf{v}$ over $\mathcal{L}$, we have to subtract the vector $\mathbf{v}-\text{proj}_{\mathcal{L}}(\mathbf{v})$ twice from our starting vector $\mathbf{v}$. This means that any $\mathbf{v}$ is mapped to $2\proj_{\mathcal{L}}(\mathbf{v})-\mathbf{v}$, so if we write $T$ for this transformation we find

$$
T(\mathbf{v})=2\proj_{\mathcal{L}}(\mathbf{v})-\mathbf{v}=(2\proj_{\mathcal{L}}-I)\mathbf{v}.
$$

::::{figure} Images/Fig-GeomLinTrans-ReflFromDoubleProj.svg
:name: Fig:GeomLinTrans:ReflFromDoubleProj
:class: dark-light

Reflection along the line $\mathcal{L}$ can be seen as the transformation $2\proj_{\mathcal{L}}-I$.
::::

Keeping this in mind, it makes sense to define general reflections as follows.

::::::{prf:definition}
If $T:\mathbb{R}^{n}\to\mathbb{R}^{n}$ is the orthogonal projection on $\text{range}(T)$ with standard matrix $P$, then

$$
S:\mathbb{R}^{n}\to\mathbb{R}^{n},\mathbf{v}\mapsto (2P-I)\mathbf{v}
$$

is the **reflection** over $\text{range}(T)$.

::::::

Since any reflection is a linear combination of some projection and the identity, we arrive at the following proposition.

::::::{prf:proposition}
:label: Prop:GeomLinTrans:Reflection

Any reflection is a linear transformation.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:GeomLinTrans:Reflection`
:class: tudproof

A reflection is by definition a sum of scaled linear transformations. As such, it is again a linear transformation.

::::::

The following proposition guarantees that, as you would expect, applying a reflection twice leaves you back where you started.

::::::{prf:proposition}
:label: Prop:GeomLinTrans:TwoReflections

If $M$ is the standard matrix of a reflection, then $R^{2}=I$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:GeomLinTrans:TwoReflections`
:class: tudproof

We know that $M=2P-I$ where $P$ is the standard matrix of some projection. By {prf:ref}`Prop:GeomLinTrans:ProjSquaredisProj`, we have $P^{2}=P$ and therefore

$$
M^{2}=(2P-I)(2P-I)=4P^{2}-4P+I=I.
$$

::::::

The definition of a reflection in combination with {prf:ref}`Prop:GeomLinTrans:MatofProjonLine` allows us to find the standard matrix for the reflection along any line through the origin in $\mathbb{R}^{2}$.

::::::{prf:proposition}
:label: Prop:GeomLinTrans:MatofReflinPlane

Let $\mathcal{L}$ be the line in the plane that passes through the origin and that makes an angle $\theta$ with the positive $x$-axis. The standard matrix of the reflection along $\mathcal{L}$ is

$$
M_{\mathcal{L}}=2\begin{bmatrix}\cos^{2}(\theta)&\sin(\theta)\cos(\theta)\\\sin(\theta)\cos(\theta)&\sin^{2}(\theta)\end{bmatrix}-I_{2}=\begin{bmatrix}\cos(2\theta)&\sin(2\theta)\\\sin(2\theta)&-\cos(2\theta)\end{bmatrix}.
$$

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:GeomLinTrans:MatofReflinPlane`
:class: tudproof

Exercise. For the second equality, remember the trigonometric identities

$$
\sin(2\theta)=2\sin(\theta)\cos(\theta)\quad\text{and}\quad\cos(2\theta)=2\cos^{2}(\theta)-1=1-2\sin^{2}(\theta).
$$

::::::

For large $n$ it is hard to picture what a reflection in $n$-dimensional space does. But for $n=3$ it is still doable. In fact, it is done in {numref}`Figure %s <Fig:GeomLinTrans:3DReflalongPlane>`.

```{applet}
:url: geom_lin_trans/3d_refl_along_plane
:fig: Images/Fig-GeomLinTRans-3DReflalongPlane.svg
:name: Fig:GeomLinTrans:3DReflalongPlane
:status: reviewed
:class: dark-light

Reflection along the plane $\mathcal{P}$ in $\mathbb{R}^{3}$.

```

One particularly interesting aspect of reflections is that they preserve lengths of vectors and angles between vectors. This is a consequence of {prf:ref}`Prop:GeomLinTrans:ReflDotProd`.

::::{prf:proposition}
:label: Prop:GeomLinTrans:ReflDotProd

If $S$ is a reflection defined on $\R^{n}$, then for any $\vect{w}_{1},\vect{w}_{2}$ in $\R^{n}$ we have:

$$S(\vect{w}_{1})\cdot S(\vect{w}_{2})=\vect{w}_{1}\cdot\vect{w}_{2}.$$

::::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:GeomLinTrans:ReflDotProd`
:class: tudproof

By definition, there is an orthogonal projection with standard matrix $P$ such that $S(\vect{w})=(2P-I)\vect{w}$. We assume $P$ is the projection on the span of a single vector $\vect{v}$. If there are more, the computations become considerably messier, but neither harder nor more enlightening.

\begin{align*}
S(\vect{w}_{1})\cdot S(\vect{w}_{2})&=(2P-I)\vect{w}_{1}\cdot(2P-I)\vect{w}_{2}\\
&=(2\left(\frac{\vect{w_{1}}\cdot\vect{v}}{\vect{v}\cdot\vect{v}}\right)\vect{v}-\vect{w}_{1})\cdot (2\left(\frac{\vect{w_{2}}\cdot\vect{v}}{\vect{v}\cdot\vect{v}}\right)\vect{v}-\vect{w}_{2})\\
&=4\left(\frac{\vect{w}_{1}\cdot \vect{v}}{\vect{v}\cdot\vect{v}}\right)\left(\frac{\vect{w}_{2}\cdot \vect{v}}{\vect{v}\cdot\vect{v}}\right)\vect{v}\cdot\vect{v}-2\left(\frac{\vect{w}_{2}\cdot \vect{v}}{\vect{v}\cdot\vect{v}}\right)\vect{w}_{1}\cdot\vect{v}-2\left(\frac{\vect{w}_{1}\cdot \vect{v}}{\vect{v}\cdot\vect{v}}\right)\vect{w}_{2}\cdot\vect{v}+\vect{w}_{1}\cdot\vect{w}_{2}\\
&=\vect{w}_{1}\cdot\vect{w}_{2}
\end{align*}

which proves the claim.

:::

## Rotations

As we have seen in {prf:ref}`Prop:GeomLinTrans:ReflDotProd`, reflections preserve the dot product and therefore lengths of vectors and the angles between vectors. However, there are other transformations that do so. These other transformations are the rotations. Let us start with the definition.

::::::{prf:definition}
A **rotation** is a transformation $T:\mathbb{R}^{n}\to\mathbb{R}^{n}$ that is not a reflection but such that for any $\mathbf{v}_{1},\mathbf{v}_{2}$ in $\mathbb{R}^{n}$ we have:

$$T(\vect{v}_{1})\cdot T(\vect{v}_{2})=\vect{v}_{1}\cdot\vect{v}_{2}.$$

For convenience, we will also call the identity transformation a rotation, even though it is the reflection over all of $\mathbb{R}^{n}$.

::::::

::::::{prf:proposition}
:label: Prop:GeomLinTrans:RotsAreLinTrans

Rotations are linear transformations.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:GeomLinTrans:RotsAreLinTrans`
:class: tudproof

Let $T:\mathbb{R}^{n}\to\mathbb{R}^{n}$ be a rotation. Because of {prf:ref}`Prop:InnerProduct:DotProdGeometric`, we have $\mathbf{v}_{1}\ip \mathbf{v}_{2}=T(\mathbf{v}_{1})\ip T(\mathbf{v}_{2})$. A tedious but not terribly hard calculation now shows that, for every $\mathbf{v}_{1},\mathbf{v}_{2}$ in $\mathbb{R}^{n}$,

$$
\lVert T(\mathbf{v}_{1}+\mathbf{v}_{2})-T(\mathbf{v}_{1})-T(\mathbf{v}_{2})\rVert ^{2}=\lVert \mathbf{v}_{1}+\mathbf{v}_{2}-\mathbf{v}_{1}-\mathbf{v}_{2}\rVert^{2}=0.
$$

This implies that $T(\mathbf{v}_{1}+\mathbf{v}_{2})-T(\mathbf{v}_{1})-T(\mathbf{v}_{2})=\mathbf{0}$, hence $T(\mathbf{v}_{1}+\mathbf{v}_{2})=T(\mathbf{v}_{1})+T(\mathbf{v}_{2})$.

Similarly, one can show that for any vector $\mathbf{v}$ in $\mathbb{R}^{n}$ and any scalar $c$, we have

$$
\lVert T(c\mathbf{v})-cT(\mathbf{v})\rVert^{2}=\lVert c\mathbf{v}-c\mathbf{v}\rVert^{2}=0.
$$

This then implies $T(c\mathbf{v})-cT(\mathbf{v})=\mathbf{0}$ whence $T(c\mathbf{v})=cT(\mathbf{v})$. In conclusion: $T$ is a linear transformation.

::::::

In fact, the proof of {prf:ref}`Prop:GeomLinTrans:RotsAreLinTrans` only uses the fact that rotations preserve the inner product. It therefore also shows that reflections are linear transformations, but we have already established that using a simpler argument.

The name _rotation_ is inspired by the following observation about rotations in the plane.

::::::{prf:proposition}
:label: Prop:GeomLinTrans:RotMatR2

For any real number $\theta$, the rotation over the angle $\theta$ in the plane has standard matrix

$$
R_{\theta}=\begin{bmatrix}
	\cos(\theta)&-\sin(\theta)\\
	\sin(\theta)&\cos(\theta)
\end{bmatrix}.


$$

This is indeed the standard matrix of a rotation.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:GeomLinTrans:RotMatR2`
:class: tudproof

Suppose we take the vector $\mathbf{e}_{1}$ and rotate it (counterclockwise) over an angle $\theta$. Where do we end up? By definition, the $x$-coordinate of our new location will be $\cos(\theta)$ and its $y$-coordinate will be $\sin(\theta)$. Similarly, if we start with the vector $\mathbf{e}_{2}$ and rotate that over the angle $\theta$, the $x$-coordinate of our new point will be $-\sin(\theta)$. This is illustrated in {numref}`Figure %s <Fig:GeomLinTrans:RotinPlane>`.

::::{figure} Images/Fig-GeomLinTrans-RotinPlane.svg
:name: Fig:GeomLinTrans:RotinPlane
:class: dark-light

The rotation over the angle $\theta$ working on $\mathbf{e}_{1}$ and $\mathbf{e}_{2}$. Note that the distance between $R_{\theta}\mathbf{e}_{2}$ and the vertical axis is $\sin(\theta)$ but, as $R_{\theta}\mathbf{e}_{2}$ lies to the left of the vertical axis, the first entry of $R_{\theta}\mathbf{e}_{2}$ is $-\sin(\theta)$.
::::

To show that $R_{\theta}$ is indeed the standard matrix of a rotation, we first note that it is only a reflection if it is the identity matrix. We leave it as an exercise to check that $(R_{\theta}\vect{v}_{1})\cdot (R_{\theta}\vect{v}_{2})=\vect{v}_{1}\cdot \vect{v}_{2}$ for any $\vect{v}_{1},\vect{v}_{2}$ in $\R^{2}$.
::::::

Alternatively, one can describe a rotation in the plane as a combination of two reflections. We make this precise in the following proposition, which is illustrated in {numref}`Figure %s <Fig:GeomLinTrans:RotisDoubleRefl>`.

::::::{prf:proposition}
:label: Prop:GeomLinTrans:RotisDoubleRefl

Any rotation in the plane is the composition of two reflections.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:GeomLinTrans:RotisDoubleRefl`
:class: tudproof

We will show that the standard matrix $R_{\theta}$ of the rotation $T_{\theta}$ over an angle $\theta$ is the product of the standard matrices of two reflections. The claim follows then from the definition of the matrix product.

Let $\mathcal{L}_{1}$ and $\mathcal{L}_{2}$ be two lines in the plane through the origin that make an angle of $\theta/2$ with each other. If we call $\phi/2$ the angle $\mathcal{L}_{1}$ makes with the positive $x$-axis, we can conclude that $\mathcal{L}_{2}$ makes an angle of $\phi/2+\theta/2$ with the positive $x$-axis. From {prf:ref}`Prop:GeomLinTrans:MatofReflinPlane`, we know that the standard matrices of the reflections $T_{\mathcal{L}_{1}}$ and $T_{\mathcal{L}_{2}}$ along $\mathcal{L}_{1}$ and $\mathcal{L}_{2}$, respectively, are

$$
M_{\mathcal{L}_{1}}=\begin{bmatrix}\cos(\phi)&\sin(\phi)\\\sin(\phi)&-\cos(\phi)\end{bmatrix}\quad
\text{and}\quad M_{\mathcal{L}_{2}}=\begin{bmatrix}\cos(\theta+\phi)&\sin(\theta+\phi)\\
\sin(\theta+\phi)&-\cos(\theta+\phi)\end{bmatrix},


$$

respectively. Using the fact that, for any angles $\alpha$ and $\beta$, we have the identities
\begin{align*}
\cos(\alpha-\beta)&= \cos(\alpha)\cos(\beta)+\sin(\alpha)\sin(\beta)\quad\text{and}\\
\sin(\alpha-\beta)&=\sin(\alpha)\cos(\beta)-\sin(\beta)\cos(\alpha),
\end{align*}
we find

$$
M_{\mathcal{L}_{2}}M_{\mathcal{L}_{1}}=\begin{bmatrix}
\cos(\theta)&\sin(-\theta)\\\sin(\theta)&\cos(\theta)
\end{bmatrix}=R_{\theta}.


$$

::::::

```{applet}
:url: geom_lin_trans/rotisdoublerefl
:fig: Images/Fig-GeomLinTrans-RotisDoubleRefl.svg
:name: Fig:GeomLinTrans:RotisDoubleRefl
:class: dark-light

{prf:ref}`Prop:GeomLinTrans:RotisDoubleRefl` illustrated. $\mathcal{L}_{1}$ and $\mathcal{L}_{2}$ are arbitrary lines that make an angle of $\theta/2$ with each other. Composing the reflections along $\mathcal{L}_{1}$ and $\mathcal{L}_{2}$ then gives the rotation over the angle $\theta$. This is shown for the particular vector $\mathbf{v}$. Note that the angle $\phi/2$ that $\mathcal{L}_{1}$ makes with the positive $x$ axis is irrelevant to the proof.
```

In the plane, you can only rotate around the origin. Things get considerably more complicated if we move to $\mathbb{R}^{3}$, because there you can rotate around any arbitrary line. We will not get into that here.

## Shear Transformations

The last class of linear transformation we will deal with in this section are the shear transformations. These are transformations which fix a certain line through the origin, $\mathcal{L}$ say, and shift all other points parallel to $\mathcal{L}$.

::::::{prf:example}
:label: Ex:GeomLinTrans:ShearTrans

Consider the linear transformation

$$
T:\mathbb{R}^{2}\to\mathbb{R}^{2},\quad \mathbf{v}\mapsto \begin{bmatrix}2&-1\\1&0\end{bmatrix}\mathbf{v}.


$$

The action of $T$ is illustrated in {numref}`Figure %s <Fig:GeomLinTrans:ShearTrans>`. Consider furthermore the line

$$
\mathcal{L}=\left\{\begin{bmatrix}c\\c\end{bmatrix}\mid c\text{ in }\mathbb{R}\right\}=\left\{c\mathbf{w}\mid c\text{ in }\mathbb{R}\right\}\quad \text{where}\quad\mathbf{w}=\begin{bmatrix}1\\1\end{bmatrix},


$$

i.e. the line through the origin in the direction of $\mathbf{w}$. Any vector $c\mathbf{w}$ in $\mathcal{L}$ is fixed:

$$
T(c\mathbf{w})=\begin{bmatrix}2&-1\\1&0\end{bmatrix}\begin{bmatrix}c\\c\end{bmatrix}=\begin{bmatrix}c\\c
\end{bmatrix}.


$$

What happens with vectors not in $\mathcal{L}$? Take two scalars $c$ and $d$ which are not equal. Then

$$
T\left(\begin{bmatrix}c\\d\end{bmatrix}\right)=\begin{bmatrix}2&-1\\1&0\end{bmatrix}\begin{bmatrix}c\\d
\end{bmatrix}=\begin{bmatrix}2c-d\\c\end{bmatrix}=\begin{bmatrix}c\\d\end{bmatrix}+\begin{bmatrix}c-d\\c-d\end{bmatrix},


$$

so $T$ moves points not on $\mathcal{L}$ parallel to $\mathcal{L}$. Points closer to $\mathcal{L}$ get moved a smaller distance than points further away from $\mathcal{L}$. Points to the left of $\mathcal{L}$, i.e. points for which $c<d$, get moved to the left. Points to the right of $\mathcal{L}$, i.e. points for which $c>d$, get moved to the right.

::::::

```{applet}
:url: geom_lin_trans/sheartrans
:fig: Images/Fig-GeomLinTrans-ShearTrans.svg
:name: Fig:GeomLinTrans:ShearTrans
:class: dark-light

The shear transformation $T$ from Example {numref}`Figure %s <Fig:GeomLinTrans:ShearTrans>` working on the vectors
$\mathbf{e}_{1}=\begin{bmatrix}1\\0\end{bmatrix}$ and $\mathbf{v}=\begin{bmatrix}-1\\1\end{bmatrix}$. Note how the distance between a vector and the line $\mathcal{L}$ is preserved by $T$. As a consequence, the area of the green and blue parallelogams on the left is the same as that of their respective images on the right.
```

::::::{prf:definition}
:label: Dfn:GeomLinTrans:ShearScale

A linear transformation $T:\mathbb{R}^{2}\to\mathbb{R}^{2}$ is called a **shear transformation**, or simply a **shear**, if there is some line $\mathcal{L}$ and some vector $\mathbf{w}$ in $\mathcal{L}$ such that

<ol type="i">
<li>

$T(\mathbf{v})=\mathbf{v}$ for all $\mathbf{v}$ on $\mathcal{L}$;

</li>
<li id="Item:GeomLinTrans:ShearScale">

for every vector $\mathbf{v}$ in $\mathbb{R}^{2}$ there is a scalar $c$ such that we have

$$
T(\mathbf{v})=\mathbf{v}+c\mathbf{w}.
$$

</li>
</ol>

::::::

Note that the scalar $c$ in [ii.](#Item:GeomLinTrans:ShearScale) from {prf:ref}`Dfn:GeomLinTrans:ShearScale` is different for different vectors. For vectors lying on one side of $\mathcal{L}$, it will be positive. For vectors on the other side of $\mathcal{L}$ it will be negative. Moreover, for vectors further away from $\mathcal{L}$, $c$ will be larger than for vectors closer to $\mathcal{L}$.

::::::{prf:proposition}
:label: Prop:GeomLinTrans:ShearTransDistance

If $T$ is a shear transformation fixing the line $\mathcal{L}$ and $\mathbf{v}$ is an arbitrary vector in $\mathbb{R}^{2}$, then the distance from $\mathbf{v}$ to $\mathcal{L}$ is the same as the distance from $T(\mathbf{v})$ to $\mathcal{L}$.

::::::

::::::{admonition} Proof of&nbsp;{prf:ref}`Prop:GeomLinTrans:ShearTransDistance`
:class: tudproof

The distance between a vector $\mathbf{v}$ and a line $\mathcal{L}$ is the length of $\mathbf{v}-\proj_{\mathcal{L}}(\mathbf{v})$. We find, for arbitrary $\mathbf{v}$ in $\mathbb{R}^{2}$,
\begin{align*}
\lVert T(\mathbf{v})-\proj_{\mathcal{L}}(T(\mathbf{v}))\rVert &= \lVert \mathbf{v}+c\mathbf{w}-\frac{(\mathbf{v}+c\mathbf{w})\ip\mathbf{w}}{\mathbf{w}\ip\mathbf{w}}\mathbf{w}\rVert=\lVert \mathbf{v}-\frac{\mathbf{v}\ip\mathbf{w}}{\mathbf{w}\ip\mathbf{w}}\mathbf{w}\rVert\\
&=\lVert \mathbf{v} -\proj_{\mathcal{L}}\mathbf{v}\rVert
\end{align*}
which had to be proven.

::::::

We can introduce a similar concept in $\mathbb{R}^{3}$, but now we need the transformation $T$ to fix not a line but rather a plane.

::::::{prf:definition}
:label: Item:GeomLinTrans:ShearScale

A linear transformation $T:\mathbb{R}^{3}\to\mathbb{R}^{3}$ is called a **shear transformation**, or simply a **shear**, if there is some plane $\mathcal{P}$ in $\mathbb{R}^{3}$ and some vector $\mathbf{w}$ in $\mathcal{P}$ such that

<ul>
<li>

$T(\mathbf{v})=\mathbf{v}$ for all $\mathbf{v}$ on $\mathcal{P}$;

</li>
<li id="Item:GeomLinTrans:ShearScale">

for every vector $\mathbf{v}$ in $\mathbb{R}^{3}$ there is a scalar $c$ such that we have

$$
T(\mathbf{v})=\mathbf{v}+c\mathbf{w}.
$$

</li>
</ul>

::::::

::::::{prf:example} Application

Suppose we have a standard deck of $52$ perfectly rectangular playing cards placed in a stack on a table. A standard playing card is about $87$ by $56$ millimeters, so we can assume that the corners of the lowest card are on

$$
\begin{bmatrix}0\\0\\0\end{bmatrix},\quad\begin{bmatrix}87\\0\\0\end{bmatrix},\quad\begin{bmatrix}0\\56\\0\end{bmatrix},\quad\text{and}\quad\begin{bmatrix}87\\56\\0\end{bmatrix},


$$

respectively. A playing card typically has a thickness of about $0.2$ millimeter, so the coordinates of the top card of the stack will be

$$
\begin{bmatrix}0\\0\\10.4\end{bmatrix},\quad\begin{bmatrix}87\\0\\10.4\end{bmatrix},\quad\begin{bmatrix}0\\56\\10.4\end{bmatrix},\quad\text{and}\quad\begin{bmatrix}87\\56\\10.4\end{bmatrix},


$$

respectively. If we now move the top card along the $x$-axis, then, due to friction, the second card will also move. This in turn will make the third card move and so on. If we assume friction with the table is high enough, the bottom card will approximately remain in place. This situation is depicted in {numref}`Figure %s <Fig:GeomLinTrans:CardsStack>`.

The movement of the cards can be described by a shear transformation. If the top card is moved 6 millimeters along the $x$-axis, then the edges parallel to the $y$-axis of the cards will make an angle of $\phi=\arctan(10.4/6)\approx \frac{\pi}{3}$ with the positive $x$-axis. A card at height $h$ will be moved a distance of about $h\frac{1}{\sqrt{3}}$ along the $x$-axis. We therefore find that the standard matrix associated to the linear transformation that describes the movement of the cards is

$$
\begin{bmatrix}1&0&\frac{1}{\sqrt{3}}\\0&1&0\\0&0&1\end{bmatrix}.


$$

Shear transformations are widely used to model this kind of displacement of layered media. For example in materials science or crystallography.

::::::

::::{figure} Images/Fig-GeomLinTrans-CardsStack.svg
:name: Fig:GeomLinTrans:CardsStack
:class: dark-light

A shear transformation applied to a stack of cards.
::::

## Grasple Exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1531c9ba-540c-4d64-bddf-169105eaa5ff?id=70393
:label: grasple_exercise_3_3_1
:dropdown:
:description: Give a geometric description for transformation with given standard matrix.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/51095023-d860-483f-8758-44d2b83d7c9e?id=70394
:label: grasple_exercise_3_3_2
:dropdown:
:description: Give a geometric description for transformation with given standard matrix.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5eae3328-453b-4065-9829-be8acb10f0fa?id=70421
:label: grasple_exercise_3_3_3
:dropdown:
:description: Give the standard matrix from a geometric desciption.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/cf49c839-9eee-4f7b-b459-cfe3edcf530b?id=70422
:label: grasple_exercise_3_3_4
:dropdown:
:description: Give the standard matrix from a geometric desciption.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/aca8c030-4392-4e22-be38-2316f9c483c4?id=70425
:label: grasple_exercise_3_3_5
:dropdown:
:description: Give the standard matrix from a geometric desciption.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e67fb238-1b3e-4cad-bbb2-4126579fa97f?id=78593
:label: grasple_exercise_3_3_6
:dropdown:
:description: Two transformations and their composition.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/795b979c-e3d9-4f24-80ad-0dfad38c84d2?id=83137
:label: grasple_exercise_3_3_7
:dropdown:
:description: Investigating a specific transformation.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7d10562b-929a-4b1f-9a90-6280e12b9c98?id=85261
:label: grasple_exercise_3_3_8
:dropdown:
:description: Understanding a shear transformation.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ee24dead-8281-493e-9ced-b2f0f9cb1421?id=85263
:label: grasple_exercise_3_3_9
:dropdown:
:description: Understanding shear transformations.

::::
