# DSA in Python
This repository supplements our mobile app "VisiGrab: Algorithms & DSA", which offers interactive visualizations of algorithms and data structures. It provides code for the concepts demonstrated in the app and is an essential resource for users seeking to understand and explore these implementations in detail. Learn more about the app: [App Store](https://apps.apple.com/us/app/visigrab-learn-algorithms/id1484525469), [Google Play](https://play.google.com/store/apps/details?id=com.iov.lordofalgorithms).

## Topics Covered

- **Binary Trees** — BST (Standard, AVL, Red-Black), In-order / Pre-order / Post-order / Breadth-first traversals
- **Graphs** — BFS/DFS traversal, Dijkstra, Bellman-Ford, Minimum Spanning Tree (Kruskal, Prim), Topological Sort. The app also features an interactive Graph Constructor — tap to add vertices, drag between them to add edges, and watch the algorithms run on your custom graph in real time.
- **Linear Data Structures** — Array, Linked List, Stack, Queue
- **Min-Heap**
- **Sorting** — Bubble, Insertion, Selection, Merge, Quick (Lomuto & Hoare), Heap Sort
- **Hash Table** — Chaining, Open Addressing (linear & quadratic probing)
- **Trie**
- **Union-Find**

## Contributing
While this project is open-source, it is not currently seeking contributions. You are welcome to fork and use the code according to the license, but please note that contributions or pull requests to this repository will not be accepted.

## Prerequisites
Before you begin, ensure you have installed the latest version of [Python](https://www.python.org/downloads/). This project is compatible with Python 3.x.

## Installation and Setup
To clone and run these examples locally, follow these steps:
```
git clone https://github.com/Lord-of-Algorithms/DSA-in-Python.git
cd DSA-in-Python
```

## Running the Examples

All commands must be run from the project root (`DSA-in-Python/`). The `-m` flag tells Python to resolve imports relative to the current directory — running from any other location will result in a "module not found" error.

```
cd DSA-in-Python
```

Then run any example:

```
python3 -m binary_tree.bst_main
python3 -m graph.dijkstra.dijkstra_main
python3 -m graph.topologicalsort.topological_sort_main
python3 -m linear_ds.queue.queue_main
python3 -m sorting.quick.quick_sort_main
python3 -m hashtable.hash_table_main
python3 -m trie.trie_main
python3 -m heap.min_heap_main
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Rate the App

If VisiGrab has helped your learning, a quick rating on the [App Store](https://apps.apple.com/us/app/visigrab-learn-algorithms/id1484525469) or [Google Play](https://play.google.com/store/apps/details?id=com.iov.lordofalgorithms) helps other learners discover it. Thanks!
