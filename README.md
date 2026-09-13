# projecteuler.net

A collection of solutions to mathematical and computational problems from [Project Euler](https://projecteuler.net/), exploring algorithms, optimization, and problem-solving techniques.

## Problem 1: Multiples of 3 or 5

Find the sum of all natural numbers below 1000 that are multiples of 3 or 5.

The solution sums the multiples of 3 and 5 using the arithmetic-series formula, then subtracts the multiples of 15 because they were counted twice:

```text
sum(3) + sum(5) - sum(15)
```

This produces the result **233168**.
