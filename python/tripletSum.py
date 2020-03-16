def main():
    x = int(input())
    lst = list(map(int, input().split()))
    recursiveTripletSum(lst, [], 0, x, 0)


def recursiveTripletSum(lst, temp, s, x, c):
    if s > x:
        return
    if len(temp) == 3:
        if s == x:
            print(temp)
            return
        else:
            return
    for i in range(c, len(lst)):
        recursiveTripletSum(lst, temp + [lst[i]], s+lst[i], x, i+1)


main()
