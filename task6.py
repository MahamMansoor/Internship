def convert_to_grade(score):
    """
    Converts a numeric score (0-100) to a letter grade.
    
    Args:
        score (float): The numeric score to convert
        
    Returns:
        str: The corresponding letter grade or 'Invalid' if out of range
    """
    if score > 100 or score < 0:
        return "Invalid"
    elif score >= 97:
        return "A+"
    elif score >= 93:
        return "A"
    elif score >= 90:
        return "A-"
    elif score >= 87:
        return "B+"
    elif score >= 83:
        return "B"
    elif score >= 80:
        return "B-"
    elif score >= 77:
        return "C+"
    elif score >= 73:
        return "C"
    elif score >= 70:
        return "C-"
    elif score >= 67:
        return "D+"
    elif score >= 63:
        return "D"
    elif score >= 60:
        return "D-"
    else:
        return "F"

def print_grade(student_name, student_score, student_grade):
    """
    Prints a formatted grade summary for a student.
    
    Args:
        student_name (str): The student's name
        student_score (float): The student's numeric score
        student_grade (str): The student's letter grade
    """
    print(f"Student {student_name} scored {student_score} → Grade: {student_grade}")

def get_valid_score():
    """
    Gets a valid score from user input .
    Returns None if input is invalid.
    """
    try:
        score = float(input("Enter student score (0-100): "))
        if 0 <= score <= 100:
            return score
        else:
            print("Score must be between 0 and 100.")
            return None
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return None

def main():
    # Get student name
    student_name = input("Enter student name: ")
    
    # Get score (without loop)
    student_score = get_valid_score()
    
    # Only proceed if we got a valid score
    if student_score is not None:
        student_grade = convert_to_grade(student_score)
        print_grade(student_name, student_score, student_grade)
    else:
        print("Cannot calculate grade - invalid score provided.")

if __name__ == "__main__":
    main()
