# Overlap Graphs

# Sample Dataset
# sample_dataset.txt

# Sample Output
# sample_output.txt

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


dna_strings = fasta_file_to_dna_strings('rosalind_grph.txt')
o3 = o3_adjacency_list(dna_strings)
with open('rosalind_output', 'w') as output:
  for edge in o3:
    output.write(edge[0] + ' ' + edge[1] + '\n')
