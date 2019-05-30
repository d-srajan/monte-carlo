# estimate value of pi using monte carlo method

import random

iterations = 1

while True:
   if iterations > 10000000:
       break

   iterations = iterations * 10
   circle = 0
   total = 0

   for i in range(iterations):
       x = random.random()
       y = random.random()

       total = total + 1
       if (x*x + y*y) <= 1:
           circle = circle + 1

   print("for " + str(iterations) + " iterations, pie ~ " + str(4*(circle/total)))
