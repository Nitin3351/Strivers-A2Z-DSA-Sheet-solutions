#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        zeros= arr.count(0)
        ones= arr.count(1)
        twos= arr.count(2)
        k=0
        for i in range(zeros):
            arr[k]= 0
            k+=1
        for j in range(ones):
            arr[k]=1
            k+=1
        for l in range(twos):
            arr[k]=2
            k+=1
        return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
