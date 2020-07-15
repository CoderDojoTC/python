```python
def visit(u):
    u.set_color("gray")
    for vert in u.adj:
        if vert.get_color() == "white":
            vert.prev = u
            path = visit(vert)
            if path != None:
                return path
        elif vert.get_color() == "blue":
            vert.prev = u
            return vert
    u.set_color("black")

def find_path(start_node):
    start_node.set_color("gray")
    start_node.prev = None        
    goal = visit(start_node)
    visited = []
    cur = goal
    while cur != None:
        visited.insert(0, cur)
        cur = cur.prev
    return visited #Placeholder return to avoid errors
```

* This lab was heavily inspired by Nathan Taylor's University of Minnesota CSCI 4041 assignment.