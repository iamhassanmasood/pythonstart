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