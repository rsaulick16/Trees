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
    'A':['B', 'C'],
    'B':['A', 'D', 'E'],
    'C':['A', 'F', 'G'],
    'D':['B', 'H', 'I'],
    'E':['B', 'J', 'K'],
    'F':['C', 'L', 'M'],
    'G':['C', 'N', 'O'],
    'H':['D'],
    'I':['D'],
    'J':['E'],
    'K':['E'],
    'L':['F'],
    'M':['F'],
    'N':['G'],
    'O':['G'],
    }
# BFS algorithm psuedocode
# 1. Assign ‘A’ as the root node and add it to the queue.
# 2. pop() node ‘A’ from the queue and add the child nodes of ‘A’ to the queue
# 3. set 'A' as current node
# 4. if the queue is not empty step 5
# 5. pop() the next node off the queue, in this case it's 'B'.
# 6. Repeat these steps 4 to 6 until the queue gets empty. 
# note: nodes that have already visited should not be added to the queue again.

# traversal the 'tree' from starting vertex/node using the bfs algorithm
# and returns the 'path' of the visited nodes
def bfs(adjList, rootNode):
    path = []
    nodeQueue = [rootNode] # 1
    currentNode = nodeQueue.pop() # 2
    neighbours = adjList[currentNode]
    while len(nodeQueue) == 0:
        for neighbour in neighbours:
            if neighbour not in nodeQueue:
                nodeQueue.append(neighbour)
                currentNode = nodeQueue.pop()
                path.append(currentNode)
                


        #if len(nodeQueue) != 0
        #path.append(currentNode)
        #neighbours = adjList[currentNode]
        #for neighbours in neighbours:
           # nodeQueue.append(neighbours)
        
        




# drive code
def main():
    path = bfs(TREE_ADJACENCY_LIST, 'A')
    print(path)

if __name__ == "__main__":
    main()
