def carg_berechnung (AK, EK, t):
    carg = ((EK/AK) ** (1/t)-1)
    AK = 100
    EK = 700
    t = 30
    return (carg)

print (carg_berechnung(100, 700, 30))

AK = 120
carg = carg_berechnung(100, 700,30)
EK = AK * (1 + carg)**t

print(EK)