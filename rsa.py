import math
import random

def modMultiInverse(exp, totient):
	"""Computes the modular multiplicative inverse"""
	exp = exp % totient
	for x in range(1, totient):
		if (exp * x) % totient == 1:
			return x
	return False

def isPrime(prime):
	"""Checks if a number is prime"""
	if prime <= 1:
		return False
	elif prime <= 3:
		return True
	elif prime % 2 == 0 or prime % 3 == 0:
		return False
	base = 5
	while base * base <= prime:
		if prime % base == 0 or prime % (base + 2) == 0:
			return False
		base += 6
	return True

def generatePrimes(min, max):
	"""Generates primes of a certain length using the sieve of Eratosthenes"""
	if min < 1:
		return False
	primes = {}
	for x in range(min, max, 2):
		primes[x] = True
	for y in range(min, int(math.sqrt(max))):
		if primes[y] == True:
			for z in range(y*y, max, y):
				primes[z] = False
	finalPrimes = []
	for a in range(1, len(primes)):
		if primes[a] == True:
			finalPrimes.append(primes[a])
		else:
			pass
	return finalPrimes

def keyGen():
	"""Generates prime numbers and uses them to create a public private key pair"""
	p1 = random.choice(generatePrimes(1, random.randrange(1000, 1000000)))
	p2 = random.choice(generatePrimes(1, random.randrange(1000, 1000000)))
	mod = p1 * p2
	totient = (p1 -1) * (p2 - 1)
	exp = random.choice(generatePrimes(1, totient))
	private = modMultiInverse(exp, totient)
	return mod, exp, private

def checkInt(input):
	"""Checks if input is an integer"""
	if isinstance(input, int):
		return True
	else:
		raise TypeError

def encrypt(plaintext, publicExp, publicMod):
	"""Encrypts a message using a public key"""
	try:
		checkInt(plaintext)
		checkInt(publicExp)
		checkInt(publicMod)
	except(TypeError):
		print("An input into rsa.encrypt() was not an integer")
		return False
	return pow(plaintext, publicExp, publicMod)

def decrypt(ciphertext, private, publicMod):
	"""Decrypts a message using a private key"""
	try:
		checkInt(ciphertext)
		checkInt(private)
		checkInt(publicMod)
	except(TypeError):
		print("An input into rsa.encrypt() was not an integer")
		return False
	return pow(ciphertext, private, publicMod)

def main():
	"""Debugging rsa functions"""
	pass

if __name__ == "__main__":
	main()