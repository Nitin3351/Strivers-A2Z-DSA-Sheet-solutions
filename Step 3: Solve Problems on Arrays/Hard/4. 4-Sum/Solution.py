class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=set()
        nums.sort()
        n= len(nums)
        for i in range(n):
            for j in range(i+1,n):
                target2= target- nums[i] - nums[j]
                left= j+1
                right= n-1
                while left<right:
                    twosum= nums[left]+nums[right]
                    if twosum < target2:
                        left+=1
                    elif twosum > target2:
                        right-=1
                    else:
                        res.add((nums[i],nums[j],nums[left],nums[right]))
                        while left < right and nums[left]== nums[left+1]:
                            left+=1
                        while left < right and nums[right]== nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
                        
                while (j+1 < n) and nums[j]== nums[j+1]:
                    j+=1
            while (i+1 < n) and nums[i]== nums[i+1]:
                i+=1
        return list(res)

                    

