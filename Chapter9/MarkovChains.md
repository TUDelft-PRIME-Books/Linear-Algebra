# Markov Chains

Suppose we have, say, three brands competing with each other in some niche of the market. Every month, a certain percentage of customers changes brands. What percentage of the market will each brand control after a given number of months? What will be the market share of each brand in the long run? To answer these kind of questions, we need Markov chains.

## Markov Chains

Assume we have a certain population divided into $n$ classes, say, by the brand they use. For every person using brand $i$, there is a certain chance $p_{ji}$ that he ends up using brand $j$ after a month. If we assume for the moment that nobody leaves or enters the population, every one must end up using _some_ brand. So $\sum_{j=1}^{n}p_{ji}=1$. Keeping in mind that every probability is a number between $0$ and $1$, we get to the following definition.

:::{prf:definition}

We call a vector $\vect{v}$ in $\R^{n}$ a **probability vector** if the sum of its entries is 1 and none of the entries are negative.

:::

Perhaps the chance that a customer of A remains with A after one month is $p_{11}$, the chance that he uses B after one month is $p_{21}$, and the chance that he uses C after one month is $p_{31}$. Then the probability vector associated to A will be

$$
\vect{p}_{1}=\begin{bmatrix}
p_{11}\\
p_{21}\\
p_{31}
\end{bmatrix}.
$$

Clearly, for brands B and C there must be similar probability vectors, say $\vect{p}_{2}$ and $\vect{p}_{3}$. If we take these three probability vectors together, they form a matrix.

:::{prf:definition}

A **stochastic matrix** is a square matrix, each column of which is a probability vector.

:::

Suppose, now, that the starting numbers of customers of brands A, B, and C are $a_{0}$, $b_{0}$, and $c_{0}$. What will be the number of customers for each brand after one month? Let's call them $a_{1}$, $b_{1}$, and $c_{1}$ respectively. Then we find

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

where $P=[\vect{p}_{1}\,\vect{p}_{2}\,\vect{p}_{3}]$ is the stochastic matrix associated to our model. We have now found the updated state after one month.

Often, it is more convenient to work with percentages instead of absolute numbers. This can be easily done by dividing $a_{0}$, $b_{0}$, and $c_{0}$ by the total population $a_{0}+b_{0}+c_{0}$. In doing so, we make sure that

$$
\vect{x}_{0}=\frac{1}{a_{0}+b_{0}+c_{0}}\begin{bmatrix}
a_{0}\\
b_{0}\\
c_{0}
\end{bmatrix}
$$

is a probability vector. It turns out that the new vector $\vect{x}_{1}$ is also a probability vector, as per the next proposition.

:::{prf:proposition}
:label: Prop:MarkovChains:StoMatPreservesProbVect

