# Markov chains

Suppose we have, say, three brands competing with each other in some niche of the market. Every month, a certain percentage of customers changes brands. What percentage of the market will each brand control after a given nubmer of months? What will be the market share of each brand in the long run? To answer these kind of questions, we need Markov chains.

One of the salient factors of this simple model is that no customers are entering or leaving the market. That is, when a customer starts for example with brand A, he will, after one month, either use brand A, B, or C. In other words, the probabilities of him using any single brand sum to 1. This leads us to the following definition.

:::{prf:def}

We call a vector $\vect{v}$ in $\R^{n}$ a **probability vector** if the sum of its entries is 1 and none of the entries are negative.

:::

In this definition, $n$ is the number of brands. Clearly, for any brand there must be such a probability vector. This yields $n$ vectors in $\R^{n}$ or, in other words, an $n\times n$-matrix.

:::{prf:def}

A **stochastic matrix** is a square matrix, each column of which is a probability vector.

:::

