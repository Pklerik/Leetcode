def factorial(n):
    if n < 1 :return
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
    

import timeit
print(timeit.timeit('factorial(984)', globals=globals(), number=1) * 100000)