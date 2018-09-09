# A simple Python function to derive the minimum positive
# integer that is not present in an array and is greater than 
def getMinPosInt(array):
 	notFound = True
 	candidate = 1
 	while notFound:
 		if candidate not in array:
 			notFound = False
 		else:
 			candidate = candidate + 1
 	return candidate

print(getMinPosInt(range(1,50000)))