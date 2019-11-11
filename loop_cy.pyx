"""
cpdef int some_loop(int x) means we are declaring a function called some_loop
cpdef -> the function can be used in both python and cython code.
int some_loop(int x) -> the function takes an integer as a parameter and it returns an integer value
"""
cpdef int some_loop(int x):
    # the following lines declare variables used in the loop.
    # this is very important in speeding up the application because of the dynamic nature of Python
    cdef int z = 0
    cdef int i
    cdef int j
    for i in range(x):
        for j in range(100):
            z += i * j * x
        return z
