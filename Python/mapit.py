import webbrowser, sys
from Tkinter import Tk

if len(sys.argv) >1:
	address = ''.join(sys.argv[1:])

else:
	address = Tk().clipboard_get()

webbrowser.open('https://www.google.com/maps/place/' + address)