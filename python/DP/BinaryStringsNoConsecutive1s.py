def countStrings(i, n, string, lookup):
    if i == n:
        return 1
    key = (i, string)
    if key not in lookup:
        add1 = 0
        if i == 0 or string[i-1] != '1':
            add1 = countStrings(i + 1, n, string + '1', lookup)
        add0 = countStrings(i + 1, n, string + '0', lookup)
        lookup[key] = add0 + add1
    return lookup[key]




n = int(input())
lookup = dict()
print(countStrings(0, n, "", lookup))