def read_student_marks(file_path):
    student_marks = {}
    skipped_entries = 0

    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):
                try:
                    line = line.strip()
                    if not line:
                        raise ValueError("Empty line")
                    name, mark = line.split(',')
                    name = name.strip()
                    mark = mark.strip()

                    if name == "" or mark == "":
                        raise ValueError("Missing name or mark")

                    mark = int(mark)  # Try converting to integer
                    student_marks[name] = mark

                except ValueError as e:
                    print(f"Skipped line {line_number}: '{line}' ({e})")
                    skipped_entries += 1

    except FileNotFoundError:
        raise  # We'll handle this in the input loop

    return student_marks, skipped_entries


def display_results(student_marks):
    print("\n🎓 Student Marks:")
    try:
        total = 0
        for name, mark in student_marks.items():
            print(f"{name}: {mark}")
            total += mark

        average = total / len(student_marks)
        print(f"\n Average Mark: {average:.2f}")

    except ZeroDivisionError:
        print(" No valid student data to calculate average.")


# --- Main Program ---
while True:
    file_path = input(" Enter the path to the student marks file: ")
    try:
        marks, skipped = read_student_marks(file_path)
        display_results(marks)
        print(f"\n⏭ Skipped entries: {skipped}")
        break  # Exit loop if successful
    except FileNotFoundError:
        print(" File not found. Please try again.\n")
