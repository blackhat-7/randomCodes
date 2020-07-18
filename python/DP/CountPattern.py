
def countPattern(string, pattern, strLen, patLen, lookup, strIndex=0, patIndex=0):
    if patIndex == patLen + 1:
        return 1
    elif strIndex == strLen + 1:
        return 0
    
    key = (strIndex, patIndex)
    if key not in lookup:
        include = 0
        if pattern[patIndex] == string[strIndex]:
            include = countPattern(string, pattern, strLen, patLen, lookup, strIndex + 1, patIndex + 1)
        exclude = countPattern(string, pattern, strLen, patLen, lookup, strIndex + 1, patIndex)
        lookup[key] = include + exclude
    
    return lookup[key]


string = "subsequence"   # Input String
pattern = "sue"		   # Pattern

lookup = dict()
print(countPattern(string, pattern, len(string) - 1, len(pattern) - 1, lookup))