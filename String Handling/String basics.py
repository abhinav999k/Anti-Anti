#'hello' is the same as "hello"
'''multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)'''

a = "Hello"
print(a[0],a[1])

for i in a:
    print(i)

#print without a newline
print("hello",end = " ")
print("world")
print(len(a))

#to check if string is present in text use (in/not in)
text = "The world famous valleys are in Kashmir and Kulu"
if "worlds" in text:
    print("Yes,Present")
else:
    print("Nah")
    
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

#String slice
b = "Hello,tWo,rld"
print(b[:5])
print(b.lower())
print(b.upper())
print(b.strip()) #similar to trim in powershell
print(b.replace('ll','k'))
print(b.split(","))
print(b)

x = "I "
y = 100
print(x+str(y))
ext = "The world famous {} are kashmir and kulu and {} located in Himalayas"
print(ext.format(10,20))
ext = "The world famous \rare kashmir and kulu and  located in Himalayas"
print(ext)

#string methods:
# https://www.w3schools.com/python/python_strings_methods.asp

stri = "Abhinav"[::-1]
print(stri)

