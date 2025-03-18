# The inverse matrix theorem

Throughout this book, there are a great many different characterizations of those matrices which are invertible. In this place, we have collected them all for conveniently looking them up.

::::{prf:theorem}
:label: Thm:Appendices:InverseMatrixTheorem

For an $n\times n$ matrix $A$, the following are equivalent:

:::{latexlist}
:enumerated: true
:type: i

\item $A$ is invertible.
\label{It:Appendices:InvDef}

\item There exists a matrix $B$ with $AB=I$.
\item There exists a matrix $B$ with $BA=I$.
\item The linear system $A\vect{x}=\vect{b}$ has a unique solution for any $\vect{b}$ in $\R^{n}$.
\item $A$ is row equivalent to the identity matrix.
\item $A$ has linearly independent columns.
\item $A$ has linearly independent rows.
\item $A\vect{x}=\vect{0}$ only has the trivial solution.
\item There is a decomposition $A=E_{1}\cdots E_{k}$ where each $E_{i}$ is an elementary matrix.
\item Every column of $A$ is a pivot column.
\item The columns of $A$ span all of $\R^{n}$.
\label{It:Appendices:InvDefColSpanRn}
\item $\mathrm{rank}{A}=n$.
\label{It:Appendices:InvIffFullRank}
\item $\det(A)\neq 0$.
\label{It:Appendices:InvIffDetNeq0}
\item $0$ is not an eigenvalue of $A$.
\label{It:Appendices:InvIffZeroNoEV}

:::

::::

:::{admonition} Proof of&nbsp;{prf:ref}`Thm:Appendices:InverseMatrixTheorem`
:class: tudproof

For the equivalence of {itemref}`It:Appendices:InvDef` through {itemref}`It:Appendices:InvDefColSpanRn`, see {prf:ref}`Thm:MatrixInv:InvertibilityCharacterizations` and {numref}`Exc:BasisDim:RankABLeqRankA`. Statement {itemref}`It:Appendices:InvIffFullRank` is part of {prf:ref}`Thm:BasisDim:RankThm`. {prf:ref}`Thm:DetRowReduction:Invertibility` says precisely that invertibility is equivalent to {itemref}`It:Appendices:InvIffDetNeq0`. For {itemref}`It:Appendices:InvIffZeroNoEV`, see {prf:ref}`Prop:EigenValues:SingularMatrix`.

:::
