# Linear Algebra Mastery
## Vectors and Vector Operations
> A vector is an ordered list of finite numbers that has both magnitude and direction. A vector is written using a small bold italic type font. Coefficient of a vector is written with italic, small but NOT bold letters.

### Key definitions
1. Span - A span is a set of all linear combination for a set of n-vectors.
2. Basis - This is a set of linearly independent vectors, that spans the entire space. With basis, you can reach every point in space spanned by a set of n-vector.
3. Linear independence - A set of n-vectors is said to be linearly independent if the only solution to $c_1\mathbf{v_1} + c_2\mathbf{v_2} + \cdots + c_n\mathbf{v_n} = 0$, for some vectors $\mathbf{v_i} \in \mathbb{R}^n$ and any scalar $c_i \in \mathbb{R}$ is $c_1 = c_2 = \cdots = c_n = 0$.  A linearly independent set of n-vectors does NOT contain the zero vector. 
4. Linear combination - Vectors are linearly combined through scaling and adding them. *i.e* $c_1\mathbf{v_1} + c_2\mathbf{v_2} + \cdots + c_n\mathbf{v_n}$.
5. Norm - ||$\mathbf{v}$|| = $\sqrt{(v_1^2 + v_2^2 + \cdots + v_n^2)}$
###  Key equations
1. Vector addition - Let $\mathbf{u}$ and $\mathbf{v}$ be some n-vector in $\mathbb{R}^n$. The two vectors are added component by component as seen below:
$$\mathbf{u} + \mathbf{v} = 
\begin{pmatrix} 
    u_1\\ u_2\\ \vdots \\ u_n
\end{pmatrix}
+
\begin{pmatrix}
    v_1 \\ v_2\\ \vdots \\ v_n
\end{pmatrix}
=
\begin{pmatrix}
    u_1 + v_1 \\
    u_2 + v_2 \\
    \vdots\\
    u_n + v_n
\end{pmatrix}
$$
2. Scalar multiplication - Let $\mathbf{v}$ be an n-vector and *c* a scalar, the scalar is multiplied by every component in a vector as shown below:
$$
c 
\begin{pmatrix}
    v_1 \\
    v_2 \\
    \vdots \\
    v_n
\end{pmatrix}
=
\begin{pmatrix}
    cv_1 \\
    cv_2 \\
    \vdots \\
    cv_n
\end{pmatrix}
$$

3. Linear independent - A collection of n-vectors is said to be linear independent if all vectors are pointing in different direction, geometrically. Conceptually, those vectors are not redundant and have the following linear combination:
$$
    c_1\mathbf{v_1} + c_2\mathbf{v_2} + \cdots + c_n\mathbf{v_n} = 0 \quad \mid  c_i \in \mathbb{R}\, , \mathbf{v_i} \in \mathbb{R}^n 
$$
Here, $c_1 = c_2 = \cdots = c_n = 0$. If this is true, then the set is said to be linearly independent.

4. Dot product - Dot product of n-vectors $\mathbf{u}$ and $\mathbf{v}$ is computed as:
$$
    \mathbf{u} \cdot \mathbf{v}
    =
    u_1v_1 + u_2v_2 + \cdots + u_nv_n
$$
The result is a scalar, telling us how much of vector $\mathbf{u}$ is pointing to vector $\mathbf{v}$. The dot product is used to compute **cosine similarity** between two vectors.
### Key properties
1. $\mathbf{u}, \mathbf{v} \text{ and } \mathbf{s}$ are some n-vectors in $\mathbf{R}^n$. Vector ADDITION has the following properties:
    - Commutative - $\mathbf{u} + \mathbf{v}$ = $\mathbf{v} + \mathbf{u}$
    - Associative - $(\mathbf{u} + \mathbf{v}) + \mathbf{s} = \mathbf{u} + (\mathbf{v} + \mathbf{s})$
    - Adding a zero vector to a nonzero vector produces no change.
    - Subtracting two identical vectors results to a zero vector.
2. Scalar multiplication has the following properties:
    - Distributive - $(c + w)\mathbf{v} = c\mathbf{v} + w\mathbf{v}$. On left, two scalars are added first then multiplied with a vector while on right, the two scalars are multiplied first with the vector, then summed.
    - Associative - (*c* $\cdot$ *w*) $\mathbf{v}$ = *c*(*w* $\cdot \mathbf{v}$). On the left, there is a scalar to scalar multiplication and scalar-vector multiplication, On right, there are two scalar-vector multiplications.
    - To get a ZERO vector, multiply the vector with a zero scalar.
