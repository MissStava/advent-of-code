from itertools import combinations

array = ["HM", "LM", "LG"]

array1 = list(combinations(array, 1))
print array1
array2 = list(combinations(array, 2))
print array2
array3 = array2 + array1
array3 = [list(elem) for elem in array3]
print array3
