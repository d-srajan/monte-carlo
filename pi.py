import random


circle = 0
total = 0

for i in range(10000):
    x = random.random()
    y = random.random()

    # print(str(x) + ', ' + str(y))
    total = total + 1
    if (x*x + y*y) <= 1: 
        circle = circle + 1

print("pie ~ " + str(4*(circle/total)))