3. A set of n-vectors is linearly dependent if it contains the zero vector(We will prove this property)
4. A collection of n-vectors forms a basis if:
    - Vectors are linearly independent
    - Spans the entire space. Every vector in the space can be reached.

### Proof
A set of n-vectors is ALWAYS linearly dependent if it contains the zero vector. Here is the proof:

Suppose $S = \{\mathbf{v_1}, \mathbf{v_2}, \mathbf{v_3}, \cdots \mathbf{v_n}\}$ is a set of n-vectors and $\mathbf{v_k} \in S$ is a zero vector.

By definition, for linear independence to hold true, the following equation must be satisfied:
$$
    c_1 \mathbf{v_1} + 
    c_2 \mathbf{v_2} +
    \cdots +
    c_n \mathbf{v_n}
    = \mathbf{0}
$$
for some n-vectors $\mathbf{v_i} \in \mathbb{R}^n$ and any scalar $c_1, c_2, \cdots, c_n \in \mathbb{R}$. It follows that:

$$
    c_1\mathbf{v_1} + 
    c_2 \mathbf{v_2} + 
    \cdots +
    c_k \mathbf{v_k} +
    \cdots + 
    c_n \mathbf{v_n} = 
    \mathbf{0}
$$
Given that $\mathbf{v_K} = \mathbf{0}$, 
$$
    c_1 \mathbf{v_1} + 
    c_2 \mathbf{v_2} + 
    \cdots +
    c_k \mathbf(0) + 
    \cdots +
    c_n \mathbf{v_n}
    = \mathbf{0}
$$
$$
    \implies 0 \mathbf{v_1} + 0 \mathbf{v_2} + \cdots + 1 (\mathbf{0}) + \cdots + 0 \mathbf{v_n} = \mathbf{0} 
$$
A nonzero solution exists, especially $c_k = 1$, therefore by definition, the set $S$ is linearly dependent. $\blacksquare$
### Python implementation
1. Vector definition - Use `np.array()` e.g. `np.array([1, 2])`. Here, NumPy is imported with an alias name **np**. 
2. Vector addition - In Python, vectors are arrays of numbers. We can add them using the `+` symbol. e.g `np.array([1, 3]) + np.array([2, -1])`. Adding them we  get `[4, 2]` as the output.

3.  Scalar multiplication - To scale a vector, you need to multiply an array with some number, in our case what we call a scalar. e.g. `2 * np.array([1, 3])` giving an output `[2, 6]`.

4. Magnitude - To compute magnitude in Python, we use `np.linalg.norm([np.array([1, 3])])`. The resultant output  will be a single number i.e. `3.1623`

5. Linear combination - A linear combination of a set of n-vectors is implemented by adding and scaling arrays. e.g `2 * np.array([1, 2]) + 3 * np.array([3, -1])`. The output is an array, `[11, 1]`.

6. Span - Span give us true dimension of some set of vectors. To know spans, we have to compute the rank i.e `np.linalg.matrix_rank(np.column_stack([np.array([1, 0]), np.array([0, 1])]))`. From the example, we first stack the two vectors together, then compute rank. In this case, rank for a set of basis vector in $\mathbb{R}^2$ is $2$.

7. Linear independence - To compute linear independence, we first need to compute rank, then compare it with total number of stacked vectors or a matrix dimension. If both are equal, then the set is said to be linearly independent. Likewise, if the two: rank and dimension, varies, the set is said to be linearly dependent. Example `np.linalg.matrix_rank(np.column_stack([np.array([1, 2]), np.array([3, 5]), np.array([2, 4])]))`. Here, rank = $2$ and number of vectors present = $3$, therefore, the set 
$$
    S = 
    \left\{
    \begin{pmatrix}
        1 \\ 2
    \end{pmatrix}, 
    \begin{pmatrix}
        3\\ 5
    \end{pmatrix}, 
    \begin{pmatrix}
        2\\ 4
    \end{pmatrix}
    \right\}
$$

is linearly dependent, at least one vector can be expressed as a linear combination of others.

### ML Connection
1. A set of features, a feature matrix, may have redundant entries. Meaning that at least one feature can be expressed as a linear combination of others. This causes *multicollinearity* problem in Machine Learning. As a result, the model weights become unstable, leading to unstable model predictions.
2. In feature normalization, vectors are scaled, either by stretching, flipping, shrink or collapse them completely.
3. Number of basis vectors, gives the true dimension of data.
4. Span of target vector, gives a set of all possible prediction a model can make. 