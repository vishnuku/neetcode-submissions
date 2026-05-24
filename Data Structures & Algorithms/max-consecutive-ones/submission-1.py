class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = []
        one_occcurance = 0
        for i, x in enumerate(nums) :
            if x == 1:
                one_occcurance += 1
            if x == 0 or (i  == len(nums)-1) :
                max_consecutive.append(one_occcurance)
                one_occcurance = 0

        return max(max_consecutive)
