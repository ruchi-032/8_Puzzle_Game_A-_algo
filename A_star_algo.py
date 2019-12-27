from Node import Node
from queue import Queue
import networkx as nx
import matplotlib.pyplot as plt

initial_state = [2,8,3,
                 1,6,4,
                 7,0,5]

G_astar = nx.Graph()

def solve_puzzle(i_state):
    i_node = Node(i_state, None, 0)
    G_astar.add_node(str(i_node), color = 'traversed')
    
    if i_node.is_goal_state():
        return i_node.find_solution()
    
    visited = []
    children_list = []

    next_node = i_node
    while True:
        visited.append(next_node.puzzle_state)
        children = next_node.expand()
        children_list.extend(children)
        max_val = 999999
        for child in children_list:
            if child.calc_f() <= max_val and child.puzzle_state not in visited:
                max_val = child.calc_f()
                selected_child = child
        G_astar.add_node(str(selected_child), color = 'traversed')
        # G_astar.remove_edge(str(selected_child.parent), str(selected_child))
        G_astar.add_edge(str(selected_child.parent), str(selected_child), label= str(selected_child.calc_f()))
        next_node = selected_child
        children_list.remove(selected_child)

        for child in children:
            if child.puzzle_state not in visited and child != selected_child:
                G_astar.add_node(str(child), color = 'traversed')
                G_astar.add_edge(str(child.parent), str(child), label= str(child.calc_f()))
        if child.is_goal_state():
            G_astar.nodes[str(child)]['color'] = 'goal'

            return child.find_solution()
    return


p = solve_puzzle(initial_state)
print(p)