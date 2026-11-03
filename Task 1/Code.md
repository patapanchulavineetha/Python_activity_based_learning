# Case Study: Student Marks Matrix Analysis

## 1. Problem Statement

Develop a Python program to analyse a matrix of student marks across multiple subjects. The program should calculate the total and average marks of each student (row-wise statistics), calculate the average marks of each subject (column-wise statistics), identify the top-performing student, and detect subjects whose average marks are below a specified threshold.

## 2. Algorithm

1. **Start** the program.
2. Initialize a matrix containing marks for each student across different subjects.
3. Store the student names and subject names in lists.
4. Calculate the total marks of each student by adding the marks in each row.
5. Calculate each student's average marks.
6. Calculate the average marks for each subject by adding the marks in each column and dividing by the number of students.
7. Identify the student with the highest average marks.
8. Set the low-performance threshold to 60 marks.
9. Identify subjects whose average marks are below 60.
10. Display the student-wise statistics, subject-wise statistics, top performer, and low-performing subjects.
11. **Stop** the program.


## 3. Sample Input

The program uses the following predefined data.

**Student names:** Ravi, Sita, Kiran, Priya

**Subjects:** Python, Maths, Physics

**Marks matrix:**

| Student | Python | Maths | Physics |
|---|---:|---:|---:|
| Ravi | 85 | 78 | 90 |
| Sita | 65 | 55 | 60 |
| Kiran | 92 | 88 | 95 |
| Priya | 70 | 45 | 50 |

**Low-performance threshold:** 60 marks.

*Note: This program uses predefined input, so you do not need to type the marks when running it.*

## 4. Sample Output

```text
STUDENT MARKS MATRIX ANALYSIS
--------------------------------------------------

Marks Matrix:
Student Python  Maths   Physics
Ravi    85      78      90
Sita    65      55      60
Kiran   92      88      95
Priya   70      45      50

1. STUDENT-WISE STATISTICS
Ravi - Total: 253 Average: 84.33
Sita - Total: 180 Average: 60.0
Kiran - Total: 275 Average: 91.67
Priya - Total: 165 Average: 55.0

2. TOP-PERFORMING STUDENT
Kiran with average marks: 91.67

3. SUBJECT-WISE STATISTICS
Python - Total: 312 Average: 78.0
Maths - Total: 266 Average: 66.5
Physics - Total: 295 Average: 73.75

4. LOW-PERFORMING SUBJECTS
(Average marks below 60)
No low-performing subjects found.
```

**Why are there no low-performing subjects?**

Python has an average of 78, Maths has 66.5, and Physics has 73.75. All three averages are above the threshold of 60 marks.

## 5. Mermaid Flowchart Code

Copy the following code into a Mermaid-compatible editor to generate a flowchart.
 ```mermaid
flowchart TD
    A([Start]) --> B[Initialize Student Names, Subject Names and Marks Matrix]
    B --> C[Calculate Row-wise Student Totals and Averages]
    C --> D[Find Highest Student Average]
    D --> E[Calculate Column-wise Subject Averages]
    E --> F{Is Subject Average Below 60?}
    F -- Yes --> G[Display Low-performing Subject]
    F -- No --> H[Check Next Subject]
    G --> H
    H --> I{More Subjects?}
    I -- Yes --> F
    I -- No --> J[Display Student and Subject Statistics]
    J --> K[Display Top-performing Student]
    K --> L([Stop])
```


## 6. Conclusion

This program analyses student marks using a two-dimensional list (matrix) in Python. It calculates row-wise and column-wise statistics, identifies the student with the highest average, and detects subjects with average marks below 60. It demonstrates the use of lists, nested loops, conditional statements, the `sum()` function, and the `max()` function.

**Important:** The sample output is consistent with the given marks matrix and the threshold of 60 marks.
