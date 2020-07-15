# This lab was heavily inspired by Nathan Taylor's University of Minnesota CSCI 4041 assignment.

#Takes as input a Square object node in a graph of Square nodes.
# This will always be the Square node representing (0,0), the start position
#Performs DFS until the goal Square is found (the Square with color = "blue").
#Returns a list containing each Square node in the path from the start
# (0,0) to the goal node, inclusive, in order from start to goal.


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


#  DO NOT EDIT BELOW THIS LINE
# Credits: Thank you to Nathan Taylor for the 

import traceback, turtle, time

#Change this value to adjust the time between turtle actions in seconds
draw_delay = 0.05

#Set this to False to turn off turtle entirely.
enable_turtle = True


#Square class
#A single square on the grid, which is a single node in the graph.
#Has several instance variables:
# self.t: The turtle object used to draw this square
# self.x: The integer x coordinate of this square
# self.y: The integer y coordinate of this square
# self.adj: A list representing all non-blocked squares adjacent
#   to this one. (This is the node's adjacency list)
# self.__color: A private string representing the color of the square
#   Must be accessed using set_color and get_color because it's private
#   The color of the square is purple if it's a blocked square.
#   The color of the square is blue if it's the goal square.
#   Otherwise, it starts as white, and then progresses to grey and then
#   black according to the DFS algorithm.
# self.depth: An integer representing the depth of the node within DFS.
#   You don't really have to use this, but it may be helpful.
# self.prev: A Square object pointing to the node from which this node
#   was discovered from within DFS: the pi variable in the textbook
class Square:
    def __init__(self,x,y,val,t):
        self.t = t
        self.x = x
        self.y = y
        self.adj = []
        if val == 1:
            self.__color = "white"
        elif val == 2:
            self.__color = "blue"
        else:
            self.__color = "purple"
        self.depth = float("inf")
        self.prev = None
        
    #Getters and setters for color variable.  You MUST use these rather
    #  than trying to change color directly: it causes the squares to
    #  actually update color within the graphics window.
    def set_color(self,color):
        if color != self.__color:
            self.__color = color
            if enable_turtle:
                self.draw()
                turtle.update()
                time.sleep(draw_delay)
    def get_color(self):
        return self.__color
    
    #Draws the square
    def draw(self):
        t = self.t
        t.hideturtle()
        t.speed(0)
        t.pencolor("blue")
        if self.__color == "purple":
            t.pencolor("purple")
        t.fillcolor(self.__color)
        t.penup()
        t.setpos(self.x-.5,self.y-.5)
        t.pendown()
        t.begin_fill()
        for i in range(4):
            t.forward(1)
            t.left(90)
        t.end_fill()
        
    #String representation of a Square object: (x,y)
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    
    #Check equality between two Square objects.
    def __eq__(self,other):
        return type(self) == type(other) and \
               self.x == other.x and self.y == other.y

#Takes as input a 2D list of numbers and a turtle object
#Outputs a 2D list of Square objects, which have their adjacency
#  lists initialized to all adjacent Square objects that aren't
#  blocked (so their val isn't 0).
def grid_to_squares(grid,t):
    square_grid = []
    for j in range(len(grid)):
        square_row = []
        for i in range(len(grid[j])):
            square_row.append(Square(i,j,grid[j][i],t))
        square_grid.append(square_row)
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            adj = []
            if j+1 < len(grid) and grid[j+1][i]:
                adj.append(square_grid[j+1][i])
            if i+1 < len(grid[j]) and grid[j][i+1]:
                adj.append(square_grid[j][i+1])
            if j-1 >= 0 and grid[j-1][i]:
                adj.append(square_grid[j-1][i])
            if i-1 >= 0 and grid[j][i-1]:
                adj.append(square_grid[j][i-1])
            square_grid[j][i].adj = adj
    return square_grid

#Draws the entire grid of Square objects.
def draw_grid(square_grid):
    for j in range(len(square_grid)):
        for i in range(len(square_grid[j])):
            square_grid[j][i].draw()

#Test cases
if enable_turtle:
    square_turtle = turtle.Turtle()
    square_turtle.hideturtle()
    square_turtle.speed(0)
    square_turtle.pencolor("blue")
else:
    square_turtle = None
grid0 = [[1,2],
         [0,0]]
