def count_word(text):
	'''list(str) -> dict (str: int)
	return count of words in given text
	'''
	word_count = dict()
	for line in text:
		arr = line.split()
		arr = list(map(arr, strip()))
		for word in arr:
			if word in word_count.key():
				word_count[word] = word_count[word]+1
			else:
				word_count[word] = 1
		return word_count


# 불용어 제거
def removeStopWord():
	pronoun = []
	adverb = []
	preposition = []
	proposition = []
	interjection = []
	pass


def preprocessing():
	removeStopWord()


def getFrequentWord():
	file_list = get_file_list(folder) #implementation needed
	tot_w = dict()
	for file in file_list:
		text = get_text(file) #implementation needed
		w_dict = count_word(text)
		merge_dict(tot_w, w_dict) #merge dictionary
	result=list()
	for w in tot_w.key():
		if some_condition:
			result.append(w, tot_w[w])
	return result

