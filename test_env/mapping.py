import sys

d = {}
with open(sys.argv[1], 'r', encoding='BIG5-HKSCS') as file:
	for line in file:
		word, zhuins = line.split(' ', 1)
		for zhuin in zhuins.split('/') :
			d.setdefault(zhuin[0], [])
			d[zhuin[0]].append(word)

file.close()

with open(sys.argv[2], 'w', encoding='BIG5-HKSCS') as file:
	for key, values in d.items():
		file.write(key+' ')
		for value in values:
			file.write(value+' ')
		file.write('\n')
		for value in values:
			file.write(value+' '+value+'\n')
file.close()
