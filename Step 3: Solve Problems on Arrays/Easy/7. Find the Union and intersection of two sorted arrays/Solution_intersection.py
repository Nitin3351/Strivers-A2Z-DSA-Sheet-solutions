class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a list of integers
	def intersect(self, A, B):
        n= len(A)
        m= len(B)
        i,j= 0,0
        C = []
        while i<n and j<m:
            if A[i] < B[j]:
                i+=1
            elif A[i] > B[j]:
                j+=1
            else:
                C.append(A[i])
                i+=1
                j+=1
        return C 
