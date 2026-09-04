"""
Lab 1: Package Tracking with Binary Search

CISC 4080 - Computer Algorithms

In this lab, you will compare linear search and binary search on a simulated
package-tracking dataset.

Note:
- The dataset is generated automatically by this file.
- The same input size always produces the same dataset because a fixed seed is used.
- Package records are already sorted by tracking ID, which allows binary search.
"""

import random
import time

# DO NOT MODIFY THESE CODE
CITIES = [
    "New York",
    "Boston",
    "Chicago",
    "Seattle",
    "Miami",
    "Los Angeles",
    "Dallas",
    "Atlanta",
    "Denver",
    "San Francisco",
]

STATUSES = [
    "Processing",
    "In Transit",
    "Out for Delivery",
    "Delivered",
]


def generate_packages(n, seed=4080):
    """
    Generate n package records.

    Each package is represented as a tuple:
        (tracking_id, city, status)

    Example:
        (152341, "Boston", "In Transit")

    The returned list is sorted by tracking_id.

    Parameters
    ----------
    n : int
        Number of package records to generate.
    seed : int
        Random seed used to make the dataset reproducible.

    Returns
    -------
    list
        A sorted list of package tuples.
    """
    if n <= 0:
        return []

    # We use a large ID range so that we can generate large datasets
    # without duplicate tracking IDs.
    rng = random.Random(seed + n)

    tracking_ids = rng.sample(range(100000000, 999999999), n)
    tracking_ids.sort()

    packages = []

    for tracking_id in tracking_ids:
        city = rng.choice(CITIES)
        status = rng.choice(STATUSES)
        packages.append((tracking_id, city, status))

    return packages


def linear_search(packages, target_id):
    """
    Search for target_id using linear search.

    TODO: Complete this function.

    Return:
        The package tuple if found, otherwise None.
    """
    # Write your code here



def binary_search(packages, target_id):
    """
    Search for target_id using binary search.

    TODO: Complete this function.

    Return:
        The package tuple if found, otherwise None.

    Requirement:
        Implement binary search yourself.
        Do NOT use list.index(), bisect, pandas, NumPy search functions,
        dictionaries, sets, or any other built-in searching shortcut.
    """
    # Write your code here





def main():
    # ------------------------------------------------------------
    # Part 1: Small example
    # ------------------------------------------------------------
    packages = generate_packages(20)

    print("First five package records:")
    for package in packages[:5]:
        print(package)

    print()

    # ------------------------------------------------------------
    # Part 2: Package lookup questions
    # ------------------------------------------------------------
    # Use this dataset for the required package lookup questions.
    lookup_packages = generate_packages(50000)

    required_tracking_ids = [
        105666090,
        320426228,
        876349143,
        999999999,
    ]

    print("Required Package Lookups")
    print("------------------------")

    for tracking_id in required_tracking_ids:
        print(f"\nSearching for package {tracking_id}")

        # TODO:
        # Call your binary_search() function and print the package information.
        #
        # Example:
        # result = binary_search(lookup_packages, tracking_id)
        # print_package_result(result)

    # ------------------------------------------------------------
    # Part 3: Runtime experiment
    # ------------------------------------------------------------
    input_sizes = [
        100,
        500,
        1000,
        5000,
        10000,
        100000,
        500000
    ]

    print("\n\nRuntime Experiment")
    print("------------------")
    print("Compare linear search and binary search as n increases.\n")

    for n in input_sizes:
        packages = generate_packages(n)

        # Use the final package as the target.
        # For linear search, this creates a worst-case successful search.
        target_id = packages[-1][0]

        # TODO:
        # 1. Measure the average runtime of linear_search().
        # 2. Measure the average runtime of binary_search().
        # 3. Print n and both average runtimes.
        #
        # Hint:
        # use the time module we introduced in class to measure the running time of the algorithms
        


if __name__ == "__main__":
    main()
