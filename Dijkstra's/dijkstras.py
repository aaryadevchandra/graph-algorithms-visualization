from sys import maxsize
import sys
import numpy as np


# Node class for defining each node
class Node:
    def __init__(self, cost, node):
        self.cost = cost
        self.node = node
        

# function to get all costs from list of 'Node' class' objects
def getNodeCosts(nodes_list):
    costs = []
    for node in nodes_list:
        costs.append(node.cost)
    return costs

# acts as extract min operation, gets min cost node for every iteration
def getNextIndexFromMinCost(relaxed):
    costs = getNodeCosts(relaxed)
    min_cost = min(costs, default=-1)
    for i in range(len(relaxed)):
        if min_cost == relaxed[i].cost:
            return relaxed[i].node, i

# function to fill list that keeps track of every iteration of costs for all nodes
def fill_node_cost_tracker(nodes1d, graphics_node_cost_tracker):
    temp = []
    for node in nodes1d:
        temp.append(node.cost)
    graphics_node_cost_tracker.append(temp)    


def dijkstras(graph, nodes1d, start_node, end_node):
    # pretty self explanatory
    relaxed = [] # relaxed is a list of all the relaxed nodes at every iteration
    discovered = []

    node_number = start_node
    discovered.append(node_number)

    graphics_node_cost_tracker = []

    while True:
        # for all neighbours of node = node_number
        for j in range(len(nodes1d)):
            # if edge exists 
            if graph[node_number][j] > 0:
                # if cost(u, v) + cost(u) < cost(v); basically condition for relaxing nodes
                if nodes1d[j].cost > (nodes1d[node_number].cost + graph[node_number][j]):
                    nodes1d[j].cost = nodes1d[node_number].cost + graph[node_number][j]
                    # fill in list 'relaxed' which holds list of all relaxed nodes at every iteration
                    relaxed.append(nodes1d[j])
                    fill_node_cost_tracker(nodes1d, graphics_node_cost_tracker)                   
        if len(relaxed) != 0:
            # get min cost node from list 'relaxed'
            node_number, i = getNextIndexFromMinCost(relaxed) # since in relaxed[] node number may not be equal to index
            
            # new node_number is this min cost node we just found and we continue iteration from this new node_number 
            if node_number not in discovered:
                discovered.append(node_number)
            # popping the min cost node, cause if not, at every iteration the min cost node will be the same
            relaxed.pop(i)
            
            # if min cost node popped is equal to our end node, exit the while loop
            if node_number == end_node:
                break
    
    print('route to take is: ', discovered)
    # print(graphics_node_cost_tracker)
    return graphics_node_cost_tracker, discovered

#################################################################################################################################
# graph = np.array([[0, 1, 7, 0, 2, 0], 
#                   [1, 0, 0, 3, 4, 0], 
#                   [7, 0, 0, 2, 0, 1], 
#                   [0, 3, 2, 0, 0, 5], 
#                   [2, 4, 0, 0, 0, 0], 
#                   [0, 0, 1, 5, 0, 0]]) 

# graph = np.array([[0, 3, 0, 0, 3], 
# [3, 0, 7, 2, 0], 
# [0, 7, 0, 1, 0], 
# [0, 2, 1, 0, 5], 
# [3, 0, 0, 5, 0]])

# graph = np.array([[0, 0, 0, 1, 2], 
# [0, 0, 1, 3, 3], 
# [0, 1, 0, 6, 0], 
# [1, 3, 6, 0, 0], 
# [2, 3, 0, 0, 0]])

# graph = np.array([[0, 2, 0, 6, 0, 0], 
#                     [2, 0, 0, 3, 2, 0], 
#                     [0, 0, 0, 1, 4, 5], 
#                     [6, 3, 1, 0, 1, 2], 
#                     [0, 2, 4, 1, 0, 3], 
#                     [0, 0, 5, 2, 3, 0]] 
#                     )



# #################################################################################################################################



# def main():
    
#     start_node = int(input('Enter starting node: '))
#     end_node = int(input('Enter ending node: '))

#     nodes1d = []    
#     for i in range(graph.shape[0]):
#         nodes1d.append(Node(maxsize, i))


#     # initializing starting nodes cost to be 0
#     nodes1d[start_node].cost = 0

#     dijkstras(graph, nodes1d, start_node, end_node)

# if __name__ == '__main__':
#     main()
