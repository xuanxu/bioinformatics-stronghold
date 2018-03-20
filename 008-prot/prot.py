# Translating RNA into Protein

# Sample Dataset
# AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

# Sample Output
# MAMAPRTEINSTRING

def prot(rna):
  position = 0
  proteins = ''

  while(position < len(rna)):
    protein = rna_codon_to_protein(rna[position:position+3])
    if protein == 'Stop' or protein == None:
      break
    else:
      proteins += protein
      position += 3
  return proteins


def rna_codon_to_protein(codon):
  codon_to_protein = { 'UUU': 'F',
                       'UUC': 'F',
                       'UUA': 'L',
                       'UUG': 'L',
                       'UCU': 'S',
                       'UCC': 'S',
                       'UCA': 'S',
                       'UCG': 'S',
                       'UAU': 'Y',
                       'UAC': 'Y',
                       'UAA': 'Stop',
                       'UAG': 'Stop',
                       'UGU': 'C',
                       'UGC': 'C',
                       'UGA': 'Stop',
                       'UGG': 'W',
                       'CUU': 'L',
                       'CUC': 'L',
                       'CUA': 'L',
                       'CUG': 'L',
                       'CCU': 'P',
                       'CCC': 'P',
                       'CCA': 'P',
                       'CCG': 'P',
                       'CAU': 'H',
                       'CAC': 'H',
                       'CAA': 'Q',
                       'CAG': 'Q',
                       'CGU': 'R',
                       'CGC': 'R',
                       'CGA': 'R',
                       'CGG': 'R',
                       'AUU': 'I',
                       'AUC': 'I',
                       'AUA': 'I',
                       'AUG': 'M',
                       'ACU': 'T',
                       'ACC': 'T',
                       'ACA': 'T',
                       'ACG': 'T',
                       'AAU': 'N',
                       'AAC': 'N',
                       'AAA': 'K',
                       'AAG': 'K',
                       'AGU': 'S',
                       'AGC': 'S',
                       'AGA': 'R',
                       'AGG': 'R',
                       'GUU': 'V',
                       'GUC': 'V',
                       'GUA': 'V',
                       'GUG': 'V',
                       'GCU': 'A',
                       'GCC': 'A',
                       'GCA': 'A',
                       'GCG': 'A',
                       'GAU': 'D',
                       'GAC': 'D',
                       'GAA': 'E',
                       'GAG': 'E',
                       'GGU': 'G',
                       'GGC': 'G',
                       'GGA': 'G',
                       'GGG': 'G' }

  return codon_to_protein.get(codon)
