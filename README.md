# 004_Functional_treat

# 📊 Data Analyzer & Transformer

A Python-based **Data Analyzer & Transformer** console application created to practice core Python programming and data-handling concepts.

The project accepts numerical data in **1D or 2D list format** and performs data transformation, summary calculations, filtering, sorting, recursion, and function-based operations.

It also demonstrates important Python concepts such as **global variables, functions, list comprehension, lambda functions, recursion, `*args`, `**kwargs`, and multiple return values**.

---

## 📌 Project Overview

The **Data Analyzer & Transformer** provides a simple menu-driven interface for working with numerical datasets.

The user can:

* 📥 Enter 1D data
* 📥 Enter 2D data
* 🔄 Convert 2D data into 1D data
* 📊 Generate a data summary
* 🔢 Calculate factorial using recursion
* 🔎 Filter values using lambda
* 🔃 Sort numerical data
* 📈 Calculate minimum, maximum and average
* 📦 Demonstrate `*args`
* 🗂️ Demonstrate `**kwargs`
* 🚪 Exit the application

---

# 🎯 Project Objectives

This project was created to practice:

* Python functions
* Global variables
* 1D and 2D lists
* Data transformation
* List comprehension
* Built-in functions
* Recursion
* Lambda functions
* Filtering
* Sorting
* `*args`
* `**kwargs`
* Multiple return values
* Tuple unpacking
* Dictionaries
* Loops
* Conditional statements
* Menu-driven programming

---

# 🛠️ Technologies Used

* **Python 3**
* Python Lists
* Functions
* Dictionaries
* List Comprehension
* Lambda
* `filter()`
* `sort()`
* `sorted()`
* Recursion
* `*args`
* `**kwargs`
* Global Variables
* Built-in Functions

---

# 📂 Project Structure

```text
Data-Analyzer-Transformer/
│
├── data_analyzer.py
└── README.md
```

---

# 🗃️ Global Dataset

The program starts with two global variables:

```python
data = []
summary = {}
```

### `data`

The `data` variable stores the numerical dataset entered by the user.

### `summary`

The `summary` dictionary stores the calculated characteristics of the dataset.

The program uses the `global` keyword inside functions to modify these global variables.

---

# 📥 1. Input Data

The `input_data()` function allows the user to enter either a **1D list** or a **2D list**.

The user is asked:

```text
Enter 1 for 1D list, 2 for 2D list:
```

---

## 1D List Example

If the user selects `1`:

```text
Enter numbers separated by space: 10 20 30 40 50
```

The data becomes:

```python
[10, 20, 30, 40, 50]
```

The input is converted into integers using:

```python
list(map(int, input().split()))
```

---

## 2D List Example

If the user selects `2`, the program asks for the number of rows.

Example:

```text
Enter number of rows: 3

Row 1: 10 20 30
Row 2: 40 50 60
Row 3: 70 80 90
```

The data becomes:

```python
[
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

---

# 🔄 2. Data Flattening

The `flatten_data()` function converts a 2D list into a 1D list.

```python
def flatten_data(d):
    if isinstance(d[0], list):
        return [item for row in d for item in row]
    return d
```

### Example

Input:

```python
[
    [10, 20],
    [30, 40],
    [50, 60]
]
```

Output:

```python
[10, 20, 30, 40, 50, 60]
```

This allows the other analysis functions to work with both 1D and 2D input.

---

# 📊 3. Data Summary

The `data_summary()` function calculates basic statistics from the dataset.

The following values are calculated:

| Statistic | Function        |
| --------- | --------------- |
| Count     | `len()`         |
| Sum       | `sum()`         |
| Minimum   | `min()`         |
| Maximum   | `max()`         |
| Average   | `sum() / len()` |

The result is stored in the `summary` dictionary.

```python
summary = {
    "Count": len(flat),
    "Sum": sum(flat),
    "Min": min(flat),
    "Max": max(flat),
    "Average": sum(flat) / len(flat)
}
```

### Example

For:

```python
[10, 20, 30, 40, 50]
```

The output is:

```text
--- Data Summary ---
Count : 5
Sum : 150
Min : 10
Max : 50
Average : 30.0
```

---

# 🔢 4. Factorial Using Recursion

The project demonstrates **recursion** through the `factorial()` function.

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```

The function calls itself until the base condition is reached.

### Example

For:

```text
5
```

The calculation is:

```text
5 × 4 × 3 × 2 × 1
```

