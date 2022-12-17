n=int(input("enter the value"))
count=1
row=1
while(row<=n):
    col=1
    while(col<=n):
        print(count,end=" ")
        count=count+1
    print()
    row=row+1    