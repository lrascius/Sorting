import math
import random
import unittest
import matplotlib.pyplot as matplot
import time

def Swap(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp

def BubbleSort(array):
	for i in range(len(array)):
		for j in range(len(array)-1):
			if array[j] > array[j+1]:
				Swap(array, j, j+1)
	return array

def SelectionSort(array):
	minimum = 0
	for i in range(len(array)-1):
		minimum = i
		for j in range(i+1, len(array)):
			if array[j] < array[minimum]:
			 	minimum = j
		if(minimum != i):
			Swap(array, i, minimum)

	return array

def InsertionSort(array):
	for i in range(1, len(array)):
		j = i
		while (j > 0 and array[j-1] > array[j]):
			Swap(array, j, j-1)
			j-=1
	return array

def Merge(left, right):
	ret_array = []
	left_index = 0
	right_index = 0
	while left_index != len(left) and right_index != len(right):
		if left[left_index] <= right[right_index]:
			ret_array.append(left[left_index])
			left_index+=1
		else:
			ret_array.append(right[right_index])
			right_index+=1
	if(left_index == len(left)):
		ret_array.extend(right[right_index:len(right)])
	else:
		ret_array.extend(left[left_index:len(left)])

	return ret_array
	

def MergeSort(array):
    if (len(array) == 1):
        return array
 
    left = MergeSort(array[0:len(array) / 2])
    right = MergeSort(array[len(array) / 2: len(array)])
    return Merge(left, right)

def Partition(array, low, high):
	
	pivot_index = random.randint(low, high)
	pivot = array[pivot_index]
	Swap(array, pivot_index, high)
	next_index = low
	for i in range(low, high):
		if array[i] <= pivot:
			Swap(array, i, next_index)
			next_index += 1
	Swap(array, next_index, high)

	return next_index

def QuicksortApply(array, low, high):
	if low < high:
		p = Partition(array, low, high)
		QuicksortApply(array, low, p-1)
		QuicksortApply(array, p+1, high)
		return array

def Quicksort(array):
	return QuicksortApply(array, 0, len(array) -1)


# Some simple unittests
class TestSorts(unittest.TestCase):
	def setUp(self):
		self.size = 100
		self.array = [int(1000*random.random()) for i in range(self.size)]
	def test_bubblesort(self):
		sorted_array = BubbleSort(self.array)
		for i in range(2,self.size):
			self.assertTrue(sorted_array[i-1] <= sorted_array[i])
	def test_selectionsort(self):
		sorted_array = SelectionSort(self.array)
		for i in range(2,self.size):
			self.assertTrue(sorted_array[i-1] <= sorted_array[i])
	def test_insertionsort(self):
		sorted_array = InsertionSort(self.array)
		for i in range(2,self.size):
			self.assertTrue(sorted_array[i-1] <= sorted_array[i])
	def test_mergesort(self):
		sorted_array = MergeSort(self.array)
		for i in range(2,self.size):
			self.assertTrue(sorted_array[i-1] <= sorted_array[i])
	def test_quicksort(self):
		sorted_array = Quicksort(self.array)
		for i in range(2,self.size):
			self.assertTrue(sorted_array[i-1] <= sorted_array[i])

def fileToArray(string):
	file_handle = open(string, "r")
	numbers_array = []
	while True:
		line = file_handle.readline()
		numbers = line.split(',')
		numbers_array.extend(numbers)
		if not line:
			break

	int_array = []
	for i in range(len(numbers_array)-1):
		if(numbers_array[i] == "\n"):
			continue
			# int_array.append(numbers_array[i])
		else:
			int_array.append(int(numbers_array[i]))

	return int_array


# print fileToArray('numbers.txt')
# print Quicksort(fileToArray('numbers.txt'))

def time_function(func, n):
	'''func is the function you want to time and n is the number of times you want that function to be called'''
	cum_sum = 0
	for i in range(n):
		array = [int(1000*random.random()) for i in range(1000)]
		start = time.clock()
		func(array)
		end = time.clock()
		cum_sum += (end-start)
	return cum_sum/n 

print time_function(BubbleSort, 10)
print time_function(InsertionSort, 10)
print time_function(SelectionSort, 10)
print time_function(MergeSort, 10)
print time_function(Quicksort, 10)



# matplot.plot([1,2,3,4])
# matplot.ylabel('some numbers')
# matplot.show()

# for i in range(10):
# 	BubbleSort(array)
# end= time.clock()

# average_time = (end-start)/10
# print average_time



# if __name__ == '__main__':
#     unittest.main()




