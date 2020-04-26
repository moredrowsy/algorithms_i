"""
Scheduling Deadline: Find the optimal sequence of jobs for maximal profits
"""
import copy


class Job(object):
    """A Job as a job number (index), deadline, and profit"""

    def __init__(self, index, deadline, profit):
        """
        Parameters
        ----------
        index (int): Job number
        deadline (int): deadline number
        profit(float): profit for this job
        """
        self.id = index
        self.deadline = deadline
        self.profit = profit

    def __repr__(self):
        return f"(ID {self.id} D {self.deadline} P {self.profit})"

    def __eq__(self, o):
        return self.id == o.id\
            and self.deadline == o.deadline\
            and self.profit == o.profit


def schedule_deadline(jobs):
    """
    Final a sequence of jobs that is within deadline with max profits.

    Time complexity: O(n^2)
    Complexity breakdown:
        sort: nlogn
        for loop: n
        feasibility check: n
        total: nlogn + n*n = O(n^2)

    Parameters
    ----------
    jobs (array): an array of Jobs

    Return
    ------
    array of Jobs

    NOTES
    -----
    First sort array of jobs by profit. Pick the top element in jobs to a
    temp array. Sort this temporary array by deadline and check if this
    sequence in temp array is feasible. Array is feasible if the deadline is
    not smaller than temp array's index + 1.
    """
    final_jobs = []
    profits = 0

    # sort jobs by highest profit
    jobs.sort(key=lambda job: job.profit, reverse=True)

    for i in range(len(jobs)):
        # temp copy of final jobs
        temp_jobs = copy.copy(final_jobs)

        # add next job and sort by lowest deadline
        temp_jobs.append(jobs[i])
        temp_jobs.sort(key=lambda job: job.deadline)

        # set temp_jobs to final_jobs if feasible sequence
        if feasible(temp_jobs):
            final_jobs = temp_jobs
            profits += jobs[i].profit

    return {'jobs': final_jobs, 'profits': profits}


def feasible(jobs):
    """Checks if the sequence of jobs is feasible"""
    for i in range(len(jobs)):
        if jobs[i].deadline < i + 1:
            return False

    return True
