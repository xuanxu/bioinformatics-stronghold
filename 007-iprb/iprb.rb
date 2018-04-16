# Mendel's First Law

# Sample Dataset
# 2 2 2

# Sample Output
# 0.78333

def dominant_allele_probability(k, m, n)
  total = (k + m + n).to_f
  k1 = k/total
  m1 = m/total
  n1 = n/total
  k2 = k/(total-1)
  m2 = m/(total-1)
  n2 = n/(total-1)
  mn1 = (m + n)/(total)
  mn2 = (m + n)/(total-1)
  m1_m2 = (m-1)/(total-1)
  k1_k2 = (k-1)/(total-1)

  (k1 * mn2) + (mn1 * k2) + (k1 * k1_k2) + (0.75 * m1 * m1_m2) + (0.5 * m1 * n2) + (0.5 * n1 * m2)
end
