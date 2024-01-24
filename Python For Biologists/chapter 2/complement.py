seq = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATATACGATGCGTTCAT'
comp = ''

for i in seq:
	if i == 'A':
		comp += 'T'
	if i == 'T':
		comp += 'A'
	if i == 'G':
		comp += 'C'
	if i == 'C':
		comp += 'G'

print(seq)
print(comp)