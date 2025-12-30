# Day 15: File Handling
# Topics:
# write to file, read from file

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is my first file handling program.\n")
    file.write("Learning Python Day 15.\n")

print("Data written to file.")

# Reading from the file
with open("sample.txt", "r") as file:
    content = file.read()

print("File content:")
print(content)
