import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from assignment1 import columnsort

class TestColumnsort(unittest.TestCase):
    
    @weight(5)
    def test_column_ex(self):
        inplist = [10, 14, 5, 8, 7, 17, 12, 1, 6, 16, 9, 11, 4, 15, 2, 18, 3, 13]
        retval = columnsort(inplist, 18)
        # student outputs
        with open('column1.txt', 'r') as outp1:
            fcolumn = outp1.read()
        with open('column2.txt', 'r') as outp2:
            socolumn = outp2.read()
        with open('column3.txt', 'r') as outp3:
            tcolumn = outp3.read()
        with open('column4.txt', 'r') as outp4:
            shcolumn = outp4.read()
        # test outputs
        with open('tests/columntests/Example/excolumn1.txt', 'r') as test1:
            testfcolumn = test1.read()
        with open('tests/columntests/Example/excolumn2.txt', 'r') as test2:
            testsocolumn = test2.read()
        with open('tests/columntests/Example/excolumn3.txt', 'r') as test3:
            testtcolumn = test3.read()
        with open('tests/columntests/Example/excolumn4.txt', 'r') as test4:
            testshcolumn = test4.read()
        try:
            self.assertEqual(fcolumn,testfcolumn)
        except AssertionError:
            assert False, "Step 0 not equal"

        try:
            self.assertEqual(socolumn,testsocolumn)
        except AssertionError:
            assert False, "Step 1 not equal"

        try:
            self.assertEqual(tcolumn,testtcolumn)
        except AssertionError:
            assert False, "Step 2 not equal"

        try:
            self.assertEqual(shcolumn,testshcolumn)
        except AssertionError:
            assert False, "Step 6 not equal"

        try:
            self.assertListEqual(retval,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
        except AssertionError:
            assert False, "Return values not equal"
    
    @weight(5)
    def test_column_some(self):
        inplist = [84, 50, 14, 95, 73, 33, 61, 70, 51, 75, 17, 25, 56, 91, 7, 21, 28, 16, 67, 90, 5, 10, 4, 23, 18, 34, 77, 46, 88, 47, 15, 9, 1, 59, 44, 2]
        retval = columnsort(inplist, 36)
        # student outputs
        with open('column1.txt', 'r') as outp1:
            fcolumn = outp1.read()
        with open('column2.txt', 'r') as outp2:
            socolumn = outp2.read()
        with open('column3.txt', 'r') as outp3:
            tcolumn = outp3.read()
        with open('column4.txt', 'r') as outp4:
            shcolumn = outp4.read()
        # test outputs
        with open('tests/columntests/Some/socolumn1.txt', 'r') as test1:
            testfcolumn = test1.read()
        with open('tests/columntests/Some/socolumn2.txt', 'r') as test2:
            testsocolumn = test2.read()
        with open('tests/columntests/Some/socolumn3.txt', 'r') as test3:
            testtcolumn = test3.read()
        with open('tests/columntests/Some/socolumn4.txt', 'r') as test4:
            testshcolumn = test4.read()
        try:
            self.assertEqual(fcolumn,testfcolumn)
        except AssertionError:
            assert False, "Step 0 not equal"

        try:
            self.assertEqual(socolumn,testsocolumn)
        except AssertionError:
            assert False, "Step 1 not equal"

        try:
            self.assertEqual(tcolumn,testtcolumn)
        except AssertionError:
            assert False, "Step 2 not equal"

        try:
            self.assertEqual(shcolumn,testshcolumn)
        except AssertionError:
            assert False, "Step 6 not equal"

        try:
            self.assertListEqual(retval,[1, 2, 4, 5, 7, 9, 10, 14, 15, 16, 17, 18, 21, 23, 25, 28, 33, 34, 44, 46, 47, 50, 51, 56, 59, 61, 67, 70, 73, 75, 77, 84, 88, 90, 91, 95])
        except AssertionError:
            assert False, "Return values not equal"
    
    @weight(5)
    def test_column_more(self):
        inplist = [22, 78, 24, 57, 8, 60, 9, 44, 53, 68, 96, 40, 46, 95, 80, 36, 42, 41, 18, 72, 90, 58, 97, 84, 89, 55, 56, 38, 19, 85, 74, 99, 92, 82, 23, 21, 31, 27, 66, 14, 61, 71, 49, 35, 5, 2, 30, 45]
        retval = columnsort(inplist, 48)
        # student outputs
        with open('column1.txt', 'r') as outp1:
            fcolumn = outp1.read()
        with open('column2.txt', 'r') as outp2:
            socolumn = outp2.read()
        with open('column3.txt', 'r') as outp3:
            tcolumn = outp3.read()
        with open('column4.txt', 'r') as outp4:
            shcolumn = outp4.read()
        # test outputs
        with open('tests/columntests/More/morcolumn1.txt', 'r') as test1:
            testfcolumn = test1.read()
        with open('tests/columntests/More/morcolumn2.txt', 'r') as test2:
            testsocolumn = test2.read()
        with open('tests/columntests/More/morcolumn3.txt', 'r') as test3:
            testtcolumn = test3.read()
        with open('tests/columntests/More/morcolumn4.txt', 'r') as test4:
            testshcolumn = test4.read()
        try:
            self.assertEqual(fcolumn,testfcolumn)
        except AssertionError:
            assert False, "Step 0 not equal"

        try:
            self.assertEqual(socolumn,testsocolumn)
        except AssertionError:
            assert False, "Step 1 not equal"

        try:
            self.assertEqual(tcolumn,testtcolumn)
        except AssertionError:
            assert False, "Step 2 not equal"

        try:
            self.assertEqual(shcolumn,testshcolumn)
        except AssertionError:
            assert False, "Step 6 not equal"
    
        try:
            self.assertListEqual(retval,[2, 5, 8, 9, 14, 18, 19, 21, 22, 23, 24, 27, 30, 31, 35, 36, 38, 40, 41, 42, 44, 45, 46, 49, 53, 55, 56, 57, 58, 60, 61, 66, 68, 71, 72, 74, 78, 80, 82, 84, 85, 89, 90, 92, 95, 96, 97, 99])
        except AssertionError:
            assert False, "Return values not equal"

    @weight(5)
    def test_column_most(self):
        inplist = [885, 119, 979, 168, 29, 704, 939, 805, 223, 740, 325, 331, 778, 60, 328, 571, 432, 621, 316, 803, 369, 697, 775, 605, 942, 84, 103, 132, 272, 88, 460, 343, 906, 811, 461, 963, 820, 185, 288, 670, 498, 147, 19, 188, 392, 590, 496, 960, 538, 580, 597, 356, 44, 335, 238, 508, 557, 632, 526, 794, 677, 338, 628, 166, 907, 416, 215, 662, 630, 126, 650, 512]
        retval = columnsort(inplist, 72)
        # student outputs
        with open('column1.txt', 'r') as outp1:
            fcolumn = outp1.read()
        with open('column2.txt', 'r') as outp2:
            socolumn = outp2.read()
        with open('column3.txt', 'r') as outp3:
            tcolumn = outp3.read()
        with open('column4.txt', 'r') as outp4:
            shcolumn = outp4.read()
        # test outputs
        with open('tests/columntests/Most/moscolumn1.txt', 'r') as test1:
            testfcolumn = test1.read()
        with open('tests/columntests/Most/moscolumn2.txt', 'r') as test2:
            testsocolumn = test2.read()
        with open('tests/columntests/Most/moscolumn3.txt', 'r') as test3:
            testtcolumn = test3.read()
        with open('tests/columntests/Most/moscolumn4.txt', 'r') as test4:
            testshcolumn = test4.read()
        try:
            self.assertEqual(fcolumn,testfcolumn)
        except AssertionError:
            assert False, "Step 0 not equal"

        try:
            self.assertEqual(socolumn,testsocolumn)
        except AssertionError:
            assert False, "Step 1 not equal"

        try:
            self.assertEqual(tcolumn,testtcolumn)
        except AssertionError:
            assert False, "Step 2 not equal"

        try:
            self.assertEqual(shcolumn,testshcolumn)
        except AssertionError:
            assert False, "Step 6 not equal"

        try:
            self.assertListEqual(retval,[19, 29, 44, 60, 84, 88, 103, 119, 126, 132, 147, 166, 168, 185, 188, 215, 223, 238, 272, 288, 316, 325, 328, 331, 335, 338, 343, 356, 369, 392, 416, 432, 460, 461, 496, 498, 508, 512, 526, 538, 557, 571, 580, 590, 597, 605, 621, 628, 630, 632, 650, 662, 670, 677, 697, 704, 740, 775, 778, 794, 803, 805, 811, 820, 885, 906, 907, 939, 942, 960, 963, 979])
        except AssertionError:
            assert False, "Return values not equal"
    
    @weight(5)
    def test_column_reps(self):
        inplist = [1, 7, 5, 9, 8, 0, 1, 7, 5, 9, 8, 0, 1, 7, 5, 9, 8, 0]
        retval = columnsort(inplist, 18)
        # student outputs
        with open('column1.txt', 'r') as outp1:
            fcolumn = outp1.read()
        with open('column2.txt', 'r') as outp2:
            socolumn = outp2.read()
        with open('column3.txt', 'r') as outp3:
            tcolumn = outp3.read()
        with open('column4.txt', 'r') as outp4:
            shcolumn = outp4.read()
        # test outputs
        with open('tests/columntests/Reps/repcolumn1.txt', 'r') as test1:
            testfcolumn = test1.read()
        with open('tests/columntests/Reps/repcolumn2.txt', 'r') as test2:
            testsocolumn = test2.read()
        with open('tests/columntests/Reps/repcolumn3.txt', 'r') as test3:
            testtcolumn = test3.read()
        with open('tests/columntests/Reps/repcolumn4.txt', 'r') as test4:
            testshcolumn = test4.read()
        try:
            self.assertEqual(fcolumn,testfcolumn)
        except AssertionError:
            assert False, "Step 0 not equal"

        try:
            self.assertEqual(socolumn,testsocolumn)
        except AssertionError:
            assert False, "Step 1 not equal"

        try:
            self.assertEqual(tcolumn,testtcolumn)
        except AssertionError:
            assert False, "Step 2 not equal"

        try:
            self.assertEqual(shcolumn,testshcolumn)
        except AssertionError:
            assert False, "Step 6 not equal"

        try:
            self.assertListEqual(retval,[0, 0, 0, 1, 1, 1, 5, 5, 5, 7, 7, 7, 8, 8, 8, 9, 9, 9])
        except AssertionError:
            assert False, "Return values not equal"
    
    @weight(5)
    def test_column_nega(self):
        inplist = [98, 73, -89, -74, 61, -85, 44, 26, -41, -3, 20, -53, 67, 79, 5, 65, 2, 70, 83, 3, -51, 86, 92, 27, 12, 59, -94, -28, -37, 84, -18, 21, -71, 81, 51, 46, 49, -8, -93, -2, 31, -81, -24, 0, -19, -83, -65, 54, 8, 47, -12, 28, -7, 69, -60, -80, 43, -59, 53, -38, -32, -15, 34, -17, -55, -67, 19, 80, 90, -14, -76, -66]
        retval = columnsort(inplist, 72)
        # student outputs
        with open('column1.txt', 'r') as outp1:
            fcolumn = outp1.read()
        with open('column2.txt', 'r') as outp2:
            socolumn = outp2.read()
        with open('column3.txt', 'r') as outp3:
            tcolumn = outp3.read()
        with open('column4.txt', 'r') as outp4:
            shcolumn = outp4.read()
        # test outputs
        with open('tests/columntests/Nega/negcolumn1.txt', 'r') as test1:
            testfcolumn = test1.read()
        with open('tests/columntests/Nega/negcolumn2.txt', 'r') as test2:
            testsocolumn = test2.read()
        with open('tests/columntests/Nega/negcolumn3.txt', 'r') as test3:
            testtcolumn = test3.read()
        with open('tests/columntests/Nega/negcolumn4.txt', 'r') as test4:
            testshcolumn = test4.read()
        try:
            self.assertEqual(fcolumn,testfcolumn)
        except AssertionError:
            assert False, "Step 0 not equal"

        try:
            self.assertEqual(socolumn,testsocolumn)
        except AssertionError:
            assert False, "Step 1 not equal"

        try:
            self.assertEqual(tcolumn,testtcolumn)
        except AssertionError:
            assert False, "Step 2 not equal"

        try:
            self.assertEqual(shcolumn,testshcolumn)
        except AssertionError:
            assert False, "Step 6 not equal"

        try:
            self.assertListEqual(retval,[-94, -93, -89, -85, -83, -81, -80, -76, -74, -71, -67, -66, -65, -60, -59, -55, -53, -51, -41, -38, -37, -32, -28, -24, -19, -18, -17, -15, -14, -12, -8, -7, -3, -2, 0, 2, 3, 5, 8, 12, 19, 20, 21, 26, 27, 28, 31, 34, 43, 44, 46, 47, 49, 51, 53, 54, 59, 61, 65, 67, 69, 70, 73, 79, 80, 81, 83, 84, 86, 90, 92, 98])
        except AssertionError:
            assert False, "Return values not equal"