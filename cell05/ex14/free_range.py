x = input().split()
a = []
if len(x) == 0:
    print("none")
else:
    for i in range(int(x[0]), int(x[1]) + 1):
        a.append(i)
    print(a)