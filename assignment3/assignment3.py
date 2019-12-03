import sys
import re

class HashTable:
    """Hast Table Class"""
    def __init__(self, size: int = 0):
        """Constructor
        
        Takes a size, stores it
        Makes a list of the given size
        """
        self.size: int = size
        self.table: list = []
        self.make_table()
    
    def make_table(self) -> None:
        """Hash Table Creator
        
        Makes a table of the class's size"""
        for x in range(self.size):
            self.table.append([])

    def make_hash(self, word: str) -> int:
        """Hash Creator
        
        Takes a string, applies a hash method to it,
        and returns an int (the index to store the word)
        """
        myhash = 0
        for x in range(len(word)):
            myhash += ord(word[x]) * (31 ** x)
        return myhash % self.size

    def insert(self, word: str) -> None:
        """Insert

        Gets a hash for the given word, and
        attaches the word there
        """
        index = self.make_hash(word)
        self.table[index].append(word)

    def lookup(self, word: str) -> bool:
        """Lookup

        Returns True if the word is in the table
        """
        index = self.make_hash(word)
        return word in self.table[index]
    
def main():
    try:
        sys.argv[1]
    except IndexError:
        print("File Not Passed")
        sys.exit()
    
    with open(sys.argv[1],'r') as f:
        story = f.readlines()
    
    try:
        sys.argv[2]
    except IndexError:
        print("Dict Not Passed")
        sys.exit()

    with open(sys.argv[2],'r') as f:
        mydict = f.read().splitlines()
    
    # make a hash table with as many lines as the dictionary
    myHashTable = HashTable(len(mydict))

    # insert all dictionary elements into our hash table
    for term in mydict:
        myHashTable.insert(term.lower())
    
    for line in story:
        # splits that trimmed line into separate words
        line = line.lower().split()
        # looks up each word in the hashtable
        # and prints if they're not there
        for word in line:
            # correct the apostrophe
            word = re.sub(r"([’])", r"(['])", word)
            # replaces unwanted characters
            word = re.sub(r"([^a-z0-9'])", r"", word)
            if not myHashTable.lookup(word):
                print(word)

if __name__ == "__main__":
    main()