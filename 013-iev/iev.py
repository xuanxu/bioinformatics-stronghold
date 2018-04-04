# Calculating Expected Offspring

# Sample Dataset
# 1 0 0 1 0 1

# Sample Output
# 3.5

def next_gen_dominant_phenotype(n1, n2, n3, n4, n5, n6, offspring_per_couple):
  p1 = n1 * prob_dominant_offspring('AA-AA')
  p2 = n2 * prob_dominant_offspring('AA-Aa')
  p3 = n3 * prob_dominant_offspring('AA-aa')
  p4 = n4 * prob_dominant_offspring('Aa-Aa')
  p5 = n5 * prob_dominant_offspring('Aa-aa')
  p6 = n6 * prob_dominant_offspring('aa-aa')

  return (p1 + p2 + p3 + p4 + p5 + p6) * offspring_per_couple

def prob_dominant_offspring(genotype_couple):
  if genotype_couple == 'AA-AA':
    return 1
  elif genotype_couple == 'AA-Aa':
    return 1
  elif genotype_couple == 'AA-aa':
    return 1
  elif genotype_couple == 'Aa-Aa':
    return 0.75
  elif genotype_couple == 'Aa-aa':
    return 0.5
  else:
    return 0


# print(next_gen_dominant_phenotype(1, 0, 0, 1, 0, 1, 2))