"""
Tower of Hanoi
"""


class TowerOfHanoi(object):
    """
    A game of Tower of Hanoi
    """

    def __init__(self, source, helper, target, label1, label2, label3):
        """
        Initializations

        Parameters
        ----------
        source (array): Source peg
        helper (array): Helper peg
        target (array): Target peg
        label1 (string): Label for source peg
        label2 (string): Label for helper peg
        label3 (string): Label for target peg
        """
        self.size = len(source)
        self.source = {"label": label1, "array": source}
        self.helper = {"label": label2, "array": helper}
        self.target = {"label": label3, "array": target}

    def solve(self, display=False):
        """
        Solves the game of hanoi.
        """
        self.move_disks(self.size, self.source,
                        self.target, self.helper, display)

    def print_pegs(self):
        """
        Print the peg's label and arrays
        """
        print(f"{self.source['label']}: {self.source['array']}")
        print(f"{self.helper['label']}: {self.helper['array']}")
        print(f"{self.target['label']}: {self.target['array']}")

    def move_disks(self, disks, source, target, helper, display=False):
        """
        Recursive function to move the disk in source peg to target peg

        Parameters
        ----------
        disks (int): Number of disks in peg (array size)
        source (dict): Source dictionary with "label" and "array" peg
        helper (dict): Helper dictionary with "label" and "array" peg
        target (dict): Target dictionary with "label" and "array" peg
        """
        if(disks > 0):
            # move (disks -1) index from source to helper
            # target is now helper peg
            self.move_disks(disks - 1, source, helper, target, display)

            # add disk to target

            target["array"].append(source["array"].pop())

            if(display):
                print(f"\nMoving from {source['label']} to {target['label']}")
                self.print_pegs()

            # move (disks - 1) index from helper to target
            # source is now helper
            self.move_disks(disks - 1, helper, target, source, display)
