import unittest
import rsa

class RSATests(unittest.TestCase):
	"""Tests for rsa.py"""

	def testIsPrime(self):
		"""Check isPrime function with primes"""
		self.assertTrue(rsa.isPrime(2) and rsa.isPrime(3) and rsa.isPrime(5) and rsa.isPrime(11) and rsa.isPrime(15485863))

	def testIsNotPrime(self):
		"""Check isPrime function with non prime numbers"""
		self.assertFalse(rsa.isPrime(8) and rsa.isPrime(200))

	def testGeneratePrimes(self):
		"""Check if generatePrimes creates primes numbers"""
		primes = rsa.generatePrimes(1, 1000)
		flag = True
		for x in primes:
			if rsa.isPrime(x) == False:
				flag = False
			else:
				pass
		self.assertTrue(flag) 
'''
	def testEncrypt(self):
		"""Checks output of encrypt function"""
		self.assertTrue(rsa.encrypt("65", 17, 3233) == 2790)

	def testDecrypt(self):
		"""Checks output of decrypt function"""
		self.assertTrue(rsa.decrypt(2790, 2753, 3233) == 65)
'''
if __name__ == "__main__":
	unittest.main()