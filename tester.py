"""
timeit is an inbuilt python library to check the time taken to run a code snippet
tabulate is a python library to display data in a tabular form
For more info on how to install tabulate check -> https://pypi.org/project/tabulate/
"""

import timeit

from tabulate import tabulate  # install this in your virtual env

no_tests = 10000  # we are going to run 10,000 tests
total_time_python = 0
total_time_cython = 0


for i in range(no_tests):
    # In each loop, we are calling the some_loop function with 500 passed
    # We then run that function 100 times (number)
    # We then add the time taken to run the tests to the cumulators defined above
    total_time_python += timeit.timeit('some_loop(5000)',
                                       number=100, setup='from loop_py import some_loop')
    # testing the cython code. Note the importation part -> we are importing from loop_cy.
    # this is because our cython code in loop_cy.pyx was compiled into loop_cy
    total_time_cython += timeit.timeit('some_loop(5000)',
                                       number=100, setup='from loop_cy import some_loop')

#  after looping get the average time taken in each loop
avg_python = total_time_python / no_tests
avg_cython = total_time_cython / no_tests

# prepare data to be displayed by tabulate
headers = ["Language", "Total Time (sec)", "Avg Time (sec)"]

python_stats = ["Python", total_time_python, avg_python]
cython_stats = ["Cython", total_time_cython, avg_cython]


all_stats = [python_stats, cython_stats]
tabulated_data = tabulate(all_stats, headers=headers)
print(tabulated_data)

# how does cython perform in comparison to python
performance = avg_python / avg_cython

print("\n-----------------------------------------------")
print(f"Cython is {performance} faster than Python!")
