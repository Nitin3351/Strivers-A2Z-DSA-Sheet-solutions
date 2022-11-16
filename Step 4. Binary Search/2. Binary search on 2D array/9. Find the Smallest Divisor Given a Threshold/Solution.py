class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low= 1
        import math
        high= max(nums)
        def feasible(div):
            return sum([math.ceil(i/div) for i in nums]) <=threshold
        while low<high:
            mid= (low+high)>>1
            if feasible(mid):
                high= mid
            else:
                low= mid+1
        return low
