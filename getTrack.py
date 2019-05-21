#getTrack.py
key = '0416DD324C5881'
loc = ''
with open('records.csv') as file:
	data = file.readlines()
	for line in data:
		line1 = line.split(',')
		if (key == line1[1].strip().replace(" ", "")):
			loc = line1[2]
print(loc)