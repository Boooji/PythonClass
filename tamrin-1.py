list_1 = []
for i in range (5):
    number = int(input(f"Enter your number {i + 1} ="))
    list_1.append(number)
top_number = list_1 [0]
low_number = list_1[0]
for num in list_1:
    if num > top_number:
        top_number = num
    if num < low_number:
        low_number = num
print(f"number list: {list_1}")
print(f"biggest number: {top_number}")
print(f"lowest number: {low_number}")