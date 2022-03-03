prices=[7,1,5,3,6,4]
m = 0
st = prices[-1]
for i in range(len(prices) - 2, -1, -1):
    if st < prices[i]:
        m = max(st - prices[i + 1], m)
        st = prices[i]
    else:
        m = max(m, st - prices[i])
print(m)