
class Solution:
    def reverseWords(self,S):
        ans=''
        n= len(S)
        ind=n
        for i in range(n-1,-1,-1):
            if S[i]==".":
                ans+= S[i+1:ind]+"."
                ind=i
        ans+= S[:ind]
        return ans

#{ 

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends
