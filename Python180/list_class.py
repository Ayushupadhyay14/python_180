# how to create list class
#l1=[10,40,20,30]
#print(type(l1))
#l2=[23,45,67,'hello']
#print(type(l2))
#l3=[2.34,'hello',3+6j,True,34]
#print(type(l3))
#l4=[20,30,40,50,60]
#print(l4)
#print(" ")
#print(l4[0],l4[-1],l4[-2]) #20,30,40
l5=[40,43.54,3+5j,10,"hello"]
print(type(l5))
print(l5[2],l5[3],l5[1])
l6=[-4,-5.67,-3,-12]
print(l6)
print(l6[1],l6[3]) ## this is a nigetive indexin in python
for n in l5:
 print(n,end="\t")
 print("\n")
del l6[0]  # this keyword to use delete element of the index
print(l6)
l6[2]=23 # this keywort to use to editkey eord of the insex
print(l6[2])