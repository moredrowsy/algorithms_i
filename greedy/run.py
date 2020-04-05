"""
Greedy Algorithms
"""
from dijkstra import dijkstra, print_dijkstra_path
from huffman import HuffmanNode, huffman_encode, huffman_decode, huffman_tree,\
    print_huffman_tree
from prim import prim
from schedule_deadline import schedule_deadline, Job


class Run(object):
    """
    Run Greedy Algorithm's methods
    """

    def prim_algorithm(self):
        """Run Prim's Algorithm on various problems"""
        INF = float('inf')

        # problem 1
        weights = [
            [0, 1, 3, INF, INF],
            [1, 0, 3, 6, INF],
            [3, 3, 0, 4, 2],
            [INF, 6, 4, 0, 5],
            [INF, INF, 2, 5, 0],
        ]

        print(f"\nWeights matrix")
        print_matrix(weights)

        source_node = 0
        result = prim(weights, source_node)

        print("\nPrim's Algorithm (MST)")
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

        print(f"\nWeights matrix")
        print_matrix(weights)

        source_node = 0
        result = prim(weights, source_node)

        print("\nPrim's Algorithm (MST)")
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

        print(f"\nWeights matrix")
        print_matrix(weights)

        source_node = 3
        result = prim(weights, source_node)

        print("\nPrim's Algorithm (MST)")
        print("Edges:", result['edges'])
        print("Cost:", result['cost'])

    def dijkstra_shortest_path(self):
        """Run Dijkstra's Algorithm on various problems"""
        INF = float('inf')

        # problem 1
        weights = [
            [0, 7, 4, 6, 1],
            [INF, 0, INF, INF, INF],
            [INF, 2, 0, 5, INF],
            [INF, 3, INF, 0, INF],
            [INF, INF, INF, 1, 0]
        ]

        print(f"\nWeights matrix")
        print_matrix(weights)

        source_node = 0
        result = dijkstra(weights, source_node)

        print("\nDijkstra's Short Path from source", source_node)
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

        print(f"\nWeights matrix")
        print_matrix(weights)

        source_node = 0
        result = dijkstra(weights, source_node)

        print("\nDijkstra's Short Path from source", source_node)
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

        print(f"\nWeights matrix")
        print_matrix(weights)

        source_node = 4
        result = dijkstra(weights, source_node)

        print("\nDijkstra's Short Path from source", source_node)
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
    Run().dijkstra_shortest_path()
    Run().scheduling()
    Run().huffman_coding()
