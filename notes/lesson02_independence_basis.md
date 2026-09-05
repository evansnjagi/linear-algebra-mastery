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
1. Linear independence - To check for linear independence in Python, follow the following steps:
    
    - Define your arrays using `np.array()`, having imported NumPy with alias `np`.
    - Combine the arrays into a matrix, `np.column_stack()`.
    - Using, `np.linalg.matrix_rank()`, compute rank of the matrix. Rank gives us the number of vectors that are linearly independent. Those that are pointing in different directions, geometrically.
    - Compare rank with the total number of vectors used to compute rank.
    - If $rank < \text{number of vectors}$, the set is linearly dependent. This means that there exist at least one vector that can be expressed as a linear combination of other vectors, redundant.
2. Standard basis - Conceptually, with a set of n-standard unit vectors, you can construct any vector in that space. This is true because the set is linearly independent, there is NO redundant vector. To check this analogy in Python, follow the steps below:

    - Define your set $S = \{e_1, e_2, \cdots, e_n\}$, a set of standard unit vectors i.e. 
    $\left\{
        \begin{pmatrix}
            1 \\ 0
        \end{pmatrix},
        \begin{pmatrix}
            0 \\ 1
        \end{pmatrix}
    \right\}$ is a set of standard unit vectors in $\mathbb{R}^2$. 
    
    - Using NumPy, stack the set of standard unit vectors together as a matrix.

    - Compute the rank of the stacked matrix, use `np.linalg.matrix_rank()`.

    - Compare the computed rank with the number of standard unit vectors, the two values should be the same.
3. ML connection - In a machine learning project, there are two types of data: feature matrix, $\mathbf{X}$ and target vector, $\mathbf{y}$. You can check if your feature matrix has redundant rows or columns using NumPy, by computing rank.

### ML Connection
In machine learning i.e. linear regression, to avoid multicollinearity we must make sure all features are linearly independent. If one feature can be derived from another, it makes the feature matrix, $\mathbf{X}$ non-invertible, and the model weights unstable or impossible to compute. 

Removing linearly dependent or redundant features, from the feature matrix, shrinks the feature space, speeding training time. It also prevents overfitting by ensuring every input contribute distinct predictive power.