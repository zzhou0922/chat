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
	person = None # Preset that person has no value which is null in other language
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	# print(s)
	print('Allen said', allen_word_count, 'word(s).')
	print('Allen used', allen_sticker_count, 'sticker(s).')
	print('Allen sent', allen_image_count, 'image(s).')
	print('Viki said', viki_word_count, 'words(s).')
	print('Viki used', viki_sticker_count, 'sticker(s).')
	print('Viki sent', viki_image_count, 'image(s).')


def write_file(filename, chats):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in chats:
			f.write(line + '\n')


def main():
	filename = 'LINE-Viki.txt'
	if os.path.isfile(filename):
		print('Found the file')
		chats = read_file(filename)
		chats = convert(chats)
		# write_file('output.txt', chats)
	else:
		print('No such a file')

main()