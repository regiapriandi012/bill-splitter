# write your code here
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

    print()
    print(dict(zip(teman, [round(bill / jumlah_teman, 2) for i in range(jumlah_teman)])))
