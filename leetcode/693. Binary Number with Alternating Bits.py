def alternatingBit(n):
    if n // 2 == 2 ** len(bin(n)[2:]) - 1 - n:
        return True
    return False
print(alternatingBit(5))