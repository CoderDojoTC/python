# Maze Solving with Breadth-First Search

In this lab, we are going to solve a maze with an **algorithm** called **breadth-first search**. Before we do though, we need to get some terminology out of the way. There are two main ways that we will be storing data, known as **data structures**. These are:

* A **graph** is a data structure representing data that is interconnected. We will be representing our maze this way. Graphs are made of of **nodes** and **edges**. Think of edges as roads that connect different nodes together. In this maze, we will hopping from node to node via these edges.

* A **queue** is another commonly used data structure. Think of it as a line that we always take from the front of and always add to the back (no budging).

First, download the code template found in the ```src/intermediate``` folder of the repository, found [here](https://github.com/CoderDojoTC/python). Then, lets try and implement a solution to solve it!

One solution is breadth-first search, or BFS. BFS works by cycling through all possible nodes one hop away from your current position, adding them to a **queue** and then cycling through all of those nodes in the queue to see if they are the solution. Lets see how it is implemented below:

```python
#Takes as input a Square object node in a graph of Square nodes.
# This will always be the Square node representing (0,0), the start position
#Performs BFS until the goal Square is found (the Square with color = "blue").
#Returns a list containing each Square node in the path from the start
# (0,0) to the goal node, inclusive, in order from start to goal.
def find_path(start_node):
    start_node.set_color("gray")
    start_node.prev = None
    
    q = [] # Our queue of nodes visited
    q.append(start_node) # Add starting node to the end of the queue
    while len(q) != 0: # Runs when there are still nodes in the queue
        start_node = q.pop(0) # Remove the node in the front of the queue
        for node in start_node.adj:   # Look at every item in the current node's adjacency list
            if node.get_color() == "white":  # If the color is white, we haven't visited this node before
                node.set_color("grey")
                node.depth = start_node.depth + 1
                node.prev = start_node
                q.append(node)  # Add this new node to the queue
            elif node.get_color() == "blue":  # If the color is blue, we have reached our goal
                node.prev = start_node
                visited = [node]
                cur = node.prev
                while cur != None: # Backtrack our path, adding nodes to the visited list as we go
                    visited.insert(0, cur)
                    cur = cur.prev
                return visited
        start_node.set_color("black")
```

There are other ways to find paths in mazes, one of which we will explore in the next lab!

* This lab was heavily inspired by Nathan Taylor's University of Minnesota CSCI 4041 assignment.