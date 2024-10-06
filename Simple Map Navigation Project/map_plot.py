#Author: Yasmeen Hussein
#Date: 3/7/2023
#Purpose: Draw the map

from cs1lib import *
from vertex import *
from load_graph import *
from breadth_first_search import *

W_WIDTH = 1012
W_HEIGHT = 811

clicked = False

mouse_x = 0
mouse_y = 0
press_x = 0
press_y = 0

start_vertex = None
goal_vertex = None

def press(mx, my):  #needed inorder to press the start vertex
    global clicked, press_x, press_y
    clicked = True
    press_x  = mx
    press_y = my

def move(mx, my): #needed to hover over the goal
    global mouse_x, mouse_y
    mouse_x = mx
    mouse_y = my


def draw():
    global vertex_dict, mouse_y, mouse_x, press_x, press_y, clicked, start_vertex, goal_vertex
    clear()
    draw_image(img, 0, 0)

    for key in vertex_dict: #every vertex will draw its self and its adjacency list in blue
        vertex_dict[key].draw_edges_adjacent(0, 0, 1)

        if vertex_dict[key].mouse_func(press_x, press_y):  #if the value at vertex_dict[key] is true and the mouse is pressed, the vertex will change color to red
            start_vertex = vertex_dict[key]  #initializes start vertex needed for bfs
            start_vertex.draw_vertex(1, 0, 0)

        elif vertex_dict[key].mouse_func(mouse_x, mouse_y) and clicked:
            goal_vertex = vertex_dict[key] #initializes goal vertex needed for bfs
            goal_vertex.draw_vertex(1, 0, 0)

        else:
            vertex_dict[key].draw_vertex(0, 0, 1)

    path = breadth_first_search(start_vertex, goal_vertex)  #calls the bfs function from another file

    i = 0
    while i < len(path)-1:
        path[i].draw_vertex(1, 0, 0)
        path[i].draw_edge(path[i + 1], 1, 0, 0) #draws the path from start to goal
        i = i + 1


vertex_dict = load_graph('dartmouth_graph.txt')
img = load_image("dartmouth_map.png")

start_graphics(draw, width = W_WIDTH, height = W_HEIGHT, mouse_press = press, mouse_move= move)
