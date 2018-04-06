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

require '../util/util'

def common_motif(dna_strings)
  longest_motif = ''
  dna = dna_strings.min {|a,b| a.length <=> b.length}

  (0..dna.length - 1).each do |start|
    (1..dna.length - start).each do |len|
      motif = dna[start, len]
      if motif.length > longest_motif.length && dna_strings.all? {|x| !x.index(motif).nil?}
        longest_motif = motif
      end
    end
  end

  longest_motif
end


list = fasta_file_to_dna_strings('rosalind_lcsm.txt').values
puts common_motif(list)

# AGAAACTTCCTACAAGCACGTACATGCAGGCACGTCCGAGTCAACGACACGATCAGTA
# TGAACAGAATTGCCTGTAATTTACGTTTTGACGTGTCATGGACAGTTTCATGCTCCGA
# TGCCAGCCTACTCGTATTCTCTCTGTGGCTACTTTGAAGCCCGCCAGACCATGTCATT
# AATACAGGGAAT