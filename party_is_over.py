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

    teman_teman = dict(zip(teman, [0 for i in range(jumlah_teman)]))

    print()
    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    lucky = input()
    if lucky == "Yes":
        tidak_lucky = random.choice(list(teman_teman.keys()))

        print()
        print("{} is the lucky one!".format(tidak_lucky))

        teman_teman = dict(zip(teman, [round(bill / (jumlah_teman-1), 2) for i in range(jumlah_teman)]))

        teman_teman[tidak_lucky] = 0

        print()
        print(teman_teman)
    else:
        print()
        print("No one is going to be lucky")
        teman_teman = dict(zip(teman, [round(bill / jumlah_teman, 2) for i in range(jumlah_teman)]))

        print()
        print(teman_teman)