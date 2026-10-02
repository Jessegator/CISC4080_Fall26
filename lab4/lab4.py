"""
Lab 4: Hash Tables & Searching
NYC Film Permit Lookup System

You will implement:
    1. Separate chaining
    2. Open addressing with linear probing
    3. Open addressing with quadratic probing

Do NOT use Python dictionaries as your hash table implementation.
"""

import csv


# -----------------------------------------------------------------------------
# Do not modify
# -----------------------------------------------------------------------------

CSV_FILE = "Film_Permits_in_Queens_and_Brooklyn_20261002.csv"
INITIAL_CAPACITY = 101

# Special marker used by the open-addressing hash table.
# A deleted slot cannot simply become None because that could break a probe
# sequence during a later search.
DELETED = object()


# -----------------------------------------------------------------------------
# Film Permit
# -----------------------------------------------------------------------------

class FilmPermit:
    """Represents one row from the NYC Film Permit dataset."""

    def __init__(
        self,
        event_id,
        event_type,
        start_date,
        end_date,
        borough,
        category,
        subcategory,
        country,
    ):
        self.event_id = event_id
        self.event_type = event_type
        self.start_date = start_date
        self.end_date = end_date
        self.borough = borough
        self.category = category
        self.subcategory = subcategory
        self.country = country

    def __repr__(self):
        return (
            f"FilmPermit(EventID={self.event_id}, "
            f"Type='{self.event_type}', "
            f"Borough='{self.borough}', "
            f"Category='{self.category}')"
        )



# CSV Loading
def load_permits(filename):
    """
    Load film permits from a CSV file.

    This function is provided for you. You do not need to modify it.
    It returns a list of FilmPermit objects.
    """

    permits = []

    # utf-8-sig also handles CSV files that contain a UTF-8 BOM.
    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Skip a malformed row if EventID is missing.
            if not row.get("EventID"):
                continue

            permit = FilmPermit(
                event_id=int(row["EventID"]),
                event_type=row.get("EventType", ""),
                start_date=row.get("StartDateTime", ""),
                end_date=row.get("EndDateTime", ""),
                borough=row.get("Borough", ""),
                category=row.get("Category", ""),
                subcategory=row.get("SubCategoryName", ""),
                country=row.get("Country", ""),
            )

            permits.append(permit)

    return permits



# Node for Separate Chaining
class Node:
    """One node in a separate-chaining linked list."""

    def __init__(self, key, value, next_node=None):
        self.key = key
        self.value = value
        self.next = next_node



# Separate Chaining Hash Table
class ChainingHashTable:
    """
    Hash table using separate chaining.

    Args:
        capacity (int): Initial number of buckets. Default: 101.
        max_load_factor (float): Resize threshold. Default: 1.0.
    """

    def __init__(self, capacity=INITIAL_CAPACITY, max_load_factor=1.0):
        # TODO: Initialize the hash table.
        # Suggested attributes:
        #   self.capacity
        #   self.max_load_factor
        #   self.table
        #   self.size
        #   self.collisions
        pass

    def hash_function(self, key):
        """
        Return the bucket index for key.

        Use the division method:
            h(k) = k % capacity
        """
        # TODO
        pass

    def load_factor(self):
        """Return size / capacity."""
        # TODO
        pass

    def insert(self, key, value):
        """
        Insert a key-value pair into the table.

        If the key already exists, update its value rather than creating a
        duplicate key.

        Remember to handle collisions and resize when necessary.
        """
        # TODO
        pass

    def search(self, key):
        """
        Search for key.

        Returns:
            FilmPermit if found, otherwise None.
        """
        # TODO
        pass

    def delete(self, key):
        """
        Delete key from the table.

        Returns:
            True if an item was deleted, otherwise False.
        """
        # TODO
        pass

    def resize(self):
        """
        Increase the table capacity and rehash all existing records.

        Do NOT simply copy each linked list to the same bucket index.
        The index must be recalculated using the new capacity.
        """
        # TODO
        # Hint: You may approximately double the capacity. Using a prime
        # capacity is recommended.
        pass


