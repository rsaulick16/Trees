def dfs_v1(graph, vertex):
    if vertex is None or vertex not in graph:
        return "vertex " + vertex + " invalid or not in the graph"
    path = []
    stack = [vertex]
    while(len(stack) != 0):
        s = stack.pop()
        if s not in path:
            path.append(s)
        for neighbour in (graph[s][::-1]):
            if neighbour not in stack and neighbour not in path:
                stack.append(neighbour)
    return path
'''
              A
             / \
            B   C
           / \
          D   E
Depth First Search Pre-order: A B D E C
'''
# tree
#          A
#        /   \
#       /     \
#      B       C
#     / \     / \
#    D   E   F   G
#   /\  /\  /\  /\
#   H I J K L M N O
TREE_ADJACENCY_LIST = {
 'A':['B','C'],
 'B':['A','D','E'],
 'C':['A','F','G'],
 'D':['B','H','I'],
 'E':['B','J','K'],
 'F':['C','L','M'],
 'G':['C','N','O'],
 'H':['D'],
 'I':['D'],
 'J':['E'],
 'K':['E'],
 'L':['F'],
 'M':['F'],
 'N':['G'],
 'O':['G'] }
    

path = dfs_v1(TREE_ADJACENCY_LIST, 'A')
print(path)
