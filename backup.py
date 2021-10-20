import networkx as nx
import matplotlib.pyplot as plt
import pylab


node_colors_hash={}
node_colors=[]


dag = nx.digraph.DiGraph()

dag.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])

dag.add_edges_from([('A', 'B'), ('A', 'E'), ('B', 'D'), ('E', 'C'),
                      ('D', 'G'),('C', 'G'),('C', 'I'), ('F', 'I')])

nodes=(dag.nodes)


def draw_graph(graph, node_size):
    global node_colors, node_colors_hash
    global dag
    global nodes

    node_colors_hash = {x:"yellow" for x in nodes}

    for k,v in node_colors_hash.items():
        node_colors.append(v)
    
    #nx.set_edge_attributes(dag,'Name', nodes)

    pos = nx.shell_layout(dag)
    nx.draw(dag, pos, with_labels=True,node_size = 600, node_color=node_colors)                        
    # show graph
    pylab.show
    plt.pause(3)


def dfs(dag, start, visited, stack):

       if start in visited:
           
           # node and all its branches have been visited
           return stack, visited


       if dag.out_degree(start) == 0:

           # if leaf node, push and backtrack
           stack.append(start)

           visited.append(start)

           return stack, visited

       #traverse all the branches
       for node in dag.neighbors(start):
           change_node_color('gray', node)
           if node in visited:

               continue

           stack, visited = dfs(dag, node, visited, stack)

       #now, push the node if not already visited
       if start not in visited:

           print("pushing %s"%start)

           stack.append(start)

           visited.append(start)
       change_node_color('black', start)
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
    
    node_colors = []

    # Color the visited node
    node_colors_hash[node]=c

    for k,v in node_colors_hash.items():
        node_colors.append(v)
    
    pos = nx.shell_layout(dag)
    nx.draw(dag, pos,node_size = 600, node_color = node_colors)
    pylab.draw()
    plt.pause(2)
    
    
draw_graph(dag,len(dag.edges))
topological_sort_using_dfs(dag) 
  
                            