classno=None
while classno==None:
    try:
        classno=int(input("How many class are you taking? "))
    except:
        print("Invalid. Please enter a number.\n")
output=0
i=0
while i<classno:
    grade=input("Enter your letter grade for Class %s. " %(str(i+1)))
    grade=grade.upper()
    if grade== 'A+' or grade== 'A' or grade== 'B' or grade== 'C' or grade== 'D' or grade== 'F':
        i+=1
        if grade== 'A+':
            output+=5
        elif grade== 'A':
            output+=4
        elif grade== 'B':
            output+=3
        elif grade== 'C':
            output+=2
        elif grade== 'D':
            output+=1
        elif grade== 'F':
            output+=0
        print(output)
    else:
        print("Error. Please enter a valid letter grade (A, B, C, D, F)\n")
average="%.2f" % (float(output)/float(classno))
print("Your current GPA is: %s " %(str(average)))
