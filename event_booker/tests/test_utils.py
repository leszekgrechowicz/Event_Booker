from ..utils import list_divider
from django.test import TestCase


class ListDividerFunctionTest(TestCase):
    """Test list_divider function that divides given list into n long chunks"""

    def setUp(self) -> None:
        self.l1 = [x for x in range(18)]
        self.l2 = [x for x in range(35)]

    def test_six_chunks_three_items_long(self):
        test_list = list_divider(self.l1, 3)
        self.assertEqual(len(test_list), 6)
        self.assertEqual(len(test_list[0]), 3)
        self.assertNotEqual(len(test_list[-1]), 2)

    def test_false_seven_chunks_from_the_list_that_can_give_only_six(self):
        test_list = list_divider(self.l1, 3)
        self.assertNotEqual(len(test_list), 7)
        self.assertNotEqual(len(test_list[1]), 4)

    def test_chunks_three_items_long_last_two_items_long(self):
        test_list = list_divider(self.l2, 3)
        self.assertEqual(len(test_list), 12)
        self.assertEqual(len(test_list[-1]), 2)
