tail = input()
body = input()
head = input()
row = [tail, body, head]
row[0], row[2] = row[2], row[0]
print(row)