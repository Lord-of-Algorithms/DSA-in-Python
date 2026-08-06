from hashtable.chaining.chaining_hash_table import ChainingHashTable
from hashtable.chaining.chaining_hash_table import HashFunctionType
from hashtable.open_addressing.open_addressing_hash_table import OpenAddressingHashTable
from hashtable.open_addressing.open_addressing_hash_table import ProbeType


# Demonstrates both hash table implementations on the same kind of data — a small
# phone book that maps names (keys) to phone numbers (values):
#
#   1. Chaining        — collisions share a slot via a linked list.
#   2. Open addressing — collisions are resolved by probing for another slot,
#                        with tombstones marking removed entries.


def demo_chaining():
    print("=== Chaining ===")
    phone_book = ChainingHashTable(5, HashFunctionType.Division)

    # Insert name -> phone number pairs.
    phone_book.put("Alice", "555-0101")
    phone_book.put("Bob", "555-0102")
    phone_book.put("Carol", "555-0103")

    print("Initial phone book:")
    phone_book.print_hash_table()

    # Retrieve a value.
    print(f"\nBob's number: {phone_book.get('Bob')}")

    # Update an existing key.
    phone_book.put("Bob", "555-9999")
    print("\nAfter updating Bob's number:")
    phone_book.print_hash_table()

    # Remove an entry.
    phone_book.remove("Carol")
    print("\nAfter removing Carol:")
    phone_book.print_hash_table()

    # Insert more entries to trigger rehashing.
    phone_book.put("Dave", "555-0104")
    phone_book.put("Eve", "555-0105")
    phone_book.put("Frank", "555-0106")
    print("\nAfter adding more names and triggering rehashing:")
    phone_book.print_hash_table()


def demo_open_addressing():
    print("=== Open addressing ===")
    phone_book = OpenAddressingHashTable(7, ProbeType.Linear)

    # Insert name -> phone number pairs.
    phone_book.put("Bob", "555-0102")
    phone_book.put("Rob", "555-0103")
    phone_book.put("Tam", "555-0104")

    print("After inserts (linear probing):")
    phone_book.print_hash_table()

    # Retrieve a value.
    print(f"\nRob's number: {phone_book.get('Rob')}")

    # Remove a key — leaves a tombstone so probe chains stay intact.
    phone_book.remove("Rob")
    print("\nAfter removing Rob:")
    phone_book.print_hash_table()

    # Searching for the removed key now fails; keys past the tombstone are still found.
    print(f"\nRob's number after removal: {phone_book.get('Rob')}")
    print(f"Tam's number after removal: {phone_book.get('Tam')}")

    # A new insert can reuse the tombstoned slot.
    phone_book.put("Max", "555-0105")
    print("\nAfter inserting Max (may reuse the tombstone):")
    phone_book.print_hash_table()

    # The same operations with quadratic probing.
    quad_book = OpenAddressingHashTable(7, ProbeType.Quadratic)
    quad_book.put("Bob", "555-0102")
    quad_book.put("Rob", "555-0103")
    quad_book.put("Vic", "555-0104")
    print("\nAfter inserts (quadratic probing):")
    quad_book.print_hash_table()


if __name__ == "__main__":
    demo_chaining()
    print()
    demo_open_addressing()
