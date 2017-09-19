
v = "v"
o = "o"
x = "x"
w = "Niemand"
u = 1

i = 	[x,o,o]
ii = 	[x,o,o]
iii = 	[o,x,x]
ttt = [i,ii,iii]


for v in [o,x]:
	for z in [0,1,2]:
		n1,n2,n3,n4 = 0,0,0,0
		for r in [0,1,2]:
			if ttt[z][r] == v:
				n1 = n1 + 1
			if ttt[r][z] == v:
				n2 = n2 + 1
			if ttt[r][r] == v:
				n3 = n3 + 1
			if ttt[r][2 - r] == v:
				n4 = n4 + 1
		for n in [n1,n2,n3,n4]:
			if n == 3:
				w = v
				break


print(w + " = WINNER")
print(ttt)
