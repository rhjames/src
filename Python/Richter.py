while True:
	try:
		richter_value = float(raw_input("How big on the Richter scale was the earthquake: "))
		break
	except ValueError:
		print("Enter a valid Richter value")
		continue


energy_release = 10**((1.5*richter_value)+4.8)
tnt_ton = 4.184*10**(9)

print energy_release, 'joules'
print energy_release/tnt_ton, 'Tons of TNT'