# Finding a Motif in DNA

# Sample Dataset
# GATATATGCATATACTT
# ATAT

# Sample Output
# 2 4 10

def find_motif(dna, motif)
  indexes = []
  start_at = 0
  while start_at < dna.size do
    i = dna.index(motif, start_at)
    if i.nil?
      break
    else
      indexes << i unless i.nil?
      start_at = i + 1
    end
  end

  # output data should be space separated 1-based numbering indexes:
  indexes.map {|x| x + 1 } * ' '
end
