status = 'selecet'
weight = 450
time = 5

if weight > 300 and time < 6:
    status = "try again"
print(status) 
    
if weight > 300 or time < 6:
    status = "Eligible"
print(status) 