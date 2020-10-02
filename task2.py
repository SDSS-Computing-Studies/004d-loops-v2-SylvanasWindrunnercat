#! python3

a = ""

namelist=("Lebron","Kobe","Michale","Shaq","Dennis")
for a in namelist:
    a = input("The username is:")
    if a in namelist:
        print("That name is on the list")
        break
    else:
        print("That name is out of the list")