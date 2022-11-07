
import math
class Solution:
    def subsetXOR(self, arr, N, K): 
        hashmap={}
        XR=0
        cnt=0
        for i in range(N):
            XR^= arr[i]
            if XR==K:
                cnt+=1
            x= XR^K
            if x in hashmap:
                cnt+= hashmap[x]
            if XR in hashmap:
                hashmap[XR] += 1
            else:
                hashmap[XR] = 1
            
        return cnt



if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K = input().split()
        N = int(N)
        K = int(K)
        arr = input().split(' ')
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        print(ob.subsetXOR(arr,N,K))
# } Driver Code Ends
