from typing import List

class Solution1:
    def rotate(self, nums: List[int], k: int) -> list:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums.pop())
        return nums

class Solution2:
    def rotate(self, nums: List[int], k: int) -> list:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k <= len(nums):
            nums[:] = nums[-k:] + nums[:-k]
        else:
            while k > len(nums):
                k -= len(nums)
            nums[:] = nums[-k:] + nums[:-k]
        return nums
nums = [1,2,3,4,5,6,7]
k = 3
Solution1().rotate(nums, k)
print(nums)