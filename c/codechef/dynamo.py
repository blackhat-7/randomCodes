import sys

t = int(input())

for i in range(t):
    n = int(input())
    a = int(input())
    s = 2*pow(10, n) + a
    print(s, flush=True)
    b = int(input())
    c = pow(10, n) - b
    print(c, flush=True)
    d = int(input())
    e = pow(10, n)-d
    print(e, flush=True)
    verdict = int(input())
    if verdict == -1:
        sys.exit(0)
