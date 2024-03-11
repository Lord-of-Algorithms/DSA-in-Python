from hashtable.hash_table import HashFunctonType
from hashtable.hash_table import HashTable

# Initialize the hash table with a small capacity of 5 for demonstration purposes.
# This small initial capacity is chosen to illustrate how rehashing operates when the hash table becomes full.
# In a practical application, especially for a dataset like the chemical elements with a
# well-defined and relatively small set of items (118 confirmed elements),
# an initial capacity between 150 and 200 could be more appropriate.
# This provides ample space for all elements and minimizes the need for rehashing, enhancing performance.
hash_table = HashTable(5, HashFunctonType.Division)

# Insert key-value pairs into the hash table
hash_table.put("Hydrogen", 1.008)
hash_table.put("Helium", 4.0026)
hash_table.put("Lithium", 6.94)

# Print the hash table's contents
print("Initial Hash Table:")
hash_table.print_hash_table()

# Retrieve and print a specific value
helium_weight = hash_table.get("Helium")
print(f"\nAtomic weight of Helium: {helium_weight}")

# Update an existing key with a new value and print the hash table
hash_table.put("Helium", 4.002602)
print("\nAfter updating Helium's atomic weight:")
hash_table.print_hash_table()

# Remove an entry and print the hash table
hash_table.remove("Lithium")
print("\nAfter removing Lithium:")
hash_table.print_hash_table()

# Insert more entries to trigger rehashing
hash_table.put("Beryllium", 9.0122)
hash_table.put("Boron", 10.81)
hash_table.put("Carbon", 12.011)
hash_table.put("Nitrogen", 14.007)
hash_table.put("Oxygen", 15.999)

print("\nAfter adding more elements and triggering rehashing:")
hash_table.print_hash_table()
