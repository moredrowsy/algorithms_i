"""
Project 2

- Fractional Knapsack
- Whole Knapsack
"""
import os.path

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
        print("\nSETUP\n-----")

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
        self.setup()

        while True:
            info = f"\nCAPACITY: {self.capacity}\t"

            print(info, end="\n\n")
            print(self.menu, end="\n")
            choice = self.input()

            if choice == "X" or choice == "x":
                break

            self.clear_screen()

            if choice == "1":
                self.knapsack()
            elif choice == "2":
                self.fract_knapsack()
            elif choice == "3":
                self.print_items(self.items, "ITEMS ENTERED")
            elif choice == "4":
                self.change_capacity()
                self.clear_screen()
            elif choice == "5":
                self.add_items()
            elif choice == "6":
                clear = self.input("Clear previous items? (Y/N)")
                if clear == "Y" or clear == "y":
                    self.clear_items()
                self.add_from_file()
            elif choice == "7":
                self.clear_items()
            else:
                pass

    def change_capacity(self, clear_screen=True):
        """User change knapsack capacity"""
        print("Enter knapsack capacity")

        while True:
            try:
                self.capacity = int(self.input())
                if self.capacity > 0:
                    break
                else:
                    raise ValueError()
            except:
                print("Invalid.")

    def add_items(self):
        """User add KnapsackItems from user"""
        err_msg = ""

        while True:
            self.clear_screen()
            self.print_items(self.items, "ITEMS ENTERED")
            print("\nFormat: [WEIGHT] [PROFIT]\nEnter X to stop")

            if err_msg:
                print(err_msg)

            data = self.input()

            if data == "X" or data == "x":
                self.clear_screen()
                self.print_items(self.items, "ITEMS ENTERED")
                break

            try:
                weight, profit = self.process_input(data)
                self.items.append(KnapsackItem(
                    len(self.items) + 1, weight, profit))
                err_msg = ""
            except Exception as err:
                err_msg = "Invalid input. " + str(err)

    def add_from_file(self, filename=None):
        """Populate KnapsackItems from file"""
        err_msg = ""

        if not filename:
            filename = self.input("Enter file name")

        while not os.path.exists(filename):
            print("Path does not exist.")
            filename = self.input()

        with open(filename) as file:
            print()
            for i, line in enumerate(file):
                try:
                    weight, profit = self.process_input(line)
                    self.items.append(KnapsackItem(
                        len(self.items) + 1, weight, profit))
                except Exception as err:
                    err_msg += f"\nInvalid input at line {i}. " + str(err)

        self.clear_screen()
        self.print_items(self.items, "ITEMS ENTERED")

        if err_msg:
            print(err_msg)

    def process_input(self, data):
        """Return valid weight, profit input. Else raises ValueError"""
        weight, profit = 0, 0
        data = data.split()

        if data:
            if len(data) < 2:
                raise ValueError("Missing profit input.")

            try:
                weight = int(data[0])
            except:
                raise ValueError("Weight must be integer.")

            try:
                profit = float(data[1])
            except:
                raise ValueError("Value must be a number.")

            if weight <= 0:
                raise ValueError("Weight must be greater than 0.")
        else:
            raise ValueError("Invalid input.")

        return weight, profit

    def clear_items(self):
        self.items = []
        print("All entered items removed.")

    def print_items(self, items, title=None, fract=False):
        """Print items entered from user or file"""

        if self.items:
            labels = ["ID", "WEIGHT", "PROFIT"]
            width = 10
            fmt_label = "{:<5} {:<{w}} {:<{w}}"
            fmt_data = "{:<5} {:<{w}} {:<{w}.2f}"

            if title:
                print(title, end="\n\n")

            if fract:
                labels = [*labels, "FRACTION"]
                fmt_label += " {:<{w}}"
                fmt_data += " {:<{w}.2f}"

            bar = [5*'-'] + [width*'-' for _ in range(1, len(labels))]
            print(fmt_label.format(*labels, w=width))
            print(fmt_label.format(*bar, w=width))

            if fract:
                for f, item in items:
                    print(fmt_data.format(item.id, item.weight, item.profit, f,
                                          w=width))
            else:
                for item in items:
                    print(fmt_data.format(item.id, item.weight, item.profit,
                                          w=width))
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
        if self.items:
            result = knapsack(self.items, self.capacity)

            title = "0-1 KNAPSACK"
            self.print_items(result['knapsack'], title)
            print(f"\nTOTAL PROFIT: {result['profit']:.2f}")
        else:
            print("No items entered")

    def fract_knapsack(self):
        """Run fractional knapsack algorithm"""
        if self.items:
            result = fractional_knapsack(self.items, self.capacity)

            title = "FRACTIONAL KNAPSACK"
            self.print_items(result['knapsack'], title, fract=True)
            print(f"\nTOTAL PROFIT: {result['profit']:.2f}")
        else:
            print("No items entered")


if __name__ == "__main__":
    Run().start()
