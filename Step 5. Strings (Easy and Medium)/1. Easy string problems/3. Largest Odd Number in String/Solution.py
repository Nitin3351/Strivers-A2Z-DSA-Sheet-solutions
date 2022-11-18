class Solution:
    def largestOddNumber(self, num: str) -> str:
        n=len(num)
        x=-1
        for i in range(n-1,-1,-1):
            if int(num[i])%2==1:
                x=i
                break
        return num[:x+1]
