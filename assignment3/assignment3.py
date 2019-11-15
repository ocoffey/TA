import sys
import re
"""
Open and read in story .txt file
"""
# make sure we can actually open the passed filename
try:
    sys.argv[1]
except IndexError:
    print("File Not Passed")
    sys.exit()

with open(sys.argv[1],'r') as f:
    story = f.readlines()

"""
Open and read in dict file
"""

try:
    sys.argv[2]
except IndexError:
    print("Dict Not Passed")
    sys.exit()

with open(sys.argv[2],'r') as f:
    mydict = f.read().splitlines()

"""
Put dict file into dictionary
"""
userdict = dict.fromkeys(mydict, True)

"""
Print words from the file if they're not in the dict
"""
# for each line in the story
for line in story:
    # replace junk chars with "", split based on whitespace
    line = re.sub(",|\.|!|\?|:|;|\(|\)|-|/", "", line).split()
    # see if each word is in the dict
    for word in line:
        try:
            userdict[word]
        # if not, print it
        except KeyError:
            print(word)
