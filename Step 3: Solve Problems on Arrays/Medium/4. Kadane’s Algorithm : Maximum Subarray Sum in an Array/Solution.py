class Solution:
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        import sys
        msf= ~sys.maxsize
        meh= 0
        start=0
        end=0
        for i in range(N):
            meh+= arr[i]
            if meh > msf:
                msf= meh
                end= i
            if meh<0:
                meh=0
                s=i+1
        return msf
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
