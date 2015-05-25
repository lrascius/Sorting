# Lukas Rascius
# Python 2.7

import math
import random
import unittest
import matplotlib.pyplot as matplot
import pylab
import time
from Tkinter import *
from tkFileDialog import asksaveasfile, askopenfile


def Swap(array, i, j):
    ''' Swaps elements in indexes i and j '''
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


class Sort:

    def __init__(self, array=[]):
    	''' The array that stores the numbers '''
        self.array = array

    def BubbleSort(self):
        ''' Bubble sort works by looping through every element and
            swapping if the next element is larger than the previous.
            Thus after every iteration i one element is in its
            proper place '''
        for i in range(len(self.array)):
            for j in range(len(self.array) - 1):
                if self.array[j] > self.array[j + 1]:
                    Swap(self.array, j, j + 1)
        return self.array

    def SelectionSort(self):
        '''Selection sort finds the minumum element, and then
           places it in the ith position'''
        minimum = 0
        for i in range(len(self.array) - 1):
            minimum = i
            for j in range(i + 1, len(self.array)):
                if self.array[j] < self.array[minimum]:
                    minimum = j
            if(minimum != i):
                Swap(self.array, i, minimum)

        return self.array

    def InsertionSort(self):
        ''' Insertion sort works by placing an element in the correct
            position with respect to the elements seen so far.'''
        for i in range(1, len(self.array)):
            j = i
            while (j > 0 and self.array[j - 1] > self.array[j]):
                Swap(self.array, j, j - 1)
                j -= 1
        return self.array

    def MergeSort(self):
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

        def MergeSortApply(array):
            ''' Helper function to allow recursion in a class function '''
            if (len(array) <= 1):
                return array

            left = MergeSortApply(array[0:len(array) / 2])
            right = MergeSortApply(array[len(array) / 2: len(array)])
            return Merge(left, right)

        return MergeSortApply(self.array)

    def Quicksort(self):
    	''' Quicksort works by picking a random pivot and moving the numbers
    	    which are greater than the pivot to the right of it and the numbers 
    	    less than the pivot to the left. It does this recursively until all
    	    the numbers are sorted in the array'''
        
        def Partition(array, low, high):
        	'''Partition moves elements to the left and right of the pivot '''
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
        	''' Recursively sort the array using the pivot '''
	        if low < high:
	            p = Partition(array, low, high)
	            QuicksortApply(array, low, p - 1)
	            QuicksortApply(array, p + 1, high)
	            return array

    	return QuicksortApply(self.array, 0, len(self.array) - 1)

    def Heapsort(self):
    	''' Heapsort works by first building a heap and then moving the
    	    root element to the end of the array and calling heapify on
    	    an array not including those maximal numbers which have been added to
    	    the end. Calling heapify then gets the next maximal value to the root'''

        def BuildHeap(array):
        	''' Builds a heap where the children are allways smaller than or equal to the root '''
     		n = len(array)
	        for i in range(int(math.floor(n / 2)) - 1, -1, -1):
		        Heapify(array, i, n)

        def Heapify(array, i, n):
        	''' Swaps children and parents to get the maximum number to the root'''
        	
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

        BuildHeap(self.array)
        n = len(self.array)
        for i in range(len(self.array), 0, -1):
            Swap(self.array, 0, i - 1)
            i -= 1
            n -= 1
            Heapify(self.array, 0, n)

        return self.array

    def CreateRandomArray(self, n):
        ''' Creates a random array of size n with numbers between 0 - 1000'''
        self.array = [int(1000 * random.random()) for i in range(n)]

    def CreateSortedArray(self, n):
        ''' Creates a sorted array of size n with numbers 1, 2 .. n'''
        self.array = [int(i) for i in range(1, n+1)]

    def CreateReversedArray(self, n):
        ''' Creates a random array of size n with numbers n, n-1 .. 1'''
        self.array = [int(i) for i in range(n, 0, -1)]

def fileToArray(file_handle):
    '''Function that takes a file name and converts it into
       an array but splitting on each , and ignoring the line
       spaces'''
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

def time_function(func, repeat, n):
    '''func: is the function you want to time
       repeat: is the number of times you want that function to be called
       n: is the size of array'''
    sort = Sort()
    function = 'sort.' + func + '()'
    cum_sum = 0
    for i in range(repeat):
    	# Get the array the user wants the sorting algorithms to be called on
    	if array_type.get() == 1:
        	sort.CreateRandomArray(n)
    	if array_type.get() == 2:
        	sort.CreateSortedArray(n)
    	if array_type.get() == 3:
        	sort.CreateReversedArray(n)        	
        # Count how long it took to evaluate the function and average the times for accuracy
        start = time.clock()
        eval(function)
        end = time.clock()
        cum_sum += (end - start)
    return cum_sum / repeat


