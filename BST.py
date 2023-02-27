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


# Test part 1
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
        self.contents = []

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

    def add(self, node):
        # If the input is of any type other than BSTNode or int, raise a ValueError.
        if type(node) != int and type(node) != BSTNode:
            raise ValueError("You must enter an int or BSTNode")
        # If the input is an int, create a BSTNode with that int as the value.
        if type(node) == int:
            node = BSTNode(node)
        # If the input is an int, create a BSTNode with that int as the value.
        if node.data in self.contents:
            return
        # If the tree is empty (root == None), set the root equal to the new node.
        if self.root == None:
            self.root = node
            self.contents.append(node.data)
            return

        self.add_node(self.root, node)
    # The node must be added in the correct spot on the tree.
    # Use a helper function, add_node(), to do this.

    def add_node(self, current, new):
        # new node larger, go right
        if new.data > current.data:
            if current.right == None:
                current.right = new
                self.contents.append(new.data)
                return
            # recursively calling the function to compare the new data to the right branch
            else:
                self.add_node(current.right, new)
        # new node smaller, go left
        else:
            if current.left == None:
                current.left = new
                self.contents.append(new.data)
                return
            else:
                self.add_node(current.left, new)


# test part 2
bst = BST()
print(bst)

bst.root = node2
print(bst)

node2.right = node3
print(bst)

# test functionality
# create tree from image
node8 = BSTNode(8)
node3 = BSTNode(3)
node10 = BSTNode(10)
node1 = BSTNode(1)
node6 = BSTNode(6)
node14 = BSTNode(14)
node4 = BSTNode(4)
node7 = BSTNode(7)
node13 = BSTNode(13)

bst = BST()
bst.add(node8)
bst.add(node3)
bst.add(node10)
bst.add(node1)
bst.add(node6)
bst.add(node14)
bst.add(node4)
bst.add(node7)
bst.add(node13)
print(bst)

# # Part 3: Add functionality to your BST class
# def add(self,node):
#     #data wrong type
#     if type(node) != int and type(node) != BSTNode:
#         raise ValueError("You must pass an int or a BSTNode")

#     #data int, make new BSTNode
#     if type(node) == int:
#      node = BSTNode(node)

#     #node already in tree
#     if node.data in self.contents:
#      return

#     #tree empty
#     if self.root == None:
#         self.root = node
#         self.contents.append(node.data)
#         return

#     #call new (recursive) function; don't need to check other conditions again
#     self.add_node(self.root, node)

# def add_node(self, cur_node, new_node):
#     # New node bigger - go right
#     if new_node.data > cur_node.data:
#         if cur_node.right == None:
#             cur_node.right = new_node
#             self.contents.append(new_node.data)
#             return
#         else:
#         #recurse/traverse
#             self.add_node(cur_node.right, new_node)
#     else: #new node smaller, go left
#         if cur_node.left == None:
#             cur_node.left = new_node
#             self.contents.append(new_node.data)
#             return
#         else:
#         #recurse/traverse
#             self.add_node(cur_node.left, new_node)
