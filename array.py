courses = ["MIT", "Cyber Security", "Data Science"]

print(courses)

# Accessing an element in an array
print(courses[1])

# Looping through an array
for course in courses:
    print(course)

# Adding an element in an array
courses.append("Android Development")
print(courses)

# Removing an element in an array
courses.remove("MIT")
print(courses)

# Inserting an element in an array
courses.insert(1, "BIT")
print(courses)
