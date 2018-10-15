# Aaron Bolyard
# 2018-10-10
# Tests for sort.
# M3T, CSC-221

import Sort
from arrays import Array

def test_sort_list_numbers():
	items = [ 5, 4, 2, 3, 1, 6 ]
	Sort.heapsort(items)

	assert(items[0] == 1)
	assert(items[1] == 2)
	assert(items[2] == 3)
	assert(items[3] == 4)
	assert(items[4] == 5)
	assert(items[5] == 6)

def test_sort_array_numbers():
	items = Array(6)
	items[0] = 5
	items[1] = 4
	items[2] = 2
	items[3] = 3
	items[4] = 1
	items[5] = 6

	Sort.heapsort(items)

	assert(items[0] == 1)
	assert(items[1] == 2)
	assert(items[2] == 3)
	assert(items[3] == 4)
	assert(items[4] == 5)
	assert(items[5] == 6)

def test_sort_list_string():
	items = [ 'bob', 'joe', 'jane', 'isabelle' ]
	Sort.heapsort(items)

	assert(items[0] == 'bob')
	assert(items[1] == 'isabelle')
	assert(items[2] == 'jane')
	assert(items[3] == 'joe')

def test_sort_list_string():
	items = Array(4)
	items[0] = 'bob'
	items[1] = 'joe'
	items[2] = 'jane'
	items[3] = 'isabelle'

	Sort.heapsort(items)

	assert(items[0] == 'bob')
	assert(items[1] == 'isabelle')
	assert(items[2] == 'jane')
	assert(items[3] == 'joe')
