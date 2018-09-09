# A simple Python utility script containing various optimized
# algorithms for simple data manipulation tasks
def getMinPosInt(A):
	""" A function to find the minimum positive 
		missing integer in a list """
 	candidate = 1
 	for i in set(A):
		if candidate < len(A) and candidate != i:
			return candidate
		elif candidate == len(A):
			return candidate + 1
		else:
			candidate = candidate + 1

def reverse(A):
	""" Function to reverse elements in an array """
	N = len(A)
	for i in xrange(N // 2):
		k = N - i - 1
		A[i], A[k] = A[k], A[i]
	return A

print(getMinPosInt(xrange(1,100000)))
print(getMinPosInt(xrange(1,50000)))
print(getMinPosInt([1,3000,10000,20000,40000]))
print(getMinPosInt([1,3,5]))
print(reverse([1,2,3]))