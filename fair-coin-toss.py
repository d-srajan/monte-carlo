# estimate the probability of heads over several coin tosses using monte carlo method

import random

print("=== Fair Coin Toss Simulation ===")
print("Goal: Estimate P[heads] for a fair coin (expected: 0.5)")
print("Method: Simulate random coin tosses and count heads\n")

iterations = 10

while True:
    if iterations > 10000000:
        break

    print(f"Tossing a coin {iterations:,} times...")
    heads = 0
    total = 0

    for i in range(iterations):
        x = random.random()

        total = total + 1
        if x >= (1/2):
           heads = heads + 1

    print("for " + str(iterations) + " coin tosses, P[heads] ~ " + str(heads/total))
    print()
    iterations = iterations * 10

print("As iterations increase, P[heads] converges to 0.5 — the true probability!")