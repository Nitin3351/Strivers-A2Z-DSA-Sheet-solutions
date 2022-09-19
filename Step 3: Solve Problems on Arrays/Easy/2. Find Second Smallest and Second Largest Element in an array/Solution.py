#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
	    large= -9223372036854775808
	    sec_large= -9223372036854775808
	    x= len(set(arr))
	    if x<2:
	        return -1
	    for i in arr:
	        if i > large:
	            sec_large = large
	            large = i
	        elif i > sec_large and i != large:
	            sec_large= i
	    return sec_large
	        
	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
