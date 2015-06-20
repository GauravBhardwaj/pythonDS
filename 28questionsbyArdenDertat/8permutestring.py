result = list()
def generate(string, start, end):
    current = 0
    if start == end-1:
        #if not string in result:
        result.append(string)
    else:
        for current in range (start, end):
            x = list(string)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp
            generate(''.join(x), start+1, end)
            #temp = x[start]
            #x[start] = x[current]
            #x[current] = temp

string = "xyz"
length = len(string)
generate(string, 0, length)
print result
