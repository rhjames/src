encode_array = []
decode_array =[]
while True:

	user_option = raw_input("Would you like to encode (e), decode (d) or quit (q)? ")

	if user_option == "e":

		encode = list(raw_input("What would you like to encode? ").lower())

		while True: 
			try:
				encode_integer = int(raw_input("What roation integer (1-26) would you like to use? "))
				if encode_integer in range(1,26):
					break
				else:
					print "Only 1-26 please"
			except ValueError:
				print "That's not an integer!"

		for x in encode:
			if x in "abcdefghijklmnopqrstuvwxyz":
				x = ord(x)
				x += encode_integer
				if x > ord("z"):
					x -= 26
				elif x < ord("a"):
					x += 26			
				x = chr(x)
				encode_array.append(x)
			else:
				encode_array.append(x)

		print ''.join(encode_array)
		encode_array = []

	elif user_option == "d":

		decode = list(raw_input("What would you like to decode? ").lower())

		while True: 
			try:
				decode_integer = int(raw_input("What roation integer would you like to decode with? "))
				if decode_integer in range(1,26):
					break
				else:
					print "Only 1-26 please"
			except ValueError:
				print "That's not an integer!"

		for x in decode:
			if x in "abcdefghijklmnopqrstuvwxyz":	
				x = ord(x)
				x -= decode_integer
				if x > ord("z"):
					x -= 26
				elif x < ord("a"):
					x += 26	
				x = chr(x)
				decode_array.append(x)
			else:
				decode_array.append(x)

		print ''.join(decode_array)
		decode_array =[]
	

	elif user_option == "q":
		print "Goodbye!"
		break


	else:
		print "Please input either e, d, or q!"




