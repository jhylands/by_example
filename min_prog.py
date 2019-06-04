# In this example the functions all take 2 primitives and return a primitive
list_of_functions = []
list_of_tokens = []

class Node:
    TOKEN
    right
    left
    function

leaf_nodes = cartesian(list_of_tokens,list_of_tokens)
layer1 = cartesian(leaf_nodes, list_of_functions)
layer1_results = [f(n1,n2) for (n1,n2),f in layer1]
#layer(n) = cartesian(set(layer(n-1)_results), list_of_functions)