Result:

```text
Factorial = 120
```

---

# 🔎 5. Lambda Filter

The `lambda_filter()` function filters the dataset using a lambda function.

The condition used is:

```python
lambda x: x > threshold
```

The program uses:

```python
filter()
```

to select values greater than the threshold.

### Example

Data:

```python
[10, 20, 30, 40, 50]
```

Threshold:

```text
25
```

Output:

```text
Filtered values: [30, 40, 50]
```

---

# 🔃 6. Sorting Demo

The `sorting_demo()` function demonstrates two Python sorting methods.

### `sort()`

```python
flat.sort()
```

Sorts the list in ascending order.

### `sorted()`

```python
sorted(flat, reverse=True)
```

Returns the data sorted in descending order.

### Example

```text
Original: [40, 10, 30, 20]

Sorted using sort(): [10, 20, 30, 40]

Sorted using sorted(): [40, 30, 20, 10]
```

---

# 📦 7. `*args`

The project demonstrates variable-length positional arguments using:

```python
def show_args(*args):
```

Example:

```python
show_args(10, 20, 30)
```

Output:

```text
Values using *args: (10, 20, 30)
```

The values passed through `*args` are collected together for processing inside the function.

---

# 🗂️ 8. `**kwargs`

The project also demonstrates variable-length keyword arguments:

```python
def show_kwargs(**kwargs):
```

The program passes the `summary` dictionary using:

```python
show_kwargs(**summary)
```

The function then displays each key and value.

Example:

```text
--- Dataset Characteristics ---
Count : 5
Sum : 150
Min : 10
Max : 50
Average : 30.0
```

---

# 🔢 9. Returning Multiple Values

The `return_multiple()` function returns three values:

```python
return min(flat), max(flat), sum(flat) / len(flat)
```

These values represent:

* Minimum
* Maximum
* Average

The returned values are unpacked:

```python
mn, mx, avg = return_multiple()
```

Output:

```text
Min: 10 Max: 50 Average: 30.0
```

---

# 🧮 Python Built-in Functions Used

| Function       | Purpose                      |
| -------------- | ---------------------------- |
| `input()`      | Takes user input             |
| `print()`      | Displays output              |
| `int()`        | Converts input into integer  |
| `list()`       | Creates a list               |
| `map()`        | Applies conversion to values |
| `len()`        | Counts elements              |
| `sum()`        | Calculates total             |
| `min()`        | Finds minimum value          |
| `max()`        | Finds maximum value          |
| `filter()`     | Filters values               |
| `isinstance()` | Checks object type           |
| `sorted()`     | Sorts data                   |

---

# 🔁 Main Menu

The application uses a continuous `while True` loop.

```text
====== MAIN MENU ======

1. Input Data
2. Display Data Summary
3. Calculate Factorial (Recursion)
4. Lambda Filter
5. Sorting Demo
6. Return Multiple Values
7. Show *args & **kwargs
8. Exit
```

The selected option calls the corresponding function.

---

# 🔄 Program Workflow

```text
                 START
                   │
                   ▼
             Display Menu
                   │
                   ▼
              Input Data
             /          \
           1D            2D
            \            /
             \          /
              ▼        ▼
             Flatten Data
                   │
                   ▼
             Analyze Data
          /      |       \
      Summary  Filter   Sorting
          \      |       /
           \     |      /
             ▼   ▼     ▼
          Other Functions
          /             \
      Recursion      *args/**kwargs
             \         /
              ▼       ▼
               Exit?
              /     \
            No       Yes
            │         │
            └─ Menu   ▼
                    END
```

---

# 📋 Features

| Feature            | Description                          |
| ------------------ | ------------------------------------ |
| 📥 Data Input      | Supports 1D and 2D numerical lists   |
| 🔄 Flattening      | Converts 2D data into 1D             |
| 📊 Summary         | Count, Sum, Min, Max, Average        |
| 🔢 Recursion       | Factorial calculation                |
| 🔎 Lambda          | Filters values above threshold       |
| 🔃 Sorting         | Demonstrates `sort()` and `sorted()` |
| 📦 `*args`         | Demonstrates positional arguments    |
| 🗂️ `**kwargs`     | Demonstrates keyword arguments       |
| 🔢 Multiple Return | Returns three calculated values      |
| 🔄 Menu            | Interactive console interface        |

---

# 🧪 Example Run

