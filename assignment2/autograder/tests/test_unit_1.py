import unittest
from gradescope_utils.autograder_utils.decorators import weight
from assignment2 import CDLL, CDLLNode
import io
import sys
import re

class TestLinkedList(unittest.TestCase):
    """Testing CDLL - 30 points"""

    def insert(self, myList: CDLL, time: str, tweet: str = "") -> None:
        # makes a new node
        myNode = CDLLNode(time, tweet)
        # manually attaches it to their list
        if myList.numnodes == 0:
            myList.head = myList.current = myNode
            myNode.next_node = myNode.prev_node = myNode
        else:
            myNode.next_node = myList.current
            myNode.prev_node = myList.current.prev_node
            myList.current.prev_node.next_node = myNode
            myList.current.prev_node = myNode
            if myList.head.time > myNode.time:
                myList.head = myList.current = myNode

        myList.numnodes += 1

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
            self.insert(llgn,"00:00:0" + str(i))
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
            self.insert(llgp,"00:00:0" + str(i))
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
            self.insert(llgf,"00:00:0" + str(i))
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
            self.insert(llgl,"00:00:0" + str(i))
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
            self.insert(lls,"00:00:0" + str(i))
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

        self.insert(llpc,"This Is","The Test")

        sys.stdout = studout
        llpc.print_current()
        try:
            self.assertEqual(re.sub(r"([\n])", r"", studout.getvalue()),"This IsThe Test")
        except AssertionError:
            assert False, "Print Current Not Equal"
        sys.stdout = origout