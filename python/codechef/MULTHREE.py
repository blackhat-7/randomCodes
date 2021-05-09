def get_next(n):
  if n == 2:
    return 4
  if n == 4:
    return 8
  if n == 8:
    return 6
  return 2


def solve(k, d0, d1):
  res = d0+d1
  cur_s = d0 + d1
  cur_d = 0
  repeat = [2, 4, 8, 6]
  j = 0

  while j < k-2 and cur_d not in repeat:
    cur_d = cur_s % 10
    res += cur_d
    cur_s += cur_d
    j += 1

  for i in range(4):
    if j >= k-2:
      break
    cur_d = get_next(cur_d)
    res += (1 + (k-j-2)//4) * cur_d
    j += 1
  print(res)
  if res % 3 == 0:
    print("YES")
  else:
    print("NO")


t = int(input())
for q in range(t):
  k, d0, d1 = map(int, input().split())
  solve(k, d0, d1)

