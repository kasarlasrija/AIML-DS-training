def remove(lst):
    f={}
    for i in lst:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    for i in f:
        if f[i]!=1:
            lst.remove(i)
            print(i)
list=[1,2,3,3,4]
remove(list)