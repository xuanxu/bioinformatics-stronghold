def fasta_file_to_dna_strings(fasta_file)
  dna_strings = {}
  File.open(fasta_file) do |f|
    code ||= ''
    f.each_line do |line|
      if line and line.start_with?('>')
        code = line[1, line.length - 1].strip
        dna_strings[code] = ''
      else
        dna_strings[code] += line.strip
      end
    end
  end
  dna_strings
end