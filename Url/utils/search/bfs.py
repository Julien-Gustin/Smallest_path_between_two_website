from utils.tree import Node
""" bfs
    @bref: just a simple graph search (bfs)

    @param nodes: a list of nodes of the depth
    @param goal: the goal node
    @param get_children: method to get all children from a node
    @param explored_set: all explored nodes

"""
def bfs(nodes, goal, get_children, explored_set, show=False):
    frontier = []

    if show:
        print("\n =={}== \n".format(len(nodes)))

    for node in nodes:
        children = get_children(node.payload)

        for child in children:
            if child not in explored_set:
                if show:
                    print(child)
                n_child = Node(child, node)

                if n_child.equal(goal):
                    sol = []
                    while n_child is not None:
                        sol.append(n_child.payload)
                        n_child = n_child.parent

                    sol.reverse()
                    return sol

                explored_set.append(n_child.payload)
                frontier.append(n_child)

    if len(frontier) == 0:
        return None

    return bfs(frontier, goal, get_children, explored_set)
