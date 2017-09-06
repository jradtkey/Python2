from random import randint

def grades(students):
    print "Scores and Grades"
    for value in range(0,students):
        grade = randint(60,100)
        if (grade < 70) & (grade > 59):
            print "Score: " + str(grade) + "; Your grade is a D"
        elif (grade < 80) & (grade > 69):
            print "Score: " + str(grade) + "; Your grade is a C"
        elif (grade < 90) & (grade > 79):
            print "Score: " + str(grade) + "; Your grade is a B"
        elif (grade < 101) & (grade > 89):
            print "Score: " + str(grade) + "; Your grade is an A"
    print "End of the program. Goodbye!"
grades(10)
