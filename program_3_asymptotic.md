```python
def quick_select(array, k):
    # Handle base cases
    if len(array) == 1:
        return array[0]
    elif k < 1 or k > len(array):
        raise ValueError("Invalid value for k")

    # Randomly select a pivot element
    pivot_index = random.randint(0, len(array) - 1)
    pivot = array[pivot_index]

    # Partition the array around the pivot
    left, right = partition(array, pivot)

    # Determine the position of the k-th smallest element relative to the pivot
    left_len = len(left)
    if k <= left_len:
        return quick_select(left, k)
    elif k == left_len + 1:
        return pivot
    else:
        return quick_select(right, k - left_len - 1)


def partition(array, pivot):
    left, right = [], []
    for num in array:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
    return left, right
```


## Exact Analysis
Examining the algorithm, split the process into:
1. $D(n)$, the time complexity of the *divide* step,
2. $aT(\frac{n}{b})$ for constants $a, b \in \mathbb{R}^+$, or the time complexity of the *conquer* step, and
3. $C(n)$, the time complexity of the *combine* step. 

The *divide* step is implemented through the `partition` subroutine. It's trivial to see that $D(n)\in O(n)$, as the function iterates once through a single array. Performing exact analysis, we obtain:
$$
\begin{align}
D(n) &= 3+n(1 + \hat{b} + (1-\hat{b})(1+\hat{c})) \\
&= 3+n(2+\hat{c} -\hat{b}\hat{c})
\end{align}
$$
where 
$$
\hat{b} = \begin{cases} 
1 & \text{ num } < \text{ pivot } \\
0 & \text{ otherwise }
\end{cases}
$$
and 
$$
\hat{c} = \begin{cases}
1 & \text{ num } > \text{ pivot } \\
0 & \text{ otherwise }
\end{cases}
$$

For this particular problem, we have the following assumption: "You may assume that the random pivot divides the elements in half each time". Therefore, we express the recurrence portion as $(a)T(\frac{n}{2})$, with $a=1$ as only one subproblem is computed out of the two partitions. 

Finally, performing exact analysis given $D(n)3+n(1 + \hat{b} + (1-\hat{b})(1+\hat{c}))$ and $aT\left( \frac{n}{b} \right) = T(\frac{n}{2})$, we find the following for our final algorithm:
$$
\begin{align} 
T(n) &= 1 + \hat{d} + (1-\hat{d})(1+\hat{e}) + 2 +3 + n(2 + \hat{c} - \hat{b}\hat{c}) + T\left( \frac{n}{2} \right) \\
\end{align}
$$
where 
$$
\hat{d} = \begin{cases}
1 & \text{n }  = 1 \\
0 & \text{ otherwise }
\end{cases}
$$
and 
$$
\hat{e} = \begin{cases}
0 & 1 \leq \text{ k } \leq n \\
1 & \text{otherwise}
\end{cases}
$$

Simplifying for worst possible cases, i.e. $\hat{b}=0$, $\hat{c}= 1$, $\hat{d} = 0$, and $\hat{e} = 1$, we find:
$$
T(n) \leq T\left(\frac{n}{2}\right)+3n+8
$$
## Closed Form
For $T(n)$, 
- $a=1$
- $b=2$
- $f(n) = 3n+8$
- $n^{\log _{b} a} = n^0 = 1$

Choose $\epsilon=1$, and assume: 
$$
3n+8 \in \Omega(n^{0+1}) \to f(n) \in \Omega(n)
$$
It follows that
$$
cn \le 3n+8
$$
Set $c=1$:
$$
\begin{align}
n &\le 3n+8 \\
1 &\le 3 + \frac{8}{n} \\
\lim_{ n \to \infty }& \left( 1 \le 3 + \frac{8}{n} \right) = 1 \le 3
\end{align}
$$
This is true for sufficiently large $n$ (really all $n$).  

Next, choose $\delta = \frac{2}{3}$. 
$$
\begin{align}
af\left( \frac{n}{b} \right) = \frac{3}{2}n+8 &\leq  \delta (3n+8) \leq 2n + \frac{16}{3} \\
3n+16 &\leq 4n + \frac{32}{3} \\
3 + \frac{16}{n} &\leq 4+\frac{32}{3n} \\
\lim_{ n \to \infty } &= 3 \leq 4
\end{align}
$$
This is true for sufficiently large $n$. 

So, there exists $\epsilon > 0$ and $\delta <1$ such that $f(n)\in \Omega(n^{\log_{b} a+\epsilon})$ and $af(\frac{n}{b}) \leq \delta f(n)$ for sufficiently large $n$.  Therefore, $T(n)\in \Theta(f(n))$. 


