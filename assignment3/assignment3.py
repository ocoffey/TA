import sys

class HashTable:




def main():
    try:
        sys.argv[1]
    except IndexError:
        print("File Not Passed")
        return

