odd_nums = 0
even_nums = 0
print("")
for x in range(3):
    num = int(input("Please enter a whole number: "))

    if num %2 == 0:
        even_nums += 1
    else:
        odd_nums += 1

print(f"\nThere were {even_nums} even numbers, and {odd_nums} odd numbers")