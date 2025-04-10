# CMPS 2200 Recitation 06
## Answers

**Name:**Viraj Choksi
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2) The recursive implementation of the Fibonacci function makes two recursive calls for each non-base input: one to compute fib_recursive(n-1, counts) and one to compute fib_recursive(n-2, counts). Therefore, the total work T(n) done by the algorithm satisfies the recurrence T(n) = T(n-1) + T(n-2), with base cases T(0) = T(1) = 1. This is the same recurrence as the Fibonacci sequence itself, so the number of calls (and thus the total work) grows exponentially. Specifically, T(n) equals the (n+1)th Fibonacci number. This implies the work is approximately proportional to phi^n, where phi = (1 + sqrt(5)) / 2, which is about 1.618. Therefore, the work of the recursive algorithm is Theta(phi^n), which is exponential in n.

- **3) Since the algorithm makes two recursive calls for each n > 1 — one to fib_recursive(n-1, counts) and one to fib_recursive(n-2, counts) — and these calls can theoretically run in parallel, the span only grows based on the longer of the two. Therefore, the span S(n) satisfies the recurrence S(n) = S(n-1) + O(1), with base cases S(0) = S(1) = O(1). This recurrence solves to S(n) = O(n), meaning the span grows linearly with n. This means this algorithm is highly parallelizable.

- **4) When inspecting the counts list after running fib_recursive(n, counts), an interesting pattern emerges: the number of times each Fibonacci number i is computed corresponds to the (n−i)th Fibonacci number. In other words, counts[i] is equal to the number of times fib_recursive(i, counts) was called, and this value is equal to Fibonacci(n−i+1). This pattern reflects the recursive structure of the algorithm, where smaller Fibonacci values are recomputed many times. For example, when computing fib_recursive(5), the number of times fib_recursive(0) is called is equal to F(6), the number of times fib_recursive(1) is called is F(5), and so on, decreasing as i increases. 

- **6)**

- **8)**
