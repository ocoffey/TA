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
        myHashTable = HashTable(100)
        try:
            self.assertEqual(myHashTable.size, 100)
        except AssertionError:
            assert False, "Hash Table Not The Size Given"

    @weight(15)
    def test_hash_range(self):
        myHashTable = HashTable(50)
        with open('tests/hashsize.txt','r') as file:
            myEntries = file.readlines()
        for entry in myEntries:
            try:
                self.assertTrue(myHashTable.make_hash(entry) < 50)
            except AssertionError:
                assert False, "Hash Larger Than Size Of Table"

    @weight(30)
    def test_insert_lookup(self):
        myHashTable = HashTable(200)
        inputs = ["hello", "test", "hi", "hey"]
        for word in inputs:
            myHashTable.insert(word)
        tests = {"hello": True, "not": False, "hey": True, "one": False}
        for test in tests:
            try:
                self.assertEqual(myHashTable.lookup(test), tests[test])
            except AssertionError:
                assert False, "Key In Hashtable Mismatch"