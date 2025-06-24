x = input()
check = False
for i in x:
    if i == "z":
        print("z",end="")
        check = True

if not check:
    print("none", end="")
