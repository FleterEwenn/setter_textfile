def Split_text(text:str)->str:
	"""
	Split properly text with space and also split punctuation
	"""
	text_toreturn = []
	chars = [',', '.', ';']
	for str_ in text.split(' '):
		if str_[-1] in chars:
			text_toreturn.append(str_[:-1])
			text_toreturn.append(str_[-1])

		else:
			text_toreturn.append(str_)
	return text_toreturn