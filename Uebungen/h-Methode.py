'Definition'
x = 0
x_i = 0.5
dx = x_i - x
stopp = 10**(-3)
z = 1
'Funktion'
f_x = x**3 - 3*x - 1
dif_f_x = 3*x**2 - 3

'Iterationsvorschrif'
while dx >= stopp and z < 10e5:
	z = z + 1
	print(z)
	x_i = x - f_x/dif_f_x
	x = x_i
	dx = x_i - x


'Ausgabe'
print(x)
print(dx)