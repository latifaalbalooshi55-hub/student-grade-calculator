print("Student Grade Calculator")

assignment = float(input("Enter assignment grade: "))
quiz = float(input("Enter quiz grade: "))
midterm = float(input("Enter midterm grade: "))
final_exam = float(input("Enter final exam grade: "))

overall_grade = (
    assignment * 0.20
    + quiz * 0.20
    + midterm * 0.25
    + final_exam * 0.35
)

if overall_grade >= 90:
    letter_grade = "A"
elif overall_grade >= 80:
    letter_grade = "B"
elif overall_grade >= 70:
    letter_grade = "C"
elif overall_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"\nOverall grade: {overall_grade:.2f}%")
print(f"Letter grade: {letter_grade}")

if overall_grade >= 60:
    print("Status: Passed")
else:
    print("Status: Failed")
