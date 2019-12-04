import unittest
from gradescope_utils.autograder_utils.decorators import weight
import os
import re
import subprocess

class TestAdditional(unittest.TestCase):
    """Additional Tests - 20 points"""

    def setUp(self):
        self.test = 'tests/nprhealth.txt'
        self.testpy = 'tests/testassignment2.py'
        self.testpy2 = 'tests/testassignment2post.py'

    def sub_func(self, stinput: str) -> bool:
        """Function call to actually run the test"""
        # runs the students file, passing a .txt file
        studp = subprocess.run(['python3', 'assignment2.py', self.test], stdout=subprocess.PIPE, input=stinput, encoding='ascii')
        # runs our file, passing the same .txt file
        testp = subprocess.run(['python3', self.testpy, self.test], stdout=subprocess.PIPE, input=stinput, encoding='ascii')
        # runs file with pre insertion for equal nodes
        testpostp = subprocess.run(['python3', self.testpy2, self.test], stdout=subprocess.PIPE, input=stinput, encoding='ascii')
        # strips students stdout of all whitespace
        studstripped = re.sub(r"([\s\t\n])", r"", studp.stdout.strip())
        # strips our stdout of all whitespace
        teststripped = re.sub(r"([\s\t\n])", r"", testp.stdout.strip())
        # strips post insert stdout
        testpoststripped = re.sub(r"([\s\t\n])", r"", testpostp.stdout.strip())
        # Make sure that everything returned 0
        if studp.returncode == testp.returncode == testpostp.returncode == 0:
            # compares outputs and returns that bool
            return (studstripped == teststripped) or (studstripped == testpoststripped)
        # Let me know if I made an error
        elif testp.returncode != 0:
            print("I made an error")
            print(self.test, end='')
            print(" was the filename passed.")
            return False
        elif testpostp.returncode != 0:
            print("I made an error")
            print(self.test, end='')
            print(" was the filename passed.")
            return False
        # If the student didn't return 0
        else:
            print("Your file returned error code: " + str(studp.returncode))
            return False

    @weight(10)
    def test_chrono(self):
        inps = 'n\nn\nn\nn\nn\nn\nn\nn\n500\nn\nn\nn\nn\nn\nn\nn\nn\nf\np\np\np\np\np\np\nq\n'
        try:
            self.assertIs(self.sub_func(inps),True)
        except AssertionError:
            assert False, "Tweets Not In Chronological Order (Note: This Test Uses Skip)"

    @weight(10)
    def test_rand(self):
        try:
            self.assertIs(self.sub_func('50000\n600\nq\n'),True)
        except AssertionError:
            assert False, "Two Random Tweets Not Equal (Note: This Test Uses Skip)"