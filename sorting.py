import math
import random
import unittest
import matplotlib.pyplot as matplot
import pylab 
import time
try:
	# Python2
    from Tkinter import *
except ImportError:
    # Python3
    from tkinter import *

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

def time_function(func, repeat, n):
	'''func: is the function you want to time
	   repeat: is the number of times you want that function to be called
	   n: is the size of array'''
	cum_sum = 0
	for i in range(repeat):
		array = [int(1000*random.random()) for i in range(n)]
		start = time.clock()
		func(array)
		end = time.clock()
		cum_sum += (end-start)
	return cum_sum/repeat

# x_axis_array = []
# bubble_array = []

# for i in range(100,1100,100):
# 	x_axis_array.append(i)
# 	bubble_array.append(time_function(BubbleSort, 10, i))

# # print time_function(InsertionSort, 10, 1000)
# # print time_function(SelectionSort, 10, 1000)
# # print time_function(MergeSort, 10, 1000)
# # print time_function(Quicksort, 10, 1000)



# matplot.plot(x_axis_array, bubble_array)
# matplot.xlabel('size of array (n)')
# matplot.ylabel('time (s)')
# matplot.show()

# for i in range(10):
# 	BubbleSort(array)
# end= time.clock()

# average_time = (end-start)/10
# print average_time

from Tkinter import *
master = Tk()
matplot.figure(1)
def plot_graph():
	x_axis_array = []
	bubble_array = []
	selection_array = []
	for i in range(100,1100,100):
		x_axis_array.append(i)	

   	if bubble_checkbox.get() == 1:
   		bubble_array = []
		for i in range(100,1100,100):
			bubble_array.append(time_function(BubbleSort, 10, i))
		pylab.plot(x_axis_array, bubble_array, label='Bubble Sort')

   	if selection_checkbox.get() == 1:
   		selection_array = []
		for i in range(100,1100,100):
			selection_array.append(time_function(SelectionSort, 10, i)) 
		pylab.plot(x_axis_array, selection_array, label='SelectionSort')

   	if insertion_checkbox.get() == 1:
   		insertion_array = []
		for i in range(100,1100,100):
			insertion_array.append(time_function(InsertionSort, 10, i))
		pylab.plot(x_axis_array, insertion_array, label="InsertionSort")

   	if mergesort_checkbox.get() == 1:
   		mergesort_array = []
		for i in range(100,1100,100):
			mergesort_array.append(time_function(MergeSort, 10, i))
		pylab.plot(x_axis_array, mergesort_array, label="MergeSort")

   	if quicksort_checkbox.get() == 1:
   		quicksort_array = []
		for i in range(100,1100,100):
			quicksort_array.append(time_function(Quicksort, 10, i))
		pylab.plot(x_axis_array, quicksort_array, label='Quicksort')
	pylab.legend(loc='upper left')
	matplot.show()
	# figure(1)
	# matplot.plot(x_axis_array, bubble_array, x_axis_array, selection_array)
	# matplot.xlabel('size of array (n)')
	# matplot.ylabel('time (s)')
	# matplot.show()



bubble_checkbox = IntVar()
Checkbutton(master, text="Bubble Sort", variable=bubble_checkbox).grid(row=0, sticky=W)
selection_checkbox = IntVar()
Checkbutton(master, text="Selection Sort", variable=selection_checkbox).grid(row=1, sticky=W)
insertion_checkbox = IntVar()
Checkbutton(master, text="Insertion Sort", variable=insertion_checkbox).grid(row=2, sticky=W)
mergesort_checkbox = IntVar()
Checkbutton(master, text="Mergesort", variable=mergesort_checkbox).grid(row=3, sticky=W)
quicksort_checkbox = IntVar()
Checkbutton(master, text="Quicksort", variable=quicksort_checkbox).grid(row=4, sticky=W)

Button(master, text='Quit', command=master.quit).grid(row=5, sticky=W, pady=4)
Button(master, text='Show', command=plot_graph).grid(row=6, sticky=W, pady=4)

mainloop()

# if __name__ == '__main__':
#     unittest.main()
# from tkinter import Tk, Button, Label, Entry, RIGHT, LEFT, TOP, BOTTOM

# container = Tk()

# num1_label = Label(container, text="Number 1:")
# num1_label.grid(row=0, column=0)

# num1_entry = Entry(container)
# num1_entry.grid(row=0, column=1)

# num2_label = Label(container, text="Number 2:")
# num2_label.grid(row=1, column=0)

# num2_entry = Entry(container)
# num2_entry.grid(row=1, column=1)

# answer_label = Label(container, text="Answer")
# answer_label.grid(row=2, columnspan=2)

# def add():
#     num1 = float(num1_entry.get())
#     num2 = float(num2_entry.get())
#     answer = num1 + num2
#     answer_label['text'] = str(answer)

# def subtract():
#     num1 = float(num1_entry.get())
#     num2 = float(num2_entry.get())
#     answer = num1 - num2
#     answer_label['text'] = str(answer)

# def multiply():
#     num1 = float(num1_entry.get())
#     num2 = float(num2_entry.get())
#     answer = num1 * num2
#     answer_label['text'] = str(answer)

# def divide():
#     num1 = float(num1_entry.get())
#     num2 = float(num2_entry.get())
#     answer = num1 / num2
#     answer_label['text'] = str(answer)
    
# button = Button(container, text="ADD", command=add)
# button.grid(row=3, columnspan=1)

# button = Button(container, text="SUBTRACT", command=subtract)
# button.grid(row=3, columnspan=2)

# button = Button(container, text="MULTIPLY", command=multiply)
# button.grid(row=4, columnspan=1)

# button = Button(container, text="DIVIDE", command=divide)
# button.grid(row=4, columnspan=2)
# container.mainloop()





