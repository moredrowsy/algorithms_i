"""
All unit tests
"""
import unittest
from tests import knapsack, sudoku, traveling_salesman


MODULES = [
    knapsack,
    traveling_salesman,
    sudoku
]


class Test(unittest.TestCase):
    """
    Run all tests
    """
    for module in MODULES:
        suite = unittest.TestLoader().loadTestsFromModule(module)
        unittest.TextTestRunner(verbosity=2).run(suite)
