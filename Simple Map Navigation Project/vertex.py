#Author: Yasmeen Hussein
#Date: 3/4/2023
#Purpose: Vertex class

from cs1lib import *

class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adjacent_list = []

    def draw_vertex(self, r, g, b): #draws the vertex with a radius of 4
        global RADIUS
        RADIUS = 7
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, RADIUS)

    def draw_edge(self, v, r, g, b): #draws an edge between this vertex and another vertex
        global EDGEWIDTH
        EDGEWIDTH = 3
        enable_stroke()
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, v.x, v.y)

    def draw_edges_adjacent(self, r, g, b): #draws all the edges between vertex and others in  the
        for vertex in self.adjacent_list:
            self.draw_edge(vertex, r, g, b)

    def mouse_func(self, x, y):
         if self.x - 10 <= x <= self.x + 10 and self.y - 10 <= y <= self.y + 10:   #if the mouse is a certain range from the circle on the map, then its hovered over the circle and returns True
             return True
         else:
            return False

    def __str__(self):
        adj_string = ""
        for ele in self.adjacent_list:
            adj_string = adj_string + ele.name + ", "
        adj_string = adj_string[:-2]   #removes the , and space after the last adjacent vertices is added
        return self.name + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent vertices: " + adj_string