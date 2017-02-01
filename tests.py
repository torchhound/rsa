import unittest
import rsa

class RSATests(unittest.TestCase):
	"""Tests for rsa.py"""

	def testIsPrime(self):
		"""Checks isPrime function with primes"""
		self.assertTrue(rsa.isPrime(2) and rsa.isPrime(3) and rsa.isPrime(5) and rsa.isPrime(11) and rsa.isPrime(15485863))

	def testIsNotPrime(self):
		"""Checks isPrime function with non prime numbers"""
		self.assertFalse(rsa.isPrime(8) and rsa.isPrime(200))

	def testGeneratePrimes(self):
		"""Checks if generatePrimes creates primes numbers"""
		primes = rsa.generatePrimes(1, 1000)
		flag = True
		for x in primes:
			if rsa.isPrime(x) == False:
				flag = False
			else:
				pass
		self.assertTrue(flag) 

	def testGenerateZeroPrimes(self):
		"""Tests behavior of generatePrimes when no primes are found"""
		self.assertFalse(rsa.generatePrimes(20, 21))

	def testModMultiInverseTrue(self):
		"""Tests modMultiInverse with known true input and output"""
		self.assertTrue(rsa.modMultiInverse(17, 3120) == 2753)

	def testModMultiInverseFalse(self):
		"""Tests modMultiInverse with known false input and output"""
		self.assertFalse(rsa.modMultiInverse(15, 5))
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