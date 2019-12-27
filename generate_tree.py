import networkx as nx
import matplotlib.pyplot as plt
from A_star_algo import G_astar
from Node import Node

initial_state = [2,8,3,
                 1,6,4,
                 7,0,5]
i_node = Node(initial_state, None, 0)
color_dict = {'traversed':'g', 'goal':'y'}

def nodes_pos(G, root, width=0.5, vert_gap = 1, vert_pos = 0, xcenter = 0, pos = None, parent = None):
    if pos is None:
        pos = {root:(xcenter,vert_pos)}
    else:
        pos[root] = (xcenter, vert_pos)
    
    children = list(G.neighbors(root))
    
    if parent is not None:
        children.remove(parent)  
    
    if len(children)!= 0:
        if len(children) == 4:
            width = 0.1
        if len(children) == 3:
            width = 1
        else:
            width = len(children)/2
        dx = width/len(children) 
        nextx = xcenter - width/2 - dx/2
        for child in children:
            nextx += dx
            pos = nodes_pos(G,child, width = dx, vert_gap = vert_gap, 
                                vert_pos = vert_pos-vert_gap, xcenter=nextx,
                                pos=pos, parent = root)
    return pos

pos = nodes_pos(G_astar, str(i_node))
tree_color_list = [color_dict[i[1]]for i in G_astar.nodes.data('color')]
# plt.title('8 puzzle solution using A*(manhattan distance)')

nx.draw(G_astar, pos= pos, node_color = tree_color_list, with_labels= True,node_size=900, font_size= 5, font_weight= 'bold')

# Draw edge labels
edge_labels =dict([((u, v), d['label']) for u, v, d in G_astar.edges(data=True)])
nx.draw_networkx_edge_labels(G_astar, pos=pos, edge_labels=edge_labels, font_size=8, label_pos= 0.5, rotate = False)
plt.savefig('solution.png')
plt.show()