# Mortal Fibonacci Rabbits

# Sample Dataset
# 6 3
# Sample Output
# 4

def fibd_rabbits(n, m):
  if n < 0:
    return 0
  elif n < 3:
    return 1
  else:
    return fibd_rabbits(n-1, m) + fibd_rabbits(n-2, m) - fibd_rabbits(n-1-m, m)
