"""
Project 2

- Fractional Knapsack
- Whole Knapsack
"""

from fractional_knapsack import fractional_knapsack, KnapsackItem


class Run(object):
    """
    Run project 2's methods
    """
    capacity = -1
    items = []
    menu = "\nOPTIONS\n"\
        "1: Change capacity\n"\
        "2: Add items manually\n"\
        "3: Add items from file\n"\
        "4. List items\n"\
        "5: List fractional knapsack items\n"\
        "6: List whole knapsack items\n"\
        "X: Exit\n"

    def setup(self):
        """Run knapsack program setup"""
        print("\nSETUP\n-----")

        self.change_capacity()

        print("\nEnter items manually or from file?")
        print("1: Manually")
        print("2: From file as input.txt")
        choice = input()

        while choice != "1" and choice != "2":
            print("Invalid choice")
            choice = input()

        if choice == "1":
            self.add_items()
        else:
            self.add_from_file("input.txt")

    def start(self):
        """Run user interactive mode"""
        while True:
            info = f"\nCAPACITY: {run.capacity}\t"
            info += f"ITEMS ENTERED: {len(run.items)} items"

            print(info)
            print(self.menu)
            choice = input()

            if choice == "X" or choice == "x":
                break
            elif choice == "1":
                self.change_capacity()
            elif choice == "2":
                self.add_items()
            elif choice == "3":
                self.add_from_file()
            elif choice == "4":
                self.print_items()
            elif choice == "5":
                self.fract_knapsack()
            else:
                pass

    def change_capacity(self):
        """User change knapsack capacity"""
        while True:
            print("Enter knapsack capacity: ", end="")
            try:
                self.capacity = int(input())

                if self.capacity > 0:
                    break
                else:
                    print("Invalid.")
            except:
                print("Invalid.")

    def add_items(self):
        """User add KnapsackItems from user"""
        instructions = "\nFormat: [WEIGHT] [PROFIT]\nEnter -1 to stop"
        info = 0

        print(instructions)
        while True:
            item_id = self.items[-1].index + 1\
                if len(self.items) > 0 else 0

            info = input()
            data = info.split()

            if info == "-1":
                break
            elif len(data) == 2:
                try:
                    self.items.append(KnapsackItem(
                        len(self.items), float(data[0]), float(data[1])))
                except:
                    print("Invalid input")
            else:
                print("Invalid input")

    def add_from_file(self, filename=None):
        """Populate KnapsackItems from file"""
        instructions = "Enter file name"
        temp_items = []

        while True:
            if not filename:
                print(instructions)
                filename = input()

            with open(filename) as file:
                item_id = 0

                for line in file:
                    data = line.split()
                    temp_items.append(KnapsackItem(
                        item_id, float(data[0]), float(data[1])))
                    item_id += 1

                self.items = temp_items
                break

    def print_items(self):
        """Print items entered from user or file"""
        if len(self.items) > 0:
            print("\nItems entered")
            for item in self.items:
                print(item)
        else:
            print("No items entered")

    def fract_knapsack(self):
        """Run fractional knapsack algorithm
        """
        if len(self.items) > 0:
            print("\nListing Fractional Knapsack")

            result = fractional_knapsack(self.items, self.capacity)

            print("Cost:", result['cost'])
            for item in result['set']:
                print("Fraction:", item[0], "\tItem:", item[1])
        else:
            print("Invalid. No items entered")


if __name__ == "__main__":
    print("\nKNAPSACK PROGRAM")
    run = Run()
    run.setup()
    run.start()
