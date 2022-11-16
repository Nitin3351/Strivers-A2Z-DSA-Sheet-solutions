
class Solution:
    def floorSqrt(self, x): 
        low=1
        high= x
        while low<=high:
            mid= (low+high)>>1
            if x== mid*mid:
                return mid
            elif x>mid*mid:
                low= mid+1
            else:
                high= mid-1
        return low-1

#{ 

import math
def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
