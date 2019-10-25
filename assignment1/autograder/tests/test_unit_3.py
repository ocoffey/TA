import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from assignment1 import bucketsort
import csv

class TestBucketSort(unittest.TestCase):
    @weight(5)
    def test_bucket_empty(self):
        # should print 10 empty buckets both times
        # store their (presumably sorted) output list
        # also gives us bucket1.txt and bucket2.txt
        retval = bucketsort([],10)
        # open and store contents of bucket1.txt
        with open('bucket1.txt', 'r') as outp1:
            ubuckets1 = outp1.read()
        # open and store contents of bucket2.txt
        with open('bucket2.txt', 'r') as outp2:
            sbuckets2 = outp2.read()
        
        # open the correct outputs to test against it
        with open('tests/buckettests/emptybucket1.txt', 'r') as test1:
            testubuckets1 = test1.read()
        with open('tests/buckettests/emptybucket2.txt', 'r') as test2:
            testsbuckets2 = test2.read()
        try:
            # test their unsorted buckets
            self.assertEqual(ubuckets1,testubuckets1)
        except AssertionError:
            assert False, "Unsorted buckets not equal"
        try:
            # test their sorted buckets
            self.assertEqual(sbuckets2,testsbuckets2)
        except AssertionError:
            assert False, "Sorted buckets not equal"
        try:
            # test their return value
            self.assertListEqual(retval,[])
        except AssertionError:
            assert False, "Return values not equal"

    @weight(5)
    def test_bucket_repeated(self):
        inplist = [0.2, 0.2, 0.21, 0.19, 0.1, 0.3, 0.99, 0.2]
        retval = bucketsort(inplist, 10)
        # student outputs
        with open('bucket1.txt', 'r') as outp1:
            ubuckets1 = outp1.read()
        with open('bucket2.txt', 'r') as outp2:
            sbuckets2 = outp2.read()
        # test outputs
        with open('tests/buckettests/repbucket1.txt', 'r') as test1:
            testubuckets1 = test1.read()
        with open('tests/buckettests/repbucket2.txt', 'r') as test2:
            testsbuckets2 = test2.read() 
        try:
            self.assertEqual(ubuckets1,testubuckets1)
        except AssertionError:
            assert False, "Unsorted buckets not equal"        
        try:
            self.assertEqual(sbuckets2,testsbuckets2)
        except AssertionError:
            assert False, "Sorted buckets not equal"
        try:
            self.assertListEqual(retval,[0.1, 0.19, 0.2, 0.2, 0.2, 0.21, 0.3, 0.99])
        except AssertionError:
            assert False, "Return values not equal"

    @weight(5)
    def test_bucket_long(self):
        inplist = [0.96, 0.95, 0.91, 0.90, 0.86, 0.85, 0.81, 0.80, 0.76, 0.75, 0.71, 0.70, 0.66, 0.65, 0.61, 0.60, 0.56, 0.55, 0.51, 0.50]
        retval = bucketsort(inplist, 20)
        # student outputs
        with open('bucket1.txt', 'r') as outp1:
            ubuckets1 = outp1.read()
        with open('bucket2.txt', 'r') as outp2:
            sbuckets2 = outp2.read()
        # test outputs
        with open('tests/buckettests/longbucket1.txt', 'r') as test1:
            testubuckets1 = test1.read()
        with open('tests/buckettests/longbucket2.txt', 'r') as test2:
            testsbuckets2 = test2.read()
        try:
            self.assertEqual(ubuckets1,testubuckets1)
        except AssertionError:
            assert False, "Unsorted buckets not equal"  
        try:
            self.assertEqual(sbuckets2,testsbuckets2)
        except AssertionError:
            assert False, "Sorted buckets not equal"
        try:
            self.assertListEqual(retval,[0.5, 0.51, 0.55, 0.56, 0.6, 0.61, 0.65, 0.66, 0.7, 0.71, 0.75, 0.76, 0.8, 0.81, 0.85, 0.86, 0.9, 0.91, 0.95, 0.96])
        except AssertionError:
            assert False, "Return values not equal"


    @weight(5)
    def test_bucket_many(self):
        inplist = [0.31, 0.72, 0.612, 0.61]
        retval = bucketsort(inplist, 100)
        # student outputs
        with open('bucket1.txt', 'r') as outp1:
            ubuckets1 = outp1.read()
        with open('bucket2.txt', 'r') as outp2:
            sbuckets2 = outp2.read()
        # test outputs
        with open('tests/buckettests/manybucket1.txt', 'r') as test1:
            testubuckets1 = test1.read()
        with open('tests/buckettests/manybucket2.txt', 'r') as test2:
            testsbuckets2 = test2.read()
        try:
            self.assertEqual(ubuckets1,testubuckets1)
        except AssertionError:
            assert False, "Unsorted buckets not equal"
        try:
            self.assertEqual(sbuckets2,testsbuckets2)
        except AssertionError:
            assert False, "Sorted buckets not equal"
        try:
            self.assertListEqual(retval,[0.31,0.61,0.612,0.72])
        except AssertionError:
            assert False, "Return values not equal"


    @weight(5)
    def test_bucket_big2(self):
        # big list, so stored it as a csv
        with open('tests/buckettests/randlist.csv','r') as randinp:
            # open the document object
            cinplist = csv.reader(randinp, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
            """
            it opens as a 2d list with one element, that element being
            the full list (for a reason completely beyond me)
            """
            # convert it to a list
            inplist = list(*cinplist)

        # get (presumably) sorted list
        retval = bucketsort(inplist,1000)

        # student outputs
        with open('bucket1.txt', 'r') as outp1:
            ubuckets1 = outp1.read()
        with open('bucket2.txt', 'r') as outp2:
            sbuckets2 = outp2.read()
        # test outputs
        with open('tests/buckettests/big2bucket1.txt', 'r') as test1:
            testubuckets1 = test1.read()
        with open('tests/buckettests/big2bucket2.txt', 'r') as test2:
            testsbuckets2 = test2.read()
        # also stored return value as csv
        with open('tests/buckettests/randsortlist.csv', 'r') as sortedret:
            cretlist = csv.reader(sortedret, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
            retlist = list(*cretlist)
        try:
            self.assertEqual(ubuckets1,testubuckets1)
        except AssertionError:
            assert False, "Unsorted buckets not equal"        
        try:
            self.assertEqual(sbuckets2,testsbuckets2)
        except AssertionError:
            assert False, "Sorted buckets not equal"
        try:
            self.assertListEqual(retval,retlist)
        except AssertionError:
            assert False, "Return values not equal"