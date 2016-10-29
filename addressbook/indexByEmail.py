class Node(object):

    def __init__(self):
        self.nodes = {}
        self.values = []

    def createTreeIndex(self, key):
        """Create a tree index for email address"""
        if key not in self.nodes:
            self.nodes[key] = Node()
        return self.nodes[key]

    def saveValue(self, value):
        """Save the firstName and lastName as value"""
        self.values.append(value)

    def getNode(self, key):
        """Get a node that matches the key"""
        if key in self.nodes:
            return self.nodes[key]
        return None

    def getValues(self):
        values = self.values
        for node in self.nodes.values():
            values += node.getValues()
        return values;

class IndexByEmail(object):

    def __init__(self):
        self.tree = Node()

    def addEmail(self, email, value):
        node = self.tree
        for ch in email:
            node = node.createTreeIndex(ch)
        if node:
            node.saveValue(value)

    def getEmail(self, value):
        ret_values = []
        node = self.tree
        for ch in value:
            if node == None:
                break
            else:
                node = node.getNode(ch)
        if node != None:
            return node.getValues()