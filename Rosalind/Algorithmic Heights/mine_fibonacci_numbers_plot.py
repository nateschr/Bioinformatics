import matplotlib.pyplot as plt
import numpy as np

#pairs = np.array(pairs)

seq = {"0":0, "1":1}
n = 10

for s in range(2, n+1):
    seq[str(s)] = seq[str(s-1)] + seq[str(s-2)]


seq_dict = seq.items()
seq_data = list(seq_dict)
seq_np = np.array(seq_data)

print(seq_np)

plt.scatter(seq_np[:,0],seq_np[:,1])
plt.show()

input()
