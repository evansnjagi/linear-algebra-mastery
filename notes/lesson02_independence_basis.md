# Linear Algebra Mastery
## Linear Independence and Basis
> A set of n-vectors is said to be linearly independent, if all vectors point in different direction, geometrically. 

> A basis is a set of n-vectors that are linearly independent and spans the entire space. 

### Key Definitions
1. Linear independence - A set of n-vectors, $\mathbf{v_1}, \mathbf{v_2}, \cdots, \mathbf{v_n}$ given that $n > 1$, is said to be linearly independent if $c_1 \mathbf{v_1} + c_2 \mathbf{v_2} + \cdots + c_n \mathbf{v_n} = \mathbf{0}$, for some scalars $c_1 = c_2 = \cdots = c_n = 0 \in \mathbb{R}$.
2. Linear dependence - A collection of n-vectors in $\mathbb{R}^n$, is linearly dependent if there exist a nonzero solution in the equation $c_1 \mathbf{v_1} + \cdots + c_n \mathbf{v_n} = \mathbf{0}$. $c_i \in \mathbf{R}$ are not all equal to zero. See the deduction below:
$$
    c_1 \mathbf{v_1} + c_2 \mathbf{v_2} + 
    \cdots +
    c_k \mathbf{v_k} + 
    \cdots + 
    c_n \mathbf{v_n} = 
    \mathbf{0}
$$
For a collection of vectors to be linearly dependent, one or more scalars must be nonzero, in this case, let $c_k$ be a nonzero scalar.
$$
0 \mathbf{v_1} + 
0 \mathbf{v_2} + 
\cdots +
c_k \mathbf{v_k} + 
\cdots + 
0 \mathbf{v_n} = \mathbf{0}
$$
$$
    \implies c_k \mathbf{v_k} = 
    \mathbf{0} - (0 \mathbf{v_1} + 0 \mathbf{v_2}+
     \cdots + 
     0 \mathbf{v_{k - 1}} + 
     0 \mathbf{v_{k + 1}} + \cdots + 
     c_n \mathbf{v_n}
     )
$$
$$
    \therefore \mathbf{v_k} = 
    \mathbf{0} - \left(\frac{0 \mathbf{v_1} + 0 \mathbf{v_2} + \cdots + c_n \mathbf{v_n}}{c_k}\right) 
$$
Vector $\mathbf{v_k}$ is a *linear combination* of other vectors, thus rendering the entire collection to be linearly dependent.

3. Basis - The minimum set of linearly independent vectors needed to reach every point in space. 
4. Standard basis - A list of standard unit vectors forms a standard basis.

### Key Properties
1. For a collection of n-vectors to be linearly independent, $c_1 = c_2 = \cdots = c_n = 0$, for all $c_i \in \mathbb{R}$. 
2. A list of n-vectors, containing a zero vector, is linearly dependent.
3. The zero vector, $\mathbf{0}$, is linearly dependent.
4. A set of n-vectors, with only standard unit vectors, is linearly independent.
5. A single nonzero vector is linearly independent.
6. Parallel vectors are linearly dependent.

### Proof 
A set of n-vectors,with a zero vector, is ALWAYS linearly dependent. Here is the prove.

By definition, a linearly independent set has $c_1 \mathbf{v_1} + c_2 \mathbf{v_2} + \cdots + c_n\mathbf{v_n} = \mathbf{0}$, with an exact solution $c_1 = c_2 = \cdots = c_n = 0$.

Let $S = \{\mathbf{v_1}, \mathbf{v_2} + \cdots + \mathbf{v_n}\}$ and $V_k \in S$ be a zero vector.
$$
    \implies 0 \mathbf{v_1} + 0 \mathbf{v_2} + \cdots + 1 \cdot \mathbf(0) + \cdots + 0 \mathbf{v_n} = 
    \mathbf{0}
$$
There exist a nonzero solution for $c_i$, $c_k = 1$, therefore the set is linearly dependent. $\blacksquare$

### Python Implementation

### ML Connection