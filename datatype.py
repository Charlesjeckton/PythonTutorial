# Data type
number = 100  # Int
second = 56.78  # Float
text = "Hello there"  # String
isPythonInteresting = True  # Bool

# Storing multiple values in a variable
cars = ["Toyota", "Nissan", "BMW", "VW"]  # List
fruits = ("Banana", "Oranges", "Apple")  # Tuple
countries = {"Kenya", "Tanzania", "Tunisia", "Algeria"}  # Set
details = {
    "firstname": "Charles",
    "age": 23,
    "course": "Web development",
    "nationality": "Kenyan"
}  # Dictionary

print(second)
print(text)
print(cars)
print(countries)
print(details["firstname"])
print(details["age"])
print(details["course"])
print(details["nationality"])

# Determine a data type
print(type(text))
print(type(second))
print(type(countries))
print(type(details))

# Typecasting - Converting one data type to another
print(float(number))
print(int(second))


