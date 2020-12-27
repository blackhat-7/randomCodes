def jaccard_similarity(s1, s2):
    if len(s1) > len(s2):
        bigger, smaller = set(s1), set(s2)
    else:
        bigger, smaller = set(s2), set(s1)
    intersection = sum([1 for item in smaller if item in bigger])
    union = len(bigger) + len(smaller) - intersection
    return intersection / union


def jacard_distance(s1, s2):
    return 1 - jaccard_similarity(s1, s2)


s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8, 9, 10}

print(jaccard_similarity(s1, s2))
print(jacard_distance(s1, s2))
