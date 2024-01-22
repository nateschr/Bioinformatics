seq = {"0":0, "1":1}

n = 500

for s in range(2, n+1):
    seq[str(s)] = seq[str(s-1)] + seq[str(s-2)]

print(seq)
input()
