# Counting DNA Nucleotides

# Sample Dataset
# AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

# Sample Output
# 20 12 17 21

def count_nucleotides(data)
  ['A', 'C', 'G', 'T'].map {|nucleotid| data.count(nucleotid)} * ' '
end
