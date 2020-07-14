```python
#Takes as input a Square object node in a graph of Square nodes.
# This will always be the Square node representing (0,0), the start position
#Performs BFS until the goal Square is found (the Square with color = "blue").
#Returns a list containing each Square node in the path from the start
# (0,0) to the goal node, inclusive, in order from start to goal.
def find_path(start_node):
    start_node.set_color("gray")
    start_node.prev = None
    
    q = []
    q.append(start_node)
    while len(q) != 0:
        start_node = q.pop(0)
        for node in start_node.adj:
            if node.get_color() == "white":
                node.set_color("grey")
                node.depth = start_node.depth + 1
                node.prev = start_node
                q.append(node)
            elif node.get_color() == "blue":
                node.prev = start_node
                visited = [node]
                cur = node.prev
                while cur != None:
                    visited.insert(0, cur)
                    cur = cur.prev
                return visited
        start_node.set_color("black")



```