import networkx as nx
import matplotlib.pyplot as plt
import pylab
node_colors_hash={}
node_colors=[]
dag = nx.digraph.DiGraph()
graph = { 1 : [],
          2 : [],
          3 : [4],
          4 : [2],
          5 : [1,2],
          6 : []
        } 

dag.add_nodes_from([1, 2, 3, 4, 5, 6])

dag.add_edges_from([(6, 3), (6, 1), (5, 1), (5, 2),
                      (3, 4),(4, 2)])
nodes=list(dag.nodes)
edges=dict(dag.edges)
print(edges)  
o=len(nodes)

def draw_graph(graph, node_size):
    global node_colors, node_colors_hash
    global dag
    global nodes
    global edges
   
   
    node_colors_hash = {x:"green" for x in nodes}

    for k,v in node_colors_hash.items():
        node_colors.append(v)
   
    pos = nx.shell_layout(dag)
    nx.draw(dag, pos, with_labels=True,node_size = 800, node_color=node_colors)                        
    # show graph
    pylab.show
    plt.pause(3)


def topologicalSortUtil(g, v, visited, stack):
        global graph
        global nodes
        change_node_color('gray', nodes[v-1])
        # Mark the current node as visited.
        visited[v-1] = True

        # Recur for all the vertices adjacent to this vertex
        for i in graph[v]:
            #print(i)
            if visited[i-1] == False:
                topologicalSortUtil(g,i, visited, stack)
        change_node_color('blue', nodes[v-1])
        # Push current vertex to stack which stores result
        stack.append(v)
def topologicalSort(g):
        global nodes
        global o
        # Mark all the vertices as not visited
        visited = [False]*o
        stack = []
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(1,o+1):
            if visited[i-1] == False:
                topologicalSortUtil(g,i, visited, stack)
 
        # Print contents of the stack
        print(stack[::-1])


def change_node_color(c, node):
    global node_colors_hash
    global node_colors
    global edge_colors,edge_colors_hash
    
    node_colors = []

    # Color the visited node
    node_colors_hash[node]=c

    for k,v in node_colors_hash.items():
        node_colors.append(v)
    
    pos = nx.shell_layout(dag)
    nx.draw(dag, pos,node_size = 800, node_color = node_colors)
    pylab.draw()
    plt.pause(2)

print(nodes)    
draw_graph(dag,len(dag.edges))
topologicalSort(dag)
plt.pause(30)  
                           