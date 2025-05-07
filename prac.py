mylist = [1, 2, 3, 4]
I = iter(mylist)

for i in range(len(mylist)): 
   print(I.__next__()) # print(next(I))            
