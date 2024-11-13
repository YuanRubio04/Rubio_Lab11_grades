grades = []
numofgrd = 5
passing_grade = 75

for i in range(numofgrd):
        while True:
                grade = int(input(f"Enter grade for student {i + 1}: "))
                if 40 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 40 and 100. Please try again.")
            

print("\nGrades entered:", grades)

    
avrgrd = sum(grades) / numofgrd

    
passstdnt = sum(1 for grade in grades if grade >= passing_grade)

    
passprcnt = (passstdnt / numofgrd) * 100

    
print(f"\nAverage grade: {avrgrd:}")
print(f"Number of students with passing grade: {passstdnt}")
print(f"Passing percentage: {passprcnt:}%")



    



    