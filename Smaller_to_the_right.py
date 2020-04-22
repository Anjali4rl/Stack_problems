from queue import LifoQueue
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=LifoQueue(maxsize=n)
    p=[]
    for j in range((len(l)-1),-1,-1):
        if s.empty():
            p.append(-1)
        elif s.qsize()>0 and s.queue[-1]<l[j]:
            p.append(s.queue[-1])
        elif s.qsize()>0 and s.queue[-1]>=l[j]:
            while(s.qsize()>0 and s.queue[-1]>=l[j]):
                s.get()
            if s.empty():
                p.append(-1)
            else:
                p.append(s.queue[-1])
        s.put(l[j])
    p=p[::-1]
    print(*p)