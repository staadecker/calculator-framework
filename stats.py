import math
from formula_prog import FormulaSet
from scipy.stats import norm
from typing import Optional

"""
Stats class contains all the functions that this program offers. Namely,

mean, median, sample_variance, sample_std (sample standard deviation) and sort.

These methods are very straight forward, they take in a list and return the result.
"""


class Stats:
    @staticmethod
    def mean(x):
        return sum(x) / len(x)

    @staticmethod
    def median(x):
        x = sorted(x)
        n = len(x)
        if n % 2 == 0:
            return (x[n // 2 - 1] + x[n // 2]) / 2
        else:
            return x[n // 2]

    @staticmethod
    def sample_variance(x):
        n = len(x)
        mean = Stats.mean(x)
        s = 0
        for e in x:
            s += (e - mean) ** 2
        return s / (n - 1)

    @staticmethod
    def sample_std(x):
        return math.sqrt(Stats.sample_variance(x))

    @staticmethod
    def sort(x):
        return sorted(x)

    @staticmethod
    def _description_binomial_dist():
        return ("x", int), ("n", int), ("p", float)

    @staticmethod
    def binomial_dist(x, n, p):
        return math.comb(n, x) * (p ** x) * ((1 - p) ** (n - x))

    @staticmethod
    def _description_binomial_dist_cuml():
        return ("x", int), ("n", int), ("p", float)

    @staticmethod
    def binomial_dist_cuml(x, n, p):
        return sum([Stats.binomial_dist(i, n, p) for i in range(0, x + 1)])

    @staticmethod
    def _description_hypergeo_dist():
        return ("x", int), ("N", int), ("n", int), ("k", int)

    @staticmethod
    def hypergeo_dist(x, N, n, k):
        return math.comb(k, x) * math.comb(N - k, n - x) / math.comb(N, n)

    @staticmethod
    def _description_inv_binomial():
        return ("x", int), ("k", int), ("p", float)

    @staticmethod
    def inv_binomial(x, k, p):
        return math.comb(x - 1, k - 1) * (p ** k) * ((1 - p) ** (x - k))

    @staticmethod
    def _description_poisson_dist():
        return ("x", int), ("mu", float)

    @staticmethod
    def poisson_dist(x, m):
        return math.exp(-m) * (m ** x) / math.factorial(x)

    @staticmethod
    def _description_poisson_dist_cuml():
        return ("x", int), ("mu", float)

    @staticmethod
    def poisson_dist_cuml(x, m):
        return sum([Stats.poisson_dist(i, m) for i in range(0, x + 1)])

    @staticmethod
    def _description_std_normal_dist_cuml():
        return {
            "inputs": [
                {
                    "name": "z_lower",
                    "parse": float,
                    "optional": True
                }, {
                    "name": "z_upper",
                    "parse": float,
                    "optional": True
                }
            ]
        }

    @staticmethod
    def std_normal_dist_cuml(z_low, z_end):
        if z_low is None and z_end is None:
            print("Invalid input.")
            return
        if z_low is None:
            return norm.cdf(z_end)
        if z_end is None:
            return 1-norm.cdf(z_low)
        return norm.cdf(z_end) - norm.cdf(z_low)


if __name__ == "__main__":
    formula_set = FormulaSet(Stats, except_many_functions=True)
    formula_set.run()
