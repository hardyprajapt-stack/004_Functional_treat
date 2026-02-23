# =========================
# Data Analyzer & Transformer
# =========================

data = []          # Global dataset
summary = {}       # Global summary using global keyword


def input_data():
    """Function to input 1D or 2D list"""
    global data
    choice = int(input("Enter 1 for 1D list, 2 for 2D list: "))

    if choice == 1:
        data = list(map(int, input("Enter numbers separated by space: ").split()))
    else:
        rows = int(input("Enter number of rows: "))
        data = []
        for i in range(rows):
            row = list(map(int, input(f"Row {i+1}: ").split()))
            data.append(row)

    print("Data stored successfully!")


def data_summary():
    """Displays summary using built-in functions"""
    global summary

    if not data:
        print("No data available")
        return

    flat = flatten_data(data)
    summary = {
        "Count": len(flat),
        "Sum": sum(flat),
        "Min": min(flat),
        "Max": max(flat),
        "Average": sum(flat) / len(flat)
    }

    print("\n--- Data Summary ---")
    for k, v in summary.items():
        print(f"{k} : {v}")


def flatten_data(d):
    """Converts 2D list to 1D list"""
    if isinstance(d[0], list):
        return [item for row in d for item in row]
    return d


def factorial(n):
    """Recursive factorial function"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def calculate_factorial():
    """Calculates factorial using recursion"""
    n = int(input("Enter number: "))
    print("Factorial =", factorial(n))


def lambda_filter():
    """Filters values using lambda"""
    flat = flatten_data(data)
    threshold = int(input("Enter threshold: "))
    result = list(filter(lambda x: x > threshold, flat))
    print("Filtered values:", result)


def show_args(*args):
    """Demonstrates *args"""
    print("Values using *args:", args)


def show_kwargs(**kwargs):
    """Demonstrates **kwargs"""
    print("\n--- Dataset Characteristics ---")
    for k, v in kwargs.items():
        print(k, ":", v)


def sorting_demo():
    """Demonstrates sorting"""
    flat = flatten_data(data)
    print("Original:", flat)

    flat.sort()
    print("Sorted using sort():", flat)

    print("Sorted using sorted():", sorted(flat, reverse=True))


def return_multiple():
    """Returns multiple values"""
    flat = flatten_data(data)
    return min(flat), max(flat), sum(flat) / len(flat)


# =========================
# MAIN MENU
# =========================

while True:
    print("\n====== MAIN MENU ======")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial (Recursion)")
    print("4. Lambda Filter")
    print("5. Sorting Demo")
    print("6. Return Multiple Values")
    print("7. Show *args & **kwargs")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        input_data()
    elif choice == 2:
        data_summary()
    elif choice == 3:
        calculate_factorial()
    elif choice == 4:
        lambda_filter()
    elif choice == 5:
        sorting_demo()
    elif choice == 6:
        mn, mx, avg = return_multiple()
        print("Min:", mn, "Max:", mx, "Average:", avg)
    elif choice == 7:
        show_args(10, 20, 30)
        show_kwargs(**summary)
    elif choice == 8:
        print("Program exited successfully!")
        break
    else:
        print("Invalid choice!")