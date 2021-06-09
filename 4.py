def reverse():
    s=input("Enter the string:")
    yield s[::-1]
reverse()

for i in reverse():
    print(i)

