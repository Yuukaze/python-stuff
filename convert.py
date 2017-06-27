


inputFile = open("big.txt", 'r')
content = inputFile.read()
with open("big transfer.txt", 'wb') as outputFile:
	outputFile.write(content.upper())
			
		
	