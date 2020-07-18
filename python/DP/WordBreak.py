def wordBreak(wordDoct, string, lookup, i=0):
    if i > len(string) - 1:
        return False
    
    key = i
    if key not in lookup:
        exists = False
        for word in wordDict:
            if string[i:].startswith(word):
                if len(word) == len(string) - i:
                    return True
                else:
                    exists = wordBreak(wordDict, string, lookup, i + len(word))
                    if exists:
                        break

        lookup[key] = exists
    
    return lookup[key]


wordDict = ("this", "th", "is", "famous", "Word", "break", "b", "r", "e", "a", "k", "br", "bre", "brea", "ak", "problem");
string = "Wordbreakproblem"
lookup = dict()
print(wordBreak(wordDict, string, lookup))
# print(lookup)
# for i in lookup:
#     print(string[i])