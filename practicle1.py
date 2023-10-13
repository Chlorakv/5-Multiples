ask_ques = int(input("Enter The Number: "))

print()

for i in range(1, 6):
    j = ask_ques*i
    print("{0} * {1} = {2}".format(ask_ques, i, j))
