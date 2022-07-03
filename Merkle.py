import hashlib



class Node:


    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value



    def hash(val):
        return hashlib.sha256(val.encode('utf-8')).hexdigest()


    def doubleHash(val):
        return Node.hash(Node.hash(val))



class Merkle():

    def __init__(self, values):
        self.buildTree(values)


    def buildTree(self, values):
        leaves = [Node(None, None, Node.doubleHash(e)) for e in values]

        if len(leaves) % 2 == 1:
            leaves.append(leaves[-1:][0])
        self.root = self.buildTreeRec(leaves)


    def buildTreeRec(self, nodes):
        half = len(nodes)
        
        if len(nodes) == 2:
            return Node(nodes[0], nodes[1], Node.doubleHash(nodes[0].value+nodes[1].value))
        left = self.buildTreeRec(nodes[:half])
        right = self.buildTreeRec(nodes[half:])
        value = Node.doubleHash(left.value + right.value)
        return Node(left, right, value)

    def printTree(self):
        self.printTreeRec(self.root)


    def printTreeRec(self, node):
        if node != None:
            print(node.value)
            self.printTreeRec(node.left)
            self.printTreeRec(node.right)



    def getRootHash(self):
        return self.root.value



el = ["hello", "mister", "john"]
mtree = Merkle(el)
print(mtree.getRootHash())
