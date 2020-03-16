t = int(input())

for i in range(t):
    s = input()
    if (s.count('1')%2==0):
        print("LOSE")
    else:
        print("WIN")