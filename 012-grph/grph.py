# Overlap Graphs

# Sample Dataset
# sample_dataset.txt

# Sample Output
# sample_output.txt

import sys
sys.path.insert(0, '../util')
from util import fasta_file_to_dna_strings

def o3_adjacency_list(dna_strings):
  o3 = []
  for name in dna_strings.keys():
    suffix = dna_strings[name][-3:]
    dnas = list(dna_strings.keys())
    dnas.remove(name)

    for other_dna in dnas:
      if dna_strings[other_dna][0:3] == suffix:
        o3.append([name, other_dna])

  return o3


dna_strings = fasta_file_to_dna_strings('rosalind_grph.txt')
o3 = o3_adjacency_list(dna_strings)
with open('rosalind_output', 'w') as output:
  for edge in o3:
    output.write(edge[0] + ' ' + edge[1] + '\n')
