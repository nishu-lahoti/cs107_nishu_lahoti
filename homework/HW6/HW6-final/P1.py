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
        self.depth_type = traversalType
        self.tree = tree
        print(self.tree)

    def __iter__(self):
        while self.index < len(self.tree):
            return self

    def __next__(self): # Uncertain how to create the iterator which can access a tree's node
            try:
                iter()
            except IndexError:
                raise StopIteration()

    def inorder(self, bst:BSTTable):
        # TODO: implement
        pass

    def preorder(self, bst:BSTTable):
        # TODO: implement
        pass

    def postorder(self, bst:BSTTable):
        # TODO: implement
        pass