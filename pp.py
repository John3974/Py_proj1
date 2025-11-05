# Ask the user for their grade's
Grade = int(input("Enter your scores:"))
# figure out the letter grade
if Grade >= 90:
    letter_grade = "A"
elif Grade >= 80:
  letter_grade = "B" 
elif Grade >= 70:
    letter_grade ="C"
elif Grade >= 60:
   letter_grade = "D"
else:
   letter_grade = "F"
# Determine the last_num
last_num = Grade % 10

    
# determine the sign
sign = ""
if last_num >= 7:
   sign = "+"

elif last_num <= 3:
    sign = "-"
   
else:
    sign = ""
    

    
# handling exeptions
if letter_grade =="A" and sign == "+":
    sign = ""
if Grade =="F":
    sign = ""

  


# display the letter grade
print(f"You have  earned {letter_grade}{sign}")