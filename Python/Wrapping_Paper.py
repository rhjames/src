data = f.read().splitlines()

def surface_area(l,w,h):
	area == (2*l*w) + (2*w*h) + (2*h*l)
	return area


def extra_wrap(l,w,h):
	if 2*l*w < 2*w*h and 2*h*l:
		return 2*l*w
	elif 2*w*h < 2*h*l and 2*l*w:
		return 2*w*h
	elif 2*h*l < 2*l*w and 2*w*h:
		return 2*h*l

surface_area(l,w,h)