import unittest
from gradescope_utils.autograder_utils.decorators import weight
import subprocess
import sys

class TestTweetReader(unittest.TestCase):
    """
    30 Points
    n - prints next tweet - 4
    p - prints prev tweet - 4
    f - prints first tweet - 4
    l - prints last tweet - 4
    <num> - skips circularly, prints that current tweet - 5
    s <word> - searches for a substring, prints if found - 8
    q - quits the program - 1 point
    """
    @weight(1)
    def test_eval_quit(self):
        """
        Open a subprocess of their assignment, passing the text file
        Communicate to it the commands we want
        """
        s = "q"
        p = subprocess.Popen(['python3', 'assignment2.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, perror = p.communicate(s.encode())
        print(p.returncode)
        if p.returncode != 0:
            raise AssertionError()
        print(out.decode())
        #sys.executable
        # , "cnnhealth.txt"
    
    @weight(1)
    def test_eval_quit_wtxt(self):
        """
        Open a subprocess of their assignment, passing the text file
        Communicate to it the commands we want
        """
        s = "q"
        p = subprocess.Popen(['python3', 'assignment2.py', 'cnnhealth.txt'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, perror = p.communicate(s.encode())
        print(p.returncode)
        if p.returncode != 0:
            raise AssertionError()
        print(out.decode())
        #sys.executable
        # 