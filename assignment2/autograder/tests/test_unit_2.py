import unittest
from gradescope_utils.autograder_utils.decorators import weight




class TestTweetReader(unittest.TestCase):
    """Test Tweet Reader - 50 points"""

    """
    20 Points
    Skip in small time
    ?????Skip in smaller time?? (go_next or go_prev based on numnodes/2,
    and how big n % numnodes is)?????
    Go Last in constant time
    Append in constant time
    """

    """
    Used for templating
    
    @weight(5)
    def test_eval_altbubsorted(self):
        self.assertEqual(alt_bubblesort([1, 2, 3, 4, 5, 6, 7, 8], 8), [1, 2, 3, 4, 5, 6, 7, 8])
    """