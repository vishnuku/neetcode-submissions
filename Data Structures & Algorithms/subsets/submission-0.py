class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = [[]]

        for num in nums:
            arr += [i + [num] for i in arr]
        
        return arr