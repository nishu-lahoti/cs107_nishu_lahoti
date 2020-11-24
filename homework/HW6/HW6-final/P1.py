from enum import Enum

class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node: 
            return BSTNode(key, val)
        if   key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if   key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    # Creating a findMin function to return the lowest value in the BST
    def findMin(self, node):
        if node is None:
            print("No nodes to delete.")
        if node.left is not None:
            node.left = self.findMin(node.left)
            return node.left
        else:
            return node

    # Creating _removemin function
    def _removemin(self, node):
        if node is None:
            print("No nodes to delete.")
        
        # If left node exists, find its minimum and reduce size by 1
        elif node.left is not None:
            node.size -=1
            node.left = self._removemin(node.left)
            return node

        # Else the minimum will be from the root to the right.
        elif node.right is not None:
            return node.right        

    def remove(self, key):
        self._root = self._remove(self._root, key)
    
    def _remove(self, node, key): # Partial Solution
        
        # Raise key error if no node exists
        if node is None: 
            raise KeyError(f'key not found: {key}')
        
        # Recursively remove the left node
        elif key < node.key:
            node.left = self._remove(node.left, key)
        
        # Recursively remove the right node
        elif key > node.key:
            node.right = self._remove(node.right, key)

        # Logic for replacing the root if the right / left don't exist
        else:
            if node.left is None:
                return node.right
            
            elif node.right is None:
                return node.left
            
            # Utilizing both findMin and _removemin functions
            succ = self.findMin(node.right)
            succ.right = self._removemin(node.right)
            succ.left = node.left

            return succ
        
        node.size = 1 + self._size(node.left) + self._size(node.right) # Might need to change this to -1 to lessen the size
        return node 

    @staticmethod
    def _size(node):
        return node.size if node else 0


class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal():
    
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        
        # Set an index, pass tree, create empty nodes list
        self.index = 0
        self.tree = tree
        self.nodes_list = []

        # Traverse based on enumerator type
        if traversalType == DFSTraversalTypes.PREORDER:
            traverse = self.preorder(tree)
        if traversalType == DFSTraversalTypes.INORDER:
            traverse = self.inorder(tree)
        if traversalType == DFSTraversalTypes.POSTORDER:
            traverse = self.postorder(tree)

    def __iter__(self):
        return self

    def __next__(self): 

        # Create a node object based on each new list item
        try:
            node = self.nodes_list[self.index]
        except IndexError:
            raise StopIteration()

        # Increment index before next call
        self.index += 1
        return node

    def inorder(self, bst:BSTTable):

        # Set starting node
        node_start = bst._root

        def traversal(node):
            if node:

                # Create a node to eventually iterate on
                new_node = BSTNode(node.key, node.val)

                # First go left, then go root, then go right
                traversal(node.left)
                self.nodes_list.append(new_node)
                traversal(node.right)

            else:
                pass

        traversal(node_start)
    
    def preorder(self, bst:BSTTable):
        
        # Set starting node
        node_start = bst._root
    
        def traversal_pre(node):

            if node:
                # Create a node to eventually iterate on
                new_node = BSTNode(node.key, node.val)

                # First go root, then go left, then go right
                self.nodes_list.append(new_node)
                traversal_pre(node.left)
                traversal_pre(node.right)
            else:
                pass
        
        traversal_pre(node_start)

    def postorder(self, bst:BSTTable):
        
        # Set starting node
        node_start = bst._root

        def traversal_post(node):

            if node:
                # Create a node to eventually iterate on
                new_node = BSTNode(node.key, node.val)

                # First go root, then go left, then go right
                traversal_post(node.left)
                traversal_post(node.right)
                self.nodes_list.append(new_node)
            else:
                pass
        
        traversal_post(node_start)