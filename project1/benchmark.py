import matplotlib.pyplot as plt
import numpy as np
import random
import time

from sort import mergesort, quicksort
from tower_of_hanoi import TowerOfHanoi
from matrix_multiply import matrix_multiply, strassen_multiply, print_matrix


class Graph(object):
    def sorting(self):
        random.seed(0)

        # x and y cooardinates for graphs
        n = [2**(i + 1) for i in range(26)]
        timings_mergesort = []
        timings_quicksort = []

        # headings variables
        heading1 = "n input"
        heading2 = "timings (seconds)"
        pad_size = len(heading1) if len(
            str(n[-1])) < len(heading1) else len(str(n[-1]))
        sep = "-"

        # merge sort benchmark
        print("\nMERGESORT\n")
        print(f"{heading1:<{pad_size}} {heading2}")
        print(f"{sep * len(heading1):<{pad_size}} {sep * len(heading2)}")

        for i in range(len(n)):
            list = [random.randrange(1, n[i], 1) for j in range(n[i])]

            start_time = time.perf_counter()
            mergesort(list)
            end_time = time.perf_counter()

            duration = end_time - start_time
            timings_mergesort.append(duration)

            print(f"{n[i]:<{pad_size}} {duration}")

        # quick sort benchmark
        print("\nQUICKSORT\n")
        print(f"{heading1:<{pad_size}} {heading2}")
        print(f"{sep * len(heading1):<{pad_size}} {sep * len(heading2)}")

        for i in range(len(n)):
            list = [random.randrange(1, n[i], 1) for j in range(n[i])]

            start_time = time.perf_counter()
            quicksort(list)
            end_time = time.perf_counter()

            duration = end_time - start_time
            timings_quicksort.append(duration)

            print(f"{n[i]:<{pad_size}} {duration}")

        # graph results
        plt.plot(n, timings_mergesort, label="Merge Sort")
        plt.plot(n, timings_quicksort, label="Quick Sort")
        plt.xlabel('n input size')
        plt.ylabel('timings in seconds')
        plt.title('Growth Rates: Merge Sort vs Quick Sort')
        plt.legend()  # show legend
        plt.show()

    def tower_of_hanoi(self):
        random.seed(0)

        # x and y cooardinates for graphs
        n = [i + 1 for i in range(32)]
        timings_tof = []

        # headings variables
        heading1 = "n input"
        heading2 = "timings (seconds)"
        pad_size = len(heading1) if len(
            str(n[-1])) < len(heading1) else len(str(n[-1]))
        sep = "-"

        # tower of hanoi benchmark
        print("\nTOWER OF HANOI\n")
        print(f"{heading1:<{pad_size}} {heading2}")
        print(f"{sep * len(heading1):<{pad_size}} {sep * len(heading2)}")

        for i in range(len(n)):
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
        plt.plot(n, timings_tof, label="Tower of Hanoi")
        plt.xlabel('n input size')
        plt.ylabel('timings in seconds')
        plt.title('Growth Rates: Tower of Hanoi')
        plt.legend()  # show legend
        plt.show()

    def matrix_multiplication(self):
        random.seed(0)

        # x and y cooardinates for graphs
        n = [2**(i + 1) for i in range(10)]
        timings_classic = []
        timings_strassen = []

        # headings variables
        heading1 = "n input"
        heading2 = "timings (seconds)"
        pad_size = len(heading1) if len(
            str(n[-1])) < len(heading1) else len(str(n[-1]))
        sep = "-"

        # classic benchmark
        print("\nCLASSIC MATRIX MULTIPLICATION\n")
        print(f"{heading1:<{pad_size}} {heading2}")
        print(f"{sep * len(heading1):<{pad_size}} {sep * len(heading2)}")

        for i in range(len(n)):
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
        print("\nSTRASSEN MATRIX MULTIPLICATION\n")
        print(f"{heading1:<{pad_size}} {heading2}")
        print(f"{sep * len(heading1):<{pad_size}} {sep * len(heading2)}")

        for i in range(len(n)):
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
        plt.plot(n, timings_classic, label="Classic Matrix Multiplication")
        plt.plot(n, timings_strassen, label="Strassen Matrix Multiplication")
        plt.xlabel('n input size')
        plt.ylabel('timings in seconds')
        plt.title('Growth Rates: Classic vs Strassen Matrix Multiplication')
        plt.legend()  # show legend
        plt.show()


if __name__ == "__main__":
    menu = "\nWhich graph to test?\n"\
        "1: Sorting\n"\
        "2: Tower of Hanoi\n"\
        "3: Matrix Multiplication\n"\
        "X: exit\n"
    choice = ""

    while(choice != "X" and choice != "x"):
        print(menu)
        choice = input()

        if(choice == "1"):
            Graph().sorting()
        elif(choice == "2"):
            Graph().tower_of_hanoi()
        elif (choice == "3"):
            Graph().matrix_multiplication()
        elif(choice == "X" or choice == "x"):
            print("Exiting...")
        else:
            print("Invalid choice")
