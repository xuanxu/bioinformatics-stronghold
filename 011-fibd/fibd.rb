# Mortal Fibonacci Rabbits

# Sample Dataset
# 6 3
# Sample Output
# 4

def fibd_rabbits(n, m)
  fibd = [1, 1]
  (3..n).each do |i|
    if i == m + 1
      fibd.append(fibd[-1] + fibd[-2] - 1)
    elsif i > m + 1
      fibd.append(fibd[-1] + fibd[-2] - fibd[-(m+1)])
    else
      fibd.append(fibd[-1] + fibd[-2])
    end
  end

  return fibd[-1]
end