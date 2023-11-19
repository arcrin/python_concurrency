from typing import Any

class Node:
    def __init__(self, value: Any):
        self.value = value
        self.adjacent_nodes = []


class DependencyGraph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node_value: Any):
        new_node = Node(node_value)
        self.nodes.append(new_node)
        return new_node
