def count1(num):
    return bin(num).count('1')%2

def xor(set, evod, visited):
    n = len(set)
    for i in range(n-1):
        a = set[i]^set[n-1]
        if not visited[a]:
            set.append(a)
            visited[a] = True
            if count1(a)==0:
                evod[0] += 1
            else:
                evod[1] += 1
        
        

t = int(input())
for i in range(t):
    q = int(input())
    set = []
    visited = [False]*100000000
    evod = [0, 0]
    for j in range(q):
        x = int(input())
        if not visited[x]:
            set.append(x)
            visited[x] = True
            if count1(x)==0:
                evod[0] += 1
            else:
                evod[1] += 1
            xor(set, evod, visited)
        print(evod[0], evod[1])