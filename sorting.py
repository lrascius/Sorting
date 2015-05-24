import math
import random
import unittest
import matplotlib.pyplot as matplot
import pylab
import time
from Tkinter import *
from tkFileDialog import askopenfilename


def Swap(array, i, j):
	''' Swaps elements in indexes i and j '''
	temp = array[i]
	array[i] = array[j]
	array[j] = temp


def BubbleSort(array):
	''' Bubble sort works by looping through every element and
	    swapping if the next element is larger than the previous.
	    Thus after every iteration i one element is in its
	    proper place '''
	for i in range(len(array)):
		for j in range(len(array) - 1):
			if array[j] > array[j + 1]:
				Swap(array, j, j + 1)
	return array


def SelectionSort(array):
	'''Selection sort finds the minumum element, and then
	   places it in the ith position'''
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
	''' Insertion sort works by placing an element in the correct 
	    position with respect to the elements seen so far.'''
	for i in range(1, len(array)):
		j = i
		while (j > 0 and array[j-1] > array[j]):
			Swap(array, j, j-1)
			j-=1
	return array


def MergeSort(array):
	'''Merge sort recursively breaks down the array into two halfs 
	   and sorts both sides and finally merges both sides back.
	   Base case occurs when the size of the list is one or less 
	   in that case we can simply return the array'''
	def Merge(left, right):
		'''Merges two sorted arrays into one '''
		ret_array = []
		left_index = 0
		right_index = 0
		while left_index != len(left) and right_index != len(right):
		    if left[left_index] <= right[right_index]:
		        ret_array.append(left[left_index])
		        left_index += 1
		    else:
		        ret_array.append(right[right_index])
		        right_index += 1
		if(left_index == len(left)):
		    ret_array.extend(right[right_index:len(right)])
		else:
		    ret_array.extend(left[left_index:len(left)])

		return ret_array 

	if (len(array) <= 1):
		return array

	left = MergeSort(array[0:len(array) / 2])
	right = MergeSort(array[len(array) / 2: len(array)])
	return Merge(left, right)

def Quicksort(array):

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
	        QuicksortApply(array, low, p - 1)
	        QuicksortApply(array, p + 1, high)
	        return array

	return QuicksortApply(array, 0, len(array) - 1)


def Heapsort(array):
	def BuildHeap(array):
	    n = len(array)
	    for i in range(int(math.floor(n / 2)) - 1, -1, -1):
	        Heapify(array, i, n)

	def Heapify(array, i, n):
	    left = 2 * i
	    right = 2 * i + 1

	    if(left <= n - 1) and (array[left] > array[i]):
	        largest = left
	    else:
	        largest = i
	    if(right <= n - 1) and (array[right] > array[largest]):
	        largest = right
	    if(largest != i):
	        Swap(array, i, largest)
	        Heapify(array, largest, n)

	BuildHeap(array)
	n = len(array)
	for i in range(len(array), 0, -1):
		Swap(array, 0, i - 1)
		i -= 1
		n -= 1
		Heapify(array, 0, n)

	return array

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
    for i in range(len(numbers_array) - 1):
        if(numbers_array[i] == "\n"):
            continue
        else:
            int_array.append(int(numbers_array[i]))

    return int_array

# def arrayToFile(string):


#     return int_array    

def time_function(func, repeat, n):
    '''func: is the function you want to time
       repeat: is the number of times you want that function to be called
       n: is the size of array'''
    cum_sum = 0
    for i in range(repeat):
        array = [int(1000 * random.random()) for i in range(n)]
        start = time.clock()
        func(array)
        end = time.clock()
        cum_sum += (end - start)
    return cum_sum / repeat

