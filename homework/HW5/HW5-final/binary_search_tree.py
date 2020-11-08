import sys
sys.setrecursionlimit(10**3) 

class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = None
        self.right = None
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
        if self._root is None:
            self._root = BSTNode(key, val)
            self._root.size +=1
        elif key < node.key:
            if(node.left):
                self._put(node.left, key, val)
                node.left.size +=1
            else:
                node.left = BSTNode(key, val)
                node.left.size +=1
        elif (key > node.key):
            if(node.right):
                self._put(node.right, key, val)
                node.right.size +=1
            else:
                node.right = BSTNode(key, val)
                node.right.size +=1
        
        return self._root


    def _get(self, node, key):
        pass # TODO

    @staticmethod
    def _size(node):
        return node.size if node else 0