Suppose $P$ is a stochastic matrix. If $\vect{x}$ is a probability vector, then so is $P\vect{x}$.

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:MarkovChains:StoMatPreservesProbVect`
:class: tudproof

Note first that every entry of a stochastic matrix or a probability vector is non-negative. Consequently, every entry of $P\vect{x}$ is also non-negative.

Since $P$ is a stochastic matrix, $\sum_{i=1}^{n} P_{ij}=1$ for every $j$. Therefore,

$$
\begin{align*}
    \sum_{i=1}^{n}(P\vect{x})_{i}&=\sum_{i=1}^{n}\left(\sum_{j=1}^{n}P_{ij}\vect{x}_{j}\right)\\
    &=\sum_{j=1}^{n} \vect{x}_{j}\sum_{i=1}^{n} P_{ij}\\
    &=\sum_{j=1}^{n}\vect{x}_{j}=1
\end{align*}
$$

which had to be proven.

:::

:::{prf:Remark}

{prf:ref}`Prop:MarkovChains:StoMatPreservesProbVect` implies that the product of two stochastic matrices is again stochastic. In particular, any power of a stochastic matrix is again a stochastic matrix.

:::

Such situations are common enough to warrant dedicated terminology.

:::{prf:definition}

Let $P$ be a stochastic matrix. A **Markov chain** is a sequence $\vect{x}_{0},\vect{x}_{1},...$ of probability vectors such that $\vect{x}_{i}=P\vect{x}_{i-1}$ for any $i>0$. The $\vect{x}_{i}$ are called the **state vectors** of the Markov chain.

:::

:::{prf:Example}
:label: Ex:MarkovChains:MarkovChain

Suppose we have three brands, A, B, and C. Let us assume that 80\% of the customers of A and B will still use the same brand after a month and that the customers that switch away choose randomly between the alternatives. Finally, let us say that C retains 70\% of its customers, that 20\% of its customers leave for A, and that 10\% leave for B.

This gives us the following stochastic matrix:

$$
P=\begin{bmatrix}
0.8&0.1&0.2\\
0.1&0.8&0.1\\
0.1&0.1&0.7
\end{bmatrix}.
$$

If we, for example, assume that the three brands start out with equal market shares, we find

$$
\vect{x}_{0}=\begin{bmatrix}
1/3\\
1/3\\
1/3
\end{bmatrix}\quad\text{so}\quad \vect{x}_{1}=P\vect{x}_{0}=\begin{bmatrix}
11/30\\
10/30\\
9/30
\end{bmatrix},\quad \vect{x}_{2}=P\vect{x}_{1}=\begin{bmatrix}
116/300\\
100/300\\
84/300
\end{bmatrix},
$$

and so on. We can see that brand A consistently wins market share at the cost of brand C, while brand B keeps a constant customer base. Note, however, that C will never have no market share, as it will, every month, gain 10\% of both A and B's customer base.

:::

## Steady States

Consider again the simple model of {prf:ref}`Ex:MarkovChains:MarkovChain`. What will happen if this model runs for a long time? We expect that C will lose market share to A, but how much? When, if ever, will the process stabilise? These are the questions we will deal with in this section.

:::{prf:Definition}

Let $P$ be a stochastic matrix. A probability vector $\vect{x}$ is called a **steady state** for $P$ if $P\vect{x}=\vect{x}$. That is, if it is an eigenvector with eigenvalue 1.

:::

If a Markov chain with stochastic matrix $P$ has arrived in a steady state of $P$, it is easy to see what will happen: nothing. The Markov chain will stay in that steady state forever. And for any stochastic matrix there really is a steady state, as we will show now.

:::{prf:Proposition}
:label: Prop:MarkovChains:StoMat1EV

If $P$ is a stochastic matrix, then $1$ is an eigenvalue of $P$. Moreover, there is an eigenvector with eigenvalue $1$ that contains no negative entries.

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Prop:MarkovChains:StoMat1EV`
:class: tudproof

Showing that $1$ is an eigenvalue is a very non-trivial exercise. Showing that there is a corresponding eigenvector without negative entries would lead us too far.

:::

:::{prf:Remark}

As an immediate consequence of {prf:ref}`Prop:MarkovChains:StoMat1EV`, any stochastic $n\times n$-matrix $P$ has a steady state $\vect{x}$ in $\R^{n}$. Indeed, we can find an eigenvector $\vect{v}$ of $P$ with eigenvalue $1$ and then scale it by $1/\sum_{i=1}^{n}\vect{v}_{i}$. This gives us a new vector $\vect{x}$ which is still an eigenvector with eigenvalue $1$ and for which $\sum_{i=1}^{n}\vect{x}_{i}=1$. That is, it is a steady state.

:::

:::{prf:Example}

Let us revisit the matrix

$$
P=\begin{bmatrix}
0.8&0.1&0.2\\
0.1&0.8&0.1\\
0.1&0.1&0.7
\end{bmatrix}
$$

from {prf:ref}`Prop:MarkovChains:StoMat1EV`. With standard computations, we find that the eigenspace of eigenvalue 1 is spanned by

$$
\vect{v}=\begin{bmatrix}
5\\
4\\
3
\end{bmatrix}. \quad\text{Hence, the probability vector}\quad \vect{x}=\frac{1}{3+4+5}\begin{bmatrix}
5\\
4\\
3
\end{bmatrix}
$$

is a steady state for $P$.

:::

There may, in general, be many steady states for a Markov chain. In the most extreme case, where the probability matrix is $I_{n}$, _every_ state is a steady state. Why is this? Suppose we have three brands ($1,2,$ and $3$) and $P_{ij}$ is the probability that a customer switches from brand $i$ to brand $j$ after $1$ month. Then $P=I_{3}$ means that no customer ever switches, so the starting market shares, whatever they are, will be the same as the final market shares.

However, if it is at all possible, for every two brands $i$ and $j$, that a customer of $i$ ends up using $j$ after some time, then something remarkable happens: there is only one steady state and, no matter what the starting market shares are, they will converge towards this single steady state. That is the content of {prf:ref}`Thm:MarkovChains:PerronFrobenius`. But first some terminology.

:::{prf:definition}

A stochastic matrix is called **regular** if there is some natural number $k$ such that $P^{k}_{ij}>0$ for all $i$ and $j$, i.e. if and only if all entries of the $k$-th power of $P$ are positive.

:::

