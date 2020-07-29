from collections import defaultdict
wordList = ["acd", "dfg", "wyz", "yab", "mop", "bdfh", "a", "x", "moqs"]

hmap = defaultdict(list)

for word in wordList:
	dif = ord(word[0]) - ord('a')
	s = ''
	for c in word:
		s += chr((ord(c)-dif)%26+ord('a'))
	hmap[(len(word), s)].append(word)
print(*hmap.values())
