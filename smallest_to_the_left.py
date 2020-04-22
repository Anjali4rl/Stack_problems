from queue import LifoQueue
t=int(input())
for i in range(t):
    n=int(input())
    s=LifoQueue(maxsize=n)
    l=list(map(int,input().split()))
    p=[]
    for j in l:
        if s.empty():
            p.append(-1)
        elif s.qsize()>0 and s.queue[-1]<j:
            p.append(s.queue[-1])
        elif s.qsize()>0 and s.queue[-1]>=j:
            while(s.qsize()>0 and s.queue[-1]>=j):
                s.get()
            if s.empty():
                p.append(-1)
            else:
                p.append(s.queue[-1])
        s.put(j)
    print(*p)