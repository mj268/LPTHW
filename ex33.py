#LPTHW - Ex33 - While loops

i = 0
numbers = []
"""
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers")

for num in numbers:
    print(num)
"""
def loopy(j):
    k = 0
    while k < j:
        print(f"At the top i is {k}")
        numbers.append(k)

        k = k + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom k is {k}")

loopy(7)
    