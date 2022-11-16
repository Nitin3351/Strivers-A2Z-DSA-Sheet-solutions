class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        import math
        high= max(piles)
        while low<=high:
            mid= (low+high)>>1
            eatall= sum([math.ceil(i/mid) for i in piles])
            if eatall<=h:
                high= mid-1
            else:
                low= mid+1
        return low
