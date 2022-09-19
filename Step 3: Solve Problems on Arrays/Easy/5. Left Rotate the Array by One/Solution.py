class Solution:
    def leftRotate(self, arr, k, n):
        k = k % n
        tmp= [0]*k
        for i in range(k):
            tmp[i]= arr[i]
        for j in range(n-k):
            arr[j]= arr[j+k]
        for x in range(n-k,n):
            arr[x] = tmp[x-n+k]

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(a,k,n)
        print(*a)
# } Driver Code Ends
