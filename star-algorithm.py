import heapq
import math


class Node:
    def __init__(self, parent=None, position=None, name=None):
        self.parent = parent
        self.position = position
        self.name = name

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f


def shortest_path(M, start, goal):
    start_node = Node(None, M.intersections[start], start)
    end_node = Node(None, M.intersections[goal], goal)

    open_nodes = []
    closed_nodes = []

    heapq.heappush(open_nodes, start_node)

    while len(open_nodes) > 0:
        current_node = heapq.heappop(open_nodes)
        closed_nodes.append(current_node.name)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.name)
                current = current.parent
            return path[::-1]

        for child in M.roads[current_node.name]:

            if child not in closed_nodes:
                child_node = Node(current_node, M.intersections[child], child)

                child_node.g = current_node.g + math.sqrt(((child_node.position[0] - current_node.position[0]) ** 2) + (
                            (child_node.position[1] - current_node.position[1]) ** 2))
                child_node.h = math.sqrt(((child_node.position[0] - end_node.position[0]) ** 2) + (
                            (child_node.position[1] - end_node.position[1]) ** 2))
                child_node.f = child_node.g + child_node.h

                heapq.heappush(open_nodes, child_node)
