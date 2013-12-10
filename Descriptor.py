# -*- coding: utf-8 -*-

#Metadata Social Event Classification: DESCRIPTOR
#Sergi Diaz, Iker Elorza, Ferran Monfort, Jordi Aguilar

import pandas as pd

meta_train = pd.read_csv('C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Metadades\sed2013_task2_dataset_train.csv', sep='\t');
tags_train = pd.read_csv('C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Metadades\sed2013_task2_dataset_train_tags.csv', sep='\t');
sol_train  = pd.read_csv('C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Metadades\sed2013_task2_dataset_train_gs.csv', sep='\t');

x = (len(tags_train)) #numero de tags
y = len(sol_train)  #numero de solucions

j = 0
cont=0

while (j < x): 
    i = cont
    str1=(tags_train.document_id[j])
    #print str1
    str2=len(tags_train.document_id[j])
    if(str1[str2-1]=='1'):
        while (i < y):
            if (tags_train.document_id[j] == sol_train.document_id[i]):
                if (sol_train.event_type[i] == 'concert'):
                    concert = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\concert_ent.txt","a")
                    concert.write(tags_train.tag[j])
                    concert.write("\n")
                    concert.close()
                elif (sol_train.event_type[i] == 'conference'):
                    conference = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\conference_ent.txt","a")
                    conference.write(tags_train.tag[j])
                    conference.write("\n")
                    conference.close()
                elif (sol_train.event_type[i] == 'exhibition'):
                    exhibition = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\exhibition_ent.txt","a")
                    exhibition.write(tags_train.tag[j])
                    exhibition.write("\n")
                    exhibition.close()
                elif (sol_train.event_type[i] == 'fashion'):
                    fashion = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\efashion_ent.txt","a")
                    fashion.write(tags_train.tag[j])
                    fashion.write("\n")
                    fashion.close()
                elif (sol_train.event_type[i] == 'non_event'):
                    non_event = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\enon_event_ent.txt","a")
                    non_event.write(tags_train.tag[j])
                    non_event.write("\n")
                    non_event.close()
                elif (sol_train.event_type[i] == 'other'):
                    other = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\other_ent.txt","a")
                    other.write(tags_train.tag[j])
                    other.write("\n")
                    other.close()
                elif (sol_train.event_type[i] == 'sports'):
                    sport = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\sport_ent.txt","a")
                    sport.write(tags_train.tag[j])
                    sport.write("\n")
                    sport.close()
                elif (sol_train.event_type[i] == 'theater_dance'):
                    theater_dance = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\etheater_dance_ent.txt","a")
                    theater_dance.write(tags_train.tag[j])
                    theater_dance.write("\n")
                    theater_dance.close()
                elif (sol_train.event_type[i] == 'protest'):
                    protest = open("C:\Users\Iker\Desktop\Q5-7\GDSA\Classificador\Fitxers_sol\protest_ent.txt","a")
                    protest.write(tags_train.tag[j])
                    protest.write("\n")
                    protest.close()
                if( j>0 and (tags_train.document_id[j] != tags_train.document_id[j-1])): # mirar si és id o type
                    cont+=1; #if diferent   
                    #print cont    
                break; 
            else: 
                i+=1;
                #print i
    j = j + 1
    #print j
