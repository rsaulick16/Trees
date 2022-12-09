from re import I
import numpy as np
# tree
#          A
#        /   \
#       /     \
#      B       C
#     / \     / \
#    D   E   F   G
#   /\  /\  /\  /\
#   H I J K L M N O
"""
aMatrix = ("0,0,0,1 \n0,0,0,1 \n0,0,0,1 \n1,1,1,0 ")
print(aMatrix)
for rows in array:
 for columns in rows:
   print(columns,end=" ")
   print()
"""
aMatrix = np.zeros((15,15), dtype=int)

tree ={
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
stack = []
visited = []

def binaryTree(graph, startNode):
    counter = 0
    stack.append(startNode)
    currentNode = stack.pop()
    for i in graph:
        x = graph[i]
        stack.append(x)
        for i in range(0,len(stack[counter])):
         print(stack[counter][i])
        counter = counter + 1


    #print(stack[1])
    



#print(tree)
 
binaryTree(tree, 'A')
#print(tree['A'])
#stack.append(list(tree)[2])
#print(stack)


#for x in list(tree)[0:len(tree)]:
#    print(tree[x])
