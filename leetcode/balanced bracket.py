def balance(s):
    d = {'{': '}', '(': ')', '[': ']'}
    st = []
    for i in s:
        if i in '{[(':
            st.append(d[i])

        else:
            if st:
                top = st.pop()
                if top != i:
                    return 'false'

            else:
                return 'false'
    if st:
        return 'false'
    return 'true'
print(balance('(]'))