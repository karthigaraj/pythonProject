t=int(input("Enter no of testcases"))
first=int(0)
second=int(0)
k=int(0)
for i in range(t):
    lst=[]
    for j in range(0, 3):
        ele = int(input())
        lst.append(ele)
    print(lst)
    while(k<3):
        if lst[k]>first:
            second=first
            first=lst[k]
        elif lst[k]>second and lst[k]<first:
            second=lst[k]
        k=k+1
    print(second)
    lst.clear()