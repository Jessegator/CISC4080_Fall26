# Lab 4: Hash Tables & Searching - NYC Film Permit Lookup System

## Overview

In this lab, you will build a small **NYC Film Permit Lookup System** using hash tables. You will implement and compare two collision-resolution approaches:

1. **Separate Chaining**
2. **Open Addressing**, supporting both:
   - Linear Probing
   - Quadratic Probing

The goal is not only to implement `insert`, `search`, and `delete`, but also to observe how collisions, load factor, probing, and resizing affect a real hash table.

> **Important:** You may use Python lists and the provided CSV-loading code, but you may **not** use Python dictionaries (`dict`) as the hash table implementation.



# Submission Requirements 

- Submit your code as lab4_{your_name}.py
- Submit a separate document (pdf or word doc) with the table and answers to the questions provided in this README.
- Make sure your program runs without errors before submission.
- Your program must:

  - Use `EventID` as the hash-table key.
  - Implement the division hash function `key % capacity`.
  - Start both hash-table implementations with capacity `101` by default.
  - Implement `load_factor()` for both hash-table classes.
  - Implement separate chaining using linked nodes.
  - Implement open addressing with **both linear and quadratic probing**.
  - Select the probing strategy through the `probing_method` argument of `OpenAddressingHashTable.__init__()`.
  - Correctly handle deletion in open addressing using `DELETED`.
  - Implement resizing and rehash existing records.
  - Track collisions and probes for open addressing.
  - Test successful and unsuccessful searches.
  - Delete at least one existing record and verify that it can no longer be found.
  - Do not use Python `dict` as a replacement for your hash table.



## Dataset: NYC Film Permits

