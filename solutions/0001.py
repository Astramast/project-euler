# https://projecteuler.net/problem=1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

# Solution 1
# We can use a for-loop to directly get the answer

accumulator = 0
for i in range(1000):
	if i % 3 == 0:
		accumulator += i
		continue # Don't count twice multiples of both 3 & 5
	if i % 5 == 0:
		accumulator += i
print(accumulator)


# Solution 2
# We now consider X a vector of sorted numbers and t a target, 
# and we search s the sum of all numbers strictly below t 
# for which there exists at least a number x\in X that divide it with a rest of zero.

