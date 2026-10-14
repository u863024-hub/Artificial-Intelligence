# Task1-Breadth-First Search (BFS) and Priority Queue
from collections import deque
# Represent the graph using an adjacency list.
# Each node stores the nodes directly connected to it.
graph ={
    0:[1,2,3],
    1:[0,4,5],
    2:[0,6,7],
    3:[0,7],
    4:[1],
    5:[1],
    6:[2],
    7:[2,3],
}

def bfs(graph,start):
    #create empty queue
    queue = deque([start])

    #mark starting node as visited
    visited = {start}

    #continue while queue is not empty
    while queue:
        # Remove the first node from the queue.
        node = queue.popleft()

        #print current node
        print(node,end=" ")

        #check all neighbours of current node
        for neighbor in graph[node]:
            #add nodes that have not been visited
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

#start bfs from node 0
print("BFS Traversal: ")
bfs(graph,0)


#Task2-BFS from A to goal G
# Represent the tree using an adjacency list.
tree={
    'A':['B','F','D','E'],
    'B':['K','J'],
    'F':[],
    'D':['G'],
    'E':['C','H','I'],
    'K':['N','M'],
    'J':[],
    'G':[],
    'C':[],
    'H':[],
    'I':['L'],
    'M':[],
    'N':[],
    'L':[],
}

def BFS(tree,start,goal):
    #create empty queue
    queue = deque([start])
    
    #mark starting node as visited
    visited = {start}
    #store each nodes parent to reconstruct path
    parent={start:None}
    #continue while queue is not empty
    while queue:
        # Remove the first node from the queue.
        node = queue.popleft()
    
        #print current node
        print("Visiting: ",node)

        #stop when goal is found
        if node==goal:
            print("Goal Found: ",goal)
            break
        # explore current nodes neighbor
        for neighbor in tree[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor]=node
                queue.append(neighbor)
    else:
        #if queue becomes empty without finding goal
        print("Goal not found")
        return
    # reconstruct path from goal to start
    path=[]
    current=goal

    while current is not None:
        path.append(current)
        current = parent[current]

    #reverse path to get start-goal
    path.reverse()

    print("Path to goal: ","->" .join(path))

#search from A until G is found
BFS(tree,'A','G')

#Task 3 — Implement a Priority Queue
import heapq
#create empty priority queue
priority_queue = []
#add item with their priority
#format:(priority,queue)
heapq.heappush(priority_queue,(1,'Task A'))
heapq.heappush(priority_queue,(2,'Task B'))
heapq.heappush(priority_queue,(3,'Task C'))
#display items
print("Priority Queue: ")
while priority_queue:
    #remove with smallest priority
    priority,item = heapq.heappop(priority_queue)

    #display remove item and priority
    print(item,"-Priority:",priority)


# Question 4.1: Implement the given graph in Python

graph = {
    0: [1, 4],
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}

# Display the graph
for node in graph:
    print(node, ":", graph[node])
