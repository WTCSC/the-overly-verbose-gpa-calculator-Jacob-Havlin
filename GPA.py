#user friendly introduction
print("Welcome to the one and only GPA Calculator that talks to much!")
print("I am going to calculate your GPA based on the 5.0 scale and how many classes you have taken.")

gpa_list = []
subjects = int(input("How many classes would you like to calculate? "))

#prevents errors and bad data
for subject in range(subjects):
    while True:
        try:
            grade = float(input(f"Please enter your grade (0.0-5.0) for class {subject+1} "))
            if 0.0 <= grade <= 5.0:
                gpa_list.append(grade)
                break
            else:
                print("Your grade must be in between 0.0 and 5.0")
        except ValueError:
            print("Please enter a numerical value!")

average_gpa = round(sum(gpa_list) / len(gpa_list), 2)
print("Calculating GPA...\n"
      f"your overall GPA is currently at a {average_gpa}")

#Helps compare performance in both semesters
while True:
    try:
        sections = int(input("Which semester would you like to focus on? "))
        if sections == 1:
            rank = ("1st")
            break
        elif sections == 2:
            rank = ("2nd")
            break
        else:
            print("You only have 2 semesters silly!")
    except ValueError:
        print("In case you didn't know a semester is expressed in the form of either 1 or 2.")

#Needed to slice the GPA list to calculate just that semester’s average.
while True:
    try:
        class_semester = int(input(f"How many classes were in the {rank} semester? "))
        if class_semester <= 0:
            print("You must have taken at least 1 class right?")
        elif class_semester > len(gpa_list):
            print("You have to many classes")
        else:
            break 
    except ValueError:
        print("Please enter a valid number.")

#Slicing the list lets the program focus on just that semester’s grades.
if sections == 1:
    semester = gpa_list[:class_semester]
elif sections == 2:
    semester_index_grades_2nd = subjects - class_semester
    if semester_index_grades_2nd < 0 or semester_index_grades_2nd >= len(gpa_list):
        print("ERROR: number of classes do not align with total grades calculated")
        semester_gpa = None
    else:
        semester = gpa_list[semester_index_grades_2nd:]

#Semester progress report
if semester and len(semester) > 0:
    semester_gpa = round(sum(semester) / len(semester), 2)
    print(f"Calculating GPA for {rank} semster...")
    print(f"Your GPA for {rank} semester is {semester_gpa}")
else:
    print(f"There was an error calculating your {rank} semester GPA due to incorrect input")

#adds personality to the calculator
if semester_gpa > average_gpa:
    print("Based on the numbers it appears to be that you are improving your overall GPA")
elif semester_gpa <  average_gpa:
    print(f"Your GPA is going downhill based on your semester GPA and you should work to improve your grades")
else:
    print("Your GPA is staying pretty consistant this semester compared to your overall semester\n"
          "Keep working hard!")

#Makes the program motivational
print("You are going to set a new overall GPA goal")
goal_set = False

#Adds logical validtion and adds more personality
while True:
    try:
        prompted_gpa = float(input("What is your goal GPA? "))
        if 0.0 <= prompted_gpa <= 5.0:
            if average_gpa >= prompted_gpa <= 5.0:
                print("Congratulations you have already met this goal")
                revert = input("Would you like to set a different goal? (yes/no) ")
                if revert.lower() == "no":
                    print("Keep up the good work")
                    exit()
                else: 
                    continue
            else:
                break
        else:
            print("Your goal GPA needs to be in between 0.0 and 5.0")
    except ValueError:
        print("Your GPA must be a valid number")

print(f"Your goal GPA is {prompted_gpa}.\n"
"Now I am going to help you identify which grade you should improve in order to achieve your new GPA")

#Helps identify which classes would make the biggest difference if improved.
possible_grade = []
for subject in range(len(gpa_list)):
    temp_list = gpa_list.copy()
    temp_list[subject] = 5.0
    new_average = round(sum(temp_list) / len(temp_list), 2)
    if new_average >= prompted_gpa:
        possible_grade.append(subject+1)

#Gives actionable feedback to the user
if possible_grade:
    print(f"You could reach your goal GPA of {prompted_gpa} by improving the following grades:")
    for subject in possible_grade:
        print(f"Class {subject}")
else:
    print("Reaching your goal will require improving multiple grades")