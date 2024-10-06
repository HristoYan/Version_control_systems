meters = int(input("Meters: "))
action = input("Miles, inches or yards: ")
action = action.lower()
result = 0
if action == "miles":
    result = meters * 0.000621
elif action == "inches":
    result = meters * 39.37
elif action == "yards":
    result = meters * 1.094

print(result)