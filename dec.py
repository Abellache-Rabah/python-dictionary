import json
import difflib
data = json.load(open("data.json"))

def get(word):
	word = word.lower()
	if (word in data):
		return data[word]
	else:
		correctWord = difflib.get_close_matches(word, data)[0]
		yesOrNo = input('did you mean [ ' + correctWord +' ] (Y for yes !!) : ')
		if (yesOrNo == 'Y' ):
			return data[correctWord]
		else:
			return "sorry can't find the word"

word = input('Enter a Word: ')
a = get(word)
print(*a, sep = "\n")