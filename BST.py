'''
In a BST, the data is kept "balanced" by enforcing certain rules.

If the tree is empty (root points to None),
put the new node at the top of the tree
If the tree is not empty, start at the root.
Compare the new node's value to the current node's value.
If the new node is bigger, move to the right.
If the new node's value is smaller, move to the left.
When there is no node at the current position,
put the new node there.
'''

# Part 1: Create a BSTNode class


class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'The data for this node is {self.data}'

    def __repr__(self):
        return f'This is the repr func for this node: {self.data}'


node1 = BSTNode(3)
print(node1)  # 3

node2 = BSTNode(4, left=node1)
print(node2)  # 4

node3 = BSTNode()
print(node3)  # None
node3.data = 5
print(node3)  # 5

# Part 2: Create a BST class


class BST:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        if self.root is None:
            return 'This tree is empty.'
        else:
            self.output = ''
            self.print_tree(node=self.root)
            return self.output

    def __repr__(self):
        if self.root is None:
            return 'This tree is empty.'
        else:
            self.output = ''
            self.print_tree(node=self.root)
            return self.output

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            self.output += ' ' * 4 * level + '->' + str(node.data) + ' '
            self.print_tree(node.left, level + 1)
    
    

bst = BST()
print(bst)

bst.root = node2
print(bst)

node2.right = node3
print(bst)

# Part 3: Add functionality to your BST class
