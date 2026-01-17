# estimate Euler's number (e) using monte carlo method
#
# Why does this work?
# e is the expected number of uniform random variables (between 0 and 1) 
# you need to sum to reach or exceed 1. This is related to the Poisson 
# distribution and exponential distribution.

import random

print("=== Euler's Number (e) Estimation Simulation ===")
print("Goal: Estimate e (expected: 2.71828...)")
print("Method: Count how many random numbers [0,1) are needed to sum past 1")
print("        The average count converges to e\n")

iterations = 10

while True:
    if iterations > 10000000:
        break

    print(f"Running {iterations:,} trials...")
    total_count = 0

    for i in range(iterations):
        total = 0
        count = 0

        while total <= 1:
            total = total + random.random()
            count = count + 1

        total_count = total_count + count

    print("for " + str(iterations) + " trials, e ~ " + str(total_count / iterations))
    print()
    iterations = iterations * 10

print("As iterations increase, the estimate converges to e ≈ 2.71828...")
