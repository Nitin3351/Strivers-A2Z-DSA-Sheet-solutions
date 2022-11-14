
class Solution:
    def searchInsertK(self, Arr, N, k):
        low=0
        high=N-1
        while low<=high:
            mid= (high+low)//2
            if Arr[mid]>k:
                high= mid-1
            elif Arr[mid]<k:
                low=mid+1
            else:
                return mid
        return high+1


#{ 
if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends
