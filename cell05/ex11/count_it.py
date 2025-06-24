x = input().split()

if len(x) == 0:
    print("none")
else:
    print(f"parameters: {len(x)}")
    for i in x:
        print(f"{i} : {len(i)}")