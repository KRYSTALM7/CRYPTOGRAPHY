a = int(input("Enter co-efficient of x: "))
b= int(input("Enter co-efficient of number: "))
z= int(input("Enter Z factor: "))
rh = []
lh = []
for i in range(0,z):
     rh.append((i**3+a*i+b)%z) 
     lh.append((i**2)%z) 
print("LHS: ",lh)
print("RHS: ",rh)
p=[]
for i in range(z):
  for j in range(z):
     if lh[i]==rh[j]:
       p.append((i,j))
print("points on curve E: ",p)
