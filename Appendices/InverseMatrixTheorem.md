# The inverse matrix theorem

Throughout this book, there are a great many different characterizations of those matrices which are invertible. In this place, we have collected them all for conveniently looking them up.

:::{prf:theorem}
:label: Thm:Appendices:InverseMatrixTheorem

For an $n\times n$ matrix $A$, the following are equivalent:

<ol type="i">

<li id="It:Appendices:InvDef">

$A$ is invertible.

</li>

<li id="It:Appendices:LinIndCol">

$A$ has linearly independent columns (or, equivalently, linearly independent rows).

</li>

<li>

There exists a matrix $B$ with $AB=I$.

</li>

<li>

There esists a matrix $B$ with $BA=I$. 

</li>

<li>

The linear system $A\vect{x}=\vect{b}$ has a unique solution for any $\vect{b}$ in $\R^{n}$.

</li>

<li>

A is similar to the identity matrix.

</li>

<li>

There is a decomposition $A=E_{1}\cdots E_{k}$ where each $E_{i}$ is an elementary matrix.

</li>

<li>

Every column of $A$ is a pivot column.

</li>

<li>

The columns of $A$ span all of $\R^{n}$.

</li>

<li>

$\det(A)\neq 0$.

</li>

<li>

$0$ is not an eigenvalue of $A$.

</li>


</ol>

:::

:::{prf:proof}

For the equivalence of [i](#It:Appendices:InvDef) and [ii](#It:Appendices:LinIndCol), see {prf:ref}`Prop:MatrixInv:Algorithm`. See {prf:ref}`Thm:MatrixInv:InvertibilityCharacterizations` for [iii.] to [vii.]. For [xi], see {prf:ref}`Prop:EigenValues:Singularity`.

:::