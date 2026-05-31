
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            nums = matrix[row]
            L, R = 0, len(nums) - 1
            while L <= R:
                mid = (L + R) // 2
                if target > nums[mid]:
                    L = mid + 1
                elif target < nums[mid]:
                    R = mid - 1
                else:
                    return True
        return False
