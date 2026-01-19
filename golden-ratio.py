# estimate the Golden Ratio (φ) using monte carlo method
#
# Why does this work?
# The golden ratio φ is the limit of the ratio of consecutive Fibonacci numbers.
# Starting with ANY two positive numbers and repeatedly adding them (like Fibonacci),
# the ratio of consecutive terms always converges to φ ≈ 1.61803...
# We use random starting values and average the results.
#
# Interestingly, this one converges faster than π or e because the Fibonacci
# ratio itself converges exponentially fast (after ~30 steps, it's already
# accurate to many decimal places).

import random

print("=== Golden Ratio (φ) Estimation Simulation ===")
print("Goal: Estimate φ (phi), the golden ratio (expected: 1.61803...)")
print("Method: Start with random numbers, generate Fibonacci-like sequences")
print("        The ratio of consecutive terms converges to φ\n")

iterations = 10
fibonacci_steps = 30  # enough steps for convergence

while True:
    if iterations > 10000000:
        break

    print(f"Running {iterations:,} trials...")
    total_ratio = 0

    for i in range(iterations):
        # start with two random positive numbers
        a = random.random() + 0.1  # avoid zero
        b = random.random() + 0.1

        # generate Fibonacci-like sequence
        for _ in range(fibonacci_steps):
            a, b = b, a + b

        # ratio of consecutive terms approximates φ
        total_ratio += b / a

    estimate = total_ratio / iterations
    print(f"for {iterations} trials, φ ~ {estimate}")
    print()
    iterations = iterations * 10

print("As iterations increase, the estimate converges to φ ≈ 1.61803...")
