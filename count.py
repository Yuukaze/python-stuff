
with open("big.txt", 'r') as inFile:
	text = inFile.read().strip()
	len_chars = sum(len(word) for word in text)
	print(len_chars)



