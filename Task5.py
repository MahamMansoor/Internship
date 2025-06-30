# Function to calculate weighted GPA from (grade, credit_hour) pairs
def calculate_gpa(grades: list[tuple[str, float]]) -> float:
    # Grade to GPA mapping
    grade_points = {
        "A+": 4.0, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "F": 0.0
    }

    t_points = 0
    t_credits = 0

    # Process each (grade, credit) pair
    g1, g2, g3 = grades[0], grades[1], grades[2]

    # Extract grade and credit
    gp1 = grade_points.get(g1[0], 0.0) * g1[1]
    gp2 = grade_points.get(g2[0], 0.0) * g2[1]
    gp3 = grade_points.get(g3[0], 0.0) * g3[1]

    t_points = gp1 + gp2 + gp3
    t_credits = g1[1] + g2[1] + g3[1]

    # Calculate weighted GPA
    if total_credits == 0:
        return 0.0
    return t_points / t_credits


# Function to print summary of GPA
def print_gpa(student_name: str, gpa: float):
    print(f"Student {student_name} has GPA: {round(gpa, 2)}")


# --- Test the functions ---

grades_input = [('A', 3), ('A+', 3), ('A', 2)]
student_name = "Maham"

# Calculate GPA
gpa_result = calculate_gpa(grades_input)

# Named parameter call
print_gpa(student_name='Maham', gpa=gpa_result)



---------------------------------------------------------------------------------------------------------------------


# ---- Using USer Input   (METHOD 02) ------------- 
# Function to calculate weighted GPA
def calculate_gpa(grades: list[tuple[str, float]]) -> float:
    grade_points = {
        "A+": 4.0, "A": 4.0, "A-": 3.7,
        "B+": 3.3, "B": 3.0, "B-": 2.7,
        "C+": 2.3, "C": 2.0, "C-": 1.7,
        "F": 0.0
    }

    t_points = 0
    t_credits = 0

    for grade, credit in grades:
        point = grade_points.get(grade.upper(), 0.0)
        t_points += point * credit
        t_credits += credit

    if t_credits == 0:
        return 0.0
    return round(t_points / t_credits, 2)


# Function to print GPA summary
def print_gpa(student_name: str, gpa: float):
    print(f"\n🎓 Student {student_name} has GPA: {round(gpa, 2)}")


# --- User Input Section ---

# Get student name
name = input("Enter student name: ")

# Get number of subjects
no_sub = int(input("Enter number of subjects: "))

# Input grades and credit hours
grade_list = []
for i in range(no_sub):
    grade = input(f"Enter grade for subject {i+1} (e.g. A, B+, C-): ")
    credit = float(input(f"Enter credit hours for subject {i+1}: "))
    grade_list.append((grade, credit))

# Calculate GPA and display summary
gpa_result = calculate_gpa(grades=grade_list)  # Named argument
print_gpa(student_name=name, gpa=gpa_result)    # Named arguments
