while True:
	try:
		slayer_guess = int(raw_input("Guess a six-digit number 'SLAYER' so the following equation is true,"+
			"where each letter stands for the digit in the position shown: SLAYER + SLAYER + SLAYER = LAYERS"+ 
			" Enter your guess for SLAYER: : "))
	except ValueError:
		print "\nYou must input numbers\n"
		continue

	if len(str(slayer_guess)) !=6:
		print "\nEnter exactly 6 numbers.\n"
		continue
	else:
		break


slayer_string = str(slayer_guess)
slayer_sum = (3 * slayer_guess)
layers = int(slayer_string[1])*100000 + int(slayer_string[2])*10000 + int(slayer_string[3])*1000 + int(slayer_string[4])*100 + int(slayer_string[5])*10 + int(slayer_string[0])



if slayer_sum == layers:
	print "You did it!"
else:
	print "Guess again!"




#print slayer_string[3]
print "LAYERS = " + str(layers) + " and SLAYER + SLAYER + SLAYER = " + str(slayer_sum)

