def get_fact(no):
    if (no // 5):
        f = no // 5 + get_fact(no // 5)

    else:
        return no // 5
    return f




def trailingZeroes(n: int) -> int:
    return get_fact(n)
print(trailingZeroes(5))