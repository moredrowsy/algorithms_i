import copy


class Job(object):
    """A Job as a job number (index), deadline, and profit"""

    def __init__(self, index, deadline, profit):
        self.index = index
        self.deadline = deadline
        self.profit = profit

    def __str__(self):
        return f"(#{self.index}], {self.deadline}, {self.profit})"

    def __repr__(self):
        return f"(#{self.index}, {self.deadline}, {self.profit})"

    def __eq__(self, o):
        return self.index == o.index\
            and self.deadline == o.deadline\
            and self.profit == o.profit


def schedule_deadline(jobs):
    """
    Final a sequence of jobs that is within deadline with max profits

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

    # sort jobs by profit
    jobs.sort(key=lambda j: j.profit, reverse=True)

    final_jobs.append(jobs[0])
    profits = profits + jobs[0].profit

    for i in range(1, len(jobs)):
        # temp copy of final jobs
        temp_jobs = copy.deepcopy(final_jobs)

        # add next job and sort by deadline
        temp_jobs.append(jobs[i])
        temp_jobs.sort(key=lambda j: j.deadline)

        # set temp_jobs to final_jobs if feasible sequence
        if feasible(temp_jobs):
            final_jobs = temp_jobs
            profits = profits + jobs[i].profit

    return {'jobs': final_jobs, 'profits': profits}


def feasible(jobs):
    """Checks if the sequence of jobs is feasible"""
    for i in range(len(jobs)):
        if jobs[i].deadline < i + 1:
            return False

    return True
