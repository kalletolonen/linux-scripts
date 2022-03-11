#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import unicodedata

usrList = ["Nakke Nertola", "Håkan Värs", "Einari Mikkonen", 
"Einari Öljysaari", "Eija Vähäkäähkä"]

modList = []
usrNameList = []

i = 0
while (i < len(usrList)):
    name = unicodedata.normalize('NFD',usrList[i]).encode('ascii', 'ignore')
    cutb = str(name,"utf-8") #cuts out the b' that unicodedata produces
    modList.append(cutb.lower())
    i+=1

j = 0
while (j < len(modList)):
    full_name = modList[j]
    first_letters = full_name[:3]
    space_index = full_name.find(" ")
    three_letters_surname = full_name[space_index + 1:space_index + 4]
    number = random.randrange (1,9)
    username = (first_letters +  three_letters_surname + str(number))
    usrNameList.append(username)
    j+=1

with open ("output.txt", "w") as f:
    for n in usrNameList:
        print(n, file=f)
