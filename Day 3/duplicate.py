def duplicate(lst):
    f={}
    count=0
    for i  in lst:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    for i in f:
        if f[i]!=0:
            count+=1
    print(count)
list=[1,2,2,3,1,4]
duplicate(list)