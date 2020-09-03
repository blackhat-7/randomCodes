
def zeroSum(arr, n):
  my_set = set()
  curr_sum = 0
  my_set.add(0)
  for num in arr:
    curr_sum += num
    if curr_sum in my_set:
      return "Yes"
    my_set.add(curr_sum)
  return "No"


t = int(input())
for q in range(t):
  n = int(input())
  arr =list(map(int, input().split()))
  print(zeroSum(arr, n))



'''
2
5
4 2 -3 1 6
5
4 2 0 1 6
'''