:::{prf:definition}

Let $\vect{x}$ be a vector and let $\vect{x}_{0},\vect{x}_{1},\vect{x}_{2},...$ be a sequence of vectors. We say that the sequence $(\vect{x}_{n})_{n\text{ in }\mathbb{N}}$ **converges** to $\vect{x}$ if the sequence of real numbers $(\norm{\vect{x_{n}}-\vect{x}})_{n\text{ in }\mathbb{N}}$ converges to $0$.

:::

Intuitively, $(\vect{x}_{n})_{n\text{ in }\mathbb{N}}$ converges to $\vect{x}$ if the distance between $\vect{x}$ and $\vect{x}_{n}$ becomes arbitrarily small for large enough $n$. In other words, if $\vect{x}_{n}$ comes arbitrarily close to $\vect{x}$.

:::{prf:Theorem} Perron-Frobenius
:label: Thm:MarkovChains:PerronFrobenius

If $P$ is a regular stochastic matrix, then it has a unique steady state $\vect{x}$. Furthermore, for any probability vector $\vect{x}_{0}$, the sequence defined by $\vect{x}_{n}=P\vect{x}_{n-1}$ for $n>0$ converges to $\vect{x}$.

:::

:::{admonition} Proof of&nbsp;{prf:ref}`Thm:MarkovChains:PerronFrobenius`
:class: tudproof

The proof is quite complicated and falls outside the scope of this text.

:::

Note that regularity is a sufficient but not a necessary condition for a stochastic matrix to have a single steady state. This can be seen in {prf:ref}`Ex:MarkovChains:MarkovChainonNodes`.

::::{prf:example}
:label: Ex:MarkovChains:MarkovChainonNodes

Let us consider the following toy problem, illustrated in {numref}`Figure %s <Fig:MarkovChains:FourNodesinCircle>`.

:::{figure} Images/Fig-MarkovChains-MarkovChainonNodes.svg
:name: Fig:MarkovChains:FourNodesinCircle
:class: dark-light

The problem from {prf:ref}`Ex:MarkovChains:MarkovChainonNodes` illustrated.

:::

Suppose four nodes are connected in a circle. One move can get us from a given node to a neighbouring node. If we make $k$ random moves, where will we end up with what probability? We can model this problem with a stochastic matrix $P$, for which the $i,j$-th entry is the probability of getting from the $i$-th to the $j$-th node in one move. This gives us

$$
P=\begin{bmatrix}
    0&\frac{1}{2}&0&\frac{1}{2}\\
    \frac{1}{2}&0&\frac{1}{2}&0\\
    0&\frac{1}{2}&0&\frac{1}{2}\\
    \frac{1}{2}&0&\frac{1}{2}&0
\end{bmatrix},\quad\text{hence}\quad P^{2}=\begin{bmatrix}
    \frac{1}{2}&0&\frac{1}{2}&0\\
    0&\frac{1}{2}&0&\frac{1}{2}\\
    \frac{1}{2}&0&\frac{1}{2}&0\\
    0&\frac{1}{2}&0&\frac{1}{2}
\end{bmatrix},
$$

$P^{3}=P$, $P^{4}=P^{2}$ etc. Since every power of $P$ contains some $0$ entry, $P$ is not regular. Nevertheless, there is only a single steady state, namely

$$
\vect{x}=\begin{bmatrix}\frac{1}{4}\\\frac{1}{4}\\\frac{1}{4}\\\frac{1}{4}\end{bmatrix}.
$$

Suppose, for instance, that we start at node $1$. This means that our starting state will be

$$
\vect{x}_{0}=\begin{bmatrix}
1\\0\\0\\0
\end{bmatrix},\quad\text{so}\quad \vect{x}_{1}=\begin{bmatrix}
0\\
\frac{1}{2}\\
0\\
\frac{1}{2}
\end{bmatrix},\quad\vect{x}_{2}=\begin{bmatrix}
\frac{1}{2}\\
0\\
\frac{1}{2}\\
0
\end{bmatrix},
$$

and $\vect{x}_{n}=\vect{x}_{n-2}$ for $n$ greater than $3$. This gives us complete information about with what probility we will be where after how many moves.

What makes this Markov chain behave so weirdly is the fact that any two nodes are either only connected by paths of even length or only by paths of odd length. Let us now apply an apparently innocuous change: if we are at node $1$, we now have a $1/3$ chance of staying in $1$. This is illustrated in {numref}`Figure %s <Fig:MarkovChains:ExtraLoop>`.

:::{figure} Images/Fig-MarkovChains-ExtraLoop.svg
:name: Fig:MarkovChains:ExtraLoop
:class: dark-light

