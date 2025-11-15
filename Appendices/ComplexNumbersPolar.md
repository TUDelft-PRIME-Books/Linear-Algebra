(Ch:ComplexNumbersPolar)=
# Polar form of complex numbers

## Modulus and argument

To consider the multiplication of complex numbers, it is best to first consider the polar coordinates of a complex number. Polar coordinates is a concept that works for points in a plane. The idea is that instead of looking at the $x$ and $y$ coordinates of a point, we describe the point by the distance to the origin and the direction from the origin.

The distance from zero to the point in the complex plane, we call the _modulus_ $|z|$. By using Pythagoras theorem and with $z=a+bi$, it holds that $|z|=\sqrt{a^2+b^2}$ and equivalently $|z|=\sqrt{z\overline{z}}$. We often denote the modulus by the symbol $r$, so $r=|z|$. The direction is designated by the angle measured from the positive real axis in a anticlockwise direction towards the ray from zero through the point. This angle, we call the _argument_ or $\arg(z)$ as seen in {numref}`Figure %s <Fig:ComplexNumbers:modarg>`. We often denote the argument by the symbol $\theta$, so $\theta=\arg(z)$. The argument uses the convention similar to the unit circle: the direction straight the right corresponds to $0$ radians, up corresponds to $\frac{1}{2}\pi$ radians, to the left to $\pi$ radians and down to $\frac{3}{2}\pi$ radians.

:::{figure} Images/Fig-ComplexNumbers-modarg.svg
:name: Fig:ComplexNumbers:modarg
:class: dark-light

The polar coordinates of a point in the complex plane $\C$ are the distance $r=|z|$ from zero to the point and the angle $\theta=\arg(z)$ measured from the positive real axis in a anticlockwise direction towards the ray from zero through the point.

:::

Notice that the argument is not uniquely defined, as you can always go a full circle extra and add $2\pi$ radians to the angle. For example, the number $1$ has argument $0$ (as it is on the positive real axis), but also $2\pi$, $4\pi$, and $-2\pi$ (etc.). In order to make a uniform choice, we sometimes work with the principal value of the argument, which is by definition the unique value of the argument between $-\pi$ and $\pi$.
We write the principal value using a capital A. Thus we have $-\pi < \arg{z} \leq \pi$.

::::{prf:example}
:label: Ex:ComplexNumbers:polarex1

Suppose $z=3+3i$. We find by using Pythagoras that the modulus (the distance to the origin) equals $|z|=\sqrt{3^2+3^2}=3\sqrt{2}$. The argument, the corresponding angle, equals $\frac14\pi$ as you can see in {numref}`Figure %s <Fig:ComplexNumbers:polarex1>`.

:::{figure} Images/Fig-ComplexNumbers-polarex1.svg
:name: Fig:ComplexNumbers:polarex1
:class: dark-light

The complex number $3+3i$.

:::

::::

::::{prf:example}
:label: Ex:ComplexNumbers:polarex2

Suppose $w=2+3i$. We can still use Pythagoras for the modulus and obtain $|w|=\sqrt{2^2+3^2} = \sqrt{13}$. The argument can't be deduced immediately from a picture, see {numref}`Figure %s <Fig:ComplexNumbers:polarex2>`, but we do see that

$$
\tan(\arg(w)) = \frac{\text{opposite}}{\text{adjacent}} = \frac{\text{imaginary part}}{\text{real part}} = \frac{3}{2}
$$

Therefore $\arg(w) = \arctan\left(\frac32\right) \approx 0.982794$.

:::{figure} Images/Fig-ComplexNumbers-polarex2.svg
:name: Fig:ComplexNumbers:polarex2
:class: dark-light

The complex number $2+3i$.
:::

::::

::::{prf:example}
:label: Ex:ComplexNumbers:polarex3

