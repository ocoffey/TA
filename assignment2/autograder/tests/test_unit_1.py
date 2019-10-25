import unittest
from gradescope_utils.autograder_utils.decorators import weight
from assignment2 import CDLL, CDLLNode
import io
import sys

class TestLinkedList(unittest.TestCase):
    """
    30 Points
    """
    @weight(5)
    def test_eval_prepend(self):
        llpre = CDLL()
        for i in range(3,0,-1):
            llpre.prepend("",str(i))
        sout = []
        for i in range(3,0,-1):
            sout.append(llpre.current.tweet)
            llpre.current = llpre.current.next_node
        self.assertListEqual(sout,["1", "2", "3"])

    @weight(5)
    def test_eval_append(self):
        llapp = CDLL()
        for i in range(10):
            llapp.append(str(i),"")
        sout = []
        for i in range(10):
            sout.append(llapp.current.time)
            llapp.current = llapp.current.next_node
        self.assertListEqual(sout,["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

    @weight(3)
    def test_eval_go_next(self):
        llgn = CDLL()
        for i in range(2):
            llgn.append("",str(i))
        self.assertEqual(llgn.current.tweet, "0")
        llgn.go_next()
        self.assertEqual(llgn.current.tweet, "1")

    @weight(3)
    def test_eval_go_prev(self):
        llgp = CDLL()
        for i in range(5):
            llgp.prepend(str(i),"")
        self.assertEqual(llgp.current.time, "4")
        llgp.go_prev()
        self.assertEqual(llgp.current.time, "0")

    @weight(3)
    def test_eval_go_first(self):
        llgf = CDLL()
        for i in range(20):
            llgf.append(str(i),"")
        for i in range(10):
            llgf.go_next()
        self.assertEqual(llgf.current.time, "10")
        llgf.go_first()
        self.assertEqual(llgf.current.time, "0")

    @weight(3)
    def test_eval_go_last(self):
        llgl = CDLL()
        for i in range(50):
            llgl.prepend("",str(i))
        for i in range(27):
            llgl.go_prev()
        self.assertEqual(llgl.current.tweet, "26")
        llgl.go_last()
        self.assertEqual(llgl.current.tweet, "0")

    @weight(5)
    def test_eval_skip(self):
        lls = CDLL()
        for i in range(40):
            if i%3 == 0:
                lls.append("Hello","")
            elif i%3 == 1:
                lls.append("There","")
            else:
                lls.append("Again","")
        self.assertEqual(lls.current.time, "Hello")
        lls.skip(50)
        self.assertEqual(lls.current.time, "There")

    @weight(3)
    def test_eval_print_cur(self):
        llpc = CDLL()
        studout = io.StringIO()
        origout = sys.stdout

        llpc.append("This Is","The Test")

        sys.stdout = studout
        llpc.print_current()

        self.assertEqual(studout.getvalue(),"This Is\nThe Test\n")
        sys.stdout = origout