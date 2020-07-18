
def findTuples(array, sum, i, n, lst, lookup):
    if sum < 0 or i > n or len(lst) == 4:
        return None
    if sum - array[i] == 0 and len(lst) == 3:
        return [tuple(lst + [array[i]])]
    
    key = (sum, i, len(lst))
    if key not in lookup:
        ans = set()
        include = findTuples(array, sum - array[i], i + 1, n, lst + [array[i]], lookup)
        exclude = findTuples(array, sum, i + 1, n, lst, lookup)

        if not include and not exclude:
            ans = None
        else:
            if include:
                for tple in include:
                    ans.add(tple)
            if exclude:
                for tple in exclude:
                    ans.add(tple)
        lookup[key] = ans
    return lookup[key]
    

array = [2, 7, 4, 0, 9, 4, 2, 5, 1, 3]
array.sort()
sum = 20
lookup = dict()
print(findTuples(array, sum, 0, len(array) - 1, [], lookup))