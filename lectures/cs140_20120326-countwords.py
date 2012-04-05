# Code Listing 8.1

# Count words in a string
speech = "to be or not to be"
speechList = speech.split()

##print speech
##print speechList

wordCountDict = {}

for word in speechList:
    if word in wordCountDict:
        wordCountDict[word] += 1
    else:
        wordCountDict[word] = 1

print wordCountDict
