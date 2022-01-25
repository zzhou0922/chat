import os

def read_file(filename):
	chats = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			line = line.strip()
			chats.append(line)
	# print(chats)
	return chats

def convert(lines):
	new = []
	person = None # Preset that person has no value which is null in other language
	for line in lines:
		# print(line)
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue	
		if person: # Here means if person has value then get into the if condition
			new.append(person + ': ' + line)
	# print(new)
	return new


def write_file(filename, chats):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in chats:
			f.write(line + '\n')


def main():
	filename = 'input.txt'
	if os.path.isfile(filename):
		print('Found the file')
		chats = read_file(filename)
		chats = convert(chats)
		write_file('output.txt', chats)
	else:
		print('No such a file')

main()