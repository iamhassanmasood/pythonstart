donut_condition = 'fresh'
buy_score = 1
donut_price = "low"

if donut_condition == "fresh":
    buy_score = 10
elif donut_price == "low":
    buy_score = 5
else:
    buy_score = 0
print(buy_score) # it will print 10