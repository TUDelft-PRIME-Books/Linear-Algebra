(Sec:DetGeometric)=
# Determinants as Areas or Volumes


## Introduction

The word "determinant" already appeared in the section about invertibility:  a $2\times2$ matrix
$A = \left[\begin{array}{cc} a & b \\ c & d\end{array}   \right]$  is invertible if and only if


:::{math}
:label: Eq:DetGeometric:DetNonzero

ad-bc \neq 0.

:::


We called the expression $ad-bc$  the *determinant* of the matrix $A$.   Formula {eq}`Eq:DetGeometric:DetNonzero` is also equivalent to the statement that the columns of the matrix $A$ are linearly independent.

Likewise, by row reducing  a general $3 \times 3$ matrix

$$
A = \left[\begin{array}{ccc} a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33}\end{array}   \right]
$$

we might end up with an expression containing all the entries  $a_{ij}$ that tells us whether  $A$ is invertible or not.
In this section we will use a geometric approach to derive such an expression, and will again call this the determinant of the matrix $A$. Its formula
(Equation {eq}`Eq:DetGeometric:3x3Det`), when looked at from the right perspective, shows an opportunity to  generalize the concept to higher dimensions.
We will follow that route in {numref}`Section %s <Sec:DeterminantsViaCofactors>`.

We will start by introducing determinants as a way to compute areas (in the plane) and volumes (in the space $\R^3$).



## Area, orientation, determinant


We start with two vectors $\vect{u}$ and $\vect{v}$  (as always, starting from the origin) in $\R^2$. They 'span' a parallelogram $OACB$,
where  $A$ and $B$ are the end points of $\vect{u}$ and $\vect{v}$,  and $C$ corresponds to the vector $\vect{u}+\vect{v}$.  See {numref}`Figure %s <Fig:DetGeometric:PargramOACB>`




::::{figure} Images/Fig-DetGeometric-PargramOACB.svg
:name: Fig:DetGeometric:PargramOACB


The  parallelogram OACB
::::


::::::{prf:proposition}
:label: Prop:DetGeometric:Area


The area of the parallelogram  $OACB$, spanned by the vectors   $ \vect{u} =\left[\begin{array}{c} a \\ b \end{array}\right]$  and 
$\vect{v}=\left[\begin{array}{c} c \\ d \end{array}\right]$ 
is given by  $|ad-bc|$, i.e., the absolute value of &nbsp;  $ad-bc$.

::::::



::::::{prf:proof}

The quickest way to prove this is to translate it to the cross product  ({numref}`Sec:CrossProduct`). To make use of the cross product we  introduce the vectors.

$$
\tilde{\vect{u}} = \left[\begin{array}{c} a \\ b \\ 0 \end{array}\right]
 \quad \text{and} \quad
\tilde{\vect{v}} = \left[\begin{array}{c} c \\ d \\ 0 \end{array}\right]
$$

Thus we embed the plane into $\R^3$ as the $x_1$-$x_2$-plane.  See  {numref}`Figure %s <Fig:DetGeometric:OrientedArea1>`.

::::{figure} Images/Fig-DetGeometric-OrientedArea1.svg
:name: Fig:DetGeometric:OrientedArea1

Oriented area
::::

So we embed the plane $\R^2$ as the $x$-$y$-plane into $\R^3$.

We then  have

$$
\tilde{\vect{u}} \times \tilde{\vect{v}} = \left[\begin{array}{c} 0 \\ 0 \\ ad-bc \end{array}\right].
$$

The length of this cross product is equal to $|ad-bc|$.  This   gives the area of the parallelogram spanned by the vectors $\tilde{\vect{u}}$ and  $\tilde{\vect{v}}$, and this is an identical copy of the original parallelogram spanned by  $\vect{u}$ and  $\vect{v}$.

::::::


Now what about the sign here?



::::::{prf:proposition}

$ad - bc = \norm{\vect{u}}\norm{\vect{v}}\sin(\varphi)$,  where $\varphi$ is the  angle from  $\vect{u}$ counterclockwise to $\vect{v}$. 
We will call this the **directed angle** from  $\vect{u}$  to $\vect{v}$.

