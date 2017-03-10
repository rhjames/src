while True:
	try:
		air_temp = float(raw_input("What is the air temperature: "))
		wind_speed = float(raw_input("What is the wind speed: "))
		break
	except ValueError:
		print("Enter a valid air and wind value")
		continue
wct_index = 35.74 + 0.6215 * air_temp \
- 35.75 * wind_speed**0.16 \
 + 0.4275 * air_temp * wind_speed**0.16

print "The temperature is ",air_temp
print "The wind speed is ", wind_speed
print "The Wind Chill Temperatur Index is: ", wct_index