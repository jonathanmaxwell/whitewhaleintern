import fileinput
import random
import sys

for line in sys.stdin:
	baseinput = line

#line= input()
#baselist = []
#for c in line:
#	baselist.append(c)
#this is a list of every character
baselist = list(baseinput)
newlist = baselist
wordlist = []
i = 0
#Becomes True to denote a word has been found; keeps track of the word length)
marked = False
first = 0
last = 0

#creates a seperate list comprised of the middle characters of the word
def getword(wordlist, i, first, last):
	first += 1
	while (first < last):
		wordlist.append(baselist[first])
		first += 1
	return wordlist

#this avoids scrambling words of 3 letters or fewer (because they can't be scrambled)
def wordlength(first, last):
	length = (last - first + 1)
	return length

#this tests if the word is an all-upper-case word (an abbreviation or acronym)
def isAbbv(wordlist):
	for x in wordlist:
		if x.isupper() == False:
			return False
	return True

#this compares two lists, returning True if they are the same.
def isSame(wordlist, newlist, first):
	first += 1
	for x in wordlist:
		if x != newlist[first]:
			return False
		first += 1
	return True

for x in baselist:
	#If the character is a letter and no word has been noted yet (it's the first letter of the word)
	if x.isalpha() == True and marked == False:
		first = i
		marked = True
	#If the character is not a letter and the start of word has been noted (last character was end of word)
	if x.isalpha() == False and marked == True:
		last = (i-1)
		wordlist = getword(wordlist, i, first, last)
		#If the word is an abbreviation/acronym, skip it
		if isAbbv(wordlist) == True:
			pass
		#If the word is 4 letters and not an abbreviation, just switch the middle two
		elif wordlength(first, last) == 4:
			newlist[first+1] = wordlist[1]
			newlist[first+2] = wordlist[0]
		#If the word is longer than 4 letters, randomly switch the letters inbetween
		elif wordlength(first, last) > 4:
			#checks to see if the word is unscrambled. If the letters are back where they startedafter scrambling , it will try again
			while isSame(wordlist, newlist, first) == True:
				j = first+1
				k = 0
				#sets middle of word to '0's
				while (j < last):
					newlist[j] = wordlist[k]
					newlist[j] = "0"
					j +=1
					k +=1
				k = 0
				#moves letters in randomly
				for y in range(0, len(wordlist)):
					while 1 == 1:
						position = random.randint(first+1, last-1)
						if newlist[position] == "0":
							newlist[position] = wordlist[y]
							break
		marked = False
		wordlist = []
	#tracks the position in the list
	i += 1
#this is how to turn a list back into a string for printing
str1 = ''.join(newlist)
print(str1)