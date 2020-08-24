def leapYear(year):
    return year%400 == 0 or (year%4==0 and year%100!=0)

t = int(input())
for i in range(t):
    m1, y1 = map(int, input().split())
    m2, y2 = map(int, input().split())
    count = 0
    if m1 > 2:
        y1 += 1
    if m2 < 2:
        y2 -= 1
    if y2 <= 2020:
        intersect = 0
        
        for j in range(2020, -1, -1):
            if (intersect == 0 or (intersect == 6 and not leapYear(j))):
                count += 1
                print(j, intersect)
            if leapYear(j-1):
                intersect = (intersect+1)%7
            intersect = (intersect+1)%7

        # for j in range(2020, 1000010):
        #     if (intersect == 0 or (intersect == 6 and not leapYear(j))):
        #         count += 1
        #         print(j, intersect)
        #     if leapYear(j-1):
        #         intersect = (intersect-1)%7
        #     intersect = (intersect-1)%7
        
    else:
        count = 0
    print(count)

