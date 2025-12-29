a = int(input("Enter a: "))
count = a if a % 2 == 1 else a - 1

result = []
for i in range(count):
    result.append(2 * i + 1)

print(", ".join(map(str, result)))
