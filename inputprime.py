#Asks you the range you want to search for primes in, then does it.
a = int(raw_input("Please enter a starting integer: "))
b = int(raw_input("Please enter an ending integer: "))
for n in range(a, b):
	for x in range(2, n):
		if n % x == 0:
			# could print n, 'equals', x, '*', n/x
			break
	else:
		#loop fell through without finding a factor
		print n, 'is a prime number'
			