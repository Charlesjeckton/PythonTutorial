# A program that checks whether a year is a leap year or not
year = int(input("Enter a year: "))
if year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# A program that checks whether an alphabet letter is a consonant or a vowel
letter = input("Enter an alphabet letter: ")

if letter.lower() in ('a', 'e', 'i', 'o', 'u'):

    print(letter, "is a vowel")

elif letter.upper() in ('A', 'E', 'I', 'O', 'U'):

    print(letter, "is a vowel")

else:

    print(letter, "is a consonant")
