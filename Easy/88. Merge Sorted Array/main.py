from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        pointer = 0 
        if n == 0:
            return
        for _ in range(m + n):
            if not nums2:
                continue
            if nums1[pointer] > nums2[0]:
                nums1.insert(pointer, nums2.pop(0))
                pointer += 1
            elif nums1[pointer] == 0:
                if len(nums2) != 0 and pointer >= n + m - len(nums2):
                    nums1.insert(pointer, nums2.pop(0))
                    pointer += 1
                else: pointer += 1
            else: pointer += 1

        for _ in range(n):
            nums1.pop(-1)

        # nums1 = nums1[:-n]

nums1 = [-1,0,0,0,3,0,0,0,0,0,0]
m = 5
nums2 = [-1,-1,0,0,1,2]
n = 6
Solution().merge(nums1, m, nums2, n)
print(nums1)