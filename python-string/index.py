a = "Hello"
print(a) 
print(type(a))   #it will be 'str'

for i in a:
    print(i)
x = "Hi Developer"
print(x)
print(x[1]) #it will be 'i'
print(len(x)) #it will print length of string x

txt = "Nothing in life comes for free!"
if "free" in txt:
  print("Yes, 'free' is present.")

newText = "A quick brown fox jumps over the lazy dog"
print("free" in newText) #False
print("expensive" not in txt) #True

multilineText = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multilineText) #Multiline text

b = "Hello, World!"
print(b[2:5]) #it will print from position 2 to position 5 (not included)

b = "Hello, World!"
print(b[:5]) #it witll print from the start to position 5 (not included)

b = "Hello, World!"
print(b[2:]) #it will print from position 2, and all the way to the end

b = "Hello, Engineers"
print(b[-5:-2]) #it will print in negative order from position 2 to position 5 (not included)

b = "Hello, Engineers"
print(b[:-2]) #it will print in negative order from position 2 to position end

b = "Hello, Engineers"
print(b[-2:]) #it will print last 2 index's

greeting = "Hello"
team = "World"
print(greeting + team)