def plot_graph():
	''' Plots the graphs of the sorting algorithms selected in the
	    checkboxes tested on array size of size selected and interval provided
	    For example, size = 1000 and interval 10, will time the selected 
	    sorting algorithms on array of 100, 200, 300, 400, .... 1000'''
	x_axis_array = []
	size = int(size_entry.get())
	intervals = int(intervals_entry.get())
	interval = int(size / intervals)

	for i in range(interval, (size + interval), interval):
	    x_axis_array.append(i)

	if bubble_checkbox.get() == 1:
	    bubble_array = []
	    for i in range(interval, (size + interval), interval):
	        bubble_array.append(time_function('BubbleSort', 10, i))
	    pylab.plot(x_axis_array, bubble_array, label='Bubble Sort')

	if selection_checkbox.get() == 1:
	    selection_array = []
	    for i in range(interval, (size + interval), interval):
	        selection_array.append(time_function('SelectionSort', 10, i))
	    pylab.plot(x_axis_array, selection_array, label='SelectionSort')

	if insertion_checkbox.get() == 1:
	    insertion_array = []
	    for i in range(interval, (size + interval), interval):
	        insertion_array.append(time_function('InsertionSort', 10, i))
	    pylab.plot(x_axis_array, insertion_array, label="InsertionSort")

	if mergesort_checkbox.get() == 1:
	    mergesort_array = []
	    for i in range(interval, (size + interval), interval):
	        mergesort_array.append(time_function('MergeSort', 10, i))
	    pylab.plot(x_axis_array, mergesort_array, label="MergeSort")

	if quicksort_checkbox.get() == 1:
	    quicksort_array = []
	    for i in range(interval, (size + interval), interval):
	        quicksort_array.append(time_function('Quicksort', 10, i))
	    pylab.plot(x_axis_array, quicksort_array, label='Quicksort')

	if heapsort_checkbox.get() == 1:
	    heapsort_array = []
	    for i in range(interval, (size + interval), interval):
	        heapsort_array.append(time_function('Heapsort', 10, i))
	    pylab.plot(x_axis_array, heapsort_array, label='Heapsort')

	pylab.legend(loc='upper left')
	pylab.xlabel('Size of array (n)')
	pylab.ylabel('Time (s)')
	pylab.title('Sorting Algorithms')
	matplot.show()


def file_input():
	''' Gets the file and creates an array of numbers from it. 
	    Then uses Quicksort to sort all the numbers.'''
	file_handle = askopenfile(mode='r')
	array = fileToArray(file_handle)
	sort = Sort(array)
	sorted_array = sort.Quicksort()
	file_save(str(sorted_array))


def file_save(string):
	''' Creates a new file based on the users choice of name
	    and then writes the numbers every 30 characters into
	    the file'''
	new_file = asksaveasfile(mode='w', defaultextension=".txt")
	if new_file is None:
	    return

	char_count = 0
	current_string = ""
	for char in string:
	    char_count += 1
	    current_string += char
	    if char_count == 30:
	        new_file.write(str(current_string))
	        new_file.write("\n")
	        char_count = 0
	        current_string = ""

	new_file.write(str(current_string))
	new_file.close()

container = Tk()

# Set the general settings of the window
container.geometry("600x400")
container.title("Sorting Application")

# Create the title and subtitles
var = StringVar()
label = Label(container, textvariable=var, anchor=CENTER, font=("Helvetica", 20, "bold"))
var.set("Sorting Application")
label.pack()

# Code for Time Analysis plots
var = StringVar()
label = Label(
    container, textvariable=var, font=("Helvetica", 15, "bold italic"))
var.set("Time Analysis Plot")
label.place(x=50, y=35)

# Code for Time Analysis description
var = StringVar()
label = Label(container, textvariable=var)
var.set("Please choose the size of array, the interval \n size and the sorting algorithms to be compared. ")
label.place(x=0, y=52)

# Labels and entries for settings for the plot
size_label = Label(container, text="Size of Array:")
size_label.place(x=0, y=90)

default_size = StringVar(value=1000)
size_entry = Entry(container, textvariable=default_size, width=6)
size_entry.place(x=120, y=90)

intervals_label = Label(container, text="Number of intervals:")
intervals_label.place(x=0, y=120)

