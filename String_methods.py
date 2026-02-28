"""
text = "python"

print(text.upper())      # PYTHON
print(text.lower())      # python
print(text.capitalize()) # Python
print(text.title())      # Python
print(text.swapcase())   # PYTHON  

text = "   hello   "

print(text.strip())   # remove both sides
print(text.lstrip())  # left side
print(text.rstrip())  # right side 

text = "python programming"
print(text.find("pro"))   # index or -1
print(text.index("gra"))  # index or error 

text = "banana"
print(text.count("a"))  # 3 

text = "I love Java"
new_text = text.replace("Java", "Python")
print(new_text)  

# Split → String to List
text = "AI engineer interview"
words = text.split()
print(words)  

words = ["AI", "Engineer"]
result = " ".join(words)
print(result) 

text = "12345"
print(text.isdigit())  # True 


email = "admin@gmail.com"
print(email.endswith(".com"))  # True 

# f-strings
name = "Maaz"
age = 25

print(f"My name is {name} and I am {age} years old.")

# String Slicing
text = "Python"
print(text[0:3])  # Pyt
print(text[::-1]) # reverse """
