"""
Project 2

- Fractional Knapsack
- Whole Knapsack
"""
import os

from fractional_knapsack import fractional_knapsack, KnapsackItem


class Run(object):
    """
    Run project 2's methods
    """
    capacity = -1
    items = []
    menu = "\nOPTIONS\n"\
        "1: List fractional knapsack items\n"\
        "2: List whole knapsack items\n"\
        "3. List entered items\n"\
        "4: Change capacity\n"\
        "5: Add items manually\n"\
        "6: Add items from file\n"\
        "7. Clear all entered items\n"\
        "X: Exit\n"

    def setup(self):
        """Run knapsack program setup"""
        print("SETUP\n-----")

        self.change_capacity()

        print("\nEnter items manually or from file?")
        print("1: Manually")
        print("2: From file as input.txt")
        choice = self.get_input()

        while choice != "1" and choice != "2":
            print("Invalid choice")
            choice = self.get_input()

        if choice == "1":
            print()
            self.add_items()
        else:
            self.add_from_file("input.txt")

    def start(self):
        """Run user interactive mode"""
        title = "\nKNAPSACK PROGRAM\n----------------\n"
        print(title)
        self.setup()

        while True:
            info = f"\nCAPACITY: {self.capacity}\t"
            info += f"ITEMS ENTERED: {len(self.items)} items"

            print(info)
            print(self.menu)
            choice = self.get_input()

            if choice == "X" or choice == "x":
                break

            self.clear_screen()
            print(title)

            if choice == "1":
                self.fract_knapsack()
            elif choice == "3":
                self.print_items()
            elif choice == "4":
                self.change_capacity()
            elif choice == "5":
                self.add_items()
            elif choice == "6":
                self.add_from_file()
            elif choice == "7":
                self.clear_items()
            else:
                pass

    def change_capacity(self):
        """User change knapsack capacity"""
        while True:
            try:
                self.capacity = int(self.get_input("Enter knapsack capacity"))

                if self.capacity > 0:
                    break
                else:
                    print("Invalid.")
            except:
                print("Invalid.")

    def add_items(self):
        """User add KnapsackItems from user"""
        info = 0
        print("Format: [WEIGHT] [PROFIT]\nEnter X to stop")

        while True:
            info = self.get_input()
            data = info.split()

            if info == "X" or info == "x":
                break
            elif len(data) == 2:
                try:
                    self.items.append(KnapsackItem(
                        len(self.items), float(data[0]), float(data[1])))
                    print("Added item:", self.items[-1])
                except:
                    print("Invalid input")
            else:
                print("Invalid input")

    def add_from_file(self, filename=None):
        """Populate KnapsackItems from file"""
        while True:
            if not filename:
                filename = self.get_input("Enter file name")

            while not os.path.exists(filename):
                print("Path does not exist.")
                filename = self.get_input("Enter file name")

            with open(filename) as file:
                print()
                for line in file:
                    data = line.split()
                    self.items.append(KnapsackItem(
                        len(self.items), float(data[0]), float(data[1])))

                    print("Added item:", self.items[-1])

                self.items = self.items
                break

    def clear_items(self):
        self.items = []
        print("All entered items removed.")

    def print_items(self):
        """Print items entered from user or file"""
        if len(self.items) > 0:
            print("Items entered")
            for item in self.items:
                print(item)
        else:
            print("No items entered")

    def clear_screen(self):
        import os
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')

    def get_input(self, msg=None, end="\n"):
        if msg:
            print(msg, end=end)
        print(">", end=" ")
        return input()

    def fract_knapsack(self):
        """Run fractional knapsack algorithm
        """
        if len(self.items) > 0:
            print("Listing Fractional Knapsack")

            result = fractional_knapsack(self.items, self.capacity)

            print(f"Profit: {result['profit']:.2f}")
            for item in result['knapsack']:
                self.print_fract_knapsack_item(item)
        else:
            print("No items entered")

    def print_fract_knapsack_item(self, item, end="\n"):
        print(f"Fraction: {item[0]:.2f}\tItem: {item[1]}", end=end)


if __name__ == "__main__":
    Run().start()
