print("Welcome to the one and only GPA Calculator that talks to much!")
print("I am going to calculate your GPA based on the 4.0 scale and how many classes you have taken.")
gpa_list = []
subjects = int(input("How many classes would you like to calculate? "))
for subject in range(subjects):
    while True:
        try:
            grade = float(input(f"Please enter your grade (0.0-4.0) for class {subject+1} "))
            if 0.0 <= grade <= 4.0:
                gpa_list.append(grade)
                break
            else:
                print("Your grade must be in between 0.0 and 4.0")
        except ValueError:
            print("Please enter a numerical value!")
average_gpa = round(sum(gpa_list) / len(gpa_list), 2)
print("Calculating gpa...\n"
      f"your gpa is currently at a {average_gpa}")
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
while True:
    try:
        class_semester = int(input(f"How many classes were in the {rank} semester? "))
        if class_semester > 0:
            break
        else:
            print("You must have taken at least 1 class right?")
    except ValueError:
        print("Please enter a valid number.")
if sections == 1:
    semester = gpa_list[:class_semester]
elif sections == 2:
    semester_index_grades_2nd = subjects - class_semester
    if semester_index_grades_2nd < 0 or semester_index_grades_2nd >= len(gpa_list):
        print("ERROR: number of classes do not align with total grades calculated")
        semester_gpa = None
    else:
        semester = gpa_list[semester_index_grades_2nd:]
if semester and len(semester) > 0:
    semester_gpa = round(sum(semester) / len(semester), 2)
    print(f"Calculating GPA for {rank}...")
    print(f"Your GPA for {rank} semester is {semester_gpa}")
else:
    print(f"There was an error calculating your {rank} semester GPA due to incorrect input")
if semester_gpa > average_gpa:
    print("Based on the numbers it appears to be that you are improving your overall GPA")
elif semester_gpa <  average_gpa:
    print(f"Your GPA is going downhill based on your semester GPA and you should work to improve your grades")
else:
    print("Your GPA is staying pretty consistant this semester compared to your overall semester\n"
          "Keep working hard!")
