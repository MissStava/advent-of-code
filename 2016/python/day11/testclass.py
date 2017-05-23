from day11 import *
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

	def test_state_seen_before(self):

		state = [['HM','LM'],['HG'],['LG'],[]]
		elevatorAt = 0
		seenStates = [([['HM','LM'],['HG'],['LG'],[]], 0)]
		self.assertEqual(state_seen_before(state, elevatorAt, seenStates), True)

		state = [['HM','LM'],['HG'],['LG'],[]]
		elevatorAt = 0
		seenStates = ([['LM'],['HG','HM'],['LG'],[]], 1)
		self.assertEqual(state_seen_before(state, elevatorAt, seenStates), False)

		state = [['HM','LM'],['HG'],['LG'],[]]
		elevatorAt = 1
		seenStates = ([['LM'],['HG','HM'],['LG'],[]], 2)
		self.assertEqual(state_seen_before(state, elevatorAt, seenStates), False)

	def test_add_seen_state(self):

		state = [['HM','LM'],['HG'],['LG'],[]]
		elevatorAt = 0
		seenStates = []
		add_seen_state(state, elevatorAt, seenStates)
		self.assertEqual(seenStates, [([['HM','LM'],['HG'],['LG'],[]], 0)])

		state = [['HM','LM'],['HG'],['LG'],[]]
		elevatorAt = 1
		seenStates = [([['HM','LM'],['HG'],['LG'],[]], 0)]
		add_seen_state(state, elevatorAt, seenStates)
		self.assertEqual(seenStates, [([['HM','LM'],['HG'],['LG'],[]], 0), ([['HM','LM'],['HG'],['LG'],[]], 1)])

	def test_add_states_to_try(self):

		state = [['LM'],['HG','HM'],['LG'],[]]
		elevatorAt = 1
		statesToTry = []
		steps = 1
		add_state_to_try(state, elevatorAt, steps, statesToTry)
		self.assertEqual(statesToTry, [([['LM'],['HG','HM'],['LG'],[]], 1, 1)])

		state = [['LM'],[],['HG','HM','LG'],[]]
		elevatorAt = 2
		statesToTry = [([['LM'],['HG','HM'],['LG'],[]], 1, 1)]
		steps = 2
		add_state_to_try(state, elevatorAt, steps, statesToTry)
		self.assertEqual(statesToTry, [([['LM'],['HG','HM'],['LG'],[]], 1, 1),([['LM'],[],['HG','HM','LG'],[]], 2, 2)])

	def test_item_is_a_pair(self):

		item = ['HM']
		self.assertEqual(item_is_a_pair(item), False)

		item = ['HM','HG']
		self.assertEqual(item_is_a_pair(item), True)

		item = ['HM','LM']
		self.assertEqual(item_is_a_pair(item), False)

if __name__ == '__main__':
	unittest.main()
