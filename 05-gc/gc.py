# Computing GC Content

# Sample Dataset
# sample_dataset.txt

# Sample Output
# Rosalind_0808
# 60.919540

dna_strings = {}
highest_gc_score = 0
highest_gc_score_id = ""

with open('sample_dataset.txt') as fasta:
  for line in fasta:
    if len(line) > 0 and line[0] == '>':
      name = line[1::].strip()
      dna_strings[name] = ""
    else:
      dna_strings[name] += line.strip()

for k in dna_strings.keys():
  dna_string = dna_strings[k]
  gc_score = round((dna_string.count('C') + dna_string.count('G')) / len(dna_string) * 100, 6)

  if gc_score > highest_gc_score:
    highest_gc_score = gc_score
    highest_gc_score_id = k

print(highest_gc_score_id)
print(highest_gc_score)
