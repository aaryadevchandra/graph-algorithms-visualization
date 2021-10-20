import networkx as nx
import matplotlib.pyplot as plt
import pylab
node_colors_hash={}
node_colors=[]
dag = nx.digraph.DiGraph()

dag.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J','K'])

dag.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'J'),
                      ('C', 'F'),('C', 'I'),('D', 'G'), ('E', 'K'),('E','H')])

nodes=(dag.nodes)
edges=(dag.edges)   

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


def dfs(dag, start, visited, stack):
       change_node_color('grey',start)
       if start in visited:

           # node and all its branches have been visited
           return stack, visited


       if dag.out_degree(start) == 0:

           # if leaf node, push and backtrack
           stack.append(start)
           visited.append(start)
           change_node_color('blue',start)  
           return stack, visited
           
       #traverse all the branches
       for node in dag.neighbors(start):

           if node in visited:

               continue

           stack, visited = dfs(dag, node, visited, stack)

       #now, push the node if not already visited
       if start not in visited:

           print("pushing %s"%start)

           stack.append(start)

           visited.append(start)

       return stack, visited

def topological_sort_using_dfs(dag):

       visited = []

       stack=[]

       start_nodes = [i for i in dag.nodes if dag.in_degree(i)==0]
       
   #     print(start_nodes)

       for s in start_nodes:
           change_node_color('gray', s)
           stack, visited = dfs(dag, s, visited, stack)

       print("Topological sorted:")

       while(len(stack)!=0):

           print(stack.pop(), end=" ")


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

    
draw_graph(dag,len(dag.edges))
topological_sort_using_dfs(dag) 
plt.pause(30)  
                            