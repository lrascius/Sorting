
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



print BubbleSort([4, 32, 3, 1])
		