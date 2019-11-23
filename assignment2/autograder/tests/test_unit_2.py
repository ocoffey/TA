import unittest
from gradescope_utils.autograder_utils.decorators import weight
import os
import re
import subprocess

class TestTweetReader(unittest.TestCase):
    """Test Tweet Reader - 50 points"""

    def setUp(self):
        self.test = 'tests/nprhealth.txt'
        self.testpy = 'tests/testassignment2.py'

    def sub_func(self, stinput: str) -> bool:
        """Function call to actually run the test"""
        # runs the students file, passing a .txt file
        studp = subprocess.run(['python3', 'assignment2.py', self.test], stdout=subprocess.PIPE, input=stinput, encoding='ascii')
        # runs our file, passing the same .txt file
        testp = subprocess.run(['python3', self.testpy, self.test], stdout=subprocess.PIPE, input=stinput, encoding='ascii')
        # strips students stdout of all whitespace
        studstripped = re.sub(r"([\s\t\n])", r"", studp.stdout.strip())
        # strips our stdout of all whitespace
        teststripped = re.sub(r"([\s\t\n])", r"", testp.stdout.strip())
        # Make sure that both returned 0
        if studp.returncode == testp.returncode and testp.returncode == 0:
            # compares outputs and returns that bool
            return studstripped == teststripped
        # Let me know if I made an error
        elif testp.returncode != 0:
            print("I made an error")
            print(self.test, end='')
            print(" was the filename passed.")
            return False
        # If the student didn't return 0
        else:
            return False


    @weight(2)
    def test_quit(self):
        testq = subprocess.run(['python3', 'assignment2.py', self.test], stdout=subprocess.PIPE, input='q\n', encoding='ascii')
        try:
            self.assertEqual(testq.returncode,0)
        except AssertionError:
            assert False, "q Input Did Not Quit"
        return
    
    @weight(4)
    def test_next(self):
        try:
            self.assertIs(self.sub_func('n\nq\n'),True)
        except AssertionError:
            assert False, "n Input Did Not Go Next"

    @weight(4)
    def test_prev(self):
        try:
            self.assertIs(self.sub_func('p\nq\n'),True)
        except AssertionError:
            assert False, "p Input Did Not Go Previous"

    @weight(4)
    def test_first(self):
        try:
            self.assertIs(self.sub_func('f\nq\n'),True)
        except AssertionError:
            assert False, "f Input Did Not Go First"

    @weight(4)
    def test_last(self):
        try:
            self.assertIs(self.sub_func('l\nq\n'),True)
        except AssertionError:
            assert False, "l Input Did Not Go Last"

    @weight(8)
    def test_num(self):
        try:
            self.assertIs(self.sub_func('num\nq\n'),True)
        except AssertionError:
            assert False, "num Input Did Not Print Number Of Nodes"

    @weight(10)
    def test_skip(self):
        try:
            self.assertIs(self.sub_func('5000\nq\n'),True)
        except AssertionError:
            assert False, "skip Input Did Not Go To The Correct Node"

    @weight(14)
    def test_search(self):
        try:
            self.assertIs(self.sub_func('s cancer\nq\n'),True)
        except AssertionError:
            assert False, "s <word> Input Did Not Give Next Occurrence Of <word>"