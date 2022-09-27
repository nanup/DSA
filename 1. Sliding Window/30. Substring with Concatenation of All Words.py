# Given a string and a list of words,
# find all the starting indices of substrings in the given string
# that are a concatenation of all the given words exactly once without any overlapping of words.
# It is given that all words are of the same length.

def findWordConcatenation(str, words):
	if len(words) == 0 or len(words[0]) == 0:
		return []

	result = []

	wordLength = len(words[0])
	wordCount = len(words)

	wordFrequency = {}

	for word in words:
		if word not in wordFrequency:
			wordFrequency[word] = 0

		wordFrequency[word] += 1

	for i in range((len(str) - wordLength * wordCount) + 1):
		wordsSeen = {}
		# solely to check if a word count is more than allowed

		for j in range(wordCount):
			nextIndex = i + j * wordLength # ensures the starting index of wordCoutn number of words

			word = str[nextIndex:nextIndex + wordLength]

			if word not in wordFrequency:
				# this i is not useful so we move on to next
				break

			if word in wordFrequency:
				if word not in wordsSeen:
					wordsSeen[word] = 0

				wordsSeen[word] += 1

			if wordsSeen[word] > wordFrequency.get(word, 0):
				# number of occurences is more than allowed, move on to next i
				break
				
			if j + 1 == wordCount:
				# successfully checked wordCount number of matches
				result.append(i)

	return result
			
def main():
	print(findWordConcatenation("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))


main()

# time complexity: O(N * M * Len)
# space complexity: O(M + N)