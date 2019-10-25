import unittest
from gradescope_utils.autograder_utils.decorators import weight
from assignment1 import columnsort

class TestTweetReaderBest(unittest.TestCase):
    """
    20 Points
    Error handling for not being passed a filename in command line args
    Error handling for not being able to open the file
    Handling 's' being input without additional word
    S handling not finding the word
    Skip for tweets???
    """

    """
    For Templating

    @weight(5)
    def test_column_ex(self):

        self.assertListEqual(retval,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])
        self.assertEqual(fcolumn,testfcolumn)
        self.assertEqual(socolumn,testsocolumn)
        self.assertEqual(tcolumn,testtcolumn)
        self.assertEqual(shcolumn,testshcolumn)
    """
    