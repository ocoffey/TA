import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from assignment1 import alt_bubblesort, switch_bubblesort

class TestBubSorts(unittest.TestCase):
    
    @weight(5)
    def test_eval_altbubsorted(self):
        try:
            self.assertEqual(alt_bubblesort([1, 2, 3, 4, 5, 6, 7, 8], 8), [[1, 2, 3, 4, 5, 6, 7, 8],
                                                                           [1, 2, 3, 4, 5, 6, 7, 8],
                                                                           [1, 2, 3, 4, 5, 6, 7, 8],
                                                                           [1, 2, 3, 4, 5, 6, 7, 8],
                                                                           [1, 2, 3, 4, 5, 6, 7, 8],
                                                                           [1, 2, 3, 4, 5, 6, 7, 8],
                                                                           [1, 2, 3, 4, 5, 6, 7, 8],
                                                                           [1, 2, 3, 4, 5, 6, 7, 8],
                                                                           [1, 2, 3, 4, 5, 6, 7, 8]])
        except AssertionError:
            assert False, "Lists not equal"

    @weight(5)
    def test_eval_altbub_reversesort(self):
        try:
            self.assertEqual(alt_bubblesort([5, 4, 3, 2, 1], 5), [[5, 4, 3, 2, 1],
                                                                  [1, 5, 4, 3, 2],
                                                                  [1, 2, 5, 4, 3],
                                                                  [1, 2, 3, 5, 4],
                                                                  [1, 2, 3, 4, 5],
                                                                  [1, 2, 3, 4, 5]])
        except AssertionError:
            assert False, "Lists not equal"

    @weight(5)
    def test_eval_altbub_randsort(self):
        try:
            self.assertEqual(alt_bubblesort([6, 7, 3, 9, 4, 8, 1, 10], 8), [[6, 7, 3, 9, 4, 8, 1, 10],
                                                                            [1, 6, 7, 3, 9, 4, 8, 10],
                                                                            [1, 3, 6, 7, 4, 9, 8, 10],
                                                                            [1, 3, 4, 6, 7, 8, 9, 10],
                                                                            [1, 3, 4, 6, 7, 8, 9, 10],
                                                                            [1, 3, 4, 6, 7, 8, 9, 10],
                                                                            [1, 3, 4, 6, 7, 8, 9, 10],
                                                                            [1, 3, 4, 6, 7, 8, 9, 10],
                                                                            [1, 3, 4, 6, 7, 8, 9, 10]])
        except AssertionError:
            assert False, "Lists not equal"

    @weight(5)
    def test_eval_altbub_partsort(self):
        try:
            self.assertEqual(alt_bubblesort([1, 2, 3, 4, 8, 6, 7], 7), [[1, 2, 3, 4, 8, 6, 7],
                                                                        [1, 2, 3, 4, 6, 8, 7],
                                                                        [1, 2, 3, 4, 6, 7, 8],
                                                                        [1, 2, 3, 4, 6, 7, 8],
                                                                        [1, 2, 3, 4, 6, 7, 8],
                                                                        [1, 2, 3, 4, 6, 7, 8],
                                                                        [1, 2, 3, 4, 6, 7, 8],
                                                                        [1, 2, 3, 4, 6, 7, 8]])
        except AssertionError:
            assert False, "Lists not equal"

    @weight(5)
    def test_eval_altbub_empty(self):
        try:
            self.assertEqual(alt_bubblesort([], 0), [[]])
        except AssertionError:
            assert False, "Lists not equal"

class TestSwitchBubSort(unittest.TestCase):
    @weight(5)
    def test_empty(self):
        try:
            self.assertEqual(switch_bubblesort([], 0), [[]])
        except AssertionError:
            assert False, "Lists not equal"

    @weight(5)
    def test_sorted(self):
        try:
            self.assertEqual(switch_bubblesort([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                                                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                                                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                                                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                                                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                                                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                                                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                                                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                                                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                                                 [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                                                                 [1, 2, 3, 4, 5, 6, 7, 8, 9]])
        except AssertionError:
            assert False, "Lists not equal"

    @weight(5)
    def test_reverse(self):
        try:
            self.assertEqual(switch_bubblesort([5, 4, 3, 2, 1], 5), [[5, 4, 3, 2, 1],
                                                                     [1, 5, 4, 3, 2],
                                                                     [1, 4, 3, 2, 5],
                                                                     [1, 2, 4, 3, 5],
                                                                     [1, 2, 3, 4, 5],
                                                                     [1, 2, 3, 4, 5],
                                                                     [1, 2, 3, 4, 5]])
        except AssertionError:
            assert False, "Lists not equal"

    @weight(5)
    def test_unsorted(self):
        try:
            self.assertEqual(switch_bubblesort([5, 7, 6, 2, 1], 5), [[5, 7, 6, 2, 1],
                                                                     [1, 5, 7, 6, 2],
                                                                     [1, 5, 6, 2, 7],
                                                                     [1, 2, 5, 6, 7],
                                                                     [1, 2, 5, 6, 7],
                                                                     [1, 2, 5, 6, 7],
                                                                     [1, 2, 5, 6, 7]])
        except AssertionError:
            assert False, "Lists not equal"

    @weight(5)
    def test_partsort(self):
        try:
            self.assertEqual(switch_bubblesort([1, 2, 3, 9, 4, 2], 6), [[1, 2, 3, 9, 4, 2],
                                                                        [1, 2, 2, 3, 9, 4],
                                                                        [1, 2, 2, 3, 4, 9],
                                                                        [1, 2, 2, 3, 4, 9],
                                                                        [1, 2, 2, 3, 4, 9],
                                                                        [1, 2, 2, 3, 4, 9],
                                                                        [1, 2, 2, 3, 4, 9]])
        except AssertionError:
            assert False, "Lists not equal"