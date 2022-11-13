class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.


    def inversionCount(self, arr, n):
        def merge(arr,left,mid,right):
            l= arr[left:mid+1]
            r= arr[mid+1:right+1]
            count=0
            i=0
            j=0
            k=left
            n1= len(l); n2=len(r)
            while i<n1 and j<n2:
                if l[i]<=r[j]:
                    arr[k]= l[i]
                    i+=1
                    k+=1
                else:
                    arr[k]= r[j]
                    j+=1
                    count+= (mid+1)-(left+i)
                    k+=1
            while i<n1:
                arr[k]= l[i]
                i+=1
                k+=1
            while j<n2:
                arr[k]= r[j]
                k+=1
                j+=1
            return count
        def merge_sortt(arr,left,right):
            inv_count= 0
            if right>left:
                mid= (left+right)//2
                inv_count+= merge_sortt(arr,left,mid)
                inv_count+= merge_sortt(arr,mid+1,right)
                inv_count+= merge(arr,left,mid,right)
            return inv_count
        ans= merge_sortt(arr,0,n-1)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends
