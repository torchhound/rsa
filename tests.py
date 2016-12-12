import unittest
import rsa

def isPrime(prime):
	"""Checks if a number is prime"""

class RSATests(unittest.TestCase):
	"""Tests for rsa.py"""

	def primeTest(self):
		"""Determine if numbers produced by generatePrimes function are prime"""
		return self.assertTrue(isPrime(rsa.generatePrimes(5)))

if __name__ == "__main__":
	unittest.main()