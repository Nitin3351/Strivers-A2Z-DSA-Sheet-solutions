class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def possible(target):
            count=1
            ans=0
            for i in nums:
                if i>target:
                    return False
                if ans+i>target:
                    count+=1
                    ans=i
                else:
                    ans+=i
            if count>k:
                return False
            else:
                return True
        n= len(nums)
        low= min(nums)
        high= sum(nums)
        res=-1
        while low<=high:
            mid= (low+high)>>1
            if possible(mid):
                res= mid
                high= mid-1
            else:
                low= mid+1
        return res
