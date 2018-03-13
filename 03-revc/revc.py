# Complementing a Strand of DNA

# Sample Dataset
# AAAACCCGGT
# Sample Output
# ACCGGGTTTT

def reverse_complement(dna_string):
  complementary = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
  complement = ""
  for nucleotide in dna_string:
    complement += complementary[nucleotide]

  return complement[::-1]
