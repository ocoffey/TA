import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess
from collections import Counter

class TestDict(unittest.TestCase):
    """Test Dictionary Lookups - 40 points
    
    Test that the outputs are as they should be
    """

    def setUp(self):
        self.test = 'tests/miserable.txt'
        self.ourdict = 'tests/american-english'
        self.testpy = 'tests/testassignment3.py'

    @weight(40)
    def test_outputs(self):
        """Testing that student outputs match correct outputs"""
        # runs the students file, passing a .txt file
        studp = subprocess.run(['python3', 'assignment3.py', self.test, self.ourdict], stdout=subprocess.PIPE, encoding='ascii')
        # runs our file, passing the same .txt file
        testp = subprocess.run(['python3', self.testpy, self.test, self.ourdict], stdout=subprocess.PIPE, encoding='ascii')
        # strips students stdout of all whitespace
        studOutList = studp.stdout.split('\n')
        # strips our stdout of all whitespace
        testOutList = testp.stdout.split('\n')
        # Make sure that both returned 0
        if studp.returncode == testp.returncode and testp.returncode == 0:
            # count the words and compare counts
            try:
                self.assertEqual(Counter(studOutList),Counter(testOutList))
            except AssertionError:
                assert False, "Word Count Not Equal"
        # Let me know if I made an error
        elif testp.returncode != 0:
            print("We made an error")
            print(self.test + " was the book passed.")
            print(self.ourdict + " was the dictionary passed.")
            self.assertTrue(False)
        # If the student didn't return 0
        else:
            assert False, "Your Assignment Returned Error Code: " + str(studp.returncode)
