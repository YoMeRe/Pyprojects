# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 20:21:47 2021

@author: Yoeri
"""

import datetime

# Tranch 1 information
tr1_begin = datetime.date(2020,10,1).strftime("%d-%m-%Y")
tr1_end = datetime.date(2020,12,31).strftime("%d-%m-%Y")
tr1_min_omzetverlies = 0.2
tr1_max_compensatie = 0.8
tr1_loon_vrijstelling = 0.1
tr1_max_loonbedragPW = 9691

# Tranch 1 omzetperiode's
periode1 = [[datetime.date(2020,10,1).strftime("%d-%m-%Y"),datetime.date(2020,10,31).strftime("%d-%m-%Y")],
            [datetime.date(2020,11,1).strftime("%d-%m-%Y"),datetime.date(2020,11,30).strftime("%d-%m-%Y")],
            [datetime.date(2020,12,1).strftime("%d-%m-%Y"),datetime.date(2020,12,31).strftime("%d-%m-%Y")]]

periode2 = [[datetime.date(2020,11,1).strftime("%d-%m-%Y"),datetime.date(2020,11,30).strftime("%d-%m-%Y")],
            [datetime.date(2020,12,1).strftime("%d-%m-%Y"),datetime.date(2020,12,31).strftime("%d-%m-%Y")],
            [datetime.date(2021,1,1).strftime("%d-%m-%Y"),datetime.date(2021,1,30).strftime("%d-%m-%Y")]]

periode3 = [[datetime.date(2020,12,1).strftime("%d-%m-%Y"),datetime.date(2020,12,31).strftime("%d-%m-%Y")],
            [datetime.date(2021,1,1).strftime("%d-%m-%Y"),datetime.date(2021,1,30).strftime("%d-%m-%Y")],
            [datetime.date(2021,2,1).strftime("%d-%m-%Y"),datetime.date(2021,2,28).strftime("%d-%m-%Y")]]

# Tranch 2 information
tr2_begin = datetime.date(2021,1,1).strftime("%d-%m-%Y")
tr2_end = datetime.date(2021,3,31).strftime("%d-%m-%Y")
tr2_min_omzetverlies = 0.3
tr2_max_compensatie = 0.7
tr2_loon_vrijstelling = 0.15
tr2_max_loonbedragPW = 9691

# Tranch 2 omzetperiode's 
periode4 = [[datetime.date(2021,1,1).strftime("%d-%m-%Y"),datetime.date(2021,1,30).strftime("%d-%m-%Y")],
            [datetime.date(2021,2,1).strftime("%d-%m-%Y"),datetime.date(2021,2,28).strftime("%d-%m-%Y")],
            [datetime.date(2021,3,1).strftime("%d-%m-%Y"),datetime.date(2021,3,31).strftime("%d-%m-%Y")]]

periode5 = [[datetime.date(2021,2,1).strftime("%d-%m-%Y"),datetime.date(2021,2,28).strftime("%d-%m-%Y")],
            [datetime.date(2021,3,1).strftime("%d-%m-%Y"),datetime.date(2021,3,31).strftime("%d-%m-%Y")],
            [datetime.date(2021,4,1).strftime("%d-%m-%Y"),datetime.date(2021,4,30).strftime("%d-%m-%Y")]]

periode6 = [[datetime.date(2021,3,1).strftime("%d-%m-%Y"),datetime.date(2021,3,31).strftime("%d-%m-%Y")],
            [datetime.date(2021,4,1).strftime("%d-%m-%Y"),datetime.date(2021,4,30).strftime("%d-%m-%Y")],
            [datetime.date(2021,5,1).strftime("%d-%m-%Y"),datetime.date(2021,5,31).strftime("%d-%m-%Y")]]

# Tranch 3 information
tr3_begin = datetime.date(2021,4,1).strftime("%d-%m-%Y")
tr3_end = datetime.date(2021,6,30).strftime("%d-%m-%Y")
tr3_min_omzetverlies = 0.3
tr3_max_compensatie = 0.6
tr3_loon_vrijstelling = 0.2
tr3_max_loonbedragPW = 4845

# Tranch 3 omzetperiode's
periode7 = [[datetime.date(2021,4,1).strftime("%d-%m-%Y"),datetime.date(2021,4,30).strftime("%d-%m-%Y")],
            [datetime.date(2021,5,1).strftime("%Y-%m-%d"),datetime.date(2021,5,31).strftime("%d-%m-%Y")],
            [datetime.date(2020,6,1).strftime("%Y-%m-%d"),datetime.date(2021,6,30).strftime("%d-%m-%Y")]]

periode8 = [[datetime.date(2021,5,1).strftime("%d-%m-%Y"),datetime.date(2021,5,31).strftime("%d-%m-%Y")],
            [datetime.date(2021,6,1).strftime("%d-%m-%Y"),datetime.date(2021,6,30).strftime("%d-%m-%Y")],
            [datetime.date(2021,7,1).strftime("%d-%m-%Y"),datetime.date(2021,7,31).strftime("%d-%m-%Y")]]

periode9 = [[datetime.date(2020,6,1).strftime("%d-%m-%Y"),datetime.date(2021,6,30).strftime("%d-%m-%Y")],
            [datetime.date(2020,7,1).strftime("%Y-%m-%d"),datetime.date(2021,7,31).strftime("%d-%m-%Y")],
            [datetime.date(2020,8,1).strftime("%Y-%m-%d"),datetime.date(2021,8,30).strftime("%d-%m-%Y")]]

#################################Excecution#######################################

# Via input keuze vastleggen van de omzetperiode die de ondernemer heeft gekozen.
print('Check NOW.pdf bestand voor het corresponderende omzetperiode getal')
omzetperiode_keuze = int(input('Welke omzetperiode wilt u gebruiken? '))

if omzetperiode_keuze == 1:
    omzetperiode_keuze = periode1
elif omzetperiode_keuze == 2:
    omzetperiode_keuze = periode2
elif omzetperiode_keuze == 3:
    omzetperiode_keuze = periode3
elif omzetperiode_keuze == 4:
    omzetperiode_keuze = periode4
elif omzetperiode_keuze == 5:
    omzetperiode_keuze = periode5
elif omzetperiode_keuze == 6:
    omzetperiode_keuze = periode6
elif omzetperiode_keuze == 7:
    omzetperiode_keuze = periode7
elif omzetperiode_keuze == 8:
    omzetperiode_keuze = periode8
elif omzetperiode_keuze == 9:
    omzetperiode_keuze = periode9

# Verdere omzetgerelateerde informatie vastleggen
omzet_2019 = int(input('Wat was uw totale omzet in 2019? '))
omzet_2020_1 = input('Wat was uw omzet tussen ' + str(omzetperiode_keuze[0]) + '? ' )
omzet_2020_2 = input('Wat was uw omzet tussen ' + str(omzetperiode_keuze[1]) + '? ' )
omzet_2020_3 = input('Wat was uw omzet tussen ' + str(omzetperiode_keuze[2]) + '? ' )

# Som van opgegeven omzet uit 2020 en berekening van 25% omzet in 2019
totale_omzet_2020 = int(omzet_2020_1) + int(omzet_2020_2) + int(omzet_2020_3)
partiële_omzet_2019 = int(omzet_2019) * 0.25

# Verliespercentage berekening
omzetverschil_percentage = (int((totale_omzet_2020) - int(partiële_omzet_2019)) / int(partiële_omzet_2019)) * 100

print('Uw omzetverschil is: ' + str(omzetverschil_percentage) + '%')

# Check of ondernemer in aanmerking komt voor NOW subsidie aan de hand van omzetverliespercentage
if omzetperiode_keuze == periode1 :
    if omzetverschil_percentage <= -20 :
        print('U komt in aanmerking voor NOW subsidie')
    elif omzetverschil_percentage >-20 :
        print('U komt niet in aanmerking voor NOW subsidie')
        print('Reden: Uw omzetverlies is lager dan 20%')
elif omzetperiode_keuze == periode2 :
    if omzetverschil_percentage <= -20 :
        print('U komt in aanmerking voor NOW subsidie')
    elif omzetverschil_percentage >-20 :
        print('U komt niet in aanmerking voor NOW subsidie')
        print('Reden: Uw omzetverlies is lager dan 20%')
elif omzetperiode_keuze == periode3 :
    if omzetverschil_percentage <= -20 :
        print('U komt in aanmerking voor NOW subsidie')
    elif omzetverschil_percentage >-20 :
        print('U komt niet in aanmerking voor NOW subsidie')
        print('Reden: Uw omzetverlies is lager dan 20%')

elif omzetperiode_keuze == periode4 :
    if omzetverschil_percentage <= -30 :
        print('U komt in aanmerking voor NOW subsidie')
    elif omzetverschil_percentage >-30 :
        print('U komt niet in aanmerking voor NOW subsidie')
        print('Reden: Uw omzetverlies is lager dan 30%')
elif omzetperiode_keuze == periode5 :
    if omzetverschil_percentage <= -30 :
        print('U komt in aanmerking voor NOW subsidie')
    elif omzetverschil_percentage >-30 :
        print('U komt niet in aanmerking voor NOW subsidie')
        print('Reden: Uw omzetverlies is lager dan 30%')
elif omzetperiode_keuze == periode6 :
    if omzetverschil_percentage <= -30 :
        print('U komt in aanmerking voor NOW subsidie')
    elif omzetverschil_percentage >-30 :
        print('U komt niet in aanmerking voor NOW subsidie')
        print('Reden: Uw omzetverlies is lager dan 30%')

elif omzetperiode_keuze == periode7 :
    if omzetverschil_percentage <= -30 :
        print('U komt in aanmerking voor NOW subsidie')
    elif omzetverschil_percentage >-30 :
        print('U komt niet in aanmerking voor NOW subsidie')
        print('Reden: Uw omzetverlies is lager dan 30%')
elif omzetperiode_keuze == periode8 :
    if omzetverschil_percentage <= -30 :
        print('U komt in aanmerking voor NOW subsidie')
    elif omzetverschil_percentage >-30 :
        print('U komt niet in aanmerking voor NOW subsidie')
        print('Reden: Uw omzetverlies is lager dan 30%')
elif omzetperiode_keuze == periode9 :
    if omzetverschil_percentage <= -30 :
        print('U komt in aanmerking voor NOW subsidie')
    elif omzetverschil_percentage >-30 :
        print('U komt niet in aanmerking voor NOW subsidie')
        print('Reden: Uw omzetverlies is lager dan 30%')

# Bepalen van maximale compensatie aan de hand van gekoze periode
if omzetperiode_keuze == periode1 :
    maximale_compensatie = tr1_max_compensatie
elif omzetperiode_keuze == periode2 :
    maximale_compensatie = tr1_max_compensatie
elif omzetperiode_keuze == periode3 :
    maximale_compensatie = tr1_max_compensatie

elif omzetperiode_keuze == periode4 :
    maximale_compensatie = tr2_max_compensatie
elif omzetperiode_keuze == periode5 :
    maximale_compensatie = tr2_max_compensatie
elif omzetperiode_keuze == periode6 :
    maximale_compensatie = tr2_max_compensatie

elif omzetperiode_keuze == periode7 :
    maximale_compensatie = tr3_max_compensatie
elif omzetperiode_keuze == periode8 :
    maximale_compensatie = tr3_max_compensatie
elif omzetperiode_keuze == periode9 :
    maximale_compensatie = tr3_max_compensatie

print('Uw maximale compensatie percentage is: ' + str((maximale_compensatie) * 100) + '%')

# Vastlegging van loonsom in juni 2020
loonsom_juni_2020 = input('Hoeveel euro aan loonkosten heeft u betaalt in juni 2020? ')

NOW_subsidie = (-float((omzetverschil_percentage / 100))) * int(loonsom_juni_2020) * 3 * 1.4 * float(maximale_compensatie)
print(-float((omzetverschil_percentage / 100)))
print(loonsom_juni_2020)
print(maximale_compensatie)
print('Uw berekende NOW-Subsidie is: €' + str(NOW_subsidie))