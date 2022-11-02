#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        for i in range(N-2,-2,-1):
            if arr[i] < arr[i+1]:
                break
        if i>=0:
            for j in range(N-1,i,-1):
                if arr[j] > arr[i]:
                    break
            arr[i], arr[j] = arr[j], arr[i]
            arr= arr[:i+1]+arr[:i:-1]
        else:
            arr= arr[::-1]
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends
