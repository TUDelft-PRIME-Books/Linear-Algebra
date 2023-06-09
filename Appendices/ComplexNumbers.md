# Complex numbers

## Introduction

Consider the equation

:::{math} 
:label: Eq:ComplexNumbers:abc-eq
ax^2+bx+c=0.

:::

Previously you probably learned that Equation {eq}`Eq:ComplexNumbers:abc-eq` only has solutions when $D=b^2-4ac$ was non-negative and in that case you would have the two solutions

:::{math} 
:label: Eq:ComplexNumbers:abc-sol
x_{1,2}=\frac{-b\pm\sqrt{D}}{2a}.

:::

Now consider the case that you _really_ need solutions of Equation {eq}`Eq:ComplexNumbers:abc-eq` even if $D$ is negative. This might sound strange, but you will encounter this case in many engineering applications, for example in solving second-order linear differential equations. Turns out that the solution in Equation {eq}`Eq:ComplexNumbers:abc-sol` is still valid when $D<0$, which means that you need to take the square root of a negative number.

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

The square root of $-1$ obviously is problem. Therefor we introduce the special number $i$:

::::{prf:definition} 

The **imaginary unit** $i$ is a number defined by the equation

:::{math} 
:label: Eq:ComplexNumbers:def-i

i^2=-1.

:::

::::


Because $i$ is defined to be a number (mind you, it is not a real number), we also assume $i$ behaves just like any normal number.

This means we can rewrite our two solutions as

\begin{equation*}
x_{1,2}=\pm\sqrt{-1}=\pm\sqrt{i^2}=\pm i.
\end{equation*}

Doesn't this already look simpler?

Now we have defined $i$, we can revisit the general case given in Equation {eq}`Eq:ComplexNumbers:abc-eq`. We start with an example:

$$
\frac{1}{2}x^2+x+\frac52=0.
$$

Using Equation {eq}`Eq:ComplexNumbers:abc-sol` we get the two solutions

$$
x_{1,2}=-1\pm \sqrt{-4},
$$

which we can rewrite using Equation {eq}`Eq:ComplexNumbers:def-i` to:

\begin{align*}
x_{1,2} &= -1\pm \sqrt{-4} \\
&= -1\pm \sqrt{4i^2} \\
&= -1\pm \sqrt{4}\sqrt{i^2} \\
&= -1\pm 2i \\
\end{align*}

As you can see, we now found two numbers that are of the form $a+bi$, where $a$ and $b$ are real numbers (for short $a\in\mathbb{R}$ and $b\in\mathbb{R}$). A number like this is called a _complex number_:


::::{prf:definition} 

A **complex number** is a number of the form

$$
a+bi,
$$

where $a\in\mathbb{R}$ and $b\in\mathbb{R}$.

The set of all complex numbers is denoted by the symbol $\mathbb{C}$, and is called the **complex plane**.

::::


Such complex numbers we usually denote with the letter $z$ (if we only have one) and also has some special parts, which we define next:


::::{prf:definition} 

If $z=a+bi$ is a complex number (with $a\in\mathbb{R}$ and $b\in\mathbb{R}$), the **real part** $\Re(z)$ is defined as

$$
\Re(z)=a,
$$

and the **imaginary part** $\Im(z)$ is defined as 

$$
\Im(z)=b.
$$

::::


Just like we can visualise real numbers on a number line, we can visualise complex numbers. For this we need two axes, one indicating the value of the real part of a complex number and one indicating the imaginary part of the same complex number. In {numref}`Figure %s <Fig:ComplexNumbers:complexplane>` you can see this visualisation. The horizontal axis always indicates the real part, while the vertical axis always represents the imaginary part.

:::{figure} Images/Fig-ComplexNumbers-complexplane.svg
:name: Fig:ComplexNumbers:complexplane

Visualisation of the complex plane $\mathbb{C}$.

:::



**Operations with complex numbers**

With complex numbers we can do the same operations as with real numbers:


::::{prf:theorem} 

If $z=a+bi$ and $w=c+di$ are a complex numbers (with $a,b,c,d\in\mathbb{R}$), then the following numbers are again complex numbers:

\begin{align*}
z+w &= (a+c)+(b+d)i, \\
z-w &= (a-c)-(b+d)i, \\
zw &= (ac-bd)+(ad+bc)i, \\
\frac{z}{w} &= \frac{(ac+bd)+(bc-ad)i}{c^2+d^2}.
\end{align*}

::::


Besides these four standard operations we have one more:


::::{prf:definition} 

If $z=a+bi$ is a complex number (with $a,b\in\mathbb{R}$), the **complex conjugate** $\overline{z}$ is defined as

$$
\overline{z}=a-bi.
$$

::::

We can combine the complex conjugate with the first four operations, which gives the following theorem:


::::{prf:theorem}

If $z$ and $w$ are a complex numbers, then the following numbers are again complex numbers:

\begin{align*}
\overline{\overline{z}} &= z, \\
\overline{z+w} &= \overline{z}+\overline{w}, \\
\overline{z-w} &= \overline{z}-\overline{w}, \\
\overline{zw} &= \overline{z}\,\overline{w}, \\
\overline{\left(\frac{z}{w}\right)} &= \frac{\overline{z}}{\overline{w}}.
\end{align*}

::::


Even better, we can relate the complex conjugate with the real and imaginary part of a complex number:

::::{prf:theorem}

If $z$ is a complex number, then the following identities hold:

\begin{align*}
\Re(z) &= \frac{z+\overline{z}}{2}, \\
\Im(z) &= \frac{z-\overline{z}}{2i}, \\
\Re(z)^2+\Im(z)^2 &= z\overline{z}.
\end{align*}

::::


From the first identity above we can even deduce the next theorem:


::::{prf:theorem}

Assume $z\in\mathbb{C}$. Then $z\in\mathbb{R}$ if and only if $z=\overline{z}$.

::::


**Geometric interpretation of the complex conjugate**

First, we look at the complex conjugation. This is a relatively straightforward case, as it involves only a single number. Recall that the complex conjugate $\bar z$ changes the sign of the imaginary part of the number $z$. That is $\overline{a+bi} = a-bi$. As the imaginary part of a complex number corresponds to the second coordinate of its representation in the complex plane, this implies that the number is reflected in the real axis (the horizontal axis). See {numref}`Figure %s <Fig:ComplexNumbers:complexconj>`.


:::{figure} Images/Fig-ComplexNumbers-complexconj.svg
:name: Fig:ComplexNumbers:complexconj

Complex conjugation reflects a number in the real axis.

:::


