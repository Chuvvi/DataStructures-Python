class node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = node()

    def add(self, data):
        current_node = self.root
        if current_node.data == None:
            current_node.data = data
        while True:
            if current_node.data > data:
                if current_node.left == None:
                    break
                current_node = current_node.left
            elif current_node.data < data:
                if current_node.right == None:
                    break
                current_node = current_node.right
            else:
                break
        new_node = node(data)
        if current_node.data > data:
            current_node.left = new_node
        elif current_node.data < data:
            current_node.right = new_node

    def find(self, element):
        current_node = self.root
        previous_node = self.root
        while True:
            if element == current_node.data:
                return [current_node, previous_node]
            elif element < current_node.data:
                if current_node.left == None:
                    break
                previous_node = current_node
                current_node = current_node.left
            elif element > current_node.data:
                if current_node.right == None:
                    break
                previous_node = current_node
                current_node = current_node.right
        return None

    def remove(self, element):
        nodes = self.find(element)
        if nodes == None:
            print (element, "does not exist in the given bst")
            exit()
        current_node = nodes[0]
        previous_node = nodes[1]
        #case 1: Leaf Node
        if current_node.left == None and current_node.right == None:
            if element < previous_node.data:
                previous_node.left = None
            else:
                previous_node.right = None
        #case 2: Left node is None
        elif current_node.left == None:
            if element < previous_node.data:
                previous_node.left = current_node.right
            else:
                previous_node.right = current_node.right
        #case 3: Right node is None
        elif current_node.right == None:
            if element < previous_node.data:
                previous_node.left = current_node.left
            else:
                previous_node.right = current_node.left
        #case 4: None of the nodes are None
        elif current_node.right != None and current_node.left != None:
            previous_node2 = current_node
            current_node2 = current_node.left
            while current_node2.right != None:
                previous_node2 = current_node2
                current_node2 = current_node2.right
            data = current_node2.data
            if data == previous_node2.left.data:
                previous_node2.left = current_node2.left
            elif data == previous_node2.right.data:
                previous_node2.right = current_node2.left
            current_node.data = data

    def preorder(self, node):
        if node == None:
            return
        print(node.data)
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

    def postorder(self, node):
        if node == None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data)

    def levelorder(self, node):
        a = []
        a.append(node)
        while a != []:
            if a[0].left == None and a[0].right != None:
                a.append(a[0].right)
            elif a[0].right == None and a[0].left != None:
                a.append(a[0].left)
            elif a[0].left != None and a[0].right != None:
                a.append(a[0].left)
                a.append(a[0].right)
            print(a[0].data)
            del a[0]

    def height(self, node):
        if node == None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def isempty(self):
        if self.root.data == None:
            return True
        return False

if __name__ == '__main__':
    '''
    bst = BinarySearchTree()
    bst.add(5)
    bst.add(4)
    bst.add(6)
    bst.add(3)
    bst.add(7)
    bst.add(2)
    bst.add(8)
    bst.add(1)
    bst.add(9)
    bst.add(0)
    root = bst.root
    print(bst.remove(6))
    bst.inorder(root)
    '''
    bst1 = BinarySearchTree()
    bst1.add(11)
    bst1.add(6)
    bst1.add(3)
    bst1.add(8)
    bst1.add(1)
    bst1.add(5)
    bst1.add(15)
    bst1.add(13)
    bst1.add(17)
    bst1.add(12)
    bst1.add(14)
    bst1.add(19)
    root = bst1.root
    print("Post Order: ")
    bst1.postorder(root)
    print("Level Order: ")
    bst1.levelorder(root)
    print(bst1.height(root))