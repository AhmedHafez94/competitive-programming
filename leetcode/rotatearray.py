# https://leetcode.com/problems/rotate-array/ 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        while k > 0:
            temp = nums.pop()
            nums.insert(0, temp)
            k = k - 1
            i = i + 1
        return(nums)

