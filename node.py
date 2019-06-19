class Node:
    def __init__(self, value=None, parent=None):
        self.value = value
        self.stack = []#defaultdict(list)
        self.parents = [parent]
        
    def funked(self, function_name):
        stack.append(function_name)
        
    def __call__(self,f):
        self.stack.append(f)
        return Node(f(self.value),parent=self)
     
    def ancestors(self):
        ancestor = self
        while ancestor is not None:
            ancestor = ancestor.parents[0]
            yield ancestor
    def add_parent(self, parent):
        self.parents.append(parent)
    def add_parents(self,parents):
        self.parents += parents
    def __str__(self):
        return self.value
    def __repr__(self):
        return str(self.value)
        
        
def layer(v,start=[Node(0)]):
    if v == 0:
        return start
    es = layer(v-1, start)
    print v, es
    return NodeSet([e(f) for e in es for f in fs if f(e.value)<10e9])
