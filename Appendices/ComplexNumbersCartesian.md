(Ch:ComplexNumbersCartesian)=
# Cartesian form of complex numbers

## Introduction

Consider the equation

:::{math}
:label: Eq:ComplexNumbers:abc-eq
ax^2+bx+c=0,

:::

where $a\neq0$. Previously you probably learned that Equation {eq}`Eq:ComplexNumbers:abc-eq` only has solutions when $D=b^2-4ac$ was non-negative and in that case you would have the two solutions

:::{math}
:label: Eq:ComplexNumbers:abc-sol
x_{1,2}=\frac{-b\pm\sqrt{D}}{2a}.

:::

Now consider the case that you _really_ need solutions of Equation {eq}`Eq:ComplexNumbers:abc-eq` even if $D$ is negative. This might sound strange, but you will encounter this case in many engineering applications, for example in solving second-order linear differential equations. It turns out that the solution in Equation {eq}`Eq:ComplexNumbers:abc-sol` is still valid when $D<0$, which means that you need to take the square root of a negative number.

Luckily, mathematicians have found a way to handle this, namely complex numbers. Before we start treating complex numbers, we first need to introduce the special number $i$. After that, we will introduce the complex numbers and some other terminologies.

## Complex numbers

**Definitions**

We start with considering an easier form of Equation {eq}`Eq:ComplexNumbers:abc-eq`, namely

$$
x^2+1=0.
$$

From this equation we find that $D=-1$ and if we just straight forward apply Equation {eq}`Eq:ComplexNumbers:abc-sol`, we get

$$
x_{1,2}=\pm\sqrt{-1}.
$$

The square root of $-1$ obviously is a problem. Therefore we introduce the special number $i$:

::::{prf:definition}
:label: Def:ComplexNumbers:i

The **imaginary unit** $i$ is a number defined by the equation

:::{math}
:label: Eq:ComplexNumbers:def-i

i^2=-1.

:::

::::

Because $i$ is defined to be a number (mind you, it is not a real number), we also assume $i$ behaves just like any normal number.

Using the imaginary unit $i$ we can prove the following theorem:

::::{prf:theorem}
:label: Thm:ComplexNumbers:roots

Let $a$ be a _positive_ real number. Then the two numbers $x_-=-ai$ and $x_+=ai$ are solutions to the equation $x^2=-a^2$.

::::

