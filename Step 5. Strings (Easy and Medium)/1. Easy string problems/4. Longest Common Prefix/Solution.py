class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x= len(min(strs))
        cnt=0
        flag= True
        while cnt<x and flag:
            for i in range(len(strs)-1):
                if strs[i][cnt]!=strs[i+1][cnt]:
                    flag=False
                    break
            cnt+=1
        if flag == False:
            return strs[0][:cnt-1]
        else:
            return strs[0][:cnt]
