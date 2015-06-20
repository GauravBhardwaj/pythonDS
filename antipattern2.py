__author__ = 'gbhardwaj'

def tokenize(token):
    #or token in string.
        yield token.split(' ')
    #return "statement removed"

print tokenize("Guarva is").next()
for t in tokenize("This sentence has five tokens."):
    print t
