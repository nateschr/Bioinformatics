datafile = 'complement.txt'

with open(datafile, 'r') as f:
	original = f.read()

transcribe = ''

for i in original:
	if i == 'A':
		transcribe += 'T'
	if i == 'T':
		transcribe += 'A'
	if i == 'C':
		transcribe += 'G'
	if i == 'G':
		transcribe += 'C'

complement = ''

for i in transcribe:
	complement = i + complement
print(complement)