**Geometric interpretation of addition**

The geometric interpretation of adding complex numbers should look familiar to you. Indeed if we add $z=a+bi$ and $w=c+di$ the new number is $z+w=(a+c)+(b+d)i$, so we add the real and imaginary parts. This means we add the coordinates of the corresponding points, just as if we were adding vectors. Thus, geometrically we can add two complex numbers by following the parallelogram rule. That is, the lines from the origin to the two complex numbers form two sides of a parallelogram with vertices $0$, $z$, $z+w$, and $w$. See {numref}`Figure %s <Fig:ComplexNumbers:complexadd>`.


:::{figure} Images/Fig-ComplexNumbers-complexadd.svg
:name: Fig:ComplexNumbers:complexadd

Adding complex numbers follows the parallelogram rule.

:::


If we want to interpet the other operations such as multiplication easily, we first need another way of writing complex numbers, which we will do after revisiting solving complex equations.

## Solving complex equations

The reason for introducing complex numbers is to ensure that more equations have solutions, for example $z^2+1=0$. In this section, we consider equations involving complex numbers. This means that the solutions may be complex, but also that the coefficients in the equations can be complex.

**Quadratic equations: Completing the square**

Being able to solve the quadratic equation $z^2=-1$ was one of the motivations for introducing complex numbers, so we certainly want a method to solve all quadratic equations. Of course, you know the quadratic formula for the solution to a general quadratic equation. If we apply this to 
$z^2+1=0$, we obtain (with $a=c=1$ and $b=0$)

$$
z= \frac{-0\pm \sqrt{0^2-4\cdot 1\cdot 1}}{2\cdot 1} = \pm \frac12 \sqrt{-4}. 
$$

Writing $\sqrt{-4}=2i$ (as $(2i)^2=4i^2=-4$), we obtain $z=\pm \frac12 \cdot 2i = \pm i$ as desired. There are several minor problems with this method.

First of all, it is unclear whether $\sqrt{-4}$ should be $2i$ or $-2i$. For positive real numbers, we distinguish $\sqrt{2}$ from $-\sqrt{2}$ by saying $\sqrt{2}$ is the positive solution to $x^2=2$. Complex numbers are not positive or negative, so we can't use this criterion to make a choice here. Of course, the choice is somewhat irrelevant in this setting: the quadratic formula contains $\pm \sqrt{\cdots}$, so either choice will lead to the same solutions. It is however somewhat unsatisfying.

Secondly, if the quadratic equation has complex coefficients, such as $z^2+i=0$, then we obtain expressions like $\sqrt{0^2-4\cdot 1\cdot i} = \sqrt{-4i}$, which are even harder to determine the value of.

Finally, using the quadratic formula does not provide any insight in what is happening; it is just a calculation tool. 

You can complete the square as a better alternative. This is a technique for simplifying quadratic expressions which has other uses as well. 


::::{prf:example}

Consider a second degree polynomial $p(z) =z^2+2z+5$. We want to rewrite this to $p(z) = (z+p)^2+q$ for some $p$ and $q$. Expanding gives that we want $z^2+2z+5=z^2+2pz + (p^2+q)$, thus $2=2p$ and $5=p^2+q$. The first equation gives us $p=1$. Plugging this into the second equation, we obtain $5=1+q$, so $q=4$. Therefore, $z^2+2z+5=(z+1)^2+4$. To solve $z^2+2z+5=0$, we can now write 

\begin{align*}
z^2+2z+5 &=0 \\
(z+1)^2+4&=0 \\
(z+1)^2 &=-4 \\
z+1 &= \pm 2i \\
z &= -1 \pm 2i.
\end{align*}

Going from $z^2+2z+5$ to $(z+1)^2+4$ is called completing the square. You can also immediately see that the minimal value of the parabola $y=z^2+2z+5$ for real values of $z$ equals 4 (as $(z+1)^2\geq 0$ for all real $z$), and the minimum is obtained when $z=-1$. 

::::


In general, you can write any polynomial $az^2+bz+c$ in the form $a ((z+p)^2+q)$ by first factoring out the $a$, subsequently choosing the $p$ such that the linear term (the term involving $z$) is correct, and letting $q$ be the remainder. Using this form, you can then determine the zeros of the polynomial.

**Fundamental Theorem of algebra**

You may think that introducing a new set of numbers as solutions to certain equations can be a never-ending process. When you introduce more numbers, you get more equations (now we need not only solve $x^2=-1$, but also $x^2=i$), which need new solutions, etc. 
It turns out that if you restrict yourself to polynomial equations, this is not the case. This statement is the Fundamental Theorem of Algebra:


::::{prf:theorem}

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


Observe that this factorization means that $b_1, b_2, \ldots, b_n$ are the zeros (= roots) of the polynomial $p(z)$. It might happen that the $b$'s are complex numbers, even if the $a$'s are real. 

We will not discuss the proof of this theorem, as that requires much more mathematics. However, we will illustrate the theorem using some examples. 


::::{prf:example}

Consider $p(z)=z^2+3z+2$. Then we know that we can factor the polynomial as $p(z) = (z+2)(z+1)$ and thus find the zeros as $-2$ and $-1$.

::::


::::{prf:example}
:label: Ex:ComplexNumbers:polycomplcon

Consider the equation $z^2=-1$. We can always rewrite an equation to an equation where one side is equal to zero by moving everything to one side. Thus this equation corresponds to $z^2+1=0$. We can now factor $z^2+1$ to $(z+i)(z-i)$ and thus find that $i$ and $-i$ are the two solutions to this equation. 

::::


::::{prf:example}

While a polynomial of degree $n$ can be factored in $n$ linear terms, and we have $n$ values $b_i$, this does not mean that there are $n$ distinct zeros. For example $p(z) = z^2+2z+4$ can be factored as $p(z)=(z+2)^2$ and thus only has $z=-2$ as a solution. However, the term $(z+2)$ occurs twice in the factorization. We therefore say that the multiplicity of the zero $-2$ is equal to two. 

::::


In particular, we see that any polynomial of degree $n$ has $n$ complex solutions _counting multiplicity_. 


::::{prf:example}

The third degree polynomial $p(z) = z^3-4z^2$ can be factored as $p(z) = z^2(z-4) = (z-0)^2(z-4)$. Therefore, it has zeros 4 and 0, where the multiplicity of 4 is equal to one and the multiplicity of 0 is equal to two. The degree of the polynomial is 3, which is equal to the sum of the multiplcities of its zeros ($1+2=3$).

::::


