"""
Greedy Approach Algorithms
"""
import sys
from prim import prim
from schedule_deadline import schedule_deadline, Job


class Run(object):
    """
    Run Greedy Algorithm's methods
    """

    def prim(self):
        """Run sorting algorithm for Merge sort and Quick sort
        """
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
        final_set = prim(weights, start_vertex)

        print("\nMST (Prim's Algorithm)")
        print(final_set)

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
        final_set = prim(weights, start_vertex)

        print("\nMST (Prim's Algorithm)")
        print(final_set)

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
        final_set = prim(weights, start_vertex)

        print("\nMST (Prim's Algorithm)")
        print(final_set)

    def scheduling(self):
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

        final_jobs = schedule_deadline(jobs)
        profits = sum(job.profit for job in final_jobs)

        print("Optimal schedule:", final_jobs)
        print("Profits:", profits)

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

        final_jobs = schedule_deadline(jobs)
        profits = sum(job.profit for job in final_jobs)

        print("Optimal schedule:", final_jobs)
        print("Profits:", profits)

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

        final_jobs = schedule_deadline(jobs)
        profits = sum(job.profit for job in final_jobs)

        print("Optimal schedule:", final_jobs)
        print("Profits:", profits)


if __name__ == "__main__":
    Run().prim()
    Run().scheduling()
