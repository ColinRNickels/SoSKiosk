#getkeys.py
keys = []
with open('records.csv') as file:
	data = file.readlines()
	for line in data:
		line1 = line.split(',')
		keys.append(line1[1].strip().replace(" ", ""))
print(keys)