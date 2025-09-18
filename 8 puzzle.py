from collections import deque
goal="123456780"
def solve(start="123456708"):
    q=deque([(start,"")]); seen={start}
    while q:
        s,p=q.popleft()
        if s==goal:return p
        i=s.index("0")
        for d,m in [(1,"R"),(-1,"L"),(3,"D"),(-3,"U")]:
            j=i+d
            if 0<=j<9 and not(i%3==2 and d==1 or i%3==0 and d==-1):
                ns=list(s);ns[i],ns[j]=ns[j],ns[i];ns="".join(ns)
                if ns not in seen:seen|={ns};q.append((ns,p+m))
print("Moves:",solve("123456708"))

