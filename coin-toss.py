# estimate the probability of heads over several coin tosses using monte carlo method

import random

iterations = 10

while True:
    if iterations > 10000000:
        break

    heads = 0
    total = 0

    for i in range(iterations):
        x = random.random()

        total = total + 1
        if x >= (1/2):
           heads = heads + 1

    print("for " + str(iterations) + " coin tosses, P[heads] ~ " + str(heads/total))
    iterations = iterations * 10