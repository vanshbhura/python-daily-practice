# Day 10: Strings
# Topics:
# string basics, indexing, string methods

text = "Python Programming"

print("Original text:", text)

# Length of string
print("Length:", len(text))

# Indexing
print("First character:", text[0])
print("Last character:", text[-1])

# String methods
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Checking content
print("Contains 'Python':", "Python" in text)

# Replacing text
new_text = text.replace("Python", "Java")
print("After replace:", new_text)

# Splitting string
words = text.split()
print("Split words:", words)
