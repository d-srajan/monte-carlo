# Monte Carlo Simulations

Using the Monte Carlo method to approximate mathematical constants and probabilities.

## What is the Monte Carlo Method?

The Monte Carlo method is a computational technique that uses random sampling to estimate numerical results. Instead of solving problems analytically, we run many random experiments and use the outcomes to approximate the answer. As the number of trials increases, the estimate converges to the true value.

## Experiments

### 1. Fair Coin Toss (`fair-coin-toss.py`)
**Estimates:** P(heads) = 0.5

Simulates flipping a fair coin many times. By the Law of Large Numbers, the proportion of heads converges to the true probability of 0.5.

### 2. Pi Estimation (`pi.py`)
**Estimates:** π ≈ 3.14159...

Generates random points in a unit square and checks if they fall inside a quarter circle. Since the quarter circle has area π/4 and the square has area 1, the ratio of points inside the circle to total points equals π/4. Multiply by 4 to get π.

### 3. Euler's Number (`eulers-number.py`)
**Estimates:** e ≈ 2.71828...

Counts how many uniform random numbers (between 0 and 1) are needed to sum past 1. The expected count equals e — a result related to the Poisson and exponential distributions.

### 4. Golden Ratio (`golden-ratio.py`)
**Estimates:** φ ≈ 1.61803...

Uses Fibonacci-like sequences with random starting values. The ratio of consecutive terms in any Fibonacci-like sequence converges to the golden ratio φ. Interestingly, this simulation converges faster than π or e because the Fibonacci ratio itself converges exponentially fast (after ~30 steps, it's already accurate to many decimal places).

### 5. Natural Log of 2 (`ln2.py`)
**Estimates:** ln(2) ≈ 0.69315...

Generates random points in a unit square and checks if they fall below the curve y = 1/(1+x). The area under this curve from 0 to 1 equals ln(2), so the fraction of points below the curve converges to the true value. This uses Monte Carlo integration — the same geometric approach as the π estimation.

## Running the Simulations

```bash
python3 fair-coin-toss.py
python3 pi.py
python3 eulers-number.py
python3 golden-ratio.py
python3 ln2.py
```

Each simulation runs with increasing iterations (10 → 10,000,000) to show how the estimates converge to the true values.
