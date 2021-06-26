n=int(input('Enter The Value: '))
if n<=100 and n>=80:
    print('your grade is A+')
    print('grade point is 4.00')
elif n<80 and n>=75:
    print('your grade is A')
    print('grade point is 3.75')
elif n<75 and n>=70:
    print('your grade is A-')
    print('grade point is 3.50')
elif n<70 and n>=65:
    print('your grade is B+')
    print('grade point is 3.25')
elif n<65 and n>=60:
    print('your grade is B')
    print('grade point is 3.00')
elif n<60 and n>=55:
    print('your grade is B-')
    print('grade point is 2.75')
elif n<55 and n>=50:
    print('your grade is C+')
    print('grade point is 2.50')
elif n<50 and n>=45:
    print('your grade is C')
    print('grade point is 2.25')
elif n<45 and n>=40:
    print('your grade is D')
    print('grade point is 2.00')
else:
    print('You are failed')

