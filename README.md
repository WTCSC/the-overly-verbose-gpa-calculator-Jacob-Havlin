[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21078749)

# The Overly Verbose GPA Calculator

## About

The Overly Verbose GPA Calculator is a Python program that enthusiastically walks you through the process of calculating your GPA on a 5.0 scale. It doesn’t just give you results — it narrates every step with personality.

Beyond simple GPA calculation, it also includes a semester analysis feature that evaluates your academic performance and gives personalized feedback based on your final GPA.


## Features

* GPA calculation on a 5.0 scale
* Input validation for numeric grades and number of classes
* Rounded GPA displayed to two decimal places
* Verbose narration of every step (it really talks a lot)
* Semester Analysis that provides feedback such as:

  * “Excellent work this semester!”
  * “Keep pushing — there’s always room to grow.”
  * “You might want to study a bit harder next time.”
* Lightweight — no external dependencies


## How It Works

1. The program greets you (at length).
2. You enter the number of classes taken this semester.
3. For each class, you input your grade (0.0–5.0).
4. The calculator validates your input and stores the grades in a list.
5. It computes your average GPA by summing all grades and dividing by the total number of classes.
6. The final GPA is displayed, followed by a semester analysis — a short message based on your performance range.


## Example Output

```
Welcome to the one and only GPA Calculator that talks too much!
I am going to calculate your GPA based on the 5.0 scale and how many classes you have taken.
How many classes would you like to calculate? 4

Please enter your grade (0.0–5.0) for class 1: 4.7
Please enter your grade (0.0–5.0) for class 2: 4.9
Please enter your grade (0.0–5.0) for class 3: 4.5
Please enter your grade (0.0–5.0) for class 4: 4.6

Your GPA is: 4.68

--- Semester Analysis ---
Excellent work this semester! Keep up the great effort!
```

If you score lower, the analysis might instead say:

```
Your GPA is: 3.1
--- Semester Analysis ---
Good job! You're doing fine, but there’s always room to improve.
```

or

```
Your GPA is: 2.2
--- Semester Analysis ---
It seems this semester was tough — stay focused and you’ll bounce back!
```

## Usage

Run the script directly in a terminal:

```bash
python GPA.py
```

Then follow the on-screen prompts to enter your grades.
At the end, you’ll receive both your final GPA and a friendly (sometimes brutally honest) semester summary and recommandiations on what grade to improve in order to meet a goal GPA.



## Code Overview

* **`gpa_list`** stores user-inputted grades
* **`subjects`** holds the total number of classes
* **`while True`** and `try/except` blocks handle input validation
* GPA is computed using:

  ```python
  gpa = sum(gpa_list) / len(gpa_list)
  ```
* Final output includes:

  * The numeric GPA (rounded to two decimals)
  * A semester feedback message determined by GPA range


## Requirements

* Python 3.6 or newer
* No additional libraries needed


## License

This project is open-source and available for educational and personal use.
