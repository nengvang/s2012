
# Code listing 8.2 (modified)
def add_word(word, wcDict):
    if word in wcDict:
        wcDict[word] += 1
    else:
        wcDict[word] = 1

# Code listing 8.3 (modified)
def process_line(line, wcDict):
    """Process the line to get lowercase words to add to the dictionary."""
    line = line.strip()
    wordList = line.split()

    for word in wordList:
        if word != '--':
            word = word.lower()
            word = word.strip()
            word = word.strip('.,!?;')
            add_word(word, wcDict)

# Code listing 8.4 (modified)
def pretty_print(wcDict):
    """Print nicely from highest to lowest frequency."""
    # Create a list of tuples (value, key)
    # val_key_list = [(val, key) for key, val in d.items()]
    val_key_list = []
    for key, val in wcDict.items():
        val_key_list.append((val, key))

    # Sort from highest to lowest
    val_key_list.sort(reverse=True)
    print '%-10s%10s' % ('Word', 'Count')
    print '_' * 20
    for val, key in val_key_list:
        print '%-12s     %3d' % (key, val)

# Code listing 8.5 (modified)
def main():
    wcDict = {}
    file_object = open('gettysburg.txt', 'r')
    for line in file_object:
        process_line(line, wcDict)

    print 'Length of the dictionary:', len(wcDict)
    pretty_print(wcDict)

main()
