import unittest
from gradescope_utils.autograder_utils.decorators import weight
from assignment3 import HashTable
import random

class TestHashTable(unittest.TestCase):
    """Testing Hash Table - 60 points
    
    -Test that the table is appropriate size
    -Test that the hash is less than size of table
    -Test insert and lookup implemented correctly (paired)
    """

    @weight(15)
    def test_table_size(self):
        """Make hash table with 100 entries,
        and make sure that it has than many"""
        myHashTable = HashTable(100)
        self.assertEqual(len(myHashTable), 100)

    @weight(15)
    def test_hash_range(self):
        """Make sure that the hashing function doesn't
        output a number larger than the size
        of the hash table
        """
        myHashTable = HashTable(50)
        myEntries = []
        for x in range(2000):
            temp = ""
            for y in range(10):
                # make a random letter between 'a' and 'z'
                myLet = random.randrange(ord('a'), ord('z'))
                temp = temp + chr(myLet)
            myEntries.append(temp)
        for entry in myEntries:
            self.assertTrue(myHashTable.make_hash(entry) < 50)
    
    @weight(30)
    def test_insert_lookup(self):
        myHashTable = HashTable(200)
        inputs = ["hello", "test", "hi", "hey"]
        for word in inputs:
            myHashTable.insert(word)
        tests = {"hello": True, "not": False, "hey": True, "one": False}
        for test in tests:
            self.assertEqual(myHashTable.lookup(test), tests[test])