The problem from {prf:ref}`Ex:MarkovChains:MarkovChainonNodes` with an extra loop. Note that the outgoing arrows from node 1 now have different probabilities.

:::

The chances of going from $1$ to either $2$ or $4$ are also $1/3$. The new stochastic matrix becomes

$$
P=\begin{bmatrix}
    \frac{1}{3}&\frac{1}{2}&0&\frac{1}{2}\\
    \frac{1}{3}&0&\frac{1}{2}&0\\
    0&\frac{1}{2}&0&\frac{1}{2}\\
    \frac{1}{3}&0&\frac{1}{2}&0
\end{bmatrix}.
$$

Using a computer, we find the following powers of $P$:

$$
P^{2}=\frac{1}{36}\begin{bmatrix}
16&6&18&6\\
4&15&0&15\\
12&0&18&0\\
4&15&0&15
\end{bmatrix}\quad\text{and}\quad
P^{3}=\frac{1}{108}\begin{bmatrix}
28&51&18&51\\
34&6&45&6\\
12&45&0&45\\
34&6&45&6
\end{bmatrix}
$$

which still contain $0$ entries, but also

$$
P^{4}=\frac{1}{648}\begin{bmatrix}
260&138&306&138\\
92&237&36&237\\
204&36&270&36\\
92&237&36&237
\end{bmatrix}
$$

and this matrix, finally, contains only strictly positive elements. So $P$ really is regular.

As you can see, computing the powers of a stochastic matrix by hand quickly becomes difficult. However, because we are dealing with a regular stochastic matrix, we can still predict what will happen after a long time. We just need to find the steady state, i.e. we need to solve $P\vect{x}=\vect{x}$ and find a solution $\vect{x}$ for which the entries add up to $1$. This is a standard computation, which yields, as it should, a single solution:

$$
\vect{x}=\begin{bmatrix}
\frac{1}{3}\\
\frac{2}{9}\\
\frac{2}{9}\\
\frac{2}{9}
\end{bmatrix}.
$$


From it, we can read off that, should we let this process continue for a long time, we will have a $1$ in $3$ chance of landing in node $1$ and a $2$ in $9$ chance for each other node.

For example, if we start in node $3$, we find the following process:

$$
\vect{x}_{0}=\begin{bmatrix}
0\\
0\\
1\\
0
\end{bmatrix},\vect{x}_{1}=\begin{bmatrix}
0\\
\frac{1}{2}\\
0\\
\frac{1}{2}
\end{bmatrix},\vect{x}_{2}=\begin{bmatrix}
\frac{1}{2}\\
0\\
\frac{1}{2}\\
0
\end{bmatrix},\vect{x}_{3}=\begin{bmatrix}
\frac{1}{6}\\
\frac{5}{12}\\
0\\
\frac{5}{12}
\end{bmatrix},...,\vect{x}_{50}\approx\begin{bmatrix}
0.3335\\
0.2221\\
0.2224\\
0.2221
\end{bmatrix},...
$$

so the distribution after $50$ moves is already quite close to the steady state. Remark that nodes $2$ and $4$ have the exact same probability in every state.

::::



## Grasple Exercises



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/ae1aee60-cada-4419-b0f1-dd1f7d4b4e13?id=110356
:label: grasple_exercise_9_2_1
:dropdown:
:description: To find the steady state of 3x3 probability matrix $P$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/c5c526e8-2a6a-4714-a99f-4a956bbfe0f0?id=110857
:label: grasple_exercise_9_2_2
:dropdown:
:description: To find the steady state of 3x3 probability matrix $P$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/e2a616ee-2bc6-4e2b-8e04-2161ae75e3f0?id=110321
:label: grasple_exercise_9_2_3
:dropdown:
:description: To find the steady state of 3x3 probability matrix $P$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/6b2f6fe5-72d8-48c0-bc12-97afeedc04bd?id=110861
:label: grasple_exercise_9_2_4
:dropdown:
:description: Steady state + high powers of 2x2 probability matrix $P$.

::::

::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/44508dbb-5a1f-42d6-918b-fc7c464b4e0d?id=110368
:label: grasple_exercise_9_2_5
:dropdown:
:description: To construct a Markov Chain from a cycling story

::::



::::{grasple}
:iframeclass: dark-light
:url: https://embed.grasple.com/exercises/632c5581-1a58-427a-a620-19da8b094470?id=110775
:label: grasple_exercise_9_2_6
:dropdown:
:description: To construct a Markov Chain for a frog on lillies

::::