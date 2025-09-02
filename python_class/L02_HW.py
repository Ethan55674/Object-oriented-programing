

def grade():
    q = 'y'
    y = 't'
    while(True):
        y = input("(A)dd, (R)emove, (M)odify,(P)rint all, (Q)uit: ")
        if (y == 'a'):
            student_1_Name = input("Enter the students name: ")
            student_1_grade = int(input("Enter the students grade: "))
        y = input("(A)dd, (R)emove, (M)odify,(P)rint all, (Q)uit: ")
        if (y == 'a'):
            student_2_Name = input("Enter the students name: ")
            student_2_grade = int(input("Enter the students grade: "))
        y = input("(A)dd, (R)emove, (M)odify,(P)rint all, (Q)uit: ")
        if (y == 'a'):
            student_3_Name = input("Enter the students name: ")
            student_3_grade = int(input("Enter the students grade: "))
        y = input("(A)dd, (R)emove, (M)odify,(P)rint all, (Q)uit: ")
        if (y == 'r'):
            removal = input("What student would you like to remove: ")
            if(removal == student_1_Name):
                student_1_Name = None
                student_1_grade = None
            if (removal == student_2_Name):
                student_2_Name = None
                student_2_grade = None
            if (removal == student_3_Name):
                student_3_Name = None
                student_3_grade = None
        y = input("(A)dd, (R)emove, (M)odify,(P)rint all, (Q)uit: ")
        if (y == 'm'):
            modify = input("Enter the name of the student to modify: ")
            if (modify == student_1_Name):
                print("The old grade is:", student_1_grade)
                student_1_grade = int(input("Enter the new grade: "))
            if (modify == student_2_Name):
                print("The old grade is:", student_2_grade)
                student_2_grade = int(input("Enter the new grade: "))
            if (modify == student_3_Name):
                print("The old grade is:", student_3_grade)
                student_3_grade = int(input("Enter the new grade: "))
        y = input("(A)dd, (R)emove, (M)odify,(P)rint all, (Q)uit: ")
        if(y == 'p'):
            if (student_1_grade == None):
                average= ((student_2_grade+student_3_grade)/2)
                print("The average is:",average)
                print(student_2_Name,":",student_2_grade)
                print(student_3_Name,":",student_3_grade)
            if (student_2_grade == None):
                average= ((student_1_grade+student_3_grade)/2)
                print("The average is:",average)
                print(student_1_Name,":",student_1_grade)
                print(student_3_Name,":",student_3_grade)
            if (student_3_grade == None):
                average = ((student_1_grade+student_2_grade)/2)
                print("The average is:",average)
                print(student_1_Name,":",student_1_grade)
                print(student_2_Name,":",student_2_grade)
        y = input("(A)dd, (R)emove, (M)odify,(P)rint all, (Q)uit: ")
        if (y == "q"):
            break
        
        


grade()    

