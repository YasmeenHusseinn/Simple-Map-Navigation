#Author: Yasmeen Hussein
#Date: 3/5/2023
#Purpose: Vertex class

from LAB_4.vertex import*

def load_graph(filename):
    global vertex_dict
    vertex_dict = {}

    #creating vertex objects
    fp = open(filename, "r")
    for line in fp:
        list = line.strip().split(";")
        coordinate_list = list[2].strip().split(", ")  #splits the coordinates into x and y
        vertex = Vertex(list[0].strip(), int(coordinate_list[0].strip()), int(coordinate_list[1].strip())) #creates a vertex object
        vertex_dict[list[0].strip()] = vertex

    fp.close()

    #creating vertex adjacents
    fp = open(filename, "r")
    for line in fp:
        list = line.strip().split(";")
        vertex = vertex_dict[list[0].strip()]
        adjacent_list = list[1].strip().split(", ")
        for v in adjacent_list:
            vertex.adjacent_list.append(vertex_dict[v])

    fp.close()

    return vertex_dict


load_graph("dartmouth_graph.txt")