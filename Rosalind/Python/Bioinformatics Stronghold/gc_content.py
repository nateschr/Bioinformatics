with open('gc_content.txt', 'r') as data:
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

# connect sequence label to sequence data
for i in seq_c:
    id = i[0:13]
    id_seq = i[13:]
    seq_dict[id] = id_seq

for key, value in seq_dict.items():
    seq_len = len(value)
    gc_content = value.count('G') + value.count('C')
    gc_content = round((gc_content / seq_len), 3) * 100

    print('GC content of', key, 'is', gc_content)
    
input()
