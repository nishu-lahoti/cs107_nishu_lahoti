class LinkedList:

    def __init__(self, head, tail):
        assert isinstance(tail, LinkedList) or isinstance(tail, Nil), TypeError(
            'tail should either be a LinkedList or a Nil')
        self._head, self._tail = head, tail

    @property
    def head(self):
        return self._head
    
    @property
    def tail(self):
        return self._tail

    def __str__(self):
        return str(self._head) + ' -> ' + str(self._tail)

    def __repr__(self):
        return f'LinkedList({repr(self._head)}, {repr(self._tail)})'

    def __len__(self):
        return 1 + len(self._tail)

    def __getitem__(self, i):
        return self._head if i == 0 else self._tail[i-1]
    
    def prepend(self, val): 
        return LinkedList(val, self)

    # Added append method through a recursive call to LinkedList.
    # Passed head and tail values.
    def append(self, val): 
        return LinkedList(self._head, self._tail.append(val))

    def summation(self):
        return self._head + self._tail.summation() if self._tail else self._head

    def minimum(self):
        def smaller(a, b):
            return a if a < b else b
        return smaller(self._head, self._tail.minimum()) if self._tail else self._head

    # Implemeneed for_each method through a recursive LinkedList call.
    # Returning LinkedList with the function applied to head, tail combo.
    # Passing function into for_each function attached to tail.
    def for_each(self, fun):
        return LinkedList(fun(self._head), self._tail.for_each(fun))

    # Implemented reduce right function by applying function to head, tail combo.
    # Passed function into recursive call on the tail.
    def reduce_right(self, fun):
        return fun(self._head, self._tail.reduce_right(fun)) if self._tail else self._head


class Nil():

    def __str__(self):
        return 'Nil'

    def __repr__(self):
        return 'Nil()'

    def __len__(self):
        return 0

    def __getitem__(self, i):
        raise IndexError('index out of range')

    def __bool__(self):
        return False

    def prepend(self, val): # Implemented prepend for Nil
        return LinkedList(val, Nil())

    def append(self, val): # Implemented append for Nil
        return LinkedList(val, Nil())

    def for_each(self, fun):
        return Nil()
