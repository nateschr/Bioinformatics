with open('counting_dna.txt', 'r') as f:
	nt = f.read()

# nt_A = nt.count('A')
# nt_T = nt.count('T')
# nt_C = nt.count('C')
# nt_G = nt.count('G')

# print(nt_A, nt_C, nt_G, nt_T)
# 
# a more eloquent solution:

def nt_count(s):
	return s.count('A'), s.count('C'), s.count('G'), s.count('T')

print(nt_count(nt))