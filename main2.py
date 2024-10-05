input1 = input("Surename: ")
input2 = float(input("points: "))

if input2 > 80:
    a = "pass the exam"
else:
    a = "not pass the exam"

print(f"{input1} did {a}")
