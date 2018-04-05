# Consensus and Profile

# Sample Dataset
# sample_dataset.txt

# Sample Output
# sample_output.txt

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

def profile(dna_strings):
  length = len(dna_strings[0])
  a, c, g, t = [0]*length, [0]*length, [0]*length, [0]*length
  profile = {'A': a, 'C': c, 'G': g, 'T': t }

  for dna_string in dna_strings:
    for i in range(len(dna_string)):
      profile[dna_string[i]][i] += 1

  return profile

def consensus(profile):
  consensus = ''
  for i in range(len(profile['A'])):
    max = 0
    symbol = ''
    for k in profile.keys():
      if profile[k][i] >= max:
        max = profile[k][i]
        symbol = k

    consensus += symbol

  return consensus

def print_profile(profile, output_file):
  with open(output_file, 'a') as output:
    for symbol in list(profile.keys()):
      output.write(symbol + ': ')
      output.write(' '.join(str(i) for i in profile[symbol]))
      output.write('\n')

def print_consensus(consensus, output_file):
  with open(output_file, 'a') as output:
    output.write(consensus)
    output.write('\n')


input_file = 'rosalind_cons.txt'
output_file = 'rosalind_cons_output.txt'

profile = profile(list(fasta_file_to_dna_strings(input_file).values()))
consensus = consensus(profile)

print_consensus(consensus, output_file)
print_profile(profile, output_file)
