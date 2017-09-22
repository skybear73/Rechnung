'''
How to call functions multiple times
'''


def fleetbonus(Anz_BS, Anz_CR, Anz_FR):
	CAP_BS = 8
	CAP_CR = 40
	CAP_FR = 80
	
	BONI_TYPE = ("BS", "CR", "FR")
	BONI_MULTI = (20, 1/3, 1/3, 1, 2/100, 2/100, 1, 2, 1, 2/100, 1/3, 1, 5, 1, 1, 1/100)
	BONI_ALLO = list(range(len(BONI_MULTI)))

	for k in range (0, 2):
		if k == 0:
			for n in [3, 4, 5, 6, 7, 8, 9, 11, 14]:
				BONI_ALLO[n] = [BONI_TYPE[k], BONI_MULTI[n]]
		elif k == 1:
			for n in [0, 1 ,2 , 10, 12]:
				BONI_ALLO[n] = [BONI_TYPE[k], BONI_MULTI[n]]
		else:
			n = 15
			k = 2
			BONI_ALLO[n] = [BONI_TYPE[k], BONI_MULTI[n]]
	print (BONI_ALLO)

	for k in range (0, 15):
		while BONI_ALLO[]


	BS_AB = BONI(Anz_CR, CAP_CR, BONI_MULTI[0])
	BS_ST = BONI(Anz_CR, CAP_CR, BONI_MULTI[1])
	BS_TT = BONI(Anz_CR, CAP_CR, BONI_MULTI[2])

	CR_PT = BONI(Anz_BS, CAP_BS, BONI_MULTI[3])
	CR_PD = BONI(Anz_BS, CAP_BS, BONI_MULTI[4])
	CR_SD = BONI(Anz_BS, CAP_BS, BONI_MULTI[5])
	CR_TR = BONI(Anz_BS, CAP_BS, BONI_MULTI[6])
	CR_TT = BONI(Anz_BS, CAP_BS, BONI_MULTI[7])

	FR_PT = BONI(Anz_BS, CAP_BS, BONI_MULTI[8])
	FR_PD = BONI(Anz_BS, CAP_BS, BONI_MULTI[9])
	FR_ST = BONI(Anz_CR, CAP_CR, BONI_MULTI[10])
	FR_MA = BONI(Anz_BS, CAP_BS, BONI_MULTI[11])
	FR_AB = BONI(Anz_CR, CAP_CR, BONI_MULTI[12])

	CO_AB = BONI(Anz_CR, CAP_CR, BONI_MULTI[13])
	CO_ST = BONI(Anz_BS, CAP_BS, BONI_MULTI[14])
	CO_SB = BONI(Anz_FR, CAP_FR, BONI_MULTI[15])

	BoniList = [(BS_AB, BS_ST, BS_TT), (CR_PT, CR_PD, CR_SD, CR_TR, CR_TT), (FR_PT, FR_PD, FR_ST, FR_MA, FR_AB), (CO_AB, CO_ST, CO_SB)]
	print (BoniList)
	return BoniList

def BONI(Anz, CAP, BONI_MULTI):
	
	if Anz <= CAP:
		BONI_VALUE = Anz * BONI_MULTI
	else:
		BONI_VALUE = CAP * BONI_MULTI
	return BONI_VALUE










p = fleetbonus(6, 30, 25)
print (p)
