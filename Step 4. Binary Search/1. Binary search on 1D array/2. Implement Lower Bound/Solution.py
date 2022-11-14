class Solution:
    def findFloor(self,A,N,X):
        l=0
        r=N-1
        while l<=r:
            mid= l+(r-l)//2
            if A[mid]< X:
                l=mid+1
            elif A[mid]>X:
                r= mid-1
            else:
                return mid
        if r>=0:
            return r
        else:
            return -1
 
#{ 
 # Driver Code Starts
import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
