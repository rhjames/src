searchphrase = raw_input("Which year would you like measles data for? ")

with open("measles.txt", "r") as f:
    searchlines = f.readlines()

for i, line in enumerate(searchlines):
    if searchphrase in line: 
        for l in searchlines[i:i+1]: print l,
        print
