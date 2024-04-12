# List van werkstatuut
werkstatuut=['medewerker','zelfstandige','ambtenaar']

# Nog geen recht op pensioen
def werken (leeftijd):
    if leeftijd <= 64:
        print ("Van werken word je gelukkig, je mag nog",65 - leeftijd,"jaar genieten van je baan")

# Pensioensbedrag voor de medewerker.   
def medewerker (leeftijd):    
    a = werkstatuut[0]
    if leeftijd >= 65 and leeftijd <= 69:
        print("U bent",a,"en u bent",leeftijd,"jaar oud, uw pensioenregeling bedraagt € 350,- per week.")
    elif leeftijd >= 70:
        print("U bent",a,"en u bent",leeftijd,"jaar oud, uw pensioenregeling bedraagt € 370,- per week")
    else:
        return werken(leeftijd)

# Pensioensbedrag voor de zelfstandige.    
def zelfstandige (leeftijd):
    a = werkstatuut[1]
    if leeftijd >= 65 and leeftijd <= 69:
        print("U bent",a,"en u bent",leeftijd,"jaar oud, uw pensioenregeling bedraagt € 300,- per week")
    elif leeftijd >= 70:
        print("U bent",a,"en u bent",leeftijd,"jaar oud, uw pensioenregeling bedraagt € 315,- per week")
    else:
        return werken(leeftijd)

# Pensioensbedrag voor de ambtenaar.
def ambtenaar (leeftijd):
    a = werkstatuut[2]
    if leeftijd >= 65 and leeftijd <= 69:
        print("U bent",a,"en u bent",leeftijd,"jaar oud, uw pensioenregeling bedraagt € 370,- per week")
    elif leeftijd >= 70:
        print("U bent",a,"en u bent",leeftijd,"jaar oud, uw pensioenregeling bedraagt € 395,- per week")
    else:
        return werken(leeftijd)

# Uitkomst (leeftijd invoeren naar wenst)    
medewerker (64)
zelfstandige (65)
ambtenaar (70)