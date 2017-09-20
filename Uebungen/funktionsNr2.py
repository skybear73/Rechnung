def newton(x, fx, dif_fx):
	stopp = 10**(-2)
	dx = 0.5
	z = 0
	while dx >= stopp:
		x_i = x - fx/dif_fx
		dx = x_i - x
		x = x_i
		z = z + 1
		if z > 10**3:
			func = "ERROR_NEWTON"
			break	
	func = x_i
	print(func)
	return func


