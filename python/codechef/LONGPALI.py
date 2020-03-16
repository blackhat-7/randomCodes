n = int(input())
s = input()

max = 1
word = s[0]

for i in range(len(s)-1):
    t = i + max + 1
    for j in range(t, len(s)+1):
        if (s[i:i+(j-i)//2] == s[i+(j-i)//2+((j-i)%2):j][::-1]) and (j-i > max):
            max = j - i
            word = s[i:j]

print(str(max)+"\n"+word)
    
