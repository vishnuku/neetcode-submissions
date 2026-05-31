
class Solution:
    def searchMatrix(self, matrix, target):

        rows = len(matrix)
        cols = len(matrix[0])

        L = 0
        R = rows * cols - 1

        while L <= R:

            mid = (L + R) // 2

            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value == target:
                return True

            elif value < target:
                L = mid + 1

            else:
                R = mid - 1

        return False
