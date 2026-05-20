path = input("Enter path of the text or log file : ").strip("'\"")

with open(path) as f:
    print(f.read())