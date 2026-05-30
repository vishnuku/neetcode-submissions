class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0  # index for L
        j = 0  # index for R
        k = 0
        arr = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
            k +=1

        while i < m:
            arr.append(nums1[i])
            i += 1
            k += 1
        while j < n:
            arr.append(nums2[j])
            j += 1
            k += 1

        nums1[:] = arr