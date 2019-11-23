import unittest
from gradescope_utils.autograder_utils.decorators import weight
from assignment2 import CDLL, CDLLNode
import io
import sys

class TestLinkedList(unittest.TestCase):
    """Testing CDLL - 30 points"""
    @weight(10)
    def test_eval_insert(self): #test if for empty list, insert starts at head
        llpre = CDLL()
        for i in range(3):
            llpre.insert(str(i), "")
        try:
            self.assertEqual(llpre.head.time, "0")
        except AssertionError:
            assert False, "Head Not Equal"

    @weight(3)
    def test_eval_go_next(self):
        llgn = CDLL()
        for i in range(2):
            llgn.insert("00:00:0"+str(i), "")
        llgn.current = llgn.head
        try:
            self.assertEqual(llgn.current.time, "00:00:00")
        except AssertionError:
            assert False, "Head Not Equal"
        llgn.go_next()
        try:
            self.assertEqual(llgn.current.time, "00:00:01")
        except AssertionError:
            assert False, "Next Element Not Equal"

    @weight(3)
    def test_eval_go_prev(self):
        llgp = CDLL()
        for i in range(5):
            llgp.insert("00:00:0"+str(i), "")
        llgp.current = llgp.head
        try:
            self.assertEqual(llgp.current.time, "00:00:00")
        except AssertionError:
            assert False, "Head Not Equal"
        llgp.go_prev()
        try:
            self.assertEqual(llgp.current.time, "00:00:04")
        except AssertionError:
            assert False, "Previous Element Not Equal"
        
        

    @weight(3)
    def test_eval_go_first(self):
        llgf = CDLL()
        for i in range(10):
            llgf.insert("00:00:0" + str(i), "")
        for i in range(5):
            llgf.go_next()
        llgf.go_first()
        try:
            self.assertEqual(llgf.current.time, "00:00:00")
        except AssertionError:
            assert False, "Head Not At Lowest Element"

    @weight(3)
    def test_eval_go_last(self):
        llgl = CDLL()
        for i in range(10):
            llgl.insert("00:00:0" + str(i), "")
        for i in range(5):
            llgl.go_prev()
        llgl.go_last()
        try:
            self.assertEqual(llgl.current.time, "00:00:09")
        except AssertionError:
            assert False, "Tail Not At Highest Element"

    @weight(5)
    def test_eval_skip(self):
        lls = CDLL()
        for i in range(10):
            lls.insert("00:00:0" + str(i), "")
        lls.go_first()
        try:
            self.assertEqual(lls.current.time, "00:00:00")
        except AssertionError:
            assert False, "Head Not Equal"
        lls.skip(34)
        try:
            self.assertEqual(lls.current.time, "00:00:04")
        except AssertionError:
            assert False, "Node Skip Not Equal"

    @weight(3)
    def test_eval_print_cur(self):
        llpc = CDLL()
        studout = io.StringIO()
        origout = sys.stdout

        llpc.insert("This Is","The Test")

        sys.stdout = studout
        llpc.print_current()
        try:
            self.assertEqual(studout.getvalue(),"This Is\nThe Test\n")
        except AssertionError:
            assert False, "Print Current Not Equal"
        sys.stdout = origout