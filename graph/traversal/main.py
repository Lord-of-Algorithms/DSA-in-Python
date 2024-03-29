# Initialize vertices
from factory import GraphTraversalFactory, GraphTraversalMethod, GraphFactory, GraphRepresentation
from graph.traversal.graph.vertex import Vertex

a, b, c, d = Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D")

# Create graph and add edges
graph = GraphFactory.create_graph(GraphRepresentation.MATRIX, [a, b, c, d])
graph.set_edge(a, b)
graph.set_edge(a, d)
graph.set_edge(b, c)
graph.set_edge(b, d)
graph.set_edge(c, d)

# Perform DFS traversal
traversal = GraphTraversalFactory.create_traversal(GraphTraversalMethod.DFS)
traversal.traverse(graph, a)
print("DFS Traversal Path:", [str(vertex) for vertex in traversal.get_traversal_path()])
traversal.reset_state()

# Perform BFS traversal
traversal = GraphTraversalFactory.create_traversal(GraphTraversalMethod.BFS)
traversal.traverse(graph, a)
print("BFS Traversal Path:", [str(vertex) for vertex in traversal.get_traversal_path()])
