
class Solution:
	def matSearch(self,mat, N, M, X):
        i=0
        j=M-1
        while i<N and j>=0:
            if mat[i][j]== X:
                return 1
            if mat[i][j]>X:
                j-=1
            else:
                i+=1
        return 0

#{ 

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        arr = [int(x) for x in input().split()]
        x = int(input())
        mat = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                mat[i][j] = arr[i * m + j]
        ob = Solution()
        print(ob.matSearch(mat, n, m, x))
# } Driver Code Ends
