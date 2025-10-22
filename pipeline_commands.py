def Replace(old:str, new:str, words:list)->list:
	"""
	Change the old string to the new in the variable words
	"""
	
	for i in range(len(words)):
		if words[i] == old:
			words[i] = new
	return words	

def Upper(words:list, wordtoupper:str, letter=None)->list:
	"""
	upper the word 'wordtoupper'
	"""

	for i in range(len(words)):
		if words[i] == wordtoupper:
			if letter:
				for j in range(len(words[i])):
					if words[i][j] == letter:
						words[i] = words[i][:j] + words[i][j].upper() + words[i][j+1:]
			else:
				words[i] = words[i].upper()

	return words

def Lower(words:list, wordtolower:str, letter=None)->list:
	"""
	lower the word 'wordtolower'
	"""
	for i in range(len(words)):
		if words[i].lower() == wordtolower:
			if letter:
				for j in range(len(words[i])):
					if words[i][j] == letter:
						words[i] = words[i][:j] + words[i][j].lower() + words[i][j+1:]
			else:
				words[i] = words[i].lower()
	return words