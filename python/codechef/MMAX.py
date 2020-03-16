t = int(input())
for i in range(t):
    n = int(input())
    k = int(input())
    num1 = 0
    num2 = 0
    if (n>2):
        if (n>=k):
            num1 = k
            num2 = n-num1

        else:
            num1 = k%n
            num2 = n-num1
        if num1==num2 :
            sum2 = 2*num1 - 1
        else :
            sum2 = 2 * min(num1, num2)
        print(sum2)
    
    else:
        print(k%2)