# Open Addressing Hash Table
class OpenAddressingHashTable:
    """
    Hash table using open addressing.

    Args:
        capacity (int): Initial table capacity. Default: 101.
        probing_method (str): "linear" or "quadratic".
        max_load_factor (float): Resize threshold. Default: 0.70.

    Example:
        linear = OpenAddressingHashTable(probing_method="linear")
        quadratic = OpenAddressingHashTable(probing_method="quadratic")
    """

    def __init__(
        self,
        capacity=INITIAL_CAPACITY,
        probing_method="linear",
        max_load_factor=0.70,
    ):
        if probing_method not in ("linear", "quadratic"):
            raise ValueError(
                "probing_method must be either 'linear' or 'quadratic'"
            )

        # TODO: Initialize the remaining attributes.
        # Suggested attributes:
        #   self.capacity
        #   self.probing_method
        #   self.max_load_factor
        #   self.table
        #   self.size
        #   self.collisions
        #   self.total_probes
        #   self.max_probes
        pass

    def hash_function(self, key):
        """
        Return the initial table index for key.

        Use:
            h(k) = k % capacity
        """
        # TODO
        pass

    def load_factor(self):
        """Return size / capacity."""
        # TODO
        pass

    def _probe_index(self, key, i):
        """
        Return the index for probe number i.

        Linear probing:
            (h(key) + i) % capacity

        Quadratic probing:
            (h(key) + i^2) % capacity

        i starts at 0.
        """
        # TODO
        pass

    def insert(self, key, value):
        """
        Insert a key-value pair using the selected probing strategy.

        Requirements:
        - Update the value if key already exists.
        - A DELETED position may be reused.
        - Track collisions/probes.
        - Resize when the load-factor threshold would be exceeded.
        """
        # TODO
        pass

    def search(self, key):
        """
        Search for key using the selected probing strategy.

        Important:
        - None means the probe sequence can stop.
        - DELETED means continue probing.

        Returns:
            FilmPermit if found, otherwise None.
        """
        # TODO
        pass

    def delete(self, key):
        """
        Think about what we should do when there is a deletion for seperate chaing

        Returns:
            True if an item was deleted, otherwise False.
        """
        # TODO
        pass

    def resize(self):
        """
        Increase capacity and rehash all active records.

        DELETED markers should NOT be copied into the new table.
        """
        # TODO

        pass



# Helper Functions for Testing
def insert_all(table, permits):
    """Insert all FilmPermit objects into a hash table."""
    for permit in permits:
        table.insert(permit.event_id, permit)


def print_statistics(name, table):
    """Print basic statistics for one hash table."""
    print(f"\n--- {name} ---")
    print(f"Records: {table.size}")
    print(f"Capacity: {table.capacity}")
    print(f"Load factor: {table.load_factor():.3f}")
    print(f"Collisions: {table.collisions}")

    # Open-addressing tables have additional probing statistics.
    if isinstance(table, OpenAddressingHashTable):
        print(f"Probing method: {table.probing_method}")
        print(f"Total probes: {table.total_probes}")
        print(f"Maximum probes: {table.max_probes}")


def deletion_test(table, event_id):
    """
    Test search -> delete -> search for one EventID.

    You may use this helper in your experiments.
    """
    print(f"\nTesting deletion of EventID {event_id}")

    before = table.search(event_id)
    print("Before deletion:", before)

    deleted = table.delete(event_id)
    print("Deleted:", deleted)

    after = table.search(event_id)
    print("After deletion:", after)

    if before is not None and deleted and after is None:
        print("Deletion test passed.")
    else:
        print("Deletion test failed.")




def main():
    # The CSV-loading portion is already completed for you.
    try:
        permits = load_permits(CSV_FILE)
    except FileNotFoundError:
        print(f"Could not find '{CSV_FILE}'.")
        print("Place the CSV file in the same folder as lab4.py.")
        return

    print(f"Loaded {len(permits)} film permits.")

    if permits:
        print("Example record:")
        print(permits[0])

    # ------------------------------------------------------------------
    # TODO 1: Create all three hash-table configurations.
    # ------------------------------------------------------------------

    # chaining_table = ChainingHashTable()

    # linear_table = OpenAddressingHashTable(
    #     probing_method="linear"
    # )

    # quadratic_table = OpenAddressingHashTable(
    #     probing_method="quadratic"
    # )

    # ------------------------------------------------------------------
    # TODO 2: Insert all permits into each table.
    # ------------------------------------------------------------------

    # insert_all(chaining_table, permits)
    # insert_all(linear_table, permits)
    # insert_all(quadratic_table, permits)

    # ------------------------------------------------------------------
    # TODO 3: Print statistics for all three tables.
    # ------------------------------------------------------------------

    # print_statistics("Separate Chaining", chaining_table)
    # print_statistics("Linear Probing", linear_table)
    # print_statistics("Quadratic Probing", quadratic_table)

    # ------------------------------------------------------------------
    # TODO 4: Search tests.
    # Search for at least five existing EventIDs and two IDs that do not
    # exist. Test all three tables.
    # ------------------------------------------------------------------

    # Example of selecting a real EventID from the loaded dataset:
    # test_id = permits[0].event_id
    # print(chaining_table.search(test_id))

    # ------------------------------------------------------------------
    # TODO 5: Deletion test.
    # Choose an existing EventID. Search for it, delete it, and then
    # search for it again. The second search should return None.
    # Perform this experiment for all three tables.
    # ------------------------------------------------------------------

    # deletion_id = permits[0].event_id
    # deletion_test(chaining_table, deletion_id)
    # deletion_test(linear_table, deletion_id)
    # deletion_test(quadratic_table, deletion_id)


if __name__ == "__main__":
    main()
