import heapq


def cookies(k, A):
    # Write your code here
    c = 0
    heapq.heapify(A)
    while True:
        t1 = heapq.heappop(A)
        if t1 >= k:
            return c

        if A:
            t2 = heapq.heappop(A)
            heapq.heappush(A, t1 + (2 * t2))
            c += 1
        else:
            return -1
print(cookies(7,[1, 2, 3, 9, 10, 12]))