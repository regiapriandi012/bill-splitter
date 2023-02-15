# write your code here
print("Enter the number of friends joining (including you):")
jumlah_teman = int(input())
if jumlah_teman <= 0:
    print()
    print("No one is joining for the party")
    print()
else:
    print("Enter the name of every friend (including you), each on a new line:")
    teman = [input() for i in range(jumlah_teman)]
    print()
    print(dict(zip(teman, [0 for i in range(jumlah_teman)])))