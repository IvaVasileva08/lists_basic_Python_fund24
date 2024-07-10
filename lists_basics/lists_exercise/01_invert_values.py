"""my_list = input().split()
oposite_number = []
for number in my_list:
    oposite_numberss = -int(number)
    oposite_number.append(oposite_numberss)
print(oposite_number)"""

print([-int(number) for number in input().split()])