def checkVowel(i) :
    v = ["a","e","i","o","u"]
    if i.lower() in v:
        return True
    else :
        return False
        
s1 = input()
s2 = input()
s3 = input()

c1=5
c2=7
c3=5

for i in s1:
    if checkVowel(i):
        c1 -= 1
for i in s2:
    if checkVowel(i):
        c2 -= 
for i in s3:
    if checkVowel(i):
        c3 -= 1
if c1==c2==c3==0 :
    print("YES")
else:
    print("NO")