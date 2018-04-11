# Computing GC Content

# Sample Dataset
# sample_dataset.txt

# Sample Output
# Rosalind_0808
# 60.919540

require '../util/util'

highest_gc_score = 0
highest_gc_score_id = ''

dna_strings = fasta_file_to_dna_strings('rosalind_gc.txt')

dna_strings.each_pair do |k, dna_string|
  gc_score = (((dna_string.count('C') + dna_string.count('G')) / dna_string.size.to_f) * 100).round(6)

  if gc_score > highest_gc_score
    highest_gc_score = gc_score
    highest_gc_score_id = k
  end
end

puts(highest_gc_score_id)
puts(highest_gc_score)
