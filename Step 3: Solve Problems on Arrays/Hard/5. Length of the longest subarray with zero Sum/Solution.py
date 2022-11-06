
class Solution:
    def maxLen(self, n, arr):
        hashset={}
        maxx= 0
        cursum=0
        for i in range(n):
            cursum+= arr[i]
            if cursum== 0:
                maxx= i+1
            elif cursum  not in hashset:
                hashset[cursum]=i+1
            else:
                maxx= max(maxx,i-hashset[cursum]+1)
        return maxx

 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
