

def grade_number():
    grade = int(input ('Enter Grade number :'))
    if grade >= 80:
        print(grade,'A')
    elif grade >= 70:
        print(grade,'B')
    elif grade >= 60:
        print(grade,'C')
    elif grade >= 50:
        print(grade,'D')
    elif grade >= 0 and grade <= 49: 
        print('F')
    else:
        print('input again')
        grade_number()

grade_number()