default_intervals = StringVar(value=10)
intervals_entry = Entry(container, textvariable=default_intervals, width=6)
intervals_entry.place(x=120, y=120)

# Radio buttons for the different arrays to test the sorting algorithms on
array_type = IntVar()
Radiobutton(container, text="Random Array", variable=array_type, value=1).place(x=50, y=150)
Radiobutton(container, text="Sorted Array", variable=array_type, value=2).place(x=50, y=170)
Radiobutton(container, text="Reversed Array", variable=array_type, value=3).place(x=50, y=190)
array_type.set(1)

# Checkboxes for the different sorting algorithms
bubble_checkbox = IntVar()
Checkbutton(container, text="Bubble Sort", variable=bubble_checkbox).place(
    x=0, y=220)

selection_checkbox = IntVar()
Checkbutton(container, text="Selection Sort", variable=selection_checkbox).place(
    x=0, y=240)

insertion_checkbox = IntVar()
Checkbutton(container, text="Insertion Sort", variable=insertion_checkbox).place(
    x=0, y=260)

mergesort_checkbox = IntVar()
Checkbutton(container, text="Mergesort", variable=mergesort_checkbox).place(
    x=150, y=220)

quicksort_checkbox = IntVar()
Checkbutton(container, text="Quicksort", variable=quicksort_checkbox).place(
    x=150, y=240)

heapsort_checkbox = IntVar()
Checkbutton(container, text="Heapsort", variable=heapsort_checkbox).place(
    x=150, y=260)


Button(container, text='Plot', command=plot_graph).place(x=75, y=300)

# Code for Sorting a file
var = StringVar()
label = Label(container, textvariable=var, font=("Helvetica", 15, "bold italic"))
var.set("Sort a file")
label.place(x=390, y=35)

# Code for Sorting a file description
var = StringVar()
label = Label(container, textvariable=var)
var.set("Choose a file you want to sort, make sure \n the numbers in the file are seperated by commas.")
label.place(x=290, y=52)

Button(text='Choose file', command=file_input).place(x=400, y=300)

# Quit button to exit the application
Button(container, text='Quit', command=container.quit, anchor=CENTER).pack(
    side=BOTTOM)

mainloop()

# Some simple unittests

class TestSorts(unittest.TestCase):

    def setUp(self):
        self.size = 100
        self.sort = Sort()

    def test_bubblesort(self):
        '''Unittest for BubbleSort'''
        self.sort.CreateRandomArray(self.size)
        sorted_array = self.sort.BubbleSort()
        for i in range(2, self.size):
            self.assertTrue(sorted_array[i - 1] <= sorted_array[i])

    def test_selectionsort(self):
        '''Unittest for SelectionSort'''
        self.sort.CreateRandomArray(self.size)
        sorted_array = self.sort.SelectionSort()
        for i in range(2, self.size):
            self.assertTrue(sorted_array[i - 1] <= sorted_array[i])

    def test_insertionsort(self):
        '''Unittest for InsertionSort'''
        self.sort.CreateRandomArray(self.size)
        sorted_array = self.sort.InsertionSort()
        for i in range(2, self.size):
            self.assertTrue(sorted_array[i - 1] <= sorted_array[i])

    def test_mergesort(self):
        '''Unittest for MergeSort'''
        self.sort.CreateRandomArray(self.size)
        sorted_array = self.sort.MergeSort()
        for i in range(2, self.size):
            self.assertTrue(sorted_array[i - 1] <= sorted_array[i])

    def test_quicksort(self):
        '''Unittest for Quicksort'''
        self.sort.CreateRandomArray(self.size)
        sorted_array = self.sort.Quicksort()
        for i in range(2, self.size):
            self.assertTrue(sorted_array[i - 1] <= sorted_array[i])

    def test_heapsort(self):
        '''Unittest for Heapsort'''
        self.sort.CreateRandomArray(self.size)
        sorted_array = self.sort.MergeSort()
        for i in range(2, self.size):
            self.assertTrue(sorted_array[i - 1] <= sorted_array[i])

    def test_sorted_array(self):
        '''Unittest for sorted array'''
        self.sort.CreateSortedArray(self.size)
        sorted_array = self.sort.array
        for i in range(2, self.size):
            self.assertTrue(sorted_array[i - 1] <= sorted_array[i])

    def test_reversed_array(self):
        '''Unittest for reversed array'''
        self.sort.CreateReversedArray(self.size)
        reversed_array = self.sort.array
        for i in range(2, self.size):
            self.assertTrue(reversed_array[i - 1] >= reversed_array[i])

if __name__ == '__main__':
    unittest.main()

