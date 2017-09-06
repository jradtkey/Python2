
#multiples:
for value in range(1,1000):
    if value % 2 == 0:
        continue
    else:
        print value

for value in range(5, 1000000):
    if value % 5 == 0:
        print value


#sum list:
a = [1, 2, 5, 10, 255, 3]
print sum(a)

#average list
a = [1, 2, 5, 10, 255, 3]
avg = sum(a)/len(a)
print avg
