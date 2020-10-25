class AutoDiffToy:

    # Initializing with value for x
    def __init__(self, value):
        self.value = value

    def val(self):
        return self.value

    ### Compute derivative of input value ###

    # Forward add with object and exception handling
    def __add__(self, other):
        try:
            return AutoDiffToy(self.value + other.value)
        except AttributeError:
            return AutoDiffToy(self.value + other)

    # Multiplication function
    def __mul__(self, other):
        try:
            return AutoDiffToy(self.value * other.value)
        except AttributeError:
            return AutoDiffToy(self.value * other)
    
    # Reverse add to allow for different equation patterns
    def __radd__(self, other):
        try:
            return AutoDiffToy(self.value + other.value)
        except AttributeError:
            return (self.value + other)

    # Reverse multiply to allow for different equation patters
    def __rmul__(self, other):
        try:
            return AutoDiffToy(self.value * other.value)
        except AttributeError:
            return AutoDiffToy(self.value * other)


a = 2
x = AutoDiffToy(a)

alpha = 2.0
beta = 3.0
f = alpha * x + beta

# print(f.val, f.der) <--- How can f become an object with .val and .der?
