# Calculating Protein Mass

# Sample Dataset
# SKADYEK

# Sample Output
# 821.392

def monoisotopic_mass(amino):
  masses_table = { 'A':  71.03711,
                   'C': 103.00919,
                   'D': 115.02694,
                   'E': 129.04259,
                   'F': 147.06841,
                   'G': 57.02146,
                   'H': 137.05891,
                   'I': 113.08406,
                   'K': 128.09496,
                   'L': 113.08406,
                   'M': 131.04049,
                   'N': 114.04293,
                   'P': 97.05276,
                   'Q': 128.05858,
                   'R': 156.10111,
                   'S': 87.03203,
                   'T': 101.04768,
                   'V': 99.06841,
                   'W': 186.07931,
                   'Y': 163.06333 }
  return masses_table[amino]


def protein_weight(protein):
  weight = 0.0
  for amino in protein:
    weight += monoisotopic_mass(amino)

  return round(weight, 3)
