# Mortal Fibonacci Rabbits

# Sample Dataset
# 6 3
# Sample Output
# 4

def fibd_rabbits(n, m):
  fibd = [1, 1]
  for i in range(3, n+1):
    if i == m + 1:
      fibd.append(fibd[-1] + fibd[-2] -1)
    elif i > m + 1:
      fibd.append(fibd[-1] + fibd[-2] - fibd[-(m+1)])
    else:
      fibd.append(fibd[-1] + fibd[-2])

  return fibd[-1]
