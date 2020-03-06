"""
Tower of Hanoi
"""


class TowerOfHanoi(object):
    """
    A game of Tower of Hanoi
    """

    def __init__(self, source, helper, target,
                 src_label="A", hlp_label="B", tgt_label="C"):
        """
        Initializations

        Parameters
        ----------
        source (array): Source peg
        helper (array): Helper peg
        target (array): Target peg
        src_label (string): Label for source peg
        hlp_label (string): Label for helper peg
        tgt_label (string): Label for target peg
        """
        self.size = len(source)
        self.source = {"label": src_label, "array": source}
        self.helper = {"label": hlp_label, "array": helper}
        self.target = {"label": tgt_label, "array": target}

    def solve(self, display=False):
        """
        Solves the game of hanoi.

        Parameters
        ----------
        display (bool): Display each steps of moving disk
        """
        self._move_disks(self.size, self.source,
                         self.target, self.helper, display)

    def print(self):
        """
        Print the peg's label and arrays
        """
        print(f"{self.source['label']}: {self.source['array']}\n"
              f"{self.helper['label']}: {self.helper['array']}\n"
              f"{self.target['label']}: {self.target['array']}")

    def _move_disks(self, disks, source, target, helper, display=False):
        """
        Recursive function to move the disk in source peg to target peg

        Parameters
        ----------
        disks (int): Number of disks in peg (array size)
        source (dict): Source dictionary with "label" and "array" peg
        helper (dict): Helper dictionary with "label" and "array" peg
        target (dict): Target dictionary with "label" and "array" peg
        display (bool): Display each steps of moving disk
        """
        if(disks > 0):
            # move disks-1 from source to helper
            # target is now helper peg
            self._move_disks(disks - 1, source, helper, target, display)

            # add disk from source to target
            target["array"].append(source["array"].pop())

            if(display):
                print(
                    f"\nMoving {target['array'][-1]} "
                    f"from {source['label']} to {target['label']}")
                self.print()

            # move disks-1 from helper to target
            # source is now helper peg
            self._move_disks(disks - 1, helper, target, source, display)
