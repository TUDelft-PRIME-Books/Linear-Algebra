<!-- ---
csp:
  frame-ancestors: 'self' https://embed.grasple.com/;
---
 -->
(Section:LinSystems)=

# Systems of Linear Equations

(Subsec:LinSystems:Intro)=

## Consistent and Inconsistent Linear Systems

In Chapter 1 the question whether two lines or two planes intersect or do not intersect was touched upon. In the case of two planes the question can be resolved by finding equations for the planes and checking whether there are points that simultaneously satisfy these two equations. We can write this in the form

$$
  \left\{\begin{array}{ccccccc}
       a_1x_1 &+& a_2x_2 &+& a_3x_3 &=& c_1 \\
      b_1x_1 &+& b_2x_2 &+& b_3x_3 &=& c_2
       \end{array}
  \right.
$$

which we will call a system of two linear equations in three unknowns.

Note that we have adapted the names of the variables from $x,y,z$ to $x_1,x_2, x_3$. This notation is more convenient when we come across equations with more than three variables.

::::{prf:definition}
:label: Dfn:LinSystems:LinearEquation

A **linear equation** is an equation that can be written in the form

$$

   a_1x_1 + a_2x_2 + \cdots + a_nx_n = b.
$$

The numbers $a_1,a_2,\ldots,a_n$ are called the **coefficients** and the variables $x_1,x_2, \ldots, x_n$ the **unknowns**. The term $b$ is referred to as the **constant term**.

::::

::::{prf:example}
:label: Ex:LinSystems:LinearEquation

The equation

$$

    3x_1 + 5x_2 = 4x_3 - 2x_4 + 10
$$

is a linear equation, as it can be rewritten as

$$

    3x_1 + 5x_2 - 4x_3 + 2x_4 = 10.
$$

By contrast, the equation

$$

  x_1 + 2x_1x_2 - 3x_2 = 5
$$

is not linear because of the nonlinear term $2x_1x_2$.

::::

::::{prf:definition}
:label: Dfn:LinSystems:LinearSystem

A set of one or more linear equations is called a **system of linear equations** (or **linear system**, for short). In the case of $m$ linear equations in the variables $x_1,x_2,\ldots, x_n$ we speak of a **system of $m$ equations in $n$ unknowns**.
The most general system then looks as follows:

$$

   \left\{\begin{array}{ccccccccc}
            a_{11}x_1\! & \!+\!&\!a_{12}x_2\! & \!+\!&\! \cdots\! & \!+\!&\!a_{1n}x_n  \! & \!=\!&\!  b_1 \\
            a_{21}x_1 \! & \!+\!&\!a_{22}x_2\! & \!+\!&\!\cdots\! & \!+\!&\!a_{2n}x_n  \! & \!=\!&\! b_2 \\
            \vdots \! & \! \!&\!  \vdots\! & \! \!&\!\cdots\! & \! \!&\! \vdots     \! & \! \!&\!  \vdots \\
            a_{m1}x_1 \! & \!+\!&\!a_{m2}x_2\! & \!+\!&\! \cdots\! & \!+\!&\!a_{mn}x_n \! & \!=\!&\! b_m \\
          \end{array}
   \right.
$$

::::

Of course, if we have equations we want to solve them. Here is what we mean by that in a precise way.

::::{prf:definition}
:label: Dfn:LinSystems:SolutionOfLinearSystem

A **solution** of a linear system is an ordered list of $n$ values $(c_1,  c_2, \ldots, c_n)$, or, depending on the context, a vector $\begin{bmatrix}c_1 \\ c_2 \\ \vdots \\ c_n  \end{bmatrix}$, such that substitution of

$$
 x_1 = c_1, \,\, x_2 = c_2, \, \ldots\, , \,\, x_n = c_n
$$

into each of the equations yields true identities.

The **solution set** or **general solution** of a system is the set of all solutions.

::::

::::{prf:example}
:label: Ex:LinSystems:SolutionOfLinearSystem

Two solutions for the system of equations

$$

   \left\{\begin{array}{ccccccc}
      2x_1&+&3x_2&+&  x_3&=&0\\
      3x_1&+& x_2&+& 5x_3&=&7\\
   \end{array}\right.
$$

are given by

$$
  (1, -1, 1)    \quad \text{and} \quad (5, -3, -1)
$$

or, equivalently, by

$$
\begin{bmatrix} 1\\-1\\1 \end{bmatrix}    \quad \text{and} \quad \begin{bmatrix} 5\\-3\\-1 \end{bmatrix}.
$$

For instance, substitution of the second proposed solution yields

$$

  \left\{\begin{array}{ccccccc}
    2\cdot 5&+&3\cdot(-3)&+&  (-1)&=&0\\
    3\cdot 5&+& (-3)&+& 5\cdot(-1)&=&7\\
  \end{array}\right.
$$

which are both true identities.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8159aed6-a915-4cc1-bf75-f243702de530?id=83000
:label: grasple_exercise_2_1_A
:dropdown:
:description: To check whether a vector is a solution of a linear system.

::::

The solution set may be empty, as in the following example.

::::{prf:example}
:label: Ex:LinSystems:EmptySolutionSet

The system

$$

   \left\{\begin{array}{ccccccc}
    2x_1&+&3x_2&+&  x_3&=&5\\
    3x_1&+& x_2&+& 4x_3&=&7\\
    4x_1&+& 6x_2&+& 2x_3&=&8\\
    \end{array}\right.
$$

has no solutions because the first equation conflicts with the third equation:
if $(c_1,c_2,c_3)$ is a triple that satisfies

$$

  2c_1 + 3c_2 + c_3 = 5
$$

then automatically

$$

  4c_1 + 6c_2 + 2c_3 = 2(2c_1 + 3c_2 + c_3) = 10 \neq 8,
$$

so $(c_1,c_2,c_3)$ cannot also be a solution of the third equation.

::::

If the solution set of a linear system is empty, a system is said to be inconsistent.
This concept and its opposite are sufficiently important to be properly defined.

::::{prf:definition}
:label: Dfn:LinSystems:Consistent

A system of linear equations is **consistent** if it has at least one solution. Otherwise it is called **inconsistent**.

::::

::::{prf:example}
:label: Ex:LinSystems:InconsistentEquation

The simplest inconsistent system may well be the system with the one equation

$$

   0x_1 + 0x_2 + \,\cdots\, + 0x_n = 1
$$

As we will see later, this conflicting equation in a way pops up in any inconsistent system.

::::

A consistent system of one equation in $n$ unknowns is easily solved.
Any unknown with a nonzero coefficient can be expressed in the other unknowns,
and the other unknowns can be chosen freely. In words this may look more complicated than it is, as the following example illustrates.

::::{prf:example}
:label: Ex:LinSystems:SystemOfOneEquation

Find all solutions of the equation in the variables $x_1,\ldots,x_5$.

$$

  x_1 + 4x_2 + 5x_3 + 0x_4 - x_5 = 7
$$

One way to denote the set of solutions:

$$

 \left\{\begin{array}{l}
        x_1 = 7 - 4x_2 -5x_3 + x_5 \\
        x_2, x_3, x_4 \text{ and  }  x_5  \text{  are free}
        \end{array}
 \right.
$$

By this we mean: if we assign arbitrary values to the variables $x_2, x_3, x_4$ and $x_5$, say

$$

  x_2 = c_1,\,\, x_3 = c_2, \,\, x_4 = c_3, \,\, x_5 = c_4,
$$

and put

$$

  x_1 = 7 - 4c_1 -5c_2 + c_4
$$

then

$$

 x_1 + 4x_2 + 5x_3 - x_5 = (7 - 4c_1 -5c_2 + c_4) +
   4c_1 +5c_2 - c_4 = 7
$$

so

$$

  (7 - 4c_1 -5c_2 + c_4, \,c_1, \,c_2,\,c_3, \,c_4)
$$

is indeed a solution of the given equation.

However, this is not the only way to write down the general solution: in this example almost any set of four variables can act as free variables. The descriptions

$$

  \left\{\begin{array}{l}
        x_5 = -7 +x_1 +4x_2 +5x_3  \\
        x_1, x_2, x_3 \text{ and  } x_4  \text{  are free}
        \end{array}
 \right.
$$

and

$$

     \left\{\begin{array}{l}
        x_2 = \frac74 - \frac14x_1 -\frac54x_3+\frac14x_5  \\
        x_1, x_3, x_4 \text{ and  } x_5  \text{  are free}
      \end{array}
    \right.
$$

are just as good. You might want to avoid fractions though. The only set of four variables that cannot act as free variables is the set $\{x_1,x_2,x_3,x_5\}$.

::::

The idea behind all methods to find the general solution of a linear system: rewrite the system in simpler forms, basically by eliminating variables from equations.
We illustrate this by an example.

::::{prf:example}
:label: Ex:LinSystems:SolWithBacksubst1

We solve the system

$$

   \left\{\begin{array}{ccccc}
    2x_1&-&5x_2&=&-2\\
    4x_1&-&7x_2&=& 2.
    \end{array}\right.
$$

**First method**: from the first equation it follows that

$$
  2x_1 = -2 + 5x_2.
$$

From this it follows that

$$
   x_1 = -1 + \tfrac52 x_2.
$$

Substitution of the expression for $x_1$ into the second equation yields

$$

  4(-1 + \tfrac52 x_2) - 7x_2 = 2,
$$

an equation with $x_2$ as single unknown (the jargon: $x_1$ has been eliminated), and then

$$

  -4 +10x_2 - 7x_2 = 2 \iff 3x_2 = 6 \iff x_2 = 2,
$$

and finally

$$

  x_1 = -1 + \tfrac52 x_2 = -1 + \tfrac52\cdot2 = 4.
$$

Thus we have found that there is a unique solution:

$$

    \left\{\begin{array}{l} x_1 = 4 \\ x_2 = 2. \end{array} \right.
$$

There is nothing wrong with this method, but with more than two equations it has the tendency to become messy.

**Second method**: take clever combinations of the equations to eliminate variables. For the above example we may for instance subtract the first equation twice from the second. Think a moment why this is okay. It is the crucial step in the elimination method we will explain in the next subsection.

$$

   \left\{\begin{array}{ccccc}
        2x_1&-&5x_2&=&-2\\
        4x_1&-&7x_2&=& 2
    \end{array}\right.\quad\Longrightarrow\quad
     \left\{\begin{array}{ccccc}
        2x_1&-&5x_2&=&-2\\
            & &3x_2&=& 6
    \end{array}\right.
$$

Again we see that $x_2 = 2$, in fact the equation $3x_2 = 6$ is the same equation that we arrived at with the substitution method above. Substitution of this into the first equation again yields

$$

   2x_1 - 5\cdot2 = -2 \quad \iff \quad x_1 = 4.
$$

::::

(Subsec:LinSystems:Elimination)=

## Solving a Linear System by Elimination

We start with an example of three equations in three unknowns.

::::{prf:example}
:label: Ex:LinSystems:EliminationFirst

$$

   \left\{\begin{array}{ccccccc}
             x_1 &+&  3x_2 &-&  2x_3 &=&  4 \\
            3x_1 &+&  7x_2 &-&  2x_3 &=&  8 \\
            2x_1 &+& 10x_2 &-&  9x_3 &=& 4.
          \end{array}
   \right.
$$

We can simplify this system by successively eliminating unknowns from equations by combining equations in a clever way. We can for instance eliminate the variable $x_1$ from the second equation by subtracting the first equation three times from the second equation. Likewise we can subtract the first equation twice from the third equation:

$$

  \left\{\begin{array}{ccccccc}
             x_1 &+&  3x_2 &-&  2x_3 &=&  4 \\
            3x_1 &+&  7x_2 &-&  2x_3 &=&  8 \\
            2x_1 &+& 10x_2 &-&  9x_3 &=& 4
          \end{array}
   \right.   \quad \Longrightarrow \quad
   \left\{\begin{array}{ccccccccccccc}
             x_1 &+&  3x_2 &-&  2x_3 &=&  4 \\
                 & & -2x_2 &+&  4x_3 &=&  -4 \\
                 & &  4x_2 &-&  5x_3 &=& -4
          \end{array}
   \right.
$$

With the arrow we express that if we have a solution of the system on the left, this will also be a solution of the system on the right.

Now, why is this okay, why is it allowed to 'subtract equations'? Let us introduce the shorthand notation

$$

 L_1 = x_1  +3x_2 -  2x_3, \quad L_2 = 3x_1 +7 x_2  -2x_3, 
$$

for the expressions on the left sides of the first two equations.
Then the given equations are:

$$

   L_1 = 4, \quad L_2 = 8.
$$

It then follows that we must have

$$

  L_2 - 3L_1 = 8 - 3\cdot4 = -4
$$

which yields

$$

   3x_1 +7 x_2  -2x_3 - 3(x_1  +3x_2 -  2x_3) = -4    \iff   -2 x_2  +4x_3 =  -4.
$$

The last equation is exactly the second equation of the second system.

The crucial thing to note is that these operations can be undone.  If in the second system the first equation is added three times to the second equation and added twice to the third equation we end up with the original system. So in fact we have

$$

   \left\{\begin{array}{ccccccccccccc}
             x_1 &+&  3x_2 &-&  2x_3 &=&  4 \\
                 & & -2x_2 &+&  4x_3 &=&  -4 \\
                 & &  4x_2 &-&  5x_3 &=& -4
          \end{array}
   \right.    \quad \Longrightarrow \quad
   \left\{\begin{array}{ccccccc}
             x_1 &+&  3x_2 &-&  2x_3 &=&  4 \\
            3x_1 &+&  7x_2 &-&  2x_3 &=&  8 \\
            2x_1 &+& 10x_2 &-&  9x_3 &=& 4
          \end{array}
   \right.
$$

The implication works two ways, which we can write as follows.

$$

   \left\{\begin{array}{ccccccc}
             x_1 &+&  3x_2 &-&  2x_3 &=&  4 \\
            3x_1 &+&  7x_2 &-&  2x_3 &=&  8 \\
            2x_1 &+& 10x_2 &-&  9x_3 &=& 4
          \end{array}
   \right.  \quad \Longleftrightarrow \quad
   \left\{\begin{array}{ccccccccccccc}
             x_1 &+&  3x_2 &-&  2x_3 &=&  4 \\
                 & & -2x_2 &+&  4x_3 &=&  -4 \\
                 & &  4x_2 &-&  5x_3 &=& -4
          \end{array}
   \right.
$$

So any triple of values $(c_1,c_2,c_3)$ that satisfies the first system satisfies the second system and vice versa. Systems that have the same set of solutions are called equivalent.

::::

::::{prf:definition}
:label: Dfn:LinSystems:EquivalentSystems

Two systems of linear equations are called **equivalent** if they have the same set of solutions.

::::

By the same line of reasoning as in the above example we can deduce that adding an arbitrary multiple of any equation to another equation does not change the solution set of the system.
Of course if we multiply an equation with some nonzero constant, the solution set also remains invariant. This operation is called **scaling**.
For the system at hand we could, as a next step, scale the second equation with a factor $-\frac12$. The following proposition summarizes the suitable operations to adapt a system of equations.

::::{prf:proposition}
:label: Prop:LinSystems:ElimOperations

The following operations applied to a linear system always yield an equivalent system

<ul>
<li>

Adding a multiple of an equation to another equation.

</li>
<li>

Scaling an equation with a nonzero scaling factor $c$.

</li>
<li>

Changing the order of the equations.

</li>
</ul>

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:LinSystems:ElimOperations`
:class: tudproof

The correctness of the first operation is illustrated in
{prf:ref}`Ex:LinSystems:EliminationFirst`. One example is by far not a proof, but the explanation given there can be generalized/formalized.  
The other two statements are rather obvious.

::::

::::{prf:example}
:label: Ex:LinSystems:I

We take up {prf:ref}`Ex:LinSystems:EliminationFirst` at the point where we left it and work our way to its solution.
Also we will introduce a notation that makes it easier for the reader to see what's going on. And also for yourself, in case you look back at your computations later, e.g., if you want to check your computations. The '$E$' stands for: 'Equation'.

We scale the second equation with a factor $-\frac12$

$$
 \left\{\begin{array}{cccccccccccccccccccccc}
             x_1 &+&  3x_2 &-&  2x_3 &=&  4  & \quad[E_1]\\
                 & & -2x_2 &+&  4x_3 &=&  -4 & \quad[-\frac12E_2]\\
                 & &  4x_2 &-&  5x_3 &=& -4  &\quad[E_3]
          \end{array}
   \right.    \quad \Longleftrightarrow \quad
  \left\{\begin{array}{ccccccccccccc}
             x_1 &+&  3x_2 &-&  2x_3 &=&  4 \\
                 & &   x_2 &-&  2x_3 &=&  2 \\
                 & &  4x_2 &-&  5x_3 &=& -4
          \end{array}
   \right.
$$

and then subtract the second equation four times from the third:

$$

   \left\{\begin{array}{cccccccccccccccccccccc}
             x_1 &+&  3x_2 &-&  2x_3 &=&  4 & \quad[E_1]\\
                 & &   x_2 &-&  2x_3 &=&  2 & \quad[E_2]\\
                 & &  4x_2 &-&  5x_3 &=& -4 & \quad[E_3-4 E_2]
          \end{array}
   \right.
    \quad \Longleftrightarrow \quad
     \left\{\begin{array}{ccccccccccccc}
             x_1 &+&  3x_2 &-&  2x_3 &=&  4 \\
                 & &   x_2 &-&  2x_3 &=&  2 \\
                 & &       & &  3x_3 &=& -12
          \end{array}
   \right.
$$

From the third equation it follows that

$$

  x_3 = \dfrac{-12}{3} = -4,
$$

and then we can work upwards to find that

$$
x_2 = 2 + 2x_3 = 2+2\cdot(-4) = -6
$$

and finally from the first equation it follows that

$$

    x_1 = 4 - 3x_2 + 2x_3 = 4 - 3\cdot(-6) + 2\cdot(-4) = 14.
$$

Conclusion: the system has the unique solution

$$

   (x_1,x_2,x_3) = (14,-6,-4).
$$

Problem solved.

The last few steps, working our way up from the last equation to successively find $x_3$, $x_2$, $x_1$, is referred to as **backward substitution**.

::::

::::{prf:example}
:label: Ex:LinSystems:Inconsistent3x3

Consider the following system of equations

$$

   \left\{\begin{array}{ccccccc}
              x_1 &+&  4x_2 &-&  5x_3 &=&  4 \\
             2x_1 &+&  7x_2 &-&  2x_3 &=&  9 \\
              x_1 &+&  3x_2 &+&  3x_3 &=&  6
          \end{array}
   \right.
$$

Making use of the notation introduced in the previous example we simplify the system:

$$

  \left\{\begin{array}{cccccccc}
              x_1 &+&  4x_2 &-&  5x_3 &=&  4 &\quad[E_1]\\
             2x_1 &+&  7x_2 &-&  2x_3 &=&  9 &\quad[E_2-2E_1]\\
              x_1 &+&  3x_2 &+&  3x_3 &=&  6 &\quad[E_3-E_1]
          \end{array}
   \right.
$$

$$

   \iff
    \left\{\begin{array}{cccccccccccccccccccccc}
              x_1 &+&  4x_2 &-&  5x_3 &=&  4 &\quad[E_1] \\
                  & &  -x_2 &+&  8x_3 &=&  1 &\quad[E_2]\\
                  & &  -x_2 &+&  8x_3 &=&  2 &\quad[E_3-E_2]
          \end{array}
   \right.
$$

$$

   \iff
    \left\{\begin{array}{ccccccccccccc}
              x_1 &+&  4x_2 &-&  5x_3 &=&  4  \\
                  & &  -x_2 &+&  8x_3 &=&  1 \\
                  & &       & &     0 &=&  1.
          \end{array}
   \right.
$$

From the last equation it immediately follows that there are no solutions, in other words, the system is *inconsistent*.

::::

Let us look at one more example. Here we will see how to find a solution that contains a free variable.

::::{prf:example}
:label: Ex:LinSystems:SolWithBacksubst2

We find the general solution of the linear system

$$

   \left\{\begin{array}{ccccccccc}
     4x_1&-&2x_2&-& 3x_3&+&7x_4&=&5\\
     3x_1&-&x_2&-& 2x_3&+&5x_4&=&7\\
     x_1&-&x_2&-& 2x_3&+&3x_4&=&3.
    \end{array}\right.
$$

Using the shorthand notation just introduced the system can be simplified as follows:
we first interchange the first and the third equation to have a first equation where the coefficient of $x_1$ is equal to 1. That way we avoid fractions in at least the first elimination step.

$$
\begin{array}{cl}
        &
         \left\{\begin{array}{cccccccccc}
     4x_1&-&2x_2&-& 3x_3&+&7x_4&=&5&\quad[E_3]\\
     3x_1&-&x_2&-& 2x_3&+&5x_4&=&7&\quad[E_2]\\
     x_1&-&x_2&-& 2x_3&+&3x_4&=&3&\quad[E_1]
    \end{array}\right.\\\iff &
   \left\{\begin{array}{cccccccccc}
      x_1&-&x_2&-& 2x_3&+&3x_4&=&3&\quad[E_1]\\
     3x_1&-&x_2&-& 2x_3&+&5x_4&=&7&\quad[E_2-3E_1]\\
      4x_1&-&2x_2&-& 3x_3&+&7x_4&=&5&\quad[E_3-4E_1]
    \end{array}\right.    \\
   \iff &
   \left\{\begin{array}{cccccccccccccccccccccccccccc}
      x_1&-&x_2&-& 2x_3&+&3x_4&=&3&\quad[E_1]\\
      &&2x_2&+& 4x_3&-&4x_4&=&-2&\quad[\frac12E_2]\\
       &&2x_2&+& 5x_3&-&5x_4&=&-7&\quad[E_3]
    \end{array}\right.
     \\
   \iff &
   \left\{\begin{array}{cccccccccccccccccccccccccccc}
      x_1&-&x_2&-& 2x_3&+&3x_4&=&3&\quad[E_1]\\
      &&x_2&+& 2x_3&-&2x_4&=&-1&\quad[E_2]\\
       &&2x_2&+& 5x_3&-&5x_4&=&-7&\quad[E_3-2E_2]
    \end{array}\right.    \\
   \iff &
   \left\{\begin{array}{ccccccccccccccccc}
      x_1&-&x_2&-& 2x_3&+&3x_4&=&3\\
      &&x_2&+& 2x_3&-&2x_4&=&-1\\
       && && x_3&-&x_4&=&-5.
    \end{array}\right.\end{array}
$$

Again we can find the solution by back-substitution:

the third equation can be rewritten as

$$

  x_3 = -5 + x_4.
$$

Via the second equation we can express $x_2$ as a function of $x_4$

$$

  x_2 + 2(-5+x_4) -2x_4 = -1 \quad \iff \quad
  x_2 = 9
$$

And then it follows from the first equation that

$$

 x_1 - 9 - 2\cdot(-5+x_4) + 3x_4 = 3 \quad \iff \quad
 x_1 = 2 -x_4
$$

So the solution can be written as

$$

  \left\{\begin{array}{l}
       x_1 = 2 -x_4 \\
       x_2 = 9 \\
       x_3 = -5 + x_4\\
       x_4 \text{  is free}
    \end{array}\right.
$$

Note that the row swap that we used as a first step is not really necessary. However, this way we avoided having to work with non-integer multiples of rows.

::::

We summarize the elimination method in a

::::{admonition} Summary
:class: remark
:name: Summ:LinSystems:EliminationMethod

Any linear system in the variables $x_1,\ldots, x_n$ can be solved as follows:

<ul>
<li>

Using the operations of {prf:ref}`Prop:LinSystems:ElimOperations` the system can be simplified to an equivalent linear system with the following property: in each equation at least one more of the first unknowns has a coefficient 0 than in the previous equation. If an unknown has a coefficient 0 we say that the unknown has been **eliminated**.

</li>
<li>

If an equation

$$

  0x_1 + 0x_2 + \cdots + 0x_n = b,
$$

with $b\neq 0$ pops up, the system is inconsistent.

</li>
<li>

If no such equation appears, the general solution can be found by backward substitution: starting from the last equation, we work our way upwards.

</li>
</ul>

::::

In theory the method works for any linear system, however large, though with pen and paper it soon becomes cumbersome. In the next subsection we will use an appropriate representation of a linear system to solve it in a more efficient way. And we will also see how the procedure of back-substitution can be incorporated in the elimination process.

(Subsec:LinSystems:AugmentedMatrix)=

## Augmented Matrices

We will introduce a convenient shorthand notation for linear systems. This notation contains the essentials of the system in a structured way.

Before that, we define the concept of one of the most basic building blocks in linear algebra: the matrix.

::::{prf:definition}
:label: Dfn:LinSystems:Matrix

An $m \times n$ **matrix** $A$ is a rectangular array of numbers $a_{ij}$, $1\leq i \leq m$, $1 \leq j \leq n$.

$$
   A = \left[\begin{array}{cccc}
            a_{11} & a_{12}&  \ldots&   a_{1n}   \\
            a_{21} & a_{22}&  \ldots&   a_{2n}   \\
            \vdots &  \vdots&  \cdots&  \vdots    \\
            a_{m1} & a_{m2}&  \ldots&   a_{mn}
          \end{array}
   \right].
$$

It consists of $m$ horizontal **rows** of size $n$, or, equivalently, of $n$ vertical **columns** of size $m$.

::::

In a statement about a matrix the first index always refers to the row(s), the second index to the column(s).
E.g., $a_{ij}$ is the number in the $i$-th row and the $j$-th column and an $m \times n$ matrix has $m$ rows and $n$ columns.

A matrix is usually surrounded by parentheses or (square) brackets. We opt for brackets.

::::{prf:example}
:label: Ex:LinSystems:FirstMatrix

The matrix

$$
B = \left[  \begin{array}{ccccc}
        1 & 2 & 3 & 4 & 5 \\
        2 & 7 & -1 & 0 & 8 \\
        5 & 5 & 5 & 0 & 4
    \end{array}\right]
$$

is a $3\times 5$ matrix.

Its second row is $\begin{bmatrix} 2 & 7 & -1 & 0 & 8  \end{bmatrix}$ and its third column is 
$
\left[  \begin{array}{c} 3 \\ -1 \\ 5   \end{array}\right].
$

::::

Matrices play an important role in linear algebra. In this section we will use them as concise representations of linear systems, in which
the computations involved to solve a system can be done quite systematically.

::::{prf:definition}
:label: Dfn:LinSystems:AugmentedMatrix

The **augmented matrix** for a system of equations

$$
   \left\{\begin{array}{ccccccccc}
            a_{11}x_1\! & \!+\!&\!a_{12}x_2\! & \!+\!&\! \ldots\! & \!+\!&\!a_{1n}x_n  \! & \!=\!&\!  b_1 \\
            a_{21}x_1 \! & \!+\!&\!a_{22}x_2\! & \!+\!&\!\ldots\! & \!+\!&\!a_{2n}x_n  \! & \!=\!&\! b_2 \\
            \vdots \! & \! \!&\!  \vdots\! & \! \!&\!\cdots\! & \! \!&\! \vdots     \! & \! \!&\!  \vdots \\
            a_{m1}x_1 \! & \!+\!&\!a_{m2}x_2\! & \!+\!&\! \ldots\! & \!+\!&\!a_{mn}x_n \! & \!=\!&\! b_m \\
          \end{array}
   \right.
$$

is the matrix

$$
   \left[    \begin{array}{cccc|c}
            a_{11} & a_{12}&  \ldots&   a_{1n}    &  b_1 \\
            a_{21} & a_{22}&  \ldots&   a_{2n}   &  b_2 \\
            \vdots &  \vdots&  \ldots&  \vdots    &  \vdots \\
            a_{m1} & a_{m2}&  \ldots&   a_{mn}    &  b_m
          \end{array}
   \right].
$$

The part before the vertical bar, i.e.

$$
    A =  \left[      \begin{array}{cccc}
            a_{11} & a_{12}&  \ldots&   a_{1n} \\
            a_{21} & a_{22}&  \ldots&   a_{2n} \\
            \vdots &  \vdots&  \ldots&  \vdots    \\
            a_{m1} & a_{m2}&  \ldots&   a_{mn}
          \end{array}
   \right]
$$

is called the **coefficient matrix** of the system. The column behind the bar contains the constant terms.

::::

The augmented matrix is nothing more than an abbreviation for a system of equations. With the vertical bar we want to indicate that the last column plays a special role, namely, it contains the constants on the right  sides of the equations. If we denote these terms by the vector

$$
  \mathbf{b} =  \left[\begin{array}{c}
                b_1\\b_2\\\vdots\\b_m
          \end{array}
   \right]
$$

the augmented matrix can be written as

$$
  [ A | \mathbf{b} ].
$$

To conclude this subsection we will reconsider the earlier example of a system of three equations in three unknowns

$$
    \left\{\begin{array}{ccccccc}
             x_1 & + & 3x_2 & -&2x_3 &=&  4 \\
            3x_1 & + & 7x_2 & -&2x_3 &=&  8 \\
            2x_1 & + &10x_2 & -&9x_3 &=& 4.
          \end{array}
   \right.
$$

We will apply the same simplifications to the system as before. Parallel to this we adapt the augmented matrix accordingly, using a notation that speaks for itself.  $R$ stands for 'row'.

$$
 \begin{array}{lcl}
  \left\{\begin{array}{ccccccc}
             x_1 & + & 3x_2 & -&2x_3 &=&  4 \\
            3x_1 & + & 7x_2 & -&2x_3 &=&  8 \\
            2x_1 & + &10x_2 & -&9x_3 &=& 4
          \end{array}
   \right.&\qquad&
\left[\begin{array}{rrr|r}1 &  3 & -2& 4\\3 &  7 & -2&  8\\2 & 10 & -9 & 4
\end{array}\right]\begin{array}{l}
{[R_1]} \\
{[R_2-3R_1]} \\
{[R_3-2R_1]} \\
\end{array} \\
    & {\Big\Updownarrow} & \\
   \left\{\begin{array}{ccccccccccccc}
             x_1 & + & 3x_2 & -&2x_3 &=&  4 \\
                 & - & 2x_2 & +&4x_3 &=&  -4 \\
                 &   &4x_2 & -&5x_3 &=& -4
          \end{array}
   \right.&\qquad&
\left[\begin{array}{rrr|r}1 &  3 & -2& 4\\0& -2 &  4 &  -4\\0 & 4 & -5 & -4
\end{array}\right]\begin{array}{l}
{[R_1]} \\
{[-\frac12R_2]} \\
{[R_3]} \\
\end{array} \\
    & {\Big\Updownarrow} & \\
   \left\{\begin{array}{ccccccccccccc}
             x_1 & + & 3x_2 & -&2x_3 &=&  4 \\
                 &  & x_2 & -&2x_3 &=&  2 \\
                 &   &4x_2 & -&5x_2 &=& -4
          \end{array}
   \right.&\qquad& \left[\begin{array}{rrr|r}1 &  3 & -2& 4\\0& 1 &  -2 &  2\\0 & 4 & -5 & -4
\end{array}\right]\begin{array}{l}
{[R_1]} \\
{[R_2]} \\
{[R_3-4R_2]} \\
\end{array} \\
    & {\Big\Updownarrow} & \\
   \left\{\begin{array}{ccccccccccccc}
             x_1 & + & 3x_2 & -&2x_3 &=&  4 \\
                 &  & x_2 & -&2x_3 &=&  2 \\
                 &   &  & &3x_3 &=& -12
          \end{array}
   \right.&\qquad&
\left[\begin{array}{rrr|r}1 &  3 & -2& 4\\0& 1 &  -2 &  2\\0 & 0 & 3 & -12
\end{array}\right]
\end{array}
$$

As we have seen before, the solution can now be found by backward substitution.

The right moment to start this backward substitution is when the augmented matrix has been simplified to so-called **echelon form**.

(Subsec:LinSystems:RowReduction)=

## Row Reduction and Echelon Forms

In {numref}`Subsec:LinSystems:Elimination` we have solved linear systems by eliminating variables from equations. It would be nice to have a clear mark where we can stop rewriting the given system, to forestall ending up in a never ending loop. When we use the notation of an augmented matrix we can identify such a mark.
We first need a few more definitions.

::::{prf:definition}
:label: Dfn:LinSystems:EchelonForm

A matrix is in **row echelon form** if it has the following two properties:

<ol type ="i">
<li>

All non-zero rows are above all rows that contain only zeros.

</li>
<li>

Each non-zero row that is not the last row starts with fewer zeros than the rows below it.

</li>
</ol>

Such a matrix is also called a **row echelon matrix**.

::::

::::{prf:example}
:label: Ex:LinSystems:EchelonForm

The following three matrices are meant to visualize the structure of an echelon matrix.
The symbol $\blacksquare$ denotes an arbitrary *nonzero* number and $\ast$ just any real number.

$$
  E_1 =
\begin{bmatrix} \blacksquare & \ast & \ast &  \ast \\
                         0  & \blacksquare & \ast & \ast \\
                         0  &  0 &\blacksquare &  \ast \\
                         0  & 0 & 0 &  0 \\
                         0  & 0 & 0 &  0  \end{bmatrix} ,
                   \quad
  E_2 =
\begin{bmatrix} \blacksquare & \ast & \ast & \ast & \ast \\
                         0  & 0 & \blacksquare &  \ast & \ast \\
                         0  & 0 & 0 &0 & \blacksquare  \end{bmatrix},
                         \quad
  E_3 =
\begin{bmatrix} \blacksquare & \ast &  \ast & \ast \\
                         0  & \blacksquare & \ast & \ast \\
                         0  & 0 & \blacksquare &   \ast \\
                         0  & 0 & 0  & \blacksquare  \\
                         0  & 0  &0  & 0  \end{bmatrix}
$$

::::

In a similar manner we can define the concept of a **column echelon matrix**.
However, since we will only consider row echelon matrices we will not do this. In the sequel we will drop the epithet 'row' and simply speak of echelon form and echelon matrix.

::::{prf:definition}
:label: Dfn:LinSystems:Pivot

A **pivot** of a row in an echelon matrix is the first nonzero element (the so-called _leading entry_) of that row.

::::

::::{prf:example}
:label: Ex:LinSystems:EchelonMatrices

The following three matrices are in echelon form:

$$
 A_1 = \left[\begin{array}{rrr}1 & 2 & 3 \\ 0 & 3 & 2 \\ 0 & 0 & 0 \end{array}  \right], \quad
 A_2 = \left[\begin{array}{rr}1 & 0 \\ 0 & 1 \\ 0 & 0 \\ 0 & 0 \end{array}  \right], \quad
 A_3 = \left[\begin{array}{rrrrr}1 & 1 & 0 &  2 &  0\\ 0 & 0 & 1 & 4 & 0\\ 0 & 0 & 0 & 0 & 1\end{array}  \right]
$$

The following two matrices are not in echelon form

$$
 A_4 = \left[\begin{array}{rrr}0 & 0 & 0 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{array}  \right], \quad
 A_5 = \left[\begin{array}{rrr}1 & 0 & 0 \\ 0 & 1 & 1  \\ 0 &1 & 0 \end{array}  \right].
$$

Namely, in matrix $A_4$ the second row is a non-zero row that is below the all-zero first row. And in matrix $A_5$ the third row does not start with _more_ zeros than the second row.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a6512aec-5f2d-4e3c-9c26-a0a22815480e?id=86165
:label: grasple_exercise_2_1_D
:dropdown:
:description: To check whether a matrix is in echelon form.

::::

::::{prf:example}
:label: Ex:LinSystems:PivotsInMatrices

Here are the three echelon matrices again, with boxes around their pivots:

$$
 \left[\begin{array}{rrr}\fbox{1} & 2 & 3 \\ 0 & \fbox{3} & 2 \\ 0 & 0 & 0 \end{array}  \right], \quad
 \left[\begin{array}{rr}\fbox{1} & 0 \\ 0 & \fbox{1} \\ 0 & 0 \\ 0 & 0 \end{array}  \right], \quad
 \left[\begin{array}{rrrrr}\fbox{1} & 1 & 0 &  2 &  0\\ 0 & 0 & \fbox{1} & 4 & 0\\ 0 & 0 & 0 & 0 & \fbox{1}\end{array}  \right].
$$

The third and the fourth row of the second matrix do not have pivots.

::::

::::{prf:remark}

In practice the pivots are the coefficients in the equations of a system that are used to eliminate variables from other equations. In the context of augmented matrices: they are the entries used to create zeros in the column below that entry.

Note that from the second condition in {prf:ref}`Dfn:LinSystems:EchelonForm` it follows that automatically all entries in the column below a pivot must be 0.

::::

Now have a look again at the derivation at the end of the previous subsection. We worked our way downwards through the rows to create zeros in the first columns, while keeping in mind that we did not change the solution set of the corresponding linear system. The process is called **row reduction**. The end point, from which we could start building the solution by backward substitution, was an augmented matrix in echelon form!

::::{prf:definition}
:label: Dfn:LinSystems:RowOperations

The **elementary row operations** that one can apply to a matrix are

<ol type ="i">
<li>

Adding a multiple of a row to another row.

</li>
<li>

Multiplying a row by a non-zero number. This is also referred to as **scaling**.

</li>
<li>

Interchanging (or: swapping) two rows.

</li>
</ol>

::::

::::{prf:remark}

Note that these row operations match exactly the operations of {prf:ref}`Prop:LinSystems:ElimOperations`. This proposition now states that the row operations do not change the solutions of the corresponding linear system.
::::

::::{prf:definition}
:label: Ex:LinSystems:RowEquivalent

Matrices that can be transformed into each other via row operations are called **row equivalent**.
If two matrices $A$ and $B$ are row equivalent we denote this by $A \sim B$.

::::

::::{prf:remark}

If two augmented matrices are row equivalent it means that the linear systems they represent are equivalent (i.e., have the same solution set).

::::

Above we applied row operations to an augmented matrix, to work our way to the solution of a system of equations.
In fact we simplified the system and the matrix along parallel paths. From now on we will simplify a system by working almost always with the corresponding augmented matrix.

In later chapters we will also apply row reduction to matrices in other contexts, i.c. for other purposes.

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/100dee65-a3fa-4747-9806-425aabb199f1?id=86189
:label: grasple_exercise_2_1_B
:dropdown:
:description: To perform row operations on a matrix.

::::

::::{prf:example}
:label: Ex:LinSystems:RowReduction-1

We will row reduce the matrix

$$
M =
\begin{bmatrix}
     4 & -4 & -4 & 8 & 12 \\ -2 & 2 & 2 & -4 & 2 \\ 3 & -3 & -1 & 5 & 4
     \end{bmatrix}
$$

to a matrix $E$ in echelon form:

$$
\begin{array}{ccl}
     M&=&
\left[\begin{array}{rrrrr}
   4 & -4 & -4 & 8 & 12 \\
   -2 & 2 & 2 & -4 & 2 \\
   3 & -3 & -1 & 5 & 4
\end{array}\right]\begin{array}{l}
   {[\frac14R_1]} \\
   {[R_2]} \\
   {[R_3]}
\end{array} \\
    &\sim&
\left[\begin{array}{rrrrr}
   1 & -1 & -1 & 2 & 3 \\
   -2 & 2 & 2 & -4 & 2 \\
   3 & -3 & -1 & 5 & 4
\end{array}\right]\begin{array}{l}
{[R_1]} \\
{[R_2+2R_1]} \\
{[R_3]}
\end{array} \\
    &\sim&
\left[\begin{array}{rrrrr}
   1 & -1 & -1 & 2 & 3 \\
   0 & 0 & 0 & 0 & 8 \\
   3 & -3 & -1 & 5 & 4
\end{array}\right]\begin{array}{l}
   {[R_1]} \\
   {[R_2]} \\
   {[R_3-3R_1]}
\end{array} \\
    &\sim&
\left[\begin{array}{rrrrr}
   1 & -1 & -1 & 2 & 3 \\
   0 & 0 & 0 & 0 & 8 \\
   0 & 0 & 2 & -1 & -5
\end{array}\right]\begin{array}{l}
{[R_1]} \\
{[R_2\leftrightarrow R_3]} \\
{[R_3\leftrightarrow R_2]}
\end{array} \\
  &\sim&
\left[\begin{array}{rrrrr}
   1 & -1 & -1 & 2 & 3 \\
   0 & 0 & 2 & -1 & -5 \\
   0 & 0 & 0 & 0 & 8
\end{array}\right]= E
  \end{array}
$$

Here a row swap was essential to bring the matrix into echelon form. Sometimes a row swap may just be convenient to simplify the computations. Note that we have also introduced a notation for a row swap. We stress again that it is *good practice* to use a notation like this when you do a row reduction process yourself.
To speed up the process it may be preferable to combine row operations that do not interfere. In this example the second and the third step both involved
adding multiples of the first row to the other rows. This can be done simultaneously:

$$
    \begin{array}{ccl}
\left[\begin{array}{rrrrr}1 & -1 & -1 & 2 & 3\\-2 & 2 & 2 & -4 & 2\\3 & -3 & -1 & 5 & 4
\end{array}\right]\begin{array}{l}
[R_1] \\
{[R_2+2R_1]} \\
{[R_3-3R_1]} \\
\end{array}
    &\sim&
\left[\begin{array}{rrrrr}1 & -1 & -1 & 2 & 3\\0 & 0 & 0 & 0 & 8\\0 & 0 & 2 & -1 & -5
\end{array}\right]   \end{array}
$$

::::

::::{prf:proposition}

Any matrix is row equivalent to an echelon matrix.

::::

::::{prf:remark}

We will not give a formal proof.

The idea that a matrix can be reduced to an echelon matrix is as follows: just start from the top left and work downwards.

If $a_{11}$ is not 0, that will be the first pivot. We can use it to make all the other elements in the first column 0.

We then get

$$
    A =  \left[\begin{array}{cccc}
            a_{11} & a_{12}&  \ldots&   a_{1n} \\
            a_{21} & a_{22}&  \ldots&   a_{2n} \\
            \vdots &  \vdots&  \ldots&  \vdots    \\
            a_{m1} & a_{m2}&  \ldots&   a_{mn}
          \end{array}
   \right]\sim  \left[\begin{array}{cccc}
            a_{11} & a_{12}&  \ldots&   a_{1n} \\
                0  & \tilde{a}_{22}&  \ldots&   \tilde{a}_{2n} \\
            \vdots &  \vdots&  \ldots&  \vdots    \\
            0 & \tilde{a}_{m2}&  \ldots&   \tilde{a}_{mn}
          \end{array}
   \right].
$$

From then on we will leave the first row as it is.

If $a_{11} = 0$, then we try to find a non-zero element in the first column. If this is the element $a_{i1}$, then we can start by interchanging the first and the $i$-th row. After this row swap we use the new first row to create zeros in the first column.

If the first column happens to consist of zeros only, we skip it and start from the first non-zero column.

We continue with the part of the matrix below and to the right of the first pivot, i.e.,

$$
   \left[\begin{array}{cccc}
             \tilde{a}_{22}&  \tilde{a}_{23}&  \ldots&   \tilde{a}_{2n} \\
             \tilde{a}_{32}&   \tilde{a}_{33}& \ldots&   \tilde{a}_{3n} \\
                \vdots     &  \vdots         &  \ldots&  \vdots    \\
           \tilde{a}_{m2}&  \tilde{a}_{m3}&  \ldots&   \tilde{a}_{mn}
          \end{array}
   \right].
$$

And so on, until we get to the last row, or until we get to a row below which all rows only contain zeros.

::::

The echelon matrix to which a matrix can be reduced is in no way unique. For instance, by scaling a row in an echelon matrix the echelon form persists. We can go a bit further, namely we can create zeros in the columns *above* the pivots as well. The following example shows how. First we work downwards to the echelon form and then work upwards to create the extra zeros, as mentioned.

::::{prf:example}
:label: Ex:LinSystems:RowReduction-2

The matrix

$$
   M =
\begin{bmatrix} 1 & 2 & 3 & 1\\ 1 & 4 & 7 & 3\\ 3 & 6 & 11 & 9
       \end{bmatrix}
$$

is row equivalent to all of the following echelon matrices:

$$
\begin{bmatrix} 1 & 2 & 3 & 1\\ 0 & 2 & 4 & 2\\ 0 & 0 & 2 & 6 \end{bmatrix} \sim
\begin{bmatrix} 1 & 2 & 3 & 1\\ 0 & 1 & 2 & 1\\ 0 & 0 & 1 & 3 \end{bmatrix} \sim
\begin{bmatrix} 1 & 2 & 0 & -8\\ 0 & 1 & 0 & -5\\ 0 & 0 & 1 & 3 \end{bmatrix} \sim
\begin{bmatrix} 1 & 0 & 0 & 2\\ 0 & 1 & 0 & -5\\ 0 & 0 & 1 & 3 \end{bmatrix}.
$$

Or, using the notation for the row operations:

$$
\left[\begin{array}{rrrr}1 & 2 & 3 & 1\\1 & 4 & 7 & 3\\3 & 6 & 11 & 9
\end{array}\right]\begin{array}{l}
[R_1] \\
{[R_2-1R_1]} \\
{[R_3-3R_1]} \\
\end{array} \sim
\left[\begin{array}{rrrr}1 & 2 & 3 & 1\\0 & 2 & 4 & 2\\0 & 0 & 2 & 6
\end{array}\right]\begin{array}{l}
[R_1] \\
{[\frac12R_2]} \\
{[\frac12R_3]} \\
\end{array}
    \quad \sim
\left[\begin{array}{rrrr}1 & 2 & 3 & 1\\0 & 1 & 2 & 1\\0 & 0 & 1 & 3
\end{array}\right]\begin{array}{l}
[R_1-3R_3] \\
{[R_2-2R_3]} \\
{[R_3]} \\
\end{array}
$$

$$
 \sim
\left[\begin{array}{rrrr}1 & 2 & 0 & -8\\0 & 1 & 0 & -5\\0 & 0 & 1 & 3
\end{array}\right]\begin{array}{l}
[R_1-2R_2] \\
{[R_2]} \\
{[R_3]} \\
\end{array}
    \sim
\left[\begin{array}{rrrr}1 &0  & 0 & 2\\0 & 1 & 0 & -5\\0 & 0 & 1 & 3
\end{array}\right]
$$

::::

There are three important observations regarding this example.

::::{prf:remark}
:label: Rem:LinSystems:CreatingZeros

Apart from the second step, where two rows were scaled, in each step one pivot was used to make all elements right above and right below it equal to 0. In this way we move forward all the time to a matrix with more and more zeros **in a structured way**.

::::

::::{prf:remark}
:label: Rem:LinSystems:RowReduceEndpoint

The last matrix can really be seen as a natural end point of the reduction process.

<ul>
<li>

The pivots are all 1, the simplest non-zero number.

</li>
<li>

If we try to create more zeros, we can only do so in the fourth column. But then we we will lose one or more of the zeros in the first three columns.

</li>
</ul>

::::

The third remark is the most important one, keeping in mind the goal of this section: solving linear systems.

::::{prf:remark}
:label: Rem:LinSystems:SolutionFromRREF

If the matrix $M$
were actually an augmented matrix for a system, in which we'd better have written

$$
    M = \left[\begin{array}{rrr|r} 1 & 2 & 3 & 1\\ 1 & 4 & 7 & 3\\ 3 & 6 & 11 & 9
       \end{array}\right],
$$

then the linear system corresponding to the final echelon matrix

$$
    \left[\begin{array}{rrr|r} 1 &0  & 0 & 2\\ 0 & 1 & 0 & -5\\ 0 & 0 & 1 & 3
       \end{array}\right]
$$

is given by

$$
 \left\{    \begin{array}{ccccccccc}
          x_1 &     &     &=& 2\\
              & x_2 &     &=&-5\\
              &     & x_3 &=& 3
    \end{array}
   \right.
$$

which is in fact the solution!

::::

This natural end point of the row reduction process has got his own name.

::::{prf:definition}
:label: Dfn:LinSystems:ReducedEchelonMatrix

A **reduced echelon matrix** or matrix **in reduced echelon form** is an echelon matrix with the extra properties

<ol type ="i">
<li>

All pivots are 1.

</li>
<li>

In a column with a pivot all other elements are 0.

</li>
</ol>

::::

::::{prf:example}
:label: Ex:LinSystems:ReducedEchelonMatrix

Of the matrices

$$
\begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 1
   \end{bmatrix}, \quad
\begin{bmatrix} 1 & 0 & 1  \\ 0 & 1 & 2  \\ 0 & 0 & 1  \\ 0 & 0 & 1
   \end{bmatrix}, \quad
\begin{bmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 3 & 0\\ 0 & 0 & 0 & 1  \\ 0 & 0 & 0 &0
   \end{bmatrix},
$$

the first and the third are echelon matrices and only the third is a reduced echelon matrix.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ec78c509-6e28-441b-bace-9d2b24f14d63?id=70366
:label: grasple_exercise_2_1_C
:dropdown:
:description: Checking whether a matrix is in (reduced) echelon form.

::::

The big advantage of reduced echelon matrices, already hinted at in {prf:ref}`Rem:LinSystems:SolutionFromRREF`, is the following:

::::{prf:proposition}
:label: Prop:LinSystems:SolutionFromRREF

If the augmented matrix of a linear system is in reduced echelon from, the solution of the system is found by expressing the variables corresponding to the pivots in terms of the other variables. These other variables can be assigned arbitrary values.

::::

::::{prf:definition}
:label: Dfn:LinSystems:BasicAndFreeVariables

In the solution as constructed according to the previous proposition the pivot variables are called the **basic variables**. The other variables are called **free variables**.

::::

::::{prf:example}
:label: Ex:LinSystems:SolutionFromRREF

We find the solution of the linear system with the following augmented matrix, which is already in row reduced echelon:

$$
\left[\begin{array}{rrrrr|r}1 & 0 & 2 & 0 & 3 & 6\\0 & 1 & -3 & 0 &-4 & 7\\0 & 0 & 0 & 1 & 5 & 8\\\end{array}\right]
$$

We go back to the corresponding system and bring the non-pivot variables $x_3$ and $x_5$ to the right:

$$
  \left\{    \begin{array}{ccccccccccccccccccccc}
          x_1 &   &    &  +& 2x_3&  &     &+&3x_5& =& 6\\
              &   &x_2 &  -& 3x_3&  &     &-& 4x_5&=&7 \\
              &   &    &   &     &  & x_4 &+&5x_5 &=& 8
    \end{array}
   \right.   \quad \iff \quad
   \left\{    \begin{array}{ccccccc}
          x_1 & = &6&-&2x_3 & - &3x_5\\
          x_2 & = &7&+&3x_3 & + &4x_5 \\
          x_4 & = &8& &     & - &5x_5
    \end{array}
   \right.
$$

and we add: '$x_3$ and $x_5$ are free'.

::::

The row reduction of the augmented matrix to echelon form corresponds to the forward substitution as in {prf:ref}`Ex:LinSystems:SolWithBacksubst1` and {prf:ref}`Ex:LinSystems:SolWithBacksubst2`. There we found the solution by backward substitution. When the augmented matrix is reduced to reduced echelon form we have in fact incorporated this backward substitution part and can write down the general solution directly. We think that to solve a system 'with pen and paper', working with the reduced echelon matrix is less error prone. This holds in particular for a system where the solution contains one or more free variables.

::::{prf:theorem}
:label: Thm:LinSystems:RowEquivalentToRREF

Any matrix is row equivalent to a reduced echelon matrix. Moreover, this last matrix is unique.

::::

::::{prf:remark}
:label: Rem:LinSystems:RowEquivalentToRREF

Again we give no formal proof.
In the previous subsection we showed, also informally, that any matrix can be reduced to a matrix in echelon form.

In this echelon matrix we may divide each row by its pivot (first nonzero element).

And lastly 'working upwards' step by step we use each pivot -- which we made equal to 1 -- to create zeros in all positions above it.

(The last two simplifications may be done in reversed order: first use the pivots to create zeros in the positions above them and then scale the rows.)
This reasoning supports the validity of the first statement.
The uniqueness is harder to show in an intuitive way, and it is definitely harder to prove rigorously.

::::

::::{prf:example}
:label: Ex:LinSystems:ReductionToRREF-1

Let us further simplify the echelon matrix

$$
\begin{bmatrix} 3 & 2 &1 &6&-2\\   0 & 2 & -2 &-3 & 1\\  0 & 0 & 0 &3 & 2
   \end{bmatrix}
$$

to reduced echelon form.

step 1: use the pivot in the third row to create zeros above it;

step 2: use the pivot in the second row to create a zero above it;

step 3: scale all rows:

$$
\left[\begin{array}{rrrrr}3 & 2 &1 &6&-2\\0 & 2 & -2 &-3 & 1\\0 & 0 & 0 &3 & 2
\end{array}\right]\begin{array}{l}
[R_1-2R_3] \\
{[R_2+1R_3]} \\
{[R_3]} \\
\end{array} \,\, \sim \,\,
\left[\begin{array}{rrrrr}3 & 2 &1 &0&-6\\0 & 2 & -2 &0 & 3\\0 & 0 & 0 &3 & 2
\end{array}\right]\begin{array}{l}
[R_1-1R_2] \\
{[R_2]} \\
{[R_3]} \\
\end{array}
    \quad
$$

$$
\sim \quad
\left[\begin{array}{rrrrr}3 & 0 &3 &0&-9\\0 & 2 & -2 & 0 & 3\\0 & 0 & 0 &3 & 2
\end{array}\right]\begin{array}{l}
[\nicefrac13R_1] \\
{[\nicefrac{1}{2}R_2]} \\
{[\nicefrac13R_3]} \\
\end{array} \quad
 \sim   \quad
\left[\begin{array}{rrrrr}1 & 0 &1 &0&-3\\0 & 1 & -1 &0 & 3/2\\0 & 0 & 0 &1 & 2/3
\end{array}\right]
$$

::::

Instead of a formal proof of the *uniqueness* of the row reduced echelon form of a matrix, we illustrate this uniqueness with one example.

::::{prf:example}
:label: Ex:LinSystems:ReductionToRREF-2

We will find the row reduced echelon form of the matrix

$$
 M =
\begin{bmatrix} 2 & -1 & -1 & 2\\ 1 & 2 & 4 & 4\\ 4 & -2 & -4 & 6
       \end{bmatrix}
$$

via two different routes.

Route 1: Use the top left entry $a_{11} = 2$ as a first pivot. An auxiliary step, to avoid fractions, is to scale the second row with a factor 2:

$$
\left[\begin{array}{rrrr}2 & -1 & -1 & 2\\1 & 2 & 4 & 4\\4 & -2 & -4 & 6
\end{array}\right]\begin{array}{l}
[R_1] \\
{[2R_2]} \\
{[R_3]} \\
\end{array} \quad\sim
\left[\begin{array}{rrrr}2 & -1 & -1 & 2\\2 & 4 & 8 & 8\\4 & -2 & -4 & 6
\end{array}\right]\begin{array}{l}
[R_1] \\
{[R_2-1R_1]} \\
{[R_3-2R_1]} \\
\end{array}
$$

$$
    \sim
\left[\begin{array}{rrrr}2 & -1 & -1 & 2\\0 & 5 & 9 & 6\\0 & 0 & -2 & 2
\end{array}\right]\begin{array}{l}
[R_1] \\
{[R_2]} \\
{[(-\nicefrac12)R_3]} \\
\end{array} \quad\sim
\left[\begin{array}{rrrr}2 & -1 & -1 & 2\\0 & 5 & 9 & 6\\0 & 0 & 1 & -1
\end{array}\right]\begin{array}{l}
[R_1+1R_3] \\
{[R_2-9R_3]} \\
{[R_3]} \\
\end{array}
$$

$$
    \sim
\left[\begin{array}{rrrr}2 & -1 & 0 & 1\\0 & 5 & 0 & 15\\0 & 0 & 1 & -1
\end{array}\right]\begin{array}{l}
[R_1] \\
{[(\nicefrac15)R_2]} \\
{[R_3]} \\
\end{array} \quad\sim
\left[\begin{array}{rrrr}2 & -1 & 0 & 1\\0 & 1 & 0 & 3\\0 & 0 & 1 & -1
\end{array}\right]\begin{array}{l}
[R_1+1R_2] \\
{[R_2]} \\
{[R_3]} \\
\end{array}
$$

$$
    \sim
\left[\begin{array}{rrrr}2 & 0 & 0 & 4\\0 & 1 & 0 & 3\\0 & 0 & 1 & -1
\end{array}\right]\begin{array}{l}
[(\nicefrac12)R_1] \\
{[R_2]} \\
{[R_3]} \\
\end{array} \quad \sim
\left[\begin{array}{rrrr}1 & 0 & 0 & 2\\0 & 1 & 0 & 3\\0 & 0 & 1 & -1
\end{array}\right].
$$

Alternatively, we may start with a row swap:

$$
\left[\begin{array}{rrrr}2 & -1 & -1 & 2\\1 & 2 & 4 & 4\\4 & -2 & -4 & 6
\end{array}\right]\begin{array}{l}
[R_1\leftrightarrow R_2] \\
{[R_2\leftrightarrow R_1] }\\
[R_3] \\
\end{array} \sim
\left[\begin{array}{rrrr}1 & 2 & 4 & 4\\2 & -1 & -1 & 2\\4 & -2 & -4 & 6
\end{array}\right]\begin{array}{l}
[R_1] \\
{[R_2-2R_1]} \\
{[R_3-4R_1]} \\
\end{array}
$$

$$
    \sim
\left[\begin{array}{rrrr}1 & 2 & 4 & 4\\0 & -5 & -9 & -6\\0 & -10 & -20 & -10
\end{array}\right]\begin{array}{l}
[R_1] \\
{[R_2]} \\
{[(-\nicefrac{1}{10})R_2]} \\
\end{array} \sim
\left[\begin{array}{rrrr}1 & 2 & 4 & 4\\0 & -5 & -9 & -6\\0 & 1 & 2 & 1
\end{array}\right]\begin{array}{l}
[R_1] \\
{[R_2\leftrightarrow R_3]} \\
{[R_3\leftrightarrow R_2]}
\end{array}
$$

$$
    \sim
\left[\begin{array}{rrrr}1 & 2 & 4 & 4\\0 & 1 & 2 & 1\\0 & -5 & -9 & -6
\end{array}\right]\begin{array}{l}
[R_1-2R_2] \\
{[R_2]} \\
{[R_3+5R_2]} \\
\end{array} \sim
\left[\begin{array}{rrrr}1 & 0 & 0 & 2\\0 & 1 & 2 & 1\\0 & 0 & 1 & -1
\end{array}\right]\begin{array}{l}
[R_1] \\
{[R_2-2R_3]} \\
{[R_3]} \\
\end{array}
$$

$$
    \sim
\left[\begin{array}{rrr}1 & 0 & 0 & 2\\0 & 1 & 0 & 3\\0 & 0 & 1 & -1
\end{array}\right],  \rule{19em}{0ex}
$$

the same outcome as before.
::::

The following algorithm summarizes the solution method for a linear system.

::::{prf:algorithm}
:label: Alg:LinSystems:ElimMethod

Elimination method to solve a linear system.

Any system of linear equations can be solved as follows.

<ol type ="i">
<li>

Write down the augmented matrix corresponding to the system.

</li>
<li>

Row reduce the augmented matrix to  echelon form.

</li>
<li>

If there is a pivot in the last column (the column 'behind the bar'), the system is inconsistent.  
End of story.

</li>
<li>

If the last column does not contain a pivot, reduce the augmented matrix further till reduced echelon form.

</li>

<li>
Write down the corresponding system of equations and express the variables in the pivot columns into the other variables (if any). These other variables are free variables.

</li>
</ol>

The word 'elimination' refers to the fact that the zeros that are created in the augmented matrix correspond to the elimination of variables from the equations.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c242961e-d472-49b4-88e0-80cac8c617f9?id=87134
:label: grasple_exercise_2_1_E
:dropdown:
:description: Applying the algorithm to compute a solution of a linear system.

::::

::::{prf:remark} Row reduced echelon matrix versus back-substitution
:label: Rem:LinSystems:RowRedVersusBackSubstitution

We started this section by solving a linear system by reducing it to an equivalent system in echelon form and then use back-substitution. This is still a viable option. The advantage of the method described in {prf:ref}`Alg:LinSystems:ElimMethod` is that it avoids the clutter back-substitution may lead to in the case of free variables.

::::

The following important general statement about the solution set of linear systems has already been lurking in the background all the time.

::::{prf:theorem}
:label: Thm:LinSystems:ZeroOneInfSolutions

A system of linear equations has either zero, or one, or infinitely many solutions. In the case when there is exactly one solution we speak of a **unique** solution.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Thm:LinSystems:ZeroOneInfSolutions`
:class: tudproof

This just depends on the outcome of the elimination method (i.e. {prf:ref}`Alg:LinSystems:ElimMethod`).
If iii. occurs, the number of solutions is zero; if iv. occurs and there are no free variables, there is just one solution. Lastly, if there is at least one free variable, the solution set automatically contains infinitely many solutions.

::::

Note that to answer the question which of the three cases -- zero solutions, a unique solution or infinitely many solutions -- holds, it suffices to reduce the augmented matrix to just any echelon form. From this echelon form it can already be decided whether the system is consistent, and if it is, whether there are free variables.

::::{prf:example}
:label: Ex:LinSystems:ZeroOneInfSolutions-1

We want to find out whether the linear system

$$
    \left\{\begin{array}{ccccccc}
             x_1 & + & 3x_2 & +&x_3 &=&  5 \\
            2x_1 & + &  x_2 & -&x_3 &=&  4 \\
            3x_1 & - &  x_2 & -&3x_2 &=& 3
          \end{array}
   \right.
$$

has zero, exactly one, or infinitely many solutions.

We row reduce the augmented matrix just as far as necessary:

$$
\left[\begin{array}{rrr|r}1 & 3 & 1 &5\\2 & 1 & -1 &4\\3 & -1 & -3 &3
\end{array}\right]\begin{array}{l}
[R_1] \\
[R_2-2R_1] \\
[R_3-3R_1] \\
\end{array} \sim
\left[\begin{array}{rrr|r}1 & 3 & 1 &5\\0 & -5& -3 &-6\\0 & -10 & -6 &-12
\end{array}\right]
\begin{array}{l}
[R_1] \\
{[R_2]} \\
{[R_3-2R_2]} \\
\end{array} \sim
\left[\begin{array}{rrr|r}1 & 3 & 1 &5\\0 & -5& -3 &-6\\0 & 0 & 0 &0
\end{array}\right]


$$

From the echelon matrix at the end we can see that the system is _consistent_ and there will be a _free variable_. We can conclude that the system has infinitely many solutions.

::::

::::{prf:example}
:label: Ex:LinSystems:ZeroOneInfSolutions-2

This example stresses that the conclusion whether a linear system has zero, one or infinitely many solutions, is basically a matter of the **structure** of an echelon matrix that is equivalent to the augmented matrix of the system.  
Suppose the augmented matrices of three linear systems can be row reduced to the following matrices

$$
  E_1 = \left[\begin{array}{rrr|r}\blacksquare&\ast&\ast&\ast\\0  &\blacksquare&\ast&\ast\\0  &  0 &\blacksquare&\ast\\0  & 0 & 0 & 0\\0  & 0 & 0 & 0\\\end{array}\right],
                   \quad
  E_2 =   \left[\begin{array}{rrrr|r}\blacksquare&\ast&\ast&\ast&\ast\\0  &\blacksquare&\ast&\ast&\ast\\0  &  0 & 0 &\blacksquare&\ast\\0  & 0 & 0 &0 & 0\\\end{array}\right],


$$

and

$$
E_3 =   \left[\begin{array}{rrr|r}\blacksquare&\ast&\ast&\ast\\0  &\blacksquare&\ast&\ast\\0  & 0 &\blacksquare&\ast\\0  & 0 & 0 &\blacksquare\\0  & 0  &0 & 0\\\end{array}\right],
$$

where $\blacksquare$ denotes an arbitrary nonzero number, and $\ast$ just any real number.

Then the first system has a unique solution, the second system has infinitely many solutions, the third system is inconsistent.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/fdf71712-2d0a-4bf2-bfb5-cdcac02f55df?id=70143
:label: grasple_exercise_2_1_F
:dropdown:
:description: Conclusions about the solutions from the structure of the echelon form.

::::

%::::{exercise}
%:label: Exc:LinSystems:Check(In)Consistency
%
%Explain why.
%
%::::

::::{prf:proposition}
:label: Prop:LinSystems:UniqueSolutionImpliesSize

A linear system of $m$ equations in $n$ unknowns can only have a unique solution if $m \geq n$, i.e. if the number of unknowns is at most equal to the number of equations.

::::

::::{admonition} Proof of&nbsp;{prf:ref}`Prop:LinSystems:UniqueSolutionImpliesSize`
:class: tudproof

Let

$$
[A |\mathbf{b}]
$$

be the augmented matrix of the system, and

$$
 [E |\mathbf{c}]
$$

an equivalent echelon matrix. Here $E$ is an $m\times n$ echelon matrix. Since the pivots are in different rows, there are at most $m$ pivots.

If $m < n$, there must be at least one column without a pivot. This implies that either the system is inconsistent (zero solutions) or the system has a solution with at least one free variable (infinitely many solutions). And we have shown that a unique solution is **impossible** for a system of $m$ equations in $n$ unknowns with $m < n$.

::::

::::{prf:remark}
:label: Rem:LinSystems:PlanesInSpace

For geometric interpretation of the last proposition, suppose $n = 3$. <BR>
The solution set of a linear equation

$$
 a_1x_1 + a_2x_2 + a_3x_3 = b
$$

can be seen as a plane in $\mathbb{R}^3$. The previous proposition tells us that the intersection of $m$ planes in $\mathbb{R}^3$, where $m < 3$, cannot be a single point.

::::

## Grasple Exercises

The first exercises are quite straightfordwardly computational.
The remaining exercises tend to be a bit more theoretic.

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c8dee65d-a165-4534-89ee-76967d660c9c?id=69544
:label: grasple_exercise_2_1_1
:dropdown:
:description: Solving a linear system of 2 equations in 2 unknowns.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/4bd179e9-99a6-436a-a178-9ad77210f86b?id=71057
:label: grasple_exercise_2_1_1B
:dropdown:
:description: To determine the number of sulutions of a $2\times 2$ linear system.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9bb8381d-f1a2-4e58-8928-4985cce492c4?id=76019
:label: grasple_exercise_2_1_2
:dropdown:
:description: Identifying the size of a linear system.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/42f38f80-f854-469d-b1e6-893539fd3572?id=82676
:label: grasple_exercise_2_1_3
:dropdown:
:description: $3 \times 3$ linear system 'in triangular form'.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/0d23f4f3-5798-4a7a-b40e-f163f7e2b37f?id=82667
:label: grasple_exercise_2_1_4
:dropdown:
:description: To solve a $3 \times 3$ linear system.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/99536b94-713b-4bae-874c-62958af0f5fe?id=80875
:label: grasple_exercise_2_1_5
:dropdown:
:description: To solve a $3 \times 4$ linear system.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ff8bfe99-7a87-4711-b589-7ba70a857a39?id=80876
:label: grasple_exercise_2_1_6
:dropdown:
:description: Two $3\times 3$ systems with the same coefficient matrix.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e1ffae46-da26-42b6-98ad-957478b6d58c?id=76653
:label: grasple_exercise_2_1_7
:dropdown:
:description: To write down the augmented matrix of a linear system.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c01e55fb-21d2-4539-a870-353a40d51db0?id=69506
:label: grasple_exercise_2_1_8
:dropdown:
:description: To check whether a linear system is consistent.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/796aca3d-2b17-4e17-bad7-a83c23c88db8?id=69545
:label: grasple_exercise_2_1_9
:dropdown:
:description: To check whether a linear system is consistent.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/447cc6ad-095e-4704-9445-8fcb4e9c4b8e?id=69587
:label: grasple_exercise_2_1_10
:dropdown:
:description: To recognize row operations.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/204cb1ad-0608-40ce-bb56-a2a6c6e8f1af?id=69559
:label: grasple_exercise_2_1_11
:dropdown:
:description: To find the row reduced echelon form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/a05fdf80-1325-4e86-874e-cd858133ad46?id=69558
:label: grasple_exercise_2_1_12
:dropdown:
:description: To find the row reduced echelon form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/73ced8a4-d6f8-494f-b58a-9e2f4053cd5b?id=82689
:label: grasple_exercise_2_1_13
:dropdown:
:description: To find the row reduced echelon form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/2b25fdf4-e662-4859-9f30-8838a1a7079f?id=69562
:label: grasple_exercise_2_1_14
:dropdown:
:description: To find the row reduced echelon form.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/1dad6770-3b71-4c80-ae78-e63d2cfd93e9?id=69563
:label: grasple_exercise_2_1_15
:dropdown:
:description: Row reduced echelon form of a $3 \times 5$ matrix.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/8d249aed-fa38-4a70-8271-8be07187dd06?id=69541
:label: grasple_exercise_2_1_16
:dropdown:
:description: Solving a linear system using the augmented matrix.

::::

%::::{grasple}
%:iframeclass: dark-light
%:url: https://embed.grasple.com/exercises/8d249aed-fa38-4a70-8271-8be07187dd06?id=69541
%:label: grasple_exercise_2_1_17
%%:dropdown:
%:description: Solving a linear system using the augmented matrix.
%
%::::

The remaining exercises are a bit more theoretical.

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/34663755-68a2-46ec-a3e7-0ad78ba9bdcd?id=71059
:label: grasple_exercise_2_1_T1
:dropdown:
:description: To solve a linear system by geometric considerations.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/3077fca5-9295-4634-a72d-18eca315de59?id=69743
:label: grasple_exercise_2_1_T2
:dropdown:
:description: How many pivots can an $m\times n$ matrix have?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e9b7c9da-fe93-46a3-bde7-6bd8c4583aa8?id=68838
:label: grasple_exercise_2_1_T3
:dropdown:
:description: To determine which variables can be taken as free variables.

::::

Four exercises about linear systems with a parameter.

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e906b587-b749-438a-a97b-4a4ef917a7b2?id=69744
:label: grasple_exercise_2_1_T4A
:dropdown:
:description: A $2\times 2$ linear system with a parameter $h$.

::::
::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9a51faa0-98f0-4934-81b5-7d78d7fef7ec?id=69745
:label: grasple_exercise_2_1_T4B
:dropdown:
:description: A $2\times 2$ linear system with a parameter $h$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/12852bd2-dfc4-41e4-8e53-c0c5664d2537?id=69746
:label: grasple_exercise_2_1_T4C
:dropdown:
:description: Yet another $2\times 2$ linear system with a parameter $h$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/69589418-544a-46c7-9d36-517b3db92bd1?id=69747
:label: grasple_exercise_2_1_T4D
:dropdown:
:description: Fourth and last $2\times 2$ linear system with a parameter $h$.

::::

Three exercises about linear systems and pivots.

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9e6cf6e3-80d2-4552-b668-cfc3bcdad27a?id=69748
:label: grasple_exercise_2_1_T5B
:dropdown:
:description: Linear systems and pivots.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/5eb59a87-6524-4563-9c86-f54e6fdca71d?id=69749
:label: grasple_exercise_2_1_T5C
:dropdown:
:description: Linear systems and pivots.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/9fdb7774-56f2-4a04-ae4a-a28fd4d2fd97?id=69750
:label: grasple_exercise_2_1_T5D
:dropdown:
:description: Linear systems and pivots.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/d8ed4c96-da3f-4fb4-baa4-77c99cfdfeae?id=70370
:label: grasple_exercise_2_1_T17
:dropdown:
:description: How many 'different' echelon forms are there?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/23a43d40-9e2d-4d92-bf63-40519dcb7d65?id=82692
:label: grasple_exercise_2_1_T18  
:dropdown:
:description: To determine (in)consistency without computations ('by inspection').

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/763dd8fd-fdbd-4d59-b49e-1d52977a1a8e?id=87122
:label: grasple_exercise_2_1_T19  
:dropdown:
:description: Freedom of free variables?

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/dbeb91c3-4834-4204-9b0f-ca7bf4bd5ecd?id=71103
:label: grasple_exercise_2_1_T20  
:dropdown:
:description: To check whether matrices are (row) equivalent.

::::
