# Counting Point Mutations

# Sample Dataset
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT

# Sample Output
# 7

def hamming_distance(string1, string2)
  h = 0
  (0..string1.length - 1).each do |i|
    h += 1 if string1[i] != string2[i]
  end
  h
end
