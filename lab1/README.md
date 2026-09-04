# Lab 1 — Package Tracking with Binary Search

### Overview

Shipping companies such as package-delivery and e-commerce companies maintain large collections of package records. When a customer enters a tracking ID, the system must quickly locate the corresponding package and return information such as its current city and delivery status.

In this lab, you will simulate a package-tracking system and compare two searching algorithms:

- **Linear Search**
- **Binary Search**

You will implement both algorithms, test them on increasingly large datasets, measure their running times, and compare your experimental observations with theoretical time-complexity analysis.

---

## Learning Objectives

After completing this lab, you should be able to:

1. Implement linear search.
2. Implement iterative binary search.
3. Explain why binary search requires sorted data.
4. Analyze the time complexity of both algorithms.
5. Use `time.perf_counter()` to measure the algorithm running time.
6. Compare theoretical time complexity with experimental runtime.
7. Understand why algorithm selection matters when working with large datasets.

---

# 1. Files Provided

You are given:

```text
lab1.py
```

The Python file already contains:

- package-data generation;
- predefined cities and package statuses;
- reproducible random-data generation;
- a runtime-measurement helper function;
- several tracking IDs that you must search for;
- several input sizes for the runtime experiment.

You **do not need to create or download a dataset**.

The dataset is generated automatically when you run the Python file.

---

# 2. Dataset Description

Each package is represented using a Python tuple:

```python
(tracking_id, city, status)
```

For example:

```python
(152341245, "Boston", "In Transit")
```

The three fields are:

| Field | Description | Example |
|---|---|---|
| `tracking_id` | Unique integer identifying the package | `152341245` |
| `city` | Current package location | `"Boston"` |
| `status` | Current delivery status | `"In Transit"` |

A dataset is therefore a Python list containing many package tuples:

```python
packages = [
    (101234567, "Boston", "Delivered"),
    (102981122, "Chicago", "Processing"),
    (105382910, "New York", "In Transit"),
]
```

### Important

The package records are **sorted by tracking ID**.

For example:

```text
101234567
102981122
105382910
...
```

This property is necessary for binary search.

---

# 3. Dataset Generation

The starter file contains:

```python
generate_packages(n)
```

where `n` is the number of package records.

For example:

```python
packages = generate_packages(1000)
```

creates 1,000 package records.

You can also create much larger datasets:

```python
packages = generate_packages(100000)
```

The generator uses a fixed random seed, so the same input size produces the same package dataset each time the program is run.

**Do not modify the `generate_packages()` function.**

---

# 4. Part A — Implement Linear Search

Complete:

```python
def linear_search(packages, target_id):
```

Your function should search through the package records one at a time.

If the tracking ID is found, return the complete package tuple.

Example:

```python
(152341245, "Boston", "In Transit")
```

If the tracking ID does not exist, return:

```python
None
```

---

# 5. Part B — Implement Binary Search

Complete:

```python
def binary_search(packages, target_id):
```

You must implement the binary-search algorithm yourself.

A useful starting structure is:

```text
left = beginning of list
right = end of list

while left <= right:

    find middle position

    if middle tracking ID == target:
        return package

    if target is smaller:
        search left half

    otherwise:
        search right half
```

If the package does not exist, return:

```python
None
```

### Restrictions

For this part, you may **not** use:

- `list.index()`
- Python's `bisect` module
- dictionaries for lookup
- sets for lookup
- any built-in search function that performs the search for you

The purpose of the lab is to implement and analyze binary search.

---

# 6. Part C — Find the Packages

Use the following dataset:

```python
lookup_packages = generate_packages(50_000)
```

The starter code contains these tracking IDs:

```python
105666090
320426228
876349143
999999999
```

Use **your binary-search implementation** to search for each ID.

For every tracking ID, report:

```text
Tracking ID:
Current City:
Status:
```

If a package does not exist, report:

```text
Package not found.
```

Do not manually inspect the generated list to obtain the answers. Your program must obtain the answers using `binary_search()`.

---

# 7. Part D — Runtime Experiment

You will study how the running time changes as the number of package records increases.

Test the following input sizes:

```python
100
1,000
10,000
100,000
500,000
```

The starter code already contains these values.

For every dataset, search for:

```python
packages[-1][0]
```

This is the tracking ID of the final package in the dataset.

This creates a worst-case successful search for linear search.

Measure the running time of:

1. Linear Search
2. Binary Search

A possible output table is:

| Input Size | Linear Search Time | Binary Search Time |
|:--:|:--:|:--:|
| 100 | ... | ... |
| 1,000 | ... | ... |
| 10,000 | ... | ... |
| 100,000 | ... | ... |
| 500,000 | ... | ... |

Your exact measured times may differ depending on your computer.

---

# 8. Part E — Analyze Your Results

Answer the following questions.

### Question 1

What is the worst-case time complexity of linear search?

### Question 2

What is the worst-case time complexity of binary search?

### Question 3

Why does binary search require the data to be sorted?

### Question 4

As the input size increases, what happens to the runtime of linear search?

Does this agree with your theoretical analysis?

### Question 5

As the input size increases, what happens to the runtime of binary search?

Does this agree with your theoretical analysis?

### Question 6

Suppose there are:

```text
1,000,000
```

package records.

Approximately how many package records might linear search inspect in the worst case?

Approximately how many iterations would binary search require in the worst case?

Hint:

```text
log2(1,000,000)
```

### Question 7

Suppose your package data is **not sorted** and you only need to perform **one search**.

Would it necessarily make sense to sort the entire dataset first and then perform binary search?

Explain using time complexity.

### Question 8

Suppose instead that you need to perform **millions of searches** on the same dataset.

Why might maintaining the package records in sorted order be worthwhile?

---

# 9. (Optional) Visualization

You are encouraged to plot the experimental running times.

For example:

```python
import matplotlib.pyplot as plt
```

Plot:

```text
x-axis: input size
y-axis: average running time
```

You may create separate plots for linear search and binary search if the difference in scale makes one curve difficult to see.

**Note:** If `matplotlib` is not installed on your computer, you can install it from the terminal using:

```bash
pip install matplotlib
```

If `pip` does not work, you may also try:

```bash
python -m pip install matplotlib
```

---

# 10. Submission Requirements

Submit:

```text
lab1_{your_name}.py
```

and a short report (word doc of pdf) containing:

1. The results of the four package lookups.
2. Your runtime table.
3. Your answers to Questions 1–8.
4. Optional runtime plots.

Your Python file should:

- run without errors;
- contain your own implementations of linear search and binary search;
- include comments where appropriate;
- produce readable output.