grid4 = [[1,0,0,0,0,0,0,0,0,0],
         [1,1,0,0,0,1,1,1,1,0],
         [0,1,0,1,1,1,0,0,1,0],
         [0,1,1,1,0,1,0,0,1,0],
         [0,1,0,1,0,1,1,0,0,0],
         [0,0,1,1,1,1,0,1,1,0],
         [0,0,1,0,0,1,1,1,0,0],
         [0,0,1,1,1,0,0,1,0,0],
         [0,0,1,0,1,0,2,1,1,0],
         [0,0,0,0,0,0,0,0,0,0]]
grid5 = [
[1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
[1, 0, 1, 1, 0, 1, 2, 1, 1, 0, 0, 1],
[1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0],
[1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
[1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
[0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
[0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1],
[0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
[0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]]
map0 = grid_to_squares(grid0,square_turtle)
map4 = grid_to_squares(grid4,square_turtle)
map5 = grid_to_squares(grid5,square_turtle)


path0 = [map0[0][0],
         map0[0][1]]
path4 = [map4[0][0],
         map4[1][0],
         map4[1][1],
         map4[2][1],
         map4[3][1],
         map4[3][2],
         map4[3][3],
         map4[4][3],
         map4[5][3],
         map4[5][4],
         map4[5][5],
         map4[6][5],
         map4[6][6],
         map4[6][7],
         map4[7][7],
         map4[8][7],
         map4[8][6]]
path5 = [map5[0][0],
         map5[1][0],
         map5[2][0],
         map5[2][1],
         map5[2][2],
         map5[2][3],
         map5[3][3],
         map5[3][4],
         map5[3][5],
         map5[4][5],
         map5[5][5],
         map5[6][5],
         map5[7][5],
         map5[8][5],
         map5[8][6],
         map5[8][7],
         map5[7][7],
         map5[6][7],
         map5[6][8],
         map5[5][8],
         map5[4][8],
         map5[4][9],
         map5[4][10],
         map5[4][11],
         map5[3][11],
         map5[3][10],
         map5[3][9],
         map5[3][8],
         map5[2][8],
         map5[1][8],
         map5[1][7],
         map5[1][6]]
path5alt = [map5[0][0],
         map5[1][0],
         map5[2][0],
         map5[2][1],
         map5[2][2],
         map5[2][3],
         map5[3][3],
         map5[3][4],
         map5[3][5],
         map5[4][5],
         map5[5][5],
         map5[6][5],
         map5[7][5],
         map5[8][5],
         map5[8][6],
         map5[8][7],
         map5[7][7],
         map5[6][7],
         map5[6][8],
         map5[5][8],
         map5[4][8],
         map5[3][8],
         map5[2][8],
         map5[1][8],
         map5[1][7],
         map5[1][6]]
tests = [map0, map4, map5]
grids = [grid0, grid4, grid5]
correct = [path0, path4, path5]
#Test cases 3 and 6 give a different path if you check neighbors
#for the goal squaure before recursing
correctalt = [path0, path4, path5alt]


#Run test cases, check whether output path correct
count = 0

import random
try:
    for i in range(len(tests)):
        print("\n---------------------------------------\n")
        print("TEST #",i+1)
        square_grid = tests[i]
        if enable_turtle:
            turtle.resetscreen()
            turtle.setworldcoordinates(-1,-1,len(tests[i][0]),len(tests[i]))
            turtle.delay(0)
            turtle.tracer(0,0)
            draw_grid(square_grid)
        else:
            print("\nTesting find_path on the following grid:")
            for row in grids[i][::-1]:
                print(row)
            print("Lower left corner is (0,0)")
            print("0 is a swamp tile")
            print("1 is a normal tile")
            print("2 is the goal tile\n")
        pathlst = find_path(square_grid[0][0])
        print("Expected:",correct[i],"\nGot     :",pathlst)
        assert type(pathlst) == list, "Return value is not of type list"
        if enable_turtle:
            square_turtle.penup()
            square_turtle.goto(0,0)
            square_turtle.pendown()
            square_turtle.color("green")
            square_turtle.shape("turtle")
            square_turtle.left(90)
            square_turtle.showturtle()
            for square in pathlst:
                square_turtle.goto(square.x,square.y)
                turtle.update()
                time.sleep(draw_delay)
        assert pathlst == correct[i] or pathlst == correctalt[i], "Path incorrect"
        print("Test Passed!\n")
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)
except Exception:
    print("\nFAIL: ",traceback.format_exc())


print(count,"out of",len(tests),"tests passed.")


