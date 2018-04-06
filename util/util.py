def fasta_file_to_dna_strings(fasta_file):
  dna_strings = {}
  with open(fasta_file) as fasta:
    for line in fasta:
      if len(line) > 0 and line[0] == '>':
        name = line[1:].strip()
        dna_strings[name] = ''
      else:
        dna_strings[name] += line.strip()
  return dna_strings

