import pygame
import bfs
from random import randint

# creating Node class that represents each node on our visualization screen
class Node:

    def __init__(self, coords, number):
        # contains the actual node number and its coordinates on our screen which are useful for rendering on the screen
        # and keeping track of which node was rendered where. coords is a tuple -> (x_coordinate, y_coordinate)
        self.number = number
        self.coords = coords


# function to render all the node circles and their numbers 
def create_node_circle(window, occurred_spots, nodeNumber):

    # node_current_occurrence_coords is a tuple storing a random (x, y) from between (200, 1500) and (10, 600) respectively  
    node_current_occurrence_coords = (randint(200, 1500), randint(10, 600))

    # initialization function calls for being able to use font/text functionality in pygame
    pygame.font.init()
    nodeFont = pygame.font.SysFont('Comic Sans MS', 19)

    # checking if our randomly generated coords have been previously already generated (probability is low but still checking was essential)
    if node_current_occurrence_coords not in occurred_spots:
        # adding the new coords if they don't already exist
        occurred_spots.append(node_current_occurrence_coords)
        
        # render circle and its text using the coordinates provided
        pygame.draw.circle(window, (255, 255, 0),
                           node_current_occurrence_coords, 20)
        textsurface = nodeFont.render(f"{nodeNumber}", False, (255, 0, 255))
        window.blit(textsurface, (node_current_occurrence_coords[0] - 9, node_current_occurrence_coords[1] - 15))

    else:
        # if exact coords had been previously generated, we call the function again to generate new coords
        create_node_circle(window, occurred_spots, nodeNumber)

    return node_current_occurrence_coords


# function to render our node circles and connect them using lines
def init_graph(graph, node_list, window, occurred_spots):

    # node_list is a list of Node objects
    for i in range(graph.shape[0]):
        node_list.append(Node(create_node_circle(window, occurred_spots, i), i))

    # traversing the 2D adjacency matrix and rendering lines between any two nodes whose edge cost is > 0 
    for i in range(graph.shape[0]):
        for j in range(graph.shape[1]):
            if graph[i][j] > 0:
                pygame.draw.line(window, (255, 255, 255),
                                 node_list[i].coords, node_list[j].coords, 2)

    # font initialization
    pygame.font.init()
    nodeFont = pygame.font.SysFont('Comic Sans MS', 19)

    # rendering circles and node number fonts/texts again

    # point to note - pygame works by rendering surfaces on top of other surfaces. when I rendered the lines on top of the node circles
    # the node circles got slightly covered by the thin lines, which gave it a bad look. 
    # hence I rendered the nodes again on top of the lines

    for i in range(graph.shape[0]):
        pygame.draw.circle(window, (255, 255, 0), node_list[i].coords, 20)
        textsurface = nodeFont.render(f"{node_list[i].number}", False, (255, 0, 255))
        window.blit(textsurface, (node_list[i].coords[0] - 9, node_list[i].coords[1] - 15))


# since I'm using an index combination of string data type, I need to split them into integer numbers for traversing and other operations
# hence this function takes the string combination of indexes eg: "3,4" and splits it into integers 3 and 4
def returnNodeIndices(node):
    x = node.split(',')
    return x[0], x[1]

