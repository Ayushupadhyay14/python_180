marks = input("marks: ")

# Convert the input to an integer (or float if fractional marks are possible)
marks = int(marks)  # Use float(marks) if marks can be fractional

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
else:
    print("fail ho gya bhaiya")
