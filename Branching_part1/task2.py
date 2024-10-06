num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))
action = input("Max, Min or Sum: ")
action = action.lower()
result = 0

if action == "max":
    result = max(num1, num2, num3)
elif action == "min":
    result = min(num1, num2, num3)
else:
    result = num1 + num2 + num3

print(result)
