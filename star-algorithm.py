import heapq
import math


class Node:
    def __init__(self, parent=None, position=None, name=None):
        # attributes of the nodes
        self.parent = parent
        self.position = position
        self.name = name

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        # function used to compare if two nodes are the same
        return self.position == other.position

    def __lt__(self, other):
        # function used to compare distance of two nodes in the heapq
        return self.f < other.f


def node_distance(first_node, second_node):
    # Distance between nodes
    return math.sqrt(((first_node.position[0] - second_node.position[0]) ** 2) + (
                            (first_node.position[1] - second_node.position[1]) ** 2))


def shortest_path(m, start, goal):
    """
    This is the implementation of the algorithm. You should adapt this code depending of the map and the nodes defined
    in the map.
    :param m: Map in which this algorithm will work
    :param start: Initial Node
    :param goal: End node
    :return: Shortest path from the initial and end node
    """
    # Create nodes
    start_node = Node(None, m.intersections[start], start)
    end_node = Node(None, m.intersections[goal], goal)

    open_nodes = []
    closed_nodes = []

    # initialize queue
    heapq.heappush(open_nodes, start_node)

    while len(open_nodes) > 0:
        # Use the next node in the queue
        current_node = heapq.heappop(open_nodes)
        # append the used node
        closed_nodes.append(current_node.name)

        # return the path when the current node matches the end node
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.name)
                current = current.parent
            return path[::-1]

        # create node objects with every node related to the actual node
        for child in m.roads[current_node.name]:

            if child not in closed_nodes:
                child_node = Node(current_node, m.intersections[child], child)

                child_node.g = current_node.g + node_distance(child_node, current_node)
                child_node.h = node_distance(child_node, end_node)
                child_node.f = child_node.g + child_node.h

                heapq.heappush(open_nodes, child_node)

    return "Unable to find a path"
