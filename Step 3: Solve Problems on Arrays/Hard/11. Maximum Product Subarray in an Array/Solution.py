class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p1= p2= res= nums[0]
        for i in nums[1:]:
            temp= max(i,p1*i,p2*i)
            p2= min(i,p1*i,p2*i)
            p1= temp
            res= max(p1,res)
        return res
