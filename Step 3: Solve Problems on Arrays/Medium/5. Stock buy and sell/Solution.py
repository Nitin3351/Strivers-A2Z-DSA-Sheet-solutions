
def stockBuySell(price, n):
    buy,sell, f = -1,-1,0
    for i in range(n-1):
        if price[i] < price[i+1]:
            if buy == -1:
                buy= i
        elif buy != -1:
            sell =i
            f=1
            print('(',buy,' ',sell,')', sep='',end= ' ')
            buy =-1
        if i == n-2 and buy!=-1:
            f=1
            print('(',buy,' ',i+1,')', sep='',end= ' ')
    if f==0:
        print("No Profit")
    else:
        print()

#{ 
 # Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        price=list(map(int, input().split()))
        stockBuySell(price, n)
# } Driver Code Ends
