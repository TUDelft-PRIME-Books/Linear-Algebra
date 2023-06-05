# Markov chains

Suppose we have, say, three brands competing with each other in some niche of the market. Every month, a certain percentage of customers changes brands. What percentage of the market will each brand control after a given nubmer of months? What will be the market share of each brand in the long run? To answer these kind of questions, we need Markov chains.

One of the salient factors of this simple model is that no customers are entering or leaving the market. That is, when a customer starts for example with brand A, he will, after one month, either use brand A, B, or C. In other words, the probabilities of him using any single brand sum to 1. This leads us to the following definition.

:::{prf:def}

We call a vector $\vect{v}$ in $\R^{n}$ a **probability vector** if the sum of its entries is 1 and none of the entries are negative.

:::

Perhaps the chance that a customer of A remains with A after one month is $p_{11}$, the chance that he uses B after one month is $p_{21}$, and the chance that he uses C after one month is $p_{31}$. Then the probability vector associated to A will be

$$\vect{p}_{1}=\begin{bmatrix}
p_{11}\\
p_{21}\\
p_{31}
\end{bmatrix}.$$

Clearly, for brands B and C there must are similar probability vectors, say $\vect{p}_{2}$ and $\vect{p}_{3}$.

In a general situation with $n$ brands, we will find $n$ vectors in $\R^{n}$. Together, this yields an $n\times n$-matrix.

:::{prf:def}

A **stochastic matrix** is a square matrix, each column of which is a probability vector.

:::

Suppose, now, that the starting numbers of customers of brands A, B, and C are $a_{0}$, $b_{0}$, and $c_{0}$. What will be the number of customers for each brand after one month? Let's call them $a_{1}$,$b_{1}$, and $c_{1}$ respectively. Then we find:

$$
\begin{align*}
p_{11}a_{0}+p_{12}b_{0}+p_{13}c_{0}&=a_{1}\\
p_{21}a_{0}+p_{22}b_{0}+p_{23}c_{0}&=b_{1}\\
p_{31}a_{0}+p_{32}b_{0}+p_{33}c_{0}&=c_{1}
\end{align*}\quad\text{i.e.}\quad P\begin{bmatrix}
a_{0}\\
b_{0}\\
c_{0}
\end{bmatrix}=\begin{bmatrix}
a_{1}\\
b_{1}\\
c_{1}
\end{bmatrix}
$$

where $P=[\vect{p}_{1},\vect{p}_{2},\vect{p}_{3}]$ is the stochastic matrix associated to our model. 