"""
Greedy Algorithms
"""
from dijkstra import dijkstra, print_dijkstra_path
from huffman import HuffmanNode, huffman_encode, huffman_decode, huffman_tree,\
    print_huffman_tree
from kruskal import kruskal
from prim import prim
from schedule_deadline import schedule_deadline, Job


class Run(object):
    """
    Run Greedy Algorithm's methods
    """

    def prim_algorithm(self):
        """Run Prim's Algorithm on various problems"""
        inf = float('inf')

        print("\n\nPRIM'S ALGORITHM\n----------------")

        # problem 1
        print("\n\nPROBLEM 1")

        weights = [
            [0, 1, 3, inf, inf],
            [1, 0, 3, 6, inf],
            [3, 3, 0, 4, 2],
            [inf, 6, 4, 0, 5],
            [inf, inf, 2, 5, 0],
        ]

        print(f"\nWeights matrix")
        print_matrix(weights)

        source = 0
        result = prim(weights, source)

        print("\nPrim's Algorithm (MST)")
        print("Edges:", result['edges'])
        print("Cost:", result['cost'])

        # problem 2
        print("\n\nPROBLEM 2")

        weights = [
            [0, 13, 3, 22, 8, inf, inf, inf],
            [13, 0, inf, 9, inf, inf, inf, inf],
            [3, inf, 0, inf, 9, inf, inf, inf],
            [22, 9, inf, 0, inf, 10, inf, inf],
            [8, inf, 9, inf, 0, 15, 10, inf],
            [inf, inf, inf, 10, 15, 0, inf, 12],
            [inf, inf, inf, inf, 10, inf, 0, inf],
            [inf, inf, inf, inf, 12, inf, inf, 0]
        ]

        print(f"\nWeights matrix")
        print_matrix(weights)

        source = 0
        result = prim(weights, source)

        print("\nPrim's Algorithm (MST)")
        print("Edges:", result['edges'])
        print("Cost:", result['cost'])

        # problem 3
        print("\n\nPROBLEM 3")

        weights = [
            [0, inf, 72, 50, 90, 35],
            [inf, 0, 71, 70, 73, 75],
            [72, 71, 0, inf, 77, 90],
            [50, 70, inf, 0, 60, 40],
            [90, 73, 77, 60, 0, 80],
            [35, 75, 90, 40, 80, 0]
        ]

        print(f"\nWeights matrix")
        print_matrix(weights)

        source = 3
        result = prim(weights, source)

        print("\nPrim's Algorithm (MST)")
        print("Edges:", result['edges'])
        print("Cost:", result['cost'])

    def kruskal_algorithm(self):
        """Run Kruskal's Algorithm on various problems"""
        inf = float('inf')

        print("\n\nKRUSKAL'S ALGORITHM\n-------------------")

        # problem 1
        print("\n\nPROBLEM 1")

        weights = [
            [0, 1, 3, inf, inf],
            [1, 0, 3, 6, inf],
            [3, 3, 0, 4, 2],
            [inf, 6, 4, 0, 5],
            [inf, inf, 2, 5, 0],
        ]

        print(f"\nWeights matrix")
        print_matrix(weights)

        result = kruskal(weights)

        print("\nKruskal's Algorithm (MST)")
        print("Edges:", result['edges'])
        print("Cost:", result['cost'])

        # problem 2
        print("\n\nPROBLEM 2")

        weights = [
            [0, 13, 3, 22, 8, inf, inf, inf],
            [13, 0, inf, 9, inf, inf, inf, inf],
            [3, inf, 0, inf, 9, inf, inf, inf],
            [22, 9, inf, 0, inf, 10, inf, inf],
            [8, inf, 9, inf, 0, 15, 10, inf],
            [inf, inf, inf, 10, 15, 0, inf, 12],
            [inf, inf, inf, inf, 10, inf, 0, inf],
            [inf, inf, inf, inf, 12, inf, inf, 0]
        ]

        print(f"\nWeights matrix")
        print_matrix(weights)

        result = kruskal(weights)

        print("\nKruskal's Algorithm (MST)")
        print("Edges:", result['edges'])
        print("Cost:", result['cost'])

        # problem 3
        print("\n\nPROBLEM 3")

        weights = [
            [0, inf, 72, 50, 90, 35],
            [inf, 0, 71, 70, 73, 75],
            [72, 71, 0, inf, 77, 90],
            [50, 70, inf, 0, 60, 40],
            [90, 73, 77, 60, 0, 80],
            [35, 75, 90, 40, 80, 0]
        ]

        print(f"\nWeights matrix")
        print_matrix(weights)

        result = kruskal(weights)

        print("\nKruskal's Algorithm (MST)")
        print("Edges:", result['edges'])
        print("Cost:", result['cost'])

    def dijkstra_shortest_path(self):
        """Run Dijkstra's Algorithm on various problems"""
        inf = float('inf')

        print("\n\nDIJKSTRA'S ALGORITHM\n--------------------")

        # problem 1
        print("\n\nPROBLEM 1")

        weights = [
            [0, 7, 4, 6, 1],
            [inf, 0, inf, inf, inf],
            [inf, 2, 0, 5, inf],
            [inf, 3, inf, 0, inf],
            [inf, inf, inf, 1, 0]
        ]

        print(f"\nWeights matrix")
        print_matrix(weights)

        source = 0
        result = dijkstra(weights, source)

        print("\nDijkstra's Short Path from source", source)
        print("Edges:", result['edges'])
        print("Predecessor:", result['predecessor'])

        target = 1
        print("Print path to target", target)
        print_dijkstra_path(result['predecessor'], target)

        # problem 2
        print("\n\nPROBLEM 2")

        weights = [
            [0, 50, 10, inf, 45, inf],
            [inf, 0, 15, inf, 10, inf],
            [20, inf, 0, 15, inf, inf],
            [inf, 20, inf, 0, 35, inf],
            [inf, inf, inf, 30, 0, 20],
            [inf, inf, inf, 3, inf, 0]
        ]

        print(f"\nWeights matrix")
        print_matrix(weights)

        source = 0
        result = dijkstra(weights, source)

        print("\nDijkstra's Short Path from source", source)
        print("Edges:", result['edges'])
        print("Predecessor:", result['predecessor'])

        target = 5
        print("Print path to target", target)
        print_dijkstra_path(result['predecessor'], target)

        # problem 3
        print("\n\nPROBLEM 3")

        weights = [
            [0, inf, 72, 50, 90, 35],
            [inf, 0, 71, 70, 73, 75],
            [72, 71, 0, inf, 77, 90],
            [50, 70, inf, 0, 60, 40],
            [90, 73, 77, 60, 0, 80],
            [35, 75, 90, 40, 80, 0]
        ]

        print(f"\nWeights matrix")
        print_matrix(weights)

        source = 4
        result = dijkstra(weights, source)

        print("\nDijkstra's Short Path from source", source)
        print("Edges:", result['edges'])
        print("Predecessor:", result['predecessor'])

        target = 3
        print("Print path to target", target)
        print_dijkstra_path(result['predecessor'], target)

    def scheduling(self):
        """Run Scheduling Deadline's Algorithm on various problems"""

        print("\n\nSCHEDULING DEADLINE\n-------------------")

        # problem 1
        print("\n\nPROBLEM 1")

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
        print("\n\nPROBLEM 2")

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
        print("\n\nPROBLEM 3")
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
        print("\n\nHUFFMAN CODING\n--------------")

        # problem 1
        print("\n\nPROBLEM 1")

        nodes = [
            HuffmanNode('b', 5),
            HuffmanNode('e', 10),
            HuffmanNode('c', 12),
            HuffmanNode('a', 16),
            HuffmanNode('d', 17),
            HuffmanNode('f', 25)
        ]

        print("\nHeapified nodes:", end=" ")
        print(list(nodes))

        root = huffman_tree(nodes)
        print("Huffman root:", root)
        print_huffman_tree(root)

        str1 = "abba"
        str2 = "dafe"

        encoded_str1 = huffman_encode(root, str1)
        encoded_str2 = huffman_encode(root, str2)
        decoded_str1 = huffman_decode(root, encoded_str1)
        decoded_str2 = huffman_decode(root, encoded_str2)

        print("Str1:", str1)
        print("Str2:", str2)
        print("Encoded str1", encoded_str1)
        print("Encoded str2", encoded_str2)
        print("Decoded str1", decoded_str1)
        print("Decoded str2", decoded_str2)

        # problem 2
        print("\n\nPROBLEM 2")

        nodes = [
            HuffmanNode('A', 12),
            HuffmanNode('B', 7),
            HuffmanNode('I', 18),
            HuffmanNode('M', 10),
            HuffmanNode('S', 9),
            HuffmanNode('X', 5),
            HuffmanNode('Z', 2)
        ]

        print("\nHeapified nodes:", end=" ")
        print(list(nodes))

        root = huffman_tree(nodes)
        print("Huffman root:", root)
        print_huffman_tree(root)

        str1 = "SAAB"
        str2 = "ZIX"

        encoded_str1 = huffman_encode(root, str1)
        encoded_str2 = huffman_encode(root, str2)
        decoded_str1 = huffman_decode(root, encoded_str1)
        decoded_str2 = huffman_decode(root, encoded_str2)

        print("Str1:", str1)
        print("Str2:", str2)
        print("Encoded str1", encoded_str1)
        print("Encoded str2", encoded_str2)
        print("Decoded str1", decoded_str1)
        print("Decoded str2", decoded_str2)

        # problem 3
        print("\n\nPROBLEM 3")

        nodes = [
            HuffmanNode('Z', 2),
            HuffmanNode('K', 7),
            HuffmanNode('M', 24),
            HuffmanNode('C', 32),
            HuffmanNode('U', 37),
            HuffmanNode('D', 42),
            HuffmanNode('L', 42),
            HuffmanNode('E', 120)
        ]

        print("\nHeapified nodes:", end=" ")
        print(list(nodes))

        root = huffman_tree(nodes)
        print("Huffman root:", root)
        print_huffman_tree(root)

        str1 = "DEED"
        str2 = "MUCK"

        encoded_str1 = huffman_encode(root, str1)
        encoded_str2 = huffman_encode(root, str2)
        decoded_str1 = huffman_decode(root, encoded_str1)
        decoded_str2 = huffman_decode(root, encoded_str2)

        print("Str1:", str1)
        print("Str2:", str2)
        print("Encoded str1", encoded_str1)
        print("Encoded str2", encoded_str2)
        print("Decoded str1", decoded_str1)
        print("Decoded str2", decoded_str2)

        # problem 4
        print("\n\nPROBLEM 4")

        nodes = [
            HuffmanNode('a', 16),
            HuffmanNode('b', 5),
            HuffmanNode('c', 12),
            HuffmanNode('d', 17),
            HuffmanNode('e', 10),
            HuffmanNode('f', 25)
        ]

        print("\nHeapified nodes:", end=" ")
        print(list(nodes))

        root = huffman_tree(nodes)
        print("Huffman root:", root)
        print_huffman_tree(root)

        str1 = "fade"
        str2 = "efface"

        encoded_str1 = huffman_encode(root, str1)
        encoded_str2 = huffman_encode(root, str2)
        decoded_str1 = huffman_decode(root, encoded_str1)
        decoded_str2 = huffman_decode(root, encoded_str2)

        print("Str1:", str1)
        print("Str2:", str2)
        print("Encoded str1", encoded_str1)
        print("Encoded str2", encoded_str2)
        print("Decoded str1", decoded_str1)
        print("Decoded str2", decoded_str2)


def print_matrix(A, pad_size=3, sep=" ", end="\n"):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(f"{(A[i][j]):>{pad_size}}", end=sep)
        if i == len(A) - 1:
            print(end, end="")
        else:
            print()


if __name__ == "__main__":
    Run().prim_algorithm()
    Run().kruskal_algorithm()
    Run().dijkstra_shortest_path()
    Run().scheduling()
    Run().huffman_coding()