::::::




::::::{prf:proof}

Again we can resort to properties of the cross product, but in fact it is  not necessary to go up one dimension.
By a small twist we can turn the determinant into an inner product:

$$
ad-bc = \left[\begin{array}{c} -b \\ a  \end{array}\right]
 \ip \left[\begin{array}{c} c \\ d  \end{array}\right]
  =
\vect{u}^{\perp} \ip \vect{v},
$$

where  $\vect{u}^{\perp}$  is the vector that is perpendicular to $\vect{u}$, points 'to the left' of $\vect{u}$, and has the same length as $\vect{u}$.  See {numref}`Figure %s <Fig:DetGeometric:AreaPargram>`.


::::{figure} Images/Fig-DetGeometric-AreaPargram.svg
:name: Fig:DetGeometric:AreaPargram


The parallelogram $OACB$ and the orthogonal vector $\vect{u}^{\perp}$
::::


So

$$
ad-bc = \vect{u}^{\perp} \ip \vect{v} = \norm{\vect{u}^{\perp}} \norm{\vect{v}}\cos(\vartheta),
$$

where  $\vartheta$ is the angle between  $\vect{u}^{\perp}$  and $\vect{v}$.
Here $h = \norm{\vect{v}}\cos(\vartheta)$  is $(\pm)$ the length of the projection of $\vect{v}$ onto the line perpendicular to $\vect{u}$, which can be interpreted as the height of the parallelogram.  So then

$$
\begin{array}{rcl}
\norm{\vect{u}^{\perp}} \norm{\vect{v}}\cos(\vartheta) 
  &=& \norm{\vect{u}}\times \norm{\vect{v}}\cos(\vartheta) \\
  &=& \pm \text{(base length)} \times \text{height} \\
  &=&   \pm \text{area of } OACB.
\end{array}  
$$

After some rewriting

$$
\begin{array}{ccl}
ad - bc &=&
\norm{\vect{u}^{\perp}}\norm{\vect{v}}\cos(\vartheta) \\
&=& \norm{\vect{u}}\norm{\vect{v}}\cos(\tfrac12\pi-\varphi)\\
&=& \norm{\vect{u}}\norm{\vect{v}}\sin(\varphi),
\end{array}
$$

where $\varphi$ is the angle from $\vect{u}$ to the left (= counterclockwise) to $\vect{v}$.

We see that  $ad-bc$  is equal to the area of the parallelogram if the angle from $\vect{u}$ to $\vect{v}$ is less then $\pi$, and minus this area if the angle is between $\pi$ and $2\pi$.

::::::





::::::{prf:definition}
:label: Dfn:DetGeometric:Orientation


The **determinant** of the ordered set  $(\vect{u},\vect{v})$  of two  vectors $\vect{u} =\left[\begin{array}{c} a \\ b \end{array}\right]
$ and $\vect{v}=\left[\begin{array}{c} c \\ d \end{array}\right]
$ in $\R^2$  is defined as

$$
\det{(\vect{u},\vect{v})} = ad - bc.
$$

Alternatively, the determinant can be seen as an operator working on $2 \times 2$ matrices, coming with its own notation:

$$
\det{\big([\, \vect{u} \,\, \vect{v}\, ]\big)}  = \det{\left(\left[\begin{array}{cc} a & c \\ b & d \end{array}\right]\right)}  =
\left|\begin{array}{cc} a & c \\ b & d \end{array}\right|= ad-bc.
$$

::::::



Apart from the area, the determinant also says something about the relative position of the two vectors $\vect{u}$ and $\vect{v}$.
In fact, we can use the determinant to *define* the orientation of two vectors in the plane (and, later, also of $n$ vectors in $\R^n$).




::::::{prf:definition}
:label: Dfn:DetGeometric:Orientation2

The ordered set  $(\vect{u},\vect{v})$  of two linearly independent vectors $\vect{u}$ and $\vect{v}$ is said to be **positively oriented**
if  $\det{(\vect{u},\vect{v})} > 0$, and **negatively oriented**
if $\det{(\vect{u},\vect{v})} < 0$.

::::::



