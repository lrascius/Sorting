
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

print BubbleSort([4, 32, 4, 43, 3, 2, 3, 1])
print SelectionSort([4, 32, 4, 43, 3, 2, 3, 1])