def plot_graph():
    x_axis_array = []
    bubble_array = []
    selection_array = []
    for i in range(100, 1100, 100):
        x_axis_array.append(i)

    if bubble_checkbox.get() == 1:
        bubble_array = []
        for i in range(100, 1100, 100):
            bubble_array.append(time_function(BubbleSort, 10, i))
        pylab.plot(x_axis_array, bubble_array, label='Bubble Sort')

    if selection_checkbox.get() == 1:
        selection_array = []
        for i in range(100, 1100, 100):
            selection_array.append(time_function(SelectionSort, 10, i))
        pylab.plot(x_axis_array, selection_array, label='SelectionSort')

    if insertion_checkbox.get() == 1:
        insertion_array = []
        for i in range(100, 1100, 100):
            insertion_array.append(time_function(InsertionSort, 10, i))
        pylab.plot(x_axis_array, insertion_array, label="InsertionSort")

    if mergesort_checkbox.get() == 1:
        mergesort_array = []
        for i in range(100, 1100, 100):
            mergesort_array.append(time_function(MergeSort, 10, i))
        pylab.plot(x_axis_array, mergesort_array, label="MergeSort")

    if quicksort_checkbox.get() == 1:
        quicksort_array = []
        for i in range(100, 1100, 100):
            quicksort_array.append(time_function(Quicksort, 10, i))
        pylab.plot(x_axis_array, quicksort_array, label='Quicksort')

    if heapsort_checkbox.get() == 1:
        heapsort_array = []
        for i in range(100, 1100, 100):
            heapsort_array.append(time_function(Heapsort, 10, i))
        pylab.plot(x_axis_array, heapsort_array, label='Heapsort')

    pylab.legend(loc='upper left')
    pylab.xlabel('Size of array (n)')
    pylab.ylabel('Time (s)')
    pylab.title('Sorting Algorithms')
    matplot.show()    

def file_input():
	name = askopenfilename()
	string = name.split("/")
	array = fileToArray(str(string[-1]))
	sorted_array = Quicksort(array)
    
# root = Tk()

# root.geometry("500x500")
# root.title("Sorting Application")

# var = StringVar()
# label = Label(root, textvariable=var, anchor=CENTER, font=("Helvetica", 20, "bold"))
# var.set("Sorting Application")
# label.pack()

# var = StringVar()
# label = Label(root, textvariable=var, font=("Helvetica", 15, "bold italic"))
# var.set("Time Analysis Plot")
# label.place(x=50, y=35)

# var = StringVar()
# label = Label(root, textvariable=var, font=("Helvetica", 15, "bold italic"))
# var.set("Sort a file")
# label.place(x=350, y=35)

# bubble_checkbox = IntVar()
# Checkbutton(root, text="Bubble Sort", variable=bubble_checkbox).place(
#     x= 50, y=100)
# selection_checkbox = IntVar()
# Checkbutton(root, text="Selection Sort", variable=selection_checkbox).place(
#     x= 50, y=120)
# insertion_checkbox = IntVar()
# Checkbutton(root, text="Insertion Sort", variable=insertion_checkbox).place(
#     x= 50, y=140)
# mergesort_checkbox = IntVar()
# Checkbutton(root, text="Mergesort", variable=mergesort_checkbox).place(
#     x= 50, y=160)
# quicksort_checkbox = IntVar()
# Checkbutton(root, text="Quicksort", variable=quicksort_checkbox).place(
#     x= 50, y=180)
# heapsort_checkbox = IntVar()
# Checkbutton(root, text="Heapsort", variable=heapsort_checkbox).place(
#     x= 50, y=200)

# Button(root, text='Plot', command=plot_graph).place(x= 100, y=300)
# Button(root, text='Quit', command=root.quit, anchor=CENTER).pack(side=BOTTOM)

# # Button(text='File Open', command=file_input).grid(row=10)


# mainloop()

# Some simple unittests


class TestSorts(unittest.TestCase):

    def setUp(self):
        self.size = 100
        self.array = [int(1000 * random.random()) for i in range(self.size)]

    def test_bubblesort(self):
        sorted_array = BubbleSort(self.array)
        for i in range(2, self.size):
            self.assertTrue(sorted_array[i - 1] <= sorted_array[i])

    def test_selectionsort(self):
        sorted_array = SelectionSort(self.array)
        for i in range(2, self.size):
            self.assertTrue(sorted_array[i - 1] <= sorted_array[i])

    def test_insertionsort(self):
        sorted_array = InsertionSort(self.array)
        for i in range(2, self.size):
            self.assertTrue(sorted_array[i - 1] <= sorted_array[i])

    def test_mergesort(self):
        sorted_array = MergeSort(self.array)
        for i in range(2, self.size):
            self.assertTrue(sorted_array[i - 1] <= sorted_array[i])

    def test_quicksort(self):
        sorted_array = Quicksort(self.array)
        for i in range(2, self.size):
            self.assertTrue(sorted_array[i - 1] <= sorted_array[i])

    def test_heapsort(self):
        sorted_array = Heapsort(self.array)
        for i in range(2, self.size):
            self.assertTrue(sorted_array[i - 1] <= sorted_array[i])

if __name__ == '__main__':
    unittest.main()
