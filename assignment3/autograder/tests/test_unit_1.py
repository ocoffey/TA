<<<<<<< HEAD
import unittest
from gradescope_utils.autograder_utils.decorators import weight
from assignment2 import CDLL, CDLLNode
import io
import sys

class TestLinkedList(unittest.TestCase):
    """Testing CDLL - 30 points"""
    @weight(5)
    def test_eval_insert_head(self): #test if for empty list, insert starts at head
        llpre = CDLL()
        for i in range(3):
            llpre.insert(str("00:00:00"), "")
        llpre.current = llpre.current.next_node
        self.assertEqual(llpre.current.time, "00:00:00")

    @weight(5)
    def test_evel_insert_list(self): #test list is in order
        llpre = CDLL()
        for i in range(10):
            llpre.insert("00:00:0"+str(i), "")
        sout = []
        for i in range(10):
            sout.append(llpre.current.time)
            llpre.go_next()

        self.assertListEqual(sout, ['00:00:09', '00:00:08', '00:00:07', '00:00:06', '00:00:05', '00:00:04', '00:00:03', '00:00:02', '00:00:01', '00:00:00'])


    @weight(3)
    def test_eval_go_next(self):
        llgn = CDLL()
        for i in range(2):
            llgn.insert("00:00:0"+str(i), "")
        self.assertEqual(llgn.current.time, "00:00:01")
        llgn.go_next()
        self.assertEqual(llgn.current.time, "00:00:00")

    @weight(3)
    def test_eval_go_prev(self):
        llgp = CDLL()
        for i in range(5):
            llgp.insert("00:00:0"+str(i), "")
        self.assertEqual(llgp.current.time, "00:00:04")
        llgp.go_prev()
        self.assertEqual(llgp.current.time, "00:00:00")

    @weight(3)
    def test_eval_go_first(self):
        llgf = CDLL()
        for i in range(10):
            llgf.insert("00:00:0" + str(i), "")
        for i in range(10):
            llgf.go_next()
        self.assertEqual(llgf.current.time, "00:00:09")
        llgf.go_first()
        self.assertEqual(llgf.current.time, "00:00:00")

    @weight(3)
    def test_eval_go_last(self):
        llgl = CDLL()
        for i in range(10):
            llgl.insert("00:00:0" + str(i), "")
        for i in range(10):
            llgl.go_prev()
        self.assertEqual(llgl.current.time, "00:00:09")
        llgl.go_last()
        self.assertEqual(llgl.current.time, "00:00:01")

    @weight(5)
    def test_eval_skip(self):
        lls = CDLL()
        for i in range(10):
            lls.insert("00:00:0" + str(i), "")
        self.assertEqual(lls.current.time, "00:00:09")
        lls.skip(34)
        self.assertEqual(lls.current.time, "00:00:05")

    @weight(3)
    def test_eval_print_cur(self):
        llpc = CDLL()
        studout = io.StringIO()
        origout = sys.stdout

        llpc.insert("This Is","The Test")

        sys.stdout = studout
        llpc.print_current()

        self.assertEqual(studout.getvalue(),"This Is\nThe Test\n")
=======
import unittest
from gradescope_utils.autograder_utils.decorators import weight
from assignment2 import CDLL, CDLLNode
import io
import sys

class TestLinkedList(unittest.TestCase):
    """Testing CDLL - 30 points"""
    @weight(5)
    def test_eval_insert_head(self): #test if for empty list, insert starts at head
        llpre = CDLL()
        for i in range(3):
            llpre.insert(str("00:00:00"), "")
        llpre.current = llpre.current.next_node
        self.assertEqual(llpre.current.time, "00:00:00")

    @weight(5)
    def test_evel_insert_list(self): #test list is in order
        llpre = CDLL()
        for i in range(10):
            llpre.insert("00:00:0"+str(i), "")
        sout = []
        for i in range(10):
            sout.append(llpre.current.time)
            llpre.go_next()
        self.assertListEqual(sout, ['00:00:09', '00:00:08', '00:00:07', '00:00:06', '00:00:05', '00:00:04', '00:00:03', '00:00:02', '00:00:01', '00:00:00'])

    @weight(3)
    def test_eval_go_next(self):
        llgn = CDLL()
        for i in range(2):
            llgn.insert("00:00:0"+str(i), "")
        self.assertEqual(llgn.current.time, "00:00:01")
        llgn.go_next()
        self.assertEqual(llgn.current.time, "00:00:00")

    @weight(3)
    def test_eval_go_prev(self):
        llgp = CDLL()
        for i in range(5):
            llgp.insert("00:00:0"+str(i), "")
        self.assertEqual(llgp.current.time, "00:00:04")
        llgp.go_prev()
        self.assertEqual(llgp.current.time, "00:00:00")

    @weight(3)
    def test_eval_go_first(self):
        llgf = CDLL()
        for i in range(10):
            llgf.insert("00:00:0" + str(i), "")
        for i in range(10):
            llgf.go_next()
        self.assertEqual(llgf.current.time, "00:00:09")
        llgf.go_first()
        self.assertEqual(llgf.current.time, "00:00:00")

    @weight(3)
    def test_eval_go_last(self):
        llgl = CDLL()
        for i in range(10):
            llgl.insert("00:00:0" + str(i), "")
        for i in range(10):
            llgl.go_prev()
        self.assertEqual(llgl.current.time, "00:00:09")
        llgl.go_last()
        self.assertEqual(llgl.current.time, "00:00:01")

    @weight(5)
    def test_eval_skip(self):
        lls = CDLL()
        for i in range(10):
            lls.insert("00:00:0" + str(i), "")
        self.assertEqual(lls.current.time, "00:00:09")
        lls.skip(34)
        self.assertEqual(lls.current.time, "00:00:05")

    @weight(3)
    def test_eval_print_cur(self):
        llpc = CDLL()
        studout = io.StringIO()
        origout = sys.stdout

        llpc.insert("This Is","The Test")

        sys.stdout = studout
        llpc.print_current()

        self.assertEqual(studout.getvalue(),"This Is\nThe Test\n")
>>>>>>> 92b7776559c84c03734bb2a41ebc1f23d238bd5c
        sys.stdout = origout