
def knapsack(weights, values, capacity, lookup, i):
    if capacity < 0:
        return float('-inf')
    if i < 0 or capacity == 0:
        return 0

    key = (i, weights[i])
    if key not in lookup:
        include = knapsack(weights, values, capacity - weights[i], lookup, i - 1) + values[i]
        exclude = knapsack(weights, values, capacity, lookup, i - 1)
        lookup[key] = max(include, exclude)

    return lookup[key]







# Input: set of items each with a weight and a value
values = [20, 5, 10, 40, 15, 25]
weights = [1, 2, 3, 8, 7, 4]
# Knapsack capacity
capacity = 10

lookup = dict()
print(knapsack(weights, values, capacity, lookup, len(values) - 1))


# for i in range(1, len(values) + 1):
#     weight = weights[i - 1]
#     value = values[i - 1]
#     for j in range(1, capacity + 1):
#         if i == 0 or j == 0:
#             lookup[i][j] = 1 if i == 0 and j == 0 else 0
#         else:
#             if weight > j:
#                 lookup[i][j] = lookup[i - 1][j]
#             else:
#                 lookup[i][j] = max(lookup[i][j], lookup[i - 1][j - weight] + value)

# print(lookup[len(values)][capacity])


'''

  0 1 2 3 4 5 6 7 8 9 10
0 1 0 0 0 0 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0 0 0 0
2 1 1 1 1
3  0 
8 0
7
4

..

'''