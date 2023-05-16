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
\item There esists a matrix $B$ with $BA=I$.
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
\item $0$ is not an eigenvalue of $A$.
\label{It:Appendices:InvIffZeroNoEV}

:::

::::


:::{prf:proof}

For the equivalence of {itemref}`It:Appendices:InvDef` through {itemref}`It:Appendices:InvDefColSpanRn`, see {prf:ref}`Thm:MatrixInv:InvertibilityCharacterizations` and . For {itemref}`It:Appendices:InvIffFullRank`. For {itemref}`It:Appendices:InvIffZeroNoEV`, see {prf:ref}`Prop:EigenValues:Singularity`.

:::


%:::{prf:proof}

%For the equivalence of {itemref}`It:Appendices:InvDef` through {itemref}`It:Appendices:InvDefColSpanRn`, see {prf:ref}`Thm:MatrixInv:InvertibilityCharacterizations` and {prf:ref}`Exc:BasisDim:ProveRankABLeqRankA`. For {itemref}`It:Appendices:InvIffFullRank`. For {itemref}`It:Appendices:InvIffZeroNoEV`, see {prf:ref}`Prop:EigenValues:Singularity`.

%:::


%:::{prf:proof}

%For the equivalence of  through, see {prf:ref}`Thm:MatrixInv:InvertibilityCharacterizations` and {prf:ref}`Exc:BasisDim:ProveRankABLeqRankA`. For , see {prf:ref}`Thm:BasisDim:RankThm`. For, see {prf:ref}`Prop:EigenValues:Singularity`.

%:::