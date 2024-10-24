""" WAP to enter marks of 3  subject from the userr and store them in a dictionary Start with an Empy Dictionary & add one by 
one USe subject name as key & marks ass values"""

marks={
}
x=int(input("Enter physics:"))
marks.update({"physics":x})
x=int(input("Enter maths:"))
marks.update({"maths":x})
x=int(input("Enter chems:"))
marks.update({"chems":x})

print(marks)