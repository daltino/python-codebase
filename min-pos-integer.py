# A simple Python function to derive the minimum positive
# integer that is not present in an array and is greater than 
def getMinPosInt(array):
 	candidate = 1
 	for i in set(array):
		if candidate < len(array) and candidate != i:
			return candidate
		elif candidate == len(array):
			return candidate + 1
		else:
			candidate = candidate + 1

print(getMinPosInt(range(1,100000)))
print(getMinPosInt(range(1,50000)))
print(getMinPosInt([1,3000,10000,20000,40000]))
print(getMinPosInt([1,3,5]))