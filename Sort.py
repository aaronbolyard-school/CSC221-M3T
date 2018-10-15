# Aaron Bolyard
# 2018-10-10
# Sorts a list-like object.
# M3T, CSC-221

"""
This module is an implementation of the heap sort psuedo-code found
on Wikipedia as of 2018-10-14.

https://en.wikipedia.org/w/index.php?title=Heapsort&oldid=862731429
"""

def parent(index):
	return (index - 1) // 2

def leftChild(index):
	return (index * 2) + 1

def rightChild(index):
	return (index * 2) + 2

def heapify(items, key):
	start = parent(len(items) - 1)

	while start >=	 0:
		siftDown(items, start, len(items) - 1, key)
		start -= 1

def siftDown(items, start, end, key):
	root = start

	while leftChild(root) <= end:
		child = leftChild(root)
		swap = root

		if key(items[swap]) < key(items[child]):
			swap = child

		if child + 1 <= end and key(items[swap]) < key(items[child + 1]):
			swap = child + 1

		if swap == root:
			return
		else:
			items[root], items[swap] = items[swap], items[root]
			root = swap

def heapsort(items, key=None):
	"""
	Sorts a list using heap sort.

	'key' can be provided to specify a specific value to sort by. 'key' should be
	a lambda. If not provided, values are compared using the less-than operator.
	"""
	if not key:
		key = lambda x: x

	count = len(items)

	heapify(items, key)

	end = count - 1
	while end > 0:
		items[end], items[0] = items[0], items[end]
		end -= 1
		siftDown(items, 0, end, key)
