#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
    	l=0
    	for i in range(n):
    	    if arr[i]!=0:
    	        if arr[l]==0:
    	            arr[l], arr[i]= arr[i],0
    	        l+=1
    	

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends
