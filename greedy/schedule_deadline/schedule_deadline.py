import copy


class Job(object):
    def __init__(self, index, deadline, profit):
        self.index = index
        self.deadline = deadline
        self.profit = profit

    def __str__(self):
        return f"(#{self.index}], {self.deadline}, {self.profit})"

    def __repr__(self):
        return f"(#{self.index}, {self.deadline}, {self.profit})"


def schedule_deadline(jobs):
    final_jobs = []

    # sort jobs by profit
    jobs.sort(key=lambda j: j.profit, reverse=True)

    final_jobs.append(jobs[0])
    for i in range(1, len(jobs)):
        # temp copy of final jobs
        temp_jobs = copy.deepcopy(final_jobs)

        # add next job and sort by deadline
        temp_jobs.append(jobs[i])
        temp_jobs.sort(key=lambda j: j.deadline)

        # check if jobs sequence is feasible and set to final_jobs if True
        if feasible(temp_jobs):
            final_jobs = temp_jobs

    return final_jobs


def feasible(jobs):
    for i in range(len(jobs)):
        if jobs[i].deadline < i + 1:
            return False

    return True