{prf:ref}`Ex:ComplexNumbers:polycomplcon` showed that both $z=i$ and its complex conjugate $\overline{z}=-i$ where roots of the polynomial $p(z)=z^2+1.$. One might wonder whether it is always the case that both $z$ and its complex conjugate $\overline{z}$ are both roots of a given polynomial. It can be shown that this is the case if all coefficients are real valued.


::::{prf:theorem}
:label: Thm:ComplexNumbers:realpoly

Let $p$ be a polynomial with _real_ coefficients. 
If $p(z)=0$, then $p(\overline{z})=0$ as well.

::::


::::{dropdown} Proof of&nbsp;{prf:ref}`Thm:ComplexNumbers:realpoly`

Consider a polynomial $p$ of degree $n$, $\sum_{i=0}^n a_i z^i$, where the coefficients $a_n, a_{n-1}, \ldots, a_0$ are real valued numbers and $a_n\neq 0$. Suppose that $z$ is root of the polynomial $p(z)$, i.e. $p(z)=0$. It then holds that

$$
\overline{\sum_{i=0}^n a_i z^i}=\overline{0}=0.
$$

Using the identities for the complex conjugate, we can also show that 

$$
\overline{\sum_{i=0}^n a_i z^i}=\sum_{i=0}^n \overline{a_i z^i}=\sum_{i=0}^n a_i \overline{z^i}=\sum_{i=0}^n a_i \overline{z}^i=p(\overline{z}).
$$

Hence, $p(\overline{z})=0$ and the complex conjugate $\overline{z}$ is thus also a root of the polynomial $p$.

::::


**Polynomial Division**

Next, we consider a method you can use whenever you know one root of a polynomial. The fundamental theorem of Algebra says that if $p(z)$ is a polynomial such that $p(b)=0$ for some $b$, then $p(z) = a_n(z-b)(z-b_2)\cdots (z-b_n) = (z-b) q(z)$ for another polynomial $q(z)=a_n(z-b_2)\cdots  (z-b_n)$. 
Thus, we divide the polynomial $p(z)$ by $(z-b)$ in this case and obtain a new polynomial. To find the zeros of $p$ we now just have to find the zeros of the quotient $\nicefrac{p(z)}{z-b}$ and add $b$ to this list.

To divide a polynomial by another polynomial you can use a long division. Let us recall how this worked for ordinary fractions.


:::: {prf:example}

Let us calculate $\frac{97813}{382}$.  In {numref}`Figure %s <Fig:ComplexNumbers:longdivisionnum>` on the left, you see the American notation for Long division, on the right the corresponding Dutch notation. Everything in red is usually not written down, but included here to clarify what happens. (Note that the calculations in the middle are true regardless of whether the red parts are included or not.)


:::{figure} Images/Fig-ComplexNumbers-longdivisionnum.svg
:name: Fig:ComplexNumbers:longdivisionnum

Example of long division for ordinary fractions.
:::

Here, the following calculation has been written down concisely:

$$
\frac{97813}{382} = 200 + \frac{21413}{382} = 250 + \frac{2313}{382} = 256 + \frac{21}{382}.
$$

First, subtract as many multiples of $100\cdot 382$ from 97813 as possible (or multiples of $100$ from $\frac{97813}{382}$). Next, you do the same with the remainder, and one digit lower, so you subtract as many multiples of $10\cdot 382$ from the remainder $21413$. You continue until you can't subtract the numerator even once from the remainder (or until you have as many digits as you want).

::::


We can do the same thing for polynomials. 


::::{prf:example}

Consider $p(z) = z^3+3z^2+z-5$. You may notice that $z=1$ is a root; $p(1)=0$. Thus $z-1$ must be a factor. If we calculate this division we obtain (on the left again US notation, on the right Dutch notation):


:::{figure} Images/Fig-ComplexNumbers-longdivisionpoly.svg
:name: Fig:ComplexNumbers:longdivisionpoly

Example of long division for polynomials.

:::

Here, we essentially calculate

$$
\frac{z^3+3z^2+z-5}{z-1} = z^2 + \frac{4z^2+z-5}{z-1} = z^2+4z+\frac{5z-5}{z-1} = z^2+4z+5.
$$

As a consequence, we see that $z^3+3z^2+z-5=(z-1)(z^2+4z+5)$, so it equals $0$ if either $z-1=0$ or $z^2+4z+5=0$. Completing the square gives $z^2+4z+5=(z+2)^2+1$, so the zeros are $z=-2\pm i$. Thus, the roots of $z^3+3z^2+z-5$ are $z=1$ and $z=-2\pm i$.

::::


## The polar form of complex numbers


**Modulus and argument**

To consider the multiplication of complex numbers, it is best to first consider the polar coordinates of a complex number. Polar coordinates is a concept that works for points in a plane. They can also be very useful if you consider double integrals. The idea is that instead of looking at the $x$ and $y$ coordinates of a point, we describe the point by the distance to the origin and the direction from the origin.

The distance from zero to the point in the complex plane, we call the _modulus_ $|z|$. By using Pythagoras theorem, it holds that $|z|=\sqrt{a^2+b^2}$. We often denote the modulus by the symbol $r$, so $r=|z|$. The direction is designated by the angle measured from the positive real axis in a counterclockwise direction towards the ray from zero through the point. This angle, we call the _argument_ or $\arg(z)$ as seen in {numref}`Figure %s <Fig:ComplexNumbers:modarg>`. We often denote the argument by the symbol $\theta$, so $\theta=\arg(z)$. The argument uses the convention similar to the unit circle: the direction straight the right corresponds to 0 radians, up corresponds to  $\frac{1}{2}\pi$ radians, to the left to  $\pi$ radians and down to $\frac{3}{2}\pi$ radians.


:::{figure} Images/Fig-ComplexNumbers-modarg.svg
:name: Fig:ComplexNumbers:modarg

The polar coordinates of a point in the complex plane $\C$ are the distance $r=|z|$ from zero to the point and the angle $\theta=\arg(z)$ measured from the positive real axis in a counterclockwise direction towards the ray from zero through the point.

:::


Notice that the argument is not uniquely defined, as you can always go a full circle extra and add $2\pi$ radians to the angle. For example, the number $1$ has argument 0 (as it is on the positive real axis), but also $2\pi$, $4\pi$, and $-2\pi$ (etc.). In order to make a uniform choice, we sometimes work with the principal value of the argument, which is by definition the unique value of the argument between $-\pi$ and $\pi$. 
We write the principal value using a capital A. Thus we have $-\pi < \text{Arg}(z) \leq \pi$. 


:::: {prf:example}

