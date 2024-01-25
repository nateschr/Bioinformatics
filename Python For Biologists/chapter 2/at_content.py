seq = 'ACTGATCGATTCTACTCGTACTAGCTATTTTGCATATCATCATATATATATATATATCGATGCGTTCATCGATTTTAAATATATA'

seq_len = len(seq)
seq_a = seq.count('A'.upper())
seq_T = seq.count('T'.upper())
AT_content = seq_a + seq_T / seq_len

print(round(AT_content, 2))