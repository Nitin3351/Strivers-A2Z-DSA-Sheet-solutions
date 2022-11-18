class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened=0
        ans=[]
        for c in s:
            if c=="(" and opened>0:
                ans.append(c)
            if c==")" and opened>1:
                ans.append(c)
            opened+= 1 if c=="(" else -1
        return "".join(ans)
                
