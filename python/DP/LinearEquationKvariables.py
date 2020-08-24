
def solve(coeff, rhs, lookup, n, i=0):
    if rhs < 0 or i > n:
        return 0
    elif rhs == 0:
        return 1
    key = (i, rhs)
    if key not in lookup:
        include = solve(coeff, rhs - coeff[i], lookup, n, i)
        exclude = solve(coeff, rhs, lookup, n, i + 1)
        lookup[key] = include + exclude

    return lookup[key]





coeff = [1, 2, 3]
n = len(coeff)
rhs = 4
lookup = dict()

print(solve(coeff, rhs, lookup, n-1, 0))