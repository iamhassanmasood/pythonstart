print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
text = "Hello"
print(bool(text)) #True
text = ""
print(bool(text)) #False
text = None
print(bool(text)) #False
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False
total_cost = bool(1 + 3 * 4)
print(total_cost)

result_of_computation = bool(((2 * 4) * 4) + 2)
print(result_of_computation)