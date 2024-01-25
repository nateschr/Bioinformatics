with open('codon_table.txt', 'r') as c:
	codons = c.read()
	c.close()

lines = codons.split()
codons_dict = {}
for i, x in enumerate(lines):

    if i == 0:
    	codons_dict[x] = lines[i+1]
    elif i % 2 == 0:
    	codons_dict[x] = lines[i+1]


with open('rosalind_prot.txt', 'r') as rna:
	rna_seq = rna.read()

transcr = ''

for i in range(0, len(rna_seq), 3):
	codon = rna_seq[i:i+3]
	if codon != '\n':
		if codons_dict[codon] != 'Stop':
			transcr += codons_dict[codon]
	else:
		continue

print(transcr)