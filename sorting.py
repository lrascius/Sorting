import math


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

print BubbleSort([4, 32, 4, 43, 3, 2, 3, 1])
print SelectionSort([4, 32, 4, 43, 3, 2, 3, 1])
print InsertionSort([4, 32, 4, 43, 3, 2, 3, 1])
print MergeSort([4, 32, 4, 43, 3, 2, 3, 1])
# array = [4, 32, 4, 43, 3, 2, 3, 1]
# array.append(1)
# print array

# array1 = [1,2,3,4]
# array2 = [3,4,5,6]
# print Merge(array1, array2)
# print math.floor(len([4, 32, 4, 43, 3, 2, 3, 1])/ 3)
# print (len([1, 2, 3, 4]) // 2)
