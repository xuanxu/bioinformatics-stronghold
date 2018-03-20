# Counting Point Mutations

# Sample Dataset
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT

# Sample Output
# 7

def hamming_distance(string1, string2):
  h = 0
  for n in range(0, len(string1)):
    if string1[n] != string2[n]: h += 1

  return h
