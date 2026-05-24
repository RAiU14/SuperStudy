with open("custom.txt") as f:
    data = f.readlines()

for line in data:
    print (line)

a = input("your name: ")
with open("custom.txt", "a") as f:
    f.write(f"{a}\n")