```text
====== MAIN MENU ======

1. Input Data
2. Display Data Summary
3. Calculate Factorial (Recursion)
4. Lambda Filter
5. Sorting Demo
6. Return Multiple Values
7. Show *args & **kwargs
8. Exit

Enter your choice: 1

Enter 1 for 1D list, 2 for 2D list: 1
Enter numbers separated by space: 10 20 30 40 50

Data stored successfully!
```

### Data Summary

```text
Enter your choice: 2

--- Data Summary ---
Count : 5
Sum : 150
Min : 10
Max : 50
Average : 30.0
```

### Lambda Filter

```text
Enter your choice: 4

Enter threshold: 25

Filtered values: [30, 40, 50]
```

### Factorial

```text
Enter your choice: 3

Enter number: 5
Factorial = 120
```

---

# 🧩 Function Overview

| Function                | Purpose                      |
| ----------------------- | ---------------------------- |
| `input_data()`          | Takes 1D or 2D input         |
| `data_summary()`        | Calculates dataset summary   |
| `flatten_data()`        | Converts 2D list into 1D     |
| `factorial()`           | Performs recursive factorial |
| `calculate_factorial()` | Takes factorial input        |
| `lambda_filter()`       | Filters dataset              |
| `show_args()`           | Demonstrates `*args`         |
| `show_kwargs()`         | Demonstrates `**kwargs`      |
| `sorting_demo()`        | Demonstrates sorting         |
| `return_multiple()`     | Returns min, max and average |

---

# 📚 Key Learning Outcomes

After completing this project, the following Python concepts are practiced:

### Core Python

* Variables
* Lists
* Dictionaries
* Loops
* Conditions
* User Input

### Functions

* Function creation
* Parameters
* Return values
* Multiple return values
* Global variables

### Data Handling

* 1D lists
* 2D lists
* Flattening
* List comprehension
* Sorting
* Filtering

### Advanced Python Concepts

* Recursion
* Lambda functions
* `*args`
* `**kwargs`
* Tuple unpacking

---

# 💼 Data Analytics Connection

This project provides a basic introduction to the workflow used in data analysis.

```text
Raw Data
   ↓
Data Input
   ↓
Data Transformation
   ↓
Data Summary
   ↓
Filtering
   ↓
Sorting
   ↓
Basic Insights
```

The same general process is used when working with larger datasets in tools such as **Pandas, NumPy, Excel, SQL, and Power BI**.

---

# 🚀 How to Run

## Step 1 — Install Python

Check whether Python is installed:

```bash
python --version
```

---

## Step 2 — Save the Program

Save the code as:

```text
data_analyzer.py
```

---

## Step 3 — Open Terminal

Navigate to the project folder:

```bash
cd path\to\Data-Analyzer-Transformer
```

---

## Step 4 — Run

```bash
python data_analyzer.py
```

The main menu will appear.

---

# ⚠️ Important Notes

* The program expects numerical input for datasets.
* The factorial function expects an integer.
* The program currently does not include `try-except` validation for invalid numerical input.
* `lambda_filter()` requires data to be available.
* `sorting_demo()` requires data to be available.
* `return_multiple()` requires data to be available.
* `show_kwargs(**summary)` displays the currently calculated summary.
* The program stores data only during the current execution.
* No external database or file storage is used.

---

# 🔮 Future Improvements

The project can be extended with:

* CSV file import
* CSV export
* Pandas integration
* NumPy integration
* Data cleaning
* Missing-value handling
* Median calculation
* Standard deviation
* Variance
* Percentiles
* Data visualization
* Matplotlib charts
* Excel integration
* SQL database integration
* Power BI dashboard integration

---

# 📌 Project Highlights

* 🐍 Python Data Analysis Project
* 📊 1D & 2D Data Handling
* 🔄 Data Transformation
* 📈 Basic Statistical Summary
* 🔢 Recursive Factorial
* 🔎 Lambda Filtering
* 🔃 Sorting Operations
* 📦 `*args`
* 🗂️ `**kwargs`
* 🔢 Multiple Return Values
* 🧠 Core Python Concepts
* 💻 Menu-Driven Application

---

# 👨‍💻 Author

**Hardik Kumawat**

Data Analytics Learner | Python | SQL | Excel | Power BI

---

## ⭐ Project Purpose

This project was developed as a practical Python learning project to strengthen **data handling, functions, recursion, lambda expressions, sorting, filtering, and core Python programming concepts** while building a simple console-based data analysis application.
