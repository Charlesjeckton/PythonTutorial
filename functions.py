# User defined functions
def greeting():
    print("Hello world")


greeting()  # Calling a function


def details():
    print("Charles")


details()


# Parameters and arguments
def student(firstname, course, age):
    print(firstname, course, age)


student("Charles", "MIT", 24)
student("John", "Data Science", 25)
student("Kevin", "BIT", 26)

# Built-in library function
y = max(78, 90, 12, 6, 56)
print(y)

x = min(78, 90, 12, 6, 56)
print(x)

x = pow(2, 3)
print(x)

