
def sub_grade(sub):
    global total
    global fail
    if sub== 'A+' or sub== 'a+':
        total+=5
    elif sub=='A' or sub== 'a':
        total+=4
    elif sub=='B' or sub=='b':
        total+=3
    elif sub=='C' or sub=='c':
        total+=2
    elif sub=='D' or sub=='d':
        totatl+=1
    elif sub=='F' or sub=='f':
        totatl=fail
    else:
        print("Invalid input")
    return total

total=0
fail=0


#def CheckGrade():
grade1=input("What is your 1st period grade? ")
grade2=(input("What is your 2nd period grade? "))
grade3=(input("What is your 3rd period grade? "))
grade4=(input("What is your 4th period grade? "))
grade5=(input("What is your 5th period grade? "))

#CheckGrade()
sub_grade(grade1)
sub_grade(grade2)
sub_grade(grade3)
sub_grade(grade4)
sub_grade(grade5)

if (grade1 or grade2 or grade3 or grade4 or grade5) in ('F' or 'f'):
    total=fail

gpa=total/5

if gpa>=5:
    gpa=5

if gpa ==0:
    print("Unfortunately, you have failed this semester! ")
    print("Your current GPA is ",gpa)
elif gpa >=0:
    print("Keep up the good work!")
    print("Your current GPA is ",gpa)
else:
    print("Please try again")
