"""
Unit tests
"""
import unittest

from schedule_deadline import schedule_deadline, Job


class TestSchedule(unittest.TestCase):
    """
    Tests Scheduling Deadline's Algorithm
    """
    # class attributes

    def setUp(self):
        """
        Test setup
        """

    def test_problem1(self):
        jobs = [
            Job(1, 3, 40),
            Job(2, 1, 35),
            Job(3, 1, 30),
            Job(4, 3, 25),
            Job(5, 1, 20),
            Job(6, 3, 15),
            Job(7, 2, 10)
        ]
        solution_set = [
            Job(2, 1, 35),
            Job(1, 3, 40),
            Job(4, 3, 25),
        ]
        profits_answer = 100

        result = schedule_deadline(jobs)

        self.assertEqual(result['jobs'], solution_set)
        self.assertEqual(result['profits'], profits_answer)

    def test_problem2(self):
        jobs = [
            Job(1, 3, 30),
            Job(2, 1, 35),
            Job(3, 2, 15),
            Job(4, 1, 40),
            Job(5, 4, 50),
            Job(6, 3, 25),
            Job(7, 4, 10)
        ]
        solution_set = [
            Job(4, 1, 40),
            Job(1, 3, 30),
            Job(6, 3, 25),
            Job(5, 4, 50)
        ]
        profits_answer = 145

        result = schedule_deadline(jobs)

        self.assertEqual(result['jobs'], solution_set)
        self.assertEqual(result['profits'], profits_answer)

    def test_problem3(self):
        jobs = [
            Job(1, 2, 40),
            Job(2, 4, 15),
            Job(3, 3, 60),
            Job(4, 2, 20),
            Job(5, 3, 10),
            Job(6, 1, 45),
            Job(7, 1, 55)
        ]
        solution_set = [
            Job(7, 1, 55),
            Job(1, 2, 40),
            Job(3, 3, 60),
            Job(2, 4, 15)
        ]
        profits_answer = 170

        result = schedule_deadline(jobs)

        self.assertEqual(result['jobs'], solution_set)
        self.assertEqual(result['profits'], profits_answer)


if __name__ == "__main__":
    unittest.main()
