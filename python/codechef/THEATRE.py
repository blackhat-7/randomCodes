def main():
    t = int(input())
    final_profit = 0

    for i in range(t):
        n = int(input())
        mat = [[0]*4 for j in range(4)]
        c = 0
        for j in range(n):
            m, t = input().split()
            if m == 'A':
                c = 0
            elif m == 'B':
                c = 1
            elif m == 'C':
                c = 2
            else:
                c = 3
            t = int(t)//3-1
            mat[c][t] += 1

        temp = []

        temp.append([mat[0][0], mat[1][1], mat[2][2], mat[3][3]])
        temp.append([mat[0][0], mat[1][1], mat[2][3], mat[3][2]])
        temp.append([mat[0][0], mat[1][2], mat[2][1], mat[3][3]])
        temp.append([mat[0][0], mat[1][2], mat[2][3], mat[3][1]])
        temp.append([mat[0][0], mat[1][3], mat[2][1], mat[3][2]])
        temp.append([mat[0][0], mat[1][3], mat[2][2], mat[3][1]])
        temp.append([mat[0][1], mat[1][0], mat[2][2], mat[3][3]])
        temp.append([mat[0][1], mat[1][0], mat[2][3], mat[3][2]])
        temp.append([mat[0][1], mat[1][2], mat[2][0], mat[3][3]])
        temp.append([mat[0][1], mat[1][2], mat[2][3], mat[3][0]])
        temp.append([mat[0][1], mat[1][3], mat[2][0], mat[3][2]])
        temp.append([mat[0][1], mat[1][3], mat[2][2], mat[3][0]])
        temp.append([mat[0][2], mat[1][0], mat[2][1], mat[3][3]])
        temp.append([mat[0][2], mat[1][0], mat[2][3], mat[3][1]])
        temp.append([mat[0][2], mat[1][1], mat[2][0], mat[3][3]])
        temp.append([mat[0][2], mat[1][1], mat[2][3], mat[3][0]])
        temp.append([mat[0][2], mat[1][3], mat[2][0], mat[3][1]])
        temp.append([mat[0][2], mat[1][3], mat[2][1], mat[3][0]])
        temp.append([mat[0][3], mat[1][0], mat[2][1], mat[3][2]])
        temp.append([mat[0][3], mat[1][0], mat[2][2], mat[3][1]])
        temp.append([mat[0][3], mat[1][1], mat[2][0], mat[3][2]])
        temp.append([mat[0][3], mat[1][1], mat[2][2], mat[3][0]])
        temp.append([mat[0][3], mat[1][2], mat[2][0], mat[3][1]])
        temp.append([mat[0][3], mat[1][2], mat[2][1], mat[3][0]])

        max_profit = -400
        for l in range(len(temp)):
            k = 100
            profit = 0
            temp[l].sort(reverse = True)
            for j in range(4):
                if temp[l][j] != 0:
                    profit += temp[l][j]*k
                    k -= 25
                else:
                    profit -= 100
            if profit > max_profit:
                max_profit = profit
        print(max_profit)
        final_profit += max_profit
    print(final_profit)

    
main()

# 1
# 32
# A 3
# B 6
# C 9
# D 12
# A 3
# B 6
# C 9
# D 12
# A 3
# B 6
# C 9
# D 12
# A 3
# B 6
# C 9
# D 12
# A 3
# B 6
# C 9
# A 12
# B 3
# C 6
# D 9
# A 12
# B 3
# C 6
# D 9
# A 12
# C 3
# D 6
# A 9
# B 12