::::::{prf:proposition}
:label: Prop:DetGeometric:Properties2by2Det


Two by two determinants obey the following rules:
<ol type = "i">
<li>

$\det{(\vect{v},\vect{u})}  = - \det{(\vect{u},\vect{v})}$.

</li>
<li>

$\det{(\vect{u},\vect{v}+\vect{w})} = \det{(\vect{u},\vect{v})} + \det{(\vect{u},\vect{w})}$.

</li>
<li>

$\det{(\vect{u},k\vect{v})} = k \det{(\vect{u},\vect{v})}$, $k \in \R$.

</li>
<li>

$\det{(\vect{e_1},\vect{e_2})} = 1$.

</li>
</ol>


These properties can also be expressed using matrices.

Two by two determinants obey the following rules:
<ol type = "i">
<li>

$ \begin{vmatrix} c & a \\ d & b  \end{vmatrix} = - \begin{vmatrix} a & c \\ b & d  \end{vmatrix}$.

</li>
<li>

$\begin{vmatrix} a_{1} & b_{1}+ c_1\\ a_{2} & b_{2}+ c_2 \end{vmatrix} = \begin{vmatrix} a_{1} & b_{1}\\ a_{2} & b_{2}\end{vmatrix}+ \begin{vmatrix} a_{1} & c_1\\ a_{2} &  c_2 \end{vmatrix}$.

</li>
<li>

$\begin{vmatrix} a_{1} & k b_{1}\\ a_{2} & k b_{2}\end{vmatrix} = k \begin{vmatrix} a_{1} & b_{1}\\ a_{2} & b_{2}\end{vmatrix}$.

</li>
<li>

$\begin{vmatrix} 1 & 0 \\ 0 & 1\end{vmatrix} =  1$.

</li>
</ol>

::::::




These properties are verified by applying the definition

$$
\left|\begin{array}{cc} a & c \\ b & d \end{array}\right| = ad-bc.
$$




::::::{exercise}
:label: Exc:DetGeometric:Properties2by2Det


Verify the four properties of {prf:ref}`Prop:DetGeometric:Properties2by2Det`

:::::: 

The properties have a clear geometric interpretation using the notion of 'signed area'.
The following alternative proof uses this geometric viewpoint.



::::::{prf:proof}


Three of the four properties are quickly settled.
<ol type = "i">
<li>

 Interchanging $\vect{u}$  and $\vect{v}$ does not alter the parallelogram.  However, it changes the orientation of the two vectors, and thus the signed area changes sign.

</li>
</ol>

<ol type = "i" start = "3">

<li>

$\det{(\vect{u},k\vect{v})} = k\times\det{(\vect{u},\vect{v})}$, $k \in \R$.

Giving one of the vectors a factor $k$ changes the area with a factor  $|k|$.  If $k > 0$, the orientation of the two vector does not change, so the determinant gets a factor $|k|$, which in this case is equal to $k$.  If however $k < 0$, then the orientation does change, so  the determinant gets a factor $-|k|$, which in this case is again equal to $k$.

</li>
<li>

$\det{(\vect{e_1},\vect{e_2})} $  is the area of the unit square.

</li>

</ol>


The remaining property,
<ol type = "i" start = "2">
<li>

$\det{(\vect{u},\vect{v}+\vect{w})} = \det{(\vect{u},\vect{v})} + \det{(\vect{u},\vect{w})}$,

</li>
</ol>

is the most interesting one.  The two pictures of {numref}`Figure %s <Fig:DetGeometric:Linearity>`  tell the story.



::::{figure} Images/Fig-DetGeometric-SumRule.svg
:name: Fig:DetGeometric:Linearity

The sum rule in a picture. Note, this is a **2D picture**.
::::


In the picture on the left,  both  $(\vect{u},\vect{v})$  and $(\vect{u},\vect{w})$ are positively oriented.
So there

$$
\begin{array}{lcl}
\det{(\vect{u},\vect{v})} + \det{(\vect{u},\vect{w})} &=&
\text{area}(OABC) + \text{area}(CBDE) \\
&=& \text{area}(OADE) = \det{(\vect{u},\vect{v}+\vect{w})},
\end{array}
$$

