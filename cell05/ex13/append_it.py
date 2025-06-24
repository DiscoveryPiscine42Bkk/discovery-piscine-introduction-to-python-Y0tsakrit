x = input().split()

if len(x) == 0:
    print("none")
else:
    for i in x:
        if i[-3] == "i" and i[-2] == "s" and i[-1] == "m":
            pass
        else:
            print(f"{i}ism")