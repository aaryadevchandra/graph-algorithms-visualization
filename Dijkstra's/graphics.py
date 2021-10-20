import pygame
import dijkstras
from random import randint
from sys import maxsize
import numpy as np


# class that defines each node circle on the screen
# contains x and y coordinate of where the node circle was rendered on the screen
# contains the number of the node which is equal to nodeNumber
class PygameNode:

    def __init__(self, x, y, nodeNumber):
        self.x = x
        self.y = y
        self.nodeNumber = nodeNumber

# okay so.......
# the cost of the edge has to be rendered at the midpoint of the edge line
# so this function does some maths to figure out the coords to render the edge cost 
def findedgeCostCoords(surface, x1, y1, x2, y2, edge_cost):
    a = (x1+x2)/2
    b = (y1+y2)/2

    # initializint text render operations and rendering it at the calculated coordinates
    pygame.font.init()
    nodeFont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = nodeFont.render(f"{edge_cost}", False, (255, 0, 255))
    surface.blit(textsurface, (a, b))

# function to render all the node circles on the screen 
def initNodes(surface, discovered):

    pygameNodes = []
    for i in range(len(discovered)):

        # the x, y coords of the node circles are randomly generated
        x = randint(20, 950)
        y = randint(20, 750)
        pygame.draw.circle(surface, (255, 255, 0), (x, y), 30, 5)

        # creating a new PygameNode object and appending in pygameNodes list
        pygameNodes.append(PygameNode(x, y, discovered[i]))

    return pygameNodes

# rendering the connecting lines for all the node circles  
def connectNodes(surface, pygameNodes, graph, node_to_update, cost_to_update):

    # rendering white connecting lines and edge costs
    for i in range(len(pygameNodes)):
        for j in range(len(pygameNodes)):
            # if edge cost between the two node circles is > 0, then draw the line
            if graph[pygameNodes[i].nodeNumber][pygameNodes[j].nodeNumber] > 0:
                # draws a white line
                pygame.draw.line(surface, (255, 255, 255), (pygameNodes[i].x, pygameNodes[i].y), (pygameNodes[j].x, pygameNodes[j].y), 3)
                # function to calculate the coords of where to render the edge costs, mentioned above
                findedgeCostCoords(surface, pygameNodes[i].x, pygameNodes[i].y, pygameNodes[j].x, pygameNodes[j].y, graph[pygameNodes[i].nodeNumber][pygameNodes[j].nodeNumber])

    pygame.font.init()
    nodeFont = pygame.font.SysFont('Comic Sans MS', 30)

    # if this flag (node_to_update) is -1, there are no node costs to update
    if node_to_update == -1:

        # if node_to_update is -1, then render node circles and their costs normally 
        for i in range(len(pygameNodes)):
            pygame.draw.circle(surface, (255, 255, 0), (pygameNodes[i].x, pygameNodes[i].y), 30, 0)
            textsurface = nodeFont.render(f"{pygameNodes[i].nodeNumber}", False, (255, 0, 0))
            surface.blit(textsurface, (pygameNodes[i].x - 10, pygameNodes[i].y - 20))
            textsurface = nodeFont.render(f"inf", False, (255, 0, 0))
            surface.blit(textsurface, (pygameNodes[i].x - 10, pygameNodes[i].y - 70))

    else:
        # if node_to_update is not -1, (and rather stores the node to update); then node circles are rendered normally
        # but cost on top of the node to update is changed to 'cost_to_update'
        for i in range(len(pygameNodes)):
            pygame.draw.circle(surface, (255, 255, 0), (pygameNodes[i].x, pygameNodes[i].y), 30, 0)
            textsurface = nodeFont.render(f"{pygameNodes[i].nodeNumber}", False, (255, 0, 0))
            surface.blit(textsurface, (pygameNodes[i].x - 10, pygameNodes[i].y - 20))
            if i == node_to_update:
                textsurface = nodeFont.render(f"{cost_to_update}", False, (255, 0, 0))
                surface.blit(textsurface, (pygameNodes[i].x - 10, pygameNodes[i].y - 70))

    return pygameNodes
    

