#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        sm= ans=0
        mp={}
        mp[0]= -1
        for i in range(n):
            sm+= arr[i]
            if sm==k:
                ans= i+1
            if sm-k in mp:
                ans= max(ans,i-mp[sm-k])
            if sm not in mp:
                mp[sm]= i
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends
