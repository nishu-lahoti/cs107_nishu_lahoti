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

    def _removemin(self, node):
        if node is None:
            print("No nodes to delete.")
        
        elif node.left is not None:
            node.size -=1
            node.left = self._removemin(node.left)
            return node

        elif node.right is not None:
            return node.right        
            
        else:
            return None

    def remove(self, key):
        self._root = self._remove(self._root, key)
    
    def _remove(self, node, key): # Partial Solution
        if node is None: 
            raise KeyError(f'key not found: {key}')
        
        elif key < node.key:
            node.size -=1
            node.left = self._remove(node.left, key)
        
        elif key > node.key:
            node.size -=1
            node.right = self._remove(node.right, key)

        else:
            if node.left is None:
                succ = node.right
                node = None
                return succ
            
            elif node.right is None:
                succ = node.left
                node = None
                return succ

        succ = self._removemin(node.right)

        node.key = succ.key
    
        return node

    @staticmethod
    def _size(node):
        return node.size if node else 0