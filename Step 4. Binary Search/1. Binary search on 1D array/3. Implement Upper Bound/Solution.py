def getFloorAndCeil(arr, n, x):
    import sys
    mx= ~sys.maxsize
    mn= sys.maxsize
    floor=-1
    ceil=-1
    for i in arr:
        if i<=x:
            mx= max(mx,i)
            floor= mx
        if i>=x:
            mn= min(mn,i)
            ceil= mn
    return [floor,ceil]


#{ 

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = getFloorAndCeil(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends
