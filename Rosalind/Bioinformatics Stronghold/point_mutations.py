with open('rosalind_hamm.txt', 'r') as r:
	data = r.read()
	r.close()

seq_data = data.split('\n')
s = seq_data[0]
t = seq_data[1]

seq_len = len(s)
hamming = 0

for s1, s2 in zip(s, t):
	
	if s1 != s2:
		hamming += 1

print(hamming)