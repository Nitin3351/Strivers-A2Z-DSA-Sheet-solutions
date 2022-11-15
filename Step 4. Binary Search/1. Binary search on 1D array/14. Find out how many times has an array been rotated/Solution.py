
class Solution:
    def findKRotation(self,arr,  n):
        low=0
        high= n-1
        while low<high:
            mid= (low+high)>>1
            if arr[mid]>arr[high]:
                low= mid+1
            else:
                high= mid
        return low


#{ 
if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1
# } Driver Code Ends
