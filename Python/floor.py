floor = 0
position = 0
final = open('Raw Text', 'r')
string = final.read()

#while floor >= 0:
for c in string:
	position += 1
	if c == "(":
		floor += 1
		#print position 
	elif c == ")":
		floor -= 1
		#print position
	if floor == -1:
		break
final.close()
print floor
print position