import unittest
import rsa

class RSATests(unittest.TestCase):
	"""Tests for rsa.py"""

	def testIsPrime(self):
		"""Checks rsa.isPrime() function with primes"""
		self.assertTrue(rsa.isPrime(2) and rsa.isPrime(3) and rsa.isPrime(5) and rsa.isPrime(11) and rsa.isPrime(15485863))

	def testIsNotPrime(self):
		"""Checks rsa.isPrime() function with non prime numbers"""
		self.assertFalse(rsa.isPrime(8) and rsa.isPrime(200))

	def testGeneratePrimes(self):
		"""Checks if rsa.generatePrimes() creates primes numbers"""
		primes = rsa.generatePrimes(1, 1000)
		flag = True
		for x in primes:
			if rsa.isPrime(x) == False:
				flag = False
			else:
				pass
		self.assertTrue(flag) 

	def testGenerateZeroPrimes(self):
		"""Tests behavior of rsa.generatePrimes() when no primes are found"""
		self.assertFalse(rsa.generatePrimes(20, 21))

	def testModMultiInverseTrue(self):
		"""Tests rsa.modMultiInverse() with known true input and output"""
		self.assertTrue(rsa.modMultiInverse(17, 3120) == 2753)

	def testModMultiInverseFalse(self):
		"""Tests rsa.modMultiInverse() with known false input and output"""
		self.assertFalse(rsa.modMultiInverse(15, 5))

	def testEncrypt(self):
		"""Checks output of rsa.encrypt()"""
		self.assertTrue(rsa.encrypt(65, 17, 3233) == 2790)

	def testDecrypt(self):
		"""Checks output of rsa.decrypt()"""
		self.assertTrue(rsa.decrypt(2790, 2753, 3233) == 65)

	def testEncryptStrInput(self):
		"""Check rsa.encrypt() with string input"""
		self.assertFalse(rsa.encrypt("65", 17, 3233))

	def testDecryptStrInput(self):
		"""Check rsa.decrypt() with string input"""
		self.assertFalse(rsa.encrypt(2790, "2753", 3233))

if __name__ == "__main__":
	unittest.main()