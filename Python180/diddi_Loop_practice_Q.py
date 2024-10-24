"""Q(1) -> to print number from 1 to 100 >"""

# i=1
# while i<=100:
#   print(i)
#   i+=1

"""Q(2)-> print number from 100 to 1 """
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1  # Decrement statement should be inside the loop

""" Print the multiplication table of a number N """

# def print_multiplication_table(N):
#     for i in range(1, 11):  # Multiplication table up to 10
#         print(f"{N} * {i} = {N * i}")

# # Example usage:
# number = int(input("Enter a number: "))
# print_multiplication_table(number)


""" Q -> search for a number x in this tuple using loop"""

nums=(1,4,9,16,25,36,49,64,81,100)
i=0
while i<len(nums):
  print(nums[i])
  i+=1
print(nums[6])