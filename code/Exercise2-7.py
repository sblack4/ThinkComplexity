import string

def infinite_alphanumeric_generator(): 
    i = 1
    while True:
        for c in string.lowercase:
            yield c+str(i)
        i += 1


if __name__ == '__main__':
    iter = infinite_alphanumeric_generator()
    for i in range(0,100):
        print iter.next()