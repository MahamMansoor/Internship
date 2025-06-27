# Store immutable student IDs using a tuple
ids = (1001, 1002, 1003, 1004, 1005)

# Display the student IDs
print("Student IDs (Immutable):", ids)

# Create a set to store unique course names
courses = {"Python", "AI", "ML", "CYS"}  # Sets automatically ignore duplicates

# Display initial courses
print("\nInitial Courses Offered:", courses)

# Add a new course
courses.add("Data Science")  # Adds a new course to the set
print("After Adding 'Data Science':", courses)

# Try adding a duplicate course
courses.add("Python")  # This won't create a duplicate in the set
print("After Attempting to Add Duplicate 'Python':", courses)

# Remove a course
courses.remove("ML")  # Removes 'ML' from the set
print("After Removing 'ML':", courses)

# Display all remaining courses 
print("\nFinal Course List:", ', '.join(courses))  # Joins set items into a string
