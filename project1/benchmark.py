"""
Benchmark program
"""
import matplotlib.pyplot as plt
import random
import time

from sort import mergesort, quicksort
from tower_of_hanoi import TowerOfHanoi
from matrix_multiply import matrix_multiply, strassen_multiply, print_matrix


class Benchmark(object):
    """
    Benchmark class:
        - Sorting benchmark
        - Tower of Hanoi benchmark
        - Matrix multiplication benchmark
    """
    random.seed(0)

    def run(self, choice=-1):
        """
        Run benchmark function by choice option and show graph(s)

        Parameters
        ----------
        choice (int): Benchmark number. -1 to run all benchmarks.

        Return
        ------
        False if invalid choice, else True.
        """
        # array of benchmark methods
        benchmarks = [self.sorting, self.tower_of_hanoi,
                      self.matrix_multiplication]

        # try to convert choice to int
        try:
            choice = int(choice)
        except:
            choice = -1 if choice == "A" or choice == "a" else 0

        # run benchmark methods
        if(choice == -1):
            for i in range(len(benchmarks)):
                benchmarks[i](i + 1)
        elif(choice >= 1 and choice <= len(benchmarks)):
            benchmarks[choice-1](choice)
        else:
            return False

        # show graph and close afterwards
        plt.show()
        plt.close("all")

        return True

    def sorting(self, fig=1):
        """
        Benchmarks sorting functions

        Parameters
        ----------
        fig (int): Figure number for plot
        """
        sample_size = 26

        # x and y cooardinates for graphs
        n = [2**(i + 1) for i in range(sample_size)]
        timings_mergesort = []
        timings_quicksort = []

        # headings variables
        heading1 = "n input"
        heading2 = "timings (seconds)"
        pad_size = len(heading1) if len(
            str(n[-1])) < len(heading1) else len(str(n[-1]))
        sep = "-"

        # merge sort benchmark
        print("\nMERGESORT\n\n"
              f"{heading1:<{pad_size}} {heading2}\n"
              f"{sep * pad_size:<{pad_size}} {sep * len(heading2)}")

        for i in range(sample_size):
            list = [random.randrange(1, n[i], 1) for j in range(n[i])]

            start_time = time.perf_counter()
            mergesort(list)
            end_time = time.perf_counter()

            duration = end_time - start_time
            timings_mergesort.append(duration)

            print(f"{n[i]:<{pad_size}} {duration}")

        # quick sort benchmark
        print("\nQUICKSORT\n\n"
              f"{heading1:<{pad_size}} {heading2}\n"
              f"{sep * pad_size:<{pad_size}} {sep * len(heading2)}")

        for i in range(sample_size):
            list = [random.randrange(1, n[i], 1) for j in range(n[i])]

            start_time = time.perf_counter()
            quicksort(list)
            end_time = time.perf_counter()

            duration = end_time - start_time
            timings_quicksort.append(duration)

            print(f"{n[i]:<{pad_size}} {duration}")

        # graph results
        plt.figure(fig)
        plt.plot(n, timings_mergesort, label="Merge Sort")
        plt.plot(n, timings_quicksort, label="Quick Sort")
        plt.xlabel('n input size')
        plt.ylabel('timings in seconds')
        plt.title('Growth Rates: Merge Sort vs Quick Sort')
        plt.legend()  # show legend

    def tower_of_hanoi(self, fig=2):
        """
        Benchmarks tower of hanoi problem

        Parameters
        ----------
        fig (int): Figure number for plot
        """
        sample_size = 32

        # x and y cooardinates for graphs
        n = [i + 1 for i in range(sample_size)]
        timings_tof = []

        # headings variables
        heading1 = "n input"
        heading2 = "timings (seconds)"
        pad_size = len(heading1) if len(
            str(n[-1])) < len(heading1) else len(str(n[-1]))
        sep = "-"

        # tower of hanoi benchmark
        print("\nTOWER OF HANOI\n\n"
              f"{heading1:<{pad_size}} {heading2}\n"
              f"{sep * pad_size:<{pad_size}} {sep * len(heading2)}")

        for i in range(sample_size):
            A = [j for j in range(n[i], 0, -1)]
            B = []
            C = []
            tof = TowerOfHanoi(A, B, C, "A", "B", "C")

            start_time = time.perf_counter()
            tof.solve(display=False)
            end_time = time.perf_counter()

            duration = end_time - start_time
            timings_tof.append(duration)

            print(f"{n[i]:<{pad_size}} {duration}")

        # graph results
        plt.figure(fig)
        plt.plot(n, timings_tof, label="Tower of Hanoi")
        plt.xlabel('n input size')
        plt.ylabel('timings in seconds')
        plt.title('Growth Rates: Tower of Hanoi')
        plt.legend()  # show legend

    def matrix_multiplication(self, fig=3):
        """
        Benchmarks matrix multiplication

        Parameters
        ----------
        fig (int): Figure number for plot
        """
        sample_size = 10

        # x and y cooardinates for graphs
        n = [2**(i + 1) for i in range(sample_size)]
        timings_classic = []
        timings_strassen = []

        # headings variables
        heading1 = "n input"
        heading2 = "timings (seconds)"
        pad_size = len(heading1) if len(
            str(n[-1])) < len(heading1) else len(str(n[-1]))
        sep = "-"

        # classic benchmark
        print("\nCLASSIC MATRIX MULTIPLICATION\n\n"
              f"{heading1:<{pad_size}} {heading2}\n"
              f"{sep * pad_size:<{pad_size}} {sep * len(heading2)}")

        for i in range(sample_size):
            A = [[random.randrange(1, n[i], 1)
                  for k in range(n[i])] for j in range(n[i])]
            B = [[random.randrange(1, n[i], 1)
                  for k in range(n[i])] for j in range(n[i])]

            start_time = time.perf_counter()
            C = matrix_multiply(A, B)
            end_time = time.perf_counter()

            duration = end_time - start_time
            timings_classic.append(duration)

            print(f"{n[i]:<{pad_size}} {duration}")

        # strassen benchmark
        print("\nSTRASSEN MATRIX MULTIPLICATION\n\n"
              f"{heading1:<{pad_size}} {heading2}\n"
              f"{sep * pad_size:<{pad_size}} {sep * len(heading2)}")

        for i in range(sample_size):
            A = [[random.randrange(1, n[i], 1)
                  for k in range(n[i])] for j in range(n[i])]
            B = [[random.randrange(1, n[i], 1)
                  for k in range(n[i])] for j in range(n[i])]

            start_time = time.perf_counter()
            C = strassen_multiply(A, B)
            end_time = time.perf_counter()

            duration = end_time - start_time
            timings_strassen.append(duration)

            print(f"{n[i]:<{pad_size}} {duration}")

        # graph results
        plt.figure(fig)
        plt.plot(n, timings_classic, label="Classic Matrix Multiplication")
        plt.plot(n, timings_strassen, label="Strassen Matrix Multiplication")
        plt.xlabel('n input size')
        plt.ylabel('timings in seconds')
        plt.title('Growth Rates: Classic vs Strassen Matrix Multiplication')
        plt.legend()  # show legend


if __name__ == "__main__":
    menu = "\nWhich task to benchmark?\n"\
        "1: Sorting\n"\
        "2: Tower of Hanoi\n"\
        "3: Matrix Multiplication\n"\
        "A: Run all benchmarks\n"\
        "X: Exit\n"

    while(True):
        print(menu)
        choice = input()

        if(choice != "X" and choice != "x"):
            # run benchmark with choice number
            valid = Benchmark().run(choice)

            if(not valid):
                print("Invalid choice")
        else:
            break

    print("Exiting benchmark...")
