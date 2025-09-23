for i in range(1, 21, 2):
    print(i, end=' ')
print()

# A
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# B
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# C
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end='')
print()

# D
number_of_lines = int(input("Number of lines: "))
for n in range(number_of_lines):
    for i in range(n + 1):
        print("*", end='')
    print()
print()
