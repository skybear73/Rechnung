#Newtonverfahren
def newton(x, fx, dif_fx):
	stopp = 10e-3
	dx = 0.5
	x_i = x + dx
	z = 0
	
	while dx >= stopp:
		x_i = x - fx / dif_fx
		dx = abs(x_i - x)
		x = x_i

		z = z + 1
		if z > (10**5/stopp):
			func = "ERROR NEWTON"
			break
	func = x_i
	print("z = ", z)
	print("dx = ", dx)
	print("func = ", func)
	return func

