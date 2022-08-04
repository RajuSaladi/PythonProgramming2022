try:
    a = int(input("Enter a value "))
except Exception as e:
    print("Error!!", e)
    print("Invalid value for a")
    a = 0
print('the value of a is ', a)
print("Type of a is ", type(a))
