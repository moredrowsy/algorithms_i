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
        print("\nKNAPSACK PROGRAM")
        self.setup()

        while True:
            info = f"\nCAPACITY: {self.capacity}\t"
            info += f"ITEMS ENTERED: {len(self.items)} items"

            print(info)
            print(self.menu)
            choice = input()

            if choice == "X" or choice == "x":
                break

            self.clear_screen()
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
        info = 0
        print("\nFormat: [WEIGHT] [PROFIT]\nEnter X to stop")

        while True:
            info = input()
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
                print("Enter file name")
                filename = input()

            with open(filename) as file:
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
            print("\nItems entered")
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

    def fract_knapsack(self):
        """Run fractional knapsack algorithm
        """
        if len(self.items) > 0:
            print("\nListing Fractional Knapsack")

            result = fractional_knapsack(self.items, self.capacity)

            print("Profit:", result['profit'])
            for item in result['knapsack']:
                self.print_fract_knapsack_item(item)
        else:
            print("Invalid. No items entered")

    def print_fract_knapsack_item(self, item, end="\n"):
        print(f"Fraction: {item[0]:.2f}\tItem: {item[1]}", end=end)


if __name__ == "__main__":
    Run().start()