Suppose $z=3+3i$. We find by using Pythagoras that the modulus (the distance to the origin) equals $|z|=\sqrt{3^2+3^2}=3\sqrt{2}$. The argument, the corresponding angle, equals $\frac14\pi$ as you can see in {numref}`Figure %s <Fig:ComplexNumbers:polarex1>`.


:::{figure} Images/Fig-ComplexNumbers-polarex1.svg
:name: Fig:ComplexNumbers:polarex1

The complex number $3+3i$.

:::

::::


::::{prf:example}

Suppose $w=2+3i$. We can still use Pythagoras for the modulus and obtain $|w|=\sqrt{2^2+3^2} = \sqrt{13}$. The argument can't be deduced immediately from a picture, see {numref}`Figure %s <Fig:ComplexNumbers:polarex2>`, but we do see that

$$
\tan(\arg(w)) = \frac{\text{opposite}}{\text{adjacent}} = \frac{\text{imaginary part}}{\text{real part}} = \frac{3}{2}
$$

Therefore $\arg(w) = \arctan\left(\frac32\right) \approx 0.982794$.

:::{figure} Images/Fig-ComplexNumbers-polarex2.svg
:name: Fig:ComplexNumbers:polarex2

The complex number $2+3i$.
:::

::::


::::{prf:example}

As a final example we consider $v=-1+2i$. Using Pythagoras theorem once again, we find that $|v|=\sqrt{(-1)^2+2^2} = \sqrt{5}$. For the argument, we say just as in the previous example that $\tan(\arg(v)) = \frac{-2}{1}$, so we would expect that $\arg(v) = \arctan( -2) \approx -1.10715$. But this answer is negative, while we can see in {numref}`Figure %s <Fig:ComplexNumbers:polarex3>` that the true argument is something between $\frac12\pi$ and $\pi$. Thus, this argument cannot be correct. If we multiply both the real and imaginary parts of a complex number by $-1$, then the quotient stays the same. Thus in this case the arctangent gives the argument of $1-2i$ instead. Fortunately, we can easily find the correct argument as it is exactly $\pi$ higher. We find $\arg(v) = \arctan(-2) + \pi \approx 2.03444$. 


:::{figure} Images/Fig-ComplexNumbers-polarex3.svg
:name: Fig:ComplexNumbers:polarex3

The complex number $-1+2i$.

:::

::::


You always have to check whether the value you find with the arctangent gives the correct angle. As the range of the arctangent is $\left(-\frac12\pi,\frac12\pi\right)$ you can only find the correct argument if the complex number is to the right of the imaginary axis, that is, if the real part is positive.

If the real part is negative, the argument is between $\frac12\pi$ and $\frac32\pi$ (or between $-\frac12\pi$ and $-\frac32\pi$ depending on which direction you want to consider) and outside the range of the arctangent. To get the correct value for the argument in these cases, you have to add or subtract $\pi$ from the arctangent.

If we write $z=a+bi$ and $r=|z|$ and $\theta=\arg(z)$, then we have the following formulas for calculating $a$ and $b$ from $r$ and $\theta$:

$$
a=r\cos(\theta), \qquad b=r\sin(\theta).
$$

For calculating $r$ and $\theta$ from $a$ and $b$ we can use

$$
r= \sqrt{a^2+b^2}, \qquad \tan(\theta)=\frac{b}{a},
$$

where it should be noted you cannot say $\theta= \arctan(b/a)$ in general. For $a\neq 0$, we can use

