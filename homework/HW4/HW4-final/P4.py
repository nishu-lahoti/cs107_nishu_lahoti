class AutoDiffToy:

    # Initializing with value for x
    def __init__(self, value, der = 1):
        self.val = value
        self.der = der

    # Forward add with object and exception handling
    def __add__(self, other):
        try:
            new_val = self.val + other.val
            der_val = self.der
        except AttributeError:
            new_val = self.val + other
            der_val = self.der
        return AutoDiffToy(new_val, der_val)
        
    # Multiplication function
    def __mul__(self, other):
        try:
            new_val = self.val * other.val
            der_val = self.der * other.val
        except AttributeError:
            new_val = self.val * other
            der_val = self.der * other
        return AutoDiffToy(new_val, der_val)

    # Reverse add by calling __add__
    def __radd__(self, other):
        return self.__add__(other)

    # Reverse multiply by calling __mul__
    def __rmul__(self, other):
        return self.__mul__(other)

# Demo

a = 2 # Value to evaluate at
x = AutoDiffToy(a)

alpha = 2.0
beta = 3.0

f = alpha * x + beta
print(f.val, f.der)
f = x * alpha + beta
print(f.val, f.der)
f = beta + alpha * x
print(f.val, f.der)
f = beta + x * alpha
print(f.val, f.der)
