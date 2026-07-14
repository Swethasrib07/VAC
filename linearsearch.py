import time


class LinearSearchAnalyzer:

    def __init__(self):
        self.data = []

    # Create Array
    def create_array(self):
        self.data = []

        print("\nEnter integers (Type 'done' to finish):")

        while True:
            value = input(">> ")

            if value.lower() == "done":
                break

            try:
                self.data.append(int(value))
            except ValueError:
                print("Please enter a valid integer.")

        print("\nArray created successfully!")

    # Display Array
    def display_array(self):
        if not self.data:
            print("\nArray is empty.")
        else:
            print("\nCurrent Array:", self.data)

    # Linear Search
    def linear_search(self):
        if not self.data:
            print("\nPlease create an array first.")
            return

        try:
            target = int(input("\nEnter element to search: "))
        except ValueError:
            print("Invalid input.")
            return

        start = time.perf_counter()

        positions = []

        for i in range(len(self.data)):
            if self.data[i] == target:
                positions.append(i)

        end = time.perf_counter()

        print("\n========== SEARCH RESULT ==========")

        if positions:
            print(f"Element {target} Found!")
            print("First Position :", positions[0])
            print("All Positions  :", positions)
            print("Occurrences    :", len(positions))
        else:
            print("Element Not Found.")

        print(f"Execution Time : {(end-start)*1000:.6f} ms")

    # Statistics
    def statistics(self):
        if not self.data:
            print("\nArray is empty.")
            return

        print("\n========== ARRAY STATISTICS ==========")
        print("Total Elements :", len(self.data))
        print("Minimum Value  :", min(self.data))
        print("Maximum Value  :", max(self.data))
        print("Sum            :", sum(self.data))
        print("Average        :", round(sum(self.data)/len(self.data), 2))

    # Sort Array
    def sort_array(self):
        if not self.data:
            print("\nArray is empty.")
            return

        self.data.sort()
        print("\nSorted Array:", self.data)

    # Reverse Array
    def reverse_array(self):
        if not self.data:
            print("\nArray is empty.")
            return

        self.data.reverse()
        print("\nReversed Array:", self.data)

    # Remove Duplicates
    def remove_duplicates(self):
        if not self.data:
            print("\nArray is empty.")
            return

        self.data = list(dict.fromkeys(self.data))
        print("\nDuplicates removed successfully.")
        print("Updated Array:", self.data)

    # Even and Odd Numbers
    def even_odd(self):
        if not self.data:
            print("\nArray is empty.")
            return

        even = []
        odd = []

        for num in self.data:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        print("\nEven Numbers:", even)
        print("Odd Numbers :", odd)

    # Insert Element
    def insert_element(self):
        try:
            value = int(input("\nEnter element to insert: "))
            self.data.append(value)
            print("Element inserted successfully.")
        except ValueError:
            print("Invalid input.")

    # Delete Element
    def delete_element(self):
        if not self.data:
            print("\nArray is empty.")
            return

        try:
            value = int(input("\nEnter element to delete: "))

            if value in self.data:
                self.data.remove(value)
                print("Element deleted successfully.")
            else:
                print("Element not found.")

        except ValueError:
            print("Invalid input.")

    # Menu
    def menu(self):

        while True:

            print("\n===================================")
            print("     LINEAR SEARCH ANALYZER")
            print("===================================")
            print("1. Create Array")
            print("2. Display Array")
            print("3. Linear Search")
            print("4. Array Statistics")
            print("5. Sort Array")
            print("6. Reverse Array")
            print("7. Remove Duplicates")
            print("8. Display Even & Odd Numbers")
            print("9. Insert Element")
            print("10. Delete Element")
            print("11. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.create_array()

            elif choice == "2":
                self.display_array()

            elif choice == "3":
                self.linear_search()

            elif choice == "4":
                self.statistics()

            elif choice == "5":
                self.sort_array()

            elif choice == "6":
                self.reverse_array()

            elif choice == "7":
                self.remove_duplicates()

            elif choice == "8":
                self.even_odd()

            elif choice == "9":
                self.insert_element()

            elif choice == "10":
                self.delete_element()

            elif choice == "11":
                print("\nThank you for using Linear Search Analyzer!")
                break

            else:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    app = LinearSearchAnalyzer()
    app.menu()