This lab uses a real dataset from [**NYC Open Data**](https://data.cityofnewyork.us/City-Government/Film-Permits-in-Queens-and-Brooklyn/qken-wcxe/about_data), provided by the NYC Mayor's Office of Media and Entertainment (MOME). Each row represents a film permit. We will use the smaller **Film Permits in Queens and Brooklyn** dataset rather than the complete NYC dataset.

The dataset contains fields such as:

- `EventID` — unique identification number for the permit
- `EventType` — type of permitted activity
- `StartDateTime` / `EndDateTime`
- `Borough`
- `Category`
- `SubCategoryName`
- `Country`
- `ZipCode(s)`

For this lab, **`EventID` will be the key** of the hash table, and the complete permit record will be the value.

**The dataset is provided in this repo. You should download and place it in the same folder as your code.**



# Part 1 — Loading the Film Permit Data

The CSV-loading code is already provided in `lab4.py`.

Each CSV row is converted into a `FilmPermit` object. For example:

```python
permit.event_id
permit.event_type
permit.borough
permit.category
```

You do **not** need to implement the CSV parser.

Before implementing the hash tables, run the starter program and make sure that the dataset loads successfully.



# Part 2 — Hash Function

Both hash-table implementations will use the same hash function.

Because `EventID` is an integer, use the **division method**:

$$
h(k) = k \bmod m
$$

where:

- $k$ is the `EventID`
- $m$ is the current capacity of the hash table
- $h(k)$ is the initial array index

For example, if:

```text
EventID = 718094
capacity = 101
```

then:

```text
718094 % 101 = 85
```

so the initial hash-table index is `85`.

Implement:

```python
def hash_function(self, key):
    # TODO
```

Do **not** use Python's built-in `hash()` function for this lab.



# Part 3 — Initial Capacity and Load Factor

Both hash tables should start with an initial capacity of:

```python
INITIAL_CAPACITY = 101
```

`101` is prime and gives us a relatively small table at the beginning so that collisions and resizing can be observed during the lab.

The **load factor** is:

$$
\alpha = \frac{n}{m}
$$

where:

- $n$ = number of records currently stored
- $m$ = current table capacity

Both hash-table classes must implement:

```python
def load_factor(self):
    # TODO
```

For example, if 60 records are stored in a table with capacity 101:

$$
\alpha = \frac{60}{101} \approx 0.594
$$



# Part 4 — Separate Chaining Hash Table

Implement:

```python
class ChainingHashTable:
    def __init__(self, capacity=101, max_load_factor=1.0):
        ...
```

Each array position represents a **bucket**. If multiple keys map to the same index, store them in a linked list at that bucket.

A `Node` class is provided in `lab4.py`.

Example:

```text
Index 0   None
Index 1   [Permit A] -> [Permit B] -> None
Index 2   [Permit C] -> None
Index 3   None
```

You must at least implement:

```python
hash_function(key)
load_factor()
insert(key, value)
search(key)
delete(key)
resize()
```

### Resizing

For this lab, resize the chaining table when:

```text
load factor > max_load_factor
```

The default `max_load_factor` is `1.0`.

When resizing, create a larger table and **rehash all existing records**. Do not simply copy records to the same array indices, because the hash function depends on the capacity.



# Part 5 — Open Addressing Hash Table

Implement:

```python
class OpenAddressingHashTable:
    def __init__(
        self,
        capacity=101,
        probing_method="linear",
        max_load_factor=0.70
    ):
        ...
```

`probing_method` must accept:

```python
"linear"
"quadratic"
```

Any other value should raise a `ValueError`.

This allows us to create different tables using the same class:

```python
linear_table = OpenAddressingHashTable(
    capacity=101,
    probing_method="linear"
)

quadratic_table = OpenAddressingHashTable(
    capacity=101,
    probing_method="quadratic"
)
```

You must at least implement:

```python
hash_function(key)
load_factor()
_probe_index(key, i)
insert(key, value)
search(key)
delete(key)
resize()
```



## Linear Probing

If a collision occurs, linear probing checks the next position:

$$
h(k,i) = (h(k)+i) \bmod m
$$

for:

$$
i=0,1,2,3,\ldots
$$

Example:

```text
Original index = 20

20 -> occupied
21 -> occupied
22 -> empty

Insert at index 22
```



## Quadratic Probing

Quadratic probing uses increasingly larger offsets:

$$
h(k,i) = (h(k)+i^2) \bmod m
$$

for:

$$
i=0,1,2,3,\ldots
$$

Example:

```text
Original index = 20

20 + 0^2 -> 20
20 + 1^2 -> 21
20 + 2^2 -> 24
20 + 3^2 -> 29
...
```

Use the selected `probing_method` inside `_probe_index()` so that the rest of your open-addressing implementation can work with either strategy.



# Part 6 — Deletion in Open Addressing

Deletion requires special attention in an open-addressing hash table.

Consider:

```text
Index 20   A
Index 21   B
Index 22   C
```

Suppose `A`, `B`, and `C` originally collided. If `A` is replaced directly with `None`, a later search may stop at index 20 and incorrectly conclude that `B` or `C` does not exist.

Therefore, the starter code provides a special marker:

```python
DELETED = object()
```

Use this marker when deleting an item from the open-addressing table.

Your `search()` and `insert()` methods must correctly handle `DELETED` positions.



# Part 7 — Insert the Dataset

Load the CSV file:

```python
permits = load_permits("Film_Permits_in_Queens_and_Brooklyn_20261002.csv")
```

Create all three configurations:

```python
chaining_table = ChainingHashTable()

linear_table = OpenAddressingHashTable(
    probing_method="linear"
)

quadratic_table = OpenAddressingHashTable(
    probing_method="quadratic"
)
```

Insert every permit using:

```python
key = permit.event_id
value = permit
```

For example:

```python
for permit in permits:
    chaining_table.insert(permit.event_id, permit)
```

Repeat for the linear-probing and quadratic-probing tables.

After insertion, print the following statistics for each table:

```text
Number of records
Current capacity
Load factor
Number of collisions
```

For open addressing, also report:

```text
Probing method
Total probes
Maximum probes for a single operation
```



# Part 8 — Search for Film Permits

Select at least **five existing EventIDs** from the dataset and search for them in all three tables.

For each search, print whether the permit was found and display the permit information.

Example:

```text
Searching for EventID: 718094

Permit found:
EventID: 718094
Event Type: Shooting Permit
Borough: Queens
Category: ...
```

Also search for at least **two EventIDs that do not exist** in the dataset. Your program should return `None` rather than crash.



# Part 9 — Delete and Search Again

Choose at least **one existing permit**.

Perform the following experiment separately for all three tables:

1. Search for the EventID and verify that it exists.
2. Delete the EventID.
3. Search for the same EventID again.
4. Verify that the second search returns `None`.

Example:

```text
Before deletion:
search(718094) -> Permit found

Deleting 718094...

After deletion:
search(718094) -> None
```

For the open-addressing implementations, verify that deleting one item does **not** prevent other items in the same probing sequence from being found.



# Part 10 — Collision and Probing Experiment

Run the same dataset using:

1. Separate Chaining
2. Linear Probing
3. Quadratic Probing

Record your results in a table similar to:

| Implementation | Final Capacity | Load Factor | Collisions | Total Probes | Max Probes |
|---|---:|---:|---:|---:|---:|
| Separate Chaining | | | | N/A | N/A |
| Linear Probing | | | | | |
| Quadratic Probing | | | | | |

Your values must come from your actual program execution.



# Part 11 — Analysis Questions

Answer the following questions in your submission. A few sentences for each question are sufficient.

### Q1. Hash Function

Explain how the following hash function converts an `EventID` into a table index:

$$
h(k)=k\bmod m
$$

What happens to the index when the table capacity changes?

### Q2. Collision Resolution

Explain the difference between how **separate chaining** and **open addressing** handle a collision.

### Q3. Linear vs. Quadratic Probing

Based on your experiment, how did linear probing and quadratic probing behave differently? Compare their collision/probe statistics.

### Q4. Load Factor

What is the load factor of a hash table? Why is load factor especially important for open addressing?

### Q5. Resizing

Why must all records be **rehashed** after the table capacity changes?

### Q6. Deletion

Why is setting a deleted position directly to `None` potentially incorrect for open addressing? What is the purpose of the `DELETED` marker?

### Q7. Comparison

Based on your implementation and experiment, describe one advantage and one disadvantage of:

- Separate chaining
- Open addressing