As a final example we consider $v=-1+2i$. Using Pythagoras theorem once again, we find that $|v|=\sqrt{(-1)^2+2^2} = \sqrt{5}$. For the argument, we obtain that, just as in the previous example, $\tan(\arg(v)) = \frac{2}{-1}$, so we would expect that $\arg(v) = \arctan( -2) \approx -1.10715$. But this answer is negative, while we can see in {numref}`Figure %s <Fig:ComplexNumbers:polarex3>` that the true argument is something between $\frac12\pi$ and $\pi$. Thus, this argument cannot be correct. If we multiply both the real and imaginary parts of a complex number by $-1$, then the quotient stays the same. Thus in this case the arctangent gives the argument of $1-2i$ instead. Fortunately, we can easily find the correct argument as it is exactly $\pi$ higher. We find $\arg(v) = \arctan(-2) + \pi \approx 2.03444$.

:::{figure} Images/Fig-ComplexNumbers-polarex3.svg
:name: Fig:ComplexNumbers:polarex3
:class: dark-light

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
\theta= \left\{ \begin{array}{lll} \arctan\left(\frac{b}{a}\right)&+2k\pi, & \text{if }a>0, \\  \arctan\left(\frac{b}{a}\right)+ \pi&+2k\pi, & \text{if }a<0, \\ \end{array}  \right.\quad\text{where $k\in\mathbb{Z}$.}
$$

In particular, we see that the complex number with modulus $r$ and argument $\theta$ equals $r\bigl(\cos(\theta) + i\sin(\theta)\bigr)$ and vice versa. The form $r\cos(\theta) + ir\sin(\theta)$ is called the _polar form_ of the complex number:

::::{prf:definition}
:label: Def:ComplexNumbers:polarform

The **polar form** of a complex number $z=a+bi$ is defined as

$$
z = r\bigl(\cos(\theta)+i\sin(\theta)),
$$

where $r=|z|$ is the modulus of $z$ and $\theta=\arg(z)$ is an argument of $z$.

::::

## Geometric interpretation

First we consider conjugation. Suppose $z$ is the complex number with modulus $|z|=r$ and argument $\arg(z)=\theta$. Hence, $z=r\cos(\theta) + i r\sin(\theta)$ and $\overline{z}=r\cos(\theta) - i r\sin(\theta)$. This least equation we can rewrite:

:::{math}
:label: Eq:ComplexNumbers:calcconj

\begin{align*}
\overline{z} &= r\cos(\theta) - i r\sin(\theta) \\
&= r\cos(\theta) + i r\sin(-\theta) \\
&= r\cos(-\theta) + i r\sin(-\theta).
\end{align*}

:::

From the last line we see that conjugating a complex number means negating the argument of that complex number.

We can now see what happens to the product of two complex numbers. Suppose we have the complex number $z$ with modulus $|z|=r$ and argument $\arg(z)=\theta$. Hence, $z=r\cos(\theta) + i r\sin(\theta)$. The second complex number we consider is $w$ with modulus $|w|=s$ and argument $\arg(w) = \phi$; thus $w=s\cos(\phi) + i s \sin(\phi)$. We can then calculate the product using the addition formulas for cosine and sine.

:::{math}
:label: Eq:ComplexNumbers:calcproduct

\begin{align*}
zw &= (r\cos(\theta) + i r \sin(\theta)) (s\cos(\phi) + is \sin(\phi))
\\&= rs \cos(\theta) \cos(\phi) + irs \cos(\theta) \sin(\phi) + irs \sin(\theta) \cos(\phi) + i^2 rs \sin(\theta) \sin(\phi)
\\&= rs( \cos(\theta) \cos(\phi) - \sin(\theta) \sin(\phi)) + irs (\cos(\theta) \sin(\phi) + \sin(\theta) \cos(\phi))
\\&= rs \cos(\theta + \phi) + irs \sin(\theta+\phi)
\end{align*}

:::

We recognize this product as the number with modulus $|zw|=rs$ and argument $\arg(zw) = \theta+\phi$. In particular we find:

::::{prf:theorem}
:label: Thm:ComplexNumbers:polarmultdiv

If you take the complex conjugate of a complex number $z$, the modulus remains the same and the argument is negated:

<ul>
<li>

$|\overline{z}| = |z|$,

</li>

<li>

$\arg(\overline{z}) = -\arg(z)$.

</li>
</ul>

If you multiply two complex numbers $z$ and $w$, you multiply the moduli and add the arguments:

<ul>
<li>

$|zw| = |z| \cdot |w|$,

</li>

<li>

$\arg(zw) = \arg(z) + \arg(w)$.

</li>
</ul>

If you divide the complex number $z$ by the complex number $w\neq0$ you divide the modulus of $z$ by the modulus of $w$ and subtract the argument of $w$ from the argument of $z$:

<ul>
<li>

$\left|\frac{z}{w}\right| = \frac{|z|}{|w|}$,

</li>

<li>

$\arg\left(\frac{z}{w}\right) = \arg(z) - \arg(w)$.

</li>
</ul>

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:polarmultdiv`
:class: dropdown, tudproof
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:polarmultdiv` -->

_Proof for conjugation_

With $|z|=r$ and $\arg{z}=\theta$, Equation {eq}`Eq:ComplexNumbers:calcconj` shows that $|\overline{z}|=|z|$ and $\arg(\overline{z})=-\arg(z)$.

_Proof for multiplication_

With $|z|=r$, $|w|=s$, $\arg{z}=\theta$ and $\arg{w}=\phi$, Equation {eq}`Eq:ComplexNumbers:calcproduct` shows that $|zw| = |z| \cdot |w|$ and $\arg(zw) = \arg(z) + \arg(w)$.

_Proof for division_

For division (assuming $w\neq0$) we do the following:

\begin{align*}
\frac{z}{w} &= \frac{z\overline{w}}{w\overline{w}} \\
&= \frac{rs\left(\cos(\theta-\phi)+i\sin(\theta-\phi)\right)}{s^2} \\
&= \frac{r}{s}\left(\cos(\theta-\phi)+i\sin(\theta-\phi)\right),
\end{align*}
where the last line shows that $\left|\frac{z}{w}\right| = \frac{|z|}{|w|}$ and $\arg\left(\frac{z}{w}\right) = \arg(z) - \arg(w)$.

::::

You can see each of these operations illustrated in {numref}`Figures %s <Fig:ComplexNumbers:conjugation>`, {numref}`%s <Fig:ComplexNumbers:multiplication>` and {numref}`%s <Fig:ComplexNumbers:division>`.

:::{figure} Images/Fig-ComplexNumbers-conjugation.svg
:name: Fig:ComplexNumbers:conjugation
:class: dark-light

Conjugating a complex number means negating the argument and keeping the modulus the same.

:::

:::{figure} Images/Fig-ComplexNumbers-multiplication.svg
:name: Fig:ComplexNumbers:multiplication
:class: dark-light

Multiplying complex numbers means adding the arguments and multiplying the moduli.

:::

:::{figure} Images/Fig-ComplexNumbers-division.svg
:name: Fig:ComplexNumbers:division
:class: dark-light

Dividig complex numbers means substracting the arguments and dividing the moduli.

:::

## Euler's formula

Given that the polar coordinates of a complex number are so convenient and that the polar form $r\left(\cos(\theta) + i\sin(\theta)\right)$ is such a long expression to write down, we would like to have a simple way of representing the complex number with given modulus $r$ and argument $\theta$.

Therefore we introduce the following identity:

::::{prf:definition}
:label: Dfn:ComplexNumbers:EulersFormule

Let $\theta\in\mathbb{R}$. Then

$$
e^{i\theta} = \cos(\theta) + i\sin(\theta),
$$

which is called **Euler's formula**.

::::

Using this definition we even can prove the following theorem:

::::{prf:theorem}
:label: Thm:ComplexNumbers:re

Let $z=a+bi$ with $a,b\in\mathbb{R}$ and define $r=|z|$ and $\theta=\arg{z}$. Then

$$
z = re^{i\theta}.
$$

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:re`
:class: dropdown, tudproof
<!-- ::::{dropdown} Proof of {prf:ref}`Thm:ComplexNumbers:re` -->

The proof is relatively straight forward:

$$
z = a+bi = r\left(\cos(\theta)+i\sin(\theta)\right) = re^{i\theta}.
$$

::::

We can even show that the following property of the derivative still is true:

::::{prf:theorem}
:label: Thm:ComplexNumbers:re_diff

Let $\theta\in\mathbb{R}$. Then

$$
\frac{d}{d\theta}\left[e^{i\theta}\right] = ie^{i\theta}.
$$

::::

::::{admonition} Proof of {prf:ref}`Thm:ComplexNumbers:re_diff`
:class: dropdown, tudproof

The proof is again straight forward:

\begin{align*}
\frac{d}{d\theta}\left[e^{i\theta}\right] &= \frac{d}{d\theta}\left[\cos(\theta)+i\sin(\theta)\right] \\
&= \frac{d}{d\theta}\left[\cos(\theta)\right]+i\frac{d}{d\theta}\left[\sin(\theta)\right] \\
&= -\sin(\theta)+i\cos(\theta) \\
&= i^2\sin(\theta)+i\cos(\theta) \\
&= i\cos(\theta)+i^2\sin(\theta) \\
&= i\left(\cos(\theta)+i\sin(\theta)\right) \\
&= ie^{i\theta}.
\end{align*}

::::

You might think it is strange to use the number $e$ and superscripts which would suggest some sort of power of $e$. But it turns out this is very convenient as this expression satisfies the rules of calculation for exponentials. Indeed the calculation in Equation {eq}`Eq:ComplexNumbers:calcproduct` shows that

$$
(re^{i\theta}) (se^{i\phi} )= rse^{i(\theta+\phi)}.
$$

This corresponds precisely with the rules for multiplying exponentials.

Thus, you can calculate with this strange notation $re^{i\theta}$ for complex numbers just as you would if you were indeed taking imaginary powers of $e$ ($=2.71828\ldots$). Some deep mathematics show that the definition given here is the only reasonable way to define taking imaginary exponents.

In practice, this polar notation of complex numbers is convenient to use when you take products or powers, whereas the $a+bi$ notation is more convenient when you have to add complex numbers.

::::{prf:example}
:label: Ex:ComplexNumbers:highpower

Let us calculate $(1+i)^6$. As this is a high power of a complex number, we use Euler's formula for the polar form. First, we write $1+i=\sqrt{2} e^{i \frac{\pi}{4}}$. Thus, we have

$$
(1+i)^6 = (\sqrt{2} e^{i\frac{\pi}{4}})^6 = \sqrt{2}^6 e^{i6\frac{\pi}{4}} = 8 e^{i \frac{3\pi}{2}} = -8i.
$$

::::

::::{prf:example}
:label: Ex:ComplexNumbers:threesolutions

Let us calculate $\dfrac{(1-\sqrt{3}i)^3}{(2+2i)^6}$. We have $1-\sqrt{3}i=2e^{-i\frac{\pi}{3}}$ and $2+2i=2\sqrt{2} e^{i\frac{\pi}{4}}$. Thus, we obtain

$$
\frac{(1-\sqrt{3}i)^3}{(2+2i)^6} = \frac{(2e^{-i\frac{\pi}{3}})^3}{(2\sqrt{2} e^{i\frac{\pi}{4}})^6}
= \frac{8e^{-\pi i}}{512 e^{i\frac{3\pi}{2}}} = \frac{1}{64} e^{-i\frac{5\pi}{2}} = -\frac{1}{64} i.
$$

::::

**De Moivre and other trigonometric identities**

The notation invented by Euler of $e^{i\theta} = \cos(\theta) + i\sin(\theta)$ allows us to quickly derive trigonometric identities. The most famous one is De Moivre's identity $e^{in\theta} = (e^{i\theta})^n$, which seems obvious now, but was discovered by De Moivre decades before the exponential notation was introduced and is a lot more impressive in the form

$$
\cos(n\theta) + i \sin(n\theta) = \big(\cos(\theta) + i \sin(\theta)\big)^n.
$$

::::{prf:example}
:label: Ex:ComplexNumbers:DeMoivre

De Moivre's identity allows us to find an expression for $\cos(3\theta)$ in terms of $\cos(\theta)$ and $\sin(\theta)$. Indeed, expanding the right-hand side of the identity we have

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
:label: Ex:ComplexNumbers:cos_sin_sum

Formulas for $\cos(\theta+\phi)$ and $\sin(\theta+\phi)$ are often used in calculus courses. These formulas can be derived using De Moivre's identity.

\begin{align*}
\cos(\theta+\phi) + i \sin(\theta +\phi) &= e^{i(\theta+ \phi)} \\
&= e^{i\theta} e^{i\phi} \\
&= \big(\cos(\theta) + i \sin(\theta)\big) \big(\cos(\phi) + i \sin(\phi)\big)
\\&= \cos(\theta) \cos(\phi) + i \cos(\theta) \sin(\phi) + i \sin(\theta) \cos(\phi) + i^2 \sin(\theta) \sin(\phi)
\\&=\cos(\theta) \cos(\phi) - \sin(\theta) \sin(\phi) + i \big(\sin(\theta) \cos(\phi) +\cos(\theta) \sin(\phi)\big)
\end{align*}

Thus $\cos(\theta+\phi) = \cos(\theta) \cos(\phi) - \sin(\theta) \sin(\phi)$ and $\sin(\theta +\phi)=\sin(\theta) \cos(\phi) +\cos(\theta) \sin(\phi)$.

::::

**Solving $z^n=w$**

The most basic equations we want to solve are of the form $z^n=w$ for a given complex number $w$, where $z$ is the variable we want to solve for. Let's consider an example:

::::{prf:example}
:label: Ex:ComplexNumbers:threesolutions2

Consider the equation $z^3=-16+16i$. We know it has $3$ complex solutions, as it is a third degree equation. If we write $z=a+bi$ and expand (to find $a$ and $b$), we get a very large expression which is not easy to work with.

If we write $z=re^{i\phi}$ in polar coordinates instead, we can easily express $z^3=r^3e^{3i\phi}$. We also have to express the right-hand side in polar coordinates: $-16+16i=16\sqrt{2} e^{\frac34 \pi i}$. Comparing the modulus and argument of these two expressions, we find

\begin{align*}
r^3&=|z^3|= |-16+16i| = 16\sqrt{2},\\
3\phi &= \arg(z^3) = \arg(-16+16i) = \frac34\pi.
\end{align*}

Taking a cube root, we find $r=2\sqrt{2}$. Note that $r>0$ is real, so here we need to consider only the single positive real solution, we don't want to find the complex solutions.

Moreover, we have $3\phi = \frac34\pi$, so $\phi = \frac14\pi$. This gives the solution $z=2\sqrt{2} e^{\frac14 \pi i}$. But this is just one solution and there ought to be two more by the fundamental theorem of algebra. So what are the remaining two?

As you know, the argument is only defined up to a multiple of $2\pi$. Thus, when we get the equation $3\phi = \frac34\pi$, we should actually write $3\phi = \frac34\pi + 2\pi k$ for some integer $k$. Dividing this by $3$ gives $\phi = \frac14\pi + \frac23 \pi k$. We see that different values of $k$ give different values of $\phi$. For $k=0$, we obtain $\phi=\frac14\pi$ as before. For $k=1$, we obtain $\phi = \frac14\pi + \frac23\pi = \frac{11}{12}\pi$. For $k=2$, we have $\phi = \frac14\pi + \frac43\pi = \frac{19}{12}\pi$. For $k=3$, we obtain $\phi = \frac14\pi + 2\pi$. This gives the same complex number as $\phi=\frac14\pi$, as the argument is shifted by one full period. Indeed, if we add a multiple of $3$ to $k$, the argument of $\phi$ is shifted by a multiple of $2\pi$ and thus the corresponding solution $z$ does not change. Therefore, only the cases $k=0$, $k=1$, and $k=2$ suffice to obtain all solutions.

The three solutions, $z_0$, $z_1$ and $z_2$, to the equation $z^3=-16+16i$ thus are

$$
\begin{array}{lllllllll}
z_0&=&2\sqrt{2} e^{\frac14\pi i} &=&  2\sqrt{2}\left( \cos\left(\frac14\pi\right) +  i\sin\left(\frac14\pi\right) \right) & = & 2+2i, \\
z_1&=& 2\sqrt{2} e^{\frac{11}{12}\pi i} &=& 2\sqrt{2} \left(\cos\left(\frac{11}{12}\pi\right) + i\sin\left(\frac{11}{12}\pi\right)\right) & = & (-1-\sqrt{3})+(-1+\sqrt{3})i, \\
z_2&=& 2\sqrt{2} e^{\frac{19}{12}\pi i} &=& 2\sqrt{2}\left(\cos\left(\frac{19}{12}\pi\right) +i\sin\left(\frac{19}{12}\pi\right)\right) &=& (-1+\sqrt{3})+(-1-\sqrt{3})i.
\end{array}
$$

You can find a visualisation of these three solutions in {numref}`Figure %s <Fig:ComplexNumbers:threesolfig>`.

```{applet}
:url: appendix/complex_numbers
:fig: Images/Fig-ComplexNumbers-threesolfig.svg
:name: Fig:ComplexNumbers:threesolfig
:status: approved
:class: dark-light

The three solutions from {prf:ref}`Ex:ComplexNumbers:threesolutions2`.
```

::::

We can generalise the method for solving $z^n=w$ from the example above:

```{prf:algorithm} Solving $z^n=w$

<ol>
<li>

Write $z=re^{i\phi}$ (for unknown $r$ and $\phi$) and express the right-hand side $w$ in polar coordinates.

</li>
<li>

Obtain equations for the modulus $r$ and argument $\phi$ by equating the modulus and argument on both sides of this equation.

</li>
<li>

Solve for $r$ (you only need the single positive real solution).

</li>

<li>

Solve for $\phi$, remembering to add $+2\pi k$ first to the right-hand side.

</li>

<li>

You obtain all solutions to the equation by taking $n$ (the degree of the equation) subsequent values of $k$ in your expression of $\phi$.

</li>

<li>

Combine the solution for $r$ and the $n$ values for $\phi$ to obtain the $n$ solutions.

</li>

</ol>

```

**Adding trigonometric functions**

Quite often, you come across expressions where a cosine and a sine of identical frequency are added. If you plot a function of the form $f(t)=b\cos(\omega t) + c\sin(\omega t)$, you notice that it becomes a new single wave. You can use complex numbers in a smart way to rewrite $f(t)$ to the form $A \cos(\omega t -\phi)$ as a single cosine with shifted argument. The variable $A$ gives the amplitude of the combined wave and the variable $\phi$ gives the phase-shift.

::::{prf:example}
:label: Ex:ComplexNumbers:sinusoid

Take $f(t) = \cos(2t) + \sqrt{3} \sin(2t)$. If you plot the graph of this function (see {numref}`Figure %s <Fig:ComplexNumbers:sinusoid>`), you notice it is a single wave.

Indeed, we have

\begin{align*}
f(t) &= \cos(2t) + \sqrt{3} \sin(2t) \\& = \Re{e^{2it}} + \Re{-i\sqrt{3} e^{2it}}
\\&= \Re{ e^{2it} -i\sqrt{3} e^{2it}} \\&= \Re{(1-i\sqrt{3}) e^{2it}}
\\&= \Re{ 2 e^{-\frac13 \pi i} e^{2it}} \\&= \Re{2 e^{i(2t-\frac13\pi)}} \\&= 2\cos\left(2t-\frac13 \pi\right).
\end{align*}

We first wrote both the cosine as the sine as real parts of complex exponentials. For the sine, we use that $-ie^{i\theta} = -i\cos(\theta) + \sin(\theta)$, so $\Re{-ie^{i\theta}} = \sin(\theta)$. Subsequently, we can take out the common factor $e^{2it}$; it is a common factor as the periods of both the cosine and sine are identical. Next, we rewrite $1-i\sqrt{3}$ in polar coordinates and work out what the result is.

:::{figure} Images/Fig-ComplexNumbers-sinusoid.svg
:name: Fig:ComplexNumbers:sinusoid
:class: dark-light

The graph of the sum of a cosine and a sine of identical period is a sinusoid as well.
:::

::::

::::{prf:example}
:label: Ex:ComplexNumbers:cos_sin_shift

In the same way you can add two cosines (or sines) with shifted arguments.

\begin{align*}
\cos\left(t+\frac13\pi\right) + \cos\left(t-\frac13\pi\right) &= \Re{e^{i\left(t+\frac13\pi\right)}} + \Re{e^{i\left(t-\frac13\pi\right)}}
\\&= \Re{\left(e^{\frac13 \pi i} +e^{-\frac13\pi i}\right) e^{it}}
\\&= \Re{ \left( \left( \frac12+\frac12\sqrt{3} i\right) + \left(\frac12 -\frac12\sqrt{3}i\right)\right)e^{it}}
\\&= \Re{ e^{it}}\\&= \cos(t).  
\end{align*}

::::

## Derivations of Euler's formula

**Using a scalar initial value problem**

To find Euler's formula, consider the initial value problem

:::{math}
:label: Eq:ComplexNumbers:exp_de

\left\{\begin{array}{rcl}
\dfrac{dy}{d\theta} & = & iy,\\
y(0) & = & 1.
\end{array}\right.

:::

Because we assumed that $i$ behaves like any other number, we can solve this initial value problem, which leads to the solution

:::{math}
:label: Eq:ComplexNumbers:exp_sol

y(\theta) = e^{i\theta}.

:::

Now we have a solution, we put it aside and focus on another function $q$, which we define as

:::{math}
:label: Eq:ComplexNumbers:exp_sol_alt

q(\theta) = \cos(\theta)+i\sin(\theta).

:::

Let us calculate first the value of $q$ in $\theta=0$:

\begin{align*}
q(0) &= \cos(0)+i\sin(0) \\
&= 1-0i \\
&= 1.
\end{align*}

This indicates that $q$ satisfies the same initial condition from Equation {eq}`Eq:ComplexNumbers:exp_de` as the function $y$ from Equation {eq}`Eq:ComplexNumbers:exp_sol`. Could it also be that $q$ is a solution to the differential equation from Equation {eq}`Eq:ComplexNumbers:exp_de`? Let us investigate by looking at the first derivative of $q$:

\begin{align*}
\frac{dq}{d\theta} &= \frac{d}{d\theta}\Bigl[\cos(\theta)+i\sin(\theta)\Bigr] \\
&= -\sin(\theta)+i\cos(\theta) \\
&= i^2\sin(\theta)+i\cos(\theta) \\
&= i\bigr(i\sin(\theta)+\cos(\theta)\bigr) \\
&= i\bigr(\cos(\theta)+i\sin(\theta)\bigr) \\
&= iq(\theta).
\end{align*}

So we found that our function $q$ from Equation {eq}`Eq:ComplexNumbers:exp_sol_alt` is also a solution to initial value problem from Equation {eq}`Eq:ComplexNumbers:exp_de`.

But because this initial value problem can only have one unique solution, the function $q$ from Equation {eq}`Eq:ComplexNumbers:exp_sol_alt` must be the same function as the first solution $y$ in Equation {eq}`Eq:ComplexNumbers:exp_sol`. This means that we found Euler's formula:

$$
e^{i\theta} = \cos(\theta) + i\sin(\theta).
$$

**Using series**

Euler's formula can also be derived using series. You may already be familiar with the following three series

\begin{align*}
e^x &= \sum_{n=0}^\infty\frac{x^n}{n!}, \\
\cos(x) &= \sum_{k=0}^\infty(-1)^k\frac{x^{2k}}{(2k)!}, \\
\sin(x) &= \sum_{l=0}^\infty(-1)^l\frac{x^{2l+1}}{(2l+1)!}.
\end{align*}

We can use these series to derive Euler's formula.

First consider the following $12$ powers of the complex number $\theta i$ with $\theta\in\mathbb{R}$:

\begin{align*}
(\theta i)^0 &= 1 & (\theta i)^4 &= \theta^4 & (\theta i)^8 &= \theta^8 \\
(\theta i)^1 &= \theta i & (\theta i)^5 &= \theta^5 i & (\theta i)^9 &= \theta^9 i \\
(\theta i)^2 &= -\theta^2 & (\theta i)^6 &= -\theta^6 & (\theta i)^{10} &= -\theta^{10}i \\
(\theta i)^3 &= -\theta^3 i & (\theta i)^7 &= -\theta^7 i & (\theta i)^{11} &= -\theta^{11}i \\
\end{align*}

Do you notice the pattern that _even_ powers give _real_ numbers and _odd_ powers give _complex_ numbers with zero real part? And also that for the list of even powers the sign flips each time? And the same for the odd powers?

Now let us consider $e^{\theta i}$ and expand the series of the exponential function using these patterns:

$$
\begin{align*}
e^{\theta i} &= \sum_{n=0}^\infty\frac{(\theta i)^n}{n!} & &\text{Using the series of $e^x$} \\
&= \sum_{\substack{n=0\\n~{\rm even}}}^\infty\frac{(\theta i)^n}{n!}+\sum_{\substack{n=0\\n~{\rm odd}}}^\infty\frac{(\theta i)^n}{n!} & &\text{Using the odd/even pattern seen above.} \\
&= \sum_{k=0}^\infty\frac{(\theta i)^{2k}}{(2k)!}+\sum_{l=0}^\infty\frac{(\theta i)^{2l+1}}{(2l+1)!} & &\text{Changing the indices using $n=2k$ and $n=2l+1$.} \\
&= \sum_{k=0}^\infty(-1)^{k}\frac{\theta^{2k}}{(2k)!}+\sum_{l=0}^\infty(-1)^l\frac{\theta^{2l+1}i}{(2l+1)!} & &\text{Using the alternating patterns seen above.} \\
&= \sum_{k=0}^\infty(-1)^{k}\frac{\theta^{2k}}{(2k)!}+i\sum_{l=0}^\infty(-1)^l\frac{\theta^{2l+1}}{(2l+1)!} & &\text{Taking $i$ out of the second series.} \\
&= \cos(\theta)+i\sin(\theta). & &\text{Using the series of $\cos(x)$ and $\sin(x)$.}
\end{align*}
$$

As you can see we have arrived at Euler's formula.

## Grasple exercises

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c849196d-814e-430f-aba7-4f39afa10923?id=122764
:label: grasple_exercise_10_2_1
:dropdown:
:description: From polar form to Cartesian form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fd366551-a8d4-40c2-ad7e-b21581677f96?id=122765
:label: grasple_exercise_10_2_2
:dropdown:
:description: From Cartesian form to polar form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a02fe0b8-24e9-484f-90ff-cb1519472bd2?id=122767
:label: grasple_exercise_10_2_3
:dropdown:
:description: Multiplication of powers of complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/740aeed0-d2e2-4259-9cdc-4e3533d10d51?id=122769
:label: grasple_exercise_10_2_4
:dropdown:
:description: Division of powers of complex numbers.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/7f2ff406-3652-47b7-ba0d-52343cb8eb4c?id=122771
:label: grasple_exercise_10_2_5
:dropdown:
:description: Cubic root of a complex number.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/22b66edd-aa49-489a-880b-3d91f864b6be?id=122772
:label: grasple_exercise_10_2_6
:dropdown:
:description: Fourth root of a complex number.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8000e2fb-af73-476b-8977-0c0ecbe5cb3d?id=122773
:label: grasple_exercise_10_2_7
:dropdown:
:description: A slightly different cubic root question.

::::