
def longestPalindromic(string, i, j, lookup):
    if i > j:
        return 0
    elif i == j:
        return 1
    key = (i, j)
    if key not in lookup:
        if string[i] == string[j]:
            lookup[key] = longestPalindromic(string, i+1, j-1, lookup) + 2
        else:
            lookup[key] = max(longestPalindromic(string, i+1, j, lookup), longestPalindromic(string, i, j-1, lookup))
    return lookup[key]

def main():
    string = input()
    length = len(string)
    lookup = dict()
    print(longestPalindromic(string, 0, length-1, lookup))
main()

