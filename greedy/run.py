"""
Greedy Approach Algorithms
"""
import heapq
import sys


from dijkstra import dijkstra, print_dijkstra_path
from huffman import huffman_tree, HuffmanNode
from prim import prim
from schedule_deadline import schedule_deadline, Job


class Run(object):
    """
    Run Greedy Algorithm's methods
    """

    def prim_algorithm(self):
        """Run Prim's Algorithm on various problems"""
        INF = sys.maxsize
        # problem 1
        weights = [
            [0, 1, 3, INF, INF],
            [1, 0, 3, 6, INF],
            [3, 3, 0, 4, 2],
            [INF, 6, 4, 0, 5],
            [INF, INF, 2, 5, 0],
        ]

        print(f"\nWeights matrix:")
        for i in range(len(weights)):
            for j in range(len(weights[i])):
                if weights[i][j] == INF:
                    print("INF", end=" ")
                else:
                    print(f"{weights[i][j]}", end=" ")

            print()

        start_vertex = 0
        result = prim(weights, start_vertex)

        print("\nMST (Prim's Algorithm)")
        print("Edges:", result['edges'])
        print("Cost:", result['cost'])

        # problem 2
        weights = [
            [0, 13, 3, 22, 8, INF, INF, INF],
            [13, 0, INF, 9, INF, INF, INF, INF],
            [3, INF, 0, INF, 9, INF, INF, INF],
            [22, 9, INF, 0, INF, 10, INF, INF],
            [8, INF, 9, INF, 0, 15, 10, INF],
            [INF, INF, INF, 10, 15, 0, INF, 12],
            [INF, INF, INF, INF, 10, INF, 0, INF],
            [INF, INF, INF, INF, 12, INF, INF, 0]
        ]

        print(f"\nWeights matrix:")
        for i in range(len(weights)):
            for j in range(len(weights[i])):
                if weights[i][j] == INF:
                    print("INF", end=" ")
                else:
                    print(f"{weights[i][j]}", end=" ")

            print()

        start_vertex = 0
        result = prim(weights, start_vertex)

        print("\nMST (Prim's Algorithm)")
        print("Edges:", result['edges'])
        print("Cost:", result['cost'])

        # problem 3
        weights = [
            [0, INF, 72, 50, 90, 35],
            [INF, 0, 71, 70, 73, 75],
            [72, 71, 0, INF, 77, 90],
            [50, 70, INF, 0, 60, 40],
            [90, 73, 77, 60, 0, 80],
            [35, 75, 90, 40, 80, 0]
        ]

        print(f"\nWeights matrix:")
        for i in range(len(weights)):
            for j in range(len(weights[i])):
                if weights[i][j] == INF:
                    print("INF", end=" ")
                else:
                    print(f"{weights[i][j]}", end=" ")

            print()

        start_vertex = 3
        result = prim(weights, start_vertex)

        print("\nMST (Prim's Algorithm)")
        print("Edges:", result['edges'])
        print("Cost:", result['cost'])

    def dijkstra_shortest_path(self):
        """Run Dijkstra's Algorithm on various problems"""
        INF = sys.maxsize

        # problem 1
        weights = [
            [0, 7, 4, 6, 1],
            [INF, 0, INF, INF, INF],
            [INF, 2, 0, 5, INF],
            [INF, 3, INF, 0, INF],
            [INF, INF, INF, 1, 0]
        ]

        print(f"\nWeights matrix:")
        for i in range(len(weights)):
            for j in range(len(weights[i])):
                if weights[i][j] == INF:
                    print("INF", end=" ")
                else:
                    print(f"{weights[i][j]}", end=" ")

            print()

        start_vertex = 0
        result = dijkstra(weights, start_vertex)

        print("\nDijkstra's Short Path from source", start_vertex)
        print("Edges:", result['edges'])
        print("Touch:", result['touch'])

        destination = 1
        print("Print path to destination", destination)
        print_dijkstra_path(result['touch'], destination)

        # problem 2
        weights = [
            [0, 50, 10, INF, 45, INF],
            [INF, 0, 15, INF, 10, INF],
            [20, INF, 0, 15, INF, INF],
            [INF, 20, INF, 0, 35, INF],
            [INF, INF, INF, 30, 0, 20],
            [INF, INF, INF, 3, INF, 0]
        ]

        print(f"\nWeights matrix:")
        for i in range(len(weights)):
            for j in range(len(weights[i])):
                if weights[i][j] == INF:
                    print("INF", end=" ")
                else:
                    print(f"{weights[i][j]}", end=" ")

            print()

        start_vertex = 0
        result = dijkstra(weights, start_vertex)

        print("\nDijkstra's Short Path from source", start_vertex)
        print("Edges:", result['edges'])
        print("Touch:", result['touch'])

        destination = 5
        print("Print path to destination", destination)
        print_dijkstra_path(result['touch'], destination)

        # problem 3
        weights = [
            [0, INF, 72, 50, 90, 35],
            [INF, 0, 71, 70, 73, 75],
            [72, 71, 0, INF, 77, 90],
            [50, 70, INF, 0, 60, 40],
            [90, 73, 77, 60, 0, 80],
            [35, 75, 90, 40, 80, 0]
        ]

        print(f"\nWeights matrix:")
        for i in range(len(weights)):
            for j in range(len(weights[i])):
                if weights[i][j] == INF:
                    print("INF", end=" ")
                else:
                    print(f"{weights[i][j]}", end=" ")

            print()

        start_vertex = 4
        result = dijkstra(weights, start_vertex)

        print("\nDijkstra's Short Path from source", start_vertex)
        print("Edges:", result['edges'])
        print("Touch:", result['touch'])

        destination = 3
        print("Print path to destination", destination)
        print_dijkstra_path(result['touch'], destination)

    def scheduling(self):
        """Run Scheduling Deadline's Algorithm on various problems"""
        # problem 1
        jobs = [
            Job(1, 3, 40),
            Job(2, 1, 35),
            Job(3, 1, 30),
            Job(4, 3, 25),
            Job(5, 1, 20),
            Job(6, 3, 15),
            Job(7, 2, 10)
        ]

        print("\nScheduling deadline")
        print("Jobs:", jobs)

        result = schedule_deadline(jobs)

        print("Optimal schedule:", result['jobs'])
        print("Profits:", result['profits'])

        # problem 2
        jobs = [
            Job(1, 3, 30),
            Job(2, 1, 35),
            Job(3, 2, 15),
            Job(4, 1, 40),
            Job(5, 4, 50),
            Job(6, 3, 25),
            Job(7, 4, 10)
        ]

        print("\nScheduling deadline")
        print("Jobs:", jobs)

        result = schedule_deadline(jobs)

        print("Optimal schedule:", result['jobs'])
        print("Profits:", result['profits'])

        # problem 3
        jobs = [
            Job(1, 2, 40),
            Job(2, 4, 15),
            Job(3, 3, 60),
            Job(4, 2, 20),
            Job(5, 3, 10),
            Job(6, 1, 45),
            Job(7, 1, 55)
        ]

        print("\nScheduling deadline")
        print("Jobs:", jobs)

        result = schedule_deadline(jobs)

        print("Optimal schedule:", result['jobs'])
        print("Profits:", result['profits'])

    def huffman_coding(self):
        # problem 1
        codes = [
            HuffmanNode('b', 5),
            HuffmanNode('e', 10),
            HuffmanNode('c', 12),
            HuffmanNode('a', 16),
            HuffmanNode('d', 17),
            HuffmanNode('f', 25)
        ]

        heapq.heapify(codes)
        print("\nHeapified codes:", end=" ")
        print(list(codes))

        root = huffman_tree(codes)
        print("Huffman root:", root)

        # problem 2
        codes = [
            HuffmanNode('A', 12),
            HuffmanNode('B', 7),
            HuffmanNode('I', 18),
            HuffmanNode('M', 10),
            HuffmanNode('S', 9),
            HuffmanNode('X', 5),
            HuffmanNode('Z', 2)
        ]

        heapq.heapify(codes)
        print("\nHeapified codes:", end=" ")
        print(list(codes))

        root = huffman_tree(codes)
        print("Huffman root:", root)

        # problem 3
        codes = [
            HuffmanNode('Z', 2),
            HuffmanNode('K', 7),
            HuffmanNode('M', 24),
            HuffmanNode('C', 32),
            HuffmanNode('U', 37),
            HuffmanNode('D', 42),
            HuffmanNode('L', 42),
            HuffmanNode('E', 120)
        ]

        heapq.heapify(codes)
        print("\nHeapified codes:", end=" ")
        print(list(codes))

        root = huffman_tree(codes)
        print("Huffman root:", root)


if __name__ == "__main__":
    Run().prim_algorithm()
    Run().dijkstra_shortest_path()
    Run().scheduling()
    Run().huffman_coding()
