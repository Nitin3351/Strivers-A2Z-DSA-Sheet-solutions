class Solution:
	def count(self,arr, n, x):
		low=0;high= n-1
		cnt=0
		idx=-1
		while low<=high:
		    mid= (low+high)//2
		    if arr[mid]<x:
		        low= mid+1
		    elif arr[mid]>x:
		        high= mid-1
		    else:
		        cnt=1
		        idx= mid
		        break
		if idx>0:
		    mid= idx-1
    		while mid>=0 and arr[mid]==x:
    		    cnt+=1
    		    mid-=1
        	if idx<n-1:
		    mid= idx+1
    		while mid<n and arr[mid]==x:
    		    cnt+=1
    		    mid+=1
    	return cnt

#{ 
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends
