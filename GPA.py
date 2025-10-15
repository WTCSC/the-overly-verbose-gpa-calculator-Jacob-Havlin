print("Welcome to the one and only GPA Calculator that talks to much!")
print("I am going to calculate your GPA based on the 4.0 scale and how many classes you have taken.")
subjects = int(input("How many classes would you like to calculate? "))
for subject in range(subjects):
    sentence = float(input(f"Please enter your grade (0.0-4.0) for class {subject+1} "))
    
