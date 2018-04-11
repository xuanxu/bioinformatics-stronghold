# Computing GC Content

# Sample Dataset
# sample_dataset.txt

# Sample Output
# Rosalind_0808
# 60.919540

import sys
sys.path.insert(0, '../util')
from util import fasta_file_to_dna_strings

dna_strings = fasta_file_to_dna_strings('rosalind_gc.txt')
highest_gc_score = 0
highest_gc_score_id = ""

for k in dna_strings.keys():
  dna_string = dna_strings[k]
  gc_score = round((dna_string.count('C') + dna_string.count('G')) / len(dna_string) * 100, 6)

  if gc_score > highest_gc_score:
    highest_gc_score = gc_score
    highest_gc_score_id = k

print(highest_gc_score_id)
print(highest_gc_score)
