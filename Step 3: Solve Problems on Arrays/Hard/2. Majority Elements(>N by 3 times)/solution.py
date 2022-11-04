#User function Template for python3

class Solution:
    def Solve(self, n, a):
        majority= []
        hashmap= {}
        for i in a:
            hashmap[i]= hashmap[i]+1 if i in hashmap else 1
        for key, value in hashmap.items():
            if value > (n//3):
                majority.append(key)
        if len(majority) == 0:
            majority.append(-1)
        return majority


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        res = ob.Solve(n, a)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends
