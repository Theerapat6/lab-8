def merge(val):
	if len(val) > 1:

		L = val[:len(val)//2] 
		R = val[len(val)//2:]
		merge(L)
		merge(R)
		
		i = x = k = 0
	
		while i < len(L) and x < len(R):
			if L[i] <= R[x]:
				val[k] = L[i]
				i += 1
			else:
				val[k] = R[x]
				x += 1
			k += 1
		while i < len(L):
			val[k] = L[i]
			i += 1
			k += 1
		while x < len(R):
			val[k] = R[x]
			x += 1
			k += 1

val = [29,10,14,37,14,20,7,16,12]
print("merge :",val)
merge(val)
print("merge sort:",val)
