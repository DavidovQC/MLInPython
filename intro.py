item = "apple"
Item = "Apple"
print(item + " " + Item)

naughty_list = ["Aayush", "Akshay"]
print(naughty_list)

integer = 3
name = "Akshay"
str_integer = "12"

print(name + str(integer))


# a = 3
# b = 5

# addition = a + b
# minus = a - b
# times = a * b
# divide = a/b
# power = a**b

# a = 3  # 11
# b = 5  # 101
# addition = a + b
# minus = a - b
# times = a * b
# divide = a/b
# power = a**b

# print(addition)
# print(minus)
# print(times)
# print(power)


# age = 7
# name = 'Mark'


# age = 12
# name = "Aayush"

# if age > 18:
#     print("You are old!")
# elif age == 18:
#     print("You are getting old!")
# else:
#     print("You are young yet")

# for i in range(3):
#     print("Hello", i)

# print(range(3))

# for name in naughty_list:
#     print("Coal for:", name)

# i = 0

# while i < 5:
#     print(i)
#     i = i+1

# while True:
#     user_input = input("Enter something >> ")
#     if (user_input == "secret_password"):
#         print("Hello!")
#         break

# while True:
#     user_input = input("Enter something >> ")
#     if (user_input == "secret_password"):
#         print("Hello!")
#         break


# functions
# def say_hello(name):
#     print("Hello", name)


# for name in naughty_list:
#     say_hello(name)

# Classes


# class Dog:
#     species = "Canine"

#     # The constructor method initializes new objects
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # A method defines behavior
#     def bark(self):
#         return f"{self.name} says woof!"


# my_dog = Dog("Buddy", 3)

# # Access attributes and call methods using dot notation
# print(my_dog.name)    # Output: Buddy
# print(my_dog.bark())  # Output: Buddy says woof!

class Dog:
    species = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"


my_dog = Dog("Buddy", 3)
print(my_dog.bark())


# For homework:
# Implement the dot product of two vectors, making sure that it is properly defined for the two input vectors
# Begin creating a perceptron
# Implement of a derivative with the paramter h
# Implement the gradient with paramter h
