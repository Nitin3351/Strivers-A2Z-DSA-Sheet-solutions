class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low= max(weights)
        high= sum(weights)
        def feasible(capacity):
            total=0
            count=1
            for wts in weights:
                if total+wts>capacity:
                    total= wts
                    count+=1
                else:
                    total+=wts
            return count<=days
        while low<high:
            mid= (low+high)>>1
            if feasible(mid):
                high= mid
            else:
                low= mid+1
        return low
