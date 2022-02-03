
def countergame(n):
    n = bin(n)[2:]
    print(n)
    n = n.split('1')
    print(n)
    turns = len(n)+len(n[-1])-2
    return 'Louise' if turns&1 else 'Richard'
print(countergame(132))