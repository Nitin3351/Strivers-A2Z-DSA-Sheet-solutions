

class Solution:
	def NthRoot(self, n, m):
		low=1
		high=m
		while low<=high:
		    mid= (low+high)>>1
		    if pow(mid,n)==m:
		        return mid
		    elif pow(mid,n)<m:
		        low= mid+1
		    else:
		        high= mid-1
		return -1


#{ 
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends
