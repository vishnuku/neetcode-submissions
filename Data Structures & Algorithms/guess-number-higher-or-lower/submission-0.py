class Solution:

    def guessNumber(self, n: int) -> int:
        L, R = 1, n
        while L <= R:
            mid = (L + R) // 2
            res = guess(mid)
            if res == 1:
                L = mid + 1
            elif res == -1:
                R = mid - 1
            else:
                return mid
        return -1
