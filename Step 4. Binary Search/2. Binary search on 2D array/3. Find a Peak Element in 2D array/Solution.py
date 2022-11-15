class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n= len(mat)
        low= 0 
        high= n-1
        while low<high:
            mid= (low+high)>>1
            if max(mat[mid]) > max(mat[mid+1]):
                high= mid
            else:
                low= mid+1
        return [high,mat[high].index(max(mat[high]))]
