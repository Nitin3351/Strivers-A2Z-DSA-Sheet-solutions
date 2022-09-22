#User function Template for python3
class Solution:
    def search(self, A, N):
        x= A[0]
        for i in A[1:]:
            x= x^i
        return x

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		print(ob.search(arr, n)) 
# } Driver Code Ends