since the two triangles $OCE$  and   $ABD$  are congruent, so have equal areas.

In the picture on the right,  the orientation of   $(\vect{u},\vect{v})$ is positive,  the orientation of $(\vect{u},\vect{w})$ is negative, and the orientation of $(\vect{u},\vect{v}+\vect{w})$ is positive again.
So there

$$
\begin{array}{lcl}
\det{(\vect{u},\vect{v})} + \det{(\vect{u},\vect{w})} &=&
\text{area}(OAFC) - \text{area}(OBDA) \\
&=& \text{area}(OAFC) - \text{area}(CGEF) \\
&=& \text{area}(OAEG) = \det{(\vect{u},\vect{v}+\vect{w})}
\end{array}
$$

since now the areas of $OAFC$ and $CGEB$  add up to the area of $OABC$,  owing to the
congruence of the triangles $OGC$  and   $AEF$.

There are more pairwise orientations to consider, but the idea is hopefully clear to you.

::::::


## $\, 3 \times 3$ determinants:   volume and orientation

Suppose $\vect{a}, \vect{b}, \vect{c}$  are three vectors in $\R^3$.  For the moment, suppose they are linearly independent.  So
$\vect{a}, \vect{b}$  are not multiples of each other, and $\vect{c}$ is not in the plane spanned by $\vect{a}, \vect{b}$.
Then  the three vectors can be interpreted as three edges of a parallelepiped.  See {numref}`Figure %s <Fig:DetGeometric:Paraped>`.



::::{figure} Images/Fig-DetGeometric-Paraped.svg
:name: Fig:DetGeometric:Paraped

Volume equals base area time height
::::



::::::{prf:proof}

Just as the area of a parallelogram can be computed as 'base length times height',  the volume of a parallelepiped can be computed as 'base area times height'.
As base region we can take  the parallelogram spanned by $\vect{a}$ and $\vect{b}$, and then the base area becomes

$$
A = \norm{\vect{a} \times  \vect{b}}.
$$

The height is found by projecting $\vect{c}$  onto the line through the origin that is perpendicular to the plane spanned by $\vect{a}$ and $\vect{b}$.  A direction vector of this line is precisely given by $\vect{a} \times  \vect{b}$.
So

$$
h =  \vect{c}\ip\vect{n}
$$

where $\vect{n}$    is the unit vector perpendicular to the 'base plane' that points to the same side as the vector $\vect{c}$.  This unit vector is given by

$$
\vect{n} = \pm   \frac{\vect{a} \times  \vect{b}}{\norm{\vect{a} \times  \vect{b}}}
$$

And then the formula 'height times base area' gives

$$
V = \vect{c}\ip\vect{n} = \pm \vect{c}\ip\frac{\vect{a} \times  \vect{b}}{\norm{\vect{a} \times  \vect{b}}}
\cdot \norm{\vect{a} \times  \vect{b}} = (\pm) \vect{c}\ip(\vect{a} \times  \vect{b}).
$$

The statement about the sign follows immediately from the third defining property of the cross product.

::::::


Note that the expression $\vect{c}\ip(\vect{a} \times  \vect{b})$ must be invariant under cyclic permutations of the three vectors.


::::::{prf:proposition}
:label: Prop:DetGeometric:CyclicPerm

$$
\vect{c}\ip(\vect{a} \times  \vect{b}) = \vect{a}\ip(\vect{b} \times  \vect{c})= \vect{b}\ip(\vect{c} \times  \vect{a})
$$

and swapping two vectors gives a minus sign:

$$
\vect{c}\ip(\vect{a} \times  \vect{b})= - \vect{c}\ip(\vect{b} \times  \vect{a}).
$$

::::::


::::::{prf:proof}

The parallelepiped spanned by the three vectors does not change under any permutation, and the orientation remains the same under a cyclic permutation.

::::::


The last proposition sets the way to take the determinant one dimension higher.


::::::{prf:definition}

The **determinant** of the ordered set of three vectors $\vect{a}, \vect{b}$ and $ \vect{c}$ in $\R^3$ is defined by the expression

