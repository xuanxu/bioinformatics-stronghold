# Rabbits and Recurrence Relations

# Sample Dataset
# 5 3
# Sample Output
# 19

# test_data = [31, 2]

def fib_rabbits(n, k):
  if n < 3:
    return 1
  else:
    return fib_rabbits(n-1, k) + fib_rabbits(n-2, k) * k
