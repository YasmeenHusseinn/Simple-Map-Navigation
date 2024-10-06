#Author: Yasmeen Hussein
#Date: 3/7/2023
#Purpose: BFS

from collections import deque

def breadth_first_search(start, goal):  
    frontier = deque()
    back_pointer = {}
    frontier.append(start)
    back_pointer[start] = None

    while (len(frontier)!=0) and (goal not in back_pointer):
        curr_vertex = frontier.popleft()
        for vertex in curr_vertex.adjacent_list:
            if vertex not in back_pointer:
                frontier.append(vertex)
                back_pointer[vertex] = curr_vertex

    v = goal
    path = []
    while v != None:
        path.append(v)
        bp = back_pointer[v]
        v = bp

    return path


