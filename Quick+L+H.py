def quick_sort(val, low, high):
	ninja = val[high]
	i = low - 1
	j = high + 1
	
	for j in range(low, high):		
		if (val[j] < ninja):
			i += 1
			val[i], val[j] = val[j], val[i]
	val[i + 1], val[high] = val[high], val[i + 1]
	return (i + 1)
	
def quick(val, low, high):
	if (low < high):
		mid = quick_sort(val, low, high)	
		quick(val, low, mid - 1)
		quick(val, mid + 1, high)
		
val = [29,10,14,37,14,20,7,16,12]
print("val :",val)
n = len(val)
quick(val, 0, n - 1)
print("-------------------------------------------")
print("Quick :", val)
print("Lomuto :",val)
print("Hoare  :",val)
