"""
Count Primes

Given an integer n, return the number of prime numbers that are strictly
less than n.

A prime number is a natural number greater than 1 that has no positive
divisors other than 1 and itself.

Example 1:

Input: n = 10
Output: 4
Explanation: There are four prime numbers less than 10: 2, 3, 5, and 7.

Example 2:

Input: n = 0
Output: 0

Example 3:

Input: n = 1
Output: 0

Constraints:

- 0 <= n <= 5 * 10^6

Think about how to avoid checking every number independently. Your solution
should be efficient enough to handle the largest allowed value of n.
"""


class Solution:
    def countPrimes(self, n):
        """Return the number of prime numbers strictly less than n."""
        
