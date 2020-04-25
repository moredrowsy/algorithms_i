"""
Project 3

- Sudoku: Backtracking
- 0-1 Knapsack: Branch and bound
- Traveling Salesman: Branch and bound
"""
import time
import threading

from knapsack import knapsack, KnapsackItem
from sudoku import Sudoku
from traveling_salesman import traveling_salesman


class Run(object):
    """
    Run project 3's tasks
    """

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

    def sudoku_puzzle(self):
        print("\nSUDOKU\n------")

        _ = Sudoku.empty
        sudoku = Sudoku()

        # problem 1
        board = [
            [3, _, 4, _],
            [_, 2, _, 3],
            [_, _, _, _],
            [_, 4, _, 1],
        ]

        sudoku.setboard(board)

        print("\nBoard")
        sudoku.print()

        print()
        print_solving = threading.Thread(target=self.print_solving)
        print_solving.start()

        if sudoku.solve():
            print("Solution  ")
            sudoku.print()
        else:
            print("Invalid board")

        self.is_solving = False
        print_solving.join()

        # problem 2
        board = [
            [_, _, _, _, _, _, 2, _, _],
            [_, 8, _, _, _, 7, _, 9, _],
            [6, _, 2, _, _, _, 5, _, _],
            [_, 7, _, _, 6, _, _, _, _],
            [_, _, _, 9, _, 1, _, _, _],
            [_, _, _, _, 2, _, _, 4, _],
            [_, _, 5, _, _, _, 6, _, 3],
            [_, 9, _, 4, _, _, _, 7, _],
            [_, _, 6, _, _, _, _, _, _]
        ]

        sudoku.setboard(board)

        print("\nBoard")
        sudoku.print()

        print()
        print_solving = threading.Thread(target=self.print_solving)
        print_solving.start()

        if sudoku.solve():
            print("Solution  ")
            sudoku.print()
        else:
            print("Invalid board")

        self.is_solving = False
        print_solving.join()

    def knapsack_problem(self):
        print("\nKNAPSACK\n--------")

        # problem 1
        items = [
            KnapsackItem(1, 2, 40),
            KnapsackItem(2, 5, 30),
            KnapsackItem(3, 10, 50),
            KnapsackItem(4, 5, 10)
        ]
        capacity = 16
        result = knapsack(items, capacity)
        print(f"\nProfit: {result['profit']} at capacity: {capacity}")
        print("Knapsack")
        print(result['knapsack'])

        # problem 2
        items = [
            KnapsackItem(1, 5, 35),
            KnapsackItem(2, 4, 16),
            KnapsackItem(3, 7, 42),
            KnapsackItem(4, 3, 9)
        ]
        capacity = 14
        result = knapsack(items, capacity)
        print(f"\nProfit: {result['profit']} at capacity: {capacity}")
        print("Knapsack")
        print(result['knapsack'])

    def travelingsalesman(self):
        print("\nTRAVELING SALESMAN\n------------------")

        # problem 1
        adj = [
            [0, 14, 4, 10, 20],
            [14, 0, 7, 8, 7],
            [4, 5, 0, 7, 16],
            [11, 7, 9, 0, 2],
            [18, 7, 17, 4, 0]
        ]

        print("\nAdjacency Matrix")
        print_matrix(adj)

        result = traveling_salesman(adj)
        print(f"\nShortest path: {result['path']}")
        print(f"Length: {result['length']}")

        # problem 2
        adj = [
            [0, 20, 30, 10, 1],
            [15, 0, 16, 4, 2],
            [3, 5, 0, 2, 4],
            [19, 6, 18, 0, 3],
            [16, 4, 7, 16, 0]
        ]

        print("\nAdjacency Matrix")
        print_matrix(adj)

        result = traveling_salesman(adj)
        print(f"\nShortest path: {result['path']}")
        print(f"Length: {result['length']}")

        # problem 3
        adj = [
            [0, 10, 15, 20],
            [10, 0, 35, 25],
            [15, 35, 0, 30],
            [20, 25, 30, 0]
        ]

        print("\nAdjacency Matrix")
        print_matrix(adj)

        result = traveling_salesman(adj)
        print(f"\nShortest path: {result['path']}")
        print(f"Length: {result['length']}")


def print_matrix(A, pad_size=3, sep=" ", end="\n"):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f"{(A[i][j]):>{pad_size}}", end=sep)
        if i == len(A) - 1:
            print(end, end="")
        else:
            print()


if __name__ == "__main__":
    # Run().sudoku_puzzle()
    Run().knapsack_problem()
    Run().travelingsalesman()
