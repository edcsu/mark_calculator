#Name of program:Grading
#Enter name
name=raw_input("Enter your name: ")
#Enter the student no.
student_no = raw_input("Enter your student number:")
#Enter test and course values
test1 = input("Enter your marks for test 1: ")
test2 = input("Enter your marks for test 2: ")
cw = input("Enter your marks for your course work: ")
#Calculate the best 2 of 3
#best1 = 0
#best2 = 0
def two_biggest(a, b, c):
    if a>=b>c :
        print a, b, 'are the biggest two'
    elif b>=c>a:
        print b, c, 'are the biggest two'
    elif a>=c>b:
        print c, a, 'are the biggest two'
    else:
        print 'none'

print two_biggest(test1, test2, cw)
#avg = float(best1) + float(best2) /2
#mark_1 = float(45)/float(100) * avg
#print mark_1
