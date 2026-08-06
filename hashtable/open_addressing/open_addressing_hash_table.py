import math
from enum import Enum
from typing import List, Optional


class ProbeType(Enum):
    Linear = 1      # offset(i) = i        -> home, home+1, home+2, ...
    Quadratic = 2   # offset(i) = i * i    -> home, home+1, home+4, home+9, ...


def next_prime(start):
    """
    Finds the next prime number greater than or equal to a given number
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


class Entry:
    """
    Represents a key-value pair stored directly in the backing array
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value


class OpenAddressingHashTable:
    """
    A hash table that resolves collisions with open addressing: every entry lives
    directly in the backing array, and collisions are handled by probing for the
    next candidate slot. Two probe sequences are supported (linear and quadratic).

    Deletion uses a tombstone marker so that probe chains passing through a
    removed slot are not broken. Keys are names (strings) and values are phone
    numbers (strings).
    """

    # A shared marker flagging a slot whose entry has been removed (a "tombstone").
    DELETED = Entry(None, None)

    # Open addressing degrades sharply as the table fills. Keeping the load factor
    # at most 0.5 also guarantees that quadratic probing on a prime-sized table
    # always finds a free slot.
    MAX_LOAD_FACTOR = 0.5

    def __init__(self, capacity, probe_type):
        if capacity < 1:
            raise ValueError("Initial capacity must be >= 1")
        # A prime capacity spreads the probe sequence across the whole table.
        capacity = capacity if is_prime(capacity) else next_prime(capacity)
        self.table: List[Optional[Entry]] = [None] * capacity
        self.size = 0  # Number of active key-value pairs
        self.probe_type = probe_type

    def _hash(self, key):
        """
        Computes the home slot for a key using the division method.

        Any hash function works here; open addressing fixes one so the probe
        sequence stays the focus (see HashFunctionType in the chaining table).
        """
        return abs(hash(key)) % len(self.table)

    def _probe(self, i):
        """
        Computes the offset added to the home slot on the i-th probe
        """
        if self.probe_type == ProbeType.Linear:
            return i          # home, home+1, home+2, ...
        elif self.probe_type == ProbeType.Quadratic:
            return i * i      # home, home+1, home+4, home+9, ...
        else:
            raise Exception("Unknown Probe Type")

    def put(self, key, value):
        """
        Inserts a new key-value pair, or updates the value if the key already exists.
        :param key: the key to insert or update
        :param value: the value associated with the key
        """
        # Resize before the table gets too full.
        if (self.size + 1) / len(self.table) > self.MAX_LOAD_FACTOR:
            self._rehash()

        home = self._hash(key)
        first_tombstone = -1

        for i in range(len(self.table)):
            index = (home + self._probe(i)) % len(self.table)
            entry = self.table[index]

            if entry is None:
                # An empty slot ends the probe chain: the key is not present.
                # Reuse the first tombstone seen along the way, if any.
                target = first_tombstone if first_tombstone != -1 else index
                self.table[target] = Entry(key, value)
                self.size += 1
                return
            elif entry is self.DELETED:
                # Remember the first tombstone so the key can be placed there.
                if first_tombstone == -1:
                    first_tombstone = index
            elif entry.key == key:
                # Key already present — update its value in place.
                entry.value = value
                return
            # Otherwise the slot holds a different key: keep probing.

        # Defensive guard — never reached while the invariants hold (prime size,
        # load factor <= 0.5); fails loudly instead of silently dropping the key.
        raise Exception("Hash table is full")

    def get(self, key):
        """
        Retrieves the value associated with a key.
        :param key: the key whose value is to be retrieved
        :return: the value, or None if the key is not found
        """
        home = self._hash(key)
        for i in range(len(self.table)):
            index = (home + self._probe(i)) % len(self.table)
            entry = self.table[index]

            if entry is None:
                return None  # An empty slot ends the probe chain.
            if entry is not self.DELETED and entry.key == key:
                return entry.value
            # A tombstone or a different key — keep probing.
        return None

    def remove(self, key):
        """
        Removes a key-value pair, leaving a tombstone in its place so that probe
        chains running through the slot are not broken.
        :param key: the key of the pair to remove
        :return: True if the key was found and removed, False otherwise
        """
        home = self._hash(key)
        for i in range(len(self.table)):
            index = (home + self._probe(i)) % len(self.table)
            entry = self.table[index]

            if entry is None:
                return False  # An empty slot ends the probe chain.
            if entry is not self.DELETED and entry.key == key:
                self.table[index] = self.DELETED  # Tombstone, not an empty slot.
                self.size -= 1
                return True
        return False

    def _rehash(self):
        """
        Doubles the capacity (rounded up to a prime) and reinserts every active
        entry. Tombstones are discarded in the process.
        """
        old_table = self.table
        new_capacity = next_prime(len(old_table) * 2)
        self.table: List[Optional[Entry]] = [None] * new_capacity
        self.size = 0
        for entry in old_table:
            if entry is not None and entry is not self.DELETED:
                self.put(entry.key, entry.value)

    def print_hash_table(self):
        """
        Prints the backing array slot by slot
        """
        for i, entry in enumerate(self.table):
            if entry is None:
                print(f'[{i}] -')
            elif entry is self.DELETED:
                print(f'[{i}] (deleted)')
            else:
                print(f'[{i}] {entry.key} = {entry.value}')
