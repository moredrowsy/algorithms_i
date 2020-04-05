"""
Dynamic Algorithms
"""
from binomial_coefficient import binomial_coefficient


class Run(object):
    """
    Run Dynamic Algorithm's methods
    """

    def binomial(self):
        """Run Binomial Coefficient algorithm"""
        n, k = 4, 2
        coefficient = binomial_coefficient(n, k)
        print(f"Binomial Coefficient\nC[{n}][{k}] = {coefficient}")


if __name__ == "__main__":
    Run().binomial()
