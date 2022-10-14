n=int(input("Number of Test Matches in a series"))
dict1={}
dict2={}
dict3={}
for i in range(n):
     str=input("Enter Test Series Number")
     m=int(input("Number of Players in each test match"))
     for j in range(m):
      
       name=input("Enter Name of player")
       runs=input("Enter runs scored by the player")
       dict1[name]=runs

       dict2[str]=runs
       
       dict3={dict1:{},dict2:{}}
#print(dict1)
#print(dict2)
print(dict3)
#match1=
