import sys
with open(sys.argv[1], 'r', encoding='BIG5-HKSCS') as file:
	for line in file:
		print(line)
