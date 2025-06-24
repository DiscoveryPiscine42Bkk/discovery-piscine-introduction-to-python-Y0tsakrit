def shrink(s):
    print(s[:8])

def enlarge(s):
    print(s + 'Z' * (8 - len(s)))


x = input().split()

if len(x) <= 1:
    print("none")
else:
    for arg in x:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)