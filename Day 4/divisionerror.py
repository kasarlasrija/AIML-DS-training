x,y=map(int,input().split())
try:
    z=x/y
except:
    print("Error:Divisionby zero is not allowed")
else:
    print(z)
finally:
    print("done")