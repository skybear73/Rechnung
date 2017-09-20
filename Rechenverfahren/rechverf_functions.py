import rechverf_subfunctions

def function():
	
	x = - 5
	fx = x**3 - 3*x**2 - 4*x + 7
	dif_fx = 3*x**2 - 6*x - 4

	newton = rechverf_subfunctions.newton(x, fx, dif_fx)

	print("newton = ", newton)


function()