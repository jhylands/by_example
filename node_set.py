class NodeSet:
    def __init__(self, iterable):
        self.leaves = {}
        for node in iterable:
            self.add(node)
    def add(self, node):
        if node.value in self.leaves:
            self.leaves[node.value].add_parents(node.parents)
        else:
            self.leaves[node.value] = node
    def __repr__(self):
        return str(self.leaves.keys())
    def __iter__(self):
        return iter(self.leaves.values())
