# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable.

width = 1
height = 2
area = width*height
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.

print('Rectangle of width ' + str(width) + ' and height ' + str(height) + ' has an area of ' + str(area))

# 2. Write code that prints the length of the string, 'python'.

print(len("python"))


# 3. Print out the first and third letter of the word 'python'.

p = "python"
print(p[0] + " " + p[2])

# 4. Ask the user to enter their name, and print out `Hello, <name>`.

name = input("What's your name?")

print("Hello " + name)

# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.

age = int(input("What is your age?"))
age_in_15 = age + 15

print("In 15 years time you will be " +str(age_in_15) + " years old")



# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.

print("Hello, " + name + ", you are currently " + str(age) + " years old. In 15 years time you will be " + str(age_in_15))


# 7. Ask the user to enter their hometown, print it out in uppercase letters.

hometown = input("what is your hometown?")
print(hometown.upper())


# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.

colour = input("what is your favourite colour?")
print(len(colour))



# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.

weather = input("What is the weather like today?")
month = input("What month is it?")

print("It is " + month + " and it is " + weather + " today.")


# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.

temp1 = int(input("What was the temperature on Monday?"))
temp2 = int(input("What was the temperature on Tuesday?"))
temp3 = int(input("What was the temperature on Wednesday?"))
temp4 = int(input("What was the temperature on Thursday?"))
temp5 = int(input("What was the temperature on Friday ?"))
month = input("What month is it?")
average = ((temp1)+(temp2)+(temp3)+(temp4)+(temp5))/5

print("It is " + month + " and the average temperature is " + str(average) + " degrees celsius.")


# 11. Print out the above sentence but make the month upper case.

print("It is " + month.upper + " and the average temperature is " + str(average) + " degrees celsius.")

# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.

fave_animals = "My favourite animals:\n\tCats,\n\tDogs,\n\tLlamas,\n\t"

print(fave_animals)

# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.
name = input("What is your name?")
number = int(input("Pick a number:"))
print(name[number].upper())


# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
str = "WelcometoPython"
print(len(str))
print(str[1:14:2])
