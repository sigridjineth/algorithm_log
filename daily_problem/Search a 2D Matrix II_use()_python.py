# LEETCODE 240 Search a 2D Matrix II
# using any() function to return true when the case of at least one element in the function is true
def searchMatrix(self, matrix, target):
    return any(target in row for row in matrix)