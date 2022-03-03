def isValid(s: str) -> bool:
    d = {'{': '}', '(': ')', '[': ']'}
    st = []
    for i in s:
        if i in '{[(':
            st.append(i)

        else:
            if st:
                top = st.pop()
                if d[top] != i:
                    return False

            else:
                return False
    if not st:
        return True
    return False
s='(()})'
print(isValid(s))