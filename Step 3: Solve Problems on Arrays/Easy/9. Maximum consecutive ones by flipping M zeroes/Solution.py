
# m is maximum number of zeroes allowed to flip, n is size of array 
def findZeroes(arr, n, m) :
    wL= wR= 0
    bestWindow=0
    zerocnt= 0
    
    while wR<n:
        if zerocnt<=m:
            if arr[wR]==0:
                zerocnt+=1
            wR+=1
        if zerocnt > m:
            if arr[wL]==0:
                zerocnt-=1
            wL+=1
        if (wR-wL > bestWindow) and (zerocnt<=m):
            bestWindow= wR-wL
    return bestWindow


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        m=int(input())
        ans= findZeroes(arr, n, m)
        print(ans)
        tc=tc-1
# } Driver Code Ends
