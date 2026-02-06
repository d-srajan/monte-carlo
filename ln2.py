# estimate the natural logarithm of 2 (ln2) using monte carlo method
#
# Why does this work?
# ln(2) equals the integral of 1/(1+x) from 0 to 1.
# We can estimate this integral by generating random points in the unit square
# and checking if the point falls below the curve y = 1/(1+x).
# The fraction of points below the curve approximates the area under it,
# which equals ln(2) ≈ 0.69315...

import random

print("=== Natural Log of 2 (ln2) Estimation Simulation ===")
print("Goal: Estimate ln(2) (expected: 0.69315...)")
print("Method: Generate random points in a unit square and check if they fall")
print("        below the curve y = 1/(1+x). The area under that curve is ln(2)\n")

iterations = 10

while True:
    if iterations > 10000000:
        break

    print(f"Generating {iterations:,} random points...")
    below = 0
    total = 0

    for i in range(iterations):
        x = random.random()
        y = random.random()

        total = total + 1
        if y <= 1 / (1 + x):
            below = below + 1

    print("for " + str(iterations) + " iterations, ln(2) ~ " + str(below / total))
    print()
    iterations = iterations * 10

print("As iterations increase, the estimate converges to ln(2) ≈ 0.69315...")
