# CMPS 2200 Recitation 06
## Answers

**Name:**Viraj Choksi
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2) The recursive implementation of the Fibonacci function makes two recursive calls for each non-base input: one to compute fib_recursive(n-1, counts) and one to compute fib_recursive(n-2, counts). Therefore, the total work T(n) done by the algorithm satisfies the recurrence T(n) = T(n-1) + T(n-2), with base cases T(0) = T(1) = 1. This is the same recurrence as the Fibonacci sequence itself, so the number of calls (and thus the total work) grows exponentially. Specifically, T(n) equals the (n+1)th Fibonacci number. This implies the work is approximately proportional to phi^n, where phi = (1 + sqrt(5)) / 2, which is about 1.618. Therefore, the work of the recursive algorithm is Theta(phi^n), which is exponential in n.

- **3) Since the algorithm makes two recursive calls for each n > 1 — one to fib_recursive(n-1, counts) and one to fib_recursive(n-2, counts) — and these calls can theoretically run in parallel, the span only grows based on the longer of the two. Therefore, the span S(n) satisfies the recurrence S(n) = S(n-1) + O(1), with base cases S(0) = S(1) = O(1). This recurrence solves to S(n) = O(n), meaning the span grows linearly with n. This means this algorithm is highly parallelizable.

- **4) When inspecting the counts list after running fib_recursive(n, counts), an interesting pattern emerges: the number of times each Fibonacci number i is computed corresponds to the (n−i)th Fibonacci number. In other words, counts[i] is equal to the number of times fib_recursive(i, counts) was called, and this value is equal to Fibonacci(n−i+1). This pattern reflects the recursive structure of the algorithm, where smaller Fibonacci values are recomputed many times. For example, when computing fib_recursive(5), the number of times fib_recursive(0) is called is equal to F(6), the number of times fib_recursive(1) is called is F(5), and so on, decreasing as i increases. 

- **6) In the fib_top_down algorithm, each value fib_top_down(i) is computed at most once for any i from 0 to n. This is because once a value F_i is computed, it is stored in the fibs list and reused in future calls. Therefore, the maximum number of times fib_top_down(i) is called for any value i is 1. As a result, the work of the algorithm is O(n), since we compute each Fibonacci number from 0 to n exactly once, and each computation takes constant time after recursive calls are resolved. The span of the algorithm is O(n) as well, because the recursive calls depend on the results of smaller values, and fib_top_down(n) calls fib_top_down(n-1) and fib_top_down(n-2). So the longest chain of dependent computations is linear in n.

- **8) In the fib_bottom_up algorithm, each value F_i is computed once and read at most twice: once when used to compute F_{i+1} and again when computing F_{i+2}. This is because each Fibonacci number is calculated using the two immediately previous values. Therefore, the maximum number of times that any F_i is read is 2. Thus, the work of the algorithm is O(n), since the loop runs from 2 to n, and each step performs a constant amount of work. The span is also O(n), because each step depends on the results of previous steps. There is a chain of dependencies that grows linearly, so the longest sequence of dependent operations is of length n.
