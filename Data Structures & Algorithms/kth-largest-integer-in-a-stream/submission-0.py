class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        return self.find()

    def find(self) -> int:
        sorted_nums = sorted(self.nums)
        return sorted_nums[-self.k]

        
