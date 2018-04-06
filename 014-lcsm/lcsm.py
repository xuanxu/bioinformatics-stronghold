# Finding a Shared Motif

# Sample Dataset
# >Rosalind_1
# GATTACA
# >Rosalind_2
# TAGACCA
# >Rosalind_3
# ATACA

# Sample Output
# AC

import sys
sys.path.insert(0, '../util')
from util import fasta_file_to_dna_strings

def common_motif(dna_strings):
  longest_motif = ''
  dna = min(dna_strings, key = len)

  for start in range(len(dna)):
    for l in range(1, len(dna) - start):
      motif = dna[start:start+l]
      if len(motif) > len(longest_motif) and all(motif in x for x in dna_strings):
        longest_motif = motif

  return longest_motif

list1 = fasta_file_to_dna_strings('rosalind_lcsm.txt').values()
print(common_motif(list1))