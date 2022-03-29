from itertools import permutations


def findevendigits(digits):
    arr = []
    p = set(permutations(digits, 3))
    for i in p:
        if i[0] != 0 and i[-1] % 2 == 0:
            temp = ''
            for ii in i:
                temp += str(ii)
            arr.append(int(temp))
    arr.sort()
    return arr
print(findevendigits([1,2,0,3]))