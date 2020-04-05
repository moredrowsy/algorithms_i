"""
All unit tests
"""
import unittest
from tests import binomial_coefficient, floyd


MODULES = [
    binomial_coefficient,
    floyd
]


class Test(unittest.TestCase):
    """
    Run all tests
    """
    for module in MODULES:
        suite = unittest.TestLoader().loadTestsFromModule(module)
        unittest.TextTestRunner(verbosity=2).run(suite)
