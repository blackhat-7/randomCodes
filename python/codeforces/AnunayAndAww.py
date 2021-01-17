n = int(input())
s = input()
count = 0
for i in range(n-2):
    if s[i] == 'a' and s[i+1] == 'w' and s[i+2] == 'w':
        count += 1

print(count)
