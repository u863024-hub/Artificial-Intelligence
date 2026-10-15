# Lab 6 - Task 1, Section 4.1
# Implement the given graph in Python

# Represent the graph using an adjacency list
graph={
    1:[2,7,8],
    2:[1,3,6],
    3:[2,4,5],
    4:[3],
    5:[3],
    6:[3],
    7:[1],
    8:[1,9,12],
    9:[8,10,11],
    10:[8],
    11:[8],
    12:[9] 
}
# display graph
print("Graph representation:")
for node in graph:
    print(node,graph[node])

# Lab 6 - Practice Task 1
# Depth-First Search using Stack

# Represent the tree using an adjacency list
tree={
    'A':['B','F','D','E'],
    'B':['K','J'],
    'F':[],
    'D':['G'],
    'E':['C','H','I'],
    'K':['N','M'],
    'J':[],
    'N':[],
    'M':[],
    'G':[],
    'C':[],
    'H':[],
    'I':['L'],
    'L':[]
}
def DFS(tree,start,goal):
    #create stack containing starting node
    stack = [start]
    #keep track of visited nodes
    visited = set()
    #continue while stack is not empty
    while stack:
        #remove top node from stack
        node = stack.pop()

        #skip node already visited
        if node in visited:
            continue
        #mark node as visited
        visited.add(node)

        #display visiting node
        print("Visiting:",node)

        #stop when goal is found
        if node==goal:
            print("Goal found:",goal)
            return

        # reverse the neighbours so leftmost is visited first
        for neighbor in reversed(tree[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    else:
        print("Goal not found")

DFS(tree,'A','G')