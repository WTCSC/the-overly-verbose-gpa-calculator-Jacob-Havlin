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
                print("You can't have a negative grade silly!\n"
                "Your grade must be in between 0.0 and 4.0")
        except ValueError:
            print("Please enter a numerical value!")
average_gpa = sum(gpa_list) / len(gpa_list)
print("Calculating gpa.../n"
      f"your gpa is currently at a {average_gpa}")
sections = int(input("Which semester would you like to focus on? "))
if sections == 1:
    print
elif sections == 2:
    