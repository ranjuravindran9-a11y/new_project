text="Hello,Python!"
print(text[0])
print(text[-1])

s=" hello python "
print(s.upper())
print(s.lower())
print(s.strip())
print(s.replace("hello","Hi"))

name="Alice"
age=25

print("My name is "+name+"and I am "+ str(age)+" years old.")
print(f"My name is {name} and I am {age} years old.")

sentence="Python is fun"
words=sentence.split()
print(" ".join(words))