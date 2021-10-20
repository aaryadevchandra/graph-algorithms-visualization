import numpy as np
from time import sleep


# class for defining each node object
class Node:

    def __init__(self, i, j, val):
        self.i = i
        self.j = j
        self.val = val
        # indexcomb stands for index combination and is used to uniquely identify a pair of nodes 
        self.indexcomb = str(i) + str(j)

# class for defining each edge object
class Edge:

    def __init__(self, u, v):
        self.u = u
        self.v = v
        # this data member 'edgecomb' is used for uniquely identifying each node pair connected by an edge
        self.edgecomb = str(u) + "," + str(v)


# function for testing out the graph (not used in actual code)
def displayNodeGraph(node_graph):

    for i in range(len(node_graph)):
        for j in range(len(node_graph)):
            print(node_graph[i][j].val) 


# function to check if an edge has been added in the tree or not
# this is done using the string combination of the 2 nodes connected by that edge
def checkTreeAddingCondition(tree, edge):

    if (str(edge.v) + str(edge.u)) in tree:
        return -1
    else:
        return 1

def bfs(graph, tree, discovered):

    node_graph = []

    # converting the 2-D numpy matrix to a 2-D list of type 'Node'
    for i in range(graph.shape[0]):
        graph_row = []
        for j in range(graph.shape[1]):
            node = Node(i, j, graph[i, j])
            graph_row.append(node)

        node_graph.append(graph_row)

    # setting all discovered to false

    # point to note - discovered is indexed by the node values and not the node indexes. and each value of discovered (indexed) by its node
    # is set to false initially
    discovered[node_graph[0][0].indexcomb] = True
    for i in range(len(node_graph)):
        for j in range(len(node_graph[0])):
            if i != 0 or j != 0:
                discovered[node_graph[i][j].indexcomb] = False

    L = []
    L.append(node_graph[0][0]) 

    while len(L) != 0: 
        curr_node = L.pop(0)

        # traversing along all neighbours of a node (traversing columns of a particular row of a graph)
        for j in range(len(node_graph[curr_node.i])):
            # if edge exists and not in discovered
            if node_graph[curr_node.i][j].val > 0 and discovered[node_graph[curr_node.i][j].indexcomb] == False:
                # discovered [ node ][ neighbour ] set to True; setting an edge to True (basically adding in discovered)
                discovered[node_graph[curr_node.i][j].indexcomb] = True
                
                # creating an Edge class' object
                edge = Edge(curr_node.i, j)

                # passing the object 'edge' to a function that checks whether this edge has been added to our final tree
                if checkTreeAddingCondition(tree, edge) == 1:
                    tree.append(edge.edgecomb) 
               # print(tree)
               # print('\n\n')

                # storing (node, neighbour) index combination in 'L' in reverse order i.e. (neighbour, node)
                # this is because if we store it in (node, neighbour) form, we will in the future at some point reach 
                # (neighbour, node) which we don't need to check in any case. so to avoid making a function that reverses 
                # each index combination and checks, we can just store the reversed combination and check without reversing
                # if such a combination exists
                L.append(node_graph[j][curr_node.i])
    
    return tree
   

# def main():

   #  graph = np.array([[0, 0, 3, 0, 0, 5, 0],
   #      [0, 0, 0, 0, 11, 7, 18], 
   #      [3, 0, 0, 0, 0, 0, 11], 
   #      [0, 0, 0, 0, 8, 0, 3], 
   #      [0, 11, 0, 8, 0, 1, 0], 
   #      [5, 7, 0, 0, 1, 0, 0], 
   #      [0, 18, 11, 3, 0, 0, 0]])


    # graph = np.array([[1,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0],
    #     [0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,1],
    #     [1,1,1,1,0,0,1,1,1,0,0,1,1,0,0,0],
    #     [0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0],
    #     [1,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0],
    #     [0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0],
    #     [1,0,1,1,0,1,0,0,0,0,0,1,1,1,1,0],
    #     [0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1],
    #     [1,0,0,1,0,1,1,0,1,0,1,1,1,1,0,1],
    #     [0,1,1,1,0,0,1,1,0,0,0,1,0,1,0,1],
    #     [0,0,1,1,1,0,1,1,1,1,0,0,1,0,1,0],
    #     [1,1,0,1,1,0,0,0,0,1,1,1,0,0,1,0],
    #     [0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0],
    #     [1,0,0,1,1,1,1,0,1,0,1,1,0,1,0,1],
    #     [0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,0],
    #     [0,1,0,1,0,1,0,1,1,1,1,1,1,0,0,1]])

   #  discovered = {}
   #  tree = []

   #  tree =  bfs(graph, tree, discovered)
   #  print(tree)



# if __name__ == '__main__':
#     main()
