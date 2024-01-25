datafile = 'transcribing_dna.txt'

with open(datafile, 'r') as f:
	dna = f.read()

rna = dna.replace('T', 'U')

print(rna)