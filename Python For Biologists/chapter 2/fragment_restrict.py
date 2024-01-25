seq = 'ACTGATCGATTACGTATAGGAATTCGCTATCATACATATATATATACGATGCGTTCAT'
motif = 'GAATTC'
motif_loci = seq.find(motif)

print(seq[:motif_loci+1])
print(seq[1+motif_loci:])