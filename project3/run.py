"""
Project 3

- Sudoku: Backtracking
- 0-1 Knapsack: Branch and bound
- Traveling Salesman: Branch and bound
"""
import time
import threading

from knapsack import knapsack, KnapsackItem, knapsack_debug
from sudoku import Sudoku
from traveling_salesman import traveling_salesman


class SudokuRun(object):
    def __init__(self):
        self.is_solving = True

    def print_solving(self):
        self.is_solving = True
        timeout = 300
        count = 0

        while self.is_solving and count < timeout:
            n = 5
            for x in range(n):
                if not self.is_solving:
                    print(" " * 20, end="\r")
                    return

                b = "Solving" + "." * x + " " * n
                print(b, end="\r")
                time.sleep(1)
                count += 1

    def start(self):
        print("\nSUDOKU\n------\n")

        board = get_2d_array_input("input_sudoku.txt")

        sudoku = Sudoku()
        sudoku.setboard(board)

        print("\nBoard")
        sudoku.print()

        print()
        print_solving = threading.Thread(target=self.print_solving)
        print_solving.start()

        try:
            is_solved = sudoku.solve()
            self.is_solving = False

            if is_solved:
                print("Solution  ")
                sudoku.print()
            else:
                print("Invalid board")
        except KeyboardInterrupt:
            print("Interrupted")
            self.is_solving = False

        print_solving.join()


class KnapsackRun(object):
    def __init__(self):
        self.capacity = 0
        self.items = []

    def start(self):
        print("\nKNAPSACK\n--------\n")

        self.get_knapsack_input("input_knapsack.txt")

        result = knapsack_debug(self.items, self.capacity)

    def get_knapsack_input(self, filename):
        self.capacity = int(input("Enter capacity: "))

        data = get_2d_array_input("input_knapsack.txt")
        profits, weights = data[0], data[1]

        for i in range(len(weights)):
            self.items.append(KnapsackItem(
                len(self.items)+1, weights[i], profits[i]))


class TravelingSalesmanRun(object):
    def start(self):
        print("\nTRAVELING SALESMAN\n------------------\n")

        adjacency = get_2d_array_input("input_salesman.txt")

        print("\nAdjacency Matrix")
        print_matrix(adjacency)

        result = traveling_salesman(adjacency)
        print(f"\nShortest path: {result['path']}")
        print(f"Length: {result['length']}")


def get_2d_array_input(filename):
    array = []

    print(f"Reading data from {filename}")
    with open(filename) as file:
        for line in file:
            if line:
                array.append([int(i) for i in line.split()])

    return array


def print_matrix(A, pad_size=3, sep=" ", end="\n"):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f"{(A[i][j]):>{pad_size}}", end=sep)
        if i == len(A) - 1:
            print(end, end="")
        else:
            print()


if __name__ == "__main__":

    menu = "\nWhich task?\n"\
        "1: Sudoku\n"\
        "2: 0-1 Knapsack\n"\
        "3: Traveling Salesman\n"\
        "X: Exit"
    print(menu)

    while True:
        choice = input("> ")

        if choice == "X" or choice == "x":
            break
        elif choice == "1":
            SudokuRun().start()
        elif choice == "2":
            KnapsackRun().start()
        elif choice == "3":
            TravelingSalesmanRun().start()
        else:
            continue

        print(menu)
