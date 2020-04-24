"""
Project 3

- FSudoku
"""
import time
import threading

from sudoku import Sudoku
from knapsack import knapsack, KnapsackItem


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
        print(f"\nProfit: {result['profit']}")
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
        print(f"\nProfit: {result['profit']}")
        print("Knapsack")
        print(result['knapsack'])


if __name__ == "__main__":
    Run().sudoku_puzzle()
    Run().knapsack_problem()
