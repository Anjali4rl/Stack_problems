from queue import LifoQueue

t = int(input())
for j in range(t):

    n = int(input())
    s = LifoQueue(maxsize=n)
    l = list(map(int, input().split()))
    p = []
    for i in range(n - 1, -1, -1):

        if s.empty():
            p.append(-1)
        elif s.qsize() > 0 and s.queue[-1] > l[i]:
            p.append(s.queue[-1])
        elif s.qsize() > 0 and s.queue[-1] <= l[i]:
            while (s.qsize() and s.queue[-1] <= l[i]):
                s.get()
            if s.qsize() == 0:
                p.append(-1)
            else:

                p.append(s.queue[-1])
        s.put(l[i])
    p = p[::-1]
    print(*p)