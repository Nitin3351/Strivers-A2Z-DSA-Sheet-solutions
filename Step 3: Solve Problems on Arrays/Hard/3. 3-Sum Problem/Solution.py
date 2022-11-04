class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n= len(nums)
        result=[]
        for i in range(n-2):
            if i==0 or (i>0 and nums[i]!= nums[i-1]):
                low= i+1
                high= n-1
                som= 0- nums[i]
                temp=[]
                while (low<high):
                    if nums[low]+ nums[high] == som:
                        temp=[nums[i],nums[low],nums[high]]
                        result.append(temp)
                        while low<high and nums[low] == nums[low+1]:
                            low+=1
                        while low<high and nums[high] == nums[high-1]:
                            high-=1
                        low+=1
                        high-=1
                    elif nums[low]+ nums[high]< som:
                        low +=1
                    else:
                        high-=1
        return result        
        
