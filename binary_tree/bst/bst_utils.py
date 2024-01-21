def min_value(root):
    """
    Get the in-order successor's key (smallest in the right subtree).

    :param root: The root node of the tree or subtree.
    :return: The minimum value key in the tree.
    """
    value = root.get_key()
    while root.get_left() is not None:
        value = root.get_left().get_key()
        root = root.get_left()
    return value


def search_recursive(current, key):
    """
    Helper method to recursively search for a node.

    :param current: The root of the subtree where the node with the specified key will be searched.
    :param key: The key to search for.
    :return: The node with the specified key, or None if not found.
    """
    if current is None:
        return None  # Base case: key not found or tree is empty
    if key == current.get_key():
        return current  # Node found
    return search_recursive(current.get_left(), key) if key < current.get_key() else search_recursive(
        current.get_right(), key)


def handle_duplicate_key(key):
    """
    Handles the scenario where a duplicate key is encountered during insertion.

    :param key: The duplicate key encountered.
    """
    print(f"Attempted to insert duplicate key: {key}")
