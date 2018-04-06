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

def common_motif(dna_strings):
  longest_motif = ''
  dna = min(dna_strings, key = len)

  for start in range(len(dna)):
    for l in range(1, len(dna) - start):
      motif = dna[start:start+l]
      if len(motif) > len(longest_motif) and all(motif in x for x in dna_strings):
        longest_motif = motif

  return longest_motif

def fasta_file_to_dna_strings(fasta_file):
  dna_strings = {}
  with open(fasta_file) as fasta:
    for line in fasta:
      if len(line) > 0 and line[0] == '>':
        name = line[1::].strip()
        dna_strings[name] = ''
      else:
        dna_strings[name] += line.strip()
  return dna_strings


list1 = fasta_file_to_dna_strings('rosalind_lcsm.txt').values()
print(common_motif(list1))