$$
\det{(\vect{a}, \vect{b},\vect{c})} = \vect{a}\ip(\vect{b} \times  \vect{c}).
$$

Note that the determinant is a real number.

Alternatively, we can define the determinant as a function working on $3 \times 3$ matrices. And that is the sole interpretation we will use from now on.

If we put

$$
A = [ \,\vect{a}\,\,\vect{b}\,\,\vect{c}\,] = \left[\begin{array}{ccc} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2\\ a_3 & b_3 & c_3 \end{array} \right] ,
$$

then we define

$$
\det{A} = \left|\begin{array}{ccc} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2\\ a_3 & b_3 & c_3 \end{array} \right|= \vect{a}\ip(\vect{b} \times  \vect{c}).
$$

::::::


::::::{prf:proposition}
:label: Prop:DetGeometric:ColExpand

:::::{math}
:label: Eq:DetGeometric:3x3Det 

\left|\begin{array}{ccc} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2\\ a_3 & b_3 & c_3 \end{array} \right|=
a_1\left|\begin{array}{cc}  b_2 & c_2\\  b_3 & c_3 \end{array} \right|-
a_2 \left|\begin{array}{cc}  b_1 & c_1 \\ b_3 & c_3 \end{array} \right|+
a_3 \left|\begin{array}{cc}  b_1 & c_1 \\ b_2 & c_2\end{array} \right|.
:::::

The last expression can be further evaluated as

$$

a_1b_2c_3 - a_1b_3c_2 - a_2b_1c_3 +a_2b_3c_1 + a_3b_1c_2 - a_3b_2c_1.
$$

::::::


The expression involving the three $2 \times 2$  determinants will be the stepping stone to define the determinant of a general $n \times n$ matrix.

::::::{prf:proof}

The identities are verified by evaluating the triple product:

$$
\left[\begin{array}{c}  a_1 \\  a_2\\ a_3 \end{array} \right]
 \ip
\left( \left[\begin{array}{c}  b_1 \\  b_2\\ b_3 \end{array} \right]
 \times \left[\begin{array}{c}  c_1 \\  c_2\\ c_3 \end{array} \right]
\right)
 =
\left[\begin{array}{c}  a_1 \\  a_2\\ a_3 \end{array} \right]
 \ip
\left[\begin{array}{c}  b_2c_3-b_3c_2 \\  b_3c_1-b_1c_3\\ b_1c_2-b_2c_1 \end{array} \right]
 =
$$


$$
\begin{array}{cl}
=& a_1(b_2c_3 - b_3c_2) - a_2(b_1c_3 -b_3c_1) + a_3(b_1c_2 - b_2c_1)\\
=& a_1b_2c_3 - a_1b_3c_2 - a_2b_1c_3 + a_2b_3c_1) + a_3b_1c_2 - a_3b_2c_1).
\end{array}
$$

::::::



The next proposition summarizes  the relevant properties of $3 \times 3$ determinants.



::::::{prf:proposition}
:label: Prop:DetGeometric:Summary

For the determinant

$$
D = \det{A} = \det{\left[\,\vect{a}\,\, \vect{b}\,\,\vect{c}\, \right]
} = \left|\begin{array}{ccc} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2\\ a_3 & b_3 & c_3 \end{array} \right|
$$

the following properties hold
<ol type = "i">
<li>

$|D|$,   the absolute value of the determinant,  is equal to the volume of the parallelepiped with the edges  $\vect{a},\vect{b}$ and $\vect{c}$.

</li>
<li>

$D=0$ if and only if     the matrix  $A$  is singular.

Equivalently,

$D\neq 0$  if and only if  the matrix  $A$  is invertible, thus if   
the vectors  $\{\vect{a}, \vect{b},\vect{c}\}$   are linearly independent.


</li>
<li>

$D > 0$  if and only if the ordered set   $(\vect{a},\vect{b},\vect{c})$  is positively oriented.  That is,  oriented in the same way as the basis   $(\vect{e}_1,\vect{e}_2,\vect{e}_3)$.

</li>

<li>

$\det{I} =  \left|\begin{array}{ccc} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array} \right| = 1$.

</li>
</ol>

::::::