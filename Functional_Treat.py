print("Welcome to the Data Analyzer and Transformer Program")

data = []
global_summary = {}


# 1. Input Data
def input_data():
    global data

    choice = input("Enter 1 for 1D array or 2 for 2D array: ")

    if choice == "1":
        values = input("Enter data for a 1D array (separated by spaces): ")
        data = list(map(int, values.split()))

    elif choice == "2":
        rows = int(input("Enter number of rows: "))
        data = []

        for i in range(rows):
            values = input("Enter row " + str(i + 1) + ": ")
            row = list(map(int, values.split()))
            data.append(row)

    else:
        print("Invalid choice!")
        return

    print("Data has been stored successfully!")


# 2. Built-in Functions
def display_summary():
    if not data:
        print("Please enter data first!")
        return

    if isinstance(data[0], list):
        values = [x for row in data for x in row]
    else:
        values = data

    print("\nData Summary:")
    print("- Total elements:", len(values))
    print("- Minimum value:", min(values))
    print("- Maximum value:", max(values))
    print("- Sum of all values:", sum(values))
    print("- Average value:", sum(values) / len(values))


# 3. Recursion
def factorial(n):
    """Calculate factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def calculate_factorial():
    n = int(input("Enter a number to calculate its factorial: "))

    if n < 0:
        print("Factorial is not possible for negative numbers.")
    else:
        print("Factorial of", n, "is:", factorial(n))


# 4. Lambda Function
def filter_data():
    if not data:
        print("Please enter data first!")
        return

    if isinstance(data[0], list):
        values = [x for row in data for x in row]
    else:
        values = data

    threshold = int(input(
        "Enter a threshold value to filter out data above this value: "
    ))

    # Lambda + filter
    result = list(filter(lambda x: x >= threshold, values))

    print("Filtered Data (values >=", threshold, "):")
    print(result)


# 5. Sorting
def sort_data():
    if not data:
        print("Please enter data first!")
        return

    if isinstance(data[0], list):
        values = [x for row in data for x in row]
    else:
        values = data.copy()

    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = input("Enter your choice: ")

    if choice == "1":
        values.sort()
        print("Sorted Data in Ascending Order:")
        print(values)

    elif choice == "2":
        values.sort(reverse=True)
        print("Sorted Data in Descending Order:")
        print(values)

    else:
        print("Invalid choice!")


# 6. Return Multiple Values
def dataset_statistics(*args, **kwargs):
    """
    Return minimum, maximum, sum and average.
    *args accepts multiple values.
    **kwargs displays dataset information.
    """

    minimum = min(args)
    maximum = max(args)
    total = sum(args)
    average = total / len(args)

    print("\nDataset Information:")
    for key, value in kwargs.items():
        print("-", key, ":", value)

    return minimum, maximum, total, average


def display_statistics():
    if not data:
        print("Please enter data first!")
        return

    if isinstance(data[0], list):
        values = [x for row in data for x in row]
    else:
        values = data

    minimum, maximum, total, average = dataset_statistics(
        *values,
        total_elements=len(values),
        data_type="1D/2D Array"
    )

    print("\nDataset Statistics:")
    print("- Minimum value:", minimum)
    print("- Maximum value:", maximum)
    print("- Sum of all values:", total)
    print("- Average value:", round(average, 2))


# Extra UDF Examples
def calculate_average(numbers):
    """Calculate average of numbers."""
    return sum(numbers) / len(numbers)


def find_duplicates(numbers):
    """Find duplicate values."""
    duplicates = []

    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)

    return duplicates


def unique_values(numbers):
    """Return unique values."""
    return list(set(numbers))


# Main Menu
while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice = input("Please enter your choice: ")

    if choice == "1":
        input_data()

    elif choice == "2":
        display_summary()

    elif choice == "3":
        calculate_factorial()

    elif choice == "4":
        filter_data()

    elif choice == "5":
        sort_data()

    elif choice == "6":
        display_statistics()

    elif choice == "7":
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
