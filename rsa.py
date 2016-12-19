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
	"""Generates primes of a certain length"""
	pass

def keyGen():
	"""Generates prime numbers and uses them to create a public private key pair"""
	pass

def encrypt(plaintext, public, mod):
	"""Encrypts a message using a public key"""
	final = [(ord(x) ** public) % mod for x in plaintext] #because pow() does not support bytes
	return final

def decrypt(ciphertext, private, mod):
	"""Decrypts a message using a private key"""
	final = [chr((x ** private) % mod) for x in ciphertext]
	return final

def main():
	"""Debugging rsa functions"""
	pass

if __name__ == "__main__":
	main()