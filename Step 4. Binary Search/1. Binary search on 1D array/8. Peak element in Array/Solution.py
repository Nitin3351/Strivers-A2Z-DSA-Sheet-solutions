class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        low=0;high=n-1
        while low<high-1:
            mid=(low+high)//2
            if nums[mid-1]<=nums[mid] and nums[mid]>=nums[mid+1]:
                    return mid
            if nums[mid]<nums[mid-1]:
                    high= mid-1
            else:
                low= mid+1
        if nums[low]>=nums[high]:
            return low
        else:
            return high
        
