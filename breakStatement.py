# Break statements are used to break a loop
# Task. Write a program that ask the user to enter their names,
# if the name is joy, they will get a welcome message.\
# Include a break statement in the loop.

name = "joy"
print("Enter your name")
nameEntered = input(">")

while True:
  if nameEntered == name:
   print("Hello, joy how are you doing today?")
   break

