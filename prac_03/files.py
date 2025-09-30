# 1. Write code that asks the user for their name, then opens a file called name.txt and writes that name to it.
name = input("Name: ")
outfile = open("name.txt", 'w')
outfile.write(name)
outfile.close()

# 2. In the same file, write code that opens name.txt and reads the same then prints
infile = open("name.txt", 'r')
name = infile.readline()
print(f"Hi {name}!")
infile.close()

# 3. Create a text file called numbers.txt and save it in your directory. Put the following three numbers on separate lines in the file and save it:
# 17, 42, 400
# Write code that opens numbers.txt, reads only the first two numbers, adds them together, and prints the result
outfile = open("numbers.txt", 'w')
outfile.write("17\n42\n400")
outfile.close()

infile = open("numbers.txt", 'r')
first_number = int(infile.readline().strip())
second_number = int(infile.readline().strip())
print(first_number + second_number)
infile.close()

# 4. Write a fourth block of code that prints the total for all lines in numbers.txt
infile = open("numbers.txt", 'r')
total = 0
for number in infile.readlines():
    total += int(number.strip())
print(total)