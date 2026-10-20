# Lab 7 - Part (a): Depth-Limited Search
 
tree = {
    "A": ["B", "F", "D", "E"],
    "B": ["K", "J"],
    "F": [],
    "D": ["G"],
    "E": ["C", "H", "I"],
    "K": ["N", "M"],
    "J": [],
    "G": [],
    "C": [],
    "H": [],
    "I": ["L"],
    "N": [],
    "M": [],
    "L": []
}
 
def depth_limited_search(tree, start, goal, limit):
    visited_order = []
    path = []
 
    def dls(node, depth):
        visited_order.append(node)
        path.append(node)
 
        if node == goal:
            return True
 
        # Do not expand nodes at the depth limit.
        if depth == limit:
            path.pop()
            return False
 
        for neighbor in tree[node]:
            if dls(neighbor, depth + 1):
                return True
 
        path.pop()
        return False
 
    found = dls(start, 0)
 
    print("Depth limit:", limit)
    print("Visit order:", " -> ".join(visited_order))
    if found:
        print("Goal found:", goal)
        print("Path:", " -> ".join(path))
    else:
        print("Goal not found within the depth limit.")
 
    return found
 
depth_limited_search(tree, "A", "G", 2)

# Lab 7 - Part (b): Iterative Deepening Search
 
def depth_limited_search(tree, start, goal, limit):
    visited_order = []
    path = []
 
    def dls(node, depth):
        visited_order.append(node)
        path.append(node)
 
        if node == goal:
            return True
 
        if depth == limit:
            path.pop()
            return False
 
        for neighbor in tree[node]:
            if dls(neighbor, depth + 1):
                return True
 
        path.pop()
        return False
 
    found = dls(start, 0)
    return found, visited_order, path.copy() if found else []
 
def iterative_deepening_search(tree, start, goal, max_depth):
    for limit in range(max_depth + 1):
        found, order, path = depth_limited_search(
            tree, start, goal, limit
        )
 
        print(f"Depth limit {limit}: {' -> '.join(order)}")
 
        if found:
            print("Goal found:", goal)
            print("Path:", " -> ".join(path))
            return path
 
    print("Goal not found up to maximum depth.")
    return None
 
iterative_deepening_search(tree, "A", "G", 3)
