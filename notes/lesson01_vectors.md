# Linear Algebra Mastery
## Vectors and Vectors Operations
> A vector is an ordered list of finite numbers that has both magnitude and direction. A vector is writen using a small bold italic type font. Coefficient of a vector is writen with italic, small but NOT bold letters.

### Key definitions
1. Span - A span is a set of all linear combination for a set of n-vectors.
2. Basis - This is a set of linearly independent vectors, that spans the entire space. With basis, you can reach every point in space spanned by a set of n-vector.
3. Linear independence - A set of n-vectors is said to be linearly independent if $c_1\mathbf{v_1} + c_2\mathbf{v_2} + \cdots + c_n\mathbf{v_n} = 0$, for some vectors $\mathbf{v_i} \in \mathbb{R}^n$ and any scalar $c_i \in \mathbb{R}$. The scalars $c_i$, are all equal to zero.  A linearly independent set of n-vectors does NOT contain the zero vector. 
4. Linear combination - Vectors are linearly combined through scalling and adding them. *i.e* $c_1\mathbf{v1} + c_2\mathbf{v_2} + \cdots + c_n\mathbf{v_n}$.
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
    u_1v_1 + u2v_2 + \cdots + u_nv_n
$$
The result is a scalar, telling us how much of vector $\mathbf{u}$ is pointing to vector $\mathbf{v}$. The dot product is used to compute **cosine similarity** between two vectors.
### Key properties
1. $\mathbf{u}, \mathbf{v} \text{ and } \mathbf{s}$ are some n-vectors in $\mathbf{R}^n$. Vector ADDITION has the following properties:
    - Commutative - $\mathbf{u} + \mathbf{v}$ = $\mathbf{v} + \mathbf{u}$
    - Assosiative - $(\mathbf{u} + \mathbf{v})\mathbf{s} = \mathbf{u}(\mathbf{v} + \mathbf{s})$
    - Adding a zero vector to a nonozero vector has change.
    - Subtracting two identical vectors results to a zero vector.
2. Scalar multiplication has the following properities:
    - Commutative - $(c + w)\mathbf{v} = c\mathbf{v} + w\mathbf{v}$. On left, two scalars are added first then multiplied with a vector while on right, the two scalars are multiplied firt with the vector, then summed.
    - Assosiative - (*c* $\cdot$ *w*) $\mathbf{v}$ = *c*(*w* $\cdot \mathbf{v}$). On the left, there is a scalar to scalar multiplication and scalar vector multiplication, On right, there are two scalar vector multiplication.
    - To get a ZERO vector, multiply the vector with a zero scalar.
3. A set of n-vectors is linearly dependent if it contains the zero vector(We will proof this property)
4. A collection of n-vectors forms a basis if:
    - Vectors are linearly independent
    - Spans the entire space. Every vector in the space can be reached.

### Proof

### Python implementation

### ML Connection