:::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:roots`
:class: tudproof, dropdown

First we consider $x_-=-ai$ and take its square:

$$
x_-^2 = \left(-ai\right)^2 = a^2i^2 = -a^2.
$$

This shows that $x_-=-ai$ is indeed a solution to the equation $x^2=-a^2$.

We repeat the same for $x_+=ai$:

$$
x_+^2 = \left(ai\right)^2 = a^2i^2 = -a^2.
$$

We also find that $x_+=ai$ is a solution to the equation $x^2=-a^2$.

:::

This means we can rewrite our two solutions as

$$
x_{1,2}=\pm i.
$$

Doesn't this already look simpler?

Now we have defined $i$, we can revisit the general case given in Equation {eq}`Eq:ComplexNumbers:abc-eq`. Let us start with an example:

::::{prf:example}
:label: Ex:ComplexNumbers:compsquare

Consider the second degree polynomial $p(z) =z^2+2z+5$ and we want to solve the equation $p(z)=0$.

We are going to do this by first rewriting $p$ to the form $p(z) = (z+p)^2+q$ for some numbers $p$ and $q$.

Expanding gives that we want $z^2+2z+5=z^2+2pz + (p^2+q)$, thus $2=2p$ and $5=p^2+q$. The first equation gives us $p=1$. Plugging this into the second equation, we obtain $5=1+q$, so $q=4$. Therefore, $z^2+2z+5=(z+1)^2+4$.

To solve $z^2+2z+5=0$, we can now write

\begin{align*}
z^2+2z+5 &=0 \\
(z+1)^2+4&=0 \\
(z+1)^2 &=-4 \\
z+1 &= \pm 2i \\
z &= -1 \pm 2i.
\end{align*}

Note that we used {prf:ref}`Thm:ComplexNumbers:roots`.

::::

Going from $z^2+2z+5$ to $(z+1)^2+4$ is called _completing the square_. You can also immediately see that the minimal value of the parabola $y=z^2+2z+5$ for real values of $z$ equals $4$ (as $(z+1)^2\geq 0$ for all real $z$), and the minimum is obtained when $z=-1$.

In general, you can write any polynomial $az^2+bz+c$ in the form $a ((z+p)^2+q)$ by first factoring out the $a$, subsequently choosing the $p$ such that the linear term (the term involving $z$) is correct, and letting $q$ be the remainder. Using this form, you can then determine the zeros of the polynomial.

As you can see in {prf:ref}`Ex:ComplexNumbers:compsquare`, we now found two numbers that are of the form $a+bi$, where $a$ and $b$ are real numbers (for short $a\in\mathbb{R}$ and $b\in\mathbb{R}$). A number like this is called a _complex number_:

::::{prf:definition}
:label: Def:ComplexNumbers:complexnumber

A **complex number** is a number of the form

$$
a+bi,
$$

where $a\in\mathbb{R}$ and $b\in\mathbb{R}$.

The set of all complex numbers is denoted by the symbol $\mathbb{C}$, and is called the **complex plane**.

::::

Such complex numbers we usually denote with the letter $z$ (if we only have one). A complex number also has some special parts, which we define next:

::::{prf:definition}
:label: Def:ComplexNumbers:realimaginary

If $z=a+bi$ is a complex number (with $a\in\mathbb{R}$ and $b\in\mathbb{R}$), the **real part** $\Re{z}$ is defined as

$$
\Re{z}=a,
$$

and the **imaginary part** $\Im{z}$ is defined as

$$
\Im{z}=b.
$$

::::

To make everything concise, we also define the relation between the set of real numbersr $\mathbb{R}$ and the set of complex numbers $\mathbb{C}$:

::::{prf:definition}
:label: Def:ComplexNumbers:realcomplex

Assume $x\in\mathbb{R}$. Then we define that $x\in\mathbb{C}$ with $\Re{x}=x$ and $\Im{x}=0$.

Assume $z\in\mathbb{C}$ and $\Im{z}=0$. Then we define that $z\in\mathbb{R}$.

::::

Just like we can visualise real numbers on a number line, we can visualise complex numbers. For this we need two axes, one indicating the value of the real part of a complex number and one indicating the imaginary part of the same complex number. In {numref}`Figure %s <Fig:ComplexNumbers:complexplane>` you can see this visualisation. The horizontal axis always indicates the real part, while the vertical axis always represents the imaginary part.

:::{figure} Images/Fig-ComplexNumbers-complexplane.svg
:name: Fig:ComplexNumbers:complexplane
:class: dark-light

Visualisation of the complex plane $\mathbb{C}$.

:::

**Operations with complex numbers**

With complex numbers we can do the same operations as with real numbers:

::::{prf:theorem}
:label: Thm:ComplexNumbers:ops

If $z=a+bi$ and $w=c+di$ are complex numbers (with $a,b,c,d\in\mathbb{R}$), then the following numbers are again complex numbers:

\begin{align*}
z+w &= (a+c)+(b+d)i, \\
z-w &= (a-c)+(b-d)i, \\
zw &= (ac-bd)+(ad+bc)i, \\
\frac{z}{w} &= \frac{(ac+bd)+(bc-ad)i}{c^2+d^2}=\frac{ac+bd}{c^2+d^2}+\frac{bc-ad}{c^2+d^2}i. \quad\text{(Assuming $w\neq0$.)}
\end{align*}

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:ops`
:class: dropdown, tudproof 
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:ops` -->

We prove the four results by working each out separately. We start with the _addition_:

\begin{align*}
z+w &= (a+bi) + (c+di) \\
&= a + bi + c + di \\
&= a + c + bi + di \\
&= (a+c)+(b+d)i.
\end{align*}

Then we treat _subtraction_ the same:

\begin{align*}
z-w &= (a+bi) - (c+di) \\
&= a + bi - c - di \\
&= a - c + bi - di \\
&= (a-c)+(b-d)i.
\end{align*}

Now we turn to _multiplication_:

\begin{align*}
zw &= (a+bi)(c+di) \\
&= a(c+di)+bi(c+di) \\
&= ac+adi+bci+bdi^2 \\
&= ac+adi+bci-bd \\
&= ac-bd+adi+bci \\
&= (ac-bd)+(ad+bc)i.
\end{align*}

Finally we look into the _division_:

\begin{align*}
\frac{z}{w} &= \frac{a+bi}{c+di} \\
&= \frac{a+bi}{c+di}\frac{a-bi}{c-di} \\
&= \frac{(a+bi)(c-di)}{(c+di)(c-di)} \\
&= \frac{(ac+bd)+(-ad+bc)i}{(c^2+d^2)+(-cd+cd)i} \\
&= \frac{(ac+bd)+(ad-bc)i}{c^2+d^2} \\
&= \frac{ac+bd}{c^2+d^2}+\frac{bc-ad}{c^2+d^2}i.
\end{align*}

::::

Besides these four standard operations we have one more:

::::{prf:definition}
:label: Def:ComplexNumbers:conjugate

If $z=a+bi$ is a complex number (with $a,b\in\mathbb{R}$), the **complex conjugate** $\overline{z}$ is defined as

$$
\overline{z}=a-bi,
$$

which is also a complex number.

::::

We can combine the complex conjugate with the first four operations, which gives the following theorem:

::::{prf:theorem}
:label: Thm:ComplexNumbers:conjops

If $z$ and $w$ are a complex numbers, then the following identities hold:

\begin{align*}
\overline{\overline{z}} &= z, \\
\overline{z+w} &= \overline{z}+\overline{w}, \\
\overline{z-w} &= \overline{z}-\overline{w}, \\
\overline{zw} &= \overline{z}\,\overline{w}, \\
\overline{\left(\frac{z}{w}\right)} &= \frac{\overline{z}}{\overline{w}}.\quad\text{(Assuming $w\neq0$.)}
\end{align*}

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:conjops`
:class: dropdown, tudproof 
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:conjops` -->

We show each of the identities, one after the other, where we assume $z=a+bi$ and $w=c+di$, $a,b,c,d\in\mathbb{R}$:

_Double conjugation_:

\begin{align*}
\overline{\overline{z}} &= \overline{\overline{a+bi}} \\
&= \overline{a-bi} \\
&= a+bi \\
&= z.
\end{align*}

_Addition and conjugation_:

\begin{align*}
\overline{z+w} &= \overline{(a+c)+(b+d)i} \\
&= (a+c)-(b+d)i \\
&= (a-bi)+(c-di) \\
&= \overline{z}+\overline{w}.
\end{align*}

_Substraction and conjugation_:

\begin{align*}
\overline{z-w} &= \overline{(a-c)+(b-d)i} \\
&= (a-c)-(b-d)i \\
&= (a-bi)-(c+di) \\
&= \overline{z}-\overline{w}.
\end{align*}

_Multiplication and conjugation_:

\begin{align*}
\overline{zw} &= \overline{(ac-bd)+(ad+bc)i} \\
&= (ac-bd)-(ad+bc)i \\
&= (ac-adi)-(bd+bci) \\
&= a(c-di)-b(d+ci) \\
&= a(c-di)-b(ci-di^2) \\
&= a(c-di)-bi(c-di) \\
&= (a-bi)(c-di) \\
&= \overline{z}\overline{w}.
\end{align*}

_Division and conjugation_:

\begin{align*}
\overline{\left(\frac{z}{w}\right)} &= \overline{\frac{ac+bd}{c^2+d^2}+\frac{bc-ad}{c^2+d^2}i} \\
&= \frac{ac+bd}{c^2+d^2}-\frac{bc-ad}{c^2+d^2}i \\
&= \frac{ac+bd-(bc-ad)i}{c^2+d^2} \\
&= \frac{(a-bi)(c+di)}{(c-di)(c+di)} \\
&= \frac{a-bi}{c-di}\frac{c+di}{c+di} \\
&= \frac{\overline{z}}{\overline{w}}.
\end{align*}

::::

Even better, we can relate the complex conjugate with the real and imaginary part of a complex number:

::::{prf:theorem}
:label: Thm:ComplexNumbers:conjparts

If $z$ is a complex number, then the following identities hold:

\begin{align*}
\frac{z+\overline{z}}{2} &= \Re{z}, \\
\frac{z-\overline{z}}{2i} &= \Im{z}, \\
z\overline{z} &= \Re{z}^2+\Im{z}^2.
\end{align*}

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:conjparts`
:class: dropdown, tudproof 
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:conjparts` -->

We show each of the identities, one after the other, where we assume $z=a+bi$, $a,b\in\mathbb{R}$:

_Conjugation and real part_:

\begin{align*}
\frac{z+\overline{z}}{2} &= \frac{(a+bi)+(a-bi)}{2} \\
&= \frac{2a}{2} \\
&= a \\
&= \Re{z}.
\end{align*}

_Conjugation and imaginary part_:

\begin{align*}
\frac{z-\overline{z}}{2i} &= \frac{(a+bi)-(a-bi)}{2i} \\
&= \frac{2bi}{2i} \\
&= b \\
&= \Im{z}.
\end{align*}

_Conjugation and product_:

\begin{align*}
z\overline{z} &= (a+bi)(a-bi) \\
&= a^2-abi+abi-b^2i^2 \\
&= a^2+b^2 \\
&= \Re{z}^2+\Im{z}^2.
\end{align*}

::::

From the second identity above we can even deduce the next theorem:

::::{prf:theorem}
:label: Thm:ComplexNumbers:realz

Assume $z\in\mathbb{C}$. $z\in\mathbb{R}$ if and only if $z=\overline{z}$.

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:realz`
:class: dropdown, tudproof
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:realz` -->

Assume $z\in\mathbb{C}$.

If $z\in\mathbb{R}$, then $\Im{z}=0$. The second identity of {prf:ref}`Thm:ComplexNumbers:conjparts` then gives $\frac{z-\overline{z}}{2i}=0$, which gives in turn $z=\overline{z}$.

If $z\notin\mathbb{R}$, then $\Im{z}\neq0$. The second identity of {prf:ref}`Thm:ComplexNumbers:conjparts` then gives $\frac{z-\overline{z}}{2i}\neq0$, which gives in turn $z\neq\overline{z}$.

::::

**Geometric interpretation of the complex conjugate**

First, we look at the complex conjugation. This is a relatively straightforward case, as it involves only a single number. Recall that the complex conjugate $\bar z$ changes the sign of the imaginary part of the number $z$. That is $\overline{a+bi} = a-bi$. As the imaginary part of a complex number corresponds to the second coordinate of its representation in the complex plane, this implies that the number is reflected in the real axis (the horizontal axis). See {numref}`Figure %s <Fig:ComplexNumbers:complexconj>`.

:::{figure} Images/Fig-ComplexNumbers-complexconj.svg
:name: Fig:ComplexNumbers:complexconj
:class: dark-light

Complex conjugation reflects a number in the real axis.

:::

**Geometric interpretation of addition**

The geometric interpretation of adding complex numbers should look familiar to you. Indeed if we add $z=a+bi$ and $w=c+di$ the new number is $z+w=(a+c)+(b+d)i$, so we add the real and imaginary parts. This means we add the coordinates of the corresponding points, just as if we were adding vectors. Thus, geometrically we can add two complex numbers by following the parallelogram rule. That is, the lines from the origin to the two complex numbers form two sides of a parallelogram with vertices $0$, $z$, $z+w$, and $w$. See {numref}`Figure %s <Fig:ComplexNumbers:complexadd>`.

:::{figure} Images/Fig-ComplexNumbers-complexadd.svg
:name: Fig:ComplexNumbers:complexadd
:class: dark-light

Adding complex numbers follows the parallelogram rule.

:::

If we want to interpet the other operations such as multiplication easily, we first need another way of writing complex numbers. But before we do that we will turn our attention first to solving equations.

## Solving equations

The reason for introducing complex numbers is to ensure that more equations have solutions, for example $z^2+1=0$. In this section, we consider equations involving complex numbers. This means that the solutions may be complex, but also that the coefficients in the equations can be complex.

We already solved quadratic equations using a new technique called _completing the square_ and in this section you will learn more ways to solve equations.

We introduced complex numbers to give the equation $x^2+1 = 0$  a solution.  It appears that something much stronger holds, namely, that every polynomial equation with coefficients in $\mathbb{C}$, for instance  $(1+i)x^4 - 2x^2 + x = 10i$,  has solutions in $\mathbb{C}$. This is the content of the following theorem.

::::{prf:theorem} Fundamental Theorem of algebra
:label: Thm:ComplexNumbers:fundamental

Consider a polynomial $p(z)$ of degree $n$,

$$
p(z) = a_n z^n + a_{n-1} z^{n-1} + \cdots + a_1 z + a_0,
$$

where the coefficients $a_n, a_{n-1}, \ldots, a_0$ are complex numbers and $a_n\neq 0$. Then you can factor the polynomial in linear terms, that is

$$
p(z) = a_n (z-b_1)(z-b_2) \cdots (z-b_n)
$$

for some complex numbers $b_1, b_2, \ldots, b_n$.

::::

Observe that this factorisation means that $b_1, b_2, \ldots, b_n$ are the zeros (= roots) of the polynomial $p(z)$. It might happen that the $b$'s are complex numbers, even if $a_1, a_2, \ldots, a_n$ are real.

We will not discuss the proof of this theorem, as that requires much more mathematics. However, we will illustrate the theorem using some examples.

::::{prf:example}
:label: Ex:ComplexNumbers:polyreal

Consider $p(z)=z^2+3z+2$. Then we know that we can factor the polynomial as $p(z) = (z+2)(z+1)$ and thus find the zeros as $-2$ and $-1$.

::::

::::{prf:example}
:label: Ex:ComplexNumbers:polycomplcon

Consider the equation $z^2=-1$. We can always rewrite an equation to an equation where one side is equal to zero by moving everything to one side. Thus this equation corresponds to $z^2+1=0$. We can now factor $z^2+1$ to $(z+i)(z-i)$ and thus find that $i$ and $-i$ are the two solutions to this equation.

::::

::::{prf:example}
:label: Ex:ComplexNumbers:polycompl

While a polynomial of degree $n$ can be factored in $n$ linear terms, and we have $n$ values $b_i$, this does not mean that there are $n$ distinct zeros. For example $p(z) = z^2+2z+4$ can be factored as $p(z)=(z+2)^2$ and thus only has $z=-2$ as a solution. However, the term $(z+2)$ occurs twice in the factorisation. We therefore say that the multiplicity of the zero $-2$ is equal to two.

::::

In particular, we see that any polynomial of degree $n$ has $n$ complex zeros _counting multiplicity_:

::::{prf:theorem}
:label: Thm:ComplexNumbers:uniquezeros

If $\{z_1,z_2,\ldots,z_k\}$ is the set of _unique_ zeros of a polynomial $p$ of degree $n$ with $p(z)=a_n z^n + a_{n-1} z^{n-1} + \cdots + a_1 z + a_0$, the polynomial $p$ can be written as

$$
p(z)=a_n(z-z_1)^{\alpha_1}(z-z_2)^{\alpha_2}\cdots(z-z_k)^{\alpha_k}
$$

where $\alpha_j,j=1,2,\ldots,k$ are positive integers and

$$
\sum_{j=1}^k\alpha_j=n.
$$

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:uniquezeros`
:class: dropdown, tudproof
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:uniquezeros` -->

Assume $\{z_1,z_2,\ldots,z_k\}$ is the set of _unique_ zeros of a polynomial $p$ of degree $n$. Then following {prf:ref}`Thm:ComplexNumbers:fundamental`, we can write

:::{math}
:label: Eq:ComplexNumbers:factorsb

p(z) = a_n (z-b_1)(z-b_2) \cdots (z-b_n).

:::

for some complex numbers $b_1, b_2, \ldots, b_n$.

Because $p(z_1)=0$ for $j\in\{1,\ldots,k\}$, we must have that $\alpha_1\in\{1,\ldots,n\}$ numbers out of the set $\{b_1, b_2, \ldots, b_n\}$ must equal $z_1$. Without loss of generality we may assume those are $b_1,\ldots,b_{\alpha_1}$. This is also means that Equation {eq}`Eq:ComplexNumbers:factorsb` transforms to

:::{math}
:label: Eq:ComplexNumbers:factorsb1

p(z) = a_n (z-z_1)^{\alpha_1}(z-b_{\alpha_1+1}) \cdots (z-b_n).

:::

We can repeat the above argument for $z_2$: we must have that $\alpha_2\in\{1,\ldots,n-\alpha_1\}$ numbers out of the set $\{b_{\alpha_1+1}, \ldots, b_n\}$ must equal $z_2$. Without loss of generality we may assume those are $b_{\alpha_1+1},\ldots,b_{\alpha_1+\alpha_2}$. This is also means that Equation {eq}`Eq:ComplexNumbers:factorsb1` transforms to

:::{math}
:label: Eq:ComplexNumbers:factorsb2

p(z) = a_n (z-z_1)^{\alpha_1}(z-z_2)^{\alpha_2}(z-b_{\alpha_1+\alpha_2+1}) \cdots (z-b_n).

:::

Repeating this argument for $z_3,\ldots,z_k$ leads to desired formulae.

::::

::::{prf:definition}
:label: Def:ComplexNumbers:multiplicity

If $z_j$ is a zero of a polynomial $p$ of degree $n$ with $p(z)=a_n(z-z_1)^{\alpha_1}(z-z_2)^{\alpha_2}\cdots(z-z_k)^{\alpha_k}$, the **(algebraic) multiplicity** of $z_j$ is equal to $\alpha_j$.

::::

::::{prf:example}
:label: Ex:ComplexNumbers:polycomplcon2

The third degree polynomial $p(z) = z^3-4z^2$ can be factored as $p(z) = z^2(z-4) = (z-0)^2(z-4)$. Therefore, it has zeros $4$ and $0$, where the multiplicity of $4$ is equal to one and the multiplicity of $0$ is equal to two. The degree of the polynomial is $3$, which is equal to the sum of the multiplcities of its zeros ($1+2=3$).

::::

{prf:ref}`Ex:ComplexNumbers:polycomplcon` showed that both $z=i$ and its complex conjugate $\overline{z}=-i$ where roots of the polynomial $p(z)=z^2+1$. One might wonder whether it is always the case that both $z$ and its complex conjugate $\overline{z}$ are both roots of a given polynomial. It can be shown that this is the case if all coefficients are real valued.

::::{prf:theorem}
:label: Thm:ComplexNumbers:realpoly

Let $p$ be a polynomial with _real_ coefficients.
If $p(z)=0$, then $p(\overline{z})=0$ as well, and the algebraic multiplicities of $z$ and $\overline{z}$ are the same.

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:realpoly`
:class: dropdown, tudproof
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:realpoly` -->

Consider a polynomial $p$ of degree $n$, $\sum_{j=0}^n a_j z^j$, where the coefficients $a_n, a_{n-1}, \ldots, a_0$ are real-valued numbers and $a_n\neq 0$.

First we show that $p(\overline{z})=0$ by considering $\overline{p(z)}$ twice:

$$
\overline{p(z)} = \overline{0} = 0,
$$

but also

$$
\begin{align*}
\overline{p(z)} &= \overline{\sum_{j=0}^n a_j z^j} \\
&= \sum_{j=0}^n\overline{a_jz^j} \\
&= \sum_{j=0}^na_j\overline{z^j} \\
&= \sum_{j=0}^na_j\overline{z}^j \\
&= p(\overline{z}).
\end{align*}
$$

Combining these two results gives the desired $p(\overline{z})=0$.

Now we focus on the algebraic multiplicity. {prf:ref}`Thm:ComplexNumbers:realpoly` shows that we can write $p(z)$ as

$$
p(z)=a_n(z-z_1)^{\alpha_1}(z-z_2)^{\alpha_2}\cdots(z-z_k)^{\alpha_k}
$$

where $\alpha_j,j=1,2,\ldots,k$ are positive integers,

$$
\sum_{j=1}^k\alpha_j=n
$$

and $z_1,z_2,\ldots,z_k$ are the unique zeros of $p$.

If $p(z)=0$, then $z=z_j$ for some $j\in\{1,2,\ldots,k\}$ and $z\neq z_i$ for $i\in\{1,2,\ldots,k\}\setminus\{j\}$. Without loss of generality we can assume $j=1$.

This means that also $(z-z_1)^{\alpha_1}=0$ and $(z- z_i)^{\alpha_i}\neq0$ for $i\in\{2,\ldots,k\}$, and even more that $\overline{(z-z_1)}^{\alpha_1}=0$ and $\overline{(z- z_i)}^{\alpha_i}\neq0$ for $i\in\{2,\ldots,k\}$.

From the last it even follows that $(\overline{z}-\overline{z_1})^{\alpha_1}=0$ and $(\overline{z}- \overline{z_i})^{\alpha_i}\neq0$ for $i\in\{2,\ldots,k\}$.

Using the previous results, we look at $p(\overline{z})$:
\begin{align*}
p(\overline{z}) &= \overline{p(z)} \\
&= \overline{a_n(z-z_1)^{\alpha_1}(z-z_2)^{\alpha_2}\cdots(z-z_k)^{\alpha_k}} \\
&= a_n\overline{(z-z_1)^{\alpha_1}}\ \overline{(z-z_2)^{\alpha_2}}\cdots\overline{(z-z_k)^{\alpha_k}} \\
&= a_n\overline{(z-z_1)}^{\alpha_1}\ \overline{(z-z_2)}^{\alpha_2}\cdots\overline{(z-z_k)}^{\alpha_k} \\
&= a_n(\overline{z}-\overline{z_1})^{\alpha_1}\ (\overline{z}-\overline{z_2})^{\alpha_2}\cdots(\overline{z}-\overline{z_k})^{\alpha_k}.
\end{align*}

As all terms except the first term $(\overline{z}-\overline{z_1})^{\alpha_1}$ are non-zero, and the first term is zero, we find that $\overline{z}=\overline{z_1}$, $\alpha_1$ times. In other words, the algebraic multiplicity of $\overline{z}$ is $\alpha_1$.

::::

**Polynomial Division**

Next, we consider a method you can use whenever you know one root of a polynomial. The fundamental theorem of Algebra says that if $p(z)$ is a polynomial such that $p(b)=0$ for some $b$, then $p(z) = a_n(z-b)(z-b_2)\cdots (z-b_n) = (z-b) q(z)$ for another polynomial $q(z)=a_n(z-b_2)\cdots  (z-b_n)$.
Thus, we divide the polynomial $p(z)$ by $(z-b)$ in this case and obtain a new polynomial. To find the zeros of $p$ we now just have to find the zeros of the quotient $\nicefrac{p(z)}{z-b}$ and add $b$ to this list.

To divide a polynomial by another polynomial you can use a long division. Let us recall how this worked for ordinary fractions.

::::{prf:example}
:label: Ex:ComplexNumbers:longdivisionnum

Let us calculate $\frac{97813}{382}$. In {numref}`Figure %s <Fig:ComplexNumbers:longdivisionnum>` on the left, you see the American notation for Long division, on the right the corresponding Dutch notation. Everything in red is usually not written down, but included here to clarify what happens. (Note that the calculations in the middle are true regardless of whether the red parts are included or not.)

:::{figure} Images/Fig-ComplexNumbers-longdivisionnum.svg
:name: Fig:ComplexNumbers:longdivisionnum
:class: dark-light

Example of long division for ordinary fractions.
:::

Here, the following calculation has been written down concisely:

$$
\frac{97813}{382} = 200 + \frac{21413}{382} = 250 + \frac{2313}{382} = 256 + \frac{21}{382}.
$$

First, subtract as many multiples of $100\cdot 382$ from $97813$ as possible (or multiples of $100$ from $\frac{97813}{382}$). Next, you do the same with the remainder, and one digit lower, so you subtract as many multiples of $10\cdot 382$ from the remainder $21413$. You continue until you can't subtract the numerator even once from the remainder (or until you have as many digits as you want).

::::

We can do the same thing for polynomials.

::::{prf:example}
:label: Ex:ComplexNumbers:longdivisionpoly

Consider $p(z) = z^3+3z^2+z-5$. You may notice that $z=1$ is a root; $p(1)=0$. Thus $z-1$ must be a factor. If we calculate this division we obtain (on the left again US notation, on the right Dutch notation):

:::{figure} Images/Fig-ComplexNumbers-longdivisionpoly.svg
:name: Fig:ComplexNumbers:longdivisionpoly
:class: dark-light

Example of long division for polynomials.

:::

Note that the remainder is zero, as we should have expected.

Here, we essentially calculate

$$
\frac{z^3+3z^2+z-5}{z-1} = z^2 + \frac{4z^2+z-5}{z-1} = z^2+4z+\frac{5z-5}{z-1} = z^2+4z+5.
$$

As a consequence, we see that $z^3+3z^2+z-5=(z-1)(z^2+4z+5)$, so it equals $0$ if either $z-1=0$ or $z^2+4z+5=0$. Completing the square gives $z^2+4z+5=(z+2)^2+1$, so the zeros are $z=-2\pm i$. Thus, the roots of $z^3+3z^2+z-5$ are $z=1$ and $z=-2\pm i$.

::::

## Grasple exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d1c5a087-af58-42a1-9fcb-1ee915c98ebe?id=122746
:label: grasple_exercise_10_1_1
:dropdown:
:description: Real part of a complex number.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c0d9602f-7f90-4ecc-a7e7-96cdc3b1da06?id=122747
:label: grasple_exercise_10_1_2
:dropdown:
:description: Imaginary part of a complex number.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/431a62c7-bb01-409b-8ca5-05db4c6a0661?id=122743
:label: grasple_exercise_10_1_3
:dropdown:
:description: Adding two complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ba2e0f24-ed35-42af-a25c-776b38653a7e?id=122744
:label: grasple_exercise_10_1_4
:dropdown:
:description: Subtracting two complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/aecbca69-79a1-4f7f-87bb-5764a1ebac18?id=122745
:label: grasple_exercise_10_1_5
:dropdown:
:description: Multiplying two complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/dd1e5d42-2b59-457f-a7fe-8b1ce4219cdc?id=122748
:label: grasple_exercise_10_1_6
:dropdown:
:description: Dividing two complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/af73fbce-2235-4e27-8447-fe6e3f287794?id=122749
:label: grasple_exercise_10_1_7
:dropdown:
:description: Complex conjugate of a complex number.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/42bbd961-c030-4c24-8965-26d9bf343c99?id=122750
:label: grasple_exercise_10_1_8
:dropdown:
:description: Multiplying a complex number with it's complex conjugate.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6da6fd51-0928-4897-b143-815389b8a9a7?id=122751
:label: grasple_exercise_10_1_9
:dropdown:
:description: Completing the square with real coefficients.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7e860cd4-a132-4084-a453-cf6977f93bca?id=122752
:label: grasple_exercise_10_1_10
:dropdown:
:description: Completing the square with complex coefficients.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d616adab-46f3-4649-9246-f51ac2ed1e7a?id=122753
:label: grasple_exercise_10_1_11
:dropdown:
:description: One more time completing the square.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/eb0d0a6f-403a-4581-acf9-7ff821835695?id=122754
:label: grasple_exercise_10_1_12
:dropdown:
:description: Polynomial long division.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fd1ba3d4-3cc1-417e-9e0a-0d33b3f808ee?id=122756
:label: grasple_exercise_10_1_13
:dropdown:
:description: Another long division with polynomials.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1a40094b-8d39-4acd-a63e-d29677dad83d?id=122758
:label: grasple_exercise_10_1_14
:dropdown:
:description: Counting solutions of a polynomial equation.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8d8087fb-aa8d-47f4-86ae-4d3e1883d4c8?id=122759
:label: grasple_exercise_10_1_15
:dropdown:
:description: On the relation between roots of polynomials.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/53af5529-e8ba-446a-b903-77cd39addb35?id=122761
:label: grasple_exercise_10_1_16
:dropdown:
:description: Solving a cubic equation given a root.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/b072da59-e30c-4fba-8594-7d025cad0eb0?id=122762
:label: grasple_exercise_10_1_17
:dropdown:
:description: Solving a quartic equation given two roots.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6661f666-cb49-4881-a80a-02971cd6c34f?id=122763
:label: grasple_exercise_10_1_18
:dropdown:
:description: Solving a quartic equation given one root.

::::