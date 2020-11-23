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

    def findMin(self, node):
        if node is None:
            print("No nodes to delete.")
        if node.left is not None:
            node.left = self.findMin(node.left)
            return node.left
        else:
            return node

    def _removemin(self, node):
        if node is None:
            print("No nodes to delete.")
        
        elif node.left is not None:
            node.size -=1
            node.left = self._removemin(node.left)
            return node

        elif node.right is not None:
            return node.right        


    def remove(self, key):
        self._root = self._remove(self._root, key)
    
    def _remove(self, node, key): # Partial Solution
        if node is None: 
            raise KeyError(f'key not found: {key}')
        
        elif key < node.key:
            node.left = self._remove(node.left, key)
        
        elif key > node.key:
            node.right = self._remove(node.right, key)

        else:
            if node.left is None:
                return node.right
            
            elif node.right is None:
                return node.left
            
            succ = self.findMin(node.right)
            succ.right = self._removemin(node.right)
            succ.left = node.left

            return succ
        
        node.size = 1 + self._size(node.left) + self._size(node.right) # Find a way to percolate down tree
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
        self.index = 0
        self.tree = tree
        self.nodes_list = []

        if traversalType == DFSTraversalTypes.PREORDER or 1:
            self.preorder(tree)
        if traversalType == DFSTraversalTypes.INORDER or 2:
            self.inorder(tree)
        if traversalType == DFSTraversalTypes.POSTORDER or 3:
            self.postorder(tree)

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

    def preorder(self, bst:BSTTable):

        if not self.tree._root:
            return("Root does not exist")     

        # First print the root note
        print(self.tree._root)

        # Then go to left child
        self.preorder(self.tree._root.left)

        # Then go to right child
        self.prorder(self.tree._root.right)

    def inorder(self, bst:BSTTable):

        def _traversal(self, node = bst._root):

            # Return user if the root node does not exist
            if not self.node.root:
                return("Root does not exist")  
            
            # Traverse to the left node
            if node.left is not None:
                self._traversal(node.left)

            # Append the root to the node list
            self.nodes_list.append(node.root)

            # Traverse to the right node         
            if node.right is not None:
                self._traversal(node.right)
        
        return _traversal

    def postorder(self, bst:BSTTable):
        
        if not self.tree._root:
            return("Root does not exist") 
            
        # First go to left child
        self.postorder(self.tree._root.left)

        # Then go to right
        self.postorder(self.tree._root.right)

        # Then print at root
        print(self.tree._root)