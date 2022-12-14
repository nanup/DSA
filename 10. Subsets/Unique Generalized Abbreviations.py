# Given a word, write a function to generate all of its unique generalized abbreviations.
# Generalized abbreviation of a word can be generated by replacing each substring of the word
# by the replaceCount of characters in the substring. Take the example of “ab” which has four substrings
# : “”, “a”, “b”, and “ab”. After replacing these substrings in the actual word
# by the replaceCount of characters we get all the generalized abbreviations:
# “ab”, “1b”, “a1”, and “2”.

from collections import deque


class AbbreviatedWord():
	def __init__(self, str, index, replaceCount):
		self.str = str
		self.index = index
		self.replaceCount = replaceCount
	
def generate_generalized_abbreviation(word):
	wordLen = len(word)

	result = []

	queue = deque()
	queue.append(AbbreviatedWord(list(), 0, 0))

	while queue:
		abWord = queue.popleft()

		if abWord.index == len(word):
			if abWord.replaceCount != 0:
				abWord.str.append(str(abWord.replaceCount))
			result.append("".join(abWord.str))
		else:
			queue.append(AbbreviatedWord(list(abWord.str), abWord.index + 1, abWord.replaceCount + 1))

			if abWord.replaceCount != 0:
				abWord.str.append(str(abWord.replaceCount))

			newWord = list(abWord.str)
			newWord.append(word[abWord.index])
			queue.append(AbbreviatedWord(newWord, abWord.index + 1, 0))

	return result

def main():
	print("Generalized abbreviation are: " +
		  str(generate_generalized_abbreviation("BAT")))
	print("Generalized abbreviation are: " +
		  str(generate_generalized_abbreviation("code")))


main()

# time complexity: O(2 ^ N)
# space complexity: O(2 ^ N)