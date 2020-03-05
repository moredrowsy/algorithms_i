"""
All unit tests
"""
import unittest
from tests import sort, tower_of_hanoi, matrix_multiply


MODULES = [
    sort, tower_of_hanoi, matrix_multiply
]


class Test(unittest.TestCase):
    """
    Run all tests
    """
    for module in MODULES:
        suite = unittest.TestLoader().loadTestsFromModule(module)
        unittest.TextTestRunner(verbosity=2).run(suite)
