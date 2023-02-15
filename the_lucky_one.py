# write your code here
import random

print("Enter the number of friends joining (including you):")
jumlah_teman = int(input())
teman = []

if jumlah_teman <= 0:
    print()
    print("No one is joining for the party")
    print()
else:
    print()
    print("Enter the name of every friend (including you), each on a new line:")
    teman += [input() for i in range(jumlah_teman)]

    print()
    print("Enter the total bill value:")
    bill = int(input())

    teman_teman = dict(zip(teman, [round(bill / jumlah_teman, 2) for i in range(jumlah_teman)]))

    print()
    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    lucky = input()
    if lucky == "Yes":
        print()
        print("{} is the lucky one!".format(random.choice(list(teman_teman.keys()))))
    else:
        print()
        print("No one is going to be lucky")
