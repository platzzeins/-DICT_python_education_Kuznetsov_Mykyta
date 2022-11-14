import random

number_friends = input("Enter the number of friends joining (including you):\n")
friends_names = {}

if int(number_friends) == 0:
    print("No one is joining for the party")
elif number_friends.isnumeric():
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(int(number_friends)):
        friends_names.update({input():0})

    total_amount = input("Enter the total amount:\n")
    choose_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if choose_lucky == "Yes":
        choosed_lucky_one = random.choice(list(friends_names.items()))
        print(f"{choosed_lucky_one[0]} is the lucky one!")
        for key, value in list(friends_names.items()):
            if key == choosed_lucky_one[0]:
                friends_names[key] = 0
            else:
                friends_names[key] = int(total_amount) / (int(number_friends) - 1)
        print(friends_names)
    elif choose_lucky == "No":
        for key, value in list(friends_names.items()):
            friends_names[key] = int(total_amount) / (int(number_friends))
        print(friends_names)
        print("No one is going to be lucky")
    else:
        print("Something went wrong")
else:
    print("Please try again and input number(NOT STRING)")
