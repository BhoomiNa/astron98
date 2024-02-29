
scores = 
scores = [int(percent*max_score) for percent in percentages]
#list comprehension- simpler way of adding to the list shortcut
scores = []
for percent in percentages:
    scores.append(int(percent*max_score))


cart_items = ['apple' , 'banana' , 'orange' , ',milk']
item_price = [1.2]
