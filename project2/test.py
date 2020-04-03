"""
All unit tests
"""
import unittest
from tests import fractional_knapsack


MODULES = [
    fractional_knapsack
]


class Test(unittest.TestCase):
    """
    Run all tests
    """
    for module in MODULES:
        suite = unittest.TestLoader().loadTestsFromModule(module)
        unittest.TextTestRunner(verbosity=2).run(suite)
