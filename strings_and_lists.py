words = "It's thanksgiving day. It's my birthday,too!"
#print words.replace('day', 'month', 18)


x = [2,54,-2,7,12,98]
#print max(x)
#print min(x)

list_item = ["hello",2,54,-2,7,12,98,"world"]
m = []
m.append(list_item[0])
n = len(list_item)
m.append(list_item[n-1])

#print m

y = [19,2,54,-2,7,12,98,32,10,-3,6]
y.sort()

new_list = []
new_list.append(y[:len(y)/2])

for value in range((len(y)/2), len(y)):
    new_list.append(y[value])

print new_list
