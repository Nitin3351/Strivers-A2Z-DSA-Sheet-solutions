class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0;high=len(nums)-1
        first=last=-1
        while low<=high:
            mid= (low+high)//2
            if nums[mid]>target:
                high= mid-1
            elif nums[mid]<target:
                low= mid+1
            else:
                last= mid
                low= mid+1
        low=0
        high=len(nums)-1
        while low<=high:
            mid= (low+high)//2
            if nums[mid]>target:
                high= mid-1
            elif nums[mid]<target:
                low= mid+1
            else:
                first= mid
                high= mid-1
        return [first, last]
