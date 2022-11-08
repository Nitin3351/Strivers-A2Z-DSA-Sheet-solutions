#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        s1= (n*(n+1))//2
        s2= sum(arr)
        p1= (n*(n+1)*(2*n+1))//6
        p2=0
        for i in arr:
            p2+=(i*i)
        s= s1-s2
        p= p1-p2
        x= (s+ (p//s))//2
        y= x-s
        return [y,x]


#{ 

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends
