class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr=[]
        n= numRows
        for i in range(n):
            temp=[]
            for j in range(i+1):
                if j==0 or i==j:
                    temp.append(1)
                else:
                    temp.append(arr[i-1][j]+ arr[i-1][j-1])
            arr.append(temp)
        return arr
	                
