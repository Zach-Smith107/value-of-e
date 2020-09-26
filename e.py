
x = int(input("Enter the amount of splits: "))
n = 1
for i in range(x):
    n = n + ((1/x) * n)
    print(n)

print(n)
