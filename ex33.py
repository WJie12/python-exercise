# def whileTest(max, step):
# 	i = 0
# 	numbers = []

# 	while i < max:
# 		print "At the top i is %d" % i
# 		numbers.append(i)

# 		i = i + step
# 		print "Numbers now:", numbers
# 		print "At the bottom i is %d" % i

# 	return numbers

# print "PLS input the max number: "
# max = int(raw_input("> "))

# print "PLS input the increment: "
# step = int(raw_input("> "))

# numbers = whileTest(max, step)
# print "The numbers: " % numbers

# for num in numbers:
# 	print num


numbers = []

for i in range(0, 6):
	print "At the top i is %d" % i
	numbers.append(i)

	# i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is  %d" % i

print "The numbers: "

for num in numbers:
	print num