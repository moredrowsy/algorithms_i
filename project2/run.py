"""
Project 2

- Fractional Knapsack
- Whole Knapsack
"""
import os

from knapsack import KnapsackItem, knapsack, fractional_knapsack


class Run(object):
    """
    Run project 2's methods
    """
    capacity = -1
    items = []
    menu = "OPTIONS\n"\
        "1: List 0-1 knapsack items\n"\
        "2: List fractional knapsack items\n"\
        "3. List entered items\n"\
        "4: Change capacity\n"\
        "5: Add items manually\n"\
        "6: Add items from file\n"\
        "7. Clear all entered items\n"\
        "X: Exit"

    def setup(self):
        """Run knapsack program setup"""
        print("SETUP\n-----")

        self.change_capacity()

        print("\nEnter items manually or from file?")
        print("1: Manually")
        print("2: From file as input.txt")
        choice = self.input()

        while choice != "1" and choice != "2":
            print("Invalid choice")
            choice = self.input()

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

            print(info, end="\n\n")
            print(self.menu, end="\n")
            choice = self.input()

            if choice == "X" or choice == "x":
                break

            self.clear_screen()
            print(title)

            if choice == "1":
                self.knapsack()
            elif choice == "2":
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
                self.capacity = int(self.input("Enter knapsack capacity"))
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
            info = self.input()
            data = info.split()

            if info == "X" or info == "x":
                break

            try:
                if int(data[0]) == 0:
                    raise ValueError("Weight can not be 0.")

                self.items.append(KnapsackItem(
                    len(self.items), int(data[0]), float(data[1])))

                print("Added item:", self.items[-1])
            except ValueError as err:
                print("Invalid input:", err)
            except Exception:
                print("Invalid input.")

    def add_from_file(self, filename=None):
        """Populate KnapsackItems from file"""
        if not filename:
            filename = self.input("Enter file name")

        while not os.path.exists(filename):
            print("Path does not exist.")
            filename = self.input("Enter file name")

        with open(filename) as file:
            print()
            for i, line in enumerate(file):
                data = line.split()

                try:
                    if int(data[0]) == 0:
                        raise ValueError("Weight can not be 0.")

                    self.items.append(KnapsackItem(
                        len(self.items), int(data[0]), float(data[1])))

                    print("Added item:", self.items[-1])
                except ValueError as err:
                    print(f"Invalid input at line {i}.", err)
                except Exception:
                    print(f"Invalid input at line {i}.")

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

    def input(self, msg=None, end="\n"):
        if msg:
            print(msg, end=end)
        return input("> ")

    def knapsack(self):
        """Run knapsack algorithm"""
        if len(self.items) > 0:
            print("0-1 KNAPSACK")

            result = knapsack(self.items, self.capacity)

            print(f"Profit: {result['profit']:.2f}")
            for item in result['knapsack']:
                print(f"Item: {item}")
        else:
            print("No items entered")

    def fract_knapsack(self):
        """Run fractional knapsack algorithm"""
        if len(self.items) > 0:
            print("FRACTIONAL KNAPSACK")

            result = fractional_knapsack(self.items, self.capacity)

            print(f"Profit: {result['profit']:.2f}")
            for item in result['knapsack']:
                print(f"Fraction: {item[0]:.2f}\tItem: {item[1]}")
        else:
            print("No items entered")


if __name__ == "__main__":
    Run().start()
