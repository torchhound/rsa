import math
import random

def modMultiInverse(exp, totient):
	"""Computes the modular multiplicative inverse"""
	if isPrime(totient) == True:
		return exp**(totient - 2) % totient
	pass

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
	for a in range(1, len(primes) + 1):
		if primes[a] == True:
			finalPrimes.append(primes[a])
		else:
			pass
	if len(finalPrimes) == 0:
		return False
	else:
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

def encrypt(plaintext, publicExp, publicMod):
	"""Encrypts a message using a public key"""
	final = [(ord(x) ** publicExp) % publicMod for x in plaintext] #because pow() does not support bytes
	return final

def decrypt(ciphertext, private, publicMod):
	"""Decrypts a message using a private key"""
	final = [chr((x ** private) % publicMod) for x in ciphertext]
	return final

def main():
	"""Debugging rsa functions"""
	pass

if __name__ == "__main__":
	main()