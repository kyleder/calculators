import math, sys

def find_primes(start, end):
	primes = []
	for i in range(start, end):
		if is_prime(i):
			primes.append(i)
	return primes


def is_prime(number):
	if number < 2:
		return False
	if number == 2:
		return True
	if number % 2 == 0:
		return False
	for i in range(3, int(math.sqrt(number))+1, 2):
		if number % i == 0:
			return False
	return True


if __name__ == "__main__":
	arg_len = len(sys.argv)
	if arg_len < 2:
		print "Please supply a number to check or a range to print"
	elif arg_len == 2:
		print is_prime(int(sys.argv[1]))
	else:
		print find_primes(int(sys.argv[1]), int(sys.argv[2]))
