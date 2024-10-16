name = input("Enter your name: ")
section = input("Enter your section: ")
preGrade = float(input("Enter your Prelim grade: "))
if preGrade >= 40.00 and preGrade <= 100.00:
    print()
    midGrade = float(input("Enter your Midterm grade: "))
    if midGrade >= 40.00 and midGrade <= 100.00:
        print()
        finGrade = float(input("Enter your Finals grade: "))
        if finGrade >= 40.00 and finGrade <= 100.00:
            print()
        else:
            print("only values between 40.00 and 100.00 are valid")
    else:
        print("only values between 40.00 and 100.00 are valid")
else:
    print("only values between 40.00 and 100.00 are valid")
    
finalGrade = round (preGrade * 0.3333) + (midGrade * 0.3333) + (finGrade * 0.3333)

if finalGrade >= 99.00:
    gradePoint = 1.00
    description = "Excellent"
elif finalGrade >= 96.00:
    gradePoint = 1.25
    description = "Outstanding"
elif finalGrade >= 93.00:
    gradePoint = 1.50
    description = "Superior"
elif finalGrade >= 90.00:
    gradePoint = 1.75
    description = "VeryGood"
elif finalGrade >= 87.00:
    gradePoint = 2.00
    description = "Good"
elif finalGrade >= 84.00:
    gradePoint = 2.25
    description = "Satifactiory"
elif finalGrade >= 81.00:
    gradePoint = 2.50
    description = "Fairly Satisfactory"
elif finalGrade >= 78.00:
    gradePoint = 2.75
    description = "Fair"
elif finalGrade >= 75.00:
    gradePoint = 3.00
    description = "Passed"
else: 
    gradePoint = 5.00
    description = "Failed"
    
print (f"Name of student: {name}")
print (f"Section: {section}")
print (f"Final Grade: {finalGrade:.2f}")
print (f"GPA: {gradePoint}")
print (description)
    
    
    


    


            
            