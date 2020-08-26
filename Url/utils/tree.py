class Node:
    def __init__(self, payload, parent=None):
        self.payload = payload
        self.parent = parent

    def equal(self, node):
        return self.payload == node.payload
