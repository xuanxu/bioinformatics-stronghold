# Transcribing DNA into RNA

# Sample Dataset
# GATGGAACTTGACTACGTAAATT
# Sample Output
# GAUGGAACUUGACUACGUAAAUU

def transcribe(dna)
  dna.gsub('T', 'U')
end
