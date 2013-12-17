# -*- coding: utf-8 -*-
#Metadata Social Event Classification: DESCRIPTOR
#Sergi Diaz, Iker Elorza, Ferran Monfort, Jordi Aguilar

import csv
import time
import datetime

tags_train = list(csv.reader(open('C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Sessio6\doc_classificador.csv','rb'),delimiter=' '));
sol_train  = list(csv.reader(open('C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Sessio6\doc_solucions.csv','rb'),delimiter=' '));

x = len(tags_train) #numero de tags
y = len(sol_train)  #numero de solucions

j = 0
timer=time.time()

while (j < x): 
     i = 0
     while (i < y):
        if (tags_train[j][0] == sol_train[i][0]):
            if (sol_train[i][1] == 'concert'):
                concert = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Sessio6\Fitxers_sol\concert_ent.txt","a")
                concert.write(str(tags_train[j][1]))
                concert.write("\n")
                concert.close()
            elif (sol_train[i][1] == 'conference'):
                conference = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Sessio6\Fitxers_sol\conference_ent.txt","a")
                conference.write(tags_train[j][1])
                conference.write("\n")
                conference.close()
            elif (sol_train[i][1] == 'exhibition'):
                exhibition = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Sessio6\Fitxers_sol\exhibition_ent.txt","a")
                exhibition.write(tags_train[j][1])
                exhibition.write("\n")
                exhibition.close()
            elif (sol_train[i][1] == 'fashion'):
                fashion = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Sessio6\Fitxers_sol\efashion_ent.txt","a")
                fashion.write(tags_train[j][1])
                fashion.write("\n")
                fashion.close()
            elif (sol_train[i][1] == 'non_event'):
                non_event = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Sessio6\Fitxers_sol\enon_event_ent.txt","a")
                non_event.write(tags_train[j][1])
                non_event.write("\n")
                non_event.close()
            elif (sol_train[i][1] == 'other'):
                other = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Sessio6\Fitxers_sol\other_ent.txt","a")
                other.write(tags_train[j][1])
                other.write("\n")
                other.close()
            elif (sol_train[i][1] == 'sports'):
                sport = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Sessio6\Fitxers_sol\sport_ent.txt","a")
                sport.write(tags_train[j][1])
                sport.write("\n")
                sport.close()
            elif (sol_train[i][1] == 'theater_dance'):
                theater_dance = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Sessio6\Fitxers_sol\etheater_dance_ent.txt","a")
                theater_dance.write(tags_train[j][1])
                theater_dance.write("\n")
                theater_dance.close()
            elif (sol_train[i][1] == 'protest'):
                protest = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Sessio6\Fitxers_sol\protest_ent.txt","a")
                protest.write(tags_train[j][1])
                protest.write("\n")
                protest.close() 
            break; 
        i+=1;
     j+=1;

print(str(datetime.timedelta(seconds=(time.time()-timer))))
