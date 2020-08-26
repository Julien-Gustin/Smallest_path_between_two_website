import time
from utils.tree import Node
from threading import Thread, RLock

lock = RLock()

""" Bfs

    @bref: A thread which execute a bfs, in theorie this class should be instantiated two times one at the goals of the search and one at the start with goals pointing in the same dictionary.

    @param node: a Node which contain a payload
    @param goals: a dictionary which contains {node.payload: node} and verify if a goal has been reached
    @param get_children: a method to get the children of a node
"""
class Bi_Bfs(Thread):
    def __init__(self, node, goals, get_children):
        Thread.__init__(self)
        self.nodes = [node]
        self.explored_set = [node.payload]
        self.get_children = get_children
        self.goals = goals
        self.sol = []

    def bfs(self):
        frontier = []

        for node in self.nodes:
            children = self.get_children(node.payload)
            print("=== {} ===".format(len(self.nodes)))

            for child in children:
                if child not in self.explored_set:
                    print(child)
                    n_child = Node(child, node)
                    self.explored_set.append(n_child.payload)
                    frontier.append(n_child)

                    with lock:
                        if n_child.payload in self.goals.keys():
                            sol = []
                            while n_child is not None:
                                sol.append(n_child.payload)
                                n_child = n_child.parent

                            self.sol = sol
                            return

                        self.goals[child] = n_child

        if len(frontier) == 0:
            return None

        self.nodes = frontier
        return self.bfs()

    def run(self):
        self.bfs()