$$
\theta= \left\{ \begin{array}{lll} \arctan\left(\frac{b}{a}\right)&+2k\pi, & \text{if }a>0 \\  \arctan\left(\frac{b}{a}\right)+ \pi&+2k\pi, & \text{if }a<0. \\ \end{array}  \right.
$$

In particular, we see that the complex number with modulus $r$ and argument $\theta$ equals $r\bigl(\cos(\theta) + i\sin(\theta)\bigr)$ and vice versa. The form $r\cos(\theta) + ir\sin(\theta)$ is called the _polar form_ of the complex number:


::::{prf:definition}

The **polar form** of a complex number $z=a+bi$ is defined as

$$
z = r\bigl(\cos(\theta)+i\sin(\theta)),
$$

where $r=|z|$ is the modulus of $z$ and $\theta=\arg(z)$ is an argument of $z$.

::::


**Geometric interpretation of multiplication**

We can now see what happens to the product of two complex numbers. Suppose we have the complex number $z$ with modulus $|z|=r$ and argument $\arg(z)=\theta$. Hence, $z=r\cos(\theta) + i r\sin(\theta)$. The second complex number we consider is $w$ with modulus $|w|=s$ and argument $\arg(w) = \phi$; thus $w=s\cos(\phi) + i s \sin(\phi)$. We can then calculate the product using the addition formulas for cosine and sine.

\begin{align}
zw &= (r\cos(\theta) + i r \sin(\theta)) (s\cos(\phi) + is \sin(\phi))\label{Eq:ComplexNumbers:calcproduct} \\
&= rs \cos(\theta) \cos(\phi) + irs \cos(\theta) \sin(\phi) + irs \sin(\theta) \cos(\phi) + i^2 rs \sin(\theta) \sin(\phi)  \nonumber\\
&= rs( \cos(\theta) \cos(\phi) - \sin(\theta) \sin(\phi)) + irs (\cos(\theta) \sin(\phi) + \sin(\theta) \cos(\phi))\nonumber\\
&= rs \cos(\theta + \phi) + irs \sin(\theta+\phi) \nonumber
\end{align}

:::

We recognize this product as the number with modulus $|zw|=rs$ and argument $\arg(zw) = \theta+\phi$. In particular we find


::::{prf:theorem}

If you multiply two complex numbers, you multiply the moduli and add the arguments:

<ul>
<li> 

$|zw| = |z| \cdot |w|$,

</li>

<li>

$\arg(zw) = \arg(z) + \arg(w)$.

</li>
</ul>

If you divide the complex number $z$ by the complex number $w$ you divide the modulus of $z$ by the modulus of $w$ and subtract the argument of $w$ from the argument of $z$: 

<ul>
<li>

 $\left|\frac{z}{w}\right| = \frac{|z|}{|w|}$, 

</li>

<li>

$\arg\left(\frac{z}{w}\right) = \arg(z) - \arg(w)$. 

</li>
</ul>

::::


You can see the multiplication of $z$ and $w$ illustrated in {numref}`Figure %s <Fig:ComplexNumbers:multiplication>`.

:::{figure} Images/Fig-ComplexNumbers-multiplication.svg
:name: Fig:ComplexNumbers:multiplication

Multiplying complex numbers means adding the arguments and multiplying the moduli.

:::



## Euler's formula

**Euler's formula for the polar form of a complex number**

Given that the polar coordinates of a complex number are so convenient and that the polar form $r\cos(\theta) + i\sin(\theta)$ is such a long expression to write down, we would like to have a simple way of representing the complex number with given modulus $r$ and argument $\theta$. 

To find such a simple representation, consider the initial value problem


:::{math} 
:label: Eq:ComplexNumbers:exp_de

\left\{\begin{array}{rcl}
\dfrac{dy}{d\theta} & = & iy,\\
y(0) & = & r.
\end{array}\right.

:::

Because we assumed that $i$ behaves like any other number, we can solve this initial value problem, which leads to the solution


:::{math}
:label: Eq:ComplexNumbers:exp_sol

y(\theta) = re^{i\theta}.

:::


Now we have a solution, we put it aside and focus on another function $q$, which we define as


:::{math}
:label: Eq:ComplexNumbers:exp_sol_alt

q(\theta) = r\bigl(\cos(\theta)+i\sin(\theta)\bigr).

:::


Let us calculate first the value of $q$ in $\theta=0$:

\begin{align*}
q(0) &= r\left(\cos(0)+i\sin(0)\right) \\
 &= r\left(1-0i\right) \\
  &= r. 
\end{align*}

This indicates that $q$ satisfies the same initial condition from Equation {eq}`Eq:ComplexNumbers:exp_de` as the function $y$ from Equation {eq}`Eq:ComplexNumbers:exp_sol`. Could it also be that $q$ is a solution to the differential equation from Equation {eq}`Eq:ComplexNumbers:exp_de`? Let us investigate by looking at the first derivative of $q$:

\begin{align*}
\frac{dq}{d\theta} &= \frac{d}{d\theta}\Bigl[r\bigl(\cos(\theta)+i\sin(\theta)\bigr)\Bigr] \\
&= r\frac{d}{d\theta}\Bigl[\cos(\theta)+i\sin(\theta)\Bigr] \\
&= r\bigr(-\sin(\theta)+i\cos(\theta)\bigr) \\
&= r\bigr(i^2\sin(\theta)+i\cos(\theta)\bigr) \\
&= ir\bigr(i\sin(\theta)+\cos(\theta)\bigr) \\
&= ir\bigr(\cos(\theta)+i\sin(\theta)\bigr) \\
&= iq(\theta).
\end{align*}

So we found that our function $q$ from Equation {eq}`Eq:ComplexNumbers:exp_sol_alt` is also a solution to initial value problem from Equation {eq}`Eq:ComplexNumbers:exp_de`.

But because one initial value problem can only have one unique solution, the function $q$ from Equation {eq}`Eq:ComplexNumbers:exp_sol_alt` must be the same function as the first solution $y$ in Equation {eq}`Eq:ComplexNumbers:exp_sol`. This means that we found the identity

$$
re^{i\theta} = r\bigl(\cos(\theta) + i\sin(\theta)\bigr).
$$

This identity is called Euler's formula:


::::{prf:definition}

Let $r>0$ and $\theta\in\mathbb{R}$. Then

$$
re^{i\theta} = r\bigl(\cos(\theta) + i\sin(\theta)\bigr),
$$

which is called **Euler's formula**.

::::


You might think it is strange to use the number $e$ and superscripts which would suggest some sort of power of $e$. But it turns out this is very convenient as this expression satisfies the rules of calculation for exponentials. Indeed the calculation in Equation {eq}`Eq:ComplexNumbers:calcproduct` shows that

$$
(re^{i\theta}) (se^{i\phi} )= rse^{i(\theta+\phi)}.
$$

This corresponds precisely with the rules for multiplying exponentials. 

Thus, you can calculate with this strange notation $re^{i\phi}$ for complex numbers just as you would if you were indeed taking imaginary powers of $e$ ($=2.71828\ldots$). Some deep mathematics show that the definition given here is the only reasonable way to define taking imaginary exponents. 

In practice, this polar notation of complex numbers is convenient to use when you take products or powers, whereas the $a+bi$ notation is more convenient when you have to add complex numbers. 


::::{prf:example}

Let us calculate $(1+i)^6$. As this is a high power of a complex number, we use Euler's formula for the polar form. First, we write $1+i=\sqrt{2} e^{i \frac{\pi}{4}}$. Thus, we have

$$
(1+i)^6 = (\sqrt{2} e^{i\frac{\pi}{4}})^6 = \sqrt{2}^6 e^{i6\frac{\pi}{4}} = 8 e^{i \frac{3\pi}{2}} = -8i.
$$

::::


::::{prf:example}

Let us calculate $\dfrac{(1-\sqrt{3}i)^3}{(2+2i)^6}$. We have $1-\sqrt{3}i=2e^{-\frac{\pi}{3}}$ and $2+2i=2\sqrt{2} e^{i\frac{\pi}{4}}$. Thus, we obtain

$$
\frac{(1-\sqrt{3}i)^3}{(2+2i)^6} = \frac{(2e^{-\frac{\pi}{3}})^3}{(2\sqrt{2} e^{i\frac{\pi}{4}})^6}
= \frac{8e^{-\pi i}}{512 e^{i\frac{3\pi}{2}}} = \frac{1}{64} e^{-i\frac{5\pi}{2}} = -\frac{1}{64} i.
$$

::::


**De Moivre and other trigonometric identities**

The notation invented by Euler of $e^{i\theta} = \cos(\theta) + i\sin(\theta)$ allows use to quickly derive trigonometric identities. The most famous one is De Moivre's identity $e^{in\theta} = (e^{i\theta})^n$, which seems obvious now, but was discovered by De Moivre decades before the exponential notation was introduced and is a lot more impressive in the form 

$$
\cos(n\theta) + i \sin(n\theta) = \big(\cos(\theta) + i \sin(\theta)\big)^n.
$$


::::{prf:example}

De Moivre's identity allows us to find an expression for $\cos(3\theta)$ in terms of $\cos(\theta)$ and $\sin(\theta)$. Indeed, expanding the right hand side of the identity we have

\begin{align*}
\cos(3\theta) + i\sin(3\theta) &= \cos(\theta)^3 + 3i\cos(\theta)^2 \sin(\theta) + 3i^2 \cos(\theta) \sin(\theta)^2 + i^3 \sin(\theta)^3
\\&= \cos(\theta)^3 - 3\cos(\theta) \sin(\theta)^2 + i \big(3\cos(\theta)^2\sin(\theta) -\sin(\theta)^3\big).
\end{align*}

Comparing the real and imaginary parts on both sides of this equation we find

\begin{align*}
\cos(3\theta) &= \cos(\theta)^3-3\cos(\theta)\sin(\theta)^2, \\
\sin(3\theta) &= 3\cos(\theta)^2 \sin(\theta) - \sin(\theta)^3.
\end{align*}

::::


You can also easily derive other formulas.


::::{prf:example}

The formula for $\cos(\theta+\phi)$ is often used in calculus courses. The formula can be derived using De Moivre's identity. 

\begin{align*}
\cos(\theta+\phi) + i \sin(\theta +\phi) &= e^{i(\theta+ \phi)} \\
&= e^{i\theta} e^{i\phi} \\
&= \big(\cos(\theta) + i \sin(\theta)\big) \big(\cos(\phi) + i \sin(\phi)\big)
\\&=  \cos(\theta) \cos(\phi) + i \cos(\theta) \sin(\phi) + i \sin(\theta) \cos(\phi) + i^2 \sin(\theta) \sin(\phi) 
\\&=\cos(\theta) \cos(\phi) - \sin(\theta) \sin(\phi) + i \big(\sin(\theta) \cos(\phi) +\cos(\theta) \sin(\phi)\big)
\end{align*}

Thus $\cos(\theta+\phi) = \cos(\theta) \cos(\phi) - \sin(\theta) \sin(\phi)$. 

::::


**Solving $z^n=w$**

The most basic complex equations we want to solve are of the form $z^n=w$ for a given complex number $w$, where $z$ is the variable we want to solve for. Let's consider an example:


::::{prf:example}
:label: Ex:ComplexNumbers:threesolutions

Consider the equation $z^3=-16+16i$. We know it has 3 complex solutions, as it is a third degree equation. If we write $z=a+bi$ and expand (to find $a$ and $b$), we get a very large expression which is not easy to work with.

If we write $z=re^{i\phi}$ in polar coordinates instead, we can easily express $z^3=r^3e^{3i\phi}$. We also have to express the right hand side in polar coordinates: $-16+16i=16\sqrt{2} e^{\frac34 \pi i}$. Comparing the modulus and argument of these two expressions, we find

\begin{align*}
r^3&=|z^3|= |-16+16i| = 16\sqrt{2},\\
3\phi &= \arg(z^3) = \arg(-16+16i) = \frac34\pi.
\end{align*}

Taking a cube root, we find $r=2\sqrt{2}$. Note that $r>0$ is real, so here we need to consider only the single positive real solution, we don't want to find the complex solutions.

Moreover, we have $3\phi = \frac34\pi$, so $\phi = \frac14\pi$. This gives the solution $z=2\sqrt{2} e^{\frac14 \pi i}$. But this is just one solution and there ought to be two more by the fundamental theorem of algebra. So what are the remaining two?

As you know, the argument is only defined up to a multiple of $2\pi$. Thus, when we get the equation $3\phi = \frac34\pi$, we should actually write $3\phi = \frac34\pi + 2\pi k$ for some integer $k$. Dividing this by 3 gives $\phi = \frac14\pi + \frac23 \pi k$. We see that different values of $k$ give different values of $\phi$. For $k=0$, we obtain $\phi=\frac14\pi$ as before. For $k=1$, we obtain $\phi = \frac14\pi + \frac23\pi = \frac{11}{12}\pi$. For $k=2$, we have $\phi = \frac14\pi + \frac43\pi = \frac{19}{12}\pi$. For $k=3$, we obtain $\phi = \frac14\pi + 2\pi$. This gives the same complex number as $\phi=\frac14\pi$, as the argument is shifted by one full period. Indeed, if we add a multiple of 3 to $k$, the argument of $\phi$ is shifted by a multiple of $2\pi$ and thus the corresponding solution $z$ does not change. Therefore, only the cases $k=0$, $1$, and $2$ suffice to obtain all solutions. 

The three solutions, $z_0$, $z_1$ and $z_2$, to the equation $z^3=-16+16i$ thus are 

$$
\begin{array}{lllllllll}
z_0&=&2\sqrt{2} e^{\frac14\pi i} &=&  2\sqrt{2}\left( \cos\left(\frac14\pi\right) +  i\sin\left(\frac14\pi\right) \right) & = & 2+2i, \\ 
z_1&=& 2\sqrt{2} e^{\frac{11}{12}\pi i} &=& 2\sqrt{2} \left(\cos\left(\frac{11}{12}\pi\right) + i\sin\left(\frac{11}{12}\pi\right)\right) & = & (-1-\sqrt{3})+(-1+\sqrt{3})i, \\
z_2&=& 2\sqrt{2} e^{\frac{19}{12}\pi i} &=& 2\sqrt{2}\left(\cos\left(\frac{19}{12}\pi\right) +\sin\left(\frac{19}{12}\pi\right)\right) &=& (-1+\sqrt{3})+(-1-\sqrt{3})i. 
\end{array}
$$

You can find a visualisation of these three solutions in {numref}`Figure %s <Fig:ComplexNumbers:threesolfig>`.

:::{figure} Images/Fig-ComplexNumbers-threesolfig.svg
:name: Fig:ComplexNumbers:threesolfig

The three solutions from {prf:ref}`Ex:ComplexNumbers:threesolutions`.
:::

::::


We can generalize the method for solving $z^n=w$ from the example above. The steps are:
<ol>
<li> 

Write $z=re^{i\phi}$ (for unknown $r$ and $\phi$) and express the right hand side $w$ in polar coordinates. 

</li>
<li>

Obtain equations for the modulus $r$ and argument $\phi$ by equating the modulus and argument on both sides of this equation.

</li>
<li>

Solve for $r$ (you only need the single positive real solution). 

</li>

<li> 

Solve for $\phi$, remembering to add $+2\pi k$ first to the right hand side. 

</li>

<li>

You obtain all solutions to the equation by taking $n$ (the degree of the equation) subsequent values of $k$ in your expression of $\phi$. 

</li>

<li>

Combine the solution for $r$ and the $n$ values for $\phi$ to obtain the $n$ solutions.

</li>

</ol>

**Adding trigonometric functions**

Quite often, you come across expressions where a cosine and a sine of identical frequency are added. If you plot a function of the form $f(t)=b\cos(\omega t) + c\sin(\omega t)$, you notice that it becomes a new single wave. You can use complex numbers in a smart way to rewrite $f(t)$ to the form $A \cos(\omega t -\phi)$ as a single cosine with shifted argument. The variable $A$ gives the amplitude of the combined wave and the variable $\phi$ gives the phase-shift.


::::{prf:example}

Take $f(t) = \cos(2t) + \sqrt{3} \sin(2t)$. If you plot the graph of this function (see Figure \ref{figsinusoid}), you notice it is a single wave. 

Indeed, we have

\begin{align*}
f(t) &= \cos(2t) + \sqrt{3} \sin(2t) \\& = \Re\left(e^{2it}\right) + \Re\left(-i\sqrt{3} e^{2it}\right) 
\\&= \Re\left( e^{2it} -i\sqrt{3} e^{2it}\right) \\&= \Re\left( (1-i\sqrt{3}) e^{2it}\right) 
\\&= \Re\left( 2 e^{-\frac16 \pi i} e^{2it}\right) \\&= \Re\left(2 e^{i(2t-\frac16\pi)}\right) \\&= 2\cos\left(2t-\frac16 \pi\right).
\end{align*}

We first wrote both the cosine as the sine as real parts of complex exponentials. For the sine, we use that $-ie^{i\theta} = -i\cos(\theta) + \sin(\theta)$, so $\Re(-ie^{i\theta}) = \sin(\theta)$. Subsequently, we can take out the common factor $e^{2it}$; it is a common factor as the periods of both the cosine and sine are identical. Next, we rewrite $1-i\sqrt{3}$ in polar coordinates and work out what the result is.

:::{figure} Images/Fig-ComplexNumbers-sinusoid.svg
:name: Fig:ComplexNumbers:sinusoid

The graph of the sum of a cosine and a sine of identical period is a sinusoid as well.
:::

::::


::::{prf:example}

In the same way you can add two cosines (or sines) with shifted arguments. 

\begin{align*}
\cos\left(t+\frac13\pi\right) + \cos\left(t-\frac13\pi\right) &= \Re\left(e^{i\left(t+\frac13\pi\right)} + e^{i\left(t-\frac13\pi\right)}\right)
\\&= \Re\left(\left(e^{\frac13 \pi i} +e^{-\frac13\pi i}\right) e^{it}\right)
\\&= \Re\left( \left( \left( \frac12+\frac12\sqrt{3} i\right) + \left(\frac12 -\frac12\sqrt{3}i\right)\right)e^{it}\right)
\\&= \Re\left(   e^{it}\right)\\&= \cos(t).  
\end{align*}

::::


## Exercises


::::::{exercise}
:label: Exc:ComplexNumbers:eval_aplusbi

Evaluate the given expression and write your answer in the form $a+bi$.

<ol type="a">

<li>

$(3-2i)+(4+3i)$

</li>

<li>

$(4-2i)-(7+4i)$

</li>

<li>

$\overline{2-6i}$

</li>

<li>

$(1-3i)(2+4i)$

</li>

<li>

$(\overline{5-4i})(2+i)$

</li>

<li>

$\displaystyle\frac{8+4i}{2-2i}$

</li>

<li>

$\displaystyle\frac{6}{3+3i}$

</li>

<li>

$i^3$

</li>

<li>

$i^{50}$

</li>

<li>

$(2 + i)^{2}$

</li>

</ol>

::::::


::::::{exercise}
:label: Exc:ComplexNumbers:solve_aplusbi

Solve the equation by finding the relevant roots of the complex number in the form $a+bi$.

<ol type="a">

<li>

$z^4=1$

</li>

<li>

$z^3=-i$

</li>

</ol>

::::::


:::::{exercise}
:label: Exc:ComplexNumbers:complete

Find the roots of the quadratic polynomial by completing the square.

<ol type="a">

<li>

$2z^2-4z+10$

</li>

<li>

$z^2+(1-i)z-i$

</li>

<li>

$z^2+4z-12$

</li>

</ol>

:::::


:::::{exercise}
:label: Exc:ComplexNumbers:division

Find $h(z)=\frac{p(z)}{q(z)}$ if it is a polynomial using long division.

<ol type="a">

<li>

$p(z)=2z^5-3z^4-5z^3+2z^2-z-1$ and $q(z)=2z^3+z^2-z+1$

</li>

<li>

$p(z)=z^4+(3+i)z^3 + (- 2+4i)z^2 + (-3 + 2i)z+1-i$ and $q(z)=z^2+iz-1+i$

</li>

<li>

$p(z)=z^4+z^3-3z^2+5z-2$ and $q(z)=z^2-z+1$

</li>

</ol>

:::::


:::::{exercise}
:label: Exc:ComplexNumbers:roots

Find the roots of $p(z)$ and their multiplicities. Certain roots may already be given.

_(Hint: use long division and completing squares.)_

<ol type="a">

<li>

$p(z)=z^3-2z^2-5z+6$ with $p(1)=0$

</li>

<li>

$p(z)=z^4-2z^3+2z^2-2z+1$ with $p(i)=0$

</li>

<li>

$p(z)=z^4-5z^3+2z^2+22z-20$ with $p(3+i)=0 $

</li>

</ol>

:::::


:::::{exercise}
:label: Exc:ComplexNumbers:argmod

Find the argument and modulus of the complex number $z$.

<ol type="a">

<li>

$z=1-i$

</li>

<li>

$z=3+\sqrt{3}i$

</li>

</ol>

:::::


:::::{exercise}
:label: Exc:ComplexNumbers:polarform

Write the complex number in polar form $r\cos(\theta) +i r\sin (\theta)$ with $-\pi \leq \theta \leq \pi$.

<ol type="a">

<li>

$-1+i$

</li>

<li>

$3\sqrt{3}-3i$

</li>

</ol>

:::::


:::::{exercise}
:label: Exc:ComplexNumbers:polar_abi

Write the complex number in the form $a+bi$.

<ol type="a">

<li>

$2 \cos(\frac{\pi}{6})+ i 2 \sin(\frac{\pi}{6})$

</li>

<li>

$4 \cos(\frac{-3\pi}{4})+ i 4 \sin(\frac{-3\pi}{4})$

</li>

<li>

$e^{\frac12\pi i}$

</li>

<li>

$e^{\frac14\pi i}$

</li>

<li>

$2e^{-\frac13\pi i}$

</li>

</ol>

:::::


:::::{exercise}
:label: Exc:ComplexNumbers:polarform_calc

Find the polar forms of $z$ and $w$ and calculate $zw$, $\frac{z}{w}$ and $\frac{1}{z}$.

<ol type="a">

<li>

$z=1+\sqrt{3} i$ and $w=\sqrt{3}+i$

</li>

<li>

$z=2\sqrt{3}-2i$ and $w=2-2i$

</li>

</ol>

:::::


:::::{exercise}
:label: Exc:ComplexNumbers:DeMoivre

Use De Moivre's identity to derive a quadruple angle formula.

In other words to express $\cos(4\theta)$ and $\sin(4\theta)$ in terms of $\cos(\theta)$ and $\sin(\theta)$.

:::::


:::::{exercise}
:label: Exc:ComplexNumbers:solve_euler

Solve the equation by finding the relevant roots of the complex number in the Euler form.

<ol type="a">

<li>

$z^4=-16i$

</li>

<li>

$z^5=16\sqrt{2}+i16\sqrt{2}$

</li>

<li>

$z^3=4\cos(\frac{\pi}{6})+4i\sin(\frac{\pi}{6})$

</li>

</ol>

:::::


## Solutions



::::{solution} Exc:ComplexNumbers:eval_aplusbi
:class: dropdown

<ol type="a">

<li>

$7+i$

</li>

<li>

$-3-6i$

</li>

<li>

$2+6i$

</li>

<li>

$14-2i$

</li>

<li>

$6+13i$

</li>

<li>

$1+3i$

</li>

<li>

$1-i$

</li>

<li>

$-i$

</li>

<li>

$-1$

</li>

<li>

$3 + 4i$

</li>

</ol>

::::


::::{solution} Exc:ComplexNumbers:solve_aplusbi
:class: dropdown

<ol type="a">

<li>

$1, -1, i, -i$

</li>

<li>

$i, -\frac{1}{2}\sqrt{3}-i\frac{1}{2}, \frac{1}{2}\sqrt{3}-i\frac{1}{2}$

</li>

</ol>

::::


:::::{solution} Exc:ComplexNumbers:complete
:class: dropdown

<ol type="a">

<li>

$1+2i, 1-2i$

</li>

<li>

$-1, i$

</li>

<li>

$2, -6$

</li>

</ol>

:::::


:::::{solution} Exc:ComplexNumbers:division
:class: dropdown

<ol type="a">

<li>

$h(z)=z^2-2z-1$

</li>

<li>

$h(z)=z^2+3z-1$

</li>

<li>

$h(z)$ is not a polynomial.

</li>

</ol>

:::::


:::::{solution} Exc:ComplexNumbers:roots
:class: dropdown

<ol type="a">

<li>

The roots of $p(z)$ are $1, -2, 3$, all with multiplicity 1.

</li>

<li>

The roots of $p(z)$ are $i, -i, 1$, where $i$ an $-i$ have multiplicity 1 and $1$ has multiplicity 2.

</li>

<li>

The roots of $p(z)$ are $3+i, 3-i, 1, -2$, all with multiplicity 1.

</li>

</ol>

:::::


:::::{solution} Exc:ComplexNumbers:argmod
:class: dropdown

<ol type="a">

<li>

$|z|=\sqrt{2}$ and $\Arg(z)=-\frac{\pi}{4}$ or $\arg(z)=-\frac{\pi}{4}+2k\pi$ for some integer $k$;

</li>

<li>

$|z|=2\sqrt{3}$ and $\Arg(z)=\frac{\pi}{6}$ or $\arg(z)=\frac{\pi}{6}+2k\pi$ for some integer $k$.

</li>

</ol>

:::::


:::::{solution} Exc:ComplexNumbers:polarform
:class: dropdown

<ol type="a">

<li>

$\sqrt{2}\cos(\frac{3\pi}{4})+ i\sqrt{2}\sin(\frac{3\pi}{4})$

</li>

<li>

$6 \cos(\frac{-\pi}{6})+ i 6 \sin(\frac{-\pi}{6})$

</li>

</ol>

:::::


:::::{solution} Exc:ComplexNumbers:polar_abi
:class: dropdown

<ol type="a">

<li>

$\sqrt{3}+i$

</li>

<li>

$-2\sqrt{2}-2\sqrt{2}i$

</li>

<li>

$i$

</li>

<li>

$\frac{1}{\sqrt{2}} +\frac{1}{\sqrt{2}} i$

</li>

<li>

$1-\sqrt{3} i$

</li>

</ol>

:::::


:::::{solution} Exc:ComplexNumbers:polarform_calc
:class: dropdown

<ol type="a">

<li>

$z=2e^{\frac13\pi i}$ and $w=2e^{\frac16\pi i}$, thus $zw=4i$, $\frac{z}{w}=\frac{\sqrt{3}}{2}+\frac{1}{2} i$ and $\frac{1}{z}=\frac{1}{4}-\frac{\sqrt{3}}{4} i$.

</li>

<li>

$z=4e^{-\frac16\pi i}$ and $w=2\sqrt{2}e^{-\frac14\pi i}$, thus $zw=8 \sqrt{2} \cos\left(-\frac{5\pi}{12} \right) + 8\sqrt{2}\sin\left(-\frac{5\pi}{12} \right) i$, $\frac{z}{w}=\sqrt{2} \cos\left(\frac{\pi}{12} \right) + \sqrt{2} \sin\left(\frac{\pi}{12} \right) i$ and $\frac{1}{z}=\frac{\sqrt{3}}{8}+\frac{1}{8} i$.

</li>

</ol>

:::::


:::::{solution} Exc:ComplexNumbers:DeMoivre
:class: dropdown

$\cos(4\theta)=\cos^4(\theta)+\sin^4(\theta)-6\cos^2(\theta)\sin^2(\theta)$

and

$\sin(4\theta)=4\cos^3(\theta)\sin(\theta)-4\cos(\theta)\sin^3(\theta)$.

:::::


:::::{solution} Exc:ComplexNumbers:solve_euler
:class: dropdown

<ol type="a">

<li>

$ 2e^{i\frac{3\pi}{8}}, 2e^{i\frac{7\pi}{8}}, 2e^{i\frac{11\pi}{8}}, 2e^{i\frac{15\pi}{8}}$

</li>

<li>

$2e^{i\frac{\pi}{20}}, 2e^{i\frac{9\pi}{20}}, 2e^{i\frac{17\pi}{20}}, 2e^{i\frac{5\pi}{4}}, 2e^{i\frac{33\pi}{20}}$

</li>

<li>

$4^{\frac{1}{3}}e^{i\frac{\pi}{18}}, 4^{\frac{1}{3}}e^{i\frac{13\pi}{18}}, 4^{\frac{1}{3}}e^{i\frac{25\pi}{18}}$

</li>

</ol>

:::::