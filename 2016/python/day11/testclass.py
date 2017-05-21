from day11 import is_state_valid, fill_empty_floors, move_items_and_sort
import unittest

class TestDay11(unittest.TestCase):

	def test_state_is_valid(self):

		self.assertEqual(is_state_valid([[],[],[],[]]), True)
		self.assertEqual(is_state_valid([['HG'],[],[],[]]), True)
		self.assertEqual(is_state_valid([['HG'],['HM'],[],[]]), True)
		self.assertEqual(is_state_valid([['HG'],['HM'],['LG'],[]]), True)
		self.assertEqual(is_state_valid([['HG'],['HM'],['LG'],['LM']]), True)
		self.assertEqual(is_state_valid([['HG', 'HM'],[],['LG'],['LM']]), True)
		self.assertEqual(is_state_valid([['HG', 'HM', 'LG'],[],[],['LM']]), True)
		self.assertEqual(is_state_valid([['HG', 'HM', 'LM'],[],[],['LG']]), False)
		self.assertEqual(is_state_valid([['HG', 'HM', 'LM', 'LG'],[],[],[]]), True)
		self.assertEqual(is_state_valid([['HM', 'LG'],['HG'],[],['LM']]), False)

	def test_fill_empty_floors(self):

		self.assertEqual(fill_empty_floors([[],[],[],[]]), [[],[],[],[]])
		self.assertEqual(fill_empty_floors([['HM'],['HG'],['LM'],['LG']]), [['HM'],['HG'],['LM'],['LG']])
		self.assertEqual(fill_empty_floors([[],None,[],None]), [[],[],[],[]])
		self.assertEqual(fill_empty_floors([[],['HM'],[],None]), [[],['HM'],[],[]])

	def test_move_items(self):

		state = [['HM','LM'],['HG'],['LG'],[]]
		move_items_and_sort(state, ['HM'], 0, 1)
		self.assertEqual(state, [['LM'],['HG','HM'],['LG'],[]])

		state = [['LM'],['HG','HM'],['LG'],[]]
		move_items_and_sort(state, ['HG','HM'], 1, 2)
		self.assertEqual(state, [['LM'],[],['HG','HM','LG'],[]])

		state = [['LM'],[],['HG','HM','LG'],[]]
		move_items_and_sort(state, ['HM'], 2, 1)
		self.assertEqual(state, [['LM'],['HM'],['HG','LG'],[]])

		state = [['LM'],['HM'],['HG','LG'],[]]
		move_items_and_sort(state, ['HM'], 1, 0)
		self.assertEqual(state, [['HM','LM'],[],['HG','LG'],[]])

		state = [['HM','LM'],[],['HG','LG'],[]]
		move_items_and_sort(state, ['HM','LM'], 0, 1)
		self.assertEqual(state, [[],['HM','LM'],['HG','LG'],[]])

		state = [[],['HM','LM'],['HG','LG'],[]]
		move_items_and_sort(state, ['HM','LM'], 1, 2)
		self.assertEqual(state, [[],[],['HG','HM','LG','LM'],[]])


if __name__ == '__main__':
	unittest.main()
