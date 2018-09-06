def quicksort(array):
	left = []
	right = []
	if len(array)<2:
		return array
	else:
		for i in range(1,len(array)):
			if array[i] <= array[0]:
				left.append(array[i])
			else:
				right.append(array[i])
		return quicksort(left) + [array[0]] + quicksort(right)

def quicksort2(array):
	left = []
	right = []
	if len(array)<2:
		return array
	else:
		for i in range(1, len(array)):
			if array[i][1] > array[0][1]:
				right.append(array[i])
			else:
				left.append(array[i])
		return quicksort2(left) + [array[0]] + quicksort2(right)