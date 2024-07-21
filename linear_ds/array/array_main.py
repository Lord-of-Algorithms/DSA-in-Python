"""
In Python, lists are used as dynamic arrays. There is no fixed-size static array
like in some other languages. This script demonstrates various operations on lists
including initialization, insertion, deletion, and more.
"""


def demo_list_operations():
    # 1. Initialization
    planets = ["Venus", "Pluto", "Earth"]
    print("Initial list of planets:", planets)

    # 2. Insertion at beginning
    planets.insert(0, "Mercury")
    print("After inserting Mercury at the beginning:", planets)

    # 3. Insertion at end
    planets.append("Jupiter")
    print("After appending Jupiter at the end:", planets)

    # 4. Deletion by value
    planets.remove("Pluto")  # Note: This will raise ValueError if 'Pluto' is not in the list
    print("After removing Pluto:", planets)

    # 5. Accessing elements
    print("Second planet:", planets[1])

    # 6. Reversing the list
    planets.reverse()
    print("Planets in reverse order:", planets)

    # 7. Sorting the list
    planets.sort()
    print("Planets sorted alphabetically:", planets)

    # 8. Popping elements
    last_planet = planets.pop()  # Removes and returns the last item in the list
    print("After popping the last planet:", last_planet)
    print("Current list of planets:", planets)


if __name__ == "__main__":
    demo_list_operations()
