class Solution:
    def reversePairs(self, nums):
        n= len(nums)
        arr= nums
        def merge(arr,left,mid,right):
            count=0
            j= mid+1
            for i in range(left,mid+1):
                while j<= right and arr[i] > 2*arr[j]:
                    j+=1
                count+= j-(mid+1)
            k=0
            l= mid+1
            temp=[]
            while k<mid+1 and l<right+1:
                if arr[k]<arr[l]:
                    temp.append(arr[k])
                    k+=1
                else:
                    temp.append(arr[l])
                    l+=1
            while k<mid+1:
                temp.append(arr[k])
                k+=1
            while l<right+1:
                temp.append(arr[l])
                l+=1
            for i in range(left,right+1):
                arr[i]= temp[i-left]
            return count
        def merge_sortt(arr,left,right):
            inv_count=0
            if right<=left:
                return 0
            mid= (left+right)//2
            inv_count+= merge_sortt(arr,left,mid)
            inv_count+= merge_sortt(arr,mid+1,right)
            inv_count+= merge(arr,left,mid,right)
            return inv_count
        ans= merge_sortt(arr,0,n-1)
        return ans
