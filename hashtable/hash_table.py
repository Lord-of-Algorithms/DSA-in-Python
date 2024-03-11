import math
from decimal import Decimal, getcontext
from enum import Enum
from typing import List, Optional

# Set the precision to accommodate large hash codes
getcontext().prec = 50


class HashTableEntry:
    """
    Represents a key-value pair in the hash table
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Reference to the next entry (node) in the linked list


class HashTableBucket:
    """
    Represents the linked list used in chaining
    """

    def __init__(self):
        self.head = None  # Head of the linked list

    def insert_at_beginning(self, key, value):
        """
        Inserts a new entry at the beginning of the list
        :param key: The key of the entry to be inserted.
        :param value: The value of the entry.
        """
        new_entry = HashTableEntry(key, value)
        new_entry.next = self.head
        self.head = new_entry

    def delete(self, key):
        """
        Deletes an entry with the specified key from the list
        :param key: The key of the entry to be deleted.
        :return: True if the entry was found and successfully deleted, False otherwise.
        """
        current = self.head
        prev = None

        while current is not None:
            if current.key == key:
                # Key found, delete the entry
                if prev is None:
                    self.head = current.next  # Deleting the first entry
                else:
                    prev.next = current.next  # Deleting a subsequent entry
                return True  # Entry successfully deleted
            prev = current
            current = current.next
        return False  # Key not found

    def find(self, key):
        """
        Finds an entry by key in the list
        """
        current = self.head
        while current is not None:
            if current.key == key:
                return current
            current = current.next
        return None  # Return None if key not found

    def print_bucket(self):
        """
        Prints all the entries in this hash table bucket.
        """
        current = self.head
        while current is not None:
            print(f'->|{current.key}, {current.value}|', end='')
            current = current.next
        print()  # For newline


class HashFunctonType(Enum):
    Division = 1
    Multiplication = 2


def next_prime(start):
    """
    Finds the next prime number greater than a given number
    """
    prime = start if start == 2 or start % 2 != 0 else start + 1

    while True:
        if is_prime(prime):
            return prime
        prime += 2


def is_prime(num):
    """
    Checks if a number is prime
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


class HashTable:
    """
    A hash table implementation using chaining with linked lists to resolve collisions.
    This class provides methods for inserting, retrieving, and removing key-value pairs,
    where keys are strings and values are numbers.
    """

    def __init__(self, capacity, hash_function_type):
        if capacity < 1:
            raise ValueError("Initial capacity must be >= 1")
        # Adjust capacity to the next prime number if it's not already prime
        capacity = capacity if is_prime(capacity) else next_prime(capacity)
        self.bucket_array: List[Optional[HashTableBucket]] = [None] * capacity
        self.size = 0  # Number of key-value pairs in the hash table
        self.hash_function_type = hash_function_type
        self.A = (math.sqrt(5) - 1) / 2  # Constant for Multiplication Method

    def hash(self, key):
        """
        Computes the hash value for a given key
        """
        hash_code = hash(key)

        if self.hash_function_type == HashFunctonType.Division:
            return abs(hash_code) % len(self.bucket_array)
        elif self.hash_function_type == HashFunctonType.Multiplication:
            # Use Decimal for high precision arithmetic
            product = Decimal(abs(hash_code)) * Decimal(self.A)
            fractional_part = product - int(product)
            return int(math.floor(len(self.bucket_array) * fractional_part))
        else:
            raise Exception("Unknown Hash Function Type")

    def put(self, key, value):
        """
        Inserts or updates a key-value pair in the hash table.
        :param key: the key to insert or update
        :param value: the value associated with the key
        """
        index = self.hash(key)  # Compute the index for this key using the hash function
        if self.bucket_array[index] is None:
            self.bucket_array[index] = HashTableBucket()  # Lazy initialization

        bucket = self.bucket_array[index]
        existing_entry = bucket.find(key)

        if existing_entry is not None:
            # Key found, update value
            existing_entry.value = value
        else:
            # Check if adding a new entry would exceed the load factor and trigger rehashing if necessary
            if (self.size + 1) / len(self.bucket_array) >= 0.75:
                self.rehash()
                index = self.hash(key)  # Recompute index as length of the array has changed
                if self.bucket_array[index] is None:
                    self.bucket_array[index] = HashTableBucket()
                bucket = self.bucket_array[index]

            bucket.insert_at_beginning(key, value)
            self.size += 1

    def get(self, key):
        """
        Retrieves the value associated with a given key.
        :param key: the key whose value is to be retrieved
        :return: the value associated with the key, or None if the key is not found
        """
        index = self.hash(key)
        bucket = self.bucket_array[index]
        if bucket is None:
            return None
        entry = bucket.find(key)
        return entry.value if entry is not None else None

    def remove(self, key):
        """
        Removes a key-value pair from the hash table.
        :param key: the key of the pair to be removed
        :return: True if the pair was successfully removed, False if the key was not found
        """
        index = self.hash(key)
        bucket = self.bucket_array[index]
        if bucket is None:
            return False
        was_deleted = bucket.delete(key)

        if was_deleted:
            self.size -= 1
        return was_deleted

    def rehash(self):
        """
        Doubles the size of the hash table and rehashes all existing entries
        """
        old_bucket_array = self.bucket_array
        # Find the next prime number greater than double the current length
        new_capacity = next_prime(len(self.bucket_array) * 2)
        self.bucket_array: List[Optional[HashTableBucket]] = [None] * new_capacity
        self.size = 0

        for bucket in old_bucket_array:
            if bucket is not None:
                current = bucket.head
                while current is not None:
                    # Re-add each entry to the new table
                    self.put(current.key, current.value)
                    current = current.next

    def print_hash_table(self):
        """
        Prints the entire contents of the hash table
        """
        for i, bucket in enumerate(self.bucket_array):
            print(f'[{i}]', end='')
            if bucket is not None:
                bucket.print_bucket()
            else:
                print()  # For newline
