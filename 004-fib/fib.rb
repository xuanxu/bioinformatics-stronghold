# Rabbits and Recurrence Relations

# Sample Dataset
# 5 3
# Sample Output
# 19

def fib_rabbits(n, k)
  return 1 if n < 3
  fib_rabbits(n-1, k) + fib_rabbits(n-2, k) * k
end
