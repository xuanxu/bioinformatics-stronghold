# Finding a Motif in DNA

# Sample Dataset
# GATATATGCATATACTT
# ATAT

# Sample Output
# 2 4 10

def find_motif(dna, motif):
  indexes = []
  start_at = 0
  while True:
    i = dna.find(motif, start_at)
    if i == -1:
      break

    indexes.append(i)
    start_at = i + 1

  # output data should be space separated 1-based numbering indexes:
  return ' '.join(str(x + 1) for x in indexes)
