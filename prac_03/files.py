# 1. Write code that asks the user for their name, then opens a file called name.txt and writes that name to it.
name = input("Name: ")
infile = open("name.txt", 'w')
infile.write(name)
infile.close()

# 2. In the same file, write code that opens name.txt and reads the same then prints

# 3. Create a text file called numbers.txt and save it in your directory. Put the following three numbers on separate lines in the file and save it:
# 17, 42, 400
# Write code that opens numbers.txt, reads only the first two numbers, adds them together, and prints the result

# 4. Write a fourth block of code that prints the total for all lines in numbers.txt
