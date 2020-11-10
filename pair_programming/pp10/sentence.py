# Coder, Sharer, Listener: Nishu Lahoti, Ninon Becquart, Matthew Quesada

class Sentence: # An iterable
    def __init__(self, text): 
        self.text = text
        self.words = text.split()

    def __iter__(self):
        for word in self.words:
            yield word

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

# Demo
my_sentence = "Hello, I am doing pair programming."
sentence = Sentence(my_sentence)

for i in sentence:
    print (i)
