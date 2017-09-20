x = 1
x_i = 0
dx = x - x_i
abort = 1**-5

f_x = x**3 - 3*x - 1

dif_f_x = 0.00

while dx >= 1:
	dx = x - x_i
	f_x = x**3 - 3*x - 1
	f_x_i = x_i**3 - 3*x_i - 1
	dif_f_xi = (f_x - f_x_i) / dx
	print(dif_f_xi)

