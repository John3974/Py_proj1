# ask the user for their grades
grades = int(input("Enter your grade scores: "))


# figure out the letter grade
if grades >= 90:
   letter_grade = "A"
elif grades >= 80:
    letter_grade = "B"
elif grades >= 70:
    letter_grade = "C"
elif grades >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
# determine the last digit of the grade
last_digit = grades % 10


# determine the sign
sign = ""
if last_digit >= 7:
    sign = "+"
elif last_digit <= 3:
    sign = "-"
else:
    sign = ""

# Handle exeptions:(no A+ ,F-, F+)
if letter_grade == "A" and sign == "+":
    sign = ""
    
if letter_grade == "F":
    sign = ""

if grades > 70:
    print("Congratulations, you passed!")
   
else:
    print("Sorry, you did not pass, better luck next time.")

# display the letter grade
print(f"You have earned grade {letter_grade}{sign}")

