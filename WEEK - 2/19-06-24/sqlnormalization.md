# Importing necessary library for display
import pandas as pd

# First Normal Form (1NF)
print("First Normal Form (1NF):")

# Initial table (Not in 1NF)
data = {'student_id': [1, 2], 'name': ['John Doe', 'Jane Smith'], 'courses': ['Math, Science', 'English, History']}
df_initial = pd.DataFrame(data)
print("Initial table (Not in 1NF):")
print(df_initial)

# Converted to 1NF
data_1nf = {'student_id': [1, 1, 2, 2], 'name': ['John Doe', 'John Doe', 'Jane Smith', 'Jane Smith'], 'course': ['Math', 'Science', 'English', 'History']}
df_1nf = pd.DataFrame(data_1nf)
print("\nConverted to 1NF:")
print(df_1nf)

# Second Normal Form (2NF)
print("\nSecond Normal Form (2NF):")

# Initial table (1NF but not 2NF)
data_1nf = {'enrollment_id': [1, 2, 3], 'student_id': [1, 1, 2], 'course': ['Math', 'Science', 'English'], 'instructor': ['Mr. Smith', 'Dr. Brown', 'Ms. White']}
df_1nf_to_2nf = pd.DataFrame(data_1nf)
print("Initial table (1NF but not 2NF):")
print(df_1nf_to_2nf)

# Splitting into two tables to achieve 2NF
data_students = {'student_id': [1, 2], 'name': ['John Doe', 'Jane Smith']}
df_students = pd.DataFrame(data_students)

data_courses = {'enrollment_id': [1, 2, 3], 'student_id': [1, 1, 2], 'course': ['Math', 'Science', 'English'], 'instructor': ['Mr. Smith', 'Dr. Brown', 'Ms. White']}
df_courses = pd.DataFrame(data_courses)

print("\nSplitting into two tables to achieve 2NF:")
print("Students table:")
print(df_students)
print("\nCourses table:")
print(df_courses)

# Third Normal Form (3NF)
print("\nThird Normal Form (3NF):")

# Initial table (2NF but not 3NF)
data_2nf = {'student_id': [1, 2], 'student_name': ['John Doe', 'Jane Smith'], 'course': ['Math', 'Science'], 'instructor': ['Mr. Smith', 'Dr. Brown'], 'instructor_office': ['Office 1', 'Office 2']}
df_2nf_to_3nf = pd.DataFrame(data_2nf)
print("Initial table (2NF but not 3NF):")
print(df_2nf_to_3nf)

# Splitting into separate tables to achieve 3NF
data_students = {'student_id': [1, 2], 'student_name': ['John Doe', 'Jane Smith']}
df_students_3nf = pd.DataFrame(data_students)

data_courses_3nf = {'course': ['Math', 'Science'], 'instructor': ['Mr. Smith', 'Dr. Brown']}
df_courses_3nf = pd.DataFrame(data_courses_3nf)

data_instructors = {'instructor': ['Mr. Smith', 'Dr. Brown'], 'instructor_office': ['Office 1', 'Office 2']}
df_instructors = pd.DataFrame(data_instructors)

print("\nSplitting into separate tables to achieve 3NF:")
print("Students table:")
print(df_students_3nf)
print("\nCourses table:")
print(df_courses_3nf)
print("\nInstructors table:")
print(df_instructors)
