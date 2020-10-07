# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums) 
        op = 1
        for i in range(length-1):
            for j in range(i+1, length):
                sum = (nums[i] - 1) * (nums[j] - 1) 
               
                if sum > op :
                    op = sum 
        if op > 1:
            return(op)			
        else:
            return 0