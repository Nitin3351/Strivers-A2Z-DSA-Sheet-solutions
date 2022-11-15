
class Solution:
    def median(self, matrix, R, C):
    	low=1
    	high= 2000
    	def cntmid(arr,midd):
    	    l=0
    	    r= len(arr)-1
    	    while l<=r:
    	        md= (l+r)>>1
    	        if arr[md]<=midd:
    	            l= md+1
    	        else:
    	            r= md-1
    	    return l 
    	while low<=high:
    	    mid= (low+high)>>1
    	    count=0
    	    for i in range(R):
    	        count+= cntmid(matrix[i],mid)
    	    if count<=((R*C)//2):
    	        low= mid+1
    	    else:
    	        high= mid-1
        return low

#{ 

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends
