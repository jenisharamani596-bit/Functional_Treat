# 🚀 Functional Treat: Data Analyzer and Transformer Program

> **Project Name:** Functional Treat (Data Analyzer and Transformer Program)  
> **Author:** Jenisha Ramani
> 
A Python-based menu-driven console application designed to manipulate, analyze, and transform data across one-dimensional (1D) and two-dimensional (2D) arrays (lists). 

---

## 🎯 Project Objectives

- **🖥️ User Interface:** Create a menu-driven interface to let users choose from different data transformation and analysis options.
- **📊 Data Input:** Support input for 1D lists or 2D nested lists with options for manual entry.
- **📈 Built-in Functions:** Demonstrate the use of built-in functions like `len()`, `sum()`, `min()`, and `max()`.
- **🔧 User-Defined Functions (UDF):** Create specific functions for tasks like calculating averages, finding duplicates, and unique values.
- **📦 Advanced Arguments (`*args` & `**kwargs`):** Use `*args` to accept multiple values and `**kwargs` for dataset metadata characteristics.
- **🔄 Recursion:** Implement a recursive function to calculate factorials.
- **⚡ Lambda Functions:** Use lambda functions in conjunction with `filter()` to extract data based on user thresholds.
- **🌐 Global Keyword:** Use global variables (`global_summary`) to track dataset metrics across functions.
- **🔃 Sorting Operations:** Sort collection data types in ascending or descending order.

---

## ✨ Features & Functionality

1. **Input Data:** Allows user selection between a 1D array or 2D nested array.
2. **Display Data Summary:** Computes and outputs total elements, minimum, maximum, sum, and average values.
3. **Calculate Factorial:** Computes factorials dynamically using recursion.
4. **Filter Data by Threshold:** Filters list elements greater than or equal to a specified user threshold using lambda functions.
5. **Sort Data:** Rearranges dataset elements in ascending or descending orders.
6. **Display Dataset Statistics:** Returns multiple statistical values leveraging `*args` and `**kwargs`.

---

## 💻 Technologies Used

- **Python 3**
- **Visual Studio Code**
- **Git & GitHub**

---

## 📂 Project Structure

```text
Functional_Treat/
│
├── Functional_Treat.py     # Main Python script containing program logic
├── README.md               # Project documentation
├── output1.png             # Screenshot of Data Input & Built-in Summary
├── output2.png             # Screenshot of Filtering, Sorting & Statistics
└── output3.png             # Screenshot of Final Statistics & Program Exit
🖥️ Complete Console Output Demonstration
Welcome to the Data Analyzer and Transformer Program

Main Menu:
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program
Please enter your choice: 1
Enter 1 for 1D array or 2 for 2D array: 1
Enter data for a 1D array (separated by spaces): 34 12 56 78 43 21 90
Data has been stored successfully!

Main Menu:
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program
Please enter your choice: 2

Data Summary:
- Total elements: 7
- Minimum value: 12
- Maximum value: 90
- Sum of all values: 334
- Average value: 47.714285714285715

Main Menu:
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program
Please enter your choice: 3
Enter a number to calculate its factorial: 5
Factorial of 5 is: 120

Main Menu:
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program
Please enter your choice: 4
Enter a threshold value to filter out data above this value: 50
Filtered Data (values >= 50 ):
[56, 78, 90]

Main Menu:
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program
Please enter your choice: 5

Choose sorting option:
1. Ascending
2. Descending
Enter your choice: 1
Sorted Data in Ascending Order:
[12, 21, 34, 43, 56, 78, 90]

Main Menu:
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program
Please enter your choice: 6

Dataset Information:
- total_elements : 7
- data_type : 1D/2D Array

Dataset Statistics:
- Minimum value: 12
- Maximum value: 90
- Sum of all values: 334
- Average value: 47.71

Main Menu:
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program
Please enter your choice: 7

Thank you for using the Data Analyzer and Transformer Program. Goodbye!
