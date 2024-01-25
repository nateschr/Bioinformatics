with open('rosalind_gc.txt', 'r') as data:
    seq = data.read()
    data.close()

# first split sequences by seq start marker: '>'
seq_c = seq.split('>')
# pop first empty list item: ''
seq_c = seq_c[1:]
# remove newline markers
seq_c = [x.replace('\n', '') for x in seq_c]

# initialize dictionary object
seq_dict = {}
gc_dict = {}

# connect sequence label to sequence data
for i in seq_c:
	# grab seq label
    id = i[0:13]
    # grab seq separate from label
    id_seq = i[13:]
    seq_dict[id] = id_seq

for key, value in seq_dict.items():
    seq_len = len(value)
    gc_content = value.count('G') + value.count('C')
    gc_content = round((gc_content / seq_len), 6) * 100
    gc_dict[key] = gc_content

print(gc_dict)

# get max gc_value
gc_max = max(gc_dict, key=gc_dict.get)

print(gc_max)
print(gc_dict[gc_max])
    
input()
