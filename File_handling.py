file=open("example.txt","w")
file.write("Hello, this is a test file.")
file.close()

file=open("example.txt","r")
content=file.read()
print(content)
file.close()

with open("example.txt","a") as f:
    f.write("\n Appending new data.")

with open("example.txt","r") as file:
    for line in file:
        print(line.strip())

try:
    with open("non_existent_file.txt","r") as file:
        content=file.read()

except FileNotFoundError:
    print("File not found.Please check the filename.")