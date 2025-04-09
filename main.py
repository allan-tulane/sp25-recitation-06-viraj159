def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1, counts) + fib_recursive(n - 2, counts)
    

    
def fib_top_down(n, fibs):
    ###TODO
    pass


def fib_bottom_up(n):
    ###TODO
    pass




