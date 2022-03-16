def camelCase(string):
    x = string.split(' ')
    x = [i.lower() for i in x]
    for i in range(1,len(x)):
        x[i] = x[i][0].upper() + x[i][1:]
    return ''.join(x)

