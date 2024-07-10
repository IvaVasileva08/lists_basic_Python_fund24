n = int(input())
word = input()

lst = []
new_lst = []

for i in range(n):
    current_string = input()
    lst.append(current_string)
    if word in current_string:
        new_lst.append(current_string)

print(lst)
print(new_lst)