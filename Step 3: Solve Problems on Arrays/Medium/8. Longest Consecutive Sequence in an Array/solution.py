
class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        hashset= {key:value for value, key in enumerate(arr)}
        longstreak,curstreak=0,0
        for i in arr:
            if i-1 not in hashset:
                curstreak=1
                curnum=i
                while (curnum+1) in hashset:
                    curstreak+=1
                    curnum+=1
            longstreak= max(longstreak,curstreak)
        return longstreak
 
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
# } Driver Code Ends
