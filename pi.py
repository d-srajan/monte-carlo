# estimate value of pi using monte carlo method

import random

print("=== Pi Estimation Simulation ===")
print("Goal: Estimate π (pi) using random points (expected: 3.14159...)")
print("Method: Generate random points in a unit square and check if they fall inside a quarter circle")
print("        π ≈ 4 × (points inside circle / total points)\n")

iterations = 1

while True:
   if iterations > 10000000:
       break

   iterations = iterations * 10
   circle = 0
   total = 0

   print(f"Generating {iterations:,} random points...")
   for i in range(iterations):
       x = random.random()
       y = random.random()

       total = total + 1
       if (x*x + y*y) <= 1:
           circle = circle + 1

   print("for " + str(iterations) + " iterations, pi ~ " + str(4*(circle/total)))
   print()

print("As iterations increase, the estimate converges to π ≈ 3.14159...")
