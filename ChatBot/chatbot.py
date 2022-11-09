
print("Hello! My name is Heizenberg.")
print("I was created in 2022.")
print("Please remind me your name.")
name = input()
print("What a great name you have, " + name + "!")
print("Let me gues your age.")
print("Enter remainders of dividing your age by 3, 5 and 7 .")
remainder3 = input()
remainder5 = input()
remainder7 = input()
age = (int(remainder3) * 70 + int(remainder5) * 21 + int(remainder7) * 15) % 105
print("Your age is " + str(age) + ";That's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
usersnumber = input()
i = 0
while i <= int(usersnumber):
   print(str(i) + " !")
   i += 1

print("Completed, have a nice day!")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")
def answer():
    answear = input()
    if int(answear) == 2:
        print("Completed, have a nice day!")
        print("Congratulations, have a nice day!")
    else:
        print("Please, try again.")
        answer()
answer()