# this function is very important for the code
# this function keeps a track of all the nodes and edges that were discovered, since when the surface is updated/refreshed
# the discovered nodes and edges have to have a separate colour  
def trackDiscoveredNodes(window, discovered_nodes_render, node_list, graph):

    # for i in range(0, len(discovered_nodes_render), 2):
    #     pygame.draw.circle(window, (0, 0, 255),
    #                        discovered_nodes_render[i].coords, 20)

    #     try:
    #         pygame.draw.line(window, (255, 0, 0), discovered_nodes_render[i].coords, discovered_nodes_render[i+1].coords, 2)
    #     except:
    #         pass

    # font initialization
    pygame.font.init()
    nodeFont = pygame.font.SysFont('Comic Sans MS', 19)

    # rendering yellow node circles
    for i in range(graph.shape[0]):
        pygame.draw.circle(window, (255, 255, 0), node_list[i].coords, 20)
        textsurface = nodeFont.render(f"{node_list[i].number}", False, (255, 0, 255))
        window.blit(textsurface, (node_list[i].coords[0] - 9, node_list[i].coords[1] - 15))

    # discovered_nodes_render is a list of 'Node' objects that have been discovered
    # all node circles rendered over here will hence be blue in colour (since that's the colour I've given for discovered nodes)
    for i in range(0, len(discovered_nodes_render), 2):
        pygame.draw.circle(window, (0, 0, 255),
                           discovered_nodes_render[i].coords, 20)

        # rendering the node numbers on the circles
        textsurface = nodeFont.render(f"{discovered_nodes_render[i].number}", False, (255, 0, 255))
        window.blit(textsurface, (discovered_nodes_render[i].coords[0] - 9, discovered_nodes_render[i].coords[1] - 15))

        # rendering red lines for all the connected nodes. for every i and i+1th node a red line is drawn and hence the for loop
        # has a step of 2, since we wish to skip the i+1th node and go to the i + 2th node cause
        # i and i+1th node are connected and the i+2th node and the i+3th node are connected but the i+1th and i+2th node
        # may not be connected 
        try:
            pygame.draw.line(window, (255, 0, 0), discovered_nodes_render[i].coords, discovered_nodes_render[i+1].coords, 2)
        except:
            pass

    


def main():

    # larger graph for more aesthetics
    # graph = bfs.np.array([[0, 3, 4, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    # [3, 0, 5, 2, 5, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    # [4, 5, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    # [0, 2, 1, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
    # [2, 5, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    # [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
    # [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
    # [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
    # [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0], 
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
    # [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0], 
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
    # [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0], 
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1], 
    # [0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])


    # smalled graph to understand and easily visualize BFS
    graph = bfs.np.array([[0, 0, 0, 1, 2], 
                    [0, 0, 1, 3, 3], 
                    [0, 1, 0, 6, 0], 
                    [1, 3, 6, 0, 0], 
                    [2, 3, 0, 0, 0]])

    discovered = {}
    tree = []

    # the tree we get in bfs.py is returned over here
    tree = bfs.bfs(graph, tree, discovered)

    # library function for initializing all pygame classes
    pygame.init()

    # variables for setting window height and width
    window_height = 700
    window_width = 1800

    # getting a surface object called 'window'
    window = pygame.display.set_mode((window_width, window_height))
    # setting caption for the pygame window (shown at the top left of the window)
    pygame.display.set_caption("Breadth First Search Visualization")

    # variable for running main game loop
    run = True

    # list to store tuples of (x, y) coords to check if the randomly generated coords are already generated
    occurred_spots = []
    
    # list to store 'Node' class objects
    node_list = []

    init_flag = 0

    # list to store 'Node' class' objects; specifically those nodes that have been discovered
    discovered_nodes_render = []

    while run:

        # we wish to run init_graph() function only once; hence the flag
        if init_flag == 0:
            init_graph(graph, node_list, window, occurred_spots)
            init_flag = 1

        # pop out an edge/node pair/index combination from the returned tree
        try:
            node = tree.pop(0)
        except IndexError:
            print("Breadth First Search Complete ")
            run = False
            exit(0)

        # split up the index combination in two integers
        i, j = returnNodeIndices(node)

        # added these integers in discovered nodes list
        discovered_nodes_render.append(node_list[int(i)])
        discovered_nodes_render.append(node_list[int(j)])

        trackDiscoveredNodes(window, discovered_nodes_render, node_list, graph)


        # code for exiting the program if the top right quit (red cross) button is clicked or the 'q' button on the keyboard is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

        # important function that updates the surface or window. if this is not called the screen will not update and everything 
        # will remain static
        pygame.display.update()

        # giving the visualization a small delay
        pygame.time.wait(1000)

    # destroy all objects and exit
    pygame.quit()


if __name__ == '__main__':
    main()
