marks =  input("Please enter your marks: ")
marks = int(marks)

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    print("A-")
elif marks >= 50:
    print("B")
else:
    print("F")