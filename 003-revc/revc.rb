# Complementing a Strand of DNA

# Sample Dataset
# AAAACCCGGT
# Sample Output
# ACCGGGTTTT

def reverse_complement(dna_string)
  complementary = {'A' => 'T', 'T' => 'A', 'C' => 'G', 'G' => 'C'}
  complement = ""
  dna_string.reverse.each_char do |nucleotide|
    complement += complementary[nucleotide]
  end
  complement
end