# important function that renders all the required surfaces of pygame along with also updating the required surfaces
def update_graph(surface, node_cost_tracker, iteration, pygameNodes, graph, discovered, maintain_red, node_cost_tracker_iterator):
    
    # each iteration has to be started again from a blank canvas hence filling screen with black
    surface.fill((0, 0, 0))

    # rendering node circles and white connecting lines
    for i in range(len(pygameNodes)):
        connectNodes(surface, pygameNodes, graph, i, node_cost_tracker[node_cost_tracker_iterator][i])

    # animation for checking neighbouring nodes
    for i in range(len(pygameNodes)):
        pygame.time.wait(2000)
        # draws green line with a 2 second delay to simulate checking neighbours of a particular node
        if iteration.nodeNumber != pygameNodes[i].nodeNumber and graph[iteration.nodeNumber][pygameNodes[i].nodeNumber] > 0:
            pygame.draw.line(surface, (0, 255, 0), (iteration.x, iteration.y), (pygameNodes[i].x, pygameNodes[i].y), 3)
            
            # maintain_red is a list of nodes that have been discovered and hence their connecting lines have to be rendered red
            # rendering red lines for all discovered pairs of nodes
            for i in range(len(maintain_red)):
                pygame.draw.line(surface, (255, 0, 0), (maintain_red[i][0].x, maintain_red[i][0].y), (maintain_red[i][1].x, maintain_red[i][1].y), 3)
            
            # updating the screen at every iteration of green line drawn, so all green lines are not rendered together
            pygame.display.update()

    # maintain_red is a list of lists of pairs of nodes whose edge has to be rendered red
    red = []
    red.append(pygameNodes[node_cost_tracker_iterator])
    red.append(pygameNodes[node_cost_tracker_iterator + 1])
    maintain_red.append(red.copy())
    

def main():
    
    # function that initializes all pygame classes and modules
    pygame.init()

    # setting the window height and width
    window_h = 800
    window_w = 1000

    # getting a surface object of the screen; this surface object is used to render any objects on the screen and is used throughout 
    # the program
    surface = pygame.display.set_mode((window_w, window_h))

    # screen filled with black colour
    surface.fill((0, 0, 0))

    initNodesFlag = 0

    # adjacency matrix
    graph = np.array([[0, 0, 0, 1, 2], 
                    [0, 0, 1, 3, 3], 
                    [0, 1, 0, 6, 0], 
                    [1, 3, 6, 0, 0], 
                    [2, 3, 0, 0, 0]])


    # start and end node input
    start_node = int(input('Enter starting node: '))
    end_node = int(input('Enter ending node: '))

    # main node list
    # initializing nodes1d list
    nodes1d = []
    for i in range(graph.shape[0]):
        nodes1d.append(dijkstras.Node(maxsize, i))

    # initializing starting nodes cost to be 0
    nodes1d[start_node].cost = 0


    node_cost_tracker, discovered = dijkstras.dijkstras(graph, nodes1d, start_node, end_node)
    print(node_cost_tracker)
    
    iteration = 0
    pygameNodes = []
    pygameNodes = initNodes(surface, discovered)

    maintain_red = []

    pygameNodes_copy = pygameNodes.copy()


    node_cost_tracker_iterator = 0

    iteration = pygameNodes_copy.pop(0)
    while iteration.nodeNumber != end_node:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()

        if initNodesFlag != 1:
            initNodesFlag = 1
            connectNodes(surface, pygameNodes, graph, -1, -1)
        
        update_graph(surface, node_cost_tracker, iteration, pygameNodes, graph, discovered, maintain_red, node_cost_tracker_iterator)
        iteration = pygameNodes_copy.pop(0)

        node_cost_tracker_iterator += 1
        
        pygame.display.update()

    pygame.quit()



if __name__ == '__main__':
    main()