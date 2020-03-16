s = "abpplel"
t = "abppall"

def match(i, j):
    return s[i]==t[j]

def LCS(s, t):
    sub_string = ""
    m = len(s)
    n = len(t)
    L = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            L[i][j] = max(L[i-1][j], L[i][j-1], L[i-1][j-1]+match(i, j))
    
    i = m-1; j = n-1
    while i>0 and j>0:
        if L[i][j] == L[i-1][j-1] + match(i, j) and match(i, j) == 1:
            sub_string = s[i] + sub_string
            i -= 1; j -= 1
        elif L[i][j] == L[i-1][j]:
            i -= 1
        else:
            j -= 1
    return sub_string

def main():
    print(LCS(s, t))

main()

        
