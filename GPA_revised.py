p=print
p("Welcome to the one and only GPA Calculator that talks to much!\nI am going to calculate your GPA based on the 5.0 scale and how many classes you have taken.")
l=[]
t=int(input("How many classes would you like to calculate? "))
for i in range(t):
    while True:
        try:
            g=float(input(f"Please enter your grade (0.0-5.0) for class {i+1} "))
            if 0<=g<=5:l.append(g);break
            p("Your grade must be in between 0.0 and 5.0")
        except:p("Please enter a numerical value!")
a=round(sum(l)/len(l),2)
p(f"Calculating GPA...\nyour overall GPA is currently at a {a}")
while True:
    try:
        s=int(input("Which semester would you like to focus on? "))
        if s in[1,2]:r=["1st","2nd"][s-1];break
        p("You only have 2 semesters silly!")
    except:p("In case you didn't know a semester is expressed in the form of either 1 or 2.")
while 1:
 try:
  c=int(I(f"How many classes were in the {r} semester? "))
  if 0<c<=len(L):break
  p("You must have taken at least 1 class right!")if c<=0 else p(f"You only entered {len(L)} classes total!")
 except:p("Please enter a valid number.")
sem=l[:c]if s==1 else l[t-c:]if t-c>=0 else[]
if sem:
    sem_gpa=round(sum(sem)/len(sem),2)
    p(f"Calculating GPA for {r} semster...\nYour GPA for {r} semester is {sem_gpa}")
    if sem_gpa>a:p("Based on the numbers it appears to be that you are improving your overall GPA")
    elif sem_gpa<a:p("Your GPA is going downhill based on your semester GPA and you should work to improve your grades")
    else:p("Your GPA is staying pretty consistant this semester compared to your overall semester\nKeep working hard!")
else:p(f"There was an error calculating your {r} semester GPA due to incorrect input")
p("You are going to set a new overall GPA goal")
while True:
    try:
        goal=float(input("What is your goal GPA? "))
        if 0<=goal<=5:
            if a>=goal:
                p("Congratulations you have already met this goal")
                if input("Would you like to set a different goal? (yes/no) ").lower()=="no":p("Keep up the good work");exit()
            else:break
        p("Your goal GPA needs to be in between 0.0 and 5.0")
    except:p("Your GPA must be a valid number")
p(f"Your goal GPA is {goal}.\nNow I am going to help you identify which grade you should improve in order to achieve your new GPA")
poss=[i+1 for i in range(len(l))if round(sum(l[:i]+[5.0]+l[i+1:])/len(l),2)>=goal]
if poss:p(f"You could reach your goal GPA of {goal} by improving the following grades:");[p(f"Class {i}")for i in poss]
else:p("Reaching your goal will require improving multiple grades")