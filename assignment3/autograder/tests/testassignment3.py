import sys
import re

def main():
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
    userdict = dict.fromkeys([word.lower() for word in mydict])

    """
    Print words from the file if they're not in the dict
    """
    # for each line in the story
    for line in story:
        # convert to lowercase, and split based on whitespace
        line = line.lower().split()
        # see if each word is in the dict
        for word in line:
            # correct the apostrophe
            word = re.sub(r"([’])", r"(['])", word)
            # remove junk chars in the word
            word = re.sub(r"([^a-z0-9'])", r"", word)
            if word not in userdict:
                print(word)

if __name__ == "__main__":
    main()