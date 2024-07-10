n = int(input())
even = []
odd = []
negative = []
positive = []
for i in range(n):
    current = int(input())
    if current % 2 == 0:
        even.append(current)
    if current % 2 != 0:
        odd.append(current)
    if current >= 0:
        positive.append(current)
    if current < 0:
        negative.append(current)

command = input()

if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "positive":
    print(positive)
elif command == "negative":